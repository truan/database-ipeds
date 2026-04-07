# database-ipeds — Project Instructions

## What This Repo Is

A forked ETL pipeline that builds a unified DuckDB database from 20+ years of IPEDS (Integrated Postsecondary Education Data System) data. Not a research project — a data utility for US higher education data. Used as a reference/control dataset for research.

**Upstream repo:** [paulgp/ipeds-database](https://github.com/paulgp/ipeds-database)
**This fork:** [truan/database-ipeds](https://github.com/truan/database-ipeds)

---

## Current Work and Write Access

Write access for the GitHub repo:
- **Editable:** `build_database.py`, `add_datapond_metadata.py`, `examples/` — scripts and examples
- **Read-only:** `~/ipeds/raw/` — cached NCES downloads (~720 MB, outside repo, do not modify)
- **Read-only:** `~/ipeds/ipeds.duckdb` — output database (~1.1 GB, outside repo); rebuild with `uv run python build_database.py`

Do not change files in any Dropbox folders unless explicitly allowed to do so.

---

## Project Structure

```
database-ipeds/               # GitHub repo
├── build_database.py          # Main ETL pipeline (~1,050 lines) — downloads, harmonizes, loads
├── add_datapond_metadata.py   # Generates _metadata table and DICTIONARY.md
├── DICTIONARY.md              # Auto-generated column-level data dictionary (189 KB)
├── pyproject.toml             # Dependencies: duckdb, pandas, requests, beautifulsoup4, lxml
└── examples/
    ├── query_examples.sql     # 11 example SQL queries
    └── figures/               # R scripts (ggplot2) and pre-generated PNGs

~/ipeds/                      # Data directory (outside repo, not committed)
├── raw/                       # Cached NCES ZIP files (~720 MB)
├── logs/                      # Timestamped build logs
└── ipeds.duckdb               # Output DuckDB database (~1.1 GB)
```

## Output Database

`ipeds.duckdb` — 27 million rows across 23 tables, 1997–2024. Key tables:

| Table | Content |
|-------|---------|
| `hd` | Institutional directory (name, location, sector, Carnegie classification) |
| `adm` | Admissions: applicants, admits, enrolled, SAT/ACT scores (2014–2023) |
| `ef_a` | Fall enrollment by race/ethnicity and gender |
| `c_a` | Completions by CIP code, race, gender, award level |
| `sfa` | Student financial aid, grants, loans, net price |
| `f1a` / `f2` / `f3` | Finance: public (GASB) / private nonprofit (FASB) / for-profit |
| `gr` | Graduation rates |
| `_metadata` | Machine-readable inventory of all tables |

Every table has `unitid` (institution ID) and `year` for joining.

## Usage

```bash
uv sync
uv run python build_database.py        # full build
uv run python build_database.py hd adm # rebuild specific tables only
```

API key / credentials: none needed (all data from public NCES servers).

---

## Team Members

| Person | Role |
|--------|------|
| Tianyue | Fork maintainer |
| Paul Goldsmith-Pinkham | Upstream author |
