---
type: "Method"
description: "Domain and functional annotation method for gene clusters and proteins"
sources: ["summaries/alphafold_msa_annotation__REPORT.md", "summaries/amr_cofitness_networks__REPORT.md", "summaries/phage_defense_arsenal__REPORT.md", "summaries/pitfalls.md", "summaries/plant_microbiome_ecotypes__REPORT.md"]
---
# InterProScan

## What this entity is

**Canonical name:** InterProScan. [src: alphafold_msa_annotation]

**Known aliases:** No aliases are specified in this source. [src: alphafold_msa_annotation]

**Stable external identifier:** No stable external identifier is specified in this source. [src: alphafold_msa_annotation]

InterProScan is a domain-annotation method used in joins among [[entities/kbase-ke-pangenome]], Bakta annotations, InterProScan domains, and [[entities/kescience-alphafold]] AlphaFold records. [src: alphafold_msa_annotation] Its annotation tables should be joined to the pangenome at the gene-cluster level: `eggnog_mapper_annotations.query_name`, Bakta annotations, and InterProScan annotations join to `gene_cluster.gene_cluster_id`, not `gene.gene_id`. [src: pitfalls] This **refines** the earlier description by making the required join grain explicit. [src: pitfalls]

## Key facts

- Of 132,531,501 total gene clusters, 111,035,431 (83.8%) had at least one InterProScan domain annotation. [src: alphafold_msa_annotation]
- Across the analysed gene clusters, the mean number of InterProScan domain hits was 7.5 and the mean number of distinct InterPro (IPR) families was 3.3. [src: alphafold_msa_annotation]
- Among 38,051,842 gene cluster–UniProt pairs, mean domain hits increased from 0.59 for AlphaFold MSA depth below 10 to 10.83 for MSA depth at least 10,000. [src: alphafold_msa_annotation]
- Across the same 38,051,842 pairs, mean distinct InterPro families increased from 0.059 for AlphaFold MSA depth below 10 to 4.601 for MSA depth at least 10,000. [src: alphafold_msa_annotation]
- The association between AlphaFold MSA depth and InterProScan domain-hit count was Spearman ρ = 0.7563 across the full 38,051,842-pair dataset. [src: alphafold_msa_annotation]
- InterProScan domain-annotation coverage of 83.8% exceeded the 29.3% AlphaFold bridge coverage in the report. [src: alphafold_msa_annotation]
- The report found that the monotone relationship between MSA depth and domain hits held within core, auxiliary non-singleton, and auxiliary+singleton pangenome classes, with core genes showing slightly higher domain richness per MSA bin than accessory genes at equivalent depth. [src: alphafold_msa_annotation]

These results support using InterProScan domain and family counts as an annotation-richness measure in [[concepts/pangenome-integration]], while the report cautions that the MSA-depth correlation was not subgroup-stratified and that the AlphaFold-linked subset was biased toward better-studied organisms. [src: alphafold_msa_annotation]

In a separate pan-bacterial cofitness analysis, InterProScan supplied Gene Ontology (GO) annotations with 68% gene coverage, reported as 3.6× better than the old SEED annotations. [src: amr_cofitness_networks] This **supports** the existing use of InterProScan as an annotation-richness measure and **refines** it by showing that the method also enables functional-enrichment analysis: InterProScan GO produced 35/3,193 significant tests at FDR < 0.05, compared with 0/280 for the old SEED/KEGG analysis. [src: amr_cofitness_networks] The enrichment analysis identified flagellum-dependent motility, flagellum assembly, histidine biosynthesis, and tryptophan biosynthesis among recurring signals, although these may reflect shared dispensability under laboratory conditions rather than direct co-regulation. [src: amr_cofitness_networks]

The phage-defense analysis **refines** InterProScan's role from a general annotation source to a practical Pfam-domain discovery source: its primary domain table contained 833-million rows, compared with 18.8-million rows in the Bakta Pfam table. [src: phage_defense_arsenal] The same scale is a computational constraint: the InterProScan table is approximately 833M rows and requires key filters before joins, with results retained in Spark until the final small output. [src: pitfalls] Filtering InterProScan for `analysis = 'Pfam'` and a curated signature list of approximately 20 accessions, then joining to `gene_cluster`, returned ~500K rows in under 90 seconds. [src: phage_defense_arsenal] The same workflow found 0 Cas1 PF01867 hits in `bakta_pfam_domains` versus ~25K in InterProScan, so the report used InterProScan for defense-marker detection. [src: phage_defense_arsenal] InterProScan uses version-free Pfam accessions such as PF01867, whereas Bakta uses versioned accessions such as PF01867.29; cross-database joins therefore need to strip Bakta versions. [src: phage_defense_arsenal] This **supports** the earlier finding that InterProScan provides broader annotation coverage, while **qualifying** cross-source comparisons because apparent differences can reflect database scale and accession formatting rather than biology. [src: phage_defense_arsenal]

The plant-microbiome analysis **supports** this broader-coverage interpretation but **refines** it with a direct audit: 12 of 22 marker Pfams were absent from `bakta_pfam_domains`, despite being abundant in `interproscan_domains`, and the ten non-zero Bakta Pfams returned only 10–35% of the InterProScan hit counts. [src: plant_microbiome_ecotypes] Versioned-Pfam matching with `LIKE` patterns recovered 19,364 hits across 7,962 species for ten queried marker Pfams. [src: plant_microbiome_ecotypes] InterProScan was therefore used for secretion-system and cell-wall-degrading-enzyme detection in the refined plant-marker pipeline; these biological assignments were unaffected by the Bakta-table gap. [src: plant_microbiome_ecotypes] The same study annotated all 50 retained plant-enriched gene families with eggNOG descriptions and InterProScan domains, while 48/50 had GO terms and 39/50 had MetaCyc pathways, **supporting** InterProScan's utility in integrated functional annotation. [src: plant_microbiome_ecotypes]

Because pangenome gene-cluster identifiers are species-specific, they must not be compared directly across species; cross-species analyses should instead use shared representations such as COG categories, KEGG orthologs, or Pfam domains. [src: pitfalls] This **refines** the interpretation of InterProScan-richness comparisons: domain annotations can provide a shared representation, but the comparison still depends on explicit cross-species normalization. [src: pitfalls]

## Related pages

- [[summaries/alphafold_msa_annotation__REPORT]] — source summary for the analysis connecting InterProScan annotations with AlphaFold MSA depth. [src: alphafold_msa_annotation]
- [[summaries/amr_cofitness_networks__REPORT]] — source summary for the pan-bacterial cofitness analysis using InterProScan GO annotations. [src: amr_cofitness_networks]
- [[summaries/phage_defense_arsenal__REPORT]] — source summary for the pan-bacterial defense-marker analysis using InterProScan Pfam domains. [src: phage_defense_arsenal]
- [[summaries/plant_microbiome_ecotypes__REPORT]] — source summary for the plant-marker and annotation-table audit. [src: plant_microbiome_ecotypes]
- [[summaries/pitfalls]] — source summary documenting InterProScan scale, join-grain, and cross-species comparison safeguards. [src: pitfalls]
- [[concepts/pangenome-integration]] — cross-project concept covering pangenome structure and annotation coverage. [src: alphafold_msa_annotation, amr_cofitness_networks]
- [[entities/kbase-ke-pangenome]] — pangenome dataset joined to InterProScan annotations in the report. [src: alphafold_msa_annotation]
- [[entities/bakta]] — annotation method whose Pfam identifiers are compared with InterProScan. [src: phage_defense_arsenal]
- [[entities/kescience-alphafold]] — AlphaFold dataset used to compare MSA depth with InterProScan richness. [src: alphafold_msa_annotation]
- [[entities/uniprot]] — protein-accession resource used in the AlphaFold bridge. [src: alphafold_msa_annotation]
