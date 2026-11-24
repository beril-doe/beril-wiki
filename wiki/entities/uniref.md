---
type: "Dataset"
description: "UniProt reference clusters at 100%, 90% and 50% identity (2026-01 snapshot) held in refdata."
sources: ["summaries/berdl_data_atlas__REPORT.md", "summaries/discoveries.md", "summaries/gene_function_ecological_agora__REPORT.md"]
aliases: ["UniRef100", "UniRef50", "UniRef50 clusters", "UniRef90", "refdata_uniref"]
---
# UniRef

This page covers UniRef, the UniProt reference clusters at 100%, 90% and 50% identity (2026-01 snapshot) held in refdata. Cluster counts come from the platform inventory. The ecological-agora pilot gives mixed evidence on how well UniRef50 resolves HGT (horizontal gene transfer) and family-level signals. [src: gene_function_ecological_agora]

## Key facts

- The KBase Data Lakehouse inventory lists 475,217,233 UniRef100, 188,848,220 UniRef90 and 60,315,044 UniRef50 clusters (2026-01). [src: berdl_data_atlas]
- A shorter summary gives the same totals as 475M UniRef100 + 189M UniRef90 + 60M UniRef50 protein clusters. [src: berdl_data_atlas]
- The tables refdata_uniref50_2026_01, refdata_uniref90_2026_01 and refdata_uniref100_2026_01 supply the clusters at 3 redundancy levels. [src: berdl_data_atlas]
- For reference proteins and families, the data atlas recommends refdata_uniref{50,90,100} plus refdata_uniprot, cross-referenced via protein_id or pfam_id. [src: berdl_data_atlas]
- The kbase_ke_pangenome bakta_db_xrefs table maps each gene_cluster to UniRef50, UniRef90 or UniRef100. These are the db = 'UniRef' rows, with the tier embedded in the accession. [src: gene_function_ecological_agora]

## UniRef50 as a bridge from Bakta annotations

In the bakta_reannotation comparison, [[entities/bakta]] uniquely provides UniRef50 links, with 79.2% coverage. [src: discoveries] The bridge reaches RefSeq for 71% of matched IDs (identifiers), OrthoDB for 46%, STRING for 40% and KEGG for 36%. [src: discoveries] GO (Gene Ontology), EC (Enzyme Commission), InterPro and Pfam are missing from the bridge. Importing full UniProt would unlock them. [src: discoveries] See [[concepts/annotation-source-disagreement-and-coverage]].

## Resolution of UniRef50 for HGT and family signals

The pilot's interpretation is that UniRef50 is the right resolution for an existence test. It reads UniRef50 as too narrow for Alm 2006-type family-level signals. [src: gene_function_ecological_agora] An earlier pre-registered claim said UniRef50 captures sequence-cluster-specific variants and is too narrow for family-level HGT or paralog signal. [src: gene_function_ecological_agora]

The report later retracted a stricter claim, "UniRef50 cannot detect HGT". It called that claim too pessimistic, because UniRef50 produces small but real HGT signal. [src: gene_function_ecological_agora] It also reformulated the substrate-hierarchy claim as "we used the wrong metric on the right substrate", rather than "UniRef50 is too narrow, aggregate to KO". [src: gene_function_ecological_agora]

The KO (KEGG ortholog) projection assigns dominant KOs to 3,592,556 UniRef50s. The median dominant-fraction is 1.0 and q25 is 0.97, which the report calls a clean projection. [src: gene_function_ecological_agora]

## Tensions

- The pilot is read as supporting UniRef50 as too narrow for Alm 2006-type family-level signals. [src: gene_function_ecological_agora] The report also retracts the strict claim that UniRef50 cannot detect HGT. [src: gene_function_ecological_agora] It reformulates the substrate-hierarchy claim as a wrong-metric problem on the right substrate. [src: gene_function_ecological_agora] The cited claims do not say whether the family-level narrowness reading survives that reformulation.

## Open Directions

- Re-test family-level HGT signal at UniRef50 with the corrected metric, and compare it with UniRef90 and UniRef100 through the bakta_db_xrefs tiers.
- Import full UniProt to fill the GO, EC, InterPro and Pfam gaps in the UniRef50 bridge, then measure the added coverage.
