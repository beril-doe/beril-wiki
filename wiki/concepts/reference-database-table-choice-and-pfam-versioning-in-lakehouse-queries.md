---
type: "Concept"
description: "Practical pitfalls when querying domain tables and writing outputs from Spark in the Lakehouse: table coverage, accession versioning, and write locations."
sources: ["summaries/gene_function_ecological_agora__REPORT.md", "summaries/phage_defense_arsenal__REPORT.md", "summaries/pitfalls.md", "summaries/plant_microbiome_ecotypes__REPORT.md"]
---
# Reference-database table choice and Pfam versioning in Lakehouse queries

This page covers pitfalls when querying domain tables and writing Spark outputs in the Lakehouse: table coverage, accession versioning and write locations. In two projects, bakta_pfam_domains had no hits for some marker Pfams: seven of 33 in one audit, and Cas1 PF01867 in another, where InterProScan had about 25K. [src: gene_function_ecological_agora, phage_defense_arsenal] Its versioned IDs (identifiers) caused zero-hit queries until a LIKE pattern fixed them. [src: plant_microbiome_ecotypes] See [[entities/bakta-pfam-domains]], [[entities/pfam-domain-annotations]] and [[concepts/domain-based-marker-detection-and-annotation-method-bias]] for related material.

## Which table to query

InterProScan is the recommended default for domain-accession queries, and bakta_pfam_domains is only a supplement. gene_function_ecological_agora recommends interproscan_domains as the default substrate for domain-accession queries, not eggNOG PFAMs. [src: gene_function_ecological_agora] Its first pilot did not use the table, which holds 146 M Pfam hits across 132.5 M cluster representatives with 83.8 % cluster coverage. [src: gene_function_ecological_agora] phage_defense_arsenal found interproscan_domains (833M rows) to be far broader than bakta_pfam_domains (18.8M rows) and used it as its primary defense-detection table. [src: phage_defense_arsenal] plant_microbiome_ecotypes advises treating bakta_pfam_domains as a supplement to interproscan_domains and cross-checking Pfam queries against it before concluding that a function is missing. [src: plant_microbiome_ecotypes]

The cost of choosing the narrow table was concrete:
- An audit found 7 of 33 marker Pfams with zero clusters in bakta_pfam_domains. These included all 4 critical PSII (photosystem II) Pfams: PsbA/PF00124, PsbB/PF02530, PsbC/PF02533 and PsbD/PF00421. [src: gene_function_ecological_agora]
- The Cyanobacteria PSII hypothesis test would have been structurally impossible on that table. [src: gene_function_ecological_agora]
- CRISPR Cas1 PF01867 returns 0 hits in bakta_pfam_domains but about 25K in InterProScan. [src: phage_defense_arsenal]

A single query on interproscan_domains is practical. Filtering to about 20 curated Pfam accessions and joining gene_cluster on gene_cluster_id returned about 500K rows in under 90 s, with no per-species batching. [src: phage_defense_arsenal]

## eggNOG PFAMs stores names, not accessions

The eggnog_mapper_annotations.PFAMs column holds domain names such as DUF4041 and GIY-YIG, not accessions such as PF13250 and PF01541. [src: pitfalls] In snipe_defense_system, searching for PF13250 returned 0 rows. [src: pitfalls] Searching for DUF4041 returned 2,962 rows. [src: pitfalls] The column holds comma-separated lists, so queries should use LIKE with % wildcards, not exact equality. [src: pitfalls] The report's checklist says to search this column by domain name, not accession. [src: pitfalls]

### Row counts after joining

In snipe_defense_system, 2,962 DUF4041 annotation records became 4,572 rows after joining gene_cluster. The same query_name can map to clusters in several species pangenomes. [src: pitfalls] The post-join count is species-level gene clusters, and the eggNOG count is unique annotation records. Both are valid, so state which one you report. [src: pitfalls]

## Looking up accessions by name

Name-only lookups can return the wrong accession. [src: pitfalls] PF13250 and PF13291 are numerically close but unrelated families. [src: pitfalls] PF01541 (canonical GIY-YIG) and PF13455 (Mug113) share a clan but are distinct families. [src: pitfalls] For SNIPE, DUF4041 is PF13250 (IPR025280), not PF13291 (ACT_4). [src: pitfalls] The SNIPE nuclease is PF13455 (Mug113, GIY-YIG clan CL0418), not PF01541. [src: pitfalls] Warning signs are zero co-occurrence hits for domains that should co-occur, such as DUF4041 with GIY-YIG in SNIPE proteins, or unexpected annotations. [src: pitfalls] The fix is to verify accessions against a known protein in InterPro or UniProt. [src: pitfalls]

## Versioned and version-free accessions

interproscan_domains.signature_acc uses version-free accessions such as PF01867. bakta_pfam_domains.pfam_id uses versioned ones such as PF01867.29. [src: phage_defense_arsenal] Cross-database joins must strip the version on the Bakta side. phage_defense_arsenal said this was not documented in docs/pitfalls.md for kbase_ke_pangenome and that it cost about 15 min of debugging. [src: phage_defense_arsenal] See [[entities/kbase-ke-pangenome]].

The pitfalls digest first recorded this as unexplained. In plant_microbiome_ecotypes, querying bakta_pfam_domains with IDs like 'PF00771' returned 0 hits across all 11 domains tested. [src: pitfalls] The digest guessed that the table might use names or versioned accessions [src: pitfalls] and left the correct format open. [src: pitfalls] plant_microbiome_ecotypes later resolved this. Its NB02 query returned zero rows because the table stores versioned IDs such as PF00771.22. [src: plant_microbiome_ecotypes] A LIKE 'PF00771%' pattern fixed it in NB13 Cell 3. [src: plant_microbiome_ecotypes] On the 10 Phase 2b marker Pfams, that pattern recovered 19,364 domain hits across 7,962 species. [src: plant_microbiome_ecotypes] This refines the earlier open item.

## Writing outputs from Spark

Spark Connect .write.parquet() writes to cluster storage (S3), not the client notebook filesystem. A call such as df.write.mode("overwrite").parquet("../data/foo.parquet") can return success and leave only an empty local _SUCCESS marker. [src: phage_defense_arsenal] For on-cluster notebook artifacts, phage_defense_arsenal recommends .toPandas() followed by pandas.to_csv(..., compression="gzip"). It cites projects/prophage_ecology/notebooks/01_prophage_gene_discovery.ipynb as the canonical example. [src: phage_defense_arsenal]

## Open Directions

- Re-run earlier bakta_pfam_domains-based absence calls with LIKE 'PFxxxxx%' patterns and compare them to interproscan_domains. This would show how many "missing function" conclusions came from the table or the ID format.
- Add the version-free versus versioned accession mismatch to the shared pitfalls documentation for kbase_ke_pangenome, with a tested join recipe that strips versions.
- Measure why bakta_pfam_domains lacks PSII and Cas1 Pfams, for example by comparing coverage per Pfam against InterProScan. This would show whether the gap is systematic.
- Report both the eggNOG record count and the post-join species-cluster count in future defense-marker tables, to close the ambiguity about which is reported.
