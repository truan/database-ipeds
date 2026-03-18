# Data Dictionary

Source: https://nces.ed.gov/ipeds/use-the-data

## adm

Rows: 20,571

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| admcon1 | BIGINT | 0.0% | 1 |  |
| admcon2 | BIGINT | 0.0% | 3 |  |
| admcon3 | BIGINT | 0.0% | 1 |  |
| admcon4 | BIGINT | 0.0% | 3 |  |
| admcon5 | BIGINT | 0.0% | 3 |  |
| admcon6 | BIGINT | 0.0% | 3 |  |
| admcon7 | BIGINT | 0.0% | 5 |  |
| admcon8 | BIGINT | 0.0% | 1 |  |
| admcon9 | BIGINT | 0.0% | 3 |  |
| admcon10 | DOUBLE | 80.7% | 3.0 |  |
| admcon11 | DOUBLE | 80.7% | 3.0 |  |
| admcon12 | DOUBLE | 80.7% | 3.0 |  |
| xapplcn | VARCHAR | 0.0% | R |  |
| applicants_total | BIGINT | 0.0% | 15628 |  |
| xapplcnm | VARCHAR | 0.0% | R |  |
| applicants_men | DOUBLE | 0.0% | 5247.0 |  |
| xapplcnw | VARCHAR | 0.0% | R |  |
| applicants_women | DOUBLE | 0.0% | 10381.0 |  |
| xapplcnan | VARCHAR | 80.7% | A |  |
| applcnan | DOUBLE | 94.2% | 0.0 |  |
| xapplcnun | VARCHAR | 80.7% | R |  |
| applcnun | DOUBLE | 82.9% | 0.0 |  |
| xadmssn | VARCHAR | 0.0% | R |  |
| admissions_total | DOUBLE | 1.0% | 10349.0 |  |
| xadmssnm | VARCHAR | 0.0% | R |  |
| admissions_men | DOUBLE | 4.5% | 3409.0 |  |
| xadmssnw | VARCHAR | 0.0% | R |  |
| admissions_women | DOUBLE | 4.9% | 6940.0 |  |
| xadmssnan | VARCHAR | 80.7% | A |  |
| admssnan | DOUBLE | 97.4% | 53.0 |  |
| xadmssnun | VARCHAR | 80.7% | R |  |
| admssnun | DOUBLE | 82.9% | 0.0 |  |
| xenrlt | VARCHAR | 0.0% | R |  |
| enrolled_total | DOUBLE | 1.2% | 1956.0 |  |
| xenrlm | VARCHAR | 0.0% | R |  |
| enrolled_men | DOUBLE | 5.2% | 799.0 |  |
| xenrlw | VARCHAR | 0.0% | R |  |
| enrolled_women | DOUBLE | 5.2% | 1157.0 |  |
| xenrlan | VARCHAR | 80.7% | A |  |
| enrlan | DOUBLE | 97.7% | 15.0 |  |
| xenrlun | VARCHAR | 80.7% | R |  |
| enrlun | DOUBLE | 82.9% | 0.0 |  |
| xenrlft | VARCHAR | 0.0% | R |  |
| enrlft | DOUBLE | 1.7% | 1944.0 |  |
| xenrlftm | VARCHAR | 0.0% | R |  |
| enrlftm | DOUBLE | 6.3% | 793.0 |  |
| xenrlftw | VARCHAR | 0.0% | R |  |
| enrlftw | DOUBLE | 5.9% | 1151.0 |  |
| xenrlftan | VARCHAR | 80.7% | A |  |
| enrlftan | DOUBLE | 98.6% | 15.0 |  |
| xenrlftun | VARCHAR | 80.7% | R |  |
| enrlftun | DOUBLE | 82.9% | 0.0 |  |
| xenrlpt | VARCHAR | 0.0% | R |  |
| enrlpt | DOUBLE | 25.0% | 12.0 |  |
| xenrlptm | VARCHAR | 0.0% | R |  |
| enrlptm | DOUBLE | 27.7% | 6.0 |  |
| xenrlptw | VARCHAR | 0.0% | R |  |
| enrlptw | DOUBLE | 25.6% | 6.0 |  |
| xenrlptan | VARCHAR | 80.7% | A |  |
| enrlptan | DOUBLE | 98.9% | 0.0 |  |
| xenrlptun | VARCHAR | 80.7% | R |  |
| enrlptun | DOUBLE | 87.0% | 0.0 |  |
| xsatnum | VARCHAR | 0.0% | R |  |
| satnum | DOUBLE | 39.1% | 462.0 |  |
| xsatpct | VARCHAR | 0.0% | R |  |
| satpct | DOUBLE | 39.3% | 24.0 |  |
| xactnum | VARCHAR | 0.0% | R |  |
| actnum | DOUBLE | 39.1% | 1312.0 |  |
| xactpct | VARCHAR | 0.0% | R |  |
| actpct | DOUBLE | 39.2% | 67.0 |  |
| xsatvr25 | VARCHAR | 0.0% | R |  |
| sat_verbal_25th | DOUBLE | 44.5% | 420.0 |  |
| xsatvr50 | VARCHAR | 80.7% | R |  |
| satvr50 | DOUBLE | 90.3% | 480.0 |  |
| xsatvr75 | VARCHAR | 0.0% | R |  |
| sat_verbal_75th | DOUBLE | 44.5% | 540.0 |  |
| xsatmt25 | VARCHAR | 0.0% | R |  |
| sat_math_25th | DOUBLE | 44.4% | 390.0 |  |
| xsatmt50 | VARCHAR | 80.7% | R |  |
| satmt50 | DOUBLE | 90.3% | 460.0 |  |
| xsatmt75 | VARCHAR | 0.0% | R |  |
| sat_math_75th | DOUBLE | 44.4% | 520.0 |  |
| xactcm25 | VARCHAR | 0.0% | R |  |
| act_composite_25th | DOUBLE | 43.1% | 14.0 |  |
| xactcm50 | VARCHAR | 80.7% | R |  |
| actcm50 | DOUBLE | 90.4% | 17.0 |  |
| xactcm75 | VARCHAR | 0.0% | R |  |
| act_composite_75th | DOUBLE | 43.1% | 19.0 |  |
| xacten25 | VARCHAR | 0.0% | R |  |
| act_english_25th | DOUBLE | 47.3% | 13.0 |  |
| xacten50 | VARCHAR | 80.7% | R |  |
| acten50 | DOUBLE | 91.0% | 15.0 |  |
| xacten75 | VARCHAR | 0.0% | R |  |
| act_english_75th | DOUBLE | 47.3% | 20.0 |  |
| xactmt25 | VARCHAR | 0.0% | R |  |
| act_math_25th | DOUBLE | 47.2% | 14.0 |  |
| xactmt50 | VARCHAR | 80.7% | R |  |
| actmt50 | DOUBLE | 90.9% | 16.0 |  |
| xactmt75 | VARCHAR | 0.0% | R |  |
| act_math_75th | DOUBLE | 47.2% | 17.0 |  |
| year | BIGINT | 0.0% | 2023 | Appears in 26 tables, common join key |
| xsatwr25 | VARCHAR | 78.4% | R |  |
| sat_writing_25th | DOUBLE | 92.8% | 370.0 |  |
| xsatwr75 | VARCHAR | 78.4% | R |  |
| sat_writing_75th | DOUBLE | 92.8% | 457.0 |  |
| xactwr25 | VARCHAR | 78.4% | A |  |
| act_writing_25th | DOUBLE | 96.9% | 7.0 |  |
| xactwr75 | VARCHAR | 78.4% | A |  |
| act_writing_75th | DOUBLE | 96.9% | 8.0 |  |

## al

Rows: 39,423

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| lexp100k | DOUBLE | 52.3% | 1.0 |  |
| lcolelyn | BIGINT | 0.0% | 2 |  |
| xlpbooks | VARCHAR | 0.0% | R |  |
| lpbooks | DOUBLE | 4.0% | 367454.0 |  |
| xlebooks | VARCHAR | 0.0% | R |  |
| lebooks | BIGINT | 0.0% | 228749 |  |
| xledatab | VARCHAR | 0.0% | R |  |
| ledatab | BIGINT | 0.0% | 107 |  |
| xlpmedia | VARCHAR | 0.0% | R |  |
| lpmedia | DOUBLE | 4.0% | 26186.0 |  |
| xlemedia | VARCHAR | 0.0% | R |  |
| lemedia | BIGINT | 0.0% | 38684 |  |
| xlpseria | VARCHAR | 21.7% | R |  |
| lpseria | DOUBLE | 25.1% | 1392.0 |  |
| xleseria | VARCHAR | 21.7% | R |  |
| leseria | DOUBLE | 21.7% | 132597.0 |  |
| xlpcollc | VARCHAR | 0.0% | R |  |
| lpcllct | DOUBLE | 4.0% | 395032.0 |  |
| xlecollc | VARCHAR | 0.0% | R |  |
| lecllct | BIGINT | 0.0% | 400137 |  |
| xltcllct | VARCHAR | 10.8% | R |  |
| ltcllct | DOUBLE | 10.8% | 795169.0 |  |
| xlpcrclt | VARCHAR | 0.0% | R |  |
| lpcrclt | DOUBLE | 4.0% | 544.0 |  |
| xlecrclt | VARCHAR | 0.0% | R |  |
| lecrclt | BIGINT | 0.0% | 134785 |  |
| xltcrclt | VARCHAR | 10.8% | R |  |
| ltcrclt | DOUBLE | 10.8% | 135329.0 |  |
| lilldyn | DOUBLE | 21.7% | 1.0 |  |
| xlilldpr | VARCHAR | 0.0% | R |  |
| lilldpr | DOUBLE | 23.8% | 1836.0 |  |
| xlilldrc | VARCHAR | 0.0% | R |  |
| lilldrc | DOUBLE | 23.8% | 258.0 |  |
| lilsyn | DOUBLE | 62.0% | 1.0 |  |
| xlstotal | VARCHAR | 62.0% | R |  |
| lstotal | DOUBLE | 64.5% | 26.0 |  |
| xlslibrn | VARCHAR | 62.0% | R |  |
| lslibrn | DOUBLE | 64.5% | 9.0 |  |
| xlsoprof | VARCHAR | 62.0% | R |  |
| lsoprof | DOUBLE | 64.5% | 5.0 |  |
| xlsopaid | VARCHAR | 62.0% | R |  |
| lsopaid | DOUBLE | 64.5% | 1.0 |  |
| xlsstast | VARCHAR | 62.0% | R |  |
| lsstast | DOUBLE | 64.5% | 11.0 |  |
| xlbranch | VARCHAR | 0.0% | R |  |
| lbranch | DOUBLE | 26.1% | 0.0 |  |
| xsalwag | VARCHAR | 0.0% | R |  |
| lsalwag | DOUBLE | 26.1% | 895925.0 |  |
| lfrngbyn | BIGINT | 0.0% | 1 |  |
| xlfrngbn | VARCHAR | 0.0% | R |  |
| lfrngbn | DOUBLE | 26.1% | 287779.0 |  |
| xlexmsbb | VARCHAR | 0.0% | R |  |
| lexmsbb | DOUBLE | 26.1% | 29577.0 |  |
| xlexmscs | VARCHAR | 0.0% | R |  |
| lexmscs | DOUBLE | 26.1% | 425257.0 |  |
| xlexmsot | VARCHAR | 0.0% | R |  |
| lexmsot | DOUBLE | 26.1% | 309946.0 |  |
| xlexmstl | VARCHAR | 0.0% | R |  |
| lexmstl | DOUBLE | 26.1% | 764780.0 |  |
| xlexomps | VARCHAR | 0.0% | R |  |
| lexomps | DOUBLE | 26.1% | 17280.0 |  |
| xlexomot | VARCHAR | 0.0% | R |  |
| lexomot | DOUBLE | 26.1% | 741184.0 |  |
| xlexomtl | VARCHAR | 0.0% | R |  |
| lexomtl | DOUBLE | 26.1% | 758464.0 |  |
| xlexptot | VARCHAR | 0.0% | R |  |
| lexptot | DOUBLE | 26.1% | 2706948.0 |  |
| lswmsom | VARCHAR | 0.0% | 2419169 |  |
| year | BIGINT | 0.0% | 2023 | Appears in 26 tables, common join key |
| lsuppvrs | DOUBLE | 78.3% | 1.0 |  |

## c_a

Rows: 6,581,665

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| cipcode | DOUBLE | 0.0% | 1.0999 |  |
| major_number | DOUBLE | 2.6% | 1.0 |  |
| award_level | BIGINT | 0.0% | 5 |  |
| xctotalt | VARCHAR | 26.0% | R |  |
| ctotalt | DOUBLE | 26.0% | 12.0 |  |
| xctotalm | VARCHAR | 26.0% | R |  |
| ctotalm | DOUBLE | 26.0% | 2.0 |  |
| xctotalw | VARCHAR | 26.0% | R |  |
| ctotalw | DOUBLE | 26.0% | 10.0 |  |
| xcaiant | VARCHAR | 26.0% | Z |  |
| caiant | DOUBLE | 33.9% | 0.0 |  |
| xcaianm | VARCHAR | 26.0% | Z |  |
| caianm | DOUBLE | 33.9% | 0.0 |  |
| xcaianw | VARCHAR | 26.0% | Z |  |
| caianw | DOUBLE | 33.9% | 0.0 |  |
| xcasiat | VARCHAR | 26.0% | Z |  |
| casiat | DOUBLE | 33.9% | 0.0 |  |
| xcasiam | VARCHAR | 26.0% | Z |  |
| casiam | DOUBLE | 33.9% | 0.0 |  |
| xcasiaw | VARCHAR | 26.0% | Z |  |
| casiaw | DOUBLE | 33.9% | 0.0 |  |
| xcbkaat | VARCHAR | 26.0% | R |  |
| cbkaat | DOUBLE | 33.9% | 10.0 |  |
| xcbkaam | VARCHAR | 26.0% | R |  |
| cbkaam | DOUBLE | 33.9% | 2.0 |  |
| xcbkaaw | VARCHAR | 26.0% | R |  |
| cbkaaw | DOUBLE | 33.9% | 8.0 |  |
| xchispt | VARCHAR | 26.0% | R |  |
| chispt | DOUBLE | 33.9% | 1.0 |  |
| xchispm | VARCHAR | 26.0% | Z |  |
| chispm | DOUBLE | 33.9% | 0.0 |  |
| xchispw | VARCHAR | 26.0% | R |  |
| chispw | DOUBLE | 33.9% | 1.0 |  |
| xcnhpit | VARCHAR | 26.0% | Z |  |
| cnhpit | DOUBLE | 33.9% | 0.0 |  |
| xcnhpim | VARCHAR | 26.0% | Z |  |
| cnhpim | DOUBLE | 33.9% | 0.0 |  |
| xcnhpiw | VARCHAR | 26.0% | Z |  |
| cnhpiw | DOUBLE | 33.9% | 0.0 |  |
| xcwhitt | VARCHAR | 26.0% | Z |  |
| cwhitt | DOUBLE | 33.9% | 0.0 |  |
| xcwhitm | VARCHAR | 26.0% | Z |  |
| cwhitm | DOUBLE | 33.9% | 0.0 |  |
| xcwhitw | VARCHAR | 26.0% | Z |  |
| cwhitw | DOUBLE | 33.9% | 0.0 |  |
| xc2mort | VARCHAR | 26.0% | R |  |
| c2mort | DOUBLE | 33.9% | 1.0 |  |
| xc2morm | VARCHAR | 26.0% | Z |  |
| c2morm | DOUBLE | 33.9% | 0.0 |  |
| xc2morw | VARCHAR | 26.0% | R |  |
| c2morw | DOUBLE | 33.9% | 1.0 |  |
| xcunknt | VARCHAR | 26.0% | Z |  |
| cunknt | DOUBLE | 26.0% | 0.0 |  |
| xcunknm | VARCHAR | 26.0% | Z |  |
| cunknm | DOUBLE | 26.0% | 0.0 |  |
| xcunknw | VARCHAR | 26.0% | Z |  |
| cunknw | DOUBLE | 26.0% | 0.0 |  |
| xcnralt | VARCHAR | 26.0% | Z |  |
| cnralt | DOUBLE | 26.0% | 0.0 |  |
| xcnralm | VARCHAR | 26.0% | Z |  |
| cnralm | DOUBLE | 26.0% | 0.0 |  |
| xcnralw | VARCHAR | 26.0% | Z |  |
| cnralw | DOUBLE | 26.0% | 0.0 |  |
| year | BIGINT | 0.0% | 2024 | Appears in 26 tables, common join key |
| cdistedp | DOUBLE | 95.9% | 2.0 |  |
| xcrace03 | VARCHAR | 62.4% | R |  |
| crace03 | DOUBLE | 65.7% | 3.0 |  |
| xcrace04 | VARCHAR | 62.4% | R |  |
| crace04 | DOUBLE | 65.7% | 3.0 |  |
| xcrace05 | VARCHAR | 62.4% | R |  |
| crace05 | DOUBLE | 65.7% | 0.0 |  |
| xcrace06 | VARCHAR | 62.4% | R |  |
| crace06 | DOUBLE | 65.7% | 0.0 |  |
| xcrace07 | VARCHAR | 62.4% | R |  |
| crace07 | DOUBLE | 65.7% | 0.0 |  |
| xcrace08 | VARCHAR | 62.4% | R |  |
| crace08 | DOUBLE | 65.7% | 2.0 |  |
| xcrace09 | VARCHAR | 62.4% | R |  |
| crace09 | DOUBLE | 65.7% | 0.0 |  |
| xcrace10 | VARCHAR | 62.4% | R |  |
| crace10 | DOUBLE | 65.7% | 0.0 |  |
| xcrace11 | VARCHAR | 62.4% | R |  |
| crace11 | DOUBLE | 65.7% | 31.0 |  |
| xcrace12 | VARCHAR | 62.4% | R |  |
| crace12 | DOUBLE | 65.7% | 16.0 |  |
| xcrace18 | VARCHAR | 67.9% | R |  |
| crace18 | DOUBLE | 71.3% | 6.0 |  |
| xcrace19 | VARCHAR | 67.9% | R |  |
| crace19 | DOUBLE | 71.3% | 0.0 |  |
| xcrace20 | VARCHAR | 67.9% | R |  |
| crace20 | DOUBLE | 71.3% | 2.0 |  |
| xcrace21 | VARCHAR | 67.9% | R |  |
| crace21 | DOUBLE | 71.3% | 0.0 |  |
| xcrace22 | VARCHAR | 67.9% | R |  |
| crace22 | DOUBLE | 71.3% | 47.0 |  |
| xdvcait | VARCHAR | 88.3% | R |  |
| dvcait | DOUBLE | 88.3% | 0.0 |  |
| xdvcaim | VARCHAR | 88.3% | R |  |
| dvcaim | DOUBLE | 88.3% | 0.0 |  |
| xdvcaiw | VARCHAR | 88.3% | R |  |
| dvcaiw | DOUBLE | 88.3% | 0.0 |  |
| xdvcapt | VARCHAR | 88.3% | R |  |
| dvcapt | DOUBLE | 88.3% | 2.0 |  |
| xdvcapm | VARCHAR | 88.3% | R |  |
| dvcapm | DOUBLE | 88.3% | 0.0 |  |
| xdvcapw | VARCHAR | 88.3% | R |  |
| dvcapw | DOUBLE | 88.3% | 2.0 |  |
| xdvcbkt | VARCHAR | 88.3% | R |  |
| dvcbkt | DOUBLE | 88.3% | 6.0 |  |
| xdvcbkm | VARCHAR | 88.3% | R |  |
| dvcbkm | DOUBLE | 88.3% | 3.0 |  |
| xdvcbkw | VARCHAR | 88.3% | R |  |
| dvcbkw | DOUBLE | 88.3% | 3.0 |  |
| xdvchst | VARCHAR | 88.3% | R |  |
| dvchst | DOUBLE | 88.3% | 0.0 |  |
| xdvchsm | VARCHAR | 88.3% | R |  |
| dvchsm | DOUBLE | 88.3% | 0.0 |  |
| xdvchsw | VARCHAR | 88.3% | R |  |
| dvchsw | DOUBLE | 88.3% | 0.0 |  |
| xdvcwht | VARCHAR | 88.3% | R |  |
| dvcwht | DOUBLE | 88.3% | 47.0 |  |
| xdvcwhm | VARCHAR | 88.3% | R |  |
| dvcwhm | DOUBLE | 88.3% | 31.0 |  |
| xdvcwhw | VARCHAR | 88.3% | R |  |
| dvcwhw | DOUBLE | 88.3% | 16.0 |  |
| xcrace01 | VARCHAR | 74.0% | R |  |
| crace01 | DOUBLE | 74.0% | 0.0 |  |
| xcrace02 | VARCHAR | 74.0% | R |  |
| crace02 | DOUBLE | 74.0% | 0.0 |  |
| xcrace13 | VARCHAR | 74.0% | R |  |
| crace13 | DOUBLE | 74.0% | 1.0 |  |
| xcrace14 | VARCHAR | 74.0% | R |  |
| crace14 | DOUBLE | 74.0% | 2.0 |  |
| xcrace15 | VARCHAR | 74.0% | R |  |
| crace15 | DOUBLE | 74.0% | 21.0 |  |
| xcrace16 | VARCHAR | 74.0% | R |  |
| crace16 | DOUBLE | 74.0% | 23.0 |  |
| xcrace17 | VARCHAR | 79.6% | R |  |
| crace17 | DOUBLE | 79.6% | 0.0 |  |
| xcrace23 | VARCHAR | 79.6% | R |  |
| crace23 | DOUBLE | 79.6% | 3.0 |  |
| xcrace24 | VARCHAR | 79.6% | R |  |
| crace24 | DOUBLE | 79.6% | 44.0 |  |

## eap

Rows: 8,714,580

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| eapcat | DOUBLE | 57.7% | 10000.0 |  |
| occupcat | DOUBLE | 57.7% | 100.0 |  |
| facstat | DOUBLE | 57.7% | 0.0 |  |
| xeaptot | VARCHAR | 0.5% | R |  |
| eaptot | DOUBLE | 0.5% | 1008.0 |  |
| xeaptyp | VARCHAR | 0.5% | R |  |
| eaptyp | DOUBLE | 0.6% | 1008.0 |  |
| xeapmed | VARCHAR | 0.5% | A |  |
| eapmed | DOUBLE | 40.7% | 5288.0 |  |
| xeapft | VARCHAR | 57.7% | R |  |
| eapft | DOUBLE | 58.0% | 772.0 |  |
| xeapftty | VARCHAR | 57.7% | R |  |
| eapfttyp | DOUBLE | 58.2% | 772.0 |  |
| xeapftmd | VARCHAR | 57.7% | A |  |
| eapftmed | DOUBLE | 97.9% | 4814.0 |  |
| xeappt | VARCHAR | 57.7% | R |  |
| eappt | DOUBLE | 60.5% | 236.0 |  |
| xeapptty | VARCHAR | 57.7% | R |  |
| eappttyp | DOUBLE | 60.6% | 236.0 |  |
| xeapptmd | VARCHAR | 57.7% | A |  |
| eapptmed | DOUBLE | 98.0% | 474.0 |  |
| year | BIGINT | 0.0% | 2023 | Appears in 26 tables, common join key |
| eaprectp | DOUBLE | 42.8% | 1100.0 |  |
| ftpt | DOUBLE | 42.8% | 1.0 |  |
| functcd | DOUBLE | 42.3% | 10.0 |  |
| fstat | DOUBLE | 42.8% | 0.0 |  |
| typecd | DOUBLE | 99.5% | 1.0 |  |
| xfstat1 | VARCHAR | 99.5% | R |  |
| fstat1 | DOUBLE | 99.5% | 93.0 |  |
| xfstat2 | VARCHAR | 99.5% | R |  |
| fstat2 | DOUBLE | 99.5% | 56.0 |  |
| xfstat3 | VARCHAR | 99.5% | R |  |
| fstat3 | DOUBLE | 99.5% | 68.0 |  |
| xfstat4 | VARCHAR | 99.5% | Z |  |
| fstat4 | DOUBLE | 99.5% | 0.0 |  |
| xfstat5 | VARCHAR | 99.5% | R |  |
| fstat5 | DOUBLE | 99.5% | 217.0 |  |
| xfstat6 | VARCHAR | 99.5% | A |  |
| fstat6 | DOUBLE | 99.5% | 0.0 |  |

## ef_a

Rows: 2,830,464

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| efalevel | DOUBLE | 4.2% | 1.0 |  |
| line | BIGINT | 0.0% | 29 | Appears in 4 tables, common join key |
| section | BIGINT | 0.0% | 3 | Appears in 3 tables, common join key |
| lstudy | BIGINT | 0.0% | 4 | Appears in 3 tables, common join key |
| xeftotlt | VARCHAR | 26.9% | R |  |
| eftotlt | DOUBLE | 26.9% | 6614.0 |  |
| xeftotlm | VARCHAR | 26.9% | R |  |
| eftotlm | DOUBLE | 26.9% | 2671.0 |  |
| xeftotlw | VARCHAR | 26.9% | R |  |
| eftotlw | DOUBLE | 26.9% | 3943.0 |  |
| xefaiant | VARCHAR | 26.9% | R |  |
| efaiant | DOUBLE | 32.9% | 9.0 |  |
| xefaianm | VARCHAR | 26.9% | R |  |
| efaianm | DOUBLE | 32.9% | 5.0 |  |
| xefaianw | VARCHAR | 26.9% | R |  |
| efaianw | DOUBLE | 32.9% | 4.0 |  |
| xefasiat | VARCHAR | 26.9% | R |  |
| efasiat | DOUBLE | 32.9% | 12.0 |  |
| xefasiam | VARCHAR | 26.9% | R |  |
| efasiam | DOUBLE | 32.9% | 3.0 |  |
| xefasiaw | VARCHAR | 26.9% | R |  |
| efasiaw | DOUBLE | 32.9% | 9.0 |  |
| xefbkaat | VARCHAR | 26.9% | R |  |
| efbkaat | DOUBLE | 32.9% | 5664.0 |  |
| xefbkaam | VARCHAR | 26.9% | R |  |
| efbkaam | DOUBLE | 32.9% | 2288.0 |  |
| xefbkaaw | VARCHAR | 26.9% | R |  |
| efbkaaw | DOUBLE | 32.9% | 3376.0 |  |
| xefhispt | VARCHAR | 26.9% | R |  |
| efhispt | DOUBLE | 32.9% | 88.0 |  |
| xefhispm | VARCHAR | 26.9% | R |  |
| efhispm | DOUBLE | 32.9% | 37.0 |  |
| xefhispw | VARCHAR | 26.9% | R |  |
| efhispw | DOUBLE | 32.9% | 51.0 |  |
| xefnhpit | VARCHAR | 26.9% | R |  |
| efnhpit | DOUBLE | 32.9% | 6.0 |  |
| xefnhpim | VARCHAR | 26.9% | R |  |
| efnhpim | DOUBLE | 32.9% | 2.0 |  |
| xefnhpiw | VARCHAR | 26.9% | R |  |
| efnhpiw | DOUBLE | 32.9% | 4.0 |  |
| xefwhitt | VARCHAR | 26.9% | R |  |
| efwhitt | DOUBLE | 32.9% | 128.0 |  |
| xefwhitm | VARCHAR | 26.9% | R |  |
| efwhitm | DOUBLE | 32.9% | 57.0 |  |
| xefwhitw | VARCHAR | 26.9% | R |  |
| efwhitw | DOUBLE | 32.9% | 71.0 |  |
| xef2mort | VARCHAR | 26.9% | R |  |
| ef2mort | DOUBLE | 32.9% | 104.0 |  |
| xef2morm | VARCHAR | 26.9% | R |  |
| ef2morm | DOUBLE | 32.9% | 36.0 |  |
| xef2morw | VARCHAR | 26.9% | R |  |
| ef2morw | DOUBLE | 32.9% | 68.0 |  |
| xefunknt | VARCHAR | 26.9% | R |  |
| efunknt | DOUBLE | 26.9% | 427.0 |  |
| xefunknm | VARCHAR | 26.9% | R |  |
| efunknm | DOUBLE | 26.9% | 135.0 |  |
| xefunknw | VARCHAR | 26.9% | R |  |
| efunknw | DOUBLE | 26.9% | 292.0 |  |
| xefnralt | VARCHAR | 26.9% | R |  |
| efnralt | DOUBLE | 26.9% | 176.0 |  |
| xefnralm | VARCHAR | 26.9% | R |  |
| efnralm | DOUBLE | 26.9% | 108.0 |  |
| xefnralw | VARCHAR | 26.9% | R |  |
| efnralw | DOUBLE | 26.9% | 68.0 |  |
| xefgndrun | VARCHAR | 95.9% | R |  |
| efgndrun | DOUBLE | 99.0% | 45.0 |  |
| xefgndran | VARCHAR | 95.9% | A |  |
| efgndran | DOUBLE | 99.7% | 0.0 |  |
| xefgndrua | VARCHAR | 95.9% | R |  |
| efgndrua | DOUBLE | 99.1% | 45.0 |  |
| xefgndrkn | VARCHAR | 95.9% | R |  |
| efgndrkn | DOUBLE | 99.1% | 6569.0 |  |
| year | BIGINT | 0.0% | 2023 | Appears in 26 tables, common join key |
| xefgndru | VARCHAR | 95.9% | Z |  |
| xefgndra | VARCHAR | 95.9% | A |  |
| xefgndru.1 | VARCHAR | 95.9% | Z |  |
| xefgndrk | VARCHAR | 95.9% | R |  |
| xdvefait | VARCHAR | 90.6% | R |  |
| dvefait | DOUBLE | 90.6% | 9.0 |  |
| xdvefaim | VARCHAR | 90.6% | R |  |
| dvefaim | DOUBLE | 90.6% | 5.0 |  |
| xdvefaiw | VARCHAR | 90.6% | R |  |
| dvefaiw | DOUBLE | 90.6% | 4.0 |  |
| xdvefapt | VARCHAR | 90.6% | R |  |
| dvefapt | DOUBLE | 90.6% | 19.0 |  |
| xdvefapm | VARCHAR | 90.6% | R |  |
| dvefapm | DOUBLE | 90.6% | 8.0 |  |
| xdvefapw | VARCHAR | 90.6% | R |  |
| dvefapw | DOUBLE | 90.6% | 11.0 |  |
| xdvefbkt | VARCHAR | 90.6% | R |  |
| dvefbkt | DOUBLE | 90.6% | 4936.0 |  |
| xdvefbkm | VARCHAR | 90.6% | R |  |
| dvefbkm | DOUBLE | 90.6% | 2235.0 |  |
| xdvefbkw | VARCHAR | 90.6% | R |  |
| dvefbkw | DOUBLE | 90.6% | 2701.0 |  |
| xdvefhst | VARCHAR | 90.6% | R |  |
| dvefhst | DOUBLE | 90.6% | 15.0 |  |
| xdvefhsm | VARCHAR | 90.6% | R |  |
| dvefhsm | DOUBLE | 90.6% | 7.0 |  |
| xdvefhsw | VARCHAR | 90.6% | R |  |
| dvefhsw | DOUBLE | 90.6% | 8.0 |  |
| xdvefwht | VARCHAR | 90.6% | R |  |
| dvefwht | DOUBLE | 90.6% | 245.0 |  |
| xdvefwhm | VARCHAR | 90.6% | R |  |
| dvefwhm | DOUBLE | 90.6% | 99.0 |  |
| xdvefwhw | VARCHAR | 90.6% | R |  |
| dvefwhw | DOUBLE | 90.6% | 146.0 |  |
| xefrac19 | VARCHAR | 67.9% | R |  |
| efrace19 | DOUBLE | 70.9% | 9.0 |  |
| xefrac05 | VARCHAR | 63.7% | R |  |
| efrace05 | DOUBLE | 66.7% | 5.0 |  |
| xefrac06 | VARCHAR | 63.7% | R |  |
| efrace06 | DOUBLE | 66.7% | 4.0 |  |
| xefrac20 | VARCHAR | 67.9% | R |  |
| efrace20 | DOUBLE | 70.9% | 19.0 |  |
| xefrac07 | VARCHAR | 63.7% | R |  |
| efrace07 | DOUBLE | 66.7% | 8.0 |  |
| xefrac08 | VARCHAR | 63.7% | R |  |
| efrace08 | DOUBLE | 66.7% | 11.0 |  |
| xefrac18 | VARCHAR | 67.9% | R |  |
| efrace18 | DOUBLE | 70.9% | 4936.0 |  |
| xefrac03 | VARCHAR | 63.7% | R |  |
| efrace03 | DOUBLE | 66.7% | 2235.0 |  |
| xefrac04 | VARCHAR | 63.7% | R |  |
| efrace04 | DOUBLE | 66.7% | 2701.0 |  |
| xefrac21 | VARCHAR | 67.9% | R |  |
| efrace21 | DOUBLE | 70.9% | 15.0 |  |
| xefrac09 | VARCHAR | 63.7% | R |  |
| efrace09 | DOUBLE | 66.7% | 7.0 |  |
| xefrac10 | VARCHAR | 63.7% | R |  |
| efrace10 | DOUBLE | 66.7% | 8.0 |  |
| xefrac22 | VARCHAR | 67.9% | R |  |
| efrace22 | DOUBLE | 70.9% | 245.0 |  |
| xefrac11 | VARCHAR | 63.7% | R |  |
| efrace11 | DOUBLE | 66.7% | 99.0 |  |
| xefrac12 | VARCHAR | 63.7% | R |  |
| efrace12 | DOUBLE | 66.7% | 146.0 |  |
| xefrac01 | VARCHAR | 73.1% | R |  |
| efrace01 | DOUBLE | 73.1% | 128.0 |  |
| xefrac02 | VARCHAR | 73.1% | R |  |
| efrace02 | DOUBLE | 73.1% | 114.0 |  |
| xefrac13 | VARCHAR | 73.1% | R |  |
| efrace13 | DOUBLE | 73.1% | 0.0 |  |
| xefrac14 | VARCHAR | 73.1% | R |  |
| efrace14 | DOUBLE | 73.1% | 0.0 |  |
| xefrac15 | VARCHAR | 73.1% | R |  |
| efrace15 | DOUBLE | 73.1% | 2505.0 |  |
| xefrac16 | VARCHAR | 73.1% | R |  |
| efrace16 | DOUBLE | 73.1% | 3201.0 |  |
| xefrac17 | VARCHAR | 77.3% | R |  |
| efrace17 | DOUBLE | 77.3% | 242.0 |  |
| xefrac23 | VARCHAR | 77.3% | Z |  |
| efrace23 | DOUBLE | 77.3% | 0.0 |  |
| xefrac24 | VARCHAR | 77.3% | R |  |
| efrace24 | DOUBLE | 77.3% | 5706.0 |  |

## ef_b

Rows: 3,288,967

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| efbage | DOUBLE | 6.3% | 1.0 |  |
| line | BIGINT | 0.0% | 412 | Appears in 4 tables, common join key |
| lstudy | DOUBLE | 2.3% | 1.0 | Appears in 3 tables, common join key |
| xefage01 | VARCHAR | 0.0% | R |  |
| efage01 | DOUBLE | 0.2% | 2282.0 |  |
| xefage02 | VARCHAR | 0.0% | R |  |
| efage02 | DOUBLE | 0.1% | 3378.0 |  |
| xefage03 | VARCHAR | 6.3% | R |  |
| efage03 | DOUBLE | 9.7% | 389.0 |  |
| xefage04 | VARCHAR | 6.3% | R |  |
| efage04 | DOUBLE | 9.7% | 565.0 |  |
| xefage05 | VARCHAR | 6.3% | R |  |
| efage05 | DOUBLE | 6.4% | 5660.0 |  |
| xefage06 | VARCHAR | 6.3% | R |  |
| efage06 | DOUBLE | 9.7% | 954.0 |  |
| xefage07 | VARCHAR | 6.3% | R |  |
| efage07 | DOUBLE | 6.3% | 2671.0 |  |
| xefage08 | VARCHAR | 6.3% | R |  |
| efage08 | DOUBLE | 6.3% | 3943.0 |  |
| xefage09 | VARCHAR | 6.3% | R |  |
| efage09 | DOUBLE | 6.3% | 6614.0 |  |
| year | BIGINT | 0.0% | 2023 | Appears in 26 tables, common join key |
| section | DOUBLE | 97.7% | 1.0 | Appears in 3 tables, common join key |

## ef_c

Rows: 1,356,739

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100663 | Primary institution ID, joins across all IPEDS tables |
| efcstate | DOUBLE | 7.2% | 1.0 |  |
| line | BIGINT | 0.0% | 1 | Appears in 4 tables, common join key |
| xefres01 | VARCHAR | 0.0% | R |  |
| efres01 | BIGINT | 0.0% | 1716 |  |
| xefres02 | VARCHAR | 0.0% | R |  |
| efres02 | DOUBLE | 2.3% | 1650.0 |  |
| year | BIGINT | 0.0% | 2023 | Appears in 26 tables, common join key |

## ef_d

Rows: 145,782

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| xgrcohrt | VARCHAR | 8.4% | R |  |
| grcohrt | DOUBLE | 39.3% | 1976.0 |  |
| xugenter | VARCHAR | 8.4% | R |  |
| ugentern | DOUBLE | 40.8% | 2354.0 |  |
| xpgrcohr | VARCHAR | 8.4% | R |  |
| pgrcohrt | DOUBLE | 40.9% | 84.0 |  |
| xrrftct | VARCHAR | 25.2% | R |  |
| rrftct | DOUBLE | 29.2% | 1547.0 |  |
| xrrftex | VARCHAR | 25.2% | R |  |
| rrftex | DOUBLE | 29.2% | 0.0 |  |
| xrrftin | VARCHAR | 67.2% | R |  |
| rrftin | DOUBLE | 69.1% | 0.0 |  |
| xrrftcta | VARCHAR | 25.2% | R |  |
| rrftcta | DOUBLE | 29.2% | 1547.0 |  |
| xret_nmf | VARCHAR | 25.2% | R |  |
| ret_nmf | DOUBLE | 29.2% | 988.0 |  |
| xret_pcf | VARCHAR | 8.4% | R |  |
| ret_pcf | DOUBLE | 19.1% | 64.0 |  |
| xrrptct | VARCHAR | 25.2% | R |  |
| rrptct | DOUBLE | 46.4% | 10.0 |  |
| xrrptex | VARCHAR | 25.2% | R |  |
| rrptex | DOUBLE | 46.4% | 0.0 |  |
| xrrptin | VARCHAR | 67.2% | R |  |
| rrptin | DOUBLE | 79.0% | 0.0 |  |
| xrrptcta | VARCHAR | 25.2% | R |  |
| rrptcta | DOUBLE | 46.4% | 10.0 |  |
| xret_nmp | VARCHAR | 25.2% | R |  |
| ret_nmp | DOUBLE | 46.4% | 4.0 |  |
| xret_pcp | VARCHAR | 8.4% | R |  |
| ret_pcp | DOUBLE | 50.6% | 40.0 |  |
| xstufacr | VARCHAR | 33.6% | R |  |
| stufacr | DOUBLE | 33.6% | 19.0 |  |
| year | BIGINT | 0.0% | 2023 | Appears in 26 tables, common join key |
| fyrpyear | DOUBLE | 95.8% | 1.0 | Appears in 4 tables, common join key |
| xtostucu | VARCHAR | 95.8% | R |  |
| tostucu | DOUBLE | 95.9% | 20239.0 |  |
| xtostucg | VARCHAR | 95.8% | R |  |
| tostucg | DOUBLE | 97.4% | 3461.0 |  |
| xtostucp | VARCHAR | 95.8% | R |  |
| tostucp | DOUBLE | 97.7% | 661.0 |  |
| xcdactua | VARCHAR | 95.8% | R |  |
| cdactua | DOUBLE | 96.6% | 873152.0 |  |
| xcnactua | VARCHAR | 95.8% | B |  |
| cnactua | DOUBLE | 97.8% | 1141600.0 |  |
| xcdactga | VARCHAR | 95.8% | R |  |
| cdactga | DOUBLE | 97.8% | 111321.0 |  |

## effy

Rows: 840,872

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| effyalev | DOUBLE | 33.8% | 1.0 |  |
| effylev | BIGINT | 0.0% | 1 |  |
| lstudy | BIGINT | 0.0% | 999 | Appears in 3 tables, common join key |
| xeytotlt | VARCHAR | 11.0% | R |  |
| efytotlt | DOUBLE | 11.0% | 7120.0 |  |
| xeytotlm | VARCHAR | 11.0% | R |  |
| efytotlm | DOUBLE | 11.0% | 2919.0 |  |
| xeytotlw | VARCHAR | 11.0% | R |  |
| efytotlw | DOUBLE | 11.0% | 4201.0 |  |
| xefyaiat | VARCHAR | 11.0% | R |  |
| efyaiant | DOUBLE | 14.2% | 9.0 |  |
| xefyaiam | VARCHAR | 11.0% | R |  |
| efyaianm | DOUBLE | 14.2% | 5.0 |  |
| xefyaiaw | VARCHAR | 11.0% | R |  |
| efyaianw | DOUBLE | 14.2% | 4.0 |  |
| xefyasit | VARCHAR | 11.0% | R |  |
| efyasiat | DOUBLE | 14.2% | 15.0 |  |
| xefyasim | VARCHAR | 11.0% | R |  |
| efyasiam | DOUBLE | 14.2% | 4.0 |  |
| xefyasiw | VARCHAR | 11.0% | R |  |
| efyasiaw | DOUBLE | 14.2% | 11.0 |  |
| xefybkat | VARCHAR | 11.0% | R |  |
| efybkaat | DOUBLE | 14.2% | 6038.0 |  |
| xefybkam | VARCHAR | 11.0% | R |  |
| efybkaam | DOUBLE | 14.2% | 2469.0 |  |
| xefybkaw | VARCHAR | 11.0% | R |  |
| efybkaaw | DOUBLE | 14.2% | 3569.0 |  |
| xefyhist | VARCHAR | 11.0% | R |  |
| efyhispt | DOUBLE | 14.2% | 108.0 |  |
| xefyhism | VARCHAR | 11.0% | R |  |
| efyhispm | DOUBLE | 14.2% | 42.0 |  |
| xefyhisw | VARCHAR | 11.0% | R |  |
| efyhispw | DOUBLE | 14.2% | 66.0 |  |
| xefynhpt | VARCHAR | 11.0% | R |  |
| efynhpit | DOUBLE | 14.2% | 6.0 |  |
| xefynhpm | VARCHAR | 11.0% | R |  |
| efynhpim | DOUBLE | 14.2% | 2.0 |  |
| xefynhpw | VARCHAR | 11.0% | R |  |
| efynhpiw | DOUBLE | 14.2% | 4.0 |  |
| xefywhit | VARCHAR | 11.0% | R |  |
| efywhitt | DOUBLE | 14.2% | 152.0 |  |
| xefywhim | VARCHAR | 11.0% | R |  |
| efywhitm | DOUBLE | 14.2% | 67.0 |  |
| xefywhiw | VARCHAR | 11.0% | R |  |
| efywhitw | DOUBLE | 14.2% | 85.0 |  |
| xefy2mot | VARCHAR | 11.0% | R |  |
| efy2mort | DOUBLE | 14.2% | 115.0 |  |
| xefy2mom | VARCHAR | 11.0% | R |  |
| efy2morm | DOUBLE | 14.2% | 44.0 |  |
| xefy2mow | VARCHAR | 11.0% | R |  |
| efy2morw | DOUBLE | 14.2% | 71.0 |  |
| xeyunknt | VARCHAR | 11.0% | R |  |
| efyunknt | DOUBLE | 11.0% | 480.0 |  |
| xeyunknm | VARCHAR | 11.0% | R |  |
| efyunknm | DOUBLE | 11.0% | 166.0 |  |
| xeyunknw | VARCHAR | 11.0% | R |  |
| efyunknw | DOUBLE | 11.0% | 314.0 |  |
| xeynralt | VARCHAR | 11.0% | R |  |
| efynralt | DOUBLE | 11.0% | 197.0 |  |
| xeynralm | VARCHAR | 11.0% | R |  |
| efynralm | DOUBLE | 11.0% | 120.0 |  |
| xeynralw | VARCHAR | 11.0% | R |  |
| efynralw | DOUBLE | 11.0% | 77.0 |  |
| xefyguun | VARCHAR | 58.5% | R |  |
| efyguun | VARCHAR | 70.8% | 51 |  |
| xefyguan | VARCHAR | 58.5% | A |  |
| efyguan | VARCHAR | 72.1% | . |  |
| xefyguto | VARCHAR | 58.5% | R |  |
| efygutot | VARCHAR | 70.8% | 51 |  |
| xefygukn | VARCHAR | 58.5% | R |  |
| efygukn | VARCHAR | 70.8% | 7069 |  |
| year | BIGINT | 0.0% | 2024 | Appears in 26 tables, common join key |
| xfyrac03 | VARCHAR | 83.3% | R |  |
| fyrace03 | DOUBLE | 85.6% | 2533.0 |  |
| xfyrac04 | VARCHAR | 83.3% | R |  |
| fyrace04 | DOUBLE | 85.6% | 3028.0 |  |
| xfyrac05 | VARCHAR | 83.3% | R |  |
| fyrace05 | DOUBLE | 85.6% | 8.0 |  |
| xfyrac06 | VARCHAR | 83.3% | R |  |
| fyrace06 | DOUBLE | 85.6% | 7.0 |  |
| xfyrac07 | VARCHAR | 83.3% | R |  |
| fyrace07 | DOUBLE | 85.6% | 12.0 |  |
| xfyrac08 | VARCHAR | 83.3% | R |  |
| fyrace08 | DOUBLE | 85.6% | 17.0 |  |
| xfyrac09 | VARCHAR | 83.3% | R |  |
| fyrace09 | DOUBLE | 85.6% | 13.0 |  |
| xfyrac10 | VARCHAR | 83.3% | R |  |
| fyrace10 | DOUBLE | 85.6% | 19.0 |  |
| xfyrac11 | VARCHAR | 83.3% | R |  |
| fyrace11 | DOUBLE | 85.6% | 152.0 |  |
| xfyrac12 | VARCHAR | 83.3% | R |  |
| fyrace12 | DOUBLE | 85.6% | 230.0 |  |
| xfyrac18 | VARCHAR | 83.3% | R |  |
| fyrace18 | DOUBLE | 85.6% | 5561.0 |  |
| xfyrac19 | VARCHAR | 83.3% | R |  |
| fyrace19 | DOUBLE | 85.6% | 15.0 |  |
| xfyrac20 | VARCHAR | 83.3% | R |  |
| fyrace20 | DOUBLE | 85.6% | 29.0 |  |
| xfyrac21 | VARCHAR | 83.3% | R |  |
| fyrace21 | DOUBLE | 85.6% | 32.0 |  |
| xfyrac22 | VARCHAR | 83.3% | R |  |
| fyrace22 | DOUBLE | 85.6% | 382.0 |  |
| xdveyait | VARCHAR | 94.3% | R |  |
| dveyait | DOUBLE | 94.3% | 15.0 |  |
| xdveyaim | VARCHAR | 94.3% | R |  |
| dveyaim | DOUBLE | 94.3% | 8.0 |  |
| xdveyaiw | VARCHAR | 94.3% | R |  |
| dveyaiw | DOUBLE | 94.3% | 7.0 |  |
| xdveyapt | VARCHAR | 94.3% | R |  |
| dveyapt | DOUBLE | 94.3% | 29.0 |  |
| xdveyapm | VARCHAR | 94.3% | R |  |
| dveyapm | DOUBLE | 94.3% | 12.0 |  |
| xdveyapw | VARCHAR | 94.3% | R |  |
| dveyapw | DOUBLE | 94.3% | 17.0 |  |
| xdveybkt | VARCHAR | 94.3% | R |  |
| dveybkt | DOUBLE | 94.3% | 5561.0 |  |
| xdveybkm | VARCHAR | 94.3% | R |  |
| dveybkm | DOUBLE | 94.3% | 2533.0 |  |
| xdveybkw | VARCHAR | 94.3% | R |  |
| dveybkw | DOUBLE | 94.3% | 3028.0 |  |
| xdveyhst | VARCHAR | 94.3% | R |  |
| dveyhst | DOUBLE | 94.3% | 32.0 |  |
| xdveyhsm | VARCHAR | 94.3% | R |  |
| dveyhsm | DOUBLE | 94.3% | 13.0 |  |
| xdveyhsw | VARCHAR | 94.3% | R |  |
| dveyhsw | DOUBLE | 94.3% | 19.0 |  |
| xdveywht | VARCHAR | 94.3% | R |  |
| dveywht | DOUBLE | 94.3% | 382.0 |  |
| xdveywhm | VARCHAR | 94.3% | R |  |
| dveywhm | DOUBLE | 94.3% | 152.0 |  |
| xdveywhw | VARCHAR | 94.3% | R |  |
| dveywhw | DOUBLE | 94.3% | 230.0 |  |
| xfyrac01 | VARCHAR | 89.0% | Z |  |
| fyrace01 | DOUBLE | 89.0% | 0.0 |  |
| xfyrac02 | VARCHAR | 89.0% | Z |  |
| fyrace02 | DOUBLE | 89.0% | 0.0 |  |
| xfyrac13 | VARCHAR | 89.0% | R |  |
| fyrace13 | DOUBLE | 89.0% | 12965.0 |  |
| xfyrac14 | VARCHAR | 89.0% | R |  |
| fyrace14 | DOUBLE | 89.0% | 3683.0 |  |
| xfyrac15 | VARCHAR | 89.0% | R |  |
| fyrace15 | DOUBLE | 89.0% | 268053.0 |  |
| xfyrac16 | VARCHAR | 89.0% | R |  |
| fyrace16 | DOUBLE | 89.0% | 64042.0 |  |
| xfyrac17 | VARCHAR | 89.0% | Z |  |
| fyrace17 | DOUBLE | 89.0% | 0.0 |  |
| xfyrac23 | VARCHAR | 89.0% | R |  |
| fyrace23 | DOUBLE | 89.0% | 16648.0 |  |
| xfyrac24 | VARCHAR | 89.0% | R |  |
| fyrace24 | DOUBLE | 89.0% | 332095.0 |  |

## efia

Rows: 154,783

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| xcdactua | VARCHAR | 0.0% | R |  |
| cdactua | DOUBLE | 31.9% | 151217.0 |  |
| xcnactua | VARCHAR | 0.0% | A |  |
| cnactua | DOUBLE | 62.5% | 62353.0 |  |
| xcdactga | VARCHAR | 0.0% | R |  |
| cdactga | DOUBLE | 68.5% | 13090.0 |  |
| xefteug | VARCHAR | 8.4% | G |  |
| efteug | DOUBLE | 12.4% | 5041.0 |  |
| xeftegd | VARCHAR | 8.4% | G |  |
| eftegd | DOUBLE | 72.2% | 545.0 |  |
| xfteug | VARCHAR | 8.4% | G |  |
| fteug | DOUBLE | 12.4% | 5041.0 |  |
| xftegd | VARCHAR | 8.4% | G |  |
| ftegd | DOUBLE | 72.2% | 545.0 |  |
| xftedpp | VARCHAR | 44.1% | A |  |
| ftedpp | VARCHAR | 87.0% | . |  |
| acttype | DOUBLE | 8.4% | 2.0 |  |
| year | BIGINT | 0.0% | 2024 | Appears in 26 tables, common join key |

## f1a

Rows: 42,334

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| xf1a01 | VARCHAR | 0.0% | R |  |
| f1a01 | DOUBLE | 19.1% | 185317695.0 |  |
| xf1a31 | VARCHAR | 25.4% | R |  |
| f1a31 | DOUBLE | 42.3% | 216635660.0 |  |
| xf1a04 | VARCHAR | 0.0% | R |  |
| f1a04 | DOUBLE | 19.1% | 114706.0 |  |
| xf1a05 | VARCHAR | 0.0% | R |  |
| f1a05 | DOUBLE | 19.1% | 216750366.0 |  |
| xf1a06 | VARCHAR | 0.0% | R |  |
| f1a06 | DOUBLE | 19.1% | 402068061.0 |  |
| xf1a19 | VARCHAR | 63.1% | R |  |
| f1a19 | DOUBLE | 71.6% | 49334293.0 |  |
| xf1a07 | VARCHAR | 0.0% | R |  |
| f1a07 | DOUBLE | 19.1% | 0.0 |  |
| xf1a08 | VARCHAR | 0.0% | R |  |
| f1a08 | DOUBLE | 19.1% | 74071288.0 |  |
| xf1a09 | VARCHAR | 0.0% | R |  |
| f1a09 | DOUBLE | 19.1% | 74071288.0 |  |
| xf1a10 | VARCHAR | 0.0% | R |  |
| f1a10 | DOUBLE | 19.1% | 65436528.0 |  |
| xf1a11 | VARCHAR | 0.0% | R |  |
| f1a11 | DOUBLE | 19.1% | 127828301.0 |  |
| xf1a12 | VARCHAR | 0.0% | R |  |
| f1a12 | DOUBLE | 19.1% | 193264829.0 |  |
| xf1a13 | VARCHAR | 0.0% | R |  |
| f1a13 | DOUBLE | 19.1% | 267336117.0 |  |
| xf1a20 | VARCHAR | 63.1% | R |  |
| f1a20 | DOUBLE | 71.6% | 42633094.0 |  |
| xf1a14 | VARCHAR | 0.0% | R |  |
| f1a14 | DOUBLE | 19.1% | 160949955.0 |  |
| xf1a15 | VARCHAR | 0.0% | R |  |
| f1a15 | DOUBLE | 19.1% | -35116319.0 |  |
| xf1a16 | VARCHAR | 0.0% | R |  |
| f1a16 | DOUBLE | 19.1% | 0.0 |  |
| xf1a17 | VARCHAR | 0.0% | R |  |
| f1a17 | DOUBLE | 19.1% | 15599507.0 |  |
| xf1a18 | VARCHAR | 0.0% | R |  |
| f1a18 | DOUBLE | 19.1% | 141433143.0 |  |
| xf1a214 | VARCHAR | 0.0% | R |  |
| f1a214 | DOUBLE | 19.1% | 5598192.0 |  |
| xf1a224 | VARCHAR | 0.0% | R |  |
| f1a224 | DOUBLE | 19.1% | 0.0 |  |
| xf1a234 | VARCHAR | 0.0% | R |  |
| f1a234 | DOUBLE | 19.1% | 280904064.0 |  |
| xf1a324 | VARCHAR | 25.4% | R |  |
| f1a324 | DOUBLE | 47.8% | 45293378.0 |  |
| xf1a274 | VARCHAR | 0.0% | R |  |
| f1a274 | DOUBLE | 19.1% | 36764776.0 |  |
| xf1a27t4 | VARCHAR | 30.1% | R |  |
| f1a27t4 | DOUBLE | 46.2% | 368560410.0 |  |
| xf1a284 | VARCHAR | 0.0% | R |  |
| f1a284 | DOUBLE | 19.1% | 147293105.0 |  |
| xf1a334 | VARCHAR | 25.4% | R |  |
| f1a334 | DOUBLE | 47.8% | 0.0 |  |
| xf1a344 | VARCHAR | 25.4% | R |  |
| f1a344 | DOUBLE | 47.8% | 7087979.0 |  |
| xf1d01 | VARCHAR | 0.0% | R |  |
| f1d01 | DOUBLE | 14.8% | 232809852.0 |  |
| xf1d02 | VARCHAR | 0.0% | R |  |
| f1d02 | DOUBLE | 14.8% | 227586697.0 |  |
| xf1d03 | VARCHAR | 0.0% | R |  |
| f1d03 | DOUBLE | 15.2% | 5223155.0 |  |
| xf1d04 | VARCHAR | 0.0% | R |  |
| f1d04 | DOUBLE | 19.0% | 136209988.0 |  |
| xf1d05 | VARCHAR | 0.0% | R |  |
| f1d05 | DOUBLE | 19.0% | 0.0 |  |
| xf1d06 | VARCHAR | 0.0% | R |  |
| f1d06 | DOUBLE | 19.0% | 141433143.0 |  |
| xf1b01 | VARCHAR | 0.0% | R |  |
| f1b01 | BIGINT | 0.0% | 51735563 |  |
| xf1b02 | VARCHAR | 0.0% | R |  |
| f1b02 | BIGINT | 0.0% | 43116021 |  |
| xf1b03 | VARCHAR | 0.0% | R |  |
| f1b03 | BIGINT | 0.0% | 1843576 |  |
| xf1b04 | VARCHAR | 0.0% | R |  |
| f1b04 | BIGINT | 0.0% | 0 |  |
| xf1b04a | VARCHAR | 25.4% | R |  |
| f1b04a | DOUBLE | 31.7% | 0.0 |  |
| xf1b04b | VARCHAR | 25.4% | R |  |
| f1b04b | DOUBLE | 31.7% | 0.0 |  |
| xf1b05 | VARCHAR | 0.0% | R |  |
| f1b05 | DOUBLE | 9.7% | 31925431.0 |  |
| xf1b06 | VARCHAR | 0.0% | R |  |
| f1b06 | DOUBLE | 57.7% | 0.0 |  |
| xf1b26 | VARCHAR | 25.4% | R |  |
| f1b26 | DOUBLE | 31.7% | 1489437.0 |  |
| xf1b07 | VARCHAR | 0.0% | R |  |
| f1b07 | DOUBLE | 57.7% | 0.0 |  |
| xf1b08 | VARCHAR | 0.0% | R |  |
| f1b08 | DOUBLE | 0.0% | 2867017.0 |  |
| xf1b09 | VARCHAR | 0.0% | R |  |
| f1b09 | DOUBLE | 0.0% | 132977045.0 |  |
| xf1b10 | VARCHAR | 0.0% | R |  |
| f1b10 | BIGINT | 0.0% | 2303040 |  |
| xf1b11 | VARCHAR | 0.0% | R |  |
| f1b11 | BIGINT | 0.0% | 74140134 |  |
| xf1b12 | VARCHAR | 0.0% | R |  |
| f1b12 | BIGINT | 0.0% | 0 |  |
| xf1b13 | VARCHAR | 0.0% | R |  |
| f1b13 | BIGINT | 0.0% | 20038415 |  |
| xf1b14 | VARCHAR | 0.0% | Z |  |
| f1b14 | BIGINT | 0.0% | 0 |  |
| xf1b15 | VARCHAR | 0.0% | Z |  |
| f1b15 | BIGINT | 0.0% | 0 |  |
| xf1b16 | VARCHAR | 0.0% | R |  |
| f1b16 | BIGINT | 0.0% | 1950000 |  |
| xf1b17 | VARCHAR | 0.0% | R |  |
| f1b17 | DOUBLE | 0.0% | 810609.0 |  |
| xf1b18 | VARCHAR | 0.0% | R |  |
| f1b18 | DOUBLE | 0.0% | 590609.0 |  |
| xf1b19 | VARCHAR | 0.0% | R |  |
| f1b19 | DOUBLE | 0.0% | 99832807.0 |  |
| xf1b27 | VARCHAR | 34.7% | R |  |
| f1b27 | DOUBLE | 34.7% | 232809852.0 |  |
| xf1b20 | VARCHAR | 0.0% | R |  |
| f1b20 | DOUBLE | 11.2% | 0.0 |  |
| xf1b21 | VARCHAR | 0.0% | R |  |
| f1b21 | DOUBLE | 11.2% | 0.0 |  |
| xf1b22 | VARCHAR | 0.0% | R |  |
| f1b22 | DOUBLE | 11.2% | 0.0 |  |
| xf1b23 | VARCHAR | 0.0% | R |  |
| f1b23 | DOUBLE | 4.6% | 0.0 |  |
| xf1b24 | VARCHAR | 0.0% | R |  |
| f1b24 | DOUBLE | 0.0% | 0.0 |  |
| xf1b25 | VARCHAR | 0.0% | R |  |
| f1b25 | DOUBLE | 0.0% | 232809852.0 |  |
| xf1c011 | VARCHAR | 0.0% | R |  |
| f1c011 | DOUBLE | 0.0% | 32549205.0 |  |
| xf1c012 | VARCHAR | 0.0% | R |  |
| f1c012 | DOUBLE | 0.0% | 25953542.0 |  |
| xf1c021 | VARCHAR | 0.0% | R |  |
| f1c021 | DOUBLE | 0.0% | 16308749.0 |  |
| xf1c022 | VARCHAR | 0.0% | R |  |
| f1c022 | DOUBLE | 0.0% | 7316158.0 |  |
| xf1c031 | VARCHAR | 0.0% | R |  |
| f1c031 | DOUBLE | 0.0% | 12768521.0 |  |
| xf1c032 | VARCHAR | 0.0% | R |  |
| f1c032 | DOUBLE | 0.0% | 6297582.0 |  |
| xf1c051 | VARCHAR | 0.0% | R |  |
| f1c051 | DOUBLE | 0.0% | 8910325.0 |  |
| xf1c052 | VARCHAR | 0.0% | R |  |
| f1c052 | DOUBLE | 0.0% | 5087615.0 |  |
| xf1c061 | VARCHAR | 0.0% | R |  |
| f1c061 | DOUBLE | 0.0% | 29971958.0 |  |
| xf1c062 | VARCHAR | 0.0% | R |  |
| f1c062 | DOUBLE | 0.0% | 6010269.0 |  |
| xf1c071 | VARCHAR | 0.0% | R |  |
| f1c071 | DOUBLE | 0.0% | 31080494.0 |  |
| xf1c072 | VARCHAR | 0.0% | R |  |
| f1c072 | DOUBLE | 0.0% | 7881636.0 |  |
| xf1c101 | VARCHAR | 0.0% | R |  |
| f1c101 | DOUBLE | 0.2% | 32581617.0 |  |
| xf1c111 | VARCHAR | 0.0% | R |  |
| f1c111 | DOUBLE | 11.2% | 37287023.0 |  |
| xf1c112 | VARCHAR | 0.0% | R |  |
| f1c112 | DOUBLE | 11.2% | 5507323.0 |  |
| xf1c121 | VARCHAR | 0.0% | Z |  |
| f1c121 | DOUBLE | 57.7% | 0.0 |  |
| xf1c122 | VARCHAR | 0.0% | Z |  |
| f1c122 | DOUBLE | 57.7% | 0.0 |  |
| xf1c131 | VARCHAR | 0.0% | Z |  |
| f1c131 | DOUBLE | 57.7% | 0.0 |  |
| xf1c132 | VARCHAR | 0.0% | Z |  |
| f1c132 | DOUBLE | 57.7% | 0.0 |  |
| xf1c141 | VARCHAR | 0.0% | R |  |
| f1c141 | DOUBLE | 0.0% | 26128805.0 |  |
| xf1c142 | VARCHAR | 0.0% | R |  |
| f1c142 | DOUBLE | 0.0% | 1670555.0 |  |
| xf1c191 | VARCHAR | 0.0% | R |  |
| f1c191 | DOUBLE | 0.0% | 227586697.0 |  |
| xf1c192 | VARCHAR | 0.0% | R |  |
| f1c192 | DOUBLE | 0.0% | 65724680.0 |  |
| xf1c193 | VARCHAR | 0.0% | R |  |
| f1c193 | DOUBLE | 0.0% | 20551730.0 |  |
| xf1c19om | VARCHAR | 63.1% | R |  |
| f1c19om | DOUBLE | 63.1% | 3421427.0 |  |
| xf1c19dp | VARCHAR | 63.1% | R |  |
| f1c19dp | DOUBLE | 63.1% | 12118538.0 |  |
| xf1c19in | VARCHAR | 63.1% | R |  |
| f1c19in | DOUBLE | 63.1% | 707475.0 |  |
| xf1c19ot | VARCHAR | 63.1% | R |  |
| f1c19ot | DOUBLE | 63.1% | 125062847.0 |  |
| f1mhp | DOUBLE | 58.4% | 1.0 |  |
| xf1m01 | VARCHAR | 58.4% | R |  |
| f1m01 | DOUBLE | 70.3% | 8288567.0 |  |
| xf1m02 | VARCHAR | 58.4% | R |  |
| f1m02 | DOUBLE | 70.3% | 107557000.0 |  |
| xf1m03 | VARCHAR | 58.4% | R |  |
| f1m03 | DOUBLE | 70.3% | 21069000.0 |  |
| xf1m04 | VARCHAR | 58.4% | R |  |
| f1m04 | DOUBLE | 70.3% | 16625000.0 |  |
| f1mhop | DOUBLE | 81.7% | 1.0 |  |
| xf1m05 | VARCHAR | 77.1% | R |  |
| f1m05 | DOUBLE | 84.4% | 2902635.0 |  |
| xf1m06 | VARCHAR | 77.1% | R |  |
| f1m06 | DOUBLE | 84.4% | 17756297.0 |  |
| xf1m07 | VARCHAR | 77.1% | R |  |
| f1m07 | DOUBLE | 84.4% | 21407014.0 |  |
| xf1m08 | VARCHAR | 77.1% | R |  |
| f1m08 | DOUBLE | 84.4% | 32709293.0 |  |
| xf1e01 | VARCHAR | 0.0% | R |  |
| f1e01 | DOUBLE | 2.9% | 20038415.0 |  |
| xf1e02 | VARCHAR | 0.0% | R |  |
| f1e02 | DOUBLE | 2.9% | 10434767.0 |  |
| xf1e03 | VARCHAR | 0.0% | R |  |
| f1e03 | DOUBLE | 2.9% | 1413863.0 |  |
| xf1e04 | VARCHAR | 0.0% | R |  |
| f1e04 | DOUBLE | 2.9% | 0.0 |  |
| xf1e05 | VARCHAR | 0.0% | Z |  |
| f1e05 | DOUBLE | 2.9% | 0.0 |  |
| xf1e06 | VARCHAR | 0.0% | R |  |
| f1e06 | DOUBLE | 2.9% | 26615257.0 |  |
| xf1e07 | VARCHAR | 0.0% | R |  |
| f1e07 | DOUBLE | 2.9% | 58502302.0 |  |
| xf1e08 | VARCHAR | 0.0% | R |  |
| f1e08 | DOUBLE | 2.9% | 25920685.0 |  |
| xf1e09 | VARCHAR | 0.0% | R |  |
| f1e09 | DOUBLE | 2.9% | 0.0 |  |
| xf1e10 | VARCHAR | 0.0% | R |  |
| f1e10 | DOUBLE | 2.9% | 25920685.0 |  |
| xf1e11 | VARCHAR | 0.0% | R |  |
| f1e11 | DOUBLE | 2.8% | 32581617.0 |  |
| xf1e12 | VARCHAR | 81.7% | R |  |
| f1e12 | DOUBLE | 82.3% | 0.0 |  |
| xf1e121 | VARCHAR | 81.7% | R |  |
| f1e121 | DOUBLE | 82.3% | 0.0 |  |
| xf1e122 | VARCHAR | 81.7% | R |  |
| f1e122 | DOUBLE | 82.3% | 0.0 |  |
| xf1e13 | VARCHAR | 81.7% | R |  |
| f1e13 | DOUBLE | 82.3% | 90250.0 |  |
| xf1e131 | VARCHAR | 81.7% | R |  |
| f1e131 | DOUBLE | 82.3% | 90250.0 |  |
| xf1e132 | VARCHAR | 81.7% | Z |  |
| f1e132 | DOUBLE | 82.3% | 0.0 |  |
| xf1e14 | VARCHAR | 81.7% | R |  |
| f1e14 | DOUBLE | 82.3% | 24775.0 |  |
| xf1e141 | VARCHAR | 81.7% | R |  |
| f1e141 | DOUBLE | 82.3% | 24775.0 |  |
| xf1e142 | VARCHAR | 81.7% | Z |  |
| f1e142 | DOUBLE | 82.3% | 0.0 |  |
| xf1e15 | VARCHAR | 81.7% | R |  |
| f1e15 | DOUBLE | 82.3% | 0.0 |  |
| xf1e151 | VARCHAR | 81.7% | Z |  |
| f1e151 | DOUBLE | 82.3% | 0.0 |  |
| xf1e152 | VARCHAR | 81.7% | Z |  |
| f1e152 | DOUBLE | 82.3% | 0.0 |  |
| xf1e16 | VARCHAR | 81.7% | R |  |
| f1e16 | DOUBLE | 82.3% | 0.0 |  |
| xf1e161 | VARCHAR | 81.7% | Z |  |
| f1e161 | DOUBLE | 82.3% | 0.0 |  |
| xf1e162 | VARCHAR | 81.7% | Z |  |
| f1e162 | DOUBLE | 82.3% | 0.0 |  |
| xf1e17 | VARCHAR | 81.7% | R |  |
| f1e17 | DOUBLE | 82.3% | 25805660.0 |  |
| xf1e171 | VARCHAR | 81.7% | R |  |
| f1e171 | DOUBLE | 82.3% | 25805660.0 |  |
| xf1e172 | VARCHAR | 81.7% | R |  |
| f1e172 | DOUBLE | 82.3% | 0.0 |  |
| f1fha | DOUBLE | 3.0% | 2.0 |  |
| xf1h01 | VARCHAR | 3.0% | A |  |
| f1h01 | DOUBLE | 36.6% | 673320170.0 |  |
| xf1h02 | VARCHAR | 3.0% | A |  |
| f1h02 | DOUBLE | 36.6% | 739372914.0 |  |
| xf1h03 | VARCHAR | 81.7% | A |  |
| f1h03 | DOUBLE | 87.4% | 66052744.0 |  |
| xf1h03a | VARCHAR | 81.7% | A |  |
| f1h03a | DOUBLE | 87.4% | 28180269.0 |  |
| xf1h03b | VARCHAR | 81.7% | A |  |
| f1h03b | DOUBLE | 87.4% | 37872475.0 |  |
| xf1h03c | VARCHAR | 81.7% | A |  |
| f1h03c | DOUBLE | 87.4% | -30412890.0 |  |
| xf1h03d | VARCHAR | 81.7% | A |  |
| f1h03d | DOUBLE | 87.4% | 30412890.0 |  |
| xf1n01 | VARCHAR | 81.7% | R |  |
| f1n01 | DOUBLE | 85.9% | 19175452.0 |  |
| xf1n02 | VARCHAR | 81.7% | R |  |
| f1n02 | DOUBLE | 85.9% | 232809484.0 |  |
| xf1n03 | VARCHAR | 81.7% | R |  |
| f1n03 | DOUBLE | 85.9% | 5223151.0 |  |
| xf1n04 | VARCHAR | 81.7% | R |  |
| f1n04 | DOUBLE | 85.9% | 141433143.0 |  |
| xf1n05 | VARCHAR | 81.7% | R |  |
| f1n05 | DOUBLE | 85.9% | -35116319.0 |  |
| xf1n06 | VARCHAR | 81.7% | R |  |
| f1n06 | DOUBLE | 85.9% | 18106512.0 |  |
| xf1n07 | VARCHAR | 81.7% | R |  |
| f1n07 | DOUBLE | 85.9% | 227586697.0 |  |
| year | BIGINT | 0.0% | 2023 | Appears in 26 tables, common join key |
| xf1c013 | VARCHAR | 36.9% | R |  |
| f1c013 | DOUBLE | 36.9% | 6893526.0 |  |
| xf1c014 | VARCHAR | 36.9% | R |  |
| f1c014 | DOUBLE | 36.9% | 2169522.0 |  |
| xf1c015 | VARCHAR | 36.9% | R |  |
| f1c015 | DOUBLE | 36.9% | 1517879.0 |  |
| xf1c016 | VARCHAR | 62.4% | R |  |
| f1c016 | DOUBLE | 68.7% | 3812817.0 |  |
| xf1c017 | VARCHAR | 67.0% | R |  |
| f1c017 | DOUBLE | 69.6% | 600867.0 |  |
| xf1c023 | VARCHAR | 36.9% | R |  |
| f1c023 | DOUBLE | 36.9% | 723458.0 |  |
| xf1c024 | VARCHAR | 36.9% | R |  |
| f1c024 | DOUBLE | 36.9% | 515745.0 |  |
| xf1c025 | VARCHAR | 36.9% | R |  |
| f1c025 | DOUBLE | 36.9% | 3127149.0 |  |
| xf1c026 | VARCHAR | 62.4% | R |  |
| f1c026 | DOUBLE | 68.7% | 906393.0 |  |
| xf1c027 | VARCHAR | 67.0% | R |  |
| f1c027 | DOUBLE | 69.6% | 142840.0 |  |
| xf1c033 | VARCHAR | 36.9% | R |  |
| f1c033 | DOUBLE | 36.9% | 2717021.0 |  |
| xf1c034 | VARCHAR | 36.9% | R |  |
| f1c034 | DOUBLE | 36.9% | 1085519.0 |  |
| xf1c035 | VARCHAR | 36.9% | R |  |
| f1c035 | DOUBLE | 36.9% | 4438690.0 |  |
| xf1c036 | VARCHAR | 62.4% | R |  |
| f1c036 | DOUBLE | 68.7% | 1907742.0 |  |
| xf1c037 | VARCHAR | 67.0% | R |  |
| f1c037 | DOUBLE | 69.6% | 300644.0 |  |
| xf1c053 | VARCHAR | 36.9% | R |  |
| f1c053 | DOUBLE | 36.9% | 926940.0 |  |
| xf1c054 | VARCHAR | 36.9% | R |  |
| f1c054 | DOUBLE | 36.9% | 443039.0 |  |
| xf1c055 | VARCHAR | 36.9% | R |  |
| f1c055 | DOUBLE | 36.9% | 2291192.0 |  |
| xf1c056 | VARCHAR | 62.4% | R |  |
| f1c056 | DOUBLE | 68.7% | 778618.0 |  |
| xf1c057 | VARCHAR | 67.0% | R |  |
| f1c057 | DOUBLE | 69.6% | 122703.0 |  |
| xf1c063 | VARCHAR | 36.9% | R |  |
| f1c063 | DOUBLE | 36.9% | 2238420.0 |  |
| xf1c064 | VARCHAR | 36.9% | R |  |
| f1c064 | DOUBLE | 36.9% | 1014962.0 |  |
| xf1c065 | VARCHAR | 36.9% | R |  |
| f1c065 | DOUBLE | 36.9% | 5195576.0 |  |
| xf1c066 | VARCHAR | 62.4% | R |  |
| f1c066 | DOUBLE | 68.7% | 1783741.0 |  |
| xf1c067 | VARCHAR | 67.0% | R |  |
| f1c067 | DOUBLE | 69.6% | 281102.0 |  |
| xf1c073 | VARCHAR | 36.9% | R |  |
| f1c073 | DOUBLE | 36.9% | 2905645.0 |  |
| xf1c074 | VARCHAR | 36.9% | R |  |
| f1c074 | DOUBLE | 36.9% | 1892470.0 |  |
| xf1c075 | VARCHAR | 36.9% | R |  |
| f1c075 | DOUBLE | 36.9% | 13067622.0 |  |
| xf1c076 | VARCHAR | 62.4% | R |  |
| f1c076 | DOUBLE | 68.7% | 3325913.0 |  |
| xf1c077 | VARCHAR | 67.0% | R |  |
| f1c077 | DOUBLE | 69.6% | 524135.0 |  |
| xf1c081 | VARCHAR | 41.7% | R |  |
| f1c081 | DOUBLE | 44.7% | 0.0 |  |
| xf1c082 | VARCHAR | 36.9% | R |  |
| f1c082 | DOUBLE | 36.9% | 336317.0 |  |
| xf1c083 | VARCHAR | 36.9% | R |  |
| f1c083 | DOUBLE | 36.9% | 124630.0 |  |
| xf1c084 | VARCHAR | 36.9% | R |  |
| f1c084 | DOUBLE | 36.9% | 0.0 |  |
| xf1c085 | VARCHAR | 36.9% | R |  |
| f1c085 | DOUBLE | 36.9% | 13382831.0 |  |
| xf1c086 | VARCHAR | 62.4% | R |  |
| f1c086 | DOUBLE | 68.7% | -13843778.0 |  |
| xf1c087 | VARCHAR | 67.0% | R |  |
| f1c087 | DOUBLE | 69.6% | 0.0 |  |
| xf1c105 | VARCHAR | 36.9% | R |  |
| f1c105 | DOUBLE | 37.2% | 16282814.0 |  |
| xf1c113 | VARCHAR | 36.9% | R |  |
| f1c113 | DOUBLE | 42.3% | 361251.0 |  |
| xf1c114 | VARCHAR | 36.9% | R |  |
| f1c114 | DOUBLE | 42.3% | 755957.0 |  |
| xf1c115 | VARCHAR | 36.9% | R |  |
| f1c115 | DOUBLE | 42.3% | 9009616.0 |  |
| xf1c116 | VARCHAR | 62.4% | R |  |
| f1c116 | DOUBLE | 74.1% | 1328554.0 |  |
| xf1c117 | VARCHAR | 67.0% | R |  |
| f1c117 | DOUBLE | 75.0% | 209369.0 |  |
| xf1c123 | VARCHAR | 36.9% | Z |  |
| f1c123 | DOUBLE | 71.7% | 0.0 |  |
| xf1c124 | VARCHAR | 36.9% | Z |  |
| f1c124 | DOUBLE | 71.7% | 0.0 |  |
| xf1c125 | VARCHAR | 36.9% | Z |  |
| f1c125 | DOUBLE | 71.7% | 0.0 |  |
| xf1c126 | VARCHAR | 62.4% | Z |  |
| f1c126 | DOUBLE | 89.8% | 0.0 |  |
| xf1c127 | VARCHAR | 67.0% | Z |  |
| f1c127 | DOUBLE | 90.1% | 0.0 |  |
| xf1c133 | VARCHAR | 36.9% | Z |  |
| f1c133 | DOUBLE | 71.7% | 0.0 |  |
| xf1c134 | VARCHAR | 36.9% | Z |  |
| f1c134 | DOUBLE | 71.7% | 0.0 |  |
| xf1c135 | VARCHAR | 36.9% | Z |  |
| f1c135 | DOUBLE | 71.7% | 0.0 |  |
| xf1c136 | VARCHAR | 62.4% | Z |  |
| f1c136 | DOUBLE | 89.8% | 0.0 |  |
| xf1c137 | VARCHAR | 67.0% | Z |  |
| f1c137 | DOUBLE | 90.1% | 0.0 |  |
| xf1c143 | VARCHAR | 36.9% | R |  |
| f1c143 | DOUBLE | 36.9% | 0.0 |  |
| xf1c144 | VARCHAR | 36.9% | R |  |
| f1c144 | DOUBLE | 36.9% | 0.0 |  |
| xf1c145 | VARCHAR | 36.9% | R |  |
| f1c145 | DOUBLE | 36.9% | 3143712.0 |  |
| xf1c146 | VARCHAR | 62.4% | R |  |
| f1c146 | DOUBLE | 68.7% | 0.0 |  |
| xf1c147 | VARCHAR | 67.0% | R |  |
| f1c147 | DOUBLE | 69.6% | 0.0 |  |
| xf1c194 | VARCHAR | 36.9% | R |  |
| f1c194 | DOUBLE | 36.9% | 7877214.0 |  |
| xf1c195 | VARCHAR | 36.9% | R |  |
| f1c195 | DOUBLE | 36.9% | 71457081.0 |  |
| xf1c196 | VARCHAR | 76.4% | R |  |
| f1c196 | DOUBLE | 76.4% | 0.0 |  |
| xf1c197 | VARCHAR | 67.0% | R |  |
| f1c197 | DOUBLE | 69.6% | 2181660.0 |  |
| i | INTEGER | 100.0% |  |  |
| xf1a02 | VARCHAR | 65.3% | R |  |
| f1a02 | DOUBLE | 71.3% | 202736045.0 |  |
| xf1a03 | VARCHAR | 65.3% | R |  |
| f1a03 | DOUBLE | 71.3% | 77530882.0 |  |
| xf1a211 | VARCHAR | 65.3% | R |  |
| f1a211 | DOUBLE | 71.3% | 4982207.0 |  |
| xf1a212 | VARCHAR | 65.3% | Z |  |
| f1a212 | DOUBLE | 71.3% | 0.0 |  |
| xf1a213 | VARCHAR | 65.3% | R |  |
| f1a213 | DOUBLE | 71.3% | 0.0 |  |
| xf1a221 | VARCHAR | 65.3% | Z |  |
| f1a221 | DOUBLE | 71.3% | 0.0 |  |
| xf1a222 | VARCHAR | 65.3% | Z |  |
| f1a222 | DOUBLE | 71.3% | 0.0 |  |
| xf1a223 | VARCHAR | 65.3% | Z |  |
| f1a223 | DOUBLE | 71.3% | 0.0 |  |
| xf1a231 | VARCHAR | 65.3% | R |  |
| f1a231 | DOUBLE | 71.3% | 141008356.0 |  |
| xf1a232 | VARCHAR | 65.3% | R |  |
| f1a232 | DOUBLE | 71.3% | 4020956.0 |  |
| xf1a233 | VARCHAR | 65.3% | R |  |
| f1a233 | DOUBLE | 71.3% | 0.0 |  |
| xf1a241 | VARCHAR | 65.3% | R |  |
| f1a241 | DOUBLE | 71.3% | 11306307.0 |  |
| xf1a242 | VARCHAR | 65.3% | R |  |
| f1a242 | DOUBLE | 71.3% | 206979.0 |  |
| xf1a243 | VARCHAR | 65.3% | R |  |
| f1a243 | DOUBLE | 71.3% | 0.0 |  |
| xf1a244 | VARCHAR | 65.3% | R |  |
| f1a244 | DOUBLE | 71.3% | 11513286.0 |  |
| xf1a251 | VARCHAR | 65.3% | R |  |
| f1a251 | DOUBLE | 71.3% | 13806677.0 |  |
| xf1a252 | VARCHAR | 65.3% | R |  |
| f1a252 | DOUBLE | 71.3% | 160376.0 |  |
| xf1a253 | VARCHAR | 65.3% | R |  |
| f1a253 | DOUBLE | 71.3% | 0.0 |  |
| xf1a254 | VARCHAR | 65.3% | R |  |
| f1a254 | DOUBLE | 71.3% | 13967053.0 |  |
| xf1a261 | VARCHAR | 65.3% | R |  |
| f1a261 | DOUBLE | 71.3% | 1883060.0 |  |
| xf1a262 | VARCHAR | 65.3% | Z |  |
| f1a262 | DOUBLE | 71.3% | 0.0 |  |
| xf1a263 | VARCHAR | 65.3% | R |  |
| f1a263 | DOUBLE | 71.3% | 1258149.0 |  |
| xf1a264 | VARCHAR | 65.3% | R |  |
| f1a264 | DOUBLE | 71.3% | 624911.0 |  |
| xf1a271 | VARCHAR | 65.3% | R |  |
| f1a271 | DOUBLE | 71.3% | 12688132.0 |  |
| xf1a272 | VARCHAR | 65.3% | R |  |
| f1a272 | DOUBLE | 71.3% | 14556055.0 |  |
| xf1a273 | VARCHAR | 65.3% | R |  |
| f1a273 | DOUBLE | 71.3% | 0.0 |  |
| xf1a27t1 | VARCHAR | 95.3% | R |  |
| f1a27t1 | DOUBLE | 97.6% | 185674739.0 |  |
| xf1a27t2 | VARCHAR | 95.3% | R |  |
| f1a27t2 | DOUBLE | 97.6% | 18944366.0 |  |
| xf1a27t3 | VARCHAR | 95.3% | R |  |
| f1a27t3 | DOUBLE | 97.6% | 1258149.0 |  |
| xf1a281 | VARCHAR | 65.3% | R |  |
| f1a281 | DOUBLE | 71.3% | 72609889.0 |  |
| xf1a282 | VARCHAR | 65.3% | R |  |
| f1a282 | DOUBLE | 71.3% | 4920993.0 |  |
| xf1a283 | VARCHAR | 65.3% | R |  |
| f1a283 | DOUBLE | 71.3% | 0.0 |  |
| xf1c091 | VARCHAR | 65.3% | R |  |
| f1c091 | DOUBLE | 68.3% | 4920993.0 |  |
| xf1c094 | VARCHAR | 65.3% | R |  |
| f1c094 | DOUBLE | 68.3% | 4920993.0 |  |
| xf1c102 | VARCHAR | 65.3% | A |  |
| f1c102 | DOUBLE | 93.1% | 0.0 |  |
| xf1c103 | VARCHAR | 65.3% | A |  |
| f1c103 | DOUBLE | 93.1% | 0.0 |  |
| xf1c104 | VARCHAR | 65.3% | A |  |
| f1c104 | DOUBLE | 93.1% | 0.0 |  |
| xf1c151 | VARCHAR | 65.3% | R |  |
| f1c151 | DOUBLE | 67.4% | 120384276.0 |  |
| xf1c152 | VARCHAR | 65.3% | R |  |
| f1c152 | DOUBLE | 67.4% | 57236714.0 |  |
| xf1c153 | VARCHAR | 65.3% | R |  |
| f1c153 | DOUBLE | 67.4% | 14981321.0 |  |
| xf1c154 | VARCHAR | 65.3% | R |  |
| f1c154 | DOUBLE | 67.4% | 4920993.0 |  |
| xf1c155 | VARCHAR | 65.3% | R |  |
| f1c155 | DOUBLE | 67.4% | 43245248.0 |  |
| xf1c161 | VARCHAR | 65.3% | R |  |
| f1c161 | DOUBLE | 67.4% | 2593617.0 |  |
| xf1c165 | VARCHAR | 65.3% | R |  |
| f1c165 | DOUBLE | 67.4% | 2593617.0 |  |
| xf1c171 | VARCHAR | 65.3% | R |  |
| f1c171 | DOUBLE | 67.4% | 0.0 |  |
| xf1c172 | VARCHAR | 65.3% | R |  |
| f1c172 | DOUBLE | 67.4% | 0.0 |  |
| xf1c173 | VARCHAR | 65.3% | R |  |
| f1c173 | DOUBLE | 67.4% | 0.0 |  |
| xf1c174 | VARCHAR | 65.3% | R |  |
| f1c174 | DOUBLE | 67.4% | 0.0 |  |
| xf1c175 | VARCHAR | 65.3% | R |  |
| f1c175 | DOUBLE | 67.4% | 0.0 |  |
| xf1c181 | VARCHAR | 65.3% | R |  |
| f1c181 | DOUBLE | 67.4% | 2593617.0 |  |
| xf1c182 | VARCHAR | 65.3% | R |  |
| f1c182 | DOUBLE | 67.4% | 0.0 |  |
| xf1c183 | VARCHAR | 65.3% | R |  |
| f1c183 | DOUBLE | 67.4% | 0.0 |  |
| xf1c184 | VARCHAR | 65.3% | R |  |
| f1c184 | DOUBLE | 67.4% | 0.0 |  |
| xf1c185 | VARCHAR | 65.3% | R |  |
| f1c185 | DOUBLE | 67.4% | 2593617.0 |  |

## f2

Rows: 42,954

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100690 | Primary institution ID, joins across all IPEDS tables |
| xf2a01 | VARCHAR | 0.0% | R |  |
| f2a01 | DOUBLE | 10.1% | 9189852.0 |  |
| xf2a19 | VARCHAR | 30.9% | R |  |
| f2a19 | DOUBLE | 44.2% | 2533200.0 |  |
| xf2a20 | VARCHAR | 30.9% | R |  |
| f2a20 | DOUBLE | 44.2% | 0.0 |  |
| xf2a02 | VARCHAR | 0.0% | R |  |
| f2a02 | DOUBLE | 10.1% | 16559959.0 |  |
| xf2a03 | VARCHAR | 0.0% | R |  |
| f2a03 | DOUBLE | 10.1% | 1052981.0 |  |
| xf2a03a | VARCHAR | 30.9% | R |  |
| f2a03a | DOUBLE | 44.2% | 0.0 |  |
| xf2a04 | VARCHAR | 0.0% | R |  |
| f2a04 | DOUBLE | 10.1% | 15021466.0 |  |
| xf2a05 | VARCHAR | 0.0% | R |  |
| f2a05 | DOUBLE | 10.1% | 485512.0 |  |
| xf2a05a | VARCHAR | 13.3% | R |  |
| f2a05a | DOUBLE | 23.2% | 174864.0 |  |
| xf2a05b | VARCHAR | 30.9% | R |  |
| f2a05b | DOUBLE | 44.2% | 310648.0 |  |
| xf2a06 | VARCHAR | 0.0% | R |  |
| f2a06 | DOUBLE | 10.1% | 15506978.0 |  |
| xf2a11 | VARCHAR | 0.0% | R |  |
| f2a11 | DOUBLE | 10.1% | 1340625.0 |  |
| xf2a12 | VARCHAR | 0.0% | R |  |
| f2a12 | DOUBLE | 10.1% | 1065662.0 |  |
| xf2a13 | VARCHAR | 0.0% | R |  |
| f2a13 | DOUBLE | 10.1% | 3216469.0 |  |
| xf2a15 | VARCHAR | 30.9% | R |  |
| f2a15 | DOUBLE | 44.2% | 0.0 |  |
| xf2a16 | VARCHAR | 30.9% | R |  |
| f2a16 | DOUBLE | 44.2% | 0.0 |  |
| xf2a17 | VARCHAR | 30.9% | R |  |
| f2a17 | DOUBLE | 44.2% | 5622756.0 |  |
| xf2a18 | VARCHAR | 30.9% | R |  |
| f2a18 | DOUBLE | 44.2% | 3089556.0 |  |
| xf2b01 | VARCHAR | 0.0% | R |  |
| f2b01 | DOUBLE | 7.1% | 8572118.0 |  |
| xf2b02 | VARCHAR | 0.0% | R |  |
| f2b02 | DOUBLE | 7.1% | 8056185.0 |  |
| xf2b03 | VARCHAR | 0.0% | R |  |
| f2b03 | DOUBLE | 8.7% | 0.0 |  |
| xf2b04 | VARCHAR | 0.0% | R |  |
| f2b04 | DOUBLE | 9.9% | 515933.0 |  |
| xf2b05 | VARCHAR | 0.0% | R |  |
| f2b05 | DOUBLE | 9.9% | 14991045.0 |  |
| xf2b06 | VARCHAR | 0.0% | R |  |
| f2b06 | DOUBLE | 9.9% | 0.0 |  |
| xf2b07 | VARCHAR | 0.0% | R |  |
| f2b07 | DOUBLE | 9.9% | 15506978.0 |  |
| xf2c01 | VARCHAR | 0.0% | R |  |
| f2c01 | DOUBLE | 0.2% | 1.0 |  |
| xf2c02 | VARCHAR | 0.0% | R |  |
| f2c02 | DOUBLE | 0.2% | 25057.0 |  |
| xf2c03 | VARCHAR | 0.0% | R |  |
| f2c03 | DOUBLE | 0.2% | 0.0 |  |
| xf2c04 | VARCHAR | 0.0% | R |  |
| f2c04 | DOUBLE | 0.2% | 0.0 |  |
| xf2c05 | VARCHAR | 0.0% | R |  |
| f2c05 | DOUBLE | 0.2% | 0.0 |  |
| xf2c06 | VARCHAR | 0.0% | R |  |
| f2c06 | DOUBLE | 0.2% | 783352.0 |  |
| xf2c07 | VARCHAR | 0.0% | R |  |
| f2c07 | DOUBLE | 0.2% | 808410.0 |  |
| xf2c08 | VARCHAR | 0.0% | R |  |
| f2c08 | DOUBLE | 0.2% | 808409.0 |  |
| xf2c09 | VARCHAR | 0.0% | R |  |
| f2c09 | DOUBLE | 0.2% | 0.0 |  |
| xf2c10 | VARCHAR | 65.9% | R |  |
| f2c10 | DOUBLE | 66.0% | 808409.0 |  |
| xf2c12 | VARCHAR | 83.3% | R |  |
| f2c12 | DOUBLE | 83.3% | 0.0 |  |
| xf2c121 | VARCHAR | 83.3% | R |  |
| f2c121 | DOUBLE | 83.3% | 0.0 |  |
| xf2c122 | VARCHAR | 83.3% | R |  |
| f2c122 | DOUBLE | 83.3% | 0.0 |  |
| xf2c13 | VARCHAR | 83.3% | R |  |
| f2c13 | DOUBLE | 83.3% | 25057.0 |  |
| xf2c131 | VARCHAR | 83.3% | R |  |
| f2c131 | DOUBLE | 83.3% | 25057.0 |  |
| xf2c132 | VARCHAR | 83.3% | R |  |
| f2c132 | DOUBLE | 83.3% | 0.0 |  |
| xf2c14 | VARCHAR | 83.3% | R |  |
| f2c14 | DOUBLE | 83.3% | 0.0 |  |
| xf2c141 | VARCHAR | 83.3% | R |  |
| f2c141 | DOUBLE | 83.3% | 0.0 |  |
| xf2c142 | VARCHAR | 83.3% | R |  |
| f2c142 | DOUBLE | 83.3% | 0.0 |  |
| xf2c15 | VARCHAR | 83.3% | R |  |
| f2c15 | DOUBLE | 83.3% | 0.0 |  |
| xf2c151 | VARCHAR | 83.3% | R |  |
| f2c151 | DOUBLE | 83.3% | 0.0 |  |
| xf2c152 | VARCHAR | 83.3% | R |  |
| f2c152 | DOUBLE | 83.3% | 0.0 |  |
| xf2c16 | VARCHAR | 83.3% | R |  |
| f2c16 | DOUBLE | 83.3% | 0.0 |  |
| xf2c161 | VARCHAR | 83.3% | R |  |
| f2c161 | DOUBLE | 83.3% | 0.0 |  |
| xf2c162 | VARCHAR | 83.3% | R |  |
| f2c162 | DOUBLE | 83.3% | 0.0 |  |
| xf2c17 | VARCHAR | 83.3% | R |  |
| f2c17 | DOUBLE | 83.3% | 783352.0 |  |
| xf2c171 | VARCHAR | 83.3% | R |  |
| f2c171 | DOUBLE | 83.3% | 783352.0 |  |
| xf2c172 | VARCHAR | 83.3% | R |  |
| f2c172 | DOUBLE | 83.3% | 0.0 |  |
| xf2d01 | VARCHAR | 0.0% | R |  |
| f2d01 | DOUBLE | 0.0% | 6909429.0 |  |
| xf2d012 | VARCHAR | 30.9% | R |  |
| f2d012 | DOUBLE | 36.3% | 6909429.0 |  |
| xf2d013 | VARCHAR | 30.9% | R |  |
| f2d013 | DOUBLE | 36.3% | 0.0 |  |
| xf2d014 | VARCHAR | 30.9% | R |  |
| f2d014 | DOUBLE | 36.3% | 0.0 |  |
| xf2d02 | VARCHAR | 0.0% | R |  |
| f2d02 | BIGINT | 0.0% | 0 |  |
| xf2d022 | VARCHAR | 30.9% | R |  |
| f2d022 | DOUBLE | 36.3% | 0.0 |  |
| xf2d023 | VARCHAR | 30.9% | R |  |
| f2d023 | DOUBLE | 36.3% | 0.0 |  |
| xf2d024 | VARCHAR | 30.9% | R |  |
| f2d024 | DOUBLE | 36.3% | 0.0 |  |
| xf2d03 | VARCHAR | 0.0% | R |  |
| f2d03 | BIGINT | 0.0% | 0 |  |
| xf2d032 | VARCHAR | 30.9% | R |  |
| f2d032 | DOUBLE | 36.3% | 0.0 |  |
| xf2d033 | VARCHAR | 30.9% | R |  |
| f2d033 | DOUBLE | 36.3% | 0.0 |  |
| xf2d034 | VARCHAR | 30.9% | R |  |
| f2d034 | DOUBLE | 36.3% | 0.0 |  |
| xf2d04 | VARCHAR | 0.0% | R |  |
| f2d04 | BIGINT | 0.0% | 0 |  |
| xf2d042 | VARCHAR | 30.9% | R |  |
| f2d042 | DOUBLE | 36.3% | 0.0 |  |
| xf2d043 | VARCHAR | 30.9% | R |  |
| f2d043 | DOUBLE | 36.3% | 0.0 |  |
| xf2d044 | VARCHAR | 30.9% | R |  |
| f2d044 | DOUBLE | 36.3% | 0.0 |  |
| xf2d05 | VARCHAR | 0.0% | R |  |
| f2d05 | DOUBLE | 0.0% | 25057.0 |  |
| xf2d052 | VARCHAR | 30.9% | R |  |
| f2d052 | DOUBLE | 36.3% | 25057.0 |  |
| xf2d053 | VARCHAR | 30.9% | R |  |
| f2d053 | DOUBLE | 36.3% | 0.0 |  |
| xf2d054 | VARCHAR | 30.9% | R |  |
| f2d054 | DOUBLE | 36.3% | 0.0 |  |
| xf2d06 | VARCHAR | 0.0% | R |  |
| f2d06 | BIGINT | 0.0% | 0 |  |
| xf2d062 | VARCHAR | 30.9% | R |  |
| f2d062 | DOUBLE | 36.3% | 0.0 |  |
| xf2d063 | VARCHAR | 30.9% | R |  |
| f2d063 | DOUBLE | 36.3% | 0.0 |  |
| xf2d064 | VARCHAR | 30.9% | R |  |
| f2d064 | DOUBLE | 36.3% | 0.0 |  |
| xf2d07 | VARCHAR | 0.0% | R |  |
| f2d07 | BIGINT | 0.0% | 0 |  |
| xf2d072 | VARCHAR | 30.9% | R |  |
| f2d072 | DOUBLE | 36.3% | 0.0 |  |
| xf2d073 | VARCHAR | 30.9% | R |  |
| f2d073 | DOUBLE | 36.3% | 0.0 |  |
| xf2d074 | VARCHAR | 30.9% | R |  |
| f2d074 | DOUBLE | 36.3% | 0.0 |  |
| xf2d08 | VARCHAR | 0.0% | R |  |
| f2d08 | DOUBLE | 0.0% | 81096.0 |  |
| xf2d082 | VARCHAR | 30.9% | R |  |
| f2d082 | DOUBLE | 36.3% | 81096.0 |  |
| xf2d083 | VARCHAR | 30.9% | R |  |
| f2d083 | DOUBLE | 36.3% | 0.0 |  |
| xf2d084 | VARCHAR | 30.9% | R |  |
| f2d084 | DOUBLE | 36.3% | 0.0 |  |
| xf2d08a | VARCHAR | 30.9% | R |  |
| f2d08a | DOUBLE | 36.3% | 81096.0 |  |
| xf2d082a | VARCHAR | 30.9% | R |  |
| f2d082a | DOUBLE | 36.3% | 81096.0 |  |
| xf2d083a | VARCHAR | 30.9% | R |  |
| f2d083a | DOUBLE | 36.3% | 0.0 |  |
| xf2d084a | VARCHAR | 30.9% | R |  |
| f2d084a | DOUBLE | 36.3% | 0.0 |  |
| xf2d08b | VARCHAR | 30.9% | R |  |
| f2d08b | DOUBLE | 36.3% | 0.0 |  |
| xf2d082b | VARCHAR | 30.9% | R |  |
| f2d082b | DOUBLE | 36.3% | 0.0 |  |
| xf2d083b | VARCHAR | 30.9% | R |  |
| f2d083b | DOUBLE | 36.3% | 0.0 |  |
| xf2d084b | VARCHAR | 30.9% | R |  |
| f2d084b | DOUBLE | 36.3% | 0.0 |  |
| xf2d09 | VARCHAR | 0.0% | R |  |
| f2d09 | BIGINT | 0.0% | 0 |  |
| xf2d092 | VARCHAR | 30.9% | R |  |
| f2d092 | DOUBLE | 36.3% | 0.0 |  |
| xf2d093 | VARCHAR | 30.9% | R |  |
| f2d093 | DOUBLE | 36.3% | 0.0 |  |
| xf2d094 | VARCHAR | 30.9% | R |  |
| f2d094 | DOUBLE | 36.3% | 0.0 |  |
| xf2d10 | VARCHAR | 0.0% | R |  |
| f2d10 | DOUBLE | 0.0% | 8707.0 |  |
| xf2d102 | VARCHAR | 30.9% | R |  |
| f2d102 | DOUBLE | 36.3% | 18667.0 |  |
| xf2d103 | VARCHAR | 30.9% | R |  |
| f2d103 | DOUBLE | 36.3% | -9960.0 |  |
| xf2d104 | VARCHAR | 30.9% | R |  |
| f2d104 | DOUBLE | 36.3% | 0.0 |  |
| xf2d11 | VARCHAR | 0.0% | R |  |
| f2d11 | DOUBLE | 0.0% | 0.0 |  |
| xf2d112 | VARCHAR | 30.9% | R |  |
| f2d112 | DOUBLE | 36.3% | 0.0 |  |
| xf2d12 | VARCHAR | 0.0% | R |  |
| f2d12 | DOUBLE | 5.3% | 0.0 |  |
| xf2d122 | VARCHAR | 30.9% | R |  |
| f2d122 | DOUBLE | 41.6% | 0.0 |  |
| xf2d13 | VARCHAR | 0.0% | R |  |
| f2d13 | DOUBLE | 11.7% | 0.0 |  |
| xf2d132 | VARCHAR | 30.9% | R |  |
| f2d132 | DOUBLE | 45.0% | 0.0 |  |
| xf2d14 | VARCHAR | 0.0% | R |  |
| f2d14 | DOUBLE | 11.7% | 0.0 |  |
| xf2d142 | VARCHAR | 30.9% | R |  |
| f2d142 | DOUBLE | 45.0% | 0.0 |  |
| xf2d143 | VARCHAR | 30.9% | R |  |
| f2d143 | DOUBLE | 45.0% | 0.0 |  |
| xf2d144 | VARCHAR | 30.9% | R |  |
| f2d144 | DOUBLE | 45.0% | 0.0 |  |
| xf2d15 | VARCHAR | 0.0% | R |  |
| f2d15 | DOUBLE | 0.0% | 1547829.0 |  |
| xf2d152 | VARCHAR | 30.9% | R |  |
| f2d152 | DOUBLE | 36.3% | 1537869.0 |  |
| xf2d153 | VARCHAR | 30.9% | R |  |
| f2d153 | DOUBLE | 36.3% | 9960.0 |  |
| xf2d154 | VARCHAR | 30.9% | R |  |
| f2d154 | DOUBLE | 36.3% | 0.0 |  |
| xf2d16 | VARCHAR | 0.0% | R |  |
| f2d16 | DOUBLE | 0.0% | 8572118.0 |  |
| xf2d162 | VARCHAR | 30.9% | R |  |
| f2d162 | DOUBLE | 36.3% | 8572118.0 |  |
| xf2d163 | VARCHAR | 30.9% | Z |  |
| f2d163 | DOUBLE | 36.3% | 0.0 |  |
| xf2d164 | VARCHAR | 30.9% | Z |  |
| f2d164 | DOUBLE | 36.3% | 0.0 |  |
| xf2d17 | VARCHAR | 48.3% | R |  |
| f2d17 | DOUBLE | 48.3% | 0.0 |  |
| xf2d172 | VARCHAR | 30.9% | R |  |
| f2d172 | DOUBLE | 36.3% | 0.0 |  |
| xf2d173 | VARCHAR | 30.9% | Z |  |
| f2d173 | DOUBLE | 36.3% | 0.0 |  |
| xf2d174 | VARCHAR | 35.2% | Z |  |
| f2d174 | DOUBLE | 37.5% | 0.0 |  |
| xf2d18 | VARCHAR | 35.2% | R |  |
| f2d18 | DOUBLE | 37.5% | 8572118.0 |  |
| xf2d182 | VARCHAR | 30.9% | R |  |
| f2d182 | DOUBLE | 36.3% | 8572118.0 |  |
| xf2d183 | VARCHAR | 30.9% | R |  |
| f2d183 | DOUBLE | 36.3% | 0.0 |  |
| xf2d184 | VARCHAR | 30.9% | R |  |
| f2d184 | DOUBLE | 36.3% | 0.0 |  |
| xf2e011 | VARCHAR | 0.0% | R |  |
| f2e011 | DOUBLE | 0.0% | 2727802.0 |  |
| xf2e012 | VARCHAR | 0.0% | R |  |
| f2e012 | DOUBLE | 0.0% | 2031937.0 |  |
| xf2e021 | VARCHAR | 0.0% | R |  |
| f2e021 | DOUBLE | 0.0% | 0.0 |  |
| xf2e022 | VARCHAR | 0.0% | R |  |
| f2e022 | DOUBLE | 0.0% | 0.0 |  |
| xf2e031 | VARCHAR | 0.0% | R |  |
| f2e031 | DOUBLE | 0.0% | 0.0 |  |
| xf2e032 | VARCHAR | 0.0% | R |  |
| f2e032 | DOUBLE | 0.0% | 0.0 |  |
| xf2e041 | VARCHAR | 0.0% | R |  |
| f2e041 | DOUBLE | 0.0% | 749081.0 |  |
| xf2e042 | VARCHAR | 0.0% | R |  |
| f2e042 | DOUBLE | 0.0% | 530094.0 |  |
| xf2e051 | VARCHAR | 0.0% | R |  |
| f2e051 | DOUBLE | 0.0% | 1226404.0 |  |
| xf2e052 | VARCHAR | 0.0% | R |  |
| f2e052 | DOUBLE | 0.0% | 927226.0 |  |
| xf2e061 | VARCHAR | 0.0% | R |  |
| f2e061 | DOUBLE | 0.0% | 3352898.0 |  |
| xf2e062 | VARCHAR | 0.0% | R |  |
| f2e062 | DOUBLE | 0.0% | 1165558.0 |  |
| xf2e071 | VARCHAR | 0.0% | R |  |
| f2e071 | DOUBLE | 5.3% | 0.0 |  |
| xf2e072 | VARCHAR | 0.0% | R |  |
| f2e072 | DOUBLE | 5.3% | 0.0 |  |
| xf2e081 | VARCHAR | 0.0% | R |  |
| f2e081 | DOUBLE | 0.0% | 0.0 |  |
| xf2e091 | VARCHAR | 0.0% | R |  |
| f2e091 | DOUBLE | 11.7% | 0.0 |  |
| xf2e092 | VARCHAR | 0.0% | R |  |
| f2e092 | DOUBLE | 11.7% | 0.0 |  |
| xf2e101 | VARCHAR | 0.0% | R |  |
| f2e101 | DOUBLE | 11.7% | 0.0 |  |
| xf2e102 | VARCHAR | 0.0% | R |  |
| f2e102 | DOUBLE | 11.7% | 0.0 |  |
| xf2e121 | VARCHAR | 0.0% | R |  |
| f2e121 | DOUBLE | 0.0% | 0.0 |  |
| xf2e122 | VARCHAR | 0.0% | R |  |
| f2e122 | DOUBLE | 0.0% | 0.0 |  |
| xf2e131 | VARCHAR | 4.4% | R |  |
| f2e131 | DOUBLE | 4.4% | 8056185.0 |  |
| xf2e132 | VARCHAR | 4.4% | R |  |
| f2e132 | DOUBLE | 4.4% | 4654815.0 |  |
| xf2e133 | VARCHAR | 4.4% | R |  |
| f2e133 | DOUBLE | 4.4% | 576595.0 |  |
| xf2e134 | VARCHAR | 4.4% | R |  |
| f2e134 | DOUBLE | 13.3% | 147762.0 |  |
| xf2e135 | VARCHAR | 4.4% | R |  |
| f2e135 | DOUBLE | 4.4% | 186465.0 |  |
| xf2e136 | VARCHAR | 4.4% | R |  |
| f2e136 | DOUBLE | 4.4% | 0.0 |  |
| xf2e137 | VARCHAR | 4.4% | R |  |
| f2e137 | DOUBLE | 4.4% | 2490548.0 |  |
| f2fha | DOUBLE | 8.8% | 1.0 |  |
| xf2h01 | VARCHAR | 8.8% | R |  |
| f2h01 | DOUBLE | 32.0% | 174819.0 |  |
| xf2h02 | VARCHAR | 8.8% | R |  |
| f2h02 | DOUBLE | 32.0% | 174864.0 |  |
| xf2h03 | VARCHAR | 83.3% | R |  |
| f2h03 | DOUBLE | 87.5% | 45.0 |  |
| xf2h03a | VARCHAR | 83.3% | R |  |
| f2h03a | DOUBLE | 87.5% | 0.0 |  |
| xf2h03b | VARCHAR | 83.3% | R |  |
| f2h03b | DOUBLE | 87.5% | 0.0 |  |
| xf2h03c | VARCHAR | 83.3% | R |  |
| f2h03c | DOUBLE | 87.5% | 0.0 |  |
| xf2h03d | VARCHAR | 83.3% | R |  |
| f2h03d | DOUBLE | 87.5% | 45.0 |  |
| xf2i01 | VARCHAR | 83.3% | R |  |
| f2i01 | DOUBLE | 85.1% | 525847.0 |  |
| xf2i02 | VARCHAR | 83.3% | R |  |
| f2i02 | DOUBLE | 85.1% | 8582078.0 |  |
| xf2i03 | VARCHAR | 83.3% | R |  |
| f2i03 | DOUBLE | 85.1% | 515933.0 |  |
| xf2i04 | VARCHAR | 83.3% | R |  |
| f2i04 | DOUBLE | 85.1% | 14991045.0 |  |
| xf2i05 | VARCHAR | 83.3% | R |  |
| f2i05 | DOUBLE | 85.1% | 15506978.0 |  |
| xf2i06 | VARCHAR | 83.3% | R |  |
| f2i06 | DOUBLE | 85.1% | 0.0 |  |
| xf2i07 | VARCHAR | 83.3% | R |  |
| f2i07 | DOUBLE | 85.1% | 8056185.0 |  |
| year | BIGINT | 0.0% | 2023 | Appears in 26 tables, common join key |
| xf2e013 | VARCHAR | 38.5% | R |  |
| f2e013 | DOUBLE | 38.5% | 290086.0 |  |
| xf2e014 | VARCHAR | 38.5% | R |  |
| f2e014 | DOUBLE | 38.5% | 136772.0 |  |
| xf2e015 | VARCHAR | 38.5% | R |  |
| f2e015 | DOUBLE | 38.5% | 0.0 |  |
| xf2e016 | VARCHAR | 38.5% | R |  |
| f2e016 | DOUBLE | 38.5% | 0.0 |  |
| xf2e017 | VARCHAR | 38.5% | R |  |
| f2e017 | DOUBLE | 38.5% | 657663.0 |  |
| xf2e023 | VARCHAR | 38.5% | R |  |
| f2e023 | DOUBLE | 38.5% | 0.0 |  |
| xf2e024 | VARCHAR | 38.5% | R |  |
| f2e024 | DOUBLE | 38.5% | 0.0 |  |
| xf2e025 | VARCHAR | 38.5% | R |  |
| f2e025 | DOUBLE | 38.5% | 0.0 |  |
| xf2e026 | VARCHAR | 38.5% | R |  |
| f2e026 | DOUBLE | 38.5% | 0.0 |  |
| xf2e027 | VARCHAR | 38.5% | R |  |
| f2e027 | DOUBLE | 38.5% | 0.0 |  |
| xf2e033 | VARCHAR | 38.5% | R |  |
| f2e033 | DOUBLE | 38.5% | 0.0 |  |
| xf2e034 | VARCHAR | 38.5% | R |  |
| f2e034 | DOUBLE | 38.5% | 0.0 |  |
| xf2e035 | VARCHAR | 38.5% | R |  |
| f2e035 | DOUBLE | 38.5% | 0.0 |  |
| xf2e036 | VARCHAR | 38.5% | R |  |
| f2e036 | DOUBLE | 38.5% | 0.0 |  |
| xf2e037 | VARCHAR | 38.5% | R |  |
| f2e037 | DOUBLE | 38.5% | 0.0 |  |
| xf2e043 | VARCHAR | 38.5% | R |  |
| f2e043 | DOUBLE | 38.5% | 7110.0 |  |
| xf2e044 | VARCHAR | 38.5% | R |  |
| f2e044 | DOUBLE | 38.5% | 13026.0 |  |
| xf2e045 | VARCHAR | 38.5% | R |  |
| f2e045 | DOUBLE | 38.5% | 0.0 |  |
| xf2e046 | VARCHAR | 38.5% | R |  |
| f2e046 | DOUBLE | 38.5% | 0.0 |  |
| xf2e047 | VARCHAR | 38.5% | R |  |
| f2e047 | DOUBLE | 38.5% | 37276.0 |  |
| xf2e053 | VARCHAR | 38.5% | R |  |
| f2e053 | DOUBLE | 38.5% | 80342.0 |  |
| xf2e054 | VARCHAR | 38.5% | R |  |
| f2e054 | DOUBLE | 38.5% | 35821.0 |  |
| xf2e055 | VARCHAR | 38.5% | R |  |
| f2e055 | DOUBLE | 38.5% | 0.0 |  |
| xf2e056 | VARCHAR | 38.5% | R |  |
| f2e056 | DOUBLE | 38.5% | 0.0 |  |
| xf2e057 | VARCHAR | 38.5% | R |  |
| f2e057 | DOUBLE | 38.5% | 74073.0 |  |
| xf2e063 | VARCHAR | 38.5% | R |  |
| f2e063 | DOUBLE | 38.5% | 510128.0 |  |
| xf2e064 | VARCHAR | 38.5% | R |  |
| f2e064 | DOUBLE | 38.5% | 140028.0 |  |
| xf2e065 | VARCHAR | 38.5% | R |  |
| f2e065 | DOUBLE | 38.5% | 139849.0 |  |
| xf2e066 | VARCHAR | 38.5% | R |  |
| f2e066 | DOUBLE | 38.5% | 118216.0 |  |
| xf2e067 | VARCHAR | 38.5% | R |  |
| f2e067 | DOUBLE | 38.5% | 2328503.0 |  |
| xf2e073 | VARCHAR | 38.5% | R |  |
| f2e073 | DOUBLE | 41.5% | 0.0 |  |
| xf2e074 | VARCHAR | 38.5% | R |  |
| f2e074 | DOUBLE | 41.5% | 0.0 |  |
| xf2e075 | VARCHAR | 38.5% | R |  |
| f2e075 | DOUBLE | 41.5% | 0.0 |  |
| xf2e076 | VARCHAR | 38.5% | R |  |
| f2e076 | DOUBLE | 41.5% | 0.0 |  |
| xf2e077 | VARCHAR | 38.5% | R |  |
| f2e077 | DOUBLE | 41.5% | 0.0 |  |
| xf2e087 | VARCHAR | 38.5% | R |  |
| f2e087 | DOUBLE | 38.5% | 0.0 |  |
| xf2e093 | VARCHAR | 38.5% | R |  |
| f2e093 | DOUBLE | 46.1% | 0.0 |  |
| xf2e094 | VARCHAR | 38.5% | R |  |
| f2e094 | DOUBLE | 46.1% | 0.0 |  |
| xf2e095 | VARCHAR | 38.5% | R |  |
| f2e095 | DOUBLE | 46.1% | 0.0 |  |
| xf2e096 | VARCHAR | 38.5% | R |  |
| f2e096 | DOUBLE | 46.1% | 0.0 |  |
| xf2e097 | VARCHAR | 38.5% | R |  |
| f2e097 | DOUBLE | 46.1% | 0.0 |  |
| xf2e103 | VARCHAR | 38.5% | R |  |
| f2e103 | DOUBLE | 46.1% | 0.0 |  |
| xf2e104 | VARCHAR | 38.5% | R |  |
| f2e104 | DOUBLE | 46.1% | 0.0 |  |
| xf2e105 | VARCHAR | 38.5% | R |  |
| f2e105 | DOUBLE | 46.1% | 0.0 |  |
| xf2e106 | VARCHAR | 38.5% | R |  |
| f2e106 | DOUBLE | 46.1% | 0.0 |  |
| xf2e107 | VARCHAR | 38.5% | R |  |
| f2e107 | DOUBLE | 46.1% | 0.0 |  |
| xf2e111 | VARCHAR | 34.1% | R |  |
| f2e111 | DOUBLE | 42.9% | 0.0 |  |
| xf2e112 | VARCHAR | 34.1% | R |  |
| f2e112 | DOUBLE | 34.1% | 0.0 |  |
| xf2e113 | VARCHAR | 38.5% | R |  |
| f2e113 | DOUBLE | 38.5% | 0.0 |  |
| xf2e114 | VARCHAR | 38.5% | R |  |
| f2e114 | DOUBLE | 38.5% | -325647.0 |  |
| xf2e115 | VARCHAR | 38.5% | R |  |
| f2e115 | DOUBLE | 38.5% | 0.0 |  |
| xf2e116 | VARCHAR | 38.5% | R |  |
| f2e116 | DOUBLE | 38.5% | 0.0 |  |
| xf2e117 | VARCHAR | 38.5% | R |  |
| f2e117 | DOUBLE | 38.5% | 325647.0 |  |
| xf2e123 | VARCHAR | 38.5% | R |  |
| f2e123 | DOUBLE | 38.5% | 0.0 |  |
| xf2e124 | VARCHAR | 38.5% | R |  |
| f2e124 | DOUBLE | 38.5% | 0.0 |  |
| xf2e125 | VARCHAR | 38.5% | R |  |
| f2e125 | DOUBLE | 38.5% | 0.0 |  |
| xf2e126 | VARCHAR | 38.5% | R |  |
| f2e126 | DOUBLE | 38.5% | 0.0 |  |
| xf2e127 | VARCHAR | 38.5% | R |  |
| f2e127 | DOUBLE | 38.5% | 0.0 |  |
| i | INTEGER | 100.0% |  |  |
| xf2a14 | VARCHAR | 60.4% | Z |  |
| f2a14 | DOUBLE | 65.8% | 0.0 |  |
| xf2e082 | VARCHAR | 60.4% | A |  |
| f2e082 | DOUBLE | 86.7% | 0.0 |  |
| xf2e083 | VARCHAR | 64.8% | A |  |
| f2e083 | DOUBLE | 91.1% | 0.0 |  |
| xf2e084 | VARCHAR | 64.8% | A |  |
| f2e084 | DOUBLE | 91.1% | 0.0 |  |
| xf2e085 | VARCHAR | 64.8% | A |  |
| f2e085 | DOUBLE | 91.1% | 0.0 |  |
| xf2e086 | VARCHAR | 64.8% | A |  |
| f2e086 | DOUBLE | 91.1% | 0.0 |  |
| xf2e141 | VARCHAR | 95.6% | R |  |
| f2e141 | DOUBLE | 95.6% | 269211.0 |  |
| xf2e151 | VARCHAR | 95.6% | R |  |
| f2e151 | DOUBLE | 95.6% | 131249.0 |  |
| xf2e161 | VARCHAR | 95.6% | R |  |
| f2e161 | DOUBLE | 95.6% | 79703.0 |  |
| xf2e171 | VARCHAR | 95.6% | R |  |
| f2e171 | DOUBLE | 95.6% | 1010784.0 |  |

## f3

Rows: 59,487

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 101116 | Primary institution ID, joins across all IPEDS tables |
| xf3a01 | VARCHAR | 0.0% | R |  |
| f3a01 | DOUBLE | 50.9% | 7370956.0 |  |
| xf3a01a | VARCHAR | 58.1% | R |  |
| f3a01a | DOUBLE | 88.8% | 0.0 |  |
| xf3a01b | VARCHAR | 58.1% | R |  |
| f3a01b | DOUBLE | 88.8% | 661625.0 |  |
| xf3a01c | VARCHAR | 58.1% | R |  |
| f3a01c | DOUBLE | 88.8% | 0.0 |  |
| xf3a02 | VARCHAR | 0.0% | R |  |
| f3a02 | DOUBLE | 50.9% | 5297552.0 |  |
| xf3a02a | VARCHAR | 58.1% | R |  |
| f3a02a | DOUBLE | 88.8% | 0.0 |  |
| xf3a03 | VARCHAR | 0.0% | R |  |
| f3a03 | DOUBLE | 50.9% | 2073404.0 |  |
| xf3a04 | VARCHAR | 0.0% | R |  |
| f3a04 | DOUBLE | 50.9% | 7370956.0 |  |
| xf3a05 | VARCHAR | 58.1% | R |  |
| f3a05 | DOUBLE | 88.8% | 0.0 |  |
| xf3a06 | VARCHAR | 58.1% | R |  |
| f3a06 | DOUBLE | 88.8% | 1286537.0 |  |
| xf3a07 | VARCHAR | 58.1% | R |  |
| f3a07 | DOUBLE | 88.8% | 414363.0 |  |
| xf3a08 | VARCHAR | 58.1% | R |  |
| f3a08 | DOUBLE | 88.8% | 0.0 |  |
| xf3a09 | VARCHAR | 58.1% | R |  |
| f3a09 | DOUBLE | 88.8% | 134740.0 |  |
| xf3a10 | VARCHAR | 58.1% | R |  |
| f3a10 | DOUBLE | 88.8% | 1835640.0 |  |
| xf3a11 | VARCHAR | 58.1% | R |  |
| f3a11 | DOUBLE | 88.8% | 1174015.0 |  |
| xf3a12 | VARCHAR | 58.1% | R |  |
| f3a12 | DOUBLE | 88.8% | 661625.0 |  |
| xf3b01 | VARCHAR | 0.0% | R |  |
| f3b01 | DOUBLE | 42.1% | 6871924.0 |  |
| xf3b02 | VARCHAR | 0.0% | R |  |
| f3b02 | DOUBLE | 42.1% | 6947979.0 |  |
| xf3b03 | VARCHAR | 0.0% | R |  |
| f3b03 | DOUBLE | 50.7% | 0.0 |  |
| xf3b04 | VARCHAR | 0.0% | R |  |
| f3b04 | DOUBLE | 50.7% | -76055.0 |  |
| xf3b05 | VARCHAR | 0.0% | R |  |
| f3b05 | DOUBLE | 51.3% | -377678.0 |  |
| xf3b06 | VARCHAR | 0.0% | R |  |
| f3b06 | DOUBLE | 50.7% | 2527137.0 |  |
| xf3b07 | VARCHAR | 0.0% | R |  |
| f3b07 | DOUBLE | 50.7% | 0.0 |  |
| xf3b08 | VARCHAR | 0.0% | R |  |
| f3b08 | DOUBLE | 50.7% | 2073404.0 |  |
| xf3c01 | VARCHAR | 0.0% | R |  |
| f3c01 | DOUBLE | 0.2% | 1570774.0 |  |
| xf3c02 | VARCHAR | 0.0% | R |  |
| f3c02 | DOUBLE | 0.2% | 748663.0 |  |
| xf3c03 | VARCHAR | 0.0% | R |  |
| f3c03 | DOUBLE | 0.2% | 167479.0 |  |
| xf3c03a | VARCHAR | 58.1% | R |  |
| f3c03a | DOUBLE | 58.2% | 167479.0 |  |
| xf3c03b | VARCHAR | 58.1% | R |  |
| f3c03b | DOUBLE | 58.2% | 0.0 |  |
| xf3c04 | VARCHAR | 0.0% | R |  |
| f3c04 | DOUBLE | 0.2% | 912724.0 |  |
| xf3c05 | VARCHAR | 0.0% | R |  |
| f3c05 | DOUBLE | 0.2% | 3399640.0 |  |
| xf3c06 | VARCHAR | 0.0% | R |  |
| f3c06 | DOUBLE | 0.2% | 0.0 |  |
| xf3c07 | VARCHAR | 0.0% | R |  |
| f3c07 | DOUBLE | 0.2% | 0.0 |  |
| xf3c08 | VARCHAR | 68.5% | R |  |
| f3c08 | DOUBLE | 68.6% | 0.0 |  |
| xf3c12 | VARCHAR | 85.5% | R |  |
| f3c12 | DOUBLE | 85.5% | 0.0 |  |
| xf3c121 | VARCHAR | 85.5% | R |  |
| f3c121 | DOUBLE | 85.5% | 0.0 |  |
| xf3c122 | VARCHAR | 85.5% | R |  |
| f3c122 | DOUBLE | 85.5% | 0.0 |  |
| xf3c13 | VARCHAR | 85.5% | R |  |
| f3c13 | DOUBLE | 85.5% | 0.0 |  |
| xf3c131 | VARCHAR | 85.5% | R |  |
| f3c131 | DOUBLE | 85.5% | 0.0 |  |
| xf3c132 | VARCHAR | 85.5% | R |  |
| f3c132 | DOUBLE | 85.5% | 0.0 |  |
| xf3c14 | VARCHAR | 85.5% | R |  |
| f3c14 | DOUBLE | 85.5% | 0.0 |  |
| xf3c141 | VARCHAR | 85.5% | R |  |
| f3c141 | DOUBLE | 85.5% | 0.0 |  |
| xf3c142 | VARCHAR | 85.5% | R |  |
| f3c142 | DOUBLE | 85.5% | 0.0 |  |
| xf3c15 | VARCHAR | 85.5% | R |  |
| f3c15 | DOUBLE | 85.5% | 0.0 |  |
| xf3c151 | VARCHAR | 85.5% | R |  |
| f3c151 | DOUBLE | 85.5% | 0.0 |  |
| xf3c152 | VARCHAR | 85.5% | R |  |
| f3c152 | DOUBLE | 85.5% | 0.0 |  |
| xf3c16 | VARCHAR | 85.5% | R |  |
| f3c16 | DOUBLE | 85.5% | 0.0 |  |
| xf3c161 | VARCHAR | 85.5% | R |  |
| f3c161 | DOUBLE | 85.5% | 0.0 |  |
| xf3c162 | VARCHAR | 85.5% | R |  |
| f3c162 | DOUBLE | 85.5% | 0.0 |  |
| xf3c17 | VARCHAR | 85.5% | R |  |
| f3c17 | DOUBLE | 85.5% | 0.0 |  |
| xf3c171 | VARCHAR | 85.5% | R |  |
| f3c171 | DOUBLE | 85.5% | 0.0 |  |
| xf3c172 | VARCHAR | 85.5% | R |  |
| f3c172 | DOUBLE | 85.5% | 0.0 |  |
| xf3d01 | VARCHAR | 0.0% | R |  |
| f3d01 | DOUBLE | 0.1% | 4266624.0 |  |
| xf3d02 | VARCHAR | 0.0% | R |  |
| f3d02 | DOUBLE | 0.1% | 2319437.0 |  |
| xf3d02a | VARCHAR | 58.1% | R |  |
| f3d02a | DOUBLE | 58.1% | 0.0 |  |
| xf3d02b | VARCHAR | 58.1% | R |  |
| f3d02b | DOUBLE | 58.1% | 2319437.0 |  |
| xf3d03 | VARCHAR | 0.0% | R |  |
| f3d03 | DOUBLE | 0.1% | 167479.0 |  |
| xf3d03a | VARCHAR | 58.1% | R |  |
| f3d03a | DOUBLE | 58.1% | 0.0 |  |
| xf3d03b | VARCHAR | 58.1% | R |  |
| f3d03b | DOUBLE | 58.1% | 167479.0 |  |
| xf3d03c | VARCHAR | 58.1% | R |  |
| f3d03c | DOUBLE | 58.1% | 0.0 |  |
| xf3d03d | VARCHAR | 58.1% | R |  |
| f3d03d | DOUBLE | 58.1% | 0.0 |  |
| xf3d04 | VARCHAR | 0.0% | R |  |
| f3d04 | DOUBLE | 0.1% | 0.0 |  |
| xf3d05 | VARCHAR | 0.0% | R |  |
| f3d05 | DOUBLE | 0.1% | 0.0 |  |
| xf3d06 | VARCHAR | 0.0% | R |  |
| f3d06 | DOUBLE | 0.1% | 0.0 |  |
| xf3d07 | VARCHAR | 0.0% | R |  |
| f3d07 | DOUBLE | 43.0% | 101753.0 |  |
| xf3d12 | VARCHAR | 58.1% | R |  |
| f3d12 | DOUBLE | 92.9% | 0.0 |  |
| xf3d08 | VARCHAR | 0.0% | R |  |
| f3d08 | DOUBLE | 0.1% | 16631.0 |  |
| xf3d09 | VARCHAR | 0.0% | R |  |
| f3d09 | DOUBLE | 0.1% | 6871924.0 |  |
| xf3e011 | VARCHAR | 58.1% | R |  |
| f3e011 | DOUBLE | 58.1% | 2659323.0 |  |
| xf3e012 | VARCHAR | 58.1% | R |  |
| f3e012 | DOUBLE | 58.1% | 1416569.0 |  |
| xf3e02a1 | VARCHAR | 58.1% | R |  |
| f3e02a1 | DOUBLE | 58.1% | 0.0 |  |
| xf3e02a2 | VARCHAR | 58.1% | R |  |
| f3e02a2 | DOUBLE | 58.1% | 0.0 |  |
| xf3e02b1 | VARCHAR | 58.1% | R |  |
| f3e02b1 | DOUBLE | 58.1% | 0.0 |  |
| xf3e02b2 | VARCHAR | 58.1% | R |  |
| f3e02b2 | DOUBLE | 58.1% | 0.0 |  |
| xf3e03a1 | VARCHAR | 58.1% | R |  |
| f3e03a1 | DOUBLE | 58.1% | 316858.0 |  |
| xf3e03a2 | VARCHAR | 58.1% | R |  |
| f3e03a2 | DOUBLE | 58.1% | 241211.0 |  |
| xf3e03b1 | VARCHAR | 58.1% | R |  |
| f3e03b1 | DOUBLE | 58.1% | 828649.0 |  |
| xf3e03b2 | VARCHAR | 58.1% | R |  |
| f3e03b2 | DOUBLE | 58.1% | 714800.0 |  |
| xf3e03c1 | VARCHAR | 58.1% | R |  |
| f3e03c1 | DOUBLE | 58.1% | 2944986.0 |  |
| xf3e03c2 | VARCHAR | 58.1% | R |  |
| f3e03c2 | DOUBLE | 58.1% | 133604.0 |  |
| xf3e041 | VARCHAR | 58.1% | R |  |
| f3e041 | DOUBLE | 85.7% | 0.0 |  |
| xf3e042 | VARCHAR | 58.1% | R |  |
| f3e042 | DOUBLE | 85.7% | 0.0 |  |
| xf3e051 | VARCHAR | 58.1% | R |  |
| f3e051 | DOUBLE | 58.1% | 0.0 |  |
| xf3e101 | VARCHAR | 58.1% | R |  |
| f3e101 | DOUBLE | 92.9% | 0.0 |  |
| xf3e102 | VARCHAR | 58.1% | R |  |
| f3e102 | DOUBLE | 92.9% | 0.0 |  |
| xf3e061 | VARCHAR | 58.1% | R |  |
| f3e061 | DOUBLE | 58.1% | 198163.0 |  |
| xf3e062 | VARCHAR | 58.1% | R |  |
| f3e062 | DOUBLE | 58.1% | 0.0 |  |
| xf3e071 | VARCHAR | 58.1% | R |  |
| f3e071 | DOUBLE | 58.1% | 6947979.0 |  |
| xf3e072 | VARCHAR | 58.1% | R |  |
| f3e072 | DOUBLE | 58.1% | 2506184.0 |  |
| xf3e073 | VARCHAR | 58.1% | R |  |
| f3e073 | DOUBLE | 58.1% | 165626.0 |  |
| xf3e074 | VARCHAR | 68.5% | R |  |
| f3e074 | DOUBLE | 68.5% | 1400584.0 |  |
| xf3e075 | VARCHAR | 58.1% | R |  |
| f3e075 | DOUBLE | 58.1% | 198162.0 |  |
| xf3e076 | VARCHAR | 58.1% | R |  |
| f3e076 | DOUBLE | 58.1% | 0.0 |  |
| xf3e077 | VARCHAR | 58.1% | R |  |
| f3e077 | DOUBLE | 58.1% | 2677423.0 |  |
| xf3f01 | VARCHAR | 58.1% | R |  |
| f3f01 | DOUBLE | 93.1% | 0.0 |  |
| xf3f02 | VARCHAR | 58.1% | R |  |
| f3f02 | DOUBLE | 93.1% | 0.0 |  |
| f3f03 | DOUBLE | 58.1% | 1.0 |  |
| xf3g01 | VARCHAR | 85.5% | R |  |
| f3g01 | DOUBLE | 96.5% | -76054.0 |  |
| xf3g02 | VARCHAR | 85.5% | R |  |
| f3g02 | DOUBLE | 96.5% | 6871924.0 |  |
| xf3g03 | VARCHAR | 85.5% | R |  |
| f3g03 | DOUBLE | 96.5% | 2073404.0 |  |
| xf3g04 | VARCHAR | 85.5% | R |  |
| f3g04 | DOUBLE | 96.5% | 7370956.0 |  |
| xf3g05 | VARCHAR | 85.5% | R |  |
| f3g05 | DOUBLE | 96.5% | 1411779.0 |  |
| xf3g06 | VARCHAR | 85.5% | R |  |
| f3g06 | DOUBLE | 96.5% | 0.0 |  |
| xf3g07 | VARCHAR | 85.5% | R |  |
| f3g07 | DOUBLE | 96.5% | 6947979.0 |  |
| year | BIGINT | 0.0% | 2023 | Appears in 26 tables, common join key |
| xf3e013 | VARCHAR | 89.6% | R |  |
| f3e013 | DOUBLE | 89.6% | 276572.0 |  |
| xf3e014 | VARCHAR | 89.6% | R |  |
| f3e014 | DOUBLE | 89.6% | 466612.0 |  |
| xf3e015 | VARCHAR | 89.6% | R |  |
| f3e015 | DOUBLE | 89.6% | 147895.0 |  |
| xf3e016 | VARCHAR | 89.6% | Z |  |
| f3e016 | DOUBLE | 89.6% | 0.0 |  |
| xf3e017 | VARCHAR | 89.6% | R |  |
| f3e017 | DOUBLE | 89.6% | 512928.0 |  |
| xf3e02a3 | VARCHAR | 89.6% | Z |  |
| f3e02a3 | DOUBLE | 89.6% | 0.0 |  |
| xf3e02a4 | VARCHAR | 89.6% | Z |  |
| f3e02a4 | DOUBLE | 89.6% | 0.0 |  |
| xf3e02a5 | VARCHAR | 89.6% | Z |  |
| f3e02a5 | DOUBLE | 89.6% | 0.0 |  |
| xf3e02a6 | VARCHAR | 89.6% | Z |  |
| f3e02a6 | DOUBLE | 89.6% | 0.0 |  |
| xf3e02a7 | VARCHAR | 89.6% | Z |  |
| f3e02a7 | DOUBLE | 89.6% | 0.0 |  |
| xf3e02b3 | VARCHAR | 89.6% | Z |  |
| f3e02b3 | DOUBLE | 89.6% | 0.0 |  |
| xf3e02b4 | VARCHAR | 89.6% | Z |  |
| f3e02b4 | DOUBLE | 89.6% | 0.0 |  |
| xf3e02b5 | VARCHAR | 89.6% | Z |  |
| f3e02b5 | DOUBLE | 89.6% | 0.0 |  |
| xf3e02b6 | VARCHAR | 89.6% | Z |  |
| f3e02b6 | DOUBLE | 89.6% | 0.0 |  |
| xf3e02b7 | VARCHAR | 89.6% | Z |  |
| f3e02b7 | DOUBLE | 89.6% | 0.0 |  |
| xf3e03a3 | VARCHAR | 89.6% | R |  |
| f3e03a3 | DOUBLE | 89.6% | 70465.0 |  |
| xf3e03a4 | VARCHAR | 89.6% | R |  |
| f3e03a4 | DOUBLE | 89.6% | 82976.0 |  |
| xf3e03a5 | VARCHAR | 89.6% | R |  |
| f3e03a5 | DOUBLE | 89.6% | 26300.0 |  |
| xf3e03a6 | VARCHAR | 89.6% | Z |  |
| f3e03a6 | DOUBLE | 89.6% | 0.0 |  |
| xf3e03a7 | VARCHAR | 89.6% | R |  |
| f3e03a7 | DOUBLE | 89.6% | 55583.0 |  |
| xf3e03b3 | VARCHAR | 89.6% | R |  |
| f3e03b3 | DOUBLE | 89.6% | 185588.0 |  |
| xf3e03b4 | VARCHAR | 89.6% | R |  |
| f3e03b4 | DOUBLE | 89.6% | 220489.0 |  |
| xf3e03b5 | VARCHAR | 89.6% | R |  |
| f3e03b5 | DOUBLE | 89.6% | 69885.0 |  |
| xf3e03b6 | VARCHAR | 89.6% | Z |  |
| f3e03b6 | DOUBLE | 89.6% | 0.0 |  |
| xf3e03b7 | VARCHAR | 89.6% | R |  |
| f3e03b7 | DOUBLE | 89.6% | 1047902.0 |  |
| xf3e03c3 | VARCHAR | 89.6% | R |  |
| f3e03c3 | DOUBLE | 89.6% | 216729.0 |  |
| xf3e03c4 | VARCHAR | 89.6% | R |  |
| f3e03c4 | DOUBLE | 89.6% | 535449.0 |  |
| xf3e03c5 | VARCHAR | 89.6% | R |  |
| f3e03c5 | DOUBLE | 89.6% | 169713.0 |  |
| xf3e03c6 | VARCHAR | 89.6% | Z |  |
| f3e03c6 | DOUBLE | 89.6% | 0.0 |  |
| xf3e03c7 | VARCHAR | 89.6% | R |  |
| f3e03c7 | DOUBLE | 89.6% | 2644406.0 |  |
| xf3e043 | VARCHAR | 89.6% | Z |  |
| f3e043 | DOUBLE | 95.8% | 0.0 |  |
| xf3e044 | VARCHAR | 89.6% | R |  |
| f3e044 | DOUBLE | 95.8% | 54729.0 |  |
| xf3e045 | VARCHAR | 89.6% | R |  |
| f3e045 | DOUBLE | 95.8% | 17347.0 |  |
| xf3e046 | VARCHAR | 89.6% | Z |  |
| f3e046 | DOUBLE | 95.8% | 0.0 |  |
| xf3e047 | VARCHAR | 89.6% | R |  |
| f3e047 | DOUBLE | 95.8% | 334697.0 |  |
| xf3e057 | VARCHAR | 89.6% | Z |  |
| f3e057 | DOUBLE | 89.6% | 0.0 |  |
| xf3e103 | VARCHAR | 89.6% | Z |  |
| f3e103 | DOUBLE | 97.7% | 0.0 |  |
| xf3e104 | VARCHAR | 89.6% | Z |  |
| f3e104 | DOUBLE | 97.7% | 0.0 |  |
| xf3e105 | VARCHAR | 89.6% | Z |  |
| f3e105 | DOUBLE | 97.7% | 0.0 |  |
| xf3e106 | VARCHAR | 89.6% | Z |  |
| f3e106 | DOUBLE | 97.7% | 0.0 |  |
| xf3e107 | VARCHAR | 89.6% | Z |  |
| f3e107 | DOUBLE | 97.7% | 0.0 |  |
| xf3e111 | VARCHAR | 89.6% | R |  |
| f3e111 | DOUBLE | 89.6% | 0.0 |  |
| xf3e112 | VARCHAR | 89.6% | R |  |
| f3e112 | DOUBLE | 89.6% | 67421.0 |  |
| xf3e113 | VARCHAR | 89.6% | R |  |
| f3e113 | DOUBLE | 89.6% | 12002.0 |  |
| xf3e114 | VARCHAR | 89.6% | R |  |
| f3e114 | DOUBLE | 89.6% | -1360255.0 |  |
| xf3e115 | VARCHAR | 89.6% | R |  |
| f3e115 | DOUBLE | 89.6% | 63817.0 |  |
| xf3e116 | VARCHAR | 89.6% | Z |  |
| f3e116 | DOUBLE | 89.6% | 0.0 |  |
| xf3e117 | VARCHAR | 89.6% | R |  |
| f3e117 | DOUBLE | 89.6% | 1217015.0 |  |
| xf3e063 | VARCHAR | 89.6% | R |  |
| f3e063 | DOUBLE | 89.6% | 0.0 |  |
| xf3e064 | VARCHAR | 89.6% | R |  |
| f3e064 | DOUBLE | 89.6% | 0.0 |  |
| xf3e065 | VARCHAR | 89.6% | R |  |
| f3e065 | DOUBLE | 89.6% | 0.0 |  |
| xf3e066 | VARCHAR | 89.6% | Z |  |
| f3e066 | DOUBLE | 89.6% | 0.0 |  |
| xf3e067 | VARCHAR | 89.6% | R |  |
| f3e067 | DOUBLE | 89.6% | 0.0 |  |
| xf3e01 | VARCHAR | 41.9% | R |  |
| f3e01 | DOUBLE | 41.9% | 2959765.0 |  |
| xf3e02 | VARCHAR | 41.9% | R |  |
| f3e02 | DOUBLE | 42.0% | 0.0 |  |
| xf3e03 | VARCHAR | 41.9% | R |  |
| f3e03 | DOUBLE | 41.9% | 8697494.0 |  |
| xf3e04 | VARCHAR | 41.9% | R |  |
| f3e04 | DOUBLE | 57.2% | 463998.0 |  |
| xf3e05 | VARCHAR | 41.9% | R |  |
| f3e05 | DOUBLE | 42.0% | 0.0 |  |
| xf3e06 | VARCHAR | 41.9% | R |  |
| f3e06 | DOUBLE | 41.9% | 0.0 |  |
| xf3e07 | VARCHAR | 41.9% | R |  |
| f3e07 | DOUBLE | 41.9% | 12121257.0 |  |

## flags

Rows: 147,769

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| stat_ic | BIGINT | 0.0% | 1 | Appears in 3 tables, common join key |
| lock_ic | BIGINT | 0.0% | 8 | Appears in 3 tables, common join key |
| imp_ic | BIGINT | 0.0% | -2 |  |
| stat_c | BIGINT | 0.0% | 1 | Appears in 3 tables, common join key |
| lock_c | BIGINT | 0.0% | 8 | Appears in 3 tables, common join key |
| prch_c | BIGINT | 0.0% | -2 | Appears in 3 tables, common join key |
| idx_c | BIGINT | 0.0% | -2 | Appears in 3 tables, common join key |
| pcc_f | VARCHAR | 28.6% | . |  |
| imp_c | BIGINT | 0.0% | -2 | Appears in 3 tables, common join key |
| stat_e12 | DOUBLE | 14.2% | 1.0 |  |
| lock_e12 | DOUBLE | 14.2% | 8.0 |  |
| prch_e12 | DOUBLE | 14.2% | -2.0 |  |
| idx_e12 | DOUBLE | 14.2% | -2.0 |  |
| pce12_f | VARCHAR | 28.7% | . |  |
| imp_e12 | DOUBLE | 14.2% | -2.0 |  |
| year | BIGINT | 0.0% | 2024 | Appears in 26 tables, common join key |
| stat_sfa | DOUBLE | 4.1% | 1.0 | Appears in 3 tables, common join key |
| lock_sfa | DOUBLE | 4.1% | 8.0 | Appears in 3 tables, common join key |
| prch_sfa | DOUBLE | 4.1% | -2.0 | Appears in 3 tables, common join key |
| idx_sfa | DOUBLE | 4.1% | -2.0 | Appears in 3 tables, common join key |
| pcsfa_f | VARCHAR | 32.7% | . |  |
| imp_sfa | DOUBLE | 4.1% | -2.0 | Appears in 3 tables, common join key |
| sfaform | DOUBLE | 53.6% | 2.0 |  |
| stat_gr | DOUBLE | 4.1% | 1.0 | Appears in 3 tables, common join key |
| lock_gr | DOUBLE | 4.1% | 8.0 | Appears in 3 tables, common join key |
| prch_gr | DOUBLE | 4.1% | -2.0 | Appears in 3 tables, common join key |
| idx_gr | DOUBLE | 4.1% | -2.0 | Appears in 3 tables, common join key |
| pcgr_f | VARCHAR | 32.8% | . |  |
| imp_gr | DOUBLE | 4.1% | -2.0 | Appears in 3 tables, common join key |
| cohrtstu | DOUBLE | 4.1% | 1.0 | Appears in 3 tables, common join key |
| stat_gr2 | DOUBLE | 27.9% | 1.0 |  |
| lock_gr2 | DOUBLE | 27.9% | 8.0 |  |
| prch_gr2 | DOUBLE | 27.9% | -2.0 |  |
| idx_gr2 | DOUBLE | 27.9% | -2.0 |  |
| pcgr2_f | VARCHAR | 58.8% | . |  |
| imp_gr2 | DOUBLE | 27.9% | -2.0 |  |
| stat_om | DOUBLE | 58.8% | 1.0 |  |
| lock_om | DOUBLE | 58.8% | 8.0 |  |
| prch_om | DOUBLE | 58.8% | -2.0 |  |
| idx_om | DOUBLE | 58.8% | -2.0 |  |
| pcom_f | VARCHAR | 58.8% | . |  |
| imp_om | DOUBLE | 58.8% | -2.0 |  |
| stat_adm | DOUBLE | 53.6% | 1.0 |  |
| lock_adm | DOUBLE | 53.6% | 8.0 |  |
| prch_adm | DOUBLE | 78.5% | -2.0 |  |
| idx_adm | DOUBLE | 78.5% | -2.0 |  |
| pcadm_f | VARCHAR | 78.5% | . |  |
| imp_adm | DOUBLE | 53.6% | -2.0 |  |
| stat_hr | DOUBLE | 8.8% | 1.0 |  |
| lock_hr | DOUBLE | 8.8% | 8.0 |  |
| prch_hr | DOUBLE | 8.8% | -2.0 |  |
| idx_hr | DOUBLE | 8.8% | -2.0 |  |
| pchr_f | VARCHAR | 32.7% | . |  |
| imp_hr | DOUBLE | 8.8% | -2.0 |  |
| ftemp15 | DOUBLE | 4.1% | 1.0 | Appears in 3 tables, common join key |
| tenursys | DOUBLE | 43.1% | 1.0 | Appears in 3 tables, common join key |
| sa_excl | DOUBLE | 4.1% | 2.0 | Appears in 3 tables, common join key |
| stat_eap | DOUBLE | 4.1% | 1.0 | Appears in 3 tables, common join key |
| stat_sa | DOUBLE | 4.1% | 1.0 | Appears in 3 tables, common join key |
| stat_s | DOUBLE | 4.1% | 1.0 | Appears in 3 tables, common join key |
| stat_ef | DOUBLE | 4.1% | 1.0 | Appears in 3 tables, common join key |
| lock_ef | DOUBLE | 4.1% | 8.0 | Appears in 3 tables, common join key |
| prch_ef | DOUBLE | 4.1% | -2.0 | Appears in 3 tables, common join key |
| idx_ef | DOUBLE | 4.1% | -2.0 | Appears in 3 tables, common join key |
| pcef_f | VARCHAR | 32.8% | . |  |
| imp_ef | DOUBLE | 4.1% | -2.0 | Appears in 3 tables, common join key |
| pta99_ef | DOUBLE | 4.1% | 1.0 | Appears in 3 tables, common join key |
| ptacipef | DOUBLE | 4.1% | -2.0 | Appears in 3 tables, common join key |
| ptb_ef | DOUBLE | 4.1% | 1.0 | Appears in 3 tables, common join key |
| ptc_ef | DOUBLE | 4.1% | 5.0 | Appears in 3 tables, common join key |
| ptd_ef | DOUBLE | 4.1% | 1.0 | Appears in 3 tables, common join key |
| stat_f | DOUBLE | 4.1% | 1.0 | Appears in 3 tables, common join key |
| lock_f | DOUBLE | 4.1% | 8.0 | Appears in 3 tables, common join key |
| prch_f | DOUBLE | 4.5% | -2.0 | Appears in 3 tables, common join key |
| idx_f | DOUBLE | 4.5% | -2.0 | Appears in 3 tables, common join key |
| pcf_f | VARCHAR | 30.7% | . |  |
| prchtp_f | DOUBLE | 64.0% | -2.0 |  |
| imp_f | DOUBLE | 4.1% | -2.0 | Appears in 3 tables, common join key |
| form_f | DOUBLE | 4.1% | 4.0 | Appears in 3 tables, common join key |
| fybeg | DOUBLE | 4.1% | 102022.0 | Appears in 3 tables, common join key |
| fyend | DOUBLE | 4.1% | 92023.0 | Appears in 3 tables, common join key |
| gpfs | DOUBLE | 4.1% | 3.0 | Appears in 3 tables, common join key |
| f1gasbal | DOUBLE | 4.1% | 3.0 | Appears in 3 tables, common join key |
| f2pell | DOUBLE | 8.8% | -2.0 |  |
| f3pell | DOUBLE | 37.9% | -2.0 |  |
| fcolathl | DOUBLE | 91.6% | 1.0 |  |
| f_athex1 | DOUBLE | 91.6% | 1.0 |  |
| f_athex2 | DOUBLE | 91.6% | 0.0 |  |
| f_athex9 | DOUBLE | 91.6% | 0.0 |  |
| f_athrv | DOUBLE | 91.6% | 1.0 |  |
| f_athrv1 | DOUBLE | 83.0% | 0.0 |  |
| f_athrv2 | DOUBLE | 83.0% | 1.0 |  |
| f_athrv9 | DOUBLE | 83.0% | 0.0 |  |
| f3bist | DOUBLE | 53.6% | -2.0 |  |
| stat_al | DOUBLE | 53.6% | 1.0 |  |
| lock_al | DOUBLE | 53.6% | 8.0 |  |
| prch_al | DOUBLE | 53.6% | -2.0 |  |
| idx_al | DOUBLE | 53.6% | -2.0 |  |
| pcal_f | VARCHAR | 53.6% | . |  |
| imp_al | DOUBLE | 53.6% | -2.0 |  |
| hasal | DOUBLE | 53.6% | 1.0 |  |
| ntrldstr | DOUBLE | 23.1% | 0.0 |  |
| rev_c | DOUBLE | 4.1% | 0.0 | Appears in 3 tables, common join key |
| rev_e12 | DOUBLE | 18.3% | 0.0 |  |
| rev_ic | DOUBLE | 23.1% | 0.0 |  |
| rev_sfa | DOUBLE | 8.3% | 0.0 | Appears in 3 tables, common join key |
| rev_gr | DOUBLE | 8.3% | 0.0 | Appears in 3 tables, common join key |
| rev_gr2 | DOUBLE | 32.1% | 0.0 |  |
| rev_om | DOUBLE | 63.0% | 0.0 |  |
| rev_adm | DOUBLE | 57.8% | 0.0 |  |
| rev_hr | DOUBLE | 13.0% | 0.0 |  |
| rev_ef | DOUBLE | 8.3% | 0.0 | Appears in 3 tables, common join key |
| rev_f | DOUBLE | 8.3% | 1.0 | Appears in 3 tables, common join key |
| rev_al | DOUBLE | 57.8% | 0.0 |  |
| f_athltc | DOUBLE | 17.2% | 1.0 |  |
| f_athrv3 | DOUBLE | 91.4% | 0.0 |  |
| omflg1gr | DOUBLE | 94.8% | -2.0 |  |
| omflg2gr | DOUBLE | 94.8% | 0.0 |  |
| omflg3gr | DOUBLE | 94.8% | -2.0 |  |
| omflg4 | DOUBLE | 94.8% | 0.0 |  |
| omflg5 | DOUBLE | 94.8% | 0.0 |  |
| omflg6gr | DOUBLE | 94.8% | 0.0 |  |
| pcf_f_rv | VARCHAR | 84.5% | . |  |
| hasgrurl | DOUBLE | 64.7% | 1.0 |  |
| grdisurl | VARCHAR | 64.7% | www.aamu.edu |  |
| re_c | DOUBLE | 85.1% | 2.0 |  |
| re_e12 | DOUBLE | 85.1% | -1.0 |  |
| fyrpyear | DOUBLE | 66.2% | -1.0 | Appears in 4 tables, common join key |
| longpgm | DOUBLE | 66.2% | -1.0 | Appears in 3 tables, common join key |
| re_gr | DOUBLE | 85.1% | -1.0 |  |
| fp_c | DOUBLE | 90.2% | -2.0 |  |
| fp_e12 | DOUBLE | 90.2% | -2.0 |  |
| re_hr | DOUBLE | 90.2% | -1.0 |  |
| re_ef | DOUBLE | 90.2% | -1.0 |  |
| f_ver | DOUBLE | 90.2% | -1.0 |  |
| cufasb | DOUBLE | 71.3% | -1.0 | Appears in 3 tables, common join key |
| cugasb | DOUBLE | 71.3% | -1.0 | Appears in 3 tables, common join key |
| f1systyp | DOUBLE | 71.3% | 1.0 | Appears in 3 tables, common join key |
| f1sysnam | VARCHAR | 71.3% | Air University | Appears in 3 tables, common join key |
| fp_ic | DOUBLE | 95.2% | -2.0 |  |
| fp_ef | DOUBLE | 95.2% | -2.0 |  |
| pteeffy | DOUBLE | 85.8% | 5.0 | Appears in 3 tables, common join key |
| pteefia | DOUBLE | 85.8% | 5.0 | Appears in 3 tables, common join key |
| pyaid | DOUBLE | 85.8% | 2.0 | Appears in 3 tables, common join key |
| sport1 | DOUBLE | 85.8% | -1.0 | Appears in 4 tables, common join key |
| sport2 | DOUBLE | 85.8% | -1.0 | Appears in 4 tables, common join key |
| sport3 | DOUBLE | 85.8% | -1.0 | Appears in 4 tables, common join key |
| sport4 | DOUBLE | 85.8% | -1.0 | Appears in 4 tables, common join key |
| sport5 | DOUBLE | 85.8% | -1.0 | Appears in 3 tables, common join key |
| ndst2005 | DOUBLE | 95.2% | 0.0 |  |
| lock_sa | DOUBLE | 95.3% | -2.0 | Appears in 3 tables, common join key |
| prch_sa | DOUBLE | 95.3% | -2.0 | Appears in 3 tables, common join key |
| idx_sa | DOUBLE | 95.3% | -2.0 | Appears in 3 tables, common join key |
| imp_sa | DOUBLE | 95.3% | -2.0 | Appears in 3 tables, common join key |
| lock_s | DOUBLE | 95.3% | 0.0 | Appears in 3 tables, common join key |
| prch_s | DOUBLE | 95.3% | -2.0 | Appears in 3 tables, common join key |
| idx_s | DOUBLE | 95.3% | -2.0 | Appears in 3 tables, common join key |
| imp_s | DOUBLE | 95.3% | -2.0 | Appears in 3 tables, common join key |
| lock_eap | DOUBLE | 95.3% | 0.0 | Appears in 3 tables, common join key |
| prch_eap | DOUBLE | 95.3% | -2.0 | Appears in 3 tables, common join key |
| idx_eap | DOUBLE | 95.3% | -2.0 | Appears in 3 tables, common join key |
| imp_eap | DOUBLE | 95.3% | -2.0 | Appears in 3 tables, common join key |
| cohrtaid | DOUBLE | 95.3% | -1.0 | Appears in 3 tables, common join key |
| pcf_m | DOUBLE | 95.3% | -2.0 |  |
| pcffp_m | DOUBLE | 95.3% | -2.0 |  |
| pcffp_f | DOUBLE | 99.7% | 10.0 |  |
| pcc_m | DOUBLE | 95.3% | -2.0 |  |
| pcef_m | DOUBLE | 95.3% | -2.0 |  |
| pcgr_m | DOUBLE | 95.3% | -2.0 |  |
| pcsfa_m | DOUBLE | 95.3% | -2.0 |  |
| pceap_m | DOUBLE | 95.3% | -2.0 |  |
| pceap_f | DOUBLE | 99.9% | 3.0 |  |
| pcsa_m | DOUBLE | 95.3% | -2.0 |  |
| pcsa_f | DOUBLE | 100.0% | 3.0 |  |
| pcs_m | DOUBLE | 95.3% | -2.0 |  |
| pcs_f | DOUBLE | 100.0% | 78.0 |  |
| rev_sa | DOUBLE | 95.3% | -2.0 | Appears in 3 tables, common join key |
| rev_s | DOUBLE | 95.3% | 0.0 | Appears in 3 tables, common join key |
| rev_eap | DOUBLE | 95.3% | 0.0 | Appears in 3 tables, common join key |

## gr

Rows: 1,200,909

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| grtype | DOUBLE | 0.0% | 1.0 |  |
| chrtstat | DOUBLE | 0.2% | 10.0 |  |
| section | BIGINT | 0.0% | 1 | Appears in 3 tables, common join key |
| cohort | BIGINT | 0.0% | 1 |  |
| line | DOUBLE | 30.5% | 999.0 | Appears in 4 tables, common join key |
| xgrtotlt | VARCHAR | 32.0% | R |  |
| grtotlt | DOUBLE | 32.0% | 1286.0 |  |
| xgrtotlm | VARCHAR | 32.0% | R |  |
| grtotlm | DOUBLE | 37.9% | 514.0 |  |
| xgrtotlw | VARCHAR | 32.0% | R |  |
| grtotlw | DOUBLE | 37.9% | 772.0 |  |
| xgraiant | VARCHAR | 32.0% | R |  |
| graiant | DOUBLE | 45.2% | 2.0 |  |
| xgraianm | VARCHAR | 32.0% | Z |  |
| graianm | DOUBLE | 45.2% | 0.0 |  |
| xgraianw | VARCHAR | 32.0% | R |  |
| graianw | DOUBLE | 45.2% | 2.0 |  |
| xgrasiat | VARCHAR | 32.0% | R |  |
| grasiat | DOUBLE | 45.2% | 2.0 |  |
| xgrasiam | VARCHAR | 32.0% | Z |  |
| grasiam | DOUBLE | 45.2% | 0.0 |  |
| xgrasiaw | VARCHAR | 32.0% | R |  |
| grasiaw | DOUBLE | 45.2% | 2.0 |  |
| xgrbkaat | VARCHAR | 32.0% | R |  |
| grbkaat | DOUBLE | 45.2% | 1158.0 |  |
| xgrbkaam | VARCHAR | 32.0% | R |  |
| grbkaam | DOUBLE | 45.2% | 464.0 |  |
| xgrbkaaw | VARCHAR | 32.0% | R |  |
| grbkaaw | DOUBLE | 45.2% | 694.0 |  |
| xgrhispt | VARCHAR | 32.0% | R |  |
| grhispt | DOUBLE | 45.2% | 13.0 |  |
| xgrhispm | VARCHAR | 32.0% | R |  |
| grhispm | DOUBLE | 45.2% | 8.0 |  |
| xgrhispw | VARCHAR | 32.0% | R |  |
| grhispw | DOUBLE | 45.2% | 5.0 |  |
| xgrnhpit | VARCHAR | 32.0% | R |  |
| grnhpit | DOUBLE | 45.2% | 1.0 |  |
| xgrnhpim | VARCHAR | 32.0% | Z |  |
| grnhpim | DOUBLE | 45.2% | 0.0 |  |
| xgrnhpiw | VARCHAR | 32.0% | R |  |
| grnhpiw | DOUBLE | 45.2% | 1.0 |  |
| xgrwhitt | VARCHAR | 32.0% | R |  |
| grwhitt | DOUBLE | 45.2% | 19.0 |  |
| xgrwhitm | VARCHAR | 32.0% | R |  |
| grwhitm | DOUBLE | 45.2% | 13.0 |  |
| xgrwhitw | VARCHAR | 32.0% | R |  |
| grwhitw | DOUBLE | 45.2% | 6.0 |  |
| xgr2mort | VARCHAR | 32.0% | R |  |
| gr2mort | DOUBLE | 45.2% | 14.0 |  |
| xgr2morm | VARCHAR | 32.0% | R |  |
| gr2morm | DOUBLE | 45.2% | 4.0 |  |
| xgr2morw | VARCHAR | 32.0% | R |  |
| gr2morw | DOUBLE | 45.2% | 10.0 |  |
| xgrunknt | VARCHAR | 32.0% | R |  |
| grunknt | DOUBLE | 37.9% | 68.0 |  |
| xgrunknm | VARCHAR | 32.0% | R |  |
| grunknm | DOUBLE | 37.9% | 22.0 |  |
| xgrunknw | VARCHAR | 32.0% | R |  |
| grunknw | DOUBLE | 37.9% | 46.0 |  |
| xgrnralt | VARCHAR | 32.0% | R |  |
| grnralt | DOUBLE | 37.9% | 9.0 |  |
| xgrnralm | VARCHAR | 32.0% | R |  |
| grnralm | DOUBLE | 37.9% | 3.0 |  |
| xgrnralw | VARCHAR | 32.0% | R |  |
| grnralw | DOUBLE | 37.9% | 6.0 |  |
| year | BIGINT | 0.0% | 2023 | Appears in 26 tables, common join key |
| xgrrac03 | VARCHAR | 57.9% | R |  |
| grrace03 | DOUBLE | 60.2% | 576.0 |  |
| xgrrac04 | VARCHAR | 57.9% | R |  |
| grrace04 | DOUBLE | 60.2% | 595.0 |  |
| xgrrac05 | VARCHAR | 57.9% | Z |  |
| grrace05 | DOUBLE | 60.2% | 0.0 |  |
| xgrrac06 | VARCHAR | 57.9% | R |  |
| grrace06 | DOUBLE | 60.2% | 1.0 |  |
| xgrrac07 | VARCHAR | 57.9% | Z |  |
| grrace07 | DOUBLE | 60.2% | 0.0 |  |
| xgrrac08 | VARCHAR | 57.9% | Z |  |
| grrace08 | DOUBLE | 60.2% | 0.0 |  |
| xgrrac09 | VARCHAR | 57.9% | R |  |
| grrace09 | DOUBLE | 60.2% | 1.0 |  |
| xgrrac10 | VARCHAR | 57.9% | R |  |
| grrace10 | DOUBLE | 60.2% | 3.0 |  |
| xgrrac11 | VARCHAR | 57.9% | R |  |
| grrace11 | DOUBLE | 60.2% | 3.0 |  |
| xgrrac12 | VARCHAR | 57.9% | R |  |
| grrace12 | DOUBLE | 60.2% | 7.0 |  |
| xgrrac18 | VARCHAR | 57.9% | R |  |
| grrace18 | DOUBLE | 60.2% | 1171.0 |  |
| xgrrac19 | VARCHAR | 57.9% | R |  |
| grrace19 | DOUBLE | 60.2% | 1.0 |  |
| xgrrac20 | VARCHAR | 57.9% | Z |  |
| grrace20 | DOUBLE | 60.2% | 0.0 |  |
| xgrrac21 | VARCHAR | 57.9% | R |  |
| grrace21 | DOUBLE | 60.2% | 4.0 |  |
| xgrrac22 | VARCHAR | 57.9% | R |  |
| grrace22 | DOUBLE | 60.2% | 10.0 |  |
| xdvgrait | VARCHAR | 89.8% | R |  |
| dvgrait | DOUBLE | 90.7% | 1.0 |  |
| xdvgraim | VARCHAR | 89.8% | Z |  |
| dvgraim | DOUBLE | 90.7% | 0.0 |  |
| xdvgraiw | VARCHAR | 89.8% | R |  |
| dvgraiw | DOUBLE | 90.7% | 1.0 |  |
| xdvgrapt | VARCHAR | 89.8% | Z |  |
| dvgrapt | DOUBLE | 90.7% | 0.0 |  |
| xdvgrapm | VARCHAR | 89.8% | Z |  |
| dvgrapm | DOUBLE | 90.7% | 0.0 |  |
| xdvgrapw | VARCHAR | 89.8% | Z |  |
| dvgrapw | DOUBLE | 90.7% | 0.0 |  |
| xdvgrbkt | VARCHAR | 89.8% | R |  |
| dvgrbkt | DOUBLE | 90.7% | 1171.0 |  |
| xdvgrbkm | VARCHAR | 89.8% | R |  |
| dvgrbkm | DOUBLE | 90.7% | 576.0 |  |
| xdvgrbkw | VARCHAR | 89.8% | R |  |
| dvgrbkw | DOUBLE | 90.7% | 595.0 |  |
| xdvgrhst | VARCHAR | 89.8% | R |  |
| dvgrhst | DOUBLE | 90.7% | 4.0 |  |
| xdvgrhsm | VARCHAR | 89.8% | R |  |
| dvgrhsm | DOUBLE | 90.7% | 1.0 |  |
| xdvgrhsw | VARCHAR | 89.8% | R |  |
| dvgrhsw | DOUBLE | 90.7% | 3.0 |  |
| xdvgrwht | VARCHAR | 89.8% | R |  |
| dvgrwht | DOUBLE | 90.7% | 10.0 |  |
| xdvgrwhm | VARCHAR | 89.8% | R |  |
| dvgrwhm | DOUBLE | 90.7% | 3.0 |  |
| xdvgrwhw | VARCHAR | 89.8% | R |  |
| dvgrwhw | DOUBLE | 90.7% | 7.0 |  |
| xgrrac01 | VARCHAR | 68.0% | R |  |
| grrace01 | DOUBLE | 68.0% | 13.0 |  |
| xgrrac02 | VARCHAR | 68.0% | R |  |
| grrace02 | DOUBLE | 68.0% | 15.0 |  |
| xgrrac13 | VARCHAR | 68.0% | R |  |
| grrace13 | DOUBLE | 68.0% | 0.0 |  |
| xgrrac14 | VARCHAR | 68.0% | R |  |
| grrace14 | DOUBLE | 68.0% | 0.0 |  |
| xgrrac15 | VARCHAR | 68.0% | R |  |
| grrace15 | DOUBLE | 68.0% | 497.0 |  |
| xgrrac16 | VARCHAR | 68.0% | R |  |
| grrace16 | DOUBLE | 68.0% | 541.0 |  |
| xgrrac17 | VARCHAR | 68.0% | R |  |
| grrace17 | DOUBLE | 68.0% | 28.0 |  |
| xgrrac23 | VARCHAR | 68.0% | R |  |
| grrace23 | DOUBLE | 68.0% | 0.0 |  |
| xgrrac24 | VARCHAR | 68.0% | R |  |
| grrace24 | DOUBLE | 68.0% | 1038.0 |  |

## gr200

Rows: 88,248

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| xbarevct | VARCHAR | 0.0% | R |  |
| barevct | DOUBLE | 63.1% | 1222.0 |  |
| xbaexclu | VARCHAR | 0.0% | R |  |
| baexclu | DOUBLE | 63.1% | 0.0 |  |
| xbaac150 | VARCHAR | 0.0% | R |  |
| baac150 | DOUBLE | 63.1% | 1222.0 |  |
| xbanc100 | VARCHAR | 0.0% | R |  |
| banc100 | DOUBLE | 63.1% | 137.0 |  |
| xbagr100 | VARCHAR | 0.0% | R |  |
| bagr100 | DOUBLE | 63.1% | 11.0 |  |
| xbanc150 | VARCHAR | 0.0% | R |  |
| banc150 | DOUBLE | 63.1% | 343.0 |  |
| xbagr150 | VARCHAR | 0.0% | R |  |
| bagr150 | DOUBLE | 63.1% | 28.0 |  |
| xbaaexcl | VARCHAR | 0.0% | R |  |
| baaexcl | DOUBLE | 63.1% | 0.0 |  |
| xbaac200 | VARCHAR | 0.0% | R |  |
| baac200 | DOUBLE | 63.1% | 1222.0 |  |
| xbanc20a | VARCHAR | 0.0% | R |  |
| banc200a | DOUBLE | 63.1% | 19.0 |  |
| xbastend | VARCHAR | 19.3% | R |  |
| bastend | DOUBLE | 69.8% | 9.0 |  |
| xbanc200 | VARCHAR | 0.0% | R |  |
| banc200 | DOUBLE | 63.1% | 362.0 |  |
| xbagr200 | VARCHAR | 0.0% | R |  |
| bagr200 | DOUBLE | 63.1% | 30.0 |  |
| xl4revct | VARCHAR | 0.0% | A |  |
| l4revct | DOUBLE | 36.9% | 328.0 |  |
| xl4exclu | VARCHAR | 0.0% | A |  |
| l4exclu | DOUBLE | 36.9% | 0.0 |  |
| xl4ac150 | VARCHAR | 0.0% | A |  |
| l4ac150 | DOUBLE | 36.9% | 328.0 |  |
| xl4nc100 | VARCHAR | 0.0% | A |  |
| l4nc100 | DOUBLE | 36.9% | 57.0 |  |
| xl4gr100 | VARCHAR | 0.0% | A |  |
| l4gr100 | DOUBLE | 36.9% | 17.0 |  |
| xl4nc150 | VARCHAR | 0.0% | A |  |
| l4nc150 | DOUBLE | 36.9% | 71.0 |  |
| xl4gr150 | VARCHAR | 0.0% | A |  |
| l4gr150 | DOUBLE | 36.9% | 22.0 |  |
| xl4aexcl | VARCHAR | 0.0% | A |  |
| l4aexcl | DOUBLE | 36.9% | 0.0 |  |
| xl4ac200 | VARCHAR | 0.0% | A |  |
| l4ac200 | DOUBLE | 36.9% | 328.0 |  |
| xl4nc20a | VARCHAR | 0.0% | A |  |
| l4nc200a | DOUBLE | 36.9% | 9.0 |  |
| xl4stend | VARCHAR | 19.3% | A |  |
| l4stend | DOUBLE | 49.4% | 19.0 |  |
| xl4nc200 | VARCHAR | 0.0% | A |  |
| l4nc200 | DOUBLE | 36.9% | 80.0 |  |
| xl4gr200 | VARCHAR | 0.0% | A |  |
| l4gr200 | DOUBLE | 36.9% | 24.0 |  |
| year | BIGINT | 0.0% | 2023 | Appears in 26 tables, common join key |

## hd

Rows: 162,442

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| institution_name | VARCHAR | 0.0% | Alabama A & M University | Appears in 4 tables, common join key |
| ialias | VARCHAR | 16.8% | AAMU |  |
| addr | VARCHAR | 0.2% | 4900 Meridian Street |  |
| city | VARCHAR | 0.0% | Normal |  |
| state | VARCHAR | 0.0% | AL | Appears in 4 tables, common join key |
| zip_code | VARCHAR | 0.0% | 35762 |  |
| fips_state | BIGINT | 0.0% | 1 |  |
| region | BIGINT | 0.0% | 5 |  |
| chfnm | VARCHAR | 0.1% | Dr. Daniel K. Wims |  |
| chftitle | VARCHAR | 0.2% | President |  |
| gentele | DOUBLE | 0.9% | 2563725000.0 |  |
| ein | DOUBLE | 0.9% | 636001097.0 |  |
| ueis | VARCHAR | 88.6% | JDVGS67MSLH7 |  |
| opeid | DOUBLE | 0.9% | 100200.0 |  |
| opeflag | BIGINT | 0.0% | 1 |  |
| website | VARCHAR | 1.5% | www.aamu.edu/ |  |
| adminurl | VARCHAR | 24.7% | https://www.aamu.edu/admissions-aid/index.html |  |
| faidurl | VARCHAR | 24.7% | https://www.aamu.edu/admissions-aid/financial-aid/ |  |
| applurl | VARCHAR | 24.8% | https://www.aamu.edu/admissions-aid/undergraduate-admissions/apply-today.html |  |
| npricurl | VARCHAR | 39.8% | www.aamu.edu/admissions-aid/tuition-fees/net-price-calculator.html |  |
| veturl | VARCHAR | 54.0% |   |  |
| athurl | VARCHAR | 54.0% |   |  |
| disaurl | VARCHAR | 63.5% | https://www.aamu.edu/administrativeoffices/VADS/Pages/Disability-Services.aspx |  |
| sector | BIGINT | 0.0% | 1 | Appears in 3 tables, common join key |
| level | BIGINT | 0.0% | 1 |  |
| control | BIGINT | 0.0% | 1 |  |
| hloffer | BIGINT | 0.0% | 9 |  |
| ugoffer | BIGINT | 0.0% | 1 |  |
| groffer | BIGINT | 0.0% | 1 |  |
| hdegofr1 | DOUBLE | 30.7% | 12.0 |  |
| degree_granting | BIGINT | 0.0% | 1 |  |
| hbcu | BIGINT | 0.0% | 1 |  |
| hospital | BIGINT | 0.0% | 2 |  |
| medical | BIGINT | 0.0% | 2 |  |
| tribal | BIGINT | 0.0% | 2 |  |
| locale_code | BIGINT | 0.0% | 12 |  |
| openpubl | BIGINT | 0.0% | 1 |  |
| act | VARCHAR | 0.0% | A |  |
| newid | DOUBLE | 0.1% | -2.0 |  |
| deathyr | BIGINT | 0.0% | -2 |  |
| close_date | VARCHAR | 0.2% | -2         |  |
| currently_active | BIGINT | 0.0% | 1 |  |
| postsec | BIGINT | 0.0% | 1 |  |
| pseflag | BIGINT | 0.0% | 1 |  |
| pset4flg | BIGINT | 0.0% | 1 |  |
| rptmth | DOUBLE | 9.0% | 1.0 |  |
| instcat | DOUBLE | 9.0% | 2.0 |  |
| c00carnegie | DOUBLE | 96.3% | 16.0 |  |
| carnegie_basic | BIGINT | 0.0% | 18 |  |
| carnegieic | DOUBLE | 96.3% | 9.0 |  |
| carnegiesaec | DOUBLE | 96.3% | 4.0 |  |
| carnegiersch | DOUBLE | 96.3% | 3.0 |  |
| carnegiesize | DOUBLE | 96.3% | 3.0 |  |
| carnegiealf | DOUBLE | 96.3% | 4.0 |  |
| carnegieapm | DOUBLE | 96.3% | 1.0 |  |
| carnegiegpm | DOUBLE | 96.3% | 2.0 |  |
| land_grant | DOUBLE | 13.3% | 1.0 |  |
| size_category | DOUBLE | 13.3% | 3.0 |  |
| f1systyp | DOUBLE | 30.9% | 2.0 | Appears in 3 tables, common join key |
| f1sysnam | VARCHAR | 30.9% | -2                                                                               | Appears in 3 tables, common join key |
| f1syscod | DOUBLE | 49.3% | -2.0 |  |
| cbsa | DOUBLE | 22.0% | 26620.0 |  |
| cbsatype | DOUBLE | 22.0% | 1.0 |  |
| csa | DOUBLE | 22.0% | 290.0 |  |
| county_fips | DOUBLE | 30.7% | 1089.0 |  |
| county_name | VARCHAR | 30.7% | Madison County |  |
| cngdstcd | DOUBLE | 30.7% | 105.0 |  |
| longitude | DOUBLE | 30.7% | -86.568502 |  |
| latitude | DOUBLE | 30.7% | 34.783368 |  |
| dfrcgid | DOUBLE | 27.1% | 106.0 |  |
| dfrcuscg | DOUBLE | 49.3% | 1.0 |  |
| year | BIGINT | 0.0% | 2024 | Appears in 26 tables, common join key |
| c21ipug | DOUBLE | 88.5% | 16.0 |  |
| c21ipgrd | DOUBLE | 88.5% | 18.0 |  |
| c21ugprf | DOUBLE | 88.5% | 10.0 |  |
| c21enprf | DOUBLE | 88.5% | 4.0 |  |
| c21szset | DOUBLE | 88.5% | 14.0 |  |
| c18basic | DOUBLE | 88.5% | 18.0 |  |
| c15basic | DOUBLE | 76.3% | 18.0 |  |
| ccbasic | DOUBLE | 62.5% | 18.0 |  |
| carnegie | DOUBLE | 17.0% | 16.0 |  |
| duns | DOUBLE | 57.8% | 197216455.0 |  |
| necta | DOUBLE | 33.3% | -2.0 |  |
| c18ipug | DOUBLE | 87.8% | 16.0 |  |
| c18ipgrd | DOUBLE | 87.8% | 17.0 |  |
| c18ugprf | DOUBLE | 87.8% | 10.0 |  |
| c18enprf | DOUBLE | 87.8% | 4.0 |  |
| c18szset | DOUBLE | 87.8% | 14.0 |  |
| c15ipug | DOUBLE | 86.3% | 16.0 |  |
| c15ipgrd | DOUBLE | 86.3% | 18.0 |  |
| c15ugprf | DOUBLE | 86.3% | 10.0 |  |
| c15enprf | DOUBLE | 86.3% | 4.0 |  |
| c15szset | DOUBLE | 86.3% | 13.0 |  |
| ccipug | DOUBLE | 54.5% | -3.0 |  |
| ccipgrad | DOUBLE | 54.5% | -3.0 |  |
| ccugprof | DOUBLE | 54.5% | -3.0 |  |
| ccenrprf | DOUBLE | 54.5% | -3.0 |  |
| ccsizset | DOUBLE | 54.5% | -3.0 |  |
| faxtele | DOUBLE | 85.1% | 2563725030.0 |  |
| tenursys | DOUBLE | 64.5% | -1.0 | Appears in 3 tables, common join key |
| fpoffer | DOUBLE | 69.3% | 2.0 |  |
| hdegoffr | DOUBLE | 69.3% | 40.0 |  |
| fintele | DOUBLE | 78.3% | 3349532223.0 |  |
| admtele | DOUBLE | 78.2% | 3349532223.0 |  |
| stat_fa | DOUBLE | 91.0% | 1.0 |  |
| stat_ic | DOUBLE | 91.0% | 1.0 | Appears in 3 tables, common join key |
| lock_ic | DOUBLE | 91.0% | 3.0 | Appears in 3 tables, common join key |
| stat_c | DOUBLE | 91.0% | 1.0 | Appears in 3 tables, common join key |
| lock_c | DOUBLE | 91.0% | 8.0 | Appears in 3 tables, common join key |
| prch_c | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| idx_c | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| imp_c | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| stat_wi | DOUBLE | 91.0% | 5.0 |  |
| stat_ef | DOUBLE | 91.0% | 5.0 | Appears in 3 tables, common join key |
| lock_ef | DOUBLE | 91.0% | 0.0 | Appears in 3 tables, common join key |
| prch_ef | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| idx_ef | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| imp_ef | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| pta99_ef | DOUBLE | 91.0% | 5.0 | Appears in 3 tables, common join key |
| ptb_ef | DOUBLE | 91.0% | 5.0 | Appears in 3 tables, common join key |
| ptc_ef | DOUBLE | 91.0% | 5.0 | Appears in 3 tables, common join key |
| ptd_ef | DOUBLE | 91.0% | 5.0 | Appears in 3 tables, common join key |
| pteeffy | DOUBLE | 91.0% | 5.0 | Appears in 3 tables, common join key |
| pteefia | DOUBLE | 91.0% | 5.0 | Appears in 3 tables, common join key |
| fyrpyear | DOUBLE | 91.0% | -1.0 | Appears in 4 tables, common join key |
| stat_sa | DOUBLE | 91.0% | 5.0 | Appears in 3 tables, common join key |
| lock_sa | DOUBLE | 91.0% | 0.0 | Appears in 3 tables, common join key |
| prch_sa | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| idx_sa | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| imp_sa | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| stat_s | DOUBLE | 91.0% | 5.0 | Appears in 3 tables, common join key |
| lock_s | DOUBLE | 91.0% | 0.0 | Appears in 3 tables, common join key |
| prch_s | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| idx_s | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| imp_s | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| stat_eap | DOUBLE | 91.0% | 5.0 | Appears in 3 tables, common join key |
| lock_eap | DOUBLE | 91.0% | 0.0 | Appears in 3 tables, common join key |
| prch_eap | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| idx_eap | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| imp_eap | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| ftemp15 | DOUBLE | 91.0% | 1.0 | Appears in 3 tables, common join key |
| sa_excl | DOUBLE | 91.0% | 2.0 | Appears in 3 tables, common join key |
| stat_sp | DOUBLE | 91.0% | 5.0 |  |
| form_f | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| stat_f | DOUBLE | 91.0% | 5.0 | Appears in 3 tables, common join key |
| lock_f | DOUBLE | 91.0% | 0.0 | Appears in 3 tables, common join key |
| prch_f | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| idx_f | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| imp_f | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| fybeg | DOUBLE | 91.0% | -1.0 | Appears in 3 tables, common join key |
| fyend | DOUBLE | 91.0% | -1.0 | Appears in 3 tables, common join key |
| gpfs | DOUBLE | 91.0% | -1.0 | Appears in 3 tables, common join key |
| f1gasbcr | DOUBLE | 91.0% | -2.0 |  |
| f1gasbal | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| stat_sfa | DOUBLE | 91.0% | 5.0 | Appears in 3 tables, common join key |
| lock_sfa | DOUBLE | 91.0% | 0.0 | Appears in 3 tables, common join key |
| prch_sfa | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| idx_sfa | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| imp_sfa | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| stat_gr | DOUBLE | 91.0% | 5.0 | Appears in 3 tables, common join key |
| lock_gr | DOUBLE | 91.0% | 0.0 | Appears in 3 tables, common join key |
| prch_gr | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| idx_gr | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| imp_gr | DOUBLE | 91.0% | -2.0 | Appears in 3 tables, common join key |
| cohrtstu | DOUBLE | 91.0% | 1.0 | Appears in 3 tables, common join key |
| pyaid | DOUBLE | 91.0% | 2.0 | Appears in 3 tables, common join key |
| cohrtaid | DOUBLE | 91.0% | -1.0 | Appears in 3 tables, common join key |
| sport1 | DOUBLE | 91.0% | -1.0 | Appears in 4 tables, common join key |
| sport2 | DOUBLE | 91.0% | -1.0 | Appears in 4 tables, common join key |
| sport3 | DOUBLE | 91.0% | -1.0 | Appears in 4 tables, common join key |
| sport4 | DOUBLE | 91.0% | -1.0 | Appears in 4 tables, common join key |
| sport5 | DOUBLE | 91.0% | -1.0 | Appears in 3 tables, common join key |
| longpgm | DOUBLE | 91.0% | -1.0 | Appears in 3 tables, common join key |
| cohrtmt | DOUBLE | 91.0% | 1.0 |  |
| tpr | DOUBLE | 91.0% | -1.0 |  |
| hpr | DOUBLE | 91.0% | -1.0 |  |
| cufasb | DOUBLE | 95.7% | -2.0 | Appears in 3 tables, common join key |
| cugasb | DOUBLE | 95.7% | -2.0 | Appears in 3 tables, common join key |
| fte | DOUBLE | 91.9% | 5881.0 |  |
| ocrmsi | DOUBLE | 91.0% | -2.0 |  |
| ocrhsi | DOUBLE | 91.0% | -2.0 |  |
| twoyrcat | DOUBLE | 95.7% | -4.0 |  |
| rev_c | DOUBLE | 95.7% | 0.0 | Appears in 3 tables, common join key |
| rev_ef | DOUBLE | 95.7% | 0.0 | Appears in 3 tables, common join key |
| rev_sa | DOUBLE | 95.7% | 0.0 | Appears in 3 tables, common join key |
| rev_s | DOUBLE | 95.7% | 0.0 | Appears in 3 tables, common join key |
| rev_eap | DOUBLE | 95.7% | 0.0 | Appears in 3 tables, common join key |
| r_form_f | DOUBLE | 95.7% | -2.0 |  |
| rev_f | DOUBLE | 95.7% | 0.0 | Appears in 3 tables, common join key |
| rev_sfa | DOUBLE | 95.7% | 0.0 | Appears in 3 tables, common join key |
| rev_gr | DOUBLE | 95.7% | 0.0 | Appears in 3 tables, common join key |
| affil | DOUBLE | 95.3% | -3.0 |  |
| pctmin1 | DOUBLE | 95.3% | -1.0 |  |
| pctmin2 | DOUBLE | 95.3% | -1.0 |  |
| pctmin3 | DOUBLE | 95.3% | -1.0 |  |
| pctmin4 | DOUBLE | 95.3% | -1.0 |  |
| ptacipef | DOUBLE | 95.3% | -2.0 | Appears in 3 tables, common join key |
| transver | DOUBLE | 95.3% | -1.0 |  |
| cindon | DOUBLE | 97.6% | 9340.0 | Appears in 3 tables, common join key |
| cinson | DOUBLE | 97.6% | 9340.0 | Appears in 3 tables, common join key |
| cotson | DOUBLE | 97.6% | 11860.0 | Appears in 3 tables, common join key |
| cindoff | DOUBLE | 97.7% | 11340.0 | Appears in 3 tables, common join key |
| cinsoff | DOUBLE | 97.7% | 11340.0 | Appears in 3 tables, common join key |
| cotsoff | DOUBLE | 97.7% | 13860.0 | Appears in 3 tables, common join key |
| cindfam | DOUBLE | 97.7% | 4440.0 | Appears in 3 tables, common join key |
| cinsfam | DOUBLE | 97.7% | 4440.0 | Appears in 3 tables, common join key |
| cotsfam | DOUBLE | 97.7% | 6960.0 | Appears in 3 tables, common join key |

## ic

Rows: 174,441

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| peo1istr | BIGINT | 0.0% | 0 |  |
| peo2istr | BIGINT | 0.0% | 1 |  |
| peo3istr | BIGINT | 0.0% | 0 |  |
| peo4istr | BIGINT | 0.0% | 0 |  |
| peo5istr | BIGINT | 0.0% | 0 |  |
| peo6istr | BIGINT | 0.0% | 0 |  |
| peo7istr | DOUBLE | 89.6% | 0.0 |  |
| cntlaffi | BIGINT | 0.0% | 1 |  |
| pubprime | BIGINT | 0.0% | 2 |  |
| pubsecon | BIGINT | 0.0% | 0 |  |
| relaffil | BIGINT | 0.0% | -2 |  |
| level1 | BIGINT | 0.0% | 0 |  |
| level1a | DOUBLE | 82.5% | 0.0 |  |
| level1b | DOUBLE | 82.5% | 0.0 |  |
| level2 | BIGINT | 0.0% | 0 |  |
| level3 | BIGINT | 0.0% | 0 |  |
| level4 | BIGINT | 0.0% | 0 |  |
| level5 | BIGINT | 0.0% | 1 |  |
| level6 | BIGINT | 0.0% | 0 |  |
| level7 | BIGINT | 0.0% | 1 |  |
| level8 | BIGINT | 0.0% | 1 |  |
| level12 | BIGINT | 0.0% | 0 |  |
| level17 | DOUBLE | 33.0% | 1.0 |  |
| level18 | DOUBLE | 33.0% | 0.0 |  |
| level19 | DOUBLE | 33.0% | 0.0 |  |
| calsys | BIGINT | 0.0% | 1 |  |
| ft_ug | BIGINT | 0.0% | 1 |  |
| ft_ftug | BIGINT | 0.0% | 1 |  |
| ftgdnidp | DOUBLE | 49.7% | 1.0 |  |
| pt_ug | DOUBLE | 9.4% | 1.0 |  |
| pt_ftug | DOUBLE | 9.4% | 1.0 |  |
| ptgdnidp | DOUBLE | 49.7% | 1.0 |  |
| docpp | DOUBLE | 49.7% | -2.0 |  |
| docppsp | DOUBLE | 49.7% | -2.0 |  |
| openadmp | BIGINT | 0.0% | 2 |  |
| noncrdt1 | DOUBLE | 89.6% | 0.0 |  |
| noncrdt2 | DOUBLE | 89.6% | 0.0 |  |
| noncrdt3 | DOUBLE | 89.6% | 1.0 |  |
| noncrdt4 | DOUBLE | 89.6% | 0.0 |  |
| noncrdt5 | DOUBLE | 89.6% | 0.0 |  |
| noncrdt6 | DOUBLE | 89.6% | 0.0 |  |
| noncrdt7 | DOUBLE | 89.6% | 0.0 |  |
| noncrdt8 | DOUBLE | 89.6% | 0.0 |  |
| noncrdt9 | DOUBLE | 89.6% | 0.0 |  |
| vet1 | DOUBLE | 58.4% | 0.0 |  |
| vet2 | DOUBLE | 58.4% | 1.0 |  |
| vet3 | DOUBLE | 58.4% | 1.0 |  |
| vet4 | DOUBLE | 58.4% | 1.0 |  |
| vet5 | DOUBLE | 58.4% | 1.0 |  |
| vet9 | DOUBLE | 58.4% | 0.0 |  |
| credits2 | DOUBLE | 5.5% | 0.0 |  |
| credits3 | DOUBLE | 5.5% | 1.0 |  |
| credits4 | DOUBLE | 5.5% | 0.0 |  |
| slo5 | DOUBLE | 5.5% | 1.0 |  |
| slo51 | DOUBLE | 5.5% | 1.0 |  |
| slo52 | DOUBLE | 5.5% | 0.0 |  |
| slo521 | DOUBLE | 89.6% | 0.0 |  |
| slo53 | DOUBLE | 5.5% | 0.0 |  |
| slo6 | DOUBLE | 5.5% | 1.0 |  |
| slo7 | DOUBLE | 5.5% | 1.0 |  |
| sloa | DOUBLE | 89.6% | 1.0 |  |
| slo8 | DOUBLE | 5.5% | 1.0 |  |
| slo81 | DOUBLE | 5.5% | 1.0 |  |
| slo82 | DOUBLE | 5.5% | 0.0 |  |
| slo83 | DOUBLE | 5.5% | 1.0 |  |
| slob | DOUBLE | 89.6% | 0.0 |  |
| slo9 | DOUBLE | 5.5% | 0.0 |  |
| yrscoll | BIGINT | 0.0% | -2 |  |
| stusrv2 | BIGINT | 0.0% | 1 |  |
| stusrv3 | BIGINT | 0.0% | 1 |  |
| stusrv4 | BIGINT | 0.0% | 1 |  |
| stusrv8 | BIGINT | 0.0% | 1 |  |
| stusrv9 | BIGINT | 0.0% | 0 |  |
| libres1 | DOUBLE | 67.0% | 1.0 |  |
| libres2 | DOUBLE | 67.0% | 1.0 |  |
| libres3 | DOUBLE | 67.0% | 1.0 |  |
| libres4 | DOUBLE | 67.0% | 1.0 |  |
| libres5 | DOUBLE | 67.0% | 1.0 |  |
| libres6 | DOUBLE | 67.0% | 1.0 |  |
| libres9 | DOUBLE | 67.0% | 0.0 |  |
| dstnugc | DOUBLE | 71.0% | 1.0 |  |
| dstnugp | DOUBLE | 71.0% | 1.0 |  |
| dstnugn | DOUBLE | 71.0% | 0.0 |  |
| dstngc | DOUBLE | 71.0% | 1.0 |  |
| dstngp | DOUBLE | 71.0% | 1.0 |  |
| dstngn | DOUBLE | 71.0% | 0.0 |  |
| distcrs | DOUBLE | 67.0% | 1.0 |  |
| distpgs | DOUBLE | 71.0% | 1.0 |  |
| dstnced1 | DOUBLE | 49.7% | 1.0 |  |
| dstnced2 | DOUBLE | 49.7% | 1.0 |  |
| dstnced3 | DOUBLE | 49.7% | 0.0 |  |
| distnced | DOUBLE | 45.3% | 2.0 |  |
| disab | DOUBLE | 37.0% | 2.0 |  |
| xdisabpc | VARCHAR | 37.0% | R |  |
| disabpct | VARCHAR | 37.0% | 3.42 |  |
| athassoc | BIGINT | 0.0% | 1 |  |
| assoc1 | BIGINT | 0.0% | 1 |  |
| assoc2 | BIGINT | 0.0% | 0 |  |
| assoc3 | BIGINT | 0.0% | 0 |  |
| assoc4 | BIGINT | 0.0% | 0 |  |
| assoc5 | BIGINT | 0.0% | 0 |  |
| assoc6 | BIGINT | 0.0% | 0 |  |
| sport1 | BIGINT | 0.0% | 1 | Appears in 4 tables, common join key |
| confno1 | BIGINT | 0.0% | 133 |  |
| sport2 | BIGINT | 0.0% | 1 | Appears in 4 tables, common join key |
| confno2 | BIGINT | 0.0% | 133 |  |
| sport3 | BIGINT | 0.0% | 1 | Appears in 4 tables, common join key |
| confno3 | BIGINT | 0.0% | 133 |  |
| sport4 | BIGINT | 0.0% | 1 | Appears in 4 tables, common join key |
| confno4 | BIGINT | 0.0% | 133 |  |
| year | BIGINT | 0.0% | 2024 | Appears in 26 tables, common join key |
| enrhsst | DOUBLE | 96.5% | 1.0 |  |
| enrhsst1 | DOUBLE | 96.5% | 1.0 |  |
| enrhsst2 | DOUBLE | 96.5% | 0.0 |  |
| tuitpl | DOUBLE | 36.4% | 1.0 |  |
| tuitpl1 | DOUBLE | 36.4% | 0.0 |  |
| tuitpl2 | DOUBLE | 36.4% | 0.0 |  |
| tuitpl3 | DOUBLE | 36.4% | 1.0 |  |
| tuitpl4 | DOUBLE | 36.4% | 0.0 |  |
| prmpgm | DOUBLE | 93.0% | 2.0 |  |
| alloncam | DOUBLE | 20.7% | 2.0 |  |
| tuitvary | DOUBLE | 3.4% | 1.0 |  |
| room | DOUBLE | 3.4% | 1.0 |  |
| xroomcap | VARCHAR | 3.4% | R |  |
| roomcap | VARCHAR | 15.7% | 3620 |  |
| board | DOUBLE | 3.4% | 1.0 |  |
| xmealswk | VARCHAR | 3.4% | R |  |
| mealswk | VARCHAR | 17.7% | 21 |  |
| xroomamt | VARCHAR | 3.4% | R |  |
| roomamt | VARCHAR | 16.7% | 3790 |  |
| xbordamt | VARCHAR | 3.4% | R |  |
| boardamt | VARCHAR | 17.4% | 4202 |  |
| xrmbdamt | VARCHAR | 3.4% | A |  |
| rmbrdamt | VARCHAR | 19.7% | . |  |
| xappfeeu | VARCHAR | 3.4% | R |  |
| applfeeu | DOUBLE | 21.6% | 30.0 |  |
| xappfeeg | VARCHAR | 3.4% | R |  |
| applfeeg | VARCHAR | 16.4% | 45 |  |
| credits1 | DOUBLE | 12.3% | 1.0 |  |
| stusrv1 | DOUBLE | 10.4% | 1.0 |  |
| libfac | DOUBLE | 33.0% | 1.0 |  |
| admcon1 | DOUBLE | 41.6% | 1.0 |  |
| admcon2 | DOUBLE | 41.6% | 2.0 |  |
| admcon3 | DOUBLE | 41.6% | 1.0 |  |
| admcon4 | DOUBLE | 41.6% | 2.0 |  |
| admcon5 | DOUBLE | 41.6% | 3.0 |  |
| admcon6 | DOUBLE | 41.6% | 2.0 |  |
| admcon7 | DOUBLE | 41.6% | 1.0 |  |
| admcon8 | DOUBLE | 41.6% | 1.0 |  |
| admcon9 | DOUBLE | 62.7% | 3.0 |  |
| appdate | DOUBLE | 47.0% | 2.0 |  |
| xapplcnm | VARCHAR | 47.0% | R |  |
| applcnm | VARCHAR | 54.1% | 2401 |  |
| xapplcnw | VARCHAR | 47.0% | R |  |
| applcnw | VARCHAR | 54.1% | 3741 |  |
| xadmssnm | VARCHAR | 47.0% | R |  |
| admssnm | VARCHAR | 54.0% | 2100 |  |
| xadmssnw | VARCHAR | 47.0% | R |  |
| admssnw | VARCHAR | 54.0% | 3421 |  |
| xenrlftm | VARCHAR | 47.0% | R |  |
| enrlftm | VARCHAR | 54.0% | 533 |  |
| xenrlftw | VARCHAR | 47.0% | R |  |
| enrlftw | VARCHAR | 54.0% | 556 |  |
| xenrlptm | VARCHAR | 47.0% | R |  |
| enrlptm | VARCHAR | 54.4% | 9 |  |
| xenrlptw | VARCHAR | 47.0% | R |  |
| enrlptw | VARCHAR | 54.4% | 6 |  |
| satactdt | DOUBLE | 47.0% | 2.0 |  |
| xsatnum | VARCHAR | 47.0% | R |  |
| satnum | VARCHAR | 56.2% | 167 |  |
| xsatpct | VARCHAR | 47.0% | R |  |
| satpct | VARCHAR | 56.2% | 15 |  |
| xactnum | VARCHAR | 47.0% | R |  |
| actnum | VARCHAR | 56.3% | 968 |  |
| xactpct | VARCHAR | 47.0% | R |  |
| actpct | VARCHAR | 56.4% | 88 |  |
| xsatvr25 | VARCHAR | 47.0% | R |  |
| satvr25 | VARCHAR | 56.9% | 370 |  |
| xsatvr75 | VARCHAR | 47.0% | R |  |
| satvr75 | VARCHAR | 56.9% | 450 |  |
| xsatmt25 | VARCHAR | 47.0% | R |  |
| satmt25 | VARCHAR | 56.9% | 350 |  |
| xsatmt75 | VARCHAR | 47.0% | R |  |
| satmt75 | VARCHAR | 56.9% | 450 |  |
| xsatwr25 | VARCHAR | 66.6% | B |  |
| satwr25 | VARCHAR | 66.6% | . |  |
| xsatwr75 | VARCHAR | 66.6% | B |  |
| satwr75 | VARCHAR | 66.6% | . |  |
| xactcm25 | VARCHAR | 47.0% | R |  |
| actcm25 | VARCHAR | 57.2% | 15 |  |
| xactcm75 | VARCHAR | 47.0% | R |  |
| actcm75 | VARCHAR | 57.2% | 19 |  |
| xacten25 | VARCHAR | 47.0% | R |  |
| acten25 | VARCHAR | 57.6% | 14 |  |
| xacten75 | VARCHAR | 47.0% | R |  |
| acten75 | VARCHAR | 57.6% | 19 |  |
| xactmt25 | VARCHAR | 47.0% | R |  |
| actmt25 | VARCHAR | 57.6% | 15 |  |
| xactmt75 | VARCHAR | 47.0% | R |  |
| actmt75 | VARCHAR | 57.6% | 18 |  |
| xactwr25 | VARCHAR | 74.6% | B |  |
| actwr25 | VARCHAR | 74.6% | . |  |
| xactwr75 | VARCHAR | 74.6% | B |  |
| actwr75 | VARCHAR | 74.6% | . |  |
| xenrlm | VARCHAR | 51.0% | R |  |
| enrlm | VARCHAR | 53.2% | 542 |  |
| xenrlw | VARCHAR | 51.0% | R |  |
| enrlw | VARCHAR | 53.3% | 562 |  |
| xenrlt | VARCHAR | 51.0% | R |  |
| enrlt | VARCHAR | 53.2% | 1104 |  |
| xapplcn | VARCHAR | 51.0% | R |  |
| applcn | VARCHAR | 53.2% | 6142 |  |
| xadmssn | VARCHAR | 51.0% | R |  |
| admssn | VARCHAR | 53.2% | 5521 |  |
| xenrlft | VARCHAR | 51.0% | R |  |
| enrlft | VARCHAR | 53.2% | 1089 |  |
| xenrlpt | VARCHAR | 51.0% | R |  |
| enrlpt | VARCHAR | 53.4% | 15 |  |
| slo3 | DOUBLE | 55.8% | 1.0 |  |
| ft_gd | DOUBLE | 50.3% | 2.0 |  |
| pt_gd | DOUBLE | 59.7% | 2.0 |  |
| pctpost | DOUBLE | 58.9% | -2.0 |  |
| level9 | DOUBLE | 63.0% | -2.0 |  |
| level10 | DOUBLE | 63.0% | -2.0 |  |
| level11 | DOUBLE | 63.0% | -2.0 |  |
| xappfeep | VARCHAR | 63.0% | A |  |
| applfeep | VARCHAR | 78.4% | . |  |
| ft_fp | DOUBLE | 63.0% | -2.0 |  |
| pt_fp | DOUBLE | 80.2% | -2.0 |  |
| apfee | DOUBLE | 71.0% | 2.0 |  |
| accrd1 | DOUBLE | 78.8% | 1.0 |  |
| accrd2 | DOUBLE | 78.8% | 1.0 |  |
| regaccrd | DOUBLE | 78.8% | 8.0 |  |
| accrd3 | DOUBLE | 78.8% | 1.0 |  |
| accrd4 | DOUBLE | 78.8% | 0.0 |  |
| saccr | DOUBLE | 78.8% | 1.0 |  |
| slo1 | DOUBLE | 84.3% | 1.0 |  |
| slo2 | DOUBLE | 84.3% | 1.0 |  |
| slo4 | DOUBLE | 84.3% | 1.0 |  |
| insttoyr | DOUBLE | 78.8% | -2.0 |  |
| fopna | DOUBLE | 82.7% | 2.0 |  |
| fopna1 | DOUBLE | 82.7% | 0.0 |  |
| fopna2 | DOUBLE | 82.7% | 0.0 |  |
| ftstu | DOUBLE | 86.7% | 1.0 |  |
| ptstu | DOUBLE | 96.1% | 1.0 |  |
| rotc | DOUBLE | 94.5% | 2.0 |  |
| rotc1 | DOUBLE | 94.5% | -2.0 |  |
| rotc2 | DOUBLE | 94.5% | -2.0 |  |
| rotc3 | DOUBLE | 94.5% | -2.0 |  |

## ic_ay

Rows: 90,151

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| xtuit1 | VARCHAR | 0.0% | R |  |
| tuition_in_district | DOUBLE | 9.9% | 8610.0 |  |
| xfee1 | VARCHAR | 0.0% | R |  |
| fee1 | DOUBLE | 10.1% | 1414.0 |  |
| xhrchg1 | VARCHAR | 0.0% | R |  |
| hrchg1 | DOUBLE | 20.9% | 287.0 |  |
| xtuit2 | VARCHAR | 0.0% | R |  |
| tuition_in_state | DOUBLE | 9.9% | 8610.0 |  |
| xfee2 | VARCHAR | 0.0% | R |  |
| fee2 | DOUBLE | 10.1% | 1414.0 |  |
| xhrchg2 | VARCHAR | 0.0% | R |  |
| hrchg2 | DOUBLE | 20.9% | 287.0 |  |
| xtuit3 | VARCHAR | 0.0% | R |  |
| tuition_out_state | DOUBLE | 9.9% | 17220.0 |  |
| xfee3 | VARCHAR | 0.0% | R |  |
| fee3 | DOUBLE | 10.1% | 1414.0 |  |
| xhrchg3 | VARCHAR | 0.0% | R |  |
| hrchg3 | DOUBLE | 20.6% | 574.0 |  |
| xtuit5 | VARCHAR | 0.0% | R |  |
| tuition5 | VARCHAR | 15.6% | 10128 |  |
| xfee5 | VARCHAR | 0.0% | R |  |
| fee5 | VARCHAR | 15.7% | 1414 |  |
| xhrchg5 | VARCHAR | 0.0% | R |  |
| hrchg5 | VARCHAR | 15.9% | 422 |  |
| xtuit6 | VARCHAR | 0.0% | R |  |
| tuition6 | VARCHAR | 15.6% | 10128 |  |
| xfee6 | VARCHAR | 0.0% | R |  |
| fee6 | VARCHAR | 15.7% | 1414 |  |
| xhrchg6 | VARCHAR | 0.0% | R |  |
| hrchg6 | VARCHAR | 15.9% | 422 |  |
| xtuit7 | VARCHAR | 0.0% | R |  |
| tuition7 | VARCHAR | 15.6% | 20160 |  |
| xfee7 | VARCHAR | 0.0% | R |  |
| fee7 | VARCHAR | 15.7% | 1414 |  |
| xhrchg7 | VARCHAR | 0.0% | R |  |
| hrchg7 | VARCHAR | 15.8% | 840 |  |
| xispro1 | VARCHAR | 0.0% | A |  |
| isprof1 | VARCHAR | 23.1% | . |  |
| xispfe1 | VARCHAR | 0.0% | A |  |
| ispfee1 | VARCHAR | 23.1% | . |  |
| xospro1 | VARCHAR | 0.0% | A |  |
| osprof1 | VARCHAR | 23.1% | . |  |
| xospfe1 | VARCHAR | 0.0% | A |  |
| ospfee1 | VARCHAR | 23.1% | . |  |
| xispro2 | VARCHAR | 0.0% | A |  |
| isprof2 | VARCHAR | 22.9% | . |  |
| xispfe2 | VARCHAR | 0.0% | A |  |
| ispfee2 | VARCHAR | 22.9% | . |  |
| xospro2 | VARCHAR | 0.0% | A |  |
| osprof2 | VARCHAR | 22.9% | . |  |
| xospfe2 | VARCHAR | 0.0% | A |  |
| ospfee2 | VARCHAR | 22.9% | . |  |
| xispro3 | VARCHAR | 0.0% | A |  |
| isprof3 | VARCHAR | 22.6% | . |  |
| xispfe3 | VARCHAR | 0.0% | A |  |
| ispfee3 | VARCHAR | 22.6% | . |  |
| xospro3 | VARCHAR | 0.0% | A |  |
| osprof3 | VARCHAR | 22.6% | . |  |
| xospfe3 | VARCHAR | 0.0% | A |  |
| ospfee3 | VARCHAR | 22.6% | . |  |
| xispro4 | VARCHAR | 0.0% | A |  |
| isprof4 | VARCHAR | 23.1% | . |  |
| xispfe4 | VARCHAR | 0.0% | A |  |
| ispfee4 | VARCHAR | 23.1% | . |  |
| xospro4 | VARCHAR | 0.0% | A |  |
| osprof4 | VARCHAR | 23.1% | . |  |
| xospfe4 | VARCHAR | 0.0% | A |  |
| ospfee4 | VARCHAR | 23.1% | . |  |
| xispro5 | VARCHAR | 0.0% | A |  |
| isprof5 | VARCHAR | 23.1% | . |  |
| xispfe5 | VARCHAR | 0.0% | A |  |
| ispfee5 | VARCHAR | 23.1% | . |  |
| xospro5 | VARCHAR | 0.0% | A |  |
| osprof5 | VARCHAR | 23.1% | . |  |
| xospfe5 | VARCHAR | 0.0% | A |  |
| ospfee5 | VARCHAR | 23.1% | . |  |
| xispro6 | VARCHAR | 0.0% | A |  |
| isprof6 | VARCHAR | 22.8% | . |  |
| xispfe6 | VARCHAR | 0.0% | A |  |
| ispfee6 | VARCHAR | 22.8% | . |  |
| xospro6 | VARCHAR | 0.0% | A |  |
| osprof6 | VARCHAR | 22.8% | . |  |
| xospfe6 | VARCHAR | 0.0% | A |  |
| ospfee6 | VARCHAR | 22.8% | . |  |
| xispro7 | VARCHAR | 0.0% | A |  |
| isprof7 | VARCHAR | 23.1% | . |  |
| xispfe7 | VARCHAR | 0.0% | A |  |
| ispfee7 | VARCHAR | 23.1% | . |  |
| xospro7 | VARCHAR | 0.0% | A |  |
| osprof7 | VARCHAR | 23.1% | . |  |
| xospfe7 | VARCHAR | 0.0% | A |  |
| ospfee7 | VARCHAR | 23.1% | . |  |
| xispro8 | VARCHAR | 0.0% | A |  |
| isprof8 | VARCHAR | 23.0% | . |  |
| xispfe8 | VARCHAR | 0.0% | A |  |
| ispfee8 | VARCHAR | 23.0% | . |  |
| xospro8 | VARCHAR | 0.0% | A |  |
| osprof8 | VARCHAR | 23.0% | . |  |
| xospfe8 | VARCHAR | 0.0% | A |  |
| ospfee8 | VARCHAR | 23.0% | . |  |
| xispro9 | VARCHAR | 0.0% | A |  |
| isprof9 | VARCHAR | 22.3% | . |  |
| xispfe9 | VARCHAR | 0.0% | A |  |
| ispfee9 | VARCHAR | 22.3% | . |  |
| xospro9 | VARCHAR | 0.0% | A |  |
| osprof9 | VARCHAR | 22.3% | . |  |
| xospfe9 | VARCHAR | 0.0% | A |  |
| ospfee9 | VARCHAR | 22.3% | . |  |
| xchg1at0 | VARCHAR | 48.6% | R |  |
| chg1at0 | DOUBLE | 54.9% | 8610.0 |  |
| xchg1af0 | VARCHAR | 48.6% | R |  |
| chg1af0 | DOUBLE | 54.9% | 1414.0 |  |
| xchg1ay0 | VARCHAR | 48.6% | R |  |
| chg1ay0 | DOUBLE | 54.9% | 10024.0 |  |
| xchg1at1 | VARCHAR | 48.6% | R |  |
| chg1at1 | DOUBLE | 54.7% | 8610.0 |  |
| xchg1af1 | VARCHAR | 48.6% | R |  |
| chg1af1 | DOUBLE | 54.7% | 1414.0 |  |
| xchg1ay1 | VARCHAR | 0.0% | R |  |
| chg1ay1 | DOUBLE | 15.1% | 10024.0 |  |
| xchg1at2 | VARCHAR | 48.6% | R |  |
| chg1at2 | DOUBLE | 54.5% | 8610.0 |  |
| xchg1af2 | VARCHAR | 48.6% | R |  |
| chg1af2 | DOUBLE | 54.5% | 1414.0 |  |
| xchg1ay2 | VARCHAR | 0.0% | R |  |
| chg1ay2 | DOUBLE | 14.4% | 10024.0 |  |
| xchg1at3 | VARCHAR | 48.6% | R |  |
| chg1at3 | DOUBLE | 54.4% | 8610.0 |  |
| xchg1af3 | VARCHAR | 48.6% | R |  |
| chg1af3 | DOUBLE | 54.4% | 1414.0 |  |
| xchg1ay3 | VARCHAR | 0.0% | R |  |
| chg1ay3 | DOUBLE | 13.8% | 10024.0 |  |
| chg1tgtd | VARCHAR | 48.6% | . |  |
| chg1fgtd | VARCHAR | 48.6% | . |  |
| xchg2at0 | VARCHAR | 48.6% | R |  |
| chg2at0 | DOUBLE | 54.9% | 8610.0 |  |
| xchg2af0 | VARCHAR | 48.6% | R |  |
| chg2af0 | DOUBLE | 54.9% | 1414.0 |  |
| xchg2ay0 | VARCHAR | 48.6% | R |  |
| chg2ay0 | DOUBLE | 54.9% | 10024.0 |  |
| xchg2at1 | VARCHAR | 48.6% | R |  |
| chg2at1 | DOUBLE | 54.7% | 8610.0 |  |
| xchg2af1 | VARCHAR | 48.6% | R |  |
| chg2af1 | DOUBLE | 54.7% | 1414.0 |  |
| xchg2ay1 | VARCHAR | 0.0% | R |  |
| chg2ay1 | DOUBLE | 14.7% | 10024.0 |  |
| xchg2at2 | VARCHAR | 48.6% | R |  |
| chg2at2 | DOUBLE | 54.5% | 8610.0 |  |
| xchg2af2 | VARCHAR | 48.6% | R |  |
| chg2af2 | DOUBLE | 54.5% | 1414.0 |  |
| xchg2ay2 | VARCHAR | 0.0% | R |  |
| chg2ay2 | DOUBLE | 14.1% | 10024.0 |  |
| xchg2at3 | VARCHAR | 48.6% | R |  |
| chg2at3 | DOUBLE | 54.4% | 8610.0 |  |
| xchg2af3 | VARCHAR | 48.6% | R |  |
| chg2af3 | DOUBLE | 54.4% | 1414.0 |  |
| xchg2ay3 | VARCHAR | 0.0% | R |  |
| chg2ay3 | DOUBLE | 13.8% | 10024.0 |  |
| chg2tgtd | VARCHAR | 48.6% | . |  |
| chg2fgtd | VARCHAR | 48.6% | . |  |
| xchg3at0 | VARCHAR | 48.6% | R |  |
| chg3at0 | DOUBLE | 54.9% | 17220.0 |  |
| xchg3af0 | VARCHAR | 48.6% | R |  |
| chg3af0 | DOUBLE | 54.9% | 1414.0 |  |
| xchg3ay0 | VARCHAR | 48.6% | R |  |
| chg3ay0 | DOUBLE | 54.9% | 18634.0 |  |
| xchg3at1 | VARCHAR | 48.6% | R |  |
| chg3at1 | DOUBLE | 54.7% | 17220.0 |  |
| xchg3af1 | VARCHAR | 48.6% | R |  |
| chg3af1 | DOUBLE | 54.7% | 1414.0 |  |
| xchg3ay1 | VARCHAR | 0.0% | R |  |
| chg3ay1 | DOUBLE | 14.8% | 18634.0 |  |
| xchg3at2 | VARCHAR | 48.6% | R |  |
| chg3at2 | DOUBLE | 54.5% | 17220.0 |  |
| xchg3af2 | VARCHAR | 48.6% | R |  |
| chg3af2 | DOUBLE | 54.5% | 1414.0 |  |
| xchg3ay2 | VARCHAR | 0.0% | R |  |
| chg3ay2 | DOUBLE | 14.1% | 18634.0 |  |
| xchg3at3 | VARCHAR | 48.6% | R |  |
| chg3at3 | DOUBLE | 54.4% | 17220.0 |  |
| xchg3af3 | VARCHAR | 48.6% | R |  |
| chg3af3 | DOUBLE | 54.4% | 1414.0 |  |
| xchg3ay3 | VARCHAR | 0.0% | R |  |
| chg3ay3 | DOUBLE | 13.8% | 18634.0 |  |
| chg3tgtd | VARCHAR | 48.6% | . |  |
| chg3fgtd | VARCHAR | 48.6% | . |  |
| xchg4ay0 | VARCHAR | 48.6% | R |  |
| chg4ay0 | DOUBLE | 56.4% | 1600.0 |  |
| xchg4ay1 | VARCHAR | 0.0% | R |  |
| chg4ay1 | DOUBLE | 16.7% | 1600.0 |  |
| xchg4ay2 | VARCHAR | 0.0% | R |  |
| chg4ay2 | DOUBLE | 16.1% | 1600.0 |  |
| xchg4ay3 | VARCHAR | 0.0% | R |  |
| chg4ay3 | DOUBLE | 16.0% | 2192.0 |  |
| xchg5ay0 | VARCHAR | 48.6% | R |  |
| chg5ay0 | VARCHAR | 48.6% | 9240 |  |
| xchg5ay1 | VARCHAR | 0.0% | R |  |
| chg5ay1 | VARCHAR | 14.6% | 9520 |  |
| xchg5ay2 | VARCHAR | 0.0% | R |  |
| chg5ay2 | VARCHAR | 14.5% | 9520 |  |
| xchg5ay3 | VARCHAR | 0.0% | R |  |
| chg5ay3 | VARCHAR | 14.7% | 11402 |  |
| xchg6ay0 | VARCHAR | 48.6% | R |  |
| chg6ay0 | VARCHAR | 48.6% | 3090 |  |
| xchg6ay1 | VARCHAR | 0.0% | R |  |
| chg6ay1 | VARCHAR | 14.8% | 3090 |  |
| xchg6ay2 | VARCHAR | 0.0% | R |  |
| chg6ay2 | VARCHAR | 14.7% | 3090 |  |
| xchg6ay3 | VARCHAR | 0.0% | R |  |
| chg6ay3 | VARCHAR | 14.8% | 3864 |  |
| xchg7ay0 | VARCHAR | 48.6% | R |  |
| chg7ay0 | DOUBLE | 56.5% | 9240.0 |  |
| xchg7ay1 | VARCHAR | 0.0% | R |  |
| chg7ay1 | DOUBLE | 20.9% | 9520.0 |  |
| xchg7ay2 | VARCHAR | 0.0% | R |  |
| chg7ay2 | DOUBLE | 20.0% | 9520.0 |  |
| xchg7ay3 | VARCHAR | 0.0% | R |  |
| chg7ay3 | DOUBLE | 19.3% | 11402.0 |  |
| xchg8ay0 | VARCHAR | 48.6% | R |  |
| chg8ay0 | DOUBLE | 56.5% | 3090.0 |  |
| xchg8ay1 | VARCHAR | 0.0% | R |  |
| chg8ay1 | DOUBLE | 21.1% | 3090.0 |  |
| xchg8ay2 | VARCHAR | 0.0% | R |  |
| chg8ay2 | DOUBLE | 20.2% | 3090.0 |  |
| xchg8ay3 | VARCHAR | 0.0% | R |  |
| chg8ay3 | DOUBLE | 19.4% | 3864.0 |  |
| xchg9ay0 | VARCHAR | 48.6% | R |  |
| chg9ay0 | DOUBLE | 56.4% | 3440.0 |  |
| xchg9ay1 | VARCHAR | 0.0% | R |  |
| chg9ay1 | DOUBLE | 21.1% | 3440.0 |  |
| xchg9ay2 | VARCHAR | 0.0% | R |  |
| chg9ay2 | DOUBLE | 19.9% | 3440.0 |  |
| xchg9ay3 | VARCHAR | 0.0% | R |  |
| chg9ay3 | DOUBLE | 19.1% | 4271.0 |  |
| year | BIGINT | 0.0% | 2023 | Appears in 26 tables, common join key |
| xcmpfee1 | VARCHAR | 51.4% | A |  |
| cmpfee1 | VARCHAR | 74.5% | . |  |
| xcmpfee2 | VARCHAR | 51.4% | A |  |
| cmpfee2 | VARCHAR | 74.5% | . |  |
| xcmpfee3 | VARCHAR | 51.4% | A |  |
| cmpfee3 | VARCHAR | 74.5% | . |  |
| xcmp1ay0 | INTEGER | 100.0% |  |  |
| cmp1ay0 | INTEGER | 100.0% |  |  |
| xcmp1ay1 | VARCHAR | 74.6% | A |  |
| cmp1ay1 | VARCHAR | 74.6% | . |  |
| xcmp1ay2 | VARCHAR | 74.6% | A |  |
| cmp1ay2 | VARCHAR | 74.6% | . |  |
| xcmp1ay3 | VARCHAR | 74.6% | A |  |
| cmp1ay3 | VARCHAR | 74.6% | . |  |
| cmp1gtd | INTEGER | 100.0% |  |  |
| xcmp2ay0 | INTEGER | 100.0% |  |  |
| cmp2ay0 | INTEGER | 100.0% |  |  |
| xcmp2ay1 | VARCHAR | 74.6% | A |  |
| cmp2ay1 | VARCHAR | 74.6% | . |  |
| xcmp2ay2 | VARCHAR | 74.6% | A |  |
| cmp2ay2 | VARCHAR | 74.6% | . |  |
| xcmp2ay3 | VARCHAR | 74.6% | A |  |
| cmp2ay3 | VARCHAR | 74.6% | . |  |
| cmp2gtd | INTEGER | 100.0% |  |  |
| xcmp3ay0 | INTEGER | 100.0% |  |  |
| cmp3ay0 | INTEGER | 100.0% |  |  |
| xcmp3ay1 | VARCHAR | 74.6% | A |  |
| cmp3ay1 | VARCHAR | 74.6% | . |  |
| xcmp3ay2 | VARCHAR | 74.6% | A |  |
| cmp3ay2 | VARCHAR | 74.6% | . |  |
| xcmp3ay3 | VARCHAR | 74.6% | A |  |
| cmp3ay3 | VARCHAR | 74.6% | . |  |
| cmp3gtd | INTEGER | 100.0% |  |  |
| xispro10 | VARCHAR | 51.4% | A |  |
| isprof10 | VARCHAR | 73.6% | . |  |
| xispfe10 | VARCHAR | 51.4% | A |  |
| ispfee10 | VARCHAR | 73.6% | . |  |
| xospro10 | VARCHAR | 51.4% | A |  |
| osprof10 | VARCHAR | 73.6% | . |  |
| xospfe10 | VARCHAR | 51.4% | A |  |
| ospfee10 | VARCHAR | 73.6% | . |  |
| xispro11 | VARCHAR | 51.4% | A |  |
| isprof11 | VARCHAR | 74.4% | . |  |
| xispfe11 | VARCHAR | 51.4% | A |  |
| ispfee11 | VARCHAR | 74.4% | . |  |
| xospro11 | VARCHAR | 51.4% | A |  |
| osprof11 | VARCHAR | 74.4% | . |  |
| xospfe11 | VARCHAR | 51.4% | A |  |
| ospfee11 | VARCHAR | 74.4% | . |  |
| cindon | VARCHAR | 87.6% | . | Appears in 3 tables, common join key |
| cindoff | DOUBLE | 86.9% | 13590.0 | Appears in 3 tables, common join key |
| cindfam | DOUBLE | 86.9% | 7520.0 | Appears in 3 tables, common join key |
| cinson | VARCHAR | 87.6% | . | Appears in 3 tables, common join key |
| cinsoff | DOUBLE | 86.9% | 13590.0 | Appears in 3 tables, common join key |
| cinsfam | DOUBLE | 86.9% | 7520.0 | Appears in 3 tables, common join key |
| cotson | VARCHAR | 87.6% | . | Appears in 3 tables, common join key |
| cotsoff | DOUBLE | 86.9% | 17490.0 | Appears in 3 tables, common join key |
| cotsfam | DOUBLE | 86.9% | 11420.0 | Appears in 3 tables, common join key |

## ic_py

Rows: 61,317

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 3 | Primary institution ID, joins across all IPEDS tables |
| prgmofr | DOUBLE | 0.0% | 12.0401 |  |
| cipcode1 | VARCHAR | 0.0% | A |  |
| xciptui1 | VARCHAR | 28.1% | . |  |
| ciptuit1 | VARCHAR | 28.1% | A |  |
| xcipsup1 | VARCHAR | 28.1% | . |  |
| cipsupp1 | VARCHAR | 28.1% | R |  |
| xciplgt1 | DOUBLE | 21.2% | 1500.0 |  |
| ciplgth1 | DOUBLE | 15.1% | 1.0 |  |
| prgmsr1 | VARCHAR | 28.1% | R |  |
| xmthcmp1 | DOUBLE | 28.3% | 12.0 |  |
| mthcmp1 | VARCHAR | 28.1% | R |  |
| xwkcmp1 | DOUBLE | 48.5% | 47.0 |  |
| wkcmp1 | VARCHAR | 47.4% | R |  |
| xlnayhr1 | DOUBLE | 48.5% | 900.0 |  |
| lnayhr1 | VARCHAR | 47.4% | R |  |
| xlnaywk1 | DOUBLE | 48.5% | 28.0 |  |
| lnaywk1 | VARCHAR | 47.4% | R |  |
| xchg1py0 | DOUBLE | 42.4% | 12000.0 |  |
| chg1py0 | VARCHAR | 39.2% | R |  |
| xchg1py1 | VARCHAR | 0.0% | 12150 |  |
| chg1py1 | VARCHAR | 9.2% | R |  |
| xchg1py2 | VARCHAR | 0.0% | 15150 |  |
| chg1py2 | VARCHAR | 8.8% | R |  |
| xchg1py3 | VARCHAR | 0.0% | 15150 |  |
| chg1py3 | VARCHAR | 8.2% | R |  |
| xchg4py0 | DOUBLE | 45.2% | 2503.0 |  |
| chg4py0 | VARCHAR | 39.2% | R |  |
| xchg4py1 | VARCHAR | 0.0% | 2649 |  |
| chg4py1 | VARCHAR | 10.1% | R |  |
| xchg4py2 | VARCHAR | 0.0% | 3040 |  |
| chg4py2 | VARCHAR | 9.7% | R |  |
| xchg4py3 | DOUBLE | 25.6% | 3258.0 |  |
| chg4py3 | VARCHAR | 8.9% | A |  |
| xchg5py0 | VARCHAR | 39.2% | . |  |
| chg5py0 | VARCHAR | 39.2% | A |  |
| xchg5py1 | VARCHAR | 0.0% | . |  |
| chg5py1 | VARCHAR | 20.8% | A |  |
| xchg5py2 | VARCHAR | 0.0% | . |  |
| chg5py2 | VARCHAR | 20.8% | A |  |
| xchg5py3 | VARCHAR | 0.0% | . |  |
| chg5py3 | VARCHAR | 21.0% | A |  |
| xchg6py0 | VARCHAR | 39.2% | . |  |
| chg6py0 | VARCHAR | 39.2% | A |  |
| xchg6py1 | VARCHAR | 0.0% | . |  |
| chg6py1 | VARCHAR | 20.8% | A |  |
| xchg6py2 | VARCHAR | 0.0% | . |  |
| chg6py2 | VARCHAR | 20.8% | A |  |
| xchg6py3 | VARCHAR | 0.0% | . |  |
| chg6py3 | VARCHAR | 21.0% | R |  |
| xchg7py0 | DOUBLE | 42.5% | 11268.0 |  |
| chg7py0 | VARCHAR | 39.2% | R |  |
| xchg7py1 | VARCHAR | 0.0% | 11268 |  |
| chg7py1 | VARCHAR | 14.0% | R |  |
| xchg7py2 | VARCHAR | 0.0% | 14171 |  |
| chg7py2 | VARCHAR | 13.4% | R |  |
| xchg7py3 | VARCHAR | 0.0% | 18483 |  |
| chg7py3 | VARCHAR | 12.0% | R |  |
| xchg8py0 | DOUBLE | 42.5% | 7978.0 |  |
| chg8py0 | VARCHAR | 39.2% | R |  |
| xchg8py1 | VARCHAR | 0.0% | 7978 |  |
| chg8py1 | VARCHAR | 14.1% | R |  |
| xchg8py2 | VARCHAR | 0.0% | 6239 |  |
| chg8py2 | VARCHAR | 13.5% | R |  |
| xchg8py3 | VARCHAR | 0.0% | 10963 |  |
| chg8py3 | VARCHAR | 12.1% | R |  |
| xchg9py0 | DOUBLE | 42.5% | 7508.0 |  |
| chg9py0 | VARCHAR | 39.2% | R |  |
| xchg9py1 | VARCHAR | 0.0% | 7508 |  |
| chg9py1 | VARCHAR | 14.1% | R |  |
| xchg9py2 | VARCHAR | 0.0% | 8531 |  |
| chg9py2 | VARCHAR | 13.4% | R |  |
| xchg9py3 | VARCHAR | 0.0% | 8531 |  |
| chg9py3 | VARCHAR | 12.1% | 12.0409 |  |
| cipcode2 | VARCHAR | 0.0% | R |  |
| xciptui2 | VARCHAR | 0.0% | 10150 |  |
| ciptuit2 | VARCHAR | 10.5% | R |  |
| xcipsup2 | VARCHAR | 0.0% | 1735 |  |
| cipsupp2 | VARCHAR | 11.0% | R |  |
| xciplgt2 | VARCHAR | 0.0% | 1000 |  |
| ciplgth2 | DOUBLE | 10.7% | 1.0 |  |
| prgmsr2 | VARCHAR | 28.1% | R |  |
| xmthcmp2 | DOUBLE | 42.7% | 10.0 |  |
| mthcmp2 | DOUBLE | 28.1% | 12.0413 |  |
| cipcode3 | VARCHAR | 0.0% | R |  |
| xciptui3 | VARCHAR | 0.0% | 2150 |  |
| ciptuit3 | VARCHAR | 12.5% | R |  |
| xcipsup3 | VARCHAR | 0.0% | 755 |  |
| cipsupp3 | VARCHAR | 13.1% | R |  |
| xciplgt3 | VARCHAR | 0.0% | 650 |  |
| ciplgth3 | DOUBLE | 13.7% | 1.0 |  |
| prgmsr3 | VARCHAR | 28.1% | R |  |
| xmthcmp3 | VARCHAR | 28.1% | 5 |  |
| mthcmp3 | DOUBLE | 28.1% | -2.0 |  |
| cipcode4 | VARCHAR | 0.0% | A |  |
| xciptui4 | VARCHAR | 0.0% | . |  |
| ciptuit4 | VARCHAR | 14.8% | A |  |
| xcipsup4 | VARCHAR | 0.0% | . |  |
| cipsupp4 | VARCHAR | 15.3% | A |  |
| xciplgt4 | VARCHAR | 0.0% | . |  |
| ciplgth4 | DOUBLE | 17.1% | -2.0 |  |
| prgmsr4 | VARCHAR | 28.1% | A |  |
| xmthcmp4 | VARCHAR | 28.1% | . |  |
| mthcmp4 | DOUBLE | 28.1% | -2.0 |  |
| cipcode5 | VARCHAR | 0.0% | A |  |
| xciptui5 | VARCHAR | 0.0% | . |  |
| ciptuit5 | VARCHAR | 16.6% | A |  |
| xcipsup5 | VARCHAR | 0.0% | . |  |
| cipsupp5 | VARCHAR | 16.9% | A |  |
| xciplgt5 | VARCHAR | 0.0% | . |  |
| ciplgth5 | DOUBLE | 19.9% | -2.0 |  |
| prgmsr5 | VARCHAR | 28.1% | A |  |
| xmthcmp5 | VARCHAR | 28.1% | . |  |
| mthcmp5 | DOUBLE | 28.1% | -2.0 |  |
| cipcode6 | VARCHAR | 0.0% | A |  |
| xciptui6 | VARCHAR | 0.0% | . |  |
| ciptuit6 | VARCHAR | 17.8% | A |  |
| xcipsup6 | VARCHAR | 0.0% | . |  |
| cipsupp6 | VARCHAR | 18.0% | A |  |
| xciplgt6 | VARCHAR | 0.0% | . |  |
| ciplgth6 | DOUBLE | 28.6% | -2.0 |  |
| prgmsr6 | VARCHAR | 28.1% | A |  |
| xmthcmp6 | VARCHAR | 28.1% | . |  |
| mthcmp6 | INTEGER | 100.0% |  |  |
| year | BIGINT | 0.0% | 2023 | Appears in 26 tables, common join key |
| xcmp1py0 | VARCHAR | 83.0% | . |  |
| cmp1py0 | VARCHAR | 83.0% | A |  |
| xcmp1py1 | VARCHAR | 68.5% | . |  |
| cmp1py1 | VARCHAR | 68.5% | A |  |
| xcmp1py2 | VARCHAR | 68.5% | . |  |
| cmp1py2 | VARCHAR | 68.5% | A |  |
| xcmp1py3 | VARCHAR | 68.5% | . |  |
| cmp1py3 | DOUBLE | 71.9% | -2.0 |  |
| pg300 | DOUBLE | 78.8% | 1.0 |  |

## om

Rows: 368,149

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| omchrt | BIGINT | 0.0% | 10 |  |
| xomrchrt | VARCHAR | 7.3% | R |  |
| omrchrt | DOUBLE | 7.3% | 1374.0 |  |
| xomexcls | VARCHAR | 7.3% | R |  |
| omexcls | DOUBLE | 7.3% | 1.0 |  |
| xomachrt | VARCHAR | 7.3% | R |  |
| omachrt | DOUBLE | 7.3% | 1373.0 |  |
| xomcert4 | VARCHAR | 7.3% | R |  |
| omcert4 | DOUBLE | 7.3% | 0.0 |  |
| xomassc4 | VARCHAR | 7.3% | R |  |
| omassc4 | DOUBLE | 7.3% | 0.0 |  |
| xombach4 | VARCHAR | 7.3% | R |  |
| ombach4 | DOUBLE | 39.8% | 143.0 |  |
| xomawdn4 | VARCHAR | 7.3% | R |  |
| omawdn4 | DOUBLE | 7.3% | 143.0 |  |
| xomawdp4 | VARCHAR | 7.3% | R |  |
| omawdp4 | DOUBLE | 7.3% | 10.0 |  |
| xomcert6 | VARCHAR | 7.3% | R |  |
| omcert6 | DOUBLE | 7.3% | 0.0 |  |
| xomassc6 | VARCHAR | 7.3% | R |  |
| omassc6 | DOUBLE | 7.3% | 0.0 |  |
| xombach6 | VARCHAR | 7.3% | R |  |
| ombach6 | DOUBLE | 39.8% | 369.0 |  |
| xomawdn6 | VARCHAR | 0.0% | R |  |
| omawdn6 | BIGINT | 0.0% | 369 |  |
| xomawdp6 | VARCHAR | 0.0% | R |  |
| omawdp6 | DOUBLE | 0.0% | 27.0 |  |
| xomcert8 | VARCHAR | 7.3% | R |  |
| omcert8 | DOUBLE | 7.3% | 0.0 |  |
| xomassc8 | VARCHAR | 7.3% | R |  |
| omassc8 | DOUBLE | 7.3% | 0.0 |  |
| xombach8 | VARCHAR | 7.3% | R |  |
| ombach8 | DOUBLE | 39.8% | 399.0 |  |
| xomawdn8 | VARCHAR | 0.0% | R |  |
| omawdn8 | BIGINT | 0.0% | 399 |  |
| xomenryi | VARCHAR | 0.0% | R |  |
| omenryi | BIGINT | 0.0% | 9 |  |
| xomenrai | VARCHAR | 0.0% | R |  |
| omenrai | BIGINT | 0.0% | 492 |  |
| xomenrun | VARCHAR | 0.0% | R |  |
| omenrun | BIGINT | 0.0% | 473 |  |
| xomnoawd | VARCHAR | 0.0% | R |  |
| omnoawd | BIGINT | 0.0% | 974 |  |
| xomawdp8 | VARCHAR | 0.0% | R |  |
| omawdp8 | DOUBLE | 0.0% | 29.0 |  |
| xomenrtp | VARCHAR | 0.0% | R |  |
| omenrtp | DOUBLE | 0.0% | 36.0 |  |
| xomenryp | VARCHAR | 0.0% | R |  |
| omenryp | DOUBLE | 0.0% | 1.0 |  |
| xomenrap | VARCHAR | 0.0% | R |  |
| omenrap | DOUBLE | 0.0% | 36.0 |  |
| xomenrup | VARCHAR | 7.3% | R |  |
| omenrup | DOUBLE | 7.3% | 34.0 |  |
| year | BIGINT | 0.0% | 2023 | Appears in 26 tables, common join key |
| xomrcht6 | VARCHAR | 92.7% | R |  |
| omrcht6 | DOUBLE | 92.7% | 1044.0 |  |
| xomexcl6 | VARCHAR | 92.7% | R |  |
| omexcl6 | DOUBLE | 92.7% | 0.0 |  |
| xomacht6 | VARCHAR | 92.7% | R |  |
| omacht6 | DOUBLE | 92.7% | 1044.0 |  |
| xomexcl8 | VARCHAR | 92.7% | R |  |
| omexcl8 | DOUBLE | 92.7% | 0.0 |  |
| xomacht8 | VARCHAR | 92.7% | R |  |
| omacht8 | DOUBLE | 92.7% | 1044.0 |  |
| xomrcht8 | VARCHAR | 96.3% | R |  |
| omrcht8 | DOUBLE | 96.3% | 882.0 |  |
| omflag | DOUBLE | 96.3% | 0.0 |  |

## sal_is

Rows: 194,576

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| arank | BIGINT | 0.0% | 1 |  |
| xsainstt | VARCHAR | 35.1% | R |  |
| sainstt | DOUBLE | 35.1% | 40.0 |  |
| xsainstm | VARCHAR | 35.1% | R |  |
| sainstm | DOUBLE | 35.1% | 31.0 |  |
| xsainstw | VARCHAR | 35.1% | R |  |
| sainstw | DOUBLE | 35.1% | 9.0 |  |
| xsa_9mct | VARCHAR | 35.1% | R |  |
| sa_9mct | DOUBLE | 35.1% | 7.0 |  |
| xsa_9mcm | VARCHAR | 35.1% | R |  |
| sa_9mcm | DOUBLE | 35.1% | 7.0 |  |
| xsa_9mcw | VARCHAR | 35.1% | Z |  |
| sa_9mcw | DOUBLE | 35.1% | 0.0 |  |
| xsatotlt | VARCHAR | 0.0% | R |  |
| satotlt | BIGINT | 0.0% | 33 |  |
| xsatotlm | VARCHAR | 0.0% | R |  |
| satotlm | BIGINT | 0.0% | 24 |  |
| xsatotlw | VARCHAR | 0.0% | R |  |
| satotlw | BIGINT | 0.0% | 9 |  |
| xsa09mct | VARCHAR | 0.0% | R |  |
| sa09mct | DOUBLE | 0.0% | 30.0 |  |
| xsa09mcm | VARCHAR | 0.0% | R |  |
| sa09mcm | DOUBLE | 0.0% | 22.0 |  |
| xsa09mcw | VARCHAR | 0.0% | R |  |
| sa09mcw | DOUBLE | 0.0% | 8.0 |  |
| xsa10mct | VARCHAR | 0.0% | R |  |
| sa10mct | DOUBLE | 0.0% | 0.0 |  |
| xsa10mcm | VARCHAR | 0.0% | Z |  |
| sa10mcm | DOUBLE | 0.0% | 0.0 |  |
| xsa10mcw | VARCHAR | 0.0% | Z |  |
| sa10mcw | DOUBLE | 0.0% | 0.0 |  |
| xsa11mct | VARCHAR | 0.0% | R |  |
| sa11mct | DOUBLE | 0.0% | 0.0 |  |
| xsa11mcm | VARCHAR | 0.0% | Z |  |
| sa11mcm | DOUBLE | 0.0% | 0.0 |  |
| xsa11mcw | VARCHAR | 0.0% | Z |  |
| sa11mcw | DOUBLE | 0.0% | 0.0 |  |
| xsa12mct | VARCHAR | 0.0% | R |  |
| sa12mct | DOUBLE | 0.0% | 3.0 |  |
| xsa12mcm | VARCHAR | 0.0% | R |  |
| sa12mcm | DOUBLE | 0.0% | 2.0 |  |
| xsa12mcw | VARCHAR | 0.0% | R |  |
| sa12mcw | DOUBLE | 0.0% | 1.0 |  |
| xsaoutlt | VARCHAR | 0.0% | R |  |
| saoutlt | BIGINT | 0.0% | 3523331 |  |
| xsaoutlm | VARCHAR | 0.0% | R |  |
| saoutlm | BIGINT | 0.0% | 2661328 |  |
| xsaoutlw | VARCHAR | 0.0% | R |  |
| saoutlw | BIGINT | 0.0% | 862003 |  |
| xsa09mot | VARCHAR | 35.1% | R |  |
| sa09mot | DOUBLE | 35.1% | 3116668.0 |  |
| xsa09mom | VARCHAR | 35.1% | R |  |
| sa09mom | DOUBLE | 35.1% | 2386065.0 |  |
| xsa09mow | VARCHAR | 35.1% | R |  |
| sa09mow | DOUBLE | 35.1% | 730603.0 |  |
| xsa10mot | VARCHAR | 35.1% | R |  |
| sa10mot | DOUBLE | 35.1% | 0.0 |  |
| xsa10mom | VARCHAR | 35.1% | Z |  |
| sa10mom | DOUBLE | 35.1% | 0.0 |  |
| xsa10mow | VARCHAR | 35.1% | Z |  |
| sa10mow | DOUBLE | 35.1% | 0.0 |  |
| xsa11mot | VARCHAR | 35.1% | R |  |
| sa11mot | DOUBLE | 35.1% | 0.0 |  |
| xsa11mom | VARCHAR | 35.1% | Z |  |
| sa11mom | DOUBLE | 35.1% | 0.0 |  |
| xsa11mow | VARCHAR | 35.1% | Z |  |
| sa11mow | DOUBLE | 35.1% | 0.0 |  |
| xsa12mot | VARCHAR | 35.1% | R |  |
| sa12mot | DOUBLE | 35.1% | 406663.0 |  |
| xsa12mom | VARCHAR | 35.1% | R |  |
| sa12mom | DOUBLE | 35.1% | 275263.0 |  |
| xsa12mow | VARCHAR | 35.1% | R |  |
| sa12mow | DOUBLE | 35.1% | 131400.0 |  |
| xsaeq9ot | VARCHAR | 35.1% | R |  |
| saeq9ot | DOUBLE | 35.1% | 3421665.0 |  |
| xsaeq9om | VARCHAR | 35.1% | R |  |
| saeq9om | DOUBLE | 35.1% | 2592512.0 |  |
| xsaeq9ow | VARCHAR | 35.1% | R |  |
| saeq9ow | DOUBLE | 35.1% | 829153.0 |  |
| xsaeq9at | VARCHAR | 35.1% | R |  |
| saeq9at | DOUBLE | 35.3% | 103687.0 |  |
| xsaeq9am | VARCHAR | 35.1% | R |  |
| saeq9am | DOUBLE | 39.4% | 108021.0 |  |
| xsaeq9aw | VARCHAR | 35.1% | R |  |
| saeq9aw | DOUBLE | 39.6% | 92128.0 |  |
| xsa09mat | VARCHAR | 35.1% | R |  |
| sa09mat | DOUBLE | 61.0% | 103889.0 |  |
| xsa09mam | VARCHAR | 35.1% | R |  |
| sa09mam | DOUBLE | 62.9% | 108458.0 |  |
| xsa09maw | VARCHAR | 35.1% | R |  |
| sa09maw | DOUBLE | 62.4% | 91325.0 |  |
| xsa10mat | VARCHAR | 35.1% | A |  |
| sa10mat | DOUBLE | 82.7% | 29600.0 |  |
| xsa10mam | VARCHAR | 35.1% | A |  |
| sa10mam | DOUBLE | 85.3% | 29600.0 |  |
| xsa10maw | VARCHAR | 35.1% | A |  |
| sa10maw | DOUBLE | 84.7% | 100648.0 |  |
| xsa11mat | VARCHAR | 35.1% | A |  |
| sa11mat | DOUBLE | 93.2% | 78723.0 |  |
| xsa11mam | VARCHAR | 35.1% | A |  |
| sa11mam | DOUBLE | 95.0% | 78723.0 |  |
| xsa11maw | VARCHAR | 35.1% | A |  |
| sa11maw | DOUBLE | 94.6% | 54743.0 |  |
| xsa12mat | VARCHAR | 35.1% | R |  |
| sa12mat | DOUBLE | 62.5% | 135554.0 |  |
| xsa12mam | VARCHAR | 35.1% | R |  |
| sa12mam | DOUBLE | 68.4% | 137632.0 |  |
| xsa12maw | VARCHAR | 35.1% | R |  |
| sa12maw | DOUBLE | 67.6% | 131400.0 |  |
| year | BIGINT | 0.0% | 2023 | Appears in 26 tables, common join key |
| xsamntht | VARCHAR | 56.4% | R |  |
| samntht | DOUBLE | 56.4% | 396.0 |  |
| xsamnthm | VARCHAR | 56.4% | R |  |
| samnthm | DOUBLE | 56.4% | 321.0 |  |
| xsamnthw | VARCHAR | 56.4% | R |  |
| samnthw | DOUBLE | 56.4% | 75.0 |  |
| xsaavmnt | VARCHAR | 56.4% | R |  |
| saavmnt | DOUBLE | 56.4% | 9613.0 |  |
| xsaavmnm | VARCHAR | 56.4% | R |  |
| saavmnm | DOUBLE | 59.1% | 9629.0 |  |
| xsaavmnw | VARCHAR | 56.4% | R |  |
| saavmnw | DOUBLE | 59.3% | 9544.0 |  |

## sfa

Rows: 132,928

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| xscugrad | VARCHAR | 27.4% | R |  |
| scugrad | DOUBLE | 27.4% | 5206.0 |  |
| xscugdgsk | VARCHAR | 91.5% | R |  |
| scugdgsk | DOUBLE | 91.5% | 5201.0 |  |
| xscugndgs | VARCHAR | 91.5% | R |  |
| scugndgs | DOUBLE | 91.5% | 5.0 |  |
| xscugffn | VARCHAR | 27.4% | R |  |
| scugffn | DOUBLE | 27.4% | 1547.0 |  |
| xscugffp | VARCHAR | 27.4% | R |  |
| scugffp | DOUBLE | 27.5% | 30.0 |  |
| xscfa2 | VARCHAR | 0.0% | R |  |
| scfa2 | DOUBLE | 36.8% | 5206.0 |  |
| xscfa2dg | VARCHAR | 91.5% | R |  |
| scfa2dg | DOUBLE | 94.7% | 5201.0 |  |
| xscfa2nd | VARCHAR | 91.5% | R |  |
| scfa2nd | DOUBLE | 94.7% | 5.0 |  |
| xscfa1n | VARCHAR | 0.0% | R |  |
| scfa1n | DOUBLE | 36.8% | 1547.0 |  |
| xscfa1p | VARCHAR | 0.0% | R |  |
| scfa1p | DOUBLE | 37.0% | 30.0 |  |
| xscfa11n | VARCHAR | 0.0% | R |  |
| scfa11n | DOUBLE | 73.8% | 0.0 |  |
| xscfa11p | VARCHAR | 0.0% | R |  |
| scfa11p | DOUBLE | 73.8% | 0.0 |  |
| xscfa12n | VARCHAR | 0.0% | R |  |
| scfa12n | DOUBLE | 73.8% | 810.0 |  |
| xscfa12p | VARCHAR | 0.0% | R |  |
| scfa12p | DOUBLE | 73.8% | 52.0 |  |
| xscfa13n | VARCHAR | 0.0% | R |  |
| scfa13n | DOUBLE | 73.8% | 737.0 |  |
| xscfa13p | VARCHAR | 0.0% | R |  |
| scfa13p | DOUBLE | 73.8% | 48.0 |  |
| xscfa14n | VARCHAR | 0.0% | R |  |
| scfa14n | DOUBLE | 73.8% | 0.0 |  |
| xscfa14p | VARCHAR | 0.0% | R |  |
| scfa14p | DOUBLE | 73.8% | 0.0 |  |
| xscfy2 | VARCHAR | 0.0% | A |  |
| scfy2 | DOUBLE | 63.2% | 79.0 |  |
| xscfy2dg | VARCHAR | 91.5% | A |  |
| scfy2dg | DOUBLE | 96.8% | 79.0 |  |
| xscfy2nd | VARCHAR | 91.5% | A |  |
| scfy2nd | DOUBLE | 96.8% | 0.0 |  |
| xscfy1n | VARCHAR | 0.0% | A |  |
| scfy1n | DOUBLE | 63.2% | 52.0 |  |
| xscfy1p | VARCHAR | 0.0% | A |  |
| scfy1p | DOUBLE | 63.2% | 66.0 |  |
| xuagrntn | VARCHAR | 32.3% | R |  |
| uagrntn | DOUBLE | 32.3% | 4326.0 |  |
| xuagrntp | VARCHAR | 32.3% | R |  |
| uagrntp | DOUBLE | 32.3% | 83.0 |  |
| xuagrntt | VARCHAR | 32.3% | R |  |
| uagrntt | DOUBLE | 32.3% | 50168163.0 |  |
| xuagrnta | VARCHAR | 32.3% | R |  |
| uagrnta | DOUBLE | 32.7% | 11597.0 |  |
| xudgagrntn | VARCHAR | 91.5% | R |  |
| udgagrntn | DOUBLE | 91.5% | 4326.0 |  |
| xudgagrntp | VARCHAR | 91.5% | R |  |
| udgagrntp | DOUBLE | 91.5% | 83.0 |  |
| xudgagrntt | VARCHAR | 91.5% | R |  |
| udgagrntt | DOUBLE | 91.5% | 50168163.0 |  |
| xudgagrnta | VARCHAR | 91.5% | R |  |
| udgagrnta | DOUBLE | 91.5% | 11597.0 |  |
| xundagrntn | VARCHAR | 91.5% | R |  |
| undagrntn | DOUBLE | 91.5% | 0.0 |  |
| xundagrntp | VARCHAR | 91.5% | R |  |
| undagrntp | DOUBLE | 91.5% | 0.0 |  |
| xundagrntt | VARCHAR | 91.5% | R |  |
| undagrntt | DOUBLE | 91.5% | 0.0 |  |
| xundagrnta | VARCHAR | 91.5% | A |  |
| undagrnta | DOUBLE | 97.1% | 2778.0 |  |
| xupgrntn | VARCHAR | 32.3% | R |  |
| upgrntn | DOUBLE | 32.3% | 3353.0 |  |
| xupgrntp | VARCHAR | 32.3% | R |  |
| upgrntp | DOUBLE | 32.3% | 64.0 |  |
| xupgrntt | VARCHAR | 32.3% | R |  |
| upgrntt | DOUBLE | 32.3% | 19363202.0 |  |
| xupgrnta | VARCHAR | 32.3% | R |  |
| upgrnta | DOUBLE | 33.3% | 5775.0 |  |
| xudgpgrntn | VARCHAR | 95.7% | R |  |
| udgpgrntn | DOUBLE | 95.7% | 3353.0 |  |
| xudgpgrntp | VARCHAR | 91.5% | R |  |
| udgpgrntp | DOUBLE | 91.5% | 64.0 |  |
| xudgpgrntt | VARCHAR | 95.7% | R |  |
| udgpgrntt | DOUBLE | 95.7% | 19363202.0 |  |
| xudgpgrnta | VARCHAR | 95.7% | R |  |
| udgpgrnta | DOUBLE | 95.8% | 5775.0 |  |
| xundpgrntn | VARCHAR | 95.7% | R |  |
| undpgrntn | DOUBLE | 95.7% | 0.0 |  |
| xundpgrntp | VARCHAR | 95.7% | R |  |
| undpgrntp | DOUBLE | 95.8% | 0.0 |  |
| xundpgrntt | VARCHAR | 95.7% | R |  |
| undpgrntt | DOUBLE | 95.7% | 0.0 |  |
| xundpgrnta | VARCHAR | 95.7% | A |  |
| undpgrnta | DOUBLE | 99.3% | 2567.0 |  |
| xufloann | VARCHAR | 32.3% | R |  |
| ufloann | DOUBLE | 32.3% | 3050.0 |  |
| xufloanp | VARCHAR | 32.3% | R |  |
| ufloanp | DOUBLE | 32.3% | 59.0 |  |
| xufloant | VARCHAR | 32.3% | R |  |
| ufloant | DOUBLE | 32.3% | 20538077.0 |  |
| xufloana | VARCHAR | 32.3% | R |  |
| ufloana | DOUBLE | 39.8% | 6734.0 |  |
| xudgfloann | VARCHAR | 95.7% | R |  |
| udgfloann | DOUBLE | 95.7% | 3050.0 |  |
| xudgfloanp | VARCHAR | 91.5% | R |  |
| udgfloanp | DOUBLE | 91.5% | 59.0 |  |
| xudgfloant | VARCHAR | 95.7% | R |  |
| udgfloant | DOUBLE | 95.7% | 20538077.0 |  |
| xudgfloana | VARCHAR | 95.7% | R |  |
| udgfloana | DOUBLE | 96.2% | 6734.0 |  |
| xundfloann | VARCHAR | 95.7% | R |  |
| undfloann | DOUBLE | 95.7% | 0.0 |  |
| xundfloanp | VARCHAR | 95.7% | R |  |
| undfloanp | DOUBLE | 95.8% | 0.0 |  |
| xundfloant | VARCHAR | 95.7% | R |  |
| undfloant | DOUBLE | 95.7% | 0.0 |  |
| xundfloana | VARCHAR | 95.7% | A |  |
| undfloana | DOUBLE | 99.4% | 5500.0 |  |
| xanyaidn | VARCHAR | 0.0% | R |  |
| anyaidn | DOUBLE | 3.2% | 1359.0 |  |
| xanyaidp | VARCHAR | 0.0% | R |  |
| anyaidp | DOUBLE | 3.2% | 88.0 |  |
| xaidfsin | VARCHAR | 37.3% | R |  |
| aidfsin | DOUBLE | 40.1% | 1359.0 |  |
| xaidfsip | VARCHAR | 37.3% | R |  |
| aidfsip | DOUBLE | 40.1% | 88.0 |  |
| xagrnt_n | VARCHAR | 27.4% | R |  |
| agrnt_n | DOUBLE | 30.6% | 1323.0 |  |
| xagrnt_p | VARCHAR | 27.4% | R |  |
| agrnt_p | DOUBLE | 30.6% | 86.0 |  |
| xagrnt_t | VARCHAR | 32.3% | R |  |
| agrnt_t | DOUBLE | 35.4% | 15362449.0 |  |
| xagrnt_a | VARCHAR | 27.4% | R |  |
| agrnt_a | DOUBLE | 31.3% | 11612.0 |  |
| xfgrnt_n | VARCHAR | 0.0% | R |  |
| fgrnt_n | DOUBLE | 3.3% | 1033.0 |  |
| xfgrnt_p | VARCHAR | 0.0% | R |  |
| fgrnt_p | DOUBLE | 3.3% | 67.0 |  |
| xfgrnt_t | VARCHAR | 32.3% | R |  |
| fgrnt_t | DOUBLE | 35.4% | 6366369.0 |  |
| xfgrnt_a | VARCHAR | 0.0% | R |  |
| fgrnt_a | DOUBLE | 5.0% | 6163.0 |  |
| xpgrnt_n | VARCHAR | 27.4% | R |  |
| pgrnt_n | DOUBLE | 30.6% | 1033.0 |  |
| xpgrnt_p | VARCHAR | 27.4% | R |  |
| pgrnt_p | DOUBLE | 30.6% | 67.0 |  |
| xpgrnt_t | VARCHAR | 32.3% | R |  |
| pgrnt_t | DOUBLE | 35.4% | 6185419.0 |  |
| xpgrnt_a | VARCHAR | 27.4% | R |  |
| pgrnt_a | DOUBLE | 31.8% | 5988.0 |  |
| xofgrt_n | VARCHAR | 27.4% | R |  |
| ofgrt_n | DOUBLE | 30.6% | 91.0 |  |
| xofgrt_p | VARCHAR | 27.4% | R |  |
| ofgrt_p | DOUBLE | 30.6% | 6.0 |  |
| xofgrt_t | VARCHAR | 32.3% | R |  |
| ofgrt_t | DOUBLE | 35.4% | 180950.0 |  |
| xofgrt_a | VARCHAR | 27.4% | R |  |
| ofgrt_a | DOUBLE | 49.9% | 1988.0 |  |
| xsgrnt_n | VARCHAR | 0.0% | R |  |
| sgrnt_n | DOUBLE | 3.3% | 29.0 |  |
| xsgrnt_p | VARCHAR | 0.0% | R |  |
| sgrnt_p | DOUBLE | 3.3% | 2.0 |  |
| xsgrnt_t | VARCHAR | 32.3% | R |  |
| sgrnt_t | DOUBLE | 35.4% | 50810.0 |  |
| xsgrnt_a | VARCHAR | 0.0% | R |  |
| sgrnt_a | DOUBLE | 33.3% | 1752.0 |  |
| xigrnt_n | VARCHAR | 0.0% | R |  |
| igrnt_n | DOUBLE | 3.3% | 1024.0 |  |
| xigrnt_p | VARCHAR | 0.0% | R |  |
| igrnt_p | DOUBLE | 3.3% | 66.0 |  |
| xigrnt_t | VARCHAR | 32.3% | R |  |
| igrnt_t | DOUBLE | 35.4% | 8945270.0 |  |
| xigrnt_a | VARCHAR | 0.0% | R |  |
| igrnt_a | DOUBLE | 33.3% | 8736.0 |  |
| xloan_n | VARCHAR | 0.0% | R |  |
| loan_n | DOUBLE | 3.3% | 887.0 |  |
| xloan_p | VARCHAR | 0.0% | R |  |
| loan_p | DOUBLE | 3.3% | 57.0 |  |
| xloan_t | VARCHAR | 32.3% | R |  |
| loan_t | DOUBLE | 35.4% | 5664417.0 |  |
| xloan_a | VARCHAR | 0.0% | R |  |
| loan_a | DOUBLE | 14.9% | 6386.0 |  |
| xfloan_n | VARCHAR | 27.4% | R |  |
| floan_n | DOUBLE | 30.6% | 880.0 |  |
| xfloan_p | VARCHAR | 27.4% | R |  |
| floan_p | DOUBLE | 30.6% | 57.0 |  |
| xfloan_t | VARCHAR | 32.3% | R |  |
| floan_t | DOUBLE | 35.4% | 5322609.0 |  |
| xfloan_a | VARCHAR | 27.4% | R |  |
| floan_a | DOUBLE | 39.1% | 6048.0 |  |
| xoloan_n | VARCHAR | 27.4% | R |  |
| oloan_n | DOUBLE | 30.6% | 26.0 |  |
| xoloan_p | VARCHAR | 27.4% | R |  |
| oloan_p | DOUBLE | 30.6% | 2.0 |  |
| xoloan_t | VARCHAR | 32.3% | R |  |
| oloan_t | DOUBLE | 35.4% | 341808.0 |  |
| xoloan_a | VARCHAR | 27.4% | R |  |
| oloan_a | DOUBLE | 67.1% | 13146.0 |  |
| xgistn2 | VARCHAR | 32.3% | R |  |
| gistn2 | DOUBLE | 80.2% | 712.0 |  |
| xgiston2 | VARCHAR | 32.3% | R |  |
| giston2 | DOUBLE | 91.0% | 619.0 |  |
| xgistwf2 | VARCHAR | 32.3% | R |  |
| gistwf2 | DOUBLE | 80.4% | 70.0 |  |
| xgistof2 | VARCHAR | 32.3% | R |  |
| gistof2 | DOUBLE | 80.4% | 22.0 |  |
| xgistun2 | VARCHAR | 32.3% | R |  |
| gistun2 | DOUBLE | 80.3% | 1.0 |  |
| xgistt2 | VARCHAR | 32.3% | R |  |
| gistt2 | DOUBLE | 80.2% | 6598275.0 |  |
| xgista2 | VARCHAR | 32.3% | R |  |
| gista2 | DOUBLE | 80.2% | 9267.0 |  |
| xgistn1 | VARCHAR | 32.3% | R |  |
| gistn1 | DOUBLE | 80.2% | 612.0 |  |
| xgiston1 | VARCHAR | 32.3% | R |  |
| giston1 | DOUBLE | 91.0% | 471.0 |  |
| xgistwf1 | VARCHAR | 32.3% | R |  |
| gistwf1 | DOUBLE | 80.5% | 78.0 |  |
| xgistof1 | VARCHAR | 32.3% | R |  |
| gistof1 | DOUBLE | 80.5% | 63.0 |  |
| xgistun1 | VARCHAR | 32.3% | R |  |
| gistun1 | DOUBLE | 80.4% | 0.0 |  |
| xgistt1 | VARCHAR | 32.3% | R |  |
| gistt1 | DOUBLE | 80.3% | 5180341.0 |  |
| xgista1 | VARCHAR | 32.3% | R |  |
| gista1 | DOUBLE | 80.3% | 8465.0 |  |
| xgistn0 | VARCHAR | 32.3% | R |  |
| gistn0 | DOUBLE | 80.2% | 693.0 |  |
| xgiston0 | VARCHAR | 32.3% | R |  |
| giston0 | DOUBLE | 91.0% | 482.0 |  |
| xgistwf0 | VARCHAR | 32.3% | R |  |
| gistwf0 | DOUBLE | 80.6% | 158.0 |  |
| xgistof0 | VARCHAR | 32.3% | R |  |
| gistof0 | DOUBLE | 80.6% | 53.0 |  |
| xgistun0 | VARCHAR | 32.3% | R |  |
| gistun0 | DOUBLE | 80.5% | 0.0 |  |
| xgistt0 | VARCHAR | 32.3% | R |  |
| gistt0 | DOUBLE | 80.4% | 6240985.0 |  |
| xgista0 | VARCHAR | 32.3% | R |  |
| gista0 | DOUBLE | 80.4% | 9006.0 |  |
| xgis4n2 | VARCHAR | 32.3% | R |  |
| gis4n2 | DOUBLE | 80.3% | 645.0 |  |
| xgis4on2 | VARCHAR | 32.3% | R |  |
| gis4on2 | DOUBLE | 91.0% | 592.0 |  |
| xgis4wf2 | VARCHAR | 32.3% | R |  |
| gis4wf2 | DOUBLE | 80.5% | 34.0 |  |
| xgis4of2 | VARCHAR | 32.3% | R |  |
| gis4of2 | DOUBLE | 80.5% | 19.0 |  |
| xgis4un2 | VARCHAR | 32.3% | R |  |
| gis4un2 | DOUBLE | 80.4% | 0.0 |  |
| xgis4g2 | VARCHAR | 37.3% | R |  |
| gis4g2 | DOUBLE | 81.6% | 636.0 |  |
| xgis4t2 | VARCHAR | 32.3% | R |  |
| gis4t2 | DOUBLE | 80.3% | 5928907.0 |  |
| xgis4a2 | VARCHAR | 32.3% | R |  |
| gis4a2 | DOUBLE | 80.3% | 9192.0 |  |
| xgis4n12 | VARCHAR | 32.3% | R |  |
| gis4n12 | DOUBLE | 80.3% | 328.0 |  |
| xgis4g12 | VARCHAR | 37.3% | R |  |
| gis4g12 | DOUBLE | 81.6% | 328.0 |  |
| xgis4t12 | VARCHAR | 32.3% | R |  |
| gis4t12 | DOUBLE | 80.3% | 3271951.0 |  |
| xgis4a12 | VARCHAR | 32.3% | R |  |
| gis4a12 | DOUBLE | 80.4% | 9975.0 |  |
| xgis4n22 | VARCHAR | 32.3% | R |  |
| gis4n22 | DOUBLE | 80.3% | 176.0 |  |
| xgis4g22 | VARCHAR | 37.3% | R |  |
| gis4g22 | DOUBLE | 81.6% | 176.0 |  |
| xgis4t22 | VARCHAR | 32.3% | R |  |
| gis4t22 | DOUBLE | 80.3% | 1729702.0 |  |
| xgis4a22 | VARCHAR | 32.3% | R |  |
| gis4a22 | DOUBLE | 81.6% | 9828.0 |  |
| xgis4n32 | VARCHAR | 32.3% | R |  |
| gis4n32 | DOUBLE | 80.3% | 94.0 |  |
| xgis4g32 | VARCHAR | 37.3% | R |  |
| gis4g32 | DOUBLE | 81.6% | 91.0 |  |
| xgis4t32 | VARCHAR | 32.3% | R |  |
| gis4t32 | DOUBLE | 80.3% | 684364.0 |  |
| xgis4a32 | VARCHAR | 32.3% | R |  |
| gis4a32 | DOUBLE | 82.2% | 7280.0 |  |
| xgis4n42 | VARCHAR | 32.3% | R |  |
| gis4n42 | DOUBLE | 80.3% | 21.0 |  |
| xgis4g42 | VARCHAR | 37.3% | R |  |
| gis4g42 | DOUBLE | 81.6% | 18.0 |  |
| xgis4t42 | VARCHAR | 32.3% | R |  |
| gis4t42 | DOUBLE | 80.3% | 98566.0 |  |
| xgis4a42 | VARCHAR | 32.3% | R |  |
| gis4a42 | DOUBLE | 84.1% | 4694.0 |  |
| xgis4n52 | VARCHAR | 32.3% | R |  |
| gis4n52 | DOUBLE | 80.3% | 26.0 |  |
| xgis4g52 | VARCHAR | 37.3% | R |  |
| gis4g52 | DOUBLE | 81.6% | 23.0 |  |
| xgis4t52 | VARCHAR | 32.3% | R |  |
| gis4t52 | DOUBLE | 80.3% | 144324.0 |  |
| xgis4a52 | VARCHAR | 32.3% | R |  |
| gis4a52 | DOUBLE | 86.5% | 5551.0 |  |
| xgis4n1 | VARCHAR | 37.3% | R |  |
| gis4n1 | DOUBLE | 81.6% | 567.0 |  |
| xgis4on1 | VARCHAR | 37.3% | R |  |
| gis4on1 | DOUBLE | 92.3% | 439.0 |  |
| xgis4wf1 | VARCHAR | 37.3% | R |  |
| gis4wf1 | DOUBLE | 81.9% | 66.0 |  |
| xgis4of1 | VARCHAR | 37.3% | R |  |
| gis4of1 | DOUBLE | 81.9% | 62.0 |  |
| xgis4un1 | VARCHAR | 37.3% | R |  |
| gis4un1 | DOUBLE | 81.8% | 0.0 |  |
| xgis4g1 | VARCHAR | 37.3% | R |  |
| gis4g1 | DOUBLE | 81.7% | 549.0 |  |
| xgis4t1 | VARCHAR | 37.3% | R |  |
| gis4t1 | DOUBLE | 81.7% | 4640730.0 |  |
| xgis4a1 | VARCHAR | 37.3% | R |  |
| gis4a1 | DOUBLE | 81.7% | 8185.0 |  |
| xgis4n11 | VARCHAR | 37.3% | R |  |
| gis4n11 | DOUBLE | 81.7% | 311.0 |  |
| xgis4g11 | VARCHAR | 37.3% | R |  |
| gis4g11 | DOUBLE | 81.7% | 307.0 |  |
| xgis4t11 | VARCHAR | 37.3% | R |  |
| gis4t11 | DOUBLE | 81.7% | 2787106.0 |  |
| xgis4a11 | VARCHAR | 37.3% | R |  |
| gis4a11 | DOUBLE | 81.8% | 8962.0 |  |
| xgis4n21 | VARCHAR | 37.3% | R |  |
| gis4n21 | DOUBLE | 81.7% | 143.0 |  |
| xgis4g21 | VARCHAR | 37.3% | R |  |
| gis4g21 | DOUBLE | 81.7% | 142.0 |  |
| xgis4t21 | VARCHAR | 37.3% | R |  |
| gis4t21 | DOUBLE | 81.7% | 1235673.0 |  |
| xgis4a21 | VARCHAR | 37.3% | R |  |
| gis4a21 | DOUBLE | 82.8% | 8641.0 |  |
| xgis4n31 | VARCHAR | 37.3% | R |  |
| gis4n31 | DOUBLE | 81.7% | 57.0 |  |
| xgis4g31 | VARCHAR | 37.3% | R |  |
| gis4g31 | DOUBLE | 81.7% | 53.0 |  |
| xgis4t31 | VARCHAR | 37.3% | R |  |
| gis4t31 | DOUBLE | 81.7% | 378171.0 |  |
| xgis4a31 | VARCHAR | 37.3% | R |  |
| gis4a31 | DOUBLE | 83.4% | 6635.0 |  |
| xgis4n41 | VARCHAR | 37.3% | R |  |
| gis4n41 | DOUBLE | 81.7% | 29.0 |  |
| xgis4g41 | VARCHAR | 37.3% | R |  |
| gis4g41 | DOUBLE | 81.7% | 22.0 |  |
| xgis4t41 | VARCHAR | 37.3% | R |  |
| gis4t41 | DOUBLE | 81.7% | 87821.0 |  |
| xgis4a41 | VARCHAR | 37.3% | R |  |
| gis4a41 | DOUBLE | 85.2% | 3028.0 |  |
| xgis4n51 | VARCHAR | 37.3% | R |  |
| gis4n51 | DOUBLE | 81.7% | 27.0 |  |
| xgis4g51 | VARCHAR | 37.3% | R |  |
| gis4g51 | DOUBLE | 81.7% | 25.0 |  |
| xgis4t51 | VARCHAR | 37.3% | R |  |
| gis4t51 | DOUBLE | 81.7% | 151959.0 |  |
| xgis4a51 | VARCHAR | 37.3% | R |  |
| gis4a51 | DOUBLE | 87.4% | 5628.0 |  |
| xgis4n0 | VARCHAR | 37.3% | R |  |
| gis4n0 | DOUBLE | 81.6% | 657.0 |  |
| xgis4on0 | VARCHAR | 37.3% | R |  |
| gis4on0 | DOUBLE | 92.3% | 457.0 |  |
| xgis4wf0 | VARCHAR | 37.3% | R |  |
| gis4wf0 | DOUBLE | 82.0% | 150.0 |  |
| xgis4of0 | VARCHAR | 37.3% | R |  |
| gis4of0 | DOUBLE | 82.0% | 50.0 |  |
| xgis4un0 | VARCHAR | 37.3% | R |  |
| gis4un0 | DOUBLE | 81.9% | 0.0 |  |
| xgis4g0 | VARCHAR | 37.3% | R |  |
| gis4g0 | DOUBLE | 81.7% | 642.0 |  |
| xgis4t0 | VARCHAR | 37.3% | R |  |
| gis4t0 | DOUBLE | 81.8% | 5825299.0 |  |
| xgis4a0 | VARCHAR | 37.3% | R |  |
| gis4a0 | DOUBLE | 81.8% | 8867.0 |  |
| xgis4n10 | VARCHAR | 37.3% | R |  |
| gis4n10 | DOUBLE | 81.8% | 381.0 |  |
| xgis4g10 | VARCHAR | 37.3% | R |  |
| gis4g10 | DOUBLE | 81.8% | 380.0 |  |
| xgis4t10 | VARCHAR | 37.3% | R |  |
| gis4t10 | DOUBLE | 81.8% | 3713735.0 |  |
| xgis4a10 | VARCHAR | 37.3% | R |  |
| gis4a10 | DOUBLE | 81.9% | 9747.0 |  |
| xgis4n20 | VARCHAR | 37.3% | R |  |
| gis4n20 | DOUBLE | 81.8% | 141.0 |  |
| xgis4g20 | VARCHAR | 37.3% | R |  |
| gis4g20 | DOUBLE | 81.8% | 141.0 |  |
| xgis4t20 | VARCHAR | 37.3% | R |  |
| gis4t20 | DOUBLE | 81.8% | 1357002.0 |  |
| xgis4a20 | VARCHAR | 37.3% | R |  |
| gis4a20 | DOUBLE | 82.9% | 9624.0 |  |
| xgis4n30 | VARCHAR | 37.3% | R |  |
| gis4n30 | DOUBLE | 81.8% | 76.0 |  |
| xgis4g30 | VARCHAR | 37.3% | R |  |
| gis4g30 | DOUBLE | 81.8% | 73.0 |  |
| xgis4t30 | VARCHAR | 37.3% | R |  |
| gis4t30 | DOUBLE | 81.8% | 487604.0 |  |
| xgis4a30 | VARCHAR | 37.3% | R |  |
| gis4a30 | DOUBLE | 83.5% | 6416.0 |  |
| xgis4n40 | VARCHAR | 37.3% | R |  |
| gis4n40 | DOUBLE | 81.8% | 40.0 |  |
| xgis4g40 | VARCHAR | 37.3% | R |  |
| gis4g40 | DOUBLE | 81.8% | 34.0 |  |
| xgis4t40 | VARCHAR | 37.3% | R |  |
| gis4t40 | DOUBLE | 81.8% | 208688.0 |  |
| xgis4a40 | VARCHAR | 37.3% | R |  |
| gis4a40 | DOUBLE | 85.4% | 5217.0 |  |
| xgis4n50 | VARCHAR | 37.3% | R |  |
| gis4n50 | DOUBLE | 81.8% | 19.0 |  |
| xgis4g50 | VARCHAR | 37.3% | R |  |
| gis4g50 | DOUBLE | 81.8% | 14.0 |  |
| xgis4t50 | VARCHAR | 37.3% | R |  |
| gis4t50 | DOUBLE | 81.8% | 58270.0 |  |
| xgis4a50 | VARCHAR | 37.3% | R |  |
| gis4a50 | DOUBLE | 87.6% | 3067.0 |  |
| xnpist2 | VARCHAR | 32.3% | R |  |
| npist2 | DOUBLE | 80.2% | 14064.0 |  |
| xnpist1 | VARCHAR | 32.3% | R |  |
| npist1 | DOUBLE | 80.3% | 14600.0 |  |
| xnpist0 | VARCHAR | 32.3% | R |  |
| npist0 | DOUBLE | 80.4% | 12921.0 |  |
| xnpis412 | VARCHAR | 32.3% | R |  |
| npis412 | DOUBLE | 80.4% | 13776.0 |  |
| xnpis422 | VARCHAR | 32.3% | R |  |
| npis422 | DOUBLE | 81.6% | 13923.0 |  |
| xnpis432 | VARCHAR | 32.3% | R |  |
| npis432 | DOUBLE | 82.2% | 16471.0 |  |
| xnpis442 | VARCHAR | 32.3% | R |  |
| npis442 | DOUBLE | 84.1% | 19057.0 |  |
| xnpis452 | VARCHAR | 32.3% | R |  |
| npis452 | DOUBLE | 86.5% | 18200.0 |  |
| xnpis411 | VARCHAR | 37.3% | R |  |
| npis411 | DOUBLE | 81.8% | 14205.0 |  |
| xnpis421 | VARCHAR | 37.3% | R |  |
| npis421 | DOUBLE | 82.8% | 14526.0 |  |
| xnpis431 | VARCHAR | 37.3% | R |  |
| npis431 | DOUBLE | 83.4% | 16532.0 |  |
| xnpis441 | VARCHAR | 37.3% | R |  |
| npis441 | DOUBLE | 85.2% | 20139.0 |  |
| xnpis451 | VARCHAR | 37.3% | R |  |
| npis451 | DOUBLE | 87.4% | 17539.0 |  |
| xnpis410 | VARCHAR | 37.3% | R |  |
| npis410 | DOUBLE | 81.9% | 12177.0 |  |
| xnpis420 | VARCHAR | 37.3% | R |  |
| npis420 | DOUBLE | 82.9% | 12300.0 |  |
| xnpis430 | VARCHAR | 37.3% | R |  |
| npis430 | DOUBLE | 83.5% | 15508.0 |  |
| xnpis440 | VARCHAR | 37.3% | R |  |
| npis440 | DOUBLE | 85.4% | 16707.0 |  |
| xnpis450 | VARCHAR | 37.3% | R |  |
| npis450 | DOUBLE | 87.6% | 18857.0 |  |
| xgrntn2 | VARCHAR | 32.3% | A |  |
| grntn2 | DOUBLE | 56.1% | 244.0 |  |
| xgrnton2 | VARCHAR | 32.3% | A |  |
| grnton2 | DOUBLE | 84.6% | 231.0 |  |
| xgrntwf2 | VARCHAR | 32.3% | A |  |
| grntwf2 | DOUBLE | 57.1% | 13.0 |  |
| xgrntof2 | VARCHAR | 32.3% | A |  |
| grntof2 | DOUBLE | 57.1% | 0.0 |  |
| xgrntun2 | VARCHAR | 32.3% | A |  |
| grntun2 | DOUBLE | 57.0% | 0.0 |  |
| xgrntt2 | VARCHAR | 32.3% | A |  |
| grntt2 | DOUBLE | 56.3% | 3470354.0 |  |
| xgrnta2 | VARCHAR | 32.3% | A |  |
| grnta2 | DOUBLE | 56.3% | 14223.0 |  |
| xgrntn1 | VARCHAR | 32.3% | A |  |
| grntn1 | DOUBLE | 56.2% | 244.0 |  |
| xgrnton1 | VARCHAR | 32.3% | A |  |
| grnton1 | DOUBLE | 84.9% | 199.0 |  |
| xgrntwf1 | VARCHAR | 32.3% | A |  |
| grntwf1 | DOUBLE | 58.7% | 45.0 |  |
| xgrntof1 | VARCHAR | 32.3% | A |  |
| grntof1 | DOUBLE | 58.7% | 0.0 |  |
| xgrntun1 | VARCHAR | 32.3% | A |  |
| grntun1 | DOUBLE | 58.5% | 0.0 |  |
| xgrntt1 | VARCHAR | 32.3% | A |  |
| grntt1 | DOUBLE | 57.9% | 3455829.0 |  |
| xgrnta1 | VARCHAR | 32.3% | A |  |
| grnta1 | DOUBLE | 57.8% | 14163.0 |  |
| xgrntn0 | VARCHAR | 32.3% | A |  |
| grntn0 | DOUBLE | 56.2% | 249.0 |  |
| xgrnton0 | VARCHAR | 32.3% | A |  |
| grnton0 | DOUBLE | 85.1% | 200.0 |  |
| xgrntwf0 | VARCHAR | 32.3% | A |  |
| grntwf0 | DOUBLE | 60.0% | 49.0 |  |
| xgrntof0 | VARCHAR | 32.3% | A |  |
| grntof0 | DOUBLE | 60.0% | 0.0 |  |
| xgrntun0 | VARCHAR | 32.3% | A |  |
| grntun0 | DOUBLE | 59.9% | 0.0 |  |
| xgrntt0 | VARCHAR | 32.3% | A |  |
| grntt0 | DOUBLE | 59.2% | 2684585.0 |  |
| xgrnta0 | VARCHAR | 32.3% | A |  |
| grnta0 | DOUBLE | 59.2% | 10781.0 |  |
| xgrn4n2 | VARCHAR | 32.3% | A |  |
| grn4n2 | DOUBLE | 56.3% | 204.0 |  |
| xgrn4on2 | VARCHAR | 32.3% | A |  |
| grn4on2 | DOUBLE | 84.8% | 193.0 |  |
| xgrn4wf2 | VARCHAR | 32.3% | A |  |
| grn4wf2 | DOUBLE | 57.4% | 11.0 |  |
| xgrn4of2 | VARCHAR | 32.3% | A |  |
| grn4of2 | DOUBLE | 57.4% | 0.0 |  |
| xgrn4un2 | VARCHAR | 32.3% | A |  |
| grn4un2 | DOUBLE | 57.2% | 0.0 |  |
| xgrn4g2 | VARCHAR | 37.3% | A |  |
| grn4g2 | DOUBLE | 60.0% | 204.0 |  |
| xgrn4t2 | VARCHAR | 32.3% | A |  |
| grn4t2 | DOUBLE | 56.6% | 3066885.0 |  |
| xgrn4a2 | VARCHAR | 32.3% | A |  |
| grn4a2 | DOUBLE | 56.6% | 15034.0 |  |
| xgrn4n12 | VARCHAR | 32.3% | A |  |
| grn4n12 | DOUBLE | 56.6% | 32.0 |  |
| xgrn4g12 | VARCHAR | 37.3% | A |  |
| grn4g12 | DOUBLE | 60.0% | 32.0 |  |
| xgrn4t12 | VARCHAR | 32.3% | A |  |
| grn4t12 | DOUBLE | 56.6% | 602338.0 |  |
| xgrn4a12 | VARCHAR | 32.3% | A |  |
| grn4a12 | DOUBLE | 57.2% | 18823.0 |  |
| xgrn4n22 | VARCHAR | 32.3% | A |  |
| grn4n22 | DOUBLE | 56.6% | 15.0 |  |
| xgrn4g22 | VARCHAR | 37.3% | A |  |
| grn4g22 | DOUBLE | 60.0% | 15.0 |  |
| xgrn4t22 | VARCHAR | 32.3% | A |  |
| grn4t22 | DOUBLE | 56.6% | 267347.0 |  |
| xgrn4a22 | VARCHAR | 32.3% | A |  |
| grn4a22 | DOUBLE | 64.5% | 17823.0 |  |
| xgrn4n32 | VARCHAR | 32.3% | A |  |
| grn4n32 | DOUBLE | 56.6% | 24.0 |  |
| xgrn4g32 | VARCHAR | 37.3% | A |  |
| grn4g32 | DOUBLE | 60.0% | 24.0 |  |
| xgrn4t32 | VARCHAR | 32.3% | A |  |
| grn4t32 | DOUBLE | 56.6% | 402016.0 |  |
| xgrn4a32 | VARCHAR | 32.3% | A |  |
| grn4a32 | DOUBLE | 68.0% | 16751.0 |  |
| xgrn4n42 | VARCHAR | 32.3% | A |  |
| grn4n42 | DOUBLE | 56.6% | 28.0 |  |
| xgrn4g42 | VARCHAR | 37.3% | A |  |
| grn4g42 | DOUBLE | 60.0% | 28.0 |  |
| xgrn4t42 | VARCHAR | 32.3% | A |  |
| grn4t42 | DOUBLE | 56.6% | 433748.0 |  |
| xgrn4a42 | VARCHAR | 32.3% | A |  |
| grn4a42 | DOUBLE | 74.0% | 15491.0 |  |
| xgrn4n52 | VARCHAR | 32.3% | A |  |
| grn4n52 | DOUBLE | 56.6% | 105.0 |  |
| xgrn4g52 | VARCHAR | 37.3% | A |  |
| grn4g52 | DOUBLE | 60.0% | 105.0 |  |
| xgrn4t52 | VARCHAR | 32.3% | A |  |
| grn4t52 | DOUBLE | 56.6% | 1361436.0 |  |
| xgrn4a52 | VARCHAR | 32.3% | A |  |
| grn4a52 | DOUBLE | 78.5% | 12966.0 |  |
| xgrn4n1 | VARCHAR | 37.3% | A |  |
| grn4n1 | DOUBLE | 59.9% | 207.0 |  |
| xgrn4on1 | VARCHAR | 37.3% | A |  |
| grn4on1 | DOUBLE | 88.3% | 172.0 |  |
| xgrn4wf1 | VARCHAR | 37.3% | A |  |
| grn4wf1 | DOUBLE | 61.5% | 35.0 |  |
| xgrn4of1 | VARCHAR | 37.3% | A |  |
| grn4of1 | DOUBLE | 61.5% | 0.0 |  |
| xgrn4un1 | VARCHAR | 37.3% | A |  |
| grn4un1 | DOUBLE | 61.3% | 0.0 |  |
| xgrn4g1 | VARCHAR | 37.3% | A |  |
| grn4g1 | DOUBLE | 60.7% | 207.0 |  |
| xgrn4t1 | VARCHAR | 37.3% | A |  |
| grn4t1 | DOUBLE | 60.7% | 3264837.0 |  |
| xgrn4a1 | VARCHAR | 37.3% | A |  |
| grn4a1 | DOUBLE | 61.5% | 15772.0 |  |
| xgrn4n11 | VARCHAR | 37.3% | A |  |
| grn4n11 | DOUBLE | 60.7% | 31.0 |  |
| xgrn4g11 | VARCHAR | 37.3% | A |  |
| grn4g11 | DOUBLE | 60.7% | 31.0 |  |
| xgrn4t11 | VARCHAR | 37.3% | A |  |
| grn4t11 | DOUBLE | 60.7% | 556903.0 |  |
| xgrn4a11 | VARCHAR | 37.3% | A |  |
| grn4a11 | DOUBLE | 61.9% | 17965.0 |  |
| xgrn4n21 | VARCHAR | 37.3% | A |  |
| grn4n21 | DOUBLE | 60.7% | 18.0 |  |
| xgrn4g21 | VARCHAR | 37.3% | A |  |
| grn4g21 | DOUBLE | 60.7% | 18.0 |  |
| xgrn4t21 | VARCHAR | 37.3% | A |  |
| grn4t21 | DOUBLE | 60.7% | 329373.0 |  |
| xgrn4a21 | VARCHAR | 37.3% | A |  |
| grn4a21 | DOUBLE | 68.1% | 18299.0 |  |
| xgrn4n31 | VARCHAR | 37.3% | A |  |
| grn4n31 | DOUBLE | 60.7% | 32.0 |  |
| xgrn4g31 | VARCHAR | 37.3% | A |  |
| grn4g31 | DOUBLE | 60.7% | 32.0 |  |
| xgrn4t31 | VARCHAR | 37.3% | A |  |
| grn4t31 | DOUBLE | 60.7% | 539065.0 |  |
| xgrn4a31 | VARCHAR | 37.3% | A |  |
| grn4a31 | DOUBLE | 71.2% | 16846.0 |  |
| xgrn4n41 | VARCHAR | 37.3% | A |  |
| grn4n41 | DOUBLE | 60.7% | 40.0 |  |
| xgrn4g41 | VARCHAR | 37.3% | A |  |
| grn4g41 | DOUBLE | 60.7% | 40.0 |  |
| xgrn4t41 | VARCHAR | 37.3% | A |  |
| grn4t41 | DOUBLE | 60.7% | 595967.0 |  |
| xgrn4a41 | VARCHAR | 37.3% | A |  |
| grn4a41 | DOUBLE | 76.4% | 14899.0 |  |
| xgrn4n51 | VARCHAR | 37.3% | A |  |
| grn4n51 | DOUBLE | 60.7% | 86.0 |  |
| xgrn4g51 | VARCHAR | 37.3% | A |  |
| grn4g51 | DOUBLE | 60.7% | 86.0 |  |
| xgrn4t51 | VARCHAR | 37.3% | A |  |
| grn4t51 | DOUBLE | 60.7% | 1243529.0 |  |
| xgrn4a51 | VARCHAR | 37.3% | A |  |
| grn4a51 | DOUBLE | 80.5% | 14460.0 |  |
| xgrn4n0 | VARCHAR | 37.3% | A |  |
| grn4n0 | DOUBLE | 59.9% | 207.0 |  |
| xgrn4on0 | VARCHAR | 37.3% | A |  |
| grn4on0 | DOUBLE | 88.3% | 171.0 |  |
| xgrn4wf0 | VARCHAR | 37.3% | A |  |
| grn4wf0 | DOUBLE | 62.1% | 36.0 |  |
| xgrn4of0 | VARCHAR | 37.3% | A |  |
| grn4of0 | DOUBLE | 62.1% | 0.0 |  |
| xgrn4un0 | VARCHAR | 37.3% | A |  |
| grn4un0 | DOUBLE | 61.9% | 0.0 |  |
| xgrn4g0 | VARCHAR | 37.3% | A |  |
| grn4g0 | DOUBLE | 61.3% | 207.0 |  |
| xgrn4t0 | VARCHAR | 37.3% | A |  |
| grn4t0 | DOUBLE | 61.3% | 2654119.0 |  |
| xgrn4a0 | VARCHAR | 37.3% | A |  |
| grn4a0 | DOUBLE | 62.8% | 12822.0 |  |
| xgrn4n10 | VARCHAR | 37.3% | A |  |
| grn4n10 | DOUBLE | 61.3% | 26.0 |  |
| xgrn4g10 | VARCHAR | 37.3% | A |  |
| grn4g10 | DOUBLE | 61.3% | 26.0 |  |
| xgrn4t10 | VARCHAR | 37.3% | A |  |
| grn4t10 | DOUBLE | 61.3% | 426922.0 |  |
| xgrn4a10 | VARCHAR | 37.3% | A |  |
| grn4a10 | DOUBLE | 63.2% | 16420.0 |  |
| xgrn4n20 | VARCHAR | 37.3% | A |  |
| grn4n20 | DOUBLE | 61.3% | 20.0 |  |
| xgrn4g20 | VARCHAR | 37.3% | A |  |
| grn4g20 | DOUBLE | 61.3% | 20.0 |  |
| xgrn4t20 | VARCHAR | 37.3% | A |  |
| grn4t20 | DOUBLE | 61.3% | 332355.0 |  |
| xgrn4a20 | VARCHAR | 37.3% | A |  |
| grn4a20 | DOUBLE | 69.0% | 16618.0 |  |
| xgrn4n30 | VARCHAR | 37.3% | A |  |
| grn4n30 | DOUBLE | 61.3% | 20.0 |  |
| xgrn4g30 | VARCHAR | 37.3% | A |  |
| grn4g30 | DOUBLE | 61.3% | 20.0 |  |
| xgrn4t30 | VARCHAR | 37.3% | A |  |
| grn4t30 | DOUBLE | 61.3% | 326359.0 |  |
| xgrn4a30 | VARCHAR | 37.3% | A |  |
| grn4a30 | DOUBLE | 72.0% | 16318.0 |  |
| xgrn4n40 | VARCHAR | 37.3% | A |  |
| grn4n40 | DOUBLE | 61.3% | 34.0 |  |
| xgrn4g40 | VARCHAR | 37.3% | A |  |
| grn4g40 | DOUBLE | 61.3% | 34.0 |  |
| xgrn4t40 | VARCHAR | 37.3% | A |  |
| grn4t40 | DOUBLE | 61.3% | 407830.0 |  |
| xgrn4a40 | VARCHAR | 37.3% | A |  |
| grn4a40 | DOUBLE | 77.0% | 11995.0 |  |
| xgrn4n50 | VARCHAR | 37.3% | A |  |
| grn4n50 | DOUBLE | 61.3% | 107.0 |  |
| xgrn4g50 | VARCHAR | 37.3% | A |  |
| grn4g50 | DOUBLE | 61.3% | 107.0 |  |
| xgrn4t50 | VARCHAR | 37.3% | A |  |
| grn4t50 | DOUBLE | 61.3% | 1160653.0 |  |
| xgrn4a50 | VARCHAR | 37.3% | A |  |
| grn4a50 | DOUBLE | 81.0% | 10847.0 |  |
| xnpgrn2 | VARCHAR | 32.3% | A |  |
| npgrn2 | DOUBLE | 56.4% | 24170.0 |  |
| xnpgrn1 | VARCHAR | 32.3% | A |  |
| npgrn1 | DOUBLE | 58.0% | 21153.0 |  |
| xnpgrn0 | VARCHAR | 32.3% | A |  |
| npgrn0 | DOUBLE | 59.3% | 22888.0 |  |
| xnpt412 | VARCHAR | 32.3% | A |  |
| npt412 | DOUBLE | 57.3% | 19562.0 |  |
| xnpt422 | VARCHAR | 32.3% | A |  |
| npt422 | DOUBLE | 64.5% | 20562.0 |  |
| xnpt432 | VARCHAR | 32.3% | A |  |
| npt432 | DOUBLE | 68.1% | 21634.0 |  |
| xnpt442 | VARCHAR | 32.3% | A |  |
| npt442 | DOUBLE | 74.0% | 22894.0 |  |
| xnpt452 | VARCHAR | 32.3% | A |  |
| npt452 | DOUBLE | 78.6% | 25419.0 |  |
| xnpt411 | VARCHAR | 37.3% | A |  |
| npt411 | DOUBLE | 62.0% | 17530.0 |  |
| xnpt421 | VARCHAR | 37.3% | A |  |
| npt421 | DOUBLE | 68.1% | 17196.0 |  |
| xnpt431 | VARCHAR | 37.3% | A |  |
| npt431 | DOUBLE | 71.3% | 18649.0 |  |
| xnpt441 | VARCHAR | 37.3% | A |  |
| npt441 | DOUBLE | 76.4% | 20596.0 |  |
| xnpt451 | VARCHAR | 37.3% | A |  |
| npt451 | DOUBLE | 80.6% | 21035.0 |  |
| xnpt410 | VARCHAR | 37.3% | A |  |
| npt410 | DOUBLE | 63.3% | 17500.0 |  |
| xnpt420 | VARCHAR | 37.3% | A |  |
| npt420 | DOUBLE | 69.0% | 17302.0 |  |
| xnpt430 | VARCHAR | 37.3% | A |  |
| npt430 | DOUBLE | 72.0% | 17602.0 |  |
| xnpt440 | VARCHAR | 37.3% | A |  |
| npt440 | DOUBLE | 77.1% | 21925.0 |  |
| xnpt450 | VARCHAR | 37.3% | A |  |
| npt450 | DOUBLE | 81.1% | 23073.0 |  |
| year | BIGINT | 0.0% | 2023 | Appears in 26 tables, common join key |
| xscfy11n | VARCHAR | 59.0% | A |  |
| scfy11n | DOUBLE | 98.1% | 0.0 |  |
| xscfy11p | VARCHAR | 59.0% | A |  |
| scfy11p | DOUBLE | 98.1% | 0.0 |  |
| xscfy12n | VARCHAR | 59.0% | A |  |
| scfy12n | DOUBLE | 98.1% | 0.0 |  |
| xscfy12p | VARCHAR | 59.0% | A |  |
| scfy12p | DOUBLE | 98.1% | 0.0 |  |
| xscfy13n | VARCHAR | 59.0% | A |  |
| scfy13n | DOUBLE | 98.1% | 0.0 |  |
| xscfy13p | VARCHAR | 59.0% | A |  |
| scfy13p | DOUBLE | 98.1% | 0.0 |  |
| xscfy14n | VARCHAR | 59.0% | A |  |
| scfy14n | DOUBLE | 98.1% | 0.0 |  |
| xscfy14p | VARCHAR | 59.0% | A |  |
| scfy14p | DOUBLE | 98.1% | 0.0 |  |
| xtotgrnt | VARCHAR | 95.1% | R |  |
| totgrnt | DOUBLE | 95.1% | 17473759.0 |  |
| xtstdpel | VARCHAR | 95.1% | R |  |
| tstdpel | DOUBLE | 95.1% | 1607.0 |  |

## v_admission_rates

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 199999 | Primary institution ID, joins across all IPEDS tables |
| year | BIGINT | 0.0% | 2014 | Appears in 26 tables, common join key |
| institution_name | VARCHAR | 0.0% | The Art Institute of Cincinnati-AIC College of Design | Appears in 4 tables, common join key |
| state | VARCHAR | 0.0% | OH | Appears in 4 tables, common join key |
| applicants_total | BIGINT | 0.0% | 129 |  |
| admissions_total | DOUBLE | 1.0% | 6638.0 |  |
| enrolled_total | DOUBLE | 1.2% | 89.0 |  |
| admit_rate_pct | DOUBLE | 1.0% | 100.0 |  |
| yield_rate_pct | DOUBLE | 1.2% | 26.5 |  |

## v_institutions

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 201140 | Primary institution ID, joins across all IPEDS tables |
| institution_name | VARCHAR | 0.0% | Athenaeum of Ohio | Appears in 4 tables, common join key |
| ialias | VARCHAR | 11.0% | Appalachian State University |  |
| addr | VARCHAR | 0.0% | 1200 Taylor Rd |  |
| city | VARCHAR | 0.0% | Cincinnati |  |
| state | VARCHAR | 0.0% | OH | Appears in 4 tables, common join key |
| zip_code | VARCHAR | 0.0% | 45230-2091 |  |
| fips_state | BIGINT | 0.0% | 39 |  |
| region | BIGINT | 0.0% | 3 |  |
| chfnm | VARCHAR | 0.4% | Quinton T. Ross |  |
| chftitle | VARCHAR | 0.6% | Chairman/CEO |  |
| gentele | DOUBLE | 11.5% | 2516755990.0 |  |
| ein | DOUBLE | 0.9% | 630417508.0 |  |
| ueis | VARCHAR | 44.0% | E6M6SVPENJG4 |  |
| opeid | DOUBLE | 1.0% | 102900.0 |  |
| opeflag | BIGINT | 0.0% | 1 |  |
| website | VARCHAR | 5.1% | www.jmu.edu/index.shtml |  |
| adminurl | VARCHAR | 13.3% | ljic.edu/ |  |
| faidurl | VARCHAR | 13.4% | https://www.cacc.edu/financial-aid/ |  |
| applurl | VARCHAR | 13.3% | https://umobile.edu/apply/ |  |
| npricurl | VARCHAR | 17.4% | ljic.edu/student-resources-and-disclosures/ |  |
| veturl | VARCHAR | 21.9% | https://www.amridgeuniversity.edu/admissions/military/ |  |
| athurl | VARCHAR | 21.9% |   |  |
| disaurl | VARCHAR | 26.5% | umobile.edu/studentsuccesscenter/disability-support-services/ |  |
| sector | BIGINT | 0.0% | 2 | Appears in 3 tables, common join key |
| level | BIGINT | 0.0% | 1 |  |
| control | BIGINT | 0.0% | 2 |  |
| hloffer | BIGINT | 0.0% | 7 |  |
| ugoffer | BIGINT | 0.0% | 1 |  |
| groffer | BIGINT | 0.0% | 1 |  |
| hdegofr1 | DOUBLE | 14.3% | 12.0 |  |
| degree_granting | BIGINT | 0.0% | 1 |  |
| hbcu | BIGINT | 0.0% | 2 |  |
| hospital | BIGINT | 0.0% | 2 |  |
| medical | BIGINT | 0.0% | 2 |  |
| tribal | BIGINT | 0.0% | 2 |  |
| locale_code | BIGINT | 0.0% | 11 |  |
| openpubl | BIGINT | 0.0% | 1 |  |
| act | VARCHAR | 0.0% | A |  |
| newid | DOUBLE | 0.1% | -2.0 |  |
| deathyr | BIGINT | 0.0% | -2 |  |
| close_date | VARCHAR | 0.7% | -2         |  |
| currently_active | BIGINT | 0.0% | 3 |  |
| postsec | BIGINT | 0.0% | 1 |  |
| pseflag | BIGINT | 0.0% | 1 |  |
| pset4flg | BIGINT | 0.0% | 2 |  |
| rptmth | DOUBLE | 8.5% | 1.0 |  |
| instcat | DOUBLE | 8.5% | 4.0 |  |
| c00carnegie | DOUBLE | 47.0% | 21.0 |  |
| carnegie_basic | BIGINT | 0.0% | 24 |  |
| carnegieic | DOUBLE | 47.0% | -2.0 |  |
| carnegiesaec | DOUBLE | 47.0% | -2.0 |  |
| carnegiersch | DOUBLE | 47.0% | -2.0 |  |
| carnegiesize | DOUBLE | 47.0% | -2.0 |  |
| carnegiealf | DOUBLE | 47.0% | -2.0 |  |
| carnegieapm | DOUBLE | 47.0% | 2.0 |  |
| carnegiegpm | DOUBLE | 47.0% | -2.0 |  |
| land_grant | DOUBLE | 9.5% | 2.0 |  |
| size_category | DOUBLE | 9.5% | 2.0 |  |
| f1systyp | DOUBLE | 13.5% | 2.0 | Appears in 3 tables, common join key |
| f1sysnam | VARCHAR | 13.5% | La James International College                                                   | Appears in 3 tables, common join key |
| f1syscod | DOUBLE | 19.7% | 137030.0 |  |
| cbsa | DOUBLE | 12.0% | 33660.0 |  |
| cbsatype | DOUBLE | 12.0% | 1.0 |  |
| csa | DOUBLE | 12.0% | 380.0 |  |
| county_fips | DOUBLE | 14.3% | 19013.0 |  |
| county_name | VARCHAR | 14.3% | Black Hawk County |  |
| cngdstcd | DOUBLE | 14.3% | 102.0 |  |
| longitude | DOUBLE | 14.3% | -86.295677 |  |
| latitude | DOUBLE | 14.3% | 30.793247 |  |
| dfrcgid | DOUBLE | 13.1% | 124.0 |  |
| dfrcuscg | DOUBLE | 19.7% | 2.0 |  |
| year | BIGINT | 0.0% | 2024 | Appears in 26 tables, common join key |
| c21ipug | DOUBLE | 95.6% | 1.0 |  |
| c21ipgrd | DOUBLE | 95.6% | 0.0 |  |
| c21ugprf | DOUBLE | 95.6% | -2.0 |  |
| c21enprf | DOUBLE | 95.6% | -2.0 |  |
| c21szset | DOUBLE | 95.6% | 6.0 |  |
| c18basic | DOUBLE | 95.6% | 22.0 |  |
| c15basic | DOUBLE | 87.8% | -2.0 |  |
| ccbasic | DOUBLE | 76.7% | -3.0 |  |
| carnegie | DOUBLE | 62.5% | -3.0 |  |
| duns | DOUBLE | 85.3% | 38913539.0 |  |
| necta | DOUBLE | 68.0% | -2.0 |  |
| c18ipug | DOUBLE | 92.3% | 16.0 |  |
| c18ipgrd | DOUBLE | 92.3% | 0.0 |  |
| c18ugprf | DOUBLE | 92.3% | -2.0 |  |
| c18enprf | DOUBLE | 92.3% | -2.0 |  |
| c18szset | DOUBLE | 92.3% | 6.0 |  |
| c15ipug | DOUBLE | 88.9% | -2.0 |  |
| c15ipgrd | DOUBLE | 88.9% | -2.0 |  |
| c15ugprf | DOUBLE | 88.9% | 6.0 |  |
| c15enprf | DOUBLE | 88.9% | -2.0 |  |
| c15szset | DOUBLE | 88.9% | 6.0 |  |
| ccipug | DOUBLE | 85.8% | -2.0 |  |
| ccipgrad | DOUBLE | 85.8% | -3.0 |  |
| ccugprof | DOUBLE | 85.8% | 2.0 |  |
| ccenrprf | DOUBLE | 85.8% | -3.0 |  |
| ccsizset | DOUBLE | 85.8% | -3.0 |  |
| faxtele | DOUBLE | 96.3% | 7328850440.0 |  |
| tenursys | DOUBLE | 90.1% | -1.0 | Appears in 3 tables, common join key |
| fpoffer | DOUBLE | 85.7% | 2.0 |  |
| hdegoffr | DOUBLE | 85.7% | 0.0 |  |
| fintele | DOUBLE | 90.6% | 6175856747.0 |  |
| admtele | DOUBLE | 89.9% | 6064323627.0 |  |
| stat_fa | DOUBLE | 91.5% | 5.0 |  |
| stat_ic | DOUBLE | 91.5% | 1.0 | Appears in 3 tables, common join key |
| lock_ic | DOUBLE | 91.5% | 0.0 | Appears in 3 tables, common join key |
| stat_c | DOUBLE | 91.5% | 5.0 | Appears in 3 tables, common join key |
| lock_c | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| prch_c | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| idx_c | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| imp_c | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| stat_wi | DOUBLE | 91.5% | -9.0 |  |
| stat_ef | DOUBLE | 91.5% | -9.0 | Appears in 3 tables, common join key |
| lock_ef | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| prch_ef | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| idx_ef | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| imp_ef | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| pta99_ef | DOUBLE | 91.5% | 5.0 | Appears in 3 tables, common join key |
| ptb_ef | DOUBLE | 91.5% | 5.0 | Appears in 3 tables, common join key |
| ptc_ef | DOUBLE | 91.5% | -9.0 | Appears in 3 tables, common join key |
| ptd_ef | DOUBLE | 91.5% | -9.0 | Appears in 3 tables, common join key |
| pteeffy | DOUBLE | 91.5% | 5.0 | Appears in 3 tables, common join key |
| pteefia | DOUBLE | 91.5% | 5.0 | Appears in 3 tables, common join key |
| fyrpyear | DOUBLE | 91.5% | -2.0 | Appears in 4 tables, common join key |
| stat_sa | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| lock_sa | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| prch_sa | DOUBLE | 91.5% | 2.0 | Appears in 3 tables, common join key |
| idx_sa | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| imp_sa | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| stat_s | DOUBLE | 91.5% | 1.0 | Appears in 3 tables, common join key |
| lock_s | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| prch_s | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| idx_s | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| imp_s | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| stat_eap | DOUBLE | 91.5% | 5.0 | Appears in 3 tables, common join key |
| lock_eap | DOUBLE | 91.5% | 0.0 | Appears in 3 tables, common join key |
| prch_eap | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| idx_eap | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| imp_eap | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| ftemp15 | DOUBLE | 91.5% | -1.0 | Appears in 3 tables, common join key |
| sa_excl | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| stat_sp | DOUBLE | 91.5% | 5.0 |  |
| form_f | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| stat_f | DOUBLE | 91.5% | 1.0 | Appears in 3 tables, common join key |
| lock_f | DOUBLE | 91.5% | 0.0 | Appears in 3 tables, common join key |
| prch_f | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| idx_f | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| imp_f | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| fybeg | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| fyend | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| gpfs | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| f1gasbcr | DOUBLE | 91.5% | -2.0 |  |
| f1gasbal | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| stat_sfa | DOUBLE | 91.5% | 5.0 | Appears in 3 tables, common join key |
| lock_sfa | DOUBLE | 91.5% | 0.0 | Appears in 3 tables, common join key |
| prch_sfa | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| idx_sfa | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| imp_sfa | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| stat_gr | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| lock_gr | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| prch_gr | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| idx_gr | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| imp_gr | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| cohrtstu | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| pyaid | DOUBLE | 91.5% | 2.0 | Appears in 3 tables, common join key |
| cohrtaid | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| sport1 | DOUBLE | 91.5% | -1.0 | Appears in 4 tables, common join key |
| sport2 | DOUBLE | 91.5% | -2.0 | Appears in 4 tables, common join key |
| sport3 | DOUBLE | 91.5% | -2.0 | Appears in 4 tables, common join key |
| sport4 | DOUBLE | 91.5% | -1.0 | Appears in 4 tables, common join key |
| sport5 | DOUBLE | 91.5% | -2.0 | Appears in 3 tables, common join key |
| longpgm | DOUBLE | 91.5% | -1.0 | Appears in 3 tables, common join key |
| cohrtmt | DOUBLE | 91.5% | 1.0 |  |
| tpr | DOUBLE | 91.5% | -1.0 |  |
| hpr | DOUBLE | 91.5% | -1.0 |  |
| cufasb | DOUBLE | 97.7% | -2.0 | Appears in 3 tables, common join key |
| cugasb | DOUBLE | 97.7% | -2.0 | Appears in 3 tables, common join key |
| fte | DOUBLE | 99.8% | 168.0 |  |
| ocrmsi | DOUBLE | 91.5% | -2.0 |  |
| ocrhsi | DOUBLE | 91.5% | -2.0 |  |
| twoyrcat | DOUBLE | 97.7% | -4.0 |  |
| rev_c | DOUBLE | 97.7% | 0.0 | Appears in 3 tables, common join key |
| rev_ef | DOUBLE | 97.7% | -2.0 | Appears in 3 tables, common join key |
| rev_sa | DOUBLE | 97.7% | 0.0 | Appears in 3 tables, common join key |
| rev_s | DOUBLE | 97.7% | -2.0 | Appears in 3 tables, common join key |
| rev_eap | DOUBLE | 97.7% | 0.0 | Appears in 3 tables, common join key |
| r_form_f | DOUBLE | 97.7% | -2.0 |  |
| rev_f | DOUBLE | 97.7% | 0.0 | Appears in 3 tables, common join key |
| rev_sfa | DOUBLE | 97.7% | 0.0 | Appears in 3 tables, common join key |
| rev_gr | DOUBLE | 97.7% | 0.0 | Appears in 3 tables, common join key |
| affil | DOUBLE | 93.8% | -3.0 |  |
| pctmin1 | DOUBLE | 93.8% | -1.0 |  |
| pctmin2 | DOUBLE | 93.8% | -1.0 |  |
| pctmin3 | DOUBLE | 93.8% | -1.0 |  |
| pctmin4 | DOUBLE | 93.8% | 0.0 |  |
| ptacipef | DOUBLE | 93.8% | -2.0 | Appears in 3 tables, common join key |
| transver | DOUBLE | 93.8% | -2.0 |  |
| cindon | DOUBLE | 100.0% |  | Appears in 3 tables, common join key |
| cinson | DOUBLE | 100.0% |  | Appears in 3 tables, common join key |
| cotson | DOUBLE | 100.0% |  | Appears in 3 tables, common join key |
| cindoff | DOUBLE | 100.0% |  | Appears in 3 tables, common join key |
| cinsoff | DOUBLE | 100.0% |  | Appears in 3 tables, common join key |
| cotsoff | DOUBLE | 100.0% |  | Appears in 3 tables, common join key |
| cindfam | DOUBLE | 100.0% |  | Appears in 3 tables, common join key |
| cinsfam | DOUBLE | 100.0% |  | Appears in 3 tables, common join key |
| cotsfam | DOUBLE | 100.0% |  | Appears in 3 tables, common join key |
| rn | BIGINT | 0.0% | 1 |  |

## v_tuition_trends

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 201140 | Primary institution ID, joins across all IPEDS tables |
| year | BIGINT | 0.0% | 2000 | Appears in 26 tables, common join key |
| institution_name | VARCHAR | 0.1% | Athenaeum of Ohio | Appears in 4 tables, common join key |
| state | VARCHAR | 0.1% | OH | Appears in 4 tables, common join key |
| sector | BIGINT | 0.1% | 1 | Appears in 3 tables, common join key |
| tuition_in_state | DOUBLE | 0.0% | 10050.0 |  |
| tuition_out_state | DOUBLE | 0.0% | 10050.0 |  |
| tuition_in_district | DOUBLE | 0.0% | 10050.0 |  |
