---
type: "Dataset"
description: "Hierarchical eggNOG orthology annotations used at the Firmicutes level with Bacteria/root fallback."
sources: ["summaries/bacillota_b_subsurface_accessory__REPORT.md", "summaries/cog_analysis__REPORT.md", "summaries/discoveries.md", "summaries/enigma_contamination_functional_potential__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/gene_function_ecological_agora__REPORT.md", "summaries/lanthanide_methylotrophy_atlas__REPORT.md", "summaries/oak_ridge_cultivation_gap__REPORT.md", "summaries/phb_granule_ecology__REPORT.md", "summaries/plant_microbiome_ecotypes__REPORT.md", "summaries/prophage_ecology__REPORT.md", "summaries/truly_dark_genes__REPORT.md"]
aliases: ["OG", "eggNOG", "eggNOG OG", "eggNOG v6", "eggNOG-mapper", "eggnog_mapper_annotations"]
---
# eggNOG orthologous groups

This page covers hierarchical eggNOG orthology annotations used at the Firmicutes level with Bacteria/root fallback. The Bacillota_B analysis used them this way. [src: bacillota_b_subsurface_accessory] Most results below are single-project measurements, and the page notes the limits next to each.

## Key facts

- eggNOG-mapper is described by Cantalapiedra et al. (2021, Mol Biol Evol). [src: lanthanide_methylotrophy_atlas]
- The Bacillota_B analysis used hierarchical eggNOG orthology at the Firmicutes level (eggNOG tax 1239) where present, falling back to Bacteria/root. [src: bacillota_b_subsurface_accessory] Its notebook 02_og_presence.ipynb builds a genome × eggNOG OG presence matrix this way. [src: bacillota_b_subsurface_accessory]
- Some enriched Bacillota_B OGs are at coarse root level. eggNOG has no Bacillota_B-specific tier, because Bacillota_B is GTDB-defined and eggNOG uses NCBI taxonomy. [src: bacillota_b_subsurface_accessory]
- The table eggnog_mapper_annotations in [[entities/kbase-ke-pangenome]] gives KO, COG, KEGG_Pathway and BRITE annotation per gene_cluster. [src: gene_function_ecological_agora] It also gives PFAMs, which projects used as a domain-name fallback for control detection. [src: gene_function_ecological_agora]
- Several projects used the table: the COG analysis (with gene_cluster and gene_genecluster_junction) [src: cog_analysis], the ENIGMA contamination project for COG-derived features [src: enigma_contamination_functional_potential], and the plant microbiome project. [src: plant_microbiome_ecotypes]

## Coverage and comparison with Bakta

eggNOG outperforms [[entities/bakta]] on enrichment-style annotations, but Bakta adds clusters that eggNOG misses. [src: discoveries]

- In the bakta_reannotation comparison, eggNOG coverage versus Bakta was 51% vs 8.2% for COG, 38.5% vs 17.3% for KEGG and 63% vs 7.7% for Pfam. [src: discoveries]
- Bakta rescues 11.2M clusters (of 39.2M) that eggNOG misses entirely. [src: discoveries]
- The union of the two raises any-functional-annotation coverage from ~70% to 77.3%. [src: discoveries]
- The report describes Bakta's PSC as using DIAMOND fast mode, while eggNOG uses HMM-based ortholog assignment. [src: discoveries]
- The report treats eggNOG as the better current source for COG/KEGG/Pfam enrichment analysis. [src: discoveries]
- In the COG analysis, COG annotations covered ~70% of genes, and unassigned genes may skew distributions. [src: cog_analysis] That report also notes that eggNOG v6 annotations may differ from original COG assignments. [src: cog_analysis]
- In the gene_function_ecological_agora KO extraction, 74,450,297 clusters were eggNOG-annotated (71.8% annotation rate). [src: gene_function_ecological_agora] Parsing KEGG_ko gave 43,803,890 gene-cluster–KO edges [src: gene_function_ecological_agora] and 13,062 unique KOs. [src: gene_function_ecological_agora]
- Among truly dark clusters, eggNOG-mapper gave 2,551 annotations for 2,551 clusters (43.5%). [src: truly_dark_genes] Only 17.0% had COG categories and 4.6% had KEGG KOs. [src: truly_dark_genes] The report says 55.4% of COG assignments were category S, function unknown. [src: truly_dark_genes]
- For candidate DvH/206658, eggNOG suggested trehalose synthase despite the hypothetical annotation. The report calls this a potential mis-annotation or novel variant. [src: truly_dark_genes]

## Agreement with Genome Depot KO calls

For 147 matched ENIGMA cultured genomes (153 ENIGMA records), the report compared Genome Depot KEGG ortholog calls with pangenome eggNOG-mapper calls. [src: oak_ridge_cultivation_gap] Pooled across genomes, the two agreed on 5,751 KOs, with 1,505 Depot-only and 148 eggNOG-only assignments (Jaccard 0.777). [src: oak_ridge_cultivation_gap] Per-genome Jaccard was much lower (median 0.140, IQR 0.057–0.400). [src: oak_ridge_cultivation_gap] The report attributes this to eggNOG calling a narrower KO set per genome (typically ~1,000–1,800 KOs, vs ~1,500–2,200 for the Depot), which inflates the union denominator. [src: oak_ridge_cultivation_gap] It reads the gap as pipeline sensitivity differences, not systematic disagreement about which functions are present. [src: oak_ridge_cultivation_gap]

## Mislabeling and non-specific calls

- eggNOG Preferred_name='lanM' flags 505 additional genomes, none also Bakta-validated. They are concentrated in unrelated gut Bacillota, such as Streptococcus pneumoniae (10), Blautia_A wexlerae (9), Enterococcus faecalis (8) and Ruminococcus_B gnavus (8). [src: discoveries, lanthanide_methylotrophy_atlas] None of them are lanthanide users. [src: lanthanide_methylotrophy_atlas] The reports suggest that the [[entities/lanmodulin]] label is a stale or propagated seed-ortholog mislabeling, not true homology, and worth reporting upstream. [src: discoveries, lanthanide_methylotrophy_atlas]
- Filtering eggNOG by KEGG_ko LIKE '%K02030%' returns 46,369 hits across nearly every phylum, almost none of which are xoxJ. [src: discoveries]
- In the lanthanide atlas, genomes were called by both sources, by eggNOG only and by Bakta only: [src: lanthanide_methylotrophy_atlas]

| Gene | Both | eggNOG only | Bakta only | Report's choice |
|---|---|---|---|---|
| xoxJ | 41 | 46,369 | 20 | Bakta only, because KO K02030 is non-specific [src: lanthanide_methylotrophy_atlas] |
| xoxF | 418 | 3,272 | 1,402 | eggNOG K00114 primary, Bakta as union [src: lanthanide_methylotrophy_atlas] |
| mxaF | 4 | 191 | 8 | eggNOG K14028 [src: lanthanide_methylotrophy_atlas] |

## Format and breadth pitfalls

- The eggNOG PFAMs column stores domain names (for example HisKA), not accessions (PF00512). [src: gene_function_ecological_agora]
- In the PHB project, all 11,792 phaC clusters fell into "other_pfam" for this reason, because eggNOG gave Abhydrolase_1 and PhaC_N instead of PF00561 and PF07167. The report says this remains a limitation. [src: phb_granule_ecology]
- In the same project, phaR (K18080) was absent from all 27K species in the eggNOG annotations. The report suggests poor annotation coverage or misassignment. [src: phb_granule_ecology]
- The eggNOG OG breadth classification does not discriminate among dark gene candidates. 99.9% of dark gene clusters (30,721 of 30,756) map to universal root-level OGs. [src: functional_dark_matter]
- Annotation-derived proxies are coarse. The ENIGMA COG-fraction proxies are coarse summaries, not curated resistance pathways. [src: enigma_contamination_functional_potential] The prophage project used eggNOG annotations as proxies for prophage genes rather than dedicated tools. [src: prophage_ecology] This likely inflates prevalence, and the false positive rate is uncharacterized. [src: prophage_ecology]

## Large-scale uses

- Dark-gene conservation (NB11b) used a Spark query exploding eggNOG_OGs across 93.5M gene clusters, matching 11,774 dark gene root OGs in the full 27,690-species GTDB r214 pangenome. [src: functional_dark_matter]
- PHB pathway KOs gave 118,513 gene clusters across 19,496 species. [src: phb_granule_ecology]
- Prophage queries (93M annotations, 112 WHERE conditions) found 4,005,537 prophage-associated gene clusters across 27,702 species. [src: prophage_ecology]
- In the plant microbiome project, server-side aggregation of 93M annotations gave prevalence for 5,671 OGs passing a 5% prevalence filter. [src: plant_microbiome_ecotypes] Fisher's exact tests with Benjamini-Hochberg false discovery rate (BH-FDR) correction found 5,341 (94.2%) significantly associated with plant status. [src: plant_microbiome_ecotypes] Of those, 3,840 showed strong enrichment (odds ratio >2). [src: plant_microbiome_ecotypes]
- The KO substrate used the Phase 1B set of 18,989 species. [src: gene_function_ecological_agora]
