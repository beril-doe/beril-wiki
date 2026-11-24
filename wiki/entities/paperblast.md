---
type: "Dataset"
description: "Curated gene–paper assignments held as kescience_paperblast."
sources: ["summaries/berdl_data_atlas__REPORT.md", "summaries/caulobacter_fur_lipida_loss__REPORT.md", "summaries/paperblast_explorer__REPORT.md", "summaries/pitfalls.md"]
aliases: ["kescience_paperblast"]
---
# PaperBLAST

Curated gene–paper assignments held as kescience_paperblast.

## Key facts

- PaperBLAST was created by Price & Arkin (2017) to connect protein sequences to relevant literature. [src: paperblast_explorer]
- Price & Arkin's interactive functional-annotation tools (2024) and Curated BLAST (2019) further developed literature text mining for gene-function discovery. [src: paperblast_explorer]
- The primary citation for the data source is Price MN, Deutschbauer AM, Arkin AP (2021), "PaperBLAST: Text Mining Papers for Information about Homologs," mSystems 6(1):e00185-19, PMID (PubMed identifier) 33531404. [src: caulobacter_fur_lipida_loss]
- Links come from text mining of PubMed Central full-text articles. Curated annotations from 13 databases and PDB structural data supplement them. [src: paperblast_explorer]
- The collection on the [[entities/kbase-data-lakehouse]] contains 12.4 million rows across 14 tables. [src: paperblast_explorer]
- For literature work, the atlas report recommends `kescience_paperblast` with `kescience_pubmed`, joined via `pmid` / `doi`. [src: berdl_data_atlas]
- The Data Lakehouse inventory lists 255,096 PaperBLAST curated genes. [src: berdl_data_atlas] The `curatedgene` table supplies 255K curated gene-paper assignments. [src: berdl_data_atlas]
- The paperblast_explorer report claims the first comprehensive protein-family-level characterization of this collection. [src: paperblast_explorer] It used all 14 tables. [src: paperblast_explorer]

### Table sizes

| Table | Rows | Content |
|---|---|---|
| genepaper | 3,195,890 | text-mined gene-to-paper links [src: paperblast_explorer] |
| site | 2,089,192 | PDB binding/active/modified sites [src: paperblast_explorer] |
| snippet | 1,951,949 | text excerpts mentioning genes [src: paperblast_explorer] |
| generif | 1,358,798 | GeneRIF functional summaries [src: paperblast_explorer] |
| gene | 1,135,366 | gene/protein metadata [src: paperblast_explorer] |
| uniq | 815,571 | unique protein sequences [src: paperblast_explorer] |
| curatedpaper | 599,587 | curated gene-paper links [src: paperblast_explorer] |
| curatedgene | 255,096 | curated annotations (SwissProt, BRENDA, etc.) [src: paperblast_explorer] |

## Coverage

### Time and organisms

The database covers papers from 1951 to 2026. [src: paperblast_explorer] Publications peak around 2020–2021, and 30.6% of records are from 2020 onwards. [src: paperblast_explorer] The 2025 data includes 125,438 records from 22,271 papers. [src: paperblast_explorer] The 1,425 records from 2026 indicate, in the report's reading, a snapshot taken in early 2026. [src: paperblast_explorer]

The 1.1M genes span 27,718 organisms across all domains of life. [src: paperblast_explorer] The report states that Bacteria dominate by organism count (6,000) and Eukarya by gene count (291K), owing to over-representation of human and model-organism genes. [src: paperblast_explorer] The domain table below does not fully match that statement: the Unknown category has more organisms (14,798) than Bacteria (5,997). [src: paperblast_explorer]

| Domain | Organisms | Genes | Share of genes |
|---|---|---|---|
| Bacteria | 5,997 | 397,544 | 35.0% [src: paperblast_explorer] |
| Unknown | 14,798 | 397,511 | 35.0% [src: paperblast_explorer] |
| Eukarya | 822 | 290,537 | 25.6% [src: paperblast_explorer] |
| Virus | 5,730 | 27,199 | 2.4% [src: paperblast_explorer] |
| Archaea | 371 | 22,575 | 2.0% [src: paperblast_explorer] |

### Gene–paper structure

845K genes link to 1.1M unique papers through 3.2M many-to-many associations. [src: paperblast_explorer] Each gene averages 3.8 papers and each paper mentions 2.9 genes. [src: paperblast_explorer] The report treats the similar gene and paper counts (~1.1M each) as partly coincidental. It says most genes have few papers and most papers mention few genes. [src: paperblast_explorer] 25.6% of genes in the gene table (290K) have no text-mined paper link. They rely solely on curated or GeneRIF annotations. [src: paperblast_explorer]

### Curated sources

SwissProt contributes the most curated entries, with 110K proteins and 182K unique papers. [src: paperblast_explorer] PaperBLAST includes about 19% of the full SwissProt database (~570K reviewed entries as of 2024). That is the subset matched to PMC open-access literature. [src: paperblast_explorer] See [[entities/swiss-prot]]. EcoCyc has the highest paper density per protein (5.3), reflecting deep curation of *E. coli* metabolism. [src: paperblast_explorer]

| Curated database | Proteins | Papers | Papers/protein |
|---|---|---|---|
| biolip | 42,571 | 23,768 | 0.6 [src: paperblast_explorer] |
| BRENDA | 33,012 | 43,760 | 1.3 [src: paperblast_explorer] |
| MetaCyc | 12,700 | 46,176 | 3.6 [src: paperblast_explorer] |
| EcoCyc | 4,198 | 22,304 | 5.3 [src: paperblast_explorer] |

### Structural site annotations

PaperBLAST includes site annotations for 132,179 PDB structures. It has 2.1M site records across 4 types: binding (1.69M), functional (182K), modified (112K), and mutagenesis (104K). [src: paperblast_explorer] The binding type has 1.69M records [src: paperblast_explorer], functional 182K [src: paperblast_explorer], modified 112K [src: paperblast_explorer] and mutagenesis 104K. [src: paperblast_explorer]

The structural annotations contain 48,991 unique ligands. [src: paperblast_explorer] The leading ligands are zinc ions (65K sites) [src: paperblast_explorer], chlorophyll A (58K) [src: paperblast_explorer], calcium ions (53K) [src: paperblast_explorer] and heme (44K). [src: paperblast_explorer]

## Data-handling pitfalls

These caveats come from the cross-project pitfalls digest. See [[summaries/pitfalls]].

### Querying the tables

- `year` is a STRING, so always use `CAST(year AS INT)` for comparisons or `ORDER BY`. [src: pitfalls]
- `protein_length` in `curatedgene` and `uniq` is a STRING and needs casting for numeric operations. [src: pitfalls]
- `isOpen` in `genepaper` is mostly NULL, so do not use it to filter for open-access papers. [src: pitfalls]
- `genepaper` has about 3.2M rows, so filter by `geneId` or `pmId` rather than full-scanning. [src: pitfalls]
- `geneId` spans several namespaces (RefSeq `NP_*`, UniProt-ish `WP_*`, VIMSS and others). Cross-namespace queries must go through `seqtoduplicate`. [src: pitfalls] See [[concepts/join-key-validity-and-identifier-format-mismatches]].
- `snippet.snippet` is raw PMC text with formatting artifacts and partial sentences, so do not display it unfiltered. [src: pitfalls]

### Exporting from SQLite

Python's `sqlite3` module defaults to strict UTF-8 decoding of TEXT columns. Non-UTF-8 bytes then raise an `OperationalError` during cursor iteration, before any cleaning runs. [src: pitfalls] Setting `conn.text_factory` to decode UTF-8 with `errors='replace'` lets iteration succeed and substitutes U+FFFD for invalid bytes. [src: pitfalls] The report says to set `text_factory` immediately after connecting, before executing any queries. [src: pitfalls]

### Schema parsing in ingest

The ingest pipeline's `parse_sql_schema()` uses regex to extract column definitions from `CREATE TABLE` statements. [src: pitfalls] If a table body begins with an inline comment, the parser can treat `/*` as a column name. That yields an invalid schema, and the pipeline silently skips the whole table with no error message or quarantine entry. [src: pitfalls] The report's solution is to strip both `/* ... */` and `--` comments before tokenization. [src: pitfalls]

## Use in the Caulobacter lipid A project

The Caulobacter project used the `gene`, `genepaper`, `snippet` and `curatedgene` tables for a SigU literature scout (NB03) and for cross-species presence/absence (NB06). [src: caulobacter_fur_lipida_loss] NB06 used PaperBLAST description-text matching. [src: caulobacter_fur_lipida_loss] It compared Caulobacter crescentus, Acinetobacter baumannii, Neisseria meningitidis and Moraxella catarrhalis. [src: caulobacter_fur_lipida_loss] The notebook screens presence and absence using PaperBLAST. [src: caulobacter_fur_lipida_loss] Its output is a 25-row file of focal-gene hit counts per species. [src: caulobacter_fur_lipida_loss] This work relates to [[concepts/alternative-routes-to-tolerating-lipid-a-or-lps-loss-across-gram-negatives]].

### False negatives

Text matching missed most Caulobacter lipid A genes, and the report puts the false-negative rate at about 80%. [src: caulobacter_fur_lipida_loss] NCBI returned 11-18 per gene. [src: caulobacter_fur_lipida_loss] Another statement lists only LpxA, LpxC, LpxD and LpxK as having 0 hits. [src: caulobacter_fur_lipida_loss] The adversarial review had flagged about 50% false negatives for known Caulobacter essential genes. [src: caulobacter_fur_lipida_loss] Per gene, PaperBLAST versus NCBI hit counts were:

- LpxA: 0 vs 11. [src: caulobacter_fur_lipida_loss]
- LpxC (the deleted gene): 0 vs 15. [src: caulobacter_fur_lipida_loss]
- LpxD: 0 vs 15. [src: caulobacter_fur_lipida_loss]
- LpxB: 1 vs 18, an under-count. [src: caulobacter_fur_lipida_loss]
- LpxK: 0 vs 18. [src: caulobacter_fur_lipida_loss]

The report states that its biological claims are unaffected, because they depend on absences in comparator species, where NCBI confirms them. [src: caulobacter_fur_lipida_loss] It now reads NB06 as a screen and treats NB06b as the authoritative comparative measurement for the headline claim. [src: caulobacter_fur_lipida_loss] The per-species comparison file documents the false-negative rate. [src: caulobacter_fur_lipida_loss] See [[concepts/annotation-based-false-negatives-in-comparative-presence-absence-searches]].

Two further limits apply. Moraxella catarrhalis is under-annotated in PaperBLAST, with 162 genes total, so its presence/absence rows are advisory only. [src: caulobacter_fur_lipida_loss] Caulobacter SigU is uncharacterized in published literature, and the scout found zero substantive snippets for CCNA_02977. This prevents validating the late cohort's biological coherence against a gold standard. [src: caulobacter_fur_lipida_loss] N. meningitidis had 9 capsule-biosynthesis PaperBLAST hits versus 2-3 in the other organisms. [src: caulobacter_fur_lipida_loss] See also [[concepts/literature-coverage-bias-and-text-mining-limits]].
