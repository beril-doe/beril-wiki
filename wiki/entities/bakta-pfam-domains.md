---
type: "Dataset"
description: "Lakehouse table of Bakta Pfam domain hits (18.8M rows) with versioned accessions; misses classical defense markers."
sources: ["summaries/amr_pangenome_atlas__REPORT.md", "summaries/phage_defense_arsenal__REPORT.md", "summaries/plant_microbiome_ecotypes__REPORT.md", "summaries/prophage_amr_comobilization__REPORT.md"]
---
# bakta_pfam_domains

`bakta_pfam_domains` is a table of Bakta Pfam domain hits in the KBase Data Lakehouse, with 18.8M rows and versioned Pfam accessions. [src: phage_defense_arsenal] Two projects, phage_defense_arsenal and plant_microbiome_ecotypes, found that it misses expected markers. [src: phage_defense_arsenal, plant_microbiome_ecotypes] The plant microbiome report therefore recommends using it as a supplement to `interproscan_domains`, not a replacement. [src: plant_microbiome_ecotypes]

## Key facts

- The table has 18.8M rows. `interproscan_domains` has 833M rows and is the primary Pfam-based defense-detection table in the phage defense report. [src: phage_defense_arsenal]
- The table is part of the [[entities/kbase-ke-pangenome]] database. The prophage and AMR (antimicrobial resistance) co-mobilization report used it with `bakta_amr` and `bakta_annotations` to identify AMR and prophage markers. [src: prophage_amr_comobilization]
- `bakta_pfam_domains.pfam_id` uses versioned accessions such as PF01867.29. `interproscan_domains.signature_acc` uses version-free ones such as PF01867. [src: phage_defense_arsenal]
- The table stores IDs such as PF13629.12, not bare accessions such as PF00771. [src: plant_microbiome_ecotypes]

## Versioned accessions

The original plant microbiome NB02 query `WHERE pfam_id IN ('PF00771', …)` returned zero rows because the table stores versioned IDs such as PF00771.22. [src: plant_microbiome_ecotypes] NB02 therefore found no Pfam hits and classified genes by gene name, KEGG ortholog (KO), and product keywords. [src: plant_microbiome_ecotypes]

A `LIKE 'PF00771%'` pattern fixed this in NB13 Cell 3. [src: plant_microbiome_ecotypes] On the 10 Phase 2b marker Pfams, it recovered 19,364 domain hits across 7,962 species. [src: plant_microbiome_ecotypes]

Cross-database joins must strip versions on the Bakta side. The phage defense report said this was undocumented in `docs/pitfalls.md` for `kbase_ke_pangenome` and cost about 15 minutes of debugging. [src: phage_defense_arsenal]

## Missing and undercounted markers

Some markers are absent or undercounted even when queried correctly.

- CRISPR Cas1 (PF01867) returns 0 hits in this table, against about 25K in InterProScan. [src: phage_defense_arsenal]
- The plant microbiome audit found 12 of 22 marker Pfams completely absent from this table, although abundant in `interproscan_domains`. [src: plant_microbiome_ecotypes]
- The missing markers were mostly secretion-system markers (T3SS, T4SS and T6SS: type III, IV and VI secretion systems). InterProScan had all of them. [src: plant_microbiome_ecotypes]
- The 10 markers that are present, mostly nitrogen fixation and CWDE (cell wall degrading enzyme) markers, returned only 10–35% of the InterProScan hit count. They are undercounted but not zero. [src: plant_microbiome_ecotypes]
- The report proposes a cause: Bakta likely uses a reduced "core" Pfam HMM profile set, while InterProScan uses the full Pfam-A release. This is a likely explanation, not a tested one. [src: plant_microbiome_ecotypes]
- The AMR pangenome atlas found zero AMR clusters with hits in this table. It suggests that AMRFinderPlus and Pfam HMM scans target non-overlapping sequence space for these families. [src: amr_pangenome_atlas]

The InterProScan-based NB10 pipeline was unaffected. The bakta-only Phase 1 NB02 query was the source of the original zero-hit problem. [src: plant_microbiome_ecotypes]

## Guidance

Treat the table as a supplement to `interproscan_domains`, not a substitute. Cross-check any Pfam query against the InterProScan table before concluding that a function is missing. [src: plant_microbiome_ecotypes] See also [[concepts/reference-database-table-choice-and-pfam-versioning-in-lakehouse-queries]], [[concepts/domain-based-marker-detection-and-annotation-method-bias]] and [[entities/interproscan-domain-annotation]].
