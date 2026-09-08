---
type: Summary
description: Module-level prophage ecology analysis across bacterial phylogeny and
  environments
doc_type: short
full_text: ../sources/prophage_ecology__REPORT.md
title: Prophage Gene Modules and Terminase-Defined Lineages Across Bacterial Phylogeny
  and Environmental Gradients
sources:
- id: prophage_ecology
  resource: ../sources/prophage_ecology__REPORT.md
  title: prophage ecology
---
# Prophage Gene Modules and Terminase-Defined Lineages Across Bacterial Phylogeny and Environmental Gradients

## Overview

This report analyzes prophage-associated gene modules across 27,702 bacterial species using 4,005,537 eggNOG-annotated gene clusters, environmental and phylogenetic metadata, TerL lineage clustering, module co-occurrence tests, and taxonomy-based validation in 6,365 NMDC metagenomic samples. It finds that prophage-associated annotations are nearly universal but structurally variable, that environment explains module composition beyond host phylogeny and genome size, and that environmental signals are concentrated in structural and anti-defense modules rather than in near-universal core modules. [^prophage_ecology]

## Key Findings

### 1. Prophage modules are widespread but structurally variable

All 27,702 analyzed bacterial species carried prophage-associated gene clusters, totaling 4,005,537 clusters. Packaging (module A) and lysogenic regulation (module F) were present in 100.0% of species, lysis (module D) in 99.9%, integration (module E) in 99.1%, anti-defense (module G) in 64.3%, head morphogenesis (module B) in 56.1%, and tail (module C) in 55.6%; 34.9% of species carried all 7 modules. [^prophage_ecology]

The module cluster counts were 707,217 for packaging, 87,336 for head morphogenesis, 189,271 for tail, 724,499 for lysis, 773,417 for integration, 1,682,902 for lysogenic regulation, and 63,508 for anti-defense. Modules D and A were predominantly core genes, with 62.6% and 57.0% core status respectively, whereas E and B were predominantly singletons, with 59.3% and 56.0% singleton status respectively. [^prophage_ecology]

The report interprets modules A, D, and F as potentially containing many domesticated, defective prophage remnants, while modules B, C, and G are more structurally variable and therefore more informative for ecological analyses of relatively complete prophage elements. This interpretation is an inference from annotation patterns and is limited by the absence of dedicated prophage detection. [^prophage_ecology]

### 2. Environment explains prophage composition beyond phylogeny

PERMANOVA, a permutation-based multivariate analysis of variance, on Bray-Curtis prophage-module composition across a 1,773-species subsample found significant effects for genome-size quartile, environment, and family-level phylogeny, each with p=0.01. Genome size was dominant (F=212.99), followed by environment (F=30.04) and phylogeny (F=6.17); genome size also correlated with prophage cluster count at rho=0.717. [^prophage_ecology]

Kruskal-Wallis tests within every genome-size quartile found significant environmental effects on prophage module count, with all p < 6.5e-78, indicating that the environmental signal was not explained solely by genome size. AlphaEarth embedding analysis of 2,008 species with at least 5 embedded genomes found a partial Spearman correlation of rho=0.468 between environmental niche breadth and prophage module count after controlling for genome size, with p=8.41e-110. [^prophage_ecology]

The report therefore rejects the hypothesis that phylogeny alone explains prophage distribution: environment affected module composition beyond phylogeny, and the environmental effect was stronger than the family-level phylogenetic effect in the reported PERMANOVA comparison. [^prophage_ecology]

### 3. Structural and anti-defense modules are enriched in human-associated environments

Constrained permutations preserving host-family and genome-size-quartile strata across 18,031 species identified 8 significant module-by-environment enrichments at FDR < 0.05, where FDR means false discovery rate. In human-associated environments, tail had log2(OR)=2.21 and Z-score=10.86, head morphogenesis had log2(OR)=1.98 and Z-score=10.00, and anti-defense had log2(OR)=1.70 and Z-score=8.76. [^prophage_ecology]

In human-clinical environments, anti-defense was enriched with log2(OR)=0.14 and Z-score=5.14, tail with log2(OR)=0.77 and Z-score=3.90, and head morphogenesis with log2(OR)=0.70 and Z-score=3.59. Anti-defense was depleted in freshwater with log2(OR)=-0.74 and Z-score=-4.74 and in animal-associated environments with log2(OR)=-0.24 and Z-score=-8.77. [^prophage_ecology]

These results support the [phage-defense-syndromes-and-arms-race](../concepts/phage-defense-syndromes-and-arms-race.md) interpretation that human-associated bacteria may experience stronger phage-mediated selection for structurally complete prophages and counter-defense functions, but the report presents this as a consistency with coevolutionary theory rather than a direct mechanistic demonstration. [^prophage_ecology]

### 4. TerL lineages include specialist and generalist strategies without independent lineage-level enrichment

MMseqs2 clustering, using 70% AAI where AAI means amino-acid identity, grouped 38,085 TerL sequences from 11,789 species into 10,991 lineages. The largest lineage contained 1,094 members across 869 species, while 6,921 lineages (63%) were singletons; threshold sensitivity yielded 4,001 lineages at 50% AAI and 16,283 at 80% AAI. [^prophage_ecology]

No individual TerL lineage showed significant environment-specific enrichment after FDR correction in 0/500 tests. Among 824 lineages with at least 5 species, 325 were classified as specialists by Shannon entropy < 1.0 or a dominant environment > 80%, while 499 were classified as generalists distributed across 3+ environments. Specialist lineages were concentrated in animal-associated, freshwater, and marine environments. [^prophage_ecology]

The report concludes that module-level ecology and lineage-level ecology are decoupled: modules show environmental effects beyond phylogeny, whereas individual TerL lineages do not exceed the constrained host-phylogeny expectation. This supports a model in which modular exchange contributes to environmental differences without requiring independent whole-lineage adaptation. [^prophage_ecology]

### 5. NMDC data independently validates module-level environmental associations

Taxonomy-based prophage-burden inference across 6,365 NMDC metagenomic samples achieved 87.2% median matching coverage and identified 57 significant module-abiotic correlations at FDR < 0.05. The strongest reported correlations were packaging with pH (Spearman rho=0.519), all modules with pH (rho=0.474), all modules with temperature (rho=0.399), all modules with depth (rho=0.361), and all modules with total nitrogen (rho=0.333). [^prophage_ecology]

Cross-validation found concordance between pangenome enrichment and NMDC correlations for head morphogenesis, tail, and anti-defense. Packaging, lysis, integration, and lysogenic regulation were significant in NMDC data but not pangenome-enriched beyond phylogenetic expectation, consistent with their near-universal presence masking environmental variation in the pangenome analysis. [^prophage_ecology]

The positive pH association, especially for packaging, is interpreted as suggesting that alkaline environments may favor lysogeny or that prophage burden responds to pH-linked ecological conditions; the report identifies this as a hypothesis requiring mechanistic testing rather than an established causal result. [^prophage_ecology]

### 6. Core modules co-occur, while integration and anti-defense functions are more dispersed

Across 15 phylogenetically stratified species, using 200 null permutations, 44/95 module-species tests (46.3%) showed significantly higher within-module gene co-occurrence than expected by chance, with mean contig co-localization of 0.769. Packaging was significant in 11/15 tests with mean Z-score=3.40 and mean co-localization=0.986; lysis was significant in 13/15 with mean Z-score=4.45 and mean co-localization=0.901; and lysogenic regulation was significant in 10/15 with mean Z-score=2.16 and mean co-localization=1.000. [^prophage_ecology]

Head morphogenesis was significant in 1/6 tests with mean Z-score=-0.44 and mean co-localization=0.474; tail was significant in 5/12 with mean Z-score=1.43 and mean co-localization=0.752; integration was significant in 1/15 with mean Z-score=-1.93 and mean co-localization=0.420; and anti-defense was significant in 3/11 with mean Z-score=1.50 and mean co-localization=0.281. [^prophage_ecology]

These results partially support the modular organization of prophage genes and refine it into a core-backbone versus accessory-function model: packaging, lysis, and lysogenic regulation are physically linked more consistently, whereas integration genes are distributed across insertion sites and anti-defense genes are more weakly co-localized, consistent with placement in defense islands separate from the core prophage backbone. [^prophage_ecology]

## Caveats and Limitations

The analysis identifies prophage-associated genes through eggNOG functional annotations rather than dedicated prophage tools such as geNomad or VIBRANT. Consequently, the reported near-universal prevalence may include domesticated remnants and bacterial homologs of phage genes, including bacterial integrases, and the false-positive rate is uncharacterized. [^prophage_ecology]

Genome size was the dominant predictor of prophage burden, with rho=0.717, and residual confounding cannot be excluded despite genome-size stratification and partial correlations because larger genomes contain more genes of all types. [^prophage_ecology]

NCBI isolation_source metadata were sparse and inconsistently labeled. The 10 environmental categories collapse substantial within-category variation, and the other_unknown category contained 9,659 species (35%), limiting statistical power. [^prophage_ecology]

NMDC prophage-burden inference was indirect and assumed genus-level conservation of prophage content, an assumption that may fail for recently acquired or lost prophages. The approach had been validated for the PHB granule ecology project but had not been independently validated for prophage genes. [^prophage_ecology]

Module co-occurrence was tested in only 15 species, one per phylum, providing broad phylogenetic coverage but limited within-phylum replication. Head morphogenesis was testable in only 6 species because of sparsity, and the 200-permutation null model was considered adequate but not exhaustive for estimating Z-scores. [^prophage_ecology]

Only 28% of genomes had AlphaEarth environmental embeddings, producing a biased subsample toward clinically and environmentally well-sampled lineages. [^prophage_ecology]

## Slots Into

- [phage-defense-syndromes-and-arms-race](../concepts/phage-defense-syndromes-and-arms-race.md) — Module G anti-defense enrichment, depletion across environments, defense-island-like genomic placement, and the proposed host-phage arms-race signal feed the synthesis of bacterial defense and counter-defense syndromes. [^prophage_ecology]
- [environment-embedding-geography](../concepts/environment-embedding-geography.md) — AlphaEarth partial-correlation results and environmental module distributions provide evidence for embedding-derived ecological gradients after controlling for genome size. [^prophage_ecology]
- [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md) — The NMDC taxonomy bridge and cross-validation of pangenome-derived prophage burden against metagenomic abiotic correlations demonstrate a cross-collection integration pattern. [^prophage_ecology]
- [multi-omics-integration](../concepts/multi-omics-integration.md) — Gene-module annotations, environmental metadata, TerL sequences, contig co-localization, and NMDC metagenomic correlations are integrated to test prophage ecology across data modalities. [^prophage_ecology]

[^prophage_ecology]: [prophage ecology](../sources/prophage_ecology__REPORT.md)
