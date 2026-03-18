#!/usr/bin/env python3
"""Add datapond metadata (_columns table and DICTIONARY.md) to the IPEDS database.

This creates a _columns data dictionary inside ipeds.duckdb and exports
DICTIONARY.md.  Idempotent — safe to re-run after rebuilds.

Usage:
    uv run python add_datapond_metadata.py
    uv run python add_datapond_metadata.py --db ipeds.duckdb

After running, re-upload the database to Hugging Face so remote users
get the updated _columns table:
    huggingface-cli upload paulgp85/ipeds-db ./ipeds.duckdb ipeds.duckdb --repo-type dataset
"""

import argparse
import sys
from pathlib import Path

import duckdb


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def has_table(con, table_name):
    return (
        con.execute(
            "SELECT COUNT(*) FROM information_schema.tables "
            "WHERE table_schema = 'main' AND table_name = ?",
            [table_name],
        ).fetchone()[0]
        > 0
    )


def get_metadata_columns(con):
    if not has_table(con, "_metadata"):
        return set()
    return {
        r[0]
        for r in con.execute(
            "SELECT column_name FROM information_schema.columns "
            "WHERE table_schema = 'main' AND table_name = '_metadata'"
        ).fetchall()
    }


def get_user_tables(con):
    return [
        r[0]
        for r in con.execute(
            "SELECT table_name FROM information_schema.tables "
            "WHERE table_schema = 'main' "
            "  AND table_name NOT IN ('_metadata', '_columns') "
            "ORDER BY table_name"
        ).fetchall()
    ]


# ---------------------------------------------------------------------------
# _metadata
# ---------------------------------------------------------------------------

SOURCE_URL = "https://nces.ed.gov/ipeds/use-the-data"
LICENSE = "Public domain"


def ensure_metadata(con):
    meta_cols = get_metadata_columns(con)

    if not has_table(con, "_metadata"):
        print("  Creating _metadata table...")
        con.execute(
            "CREATE TABLE _metadata ("
            "  table_name VARCHAR, description VARCHAR, row_count BIGINT, "
            "  column_count INTEGER, source_url VARCHAR, license VARCHAR)"
        )
        for tname in get_user_tables(con):
            rc = con.execute(f'SELECT COUNT(*) FROM "{tname}"').fetchone()[0]
            cc = con.execute(
                "SELECT COUNT(*) FROM information_schema.columns "
                "WHERE table_schema = 'main' AND table_name = ?",
                [tname],
            ).fetchone()[0]
            con.execute(
                "INSERT INTO _metadata (table_name, row_count, column_count) "
                "VALUES (?, ?, ?)",
                [tname, rc, cc],
            )

    meta_cols = get_metadata_columns(con)
    if "source_url" not in meta_cols:
        con.execute("ALTER TABLE _metadata ADD COLUMN source_url VARCHAR")
    con.execute("UPDATE _metadata SET source_url = ?", [SOURCE_URL])

    if "license" not in meta_cols:
        con.execute("ALTER TABLE _metadata ADD COLUMN license VARCHAR")
    con.execute("UPDATE _metadata SET license = ?", [LICENSE])


# ---------------------------------------------------------------------------
# _columns
# ---------------------------------------------------------------------------

# Manual join hints for well-known IPEDS columns
JOIN_HINTS = {
    "unitid": "Primary institution ID, joins across all IPEDS tables",
}


def detect_join_hints(con):
    hints = {}
    freq = con.execute(
        "SELECT column_name, COUNT(DISTINCT table_name) AS n "
        "FROM information_schema.columns "
        "WHERE table_schema = 'main' "
        "  AND table_name NOT IN ('_metadata', '_columns') "
        "GROUP BY column_name HAVING COUNT(DISTINCT table_name) >= 3 "
        "ORDER BY n DESC"
    ).fetchall()
    for col, n in freq:
        hints[col] = f"Appears in {n} tables, common join key"

    id_cols = con.execute(
        "SELECT DISTINCT column_name "
        "FROM information_schema.columns "
        "WHERE table_schema = 'main' "
        "  AND table_name NOT IN ('_metadata', '_columns') "
        "  AND (column_name LIKE '%\\_id' ESCAPE '\\' OR column_name = 'id')"
    ).fetchall()
    for (col,) in id_cols:
        if col not in hints:
            hints[col] = "Likely primary or foreign key"

    # Override with manual hints
    hints.update(JOIN_HINTS)
    return hints


def build_columns_table(con):
    con.execute("DROP TABLE IF EXISTS _columns")
    con.execute(
        "CREATE TABLE _columns AS "
        "SELECT c.table_name, c.column_name, c.data_type, "
        "  NULL::VARCHAR AS source_file "
        "FROM information_schema.columns c "
        "WHERE c.table_schema = 'main' "
        "  AND c.table_name NOT IN ('_metadata', '_columns')"
    )
    con.execute("ALTER TABLE _columns ADD COLUMN example_value VARCHAR")
    con.execute("ALTER TABLE _columns ADD COLUMN join_hint VARCHAR")
    con.execute("ALTER TABLE _columns ADD COLUMN null_pct DOUBLE")

    hints = detect_join_hints(con)
    for col, hint in hints.items():
        con.execute(
            "UPDATE _columns SET join_hint = ? WHERE column_name = ?",
            [hint, col],
        )
    print(f"  {len(hints)} join hints applied")

    rows = con.execute(
        "SELECT table_name, column_name FROM _columns"
    ).fetchall()
    total = len(rows)

    for i, (table_name, column_name) in enumerate(rows):
        if (i + 1) % 500 == 0 or i + 1 == total:
            print(f"  Enriching columns: {i + 1}/{total}", end="\r", flush=True)

        try:
            result = con.execute(
                f'SELECT CAST("{column_name}" AS VARCHAR) '
                f'FROM "{table_name}" '
                f'WHERE "{column_name}" IS NOT NULL LIMIT 1'
            ).fetchone()
            if result and result[0] is not None:
                val = result[0].replace("\x00", "")
                if len(val) > 80:
                    val = val[:77] + "..."
                con.execute(
                    "UPDATE _columns SET example_value = ? "
                    "WHERE table_name = ? AND column_name = ?",
                    [val, table_name, column_name],
                )
        except Exception:
            pass

        try:
            result = con.execute(
                f'SELECT ROUND(100.0 * COUNT(*) FILTER '
                f'(WHERE "{column_name}" IS NULL) / COUNT(*), 1) '
                f'FROM "{table_name}"'
            ).fetchone()
            if result and result[0] is not None:
                con.execute(
                    "UPDATE _columns SET null_pct = ? "
                    "WHERE table_name = ? AND column_name = ?",
                    [result[0], table_name, column_name],
                )
        except Exception:
            pass

    print()
    col_count = con.execute("SELECT COUNT(*) FROM _columns").fetchone()[0]
    hint_count = con.execute(
        "SELECT COUNT(*) FROM _columns WHERE join_hint IS NOT NULL"
    ).fetchone()[0]
    print(f"  {col_count} columns cataloged, {hint_count} with join hints")


# ---------------------------------------------------------------------------
# DICTIONARY.md
# ---------------------------------------------------------------------------


def export_dictionary(con, output_path):
    meta_cols = get_metadata_columns(con)
    lines = ["# Data Dictionary", ""]

    if "source_url" in meta_cols:
        url = con.execute(
            "SELECT source_url FROM _metadata WHERE source_url IS NOT NULL LIMIT 1"
        ).fetchone()
        if url:
            lines.append(f"Source: [{url[0]}]({url[0]})")
            lines.append("")

    tables = con.execute(
        "SELECT DISTINCT table_name FROM _columns ORDER BY table_name"
    ).fetchall()

    for (table_name,) in tables:
        lines.append(f"## {table_name}")
        lines.append("")

        if has_table(con, "_metadata"):
            select_parts = []
            if "row_count" in meta_cols:
                select_parts.append("row_count")
            if "description" in meta_cols:
                select_parts.append("description")
            if select_parts:
                meta = con.execute(
                    f"SELECT {', '.join(select_parts)} FROM _metadata "
                    f"WHERE table_name = ?",
                    [table_name],
                ).fetchone()
                if meta:
                    if "description" in meta_cols:
                        desc = meta[select_parts.index("description")]
                        if desc:
                            lines.append(desc)
                            lines.append("")
                    if "row_count" in meta_cols:
                        rc = meta[select_parts.index("row_count")]
                        if rc:
                            lines.append(f"Rows: {rc:,}")
                    lines.append("")

        lines.append("| Column | Type | Nulls | Example | Join |")
        lines.append("|--------|------|-------|---------|------|")

        cols = con.execute(
            "SELECT column_name, data_type, null_pct, example_value, join_hint "
            "FROM _columns WHERE table_name = ? ORDER BY rowid",
            [table_name],
        ).fetchall()

        for col_name, dtype, null_pct, example, join_hint in cols:
            null_str = f"{null_pct:.1f}%" if null_pct is not None else ""
            example_str = (example or "").replace("|", "\\|")
            join_str = join_hint or ""
            lines.append(
                f"| {col_name} | {dtype} | {null_str} | {example_str} | {join_str} |"
            )

        lines.append("")

    content = "\n".join(lines)
    content = content.replace("\x00", "")

    with open(output_path, "w") as f:
        f.write(content)
    print(f"  Exported {output_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="Add _columns and DICTIONARY.md to the IPEDS database"
    )
    parser.add_argument("--db", type=Path, default=Path("ipeds.duckdb"))
    args = parser.parse_args()

    if not args.db.exists():
        print(f"Error: {args.db} not found. Run build_database.py first.")
        sys.exit(1)

    print(f"Opening {args.db}")
    con = duckdb.connect(str(args.db))

    print("\n[1/3] Ensuring _metadata")
    ensure_metadata(con)

    print("\n[2/3] Building _columns")
    build_columns_table(con)

    print("\n[3/3] Exporting DICTIONARY.md")
    export_dictionary(con, args.db.parent / "DICTIONARY.md")

    total_rows = con.execute("SELECT SUM(row_count) FROM _metadata").fetchone()[0]
    n_tables = con.execute("SELECT COUNT(*) FROM _metadata").fetchone()[0]
    n_cols = con.execute("SELECT COUNT(*) FROM _columns").fetchone()[0]
    print(f"\nDone. {n_tables} tables, {total_rows:,} total rows, {n_cols} columns")
    print("\nTo update the remote database on Hugging Face:")
    print("  huggingface-cli upload paulgp85/ipeds-db ./ipeds.duckdb ipeds.duckdb --repo-type dataset")

    con.close()


if __name__ == "__main__":
    main()
