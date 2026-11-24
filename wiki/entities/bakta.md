---
type: "Method"
description: "Genome annotation tool whose alternative EC and product annotations were queried for dark reactions."
sources: ["summaries/annotation_gap_discovery__REPORT.md", "summaries/discoveries.md", "summaries/functional_dark_matter__REPORT.md", "summaries/lanthanide_methylotrophy_atlas__REPORT.md", "summaries/truly_dark_genes__REPORT.md"]
aliases: ["Bakta v1.12.0", "bakta v1.12.0"]
---
# Bakta

Bakta (also written Bakta v1.12.0 or bakta v1.12.0) is a genome annotation tool. Across the reports below, its annotations were used to re-annotate dark genes and to look for alternative EC and product annotations for dark reactions. Schwengers et al. (2021, Microbial Genomics) describes the bakta annotation pipeline. [src: lanthanide_methylotrophy_atlas]

## Key facts

- The bakta_reannotation comparison covers bakta v1.12.0 against eggNOG-mapper across 132.5M gene clusters. [src: discoveries]
- The functional_dark_matter report cross-references Bakta v1.12.0 (DB v6.0) annotations for the 132.5M pangenome cluster representatives against its 57,011 dark-gene catalog. [src: functional_dark_matter]

## Coverage compared with eggNOG

eggNOG has higher coverage for enrichment-style annotations. It reaches 51% vs 8.2% for COG (clusters of orthologous groups), 38.5% vs 17.3% for KEGG and 63% vs 7.7% for Pfam. [src: discoveries] Bakta has higher coverage for GO (Gene Ontology) terms (15% vs 7.4%) [src: discoveries] and for product descriptions (71.2% vs 70.4%). [src: discoveries] Bakta uniquely provides UniRef50 links, at 79.2% coverage. [src: discoveries] See [[entities/eggnog-orthologous-groups]], [[entities/uniref]] and [[concepts/annotation-source-disagreement-and-coverage]].

### Why COG, KEGG and Pfam coverage is low

The report attributes confirmation of this design-driven gap to developer Oliver Schwengers across GitHub issues #350, #385, #391 and #393. [src: discoveries] It lists these causes:

- Bakta's PSC database is optimized for product descriptions, not functional categories. Only ~14% of PSC entries have COG and ~19% have KEGG. [src: discoveries]
- COG 2024 no longer provides representative sequences. This forces a lossy indirect WP accession→IPS→PSC mapping. [src: discoveries]
- HMMER runs only on hypotheticals (~7.7%). The 92% with PSC matches never get Pfam searched. [src: discoveries]
- Bakta's PSC uses DIAMOND fast mode, while eggNOG uses HMM-based ortholog assignment, which the report describes as more sensitive. [src: discoveries]
- The developer planned to integrate eggNOG into PSC representatives (issue #325). This may have partially happened in DB v6.0, but with limited impact. [src: discoveries]

The report states that the Arche benchmark paper (Alonso-Reyes & Albarracin 2025, PMID 40811208) independently confirmed Bakta's conservative annotation transfer relative to other tools. [src: discoveries]

## Dark-gene reannotation

Of 39,532 dark genes with pangenome links, Bakta reclassifies 33,105 (83.7%) as not hypothetical. Its PSC/PSCC pipeline assigns product descriptions where the Fitness Browser had only "hypothetical protein". [src: functional_dark_matter] This leaves 6,427 truly dark genes that both pipelines call hypothetical. [src: truly_dark_genes] The reclassified genes represent 58.1% of all dark genes. [src: functional_dark_matter] The truly_dark_genes report labels these 33,105 genes "annotation-lag" and interprets them as a database vintage problem. [src: truly_dark_genes] See [[entities/fitness-browser]] and [[concepts/reannotation-lag-versus-genuinely-unannotatable-dark-genes]].

- The functional_dark_matter report reads the Bakta annotations as independent validation of experimental prioritization. It says the dark genes with the strongest fitness effects tend to be annotated in UniProt but absent from the Fitness Browser's annotation vintage. [src: functional_dark_matter]
- Bakta's AMRFinderPlus assigns AMR (antimicrobial resistance) annotations to 5 dark genes. [src: functional_dark_matter]
- Of the 6,427 genes still hypothetical in both the Fitness Browser and Bakta, 79.4% gain UniRef50 links. [src: functional_dark_matter]
- Adding has_bakta_annotation as a 7th evidence flag changes the darkness tier of 18,019 genes. The largest shifts are from T4 Penumbra to T5 Dawn, as genes gain their final missing evidence line. [src: functional_dark_matter]
- Caveat: some "hypothetical protein" calls may be Bakta false negatives. These would be genes with known functions that did not match the PSC database at the version tested (v6.0). [src: truly_dark_genes]

## Dark reactions

The annotation_gap_discovery pipeline queried Bakta annotations for alternative EC (Enzyme Commission) numbers and product-name matches for dark reactions. [src: annotation_gap_discovery] This added 22 newly resolved pairs (10.9%) and yielded 1,459 Bakta EC candidate entries. [src: annotation_gap_discovery] The run produced data/bakta_ec_alternatives.tsv, with 1,459 rows of Bakta-derived alternative EC annotations for dark or unmatched reactions. [src: annotation_gap_discovery] It also produced data/uniref_ids_for_blast.tsv, with 54,549 rows of UniRef IDs (identifiers) extracted from Bakta for target gene clusters. [src: annotation_gap_discovery] See [[concepts/multi-evidence-triangulation-of-metabolic-annotation-gaps]].

## Lanmodulin and specialty markers

Bakta product='Lanmodulin' flags 62 genomes. All are in α-Proteobacterial methylotroph clades: Beijerinckiaceae Methylobacterium, Acetobacteraceae BOG-930 and Hyphomicrobiaceae. [src: discoveries, lanthanide_methylotrophy_atlas] For specialty markers such as Lanmodulin and XoxJ, the lanthanide_methylotrophy_atlas calibration finds that Bakta's curated product field outperforms eggNOG's Preferred_name. The report calls this generalizable beyond rare-earth-element biology. [src: lanthanide_methylotrophy_atlas] That report recommends using bakta product exclusively for lanmodulin work in the KBase Data Lakehouse pangenome. [src: lanthanide_methylotrophy_atlas] It calls bakta product the trustworthy lanmodulin source, because eggNOG Preferred_name='lanM' is unusable. [src: lanthanide_methylotrophy_atlas] See [[entities/lanmodulin]].
