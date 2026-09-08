---
type: Summary
description: Links metabolic pathway capability, fitness dependency, and pangenome
  openness.
doc_type: short
full_text: ../sources/pathway_capability_dependency__REPORT.md
title: Metabolic Capability vs Dependency
sources:
- id: pathway_capability_dependency
  resource: ../sources/pathway_capability_dependency__REPORT.md
  title: pathway capability dependency
---
# Metabolic Capability vs Dependency

## Overview

This project crossed GapMind pathway-completeness predictions with RB-TnSeq fitness data from the Fitness Browser to classify 161 organism-pathway combinations across 7 model bacteria. It distinguishes genomic capability from experimentally observed dependency and extends the analysis to 2,810 GTDB species with at least 10 genomes, testing relationships among pathway variation, accessory genes, pangenome openness, and metabolic ecotypes. [^pathway_capability_dependency]

## Key Findings

### Capability and dependency are distinct

Of 161 organism-pathway pairs spanning 7 Fitness Browser organisms and 23 GapMind pathways, 57 (35.4%) were **Active Dependency** pairs, 66 (41.0%) were **Latent Capability**, 24 (14.9%) were **Incomplete but Important**, and 14 (8.7%) were **Missing**. Active Dependency denotes a complete pathway containing fitness-important genes; Latent Capability denotes a complete pathway whose genes showed no significant fitness defects under standard conditions; Incomplete but Important denotes GapMind-incomplete pathways whose mapped genes were fitness-important; and Missing denotes pathways that were neither complete nor important. [^pathway_capability_dependency]

The composite importance score weighted essentiality at 40%, fitness breadth at 30%, and fitness magnitude at 30%. Fitness Browser genes were mapped to GapMind pathways through Fitness Browser-native KEGG annotations using the besthitkegg-to-keggmember-to-EC-to-KEGG-map-to-GapMind pathway route. [^pathway_capability_dependency]

### Latent capability is condition-dependent

Condition-type stratification showed that all 66 Latent Capability organism-pathway pairs became fitness-important under at least one condition type. Nitrogen limitation, stress, and carbon limitation were the most frequent triggers, indicating that the aggregate laboratory classification reflects tested conditions rather than permanent dispensability. [^pathway_capability_dependency]

The report cautions that this result is partly affected by the median-based importance threshold: applying condition-specific subsets and a median threshold can cause pathways to cross the threshold by construction. Independent calibration against known essentials is needed before treating every reclassification as biological confirmation. [^pathway_capability_dependency]

### Active Dependencies are slightly more conserved

Active Dependencies had mean core gene completeness of 0.986, compared with 0.975 for Latent Capabilities. The small difference was attributed partly to the use of well-studied model organisms with near-complete, well-annotated core genomes. [^pathway_capability_dependency]

The Tier 1 organisms were *Desulfovibrio vulgaris* Hildenborough, *Shewanella oneidensis* MR-1, *Pseudomonas putida* KT2440, *Pseudomonas stutzeri* RCH2, *Caulobacter crescentus*, *Sinorhizobium meliloti*, and *Azospirillum brasilense*. Only 7 of the 48 Fitness Browser organisms had matching GapMind genome data. [^pathway_capability_dependency]

### Variable pathways correlate with open pangenomes

Across 2,810 GTDB species with at least 10 genomes, variable pathway count had a raw Spearman correlation with pangenome openness of rho=0.327, p=7.2e-71. The partial Spearman correlation controlling for genome count was rho=0.530, p=2.83e-203, supporting the hypothesis that species with more pathway variation tend to have more open and fluid pangenomes. [^pathway_capability_dependency]

The pathway-openness signal was positive in 13 of 18 genera tested and statistically significant at p<0.05 in 5 of 18 genera: Clostridium, Eubacterium, Mesorhizobium, Pseudomonas, and Streptomyces. The strongest within-genus correlations were rho=0.534 for Clostridium and rho=0.506 for Eubacterium. [^pathway_capability_dependency]

The analysis covered 80 GapMind pathways—18 amino acid biosynthesis pathways and 62 carbon-source utilization pathways—using data from approximately 293,000 genomes. The report presents pathway variability as a mechanistically interpretable correlate of pangenome openness, contrasting with the null relationships between openness and broader environment or phylogeny effect sizes reported by the pangenome_openness project. [^pathway_capability_dependency]

### Accessory genes contribute to amino acid biosynthesis

Core-only versus all-gene GapMind completeness showed the largest accessory-dependent gaps for amino acid biosynthesis. Leucine biosynthesis had all-gene completeness 0.614, core-only completeness 0.468, and a gap of 0.146; valine had 0.614, 0.468, and 0.146; arginine had 0.613, 0.472, and 0.141; lysine had 0.804, 0.664, and 0.140; and threonine had 0.803, 0.663, and 0.140. [^pathway_capability_dependency]

These exact core-versus-all differences indicate that pathway completeness for these amino acid biosynthesis routes depends partly on genes outside the universally conserved core. The report interprets this distribution as consistent with Black Queen dynamics and as a potential basis for community-level sharing of leucine, valine, arginine, and lysine biosynthetic capacity, while noting that the analysis does not itself demonstrate metabolite exchange. [^pathway_capability_dependency]

### Metabolic ecotypes track pangenome openness

Among 225 species with at least 50 genomes and at least 3 variable pathways, binary completeness profiles across 80 pathways were clustered using hierarchical clustering with Jaccard distance. The median number of metabolic ecotypes was 4 per species, and the maximum was 8, observed in *Alistipes onderdonkii* and *Barnesiella intestinihominis*. [^pathway_capability_dependency]

Ecotype count correlated with pangenome openness at raw Spearman rho=0.262, p=6.8e-05, and at partial rho=0.322, p=8.0e-07 after controlling for genome count. This supports the interpretation that within-species metabolic diversity is associated with genome fluidity rather than being explained only by sampling depth. [^pathway_capability_dependency]

### Relationship to fitness conservation

The report connects its findings to prior BERDL results: 87.4% of metal-fitness genes were core, with OR=2.08 for enrichment; 28,017 genes were costly in laboratory conditions but conserved in nature; and field-important genes were 83.6% core compared with a 76.3% baseline. These comparisons frame Active Dependencies and accessory-dependent pathways as pathway-level extensions of broader fitness-conservation and condition-dependent-fitness patterns. [^pathway_capability_dependency]

## Caveats

- Fitness Browser coverage limited Tier 1 to 7 of 48 organisms with matching GapMind data, and these model organisms had near-complete core genomes that compressed the conservation-validation signal. [^pathway_capability_dependency]
- GapMind covered 80 pathways—18 amino acid biosynthesis pathways and 62 carbon-source utilization pathways—but did not assess cofactor biosynthesis, lipid metabolism, or secondary metabolism. [^pathway_capability_dependency]
- Laboratory fitness does not capture the full range of natural selective pressures; the report specifically notes that 28,017 genes were costly in laboratory conditions but conserved in nature. [^pathway_capability_dependency]
- KEGG-based mapping can miss genes lacking KEGG annotations or carrying incorrect annotations, potentially underestimating the number of genes assigned to a pathway. [^pathway_capability_dependency]
- Ecotype counts depend on hierarchical clustering with a fixed 50% maximum-distance cut; different thresholds would produce different counts, so the median of 4 should be treated as an order-of-magnitude estimate. [^pathway_capability_dependency]
- Correlations were controlled for genome count and checked within taxonomic groups, but full phylogenetic independent contrasts were not computed. The related ecotype_analysis project found that phylogeny dominates gene content in 60.5% of species. [^pathway_capability_dependency]
- Species with more sequenced genomes are more likely to show pathway variation and more ecotypes; partial correlations reduce but do not eliminate this sampling bias. [^pathway_capability_dependency]
- The median-based importance threshold is circular for condition-specific reclassification, because applying a median threshold to each subset can cause pathways to cross it. An independent validation set, such as known essentials from essential_metabolome, would provide a more defensible threshold. [^pathway_capability_dependency]
- The proposed correlation between metabolic ecotypes and AlphaEarth environmental niche breadth was not executed. AlphaEarth embeddings covered 28% of genomes, or 83K/293K, which would limit the available sample size. [^pathway_capability_dependency]

## Slots Into

- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — the finding that all 66 aggregate Latent Capability pairs became fitness-important under at least one condition type, while the threshold caveat motivates independent validation. [^pathway_capability_dependency]
- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) — the comparison of GapMind pathway completeness with fitness evidence, including 24 Incomplete but Important pairs that may reflect annotation gaps or salvage routes. [^pathway_capability_dependency]
- [pangenome-integration](../concepts/pangenome-integration.md) — the partial Spearman relationship between variable pathway count and pangenome openness, rho=0.530 and p=2.83e-203 after controlling for genome count. [^pathway_capability_dependency]
- [ecotype-environment-gene-content](../concepts/ecotype-environment-gene-content.md) — the identification of 2–8 metabolic ecotypes per species and the partial ecotype-openness correlation of rho=0.322, p=8.0e-07. [^pathway_capability_dependency]
- [gene-essentiality](../concepts/gene-essentiality.md) — the four-way classification combining pathway completeness with gene-level essentiality and fitness breadth. [^pathway_capability_dependency]
- [gene-function-acquisition-depth](../concepts/gene-function-acquisition-depth.md) — the evidence that accessory genes contribute to pathway completeness, with exact gaps of 0.146 for leucine and valine and 0.141–0.140 for arginine, lysine, and threonine biosynthesis. [^pathway_capability_dependency]

[^pathway_capability_dependency]: [pathway capability dependency](../sources/pathway_capability_dependency__REPORT.md)
