---
type: "Summary"
description: "Tiered census maps carbon-utilization knowledge gaps across 83 compounds."
doc_type: "short"
full_text: "sources/enigma_carbon_census_1__REPORT.md"
---
# ENIGMA Carbon Census — Tiered Knowledge Census of 83 Enrichment Compounds

## Overview

The ENIGMA Carbon Census integrates compound identity resolution, pathway and enzyme linkage, ENIGMA-isolate utilization predictions, GTDB strain placement, SSO field occurrence, and global environmental abundance for 83 enrichment compounds: 59 from SSO groundwater and 24 from necromass. All 83 compounds resolved to structures with InChIKeys via PubChem, 54 linked to KEGG, and 9 were callable under the project definition: 8 through an ENIGMA-isolate utilizer call and 1 through a Tier-1 measured RB-TnSeq carbon-source fitness experiment. The central result is a resource-defined knowledge gap: 74/83 compounds (89%) were organism-dark, meaning their genetic determinants of utilization were not linkable through the queried BERDL and curated resources. [src: enigma_carbon_census_1]

## Key Findings

### Coverage and the organism-dark set

The census funnel was 83 compounds → 83 structure-resolved → 54 KEGG-linked → 9 callable → 74 organism-dark. The dark fraction was similar by source: 53/59 groundwater compounds (90%) and 21/24 necromass compounds (88%) were dark, indicating that the observed gap tracks chemical class more closely than sampling source. The 74 dark compounds comprised 33 KEGG-linked compounds with no reaction in queried genomes, 29 fully orphan compounds with no KEGG link, 6 biosynthesis-known/catabolism-unknown compounds, and 6 compounds represented only by generic reactions. [src: enigma_carbon_census_1]

The 6 biosynthesis-known dark compounds were Tyramine, guanidineacetic acid, cinnamic acid, caffeic acid, palmitic acid, and farnesol; they are targets for external MIBiG and biosynthetic-literature consultation rather than equivalent to fully orphan compounds. The 29 fully orphan compounds are the hardest discovery targets and were disproportionately necromass-derived: 13/24 necromass compounds versus 16/59 groundwater compounds were fully orphan. [src: enigma_carbon_census_1]

### Chemical-class coverage and H1

The 8 ENIGMA-isolate-callable compounds were salicylic acid, 3-hydroxybenzoic acid, 4-hydroxybenzaldehyde, phthalic acid, terephthalic acid, Phenylethylamine, xanthine, and Abscisic acid. The additional callable compound, lauric acid, was callable only through measured fitness and had no ENIGMA-isolate utilizer rows. The isolate-callable set was concentrated in Shikimates/Phenylpropanoids: salicylic acid, 3-hydroxybenzoic acid, 4-hydroxybenzaldehyde, phthalic acid, and terephthalic acid; the other isolate calls were Phenylethylamine and xanthine in Alkaloids and Abscisic acid in Terpenoids. [src: enigma_carbon_census_1]

H1, the hypothesis of a coverage gradient by chemical class, was not formally supported. A chi-square test on the 8 ENIGMA-isolate-callable compounds gave χ²=5.07, p=0.53, df=6, using class counts of Shikimates 5/25, Alkaloids 2/26, Terpenoids 1/17, Fatty acids 0/10, Polyketides 0/2, AA/Peptides 0/2, and mixed 0/1. Adding measured-fitness lauric acid did not change the verdict. The pattern remains directionally useful for enrichment design but is underpowered and confounded with annotation coverage. [src: enigma_carbon_census_1]

Xanthine was mis-scored as carbon-catabolic because allowlisted reaction R02107, xanthine→urate, represents purine nitrogen acquisition rather than carbon catabolism. The effective carbon-callable set is therefore 8 rather than 9; R02107 was removed from the carbon allowlist, but committed tables still contain xanthine because they were not regenerated. [src: enigma_carbon_census_1]

### Co-occurrence, specialization, and H2

H2, the hypothesis of broad cross-module modularity, was not supported beyond a shared aromatic funnel. Among 8 ENIGMA-isolate-callable capacities across genomes carrying at least 1 capacity, the mean versatility was ~1.19, the median was 1, and the maximum was 4 capacities per genome. Using Haldane-corrected odds ratios (ORs) with 95% confidence intervals and Jaccard indices, within-aromatic pairs had median OR 1.12 and median Jaccard 0.026; within-other pairs had median OR 7.43 and median Jaccard values driven by near-zero counts; and cross-block pairs had median OR 2.28, with 4/15 confidence intervals entirely above 1 and median Jaccard approximately 0. [src: enigma_carbon_census_1]

The strongest cross-block signals involved Phenylethylamine and aromatic-funnel acids: 4-hydroxybenzaldehyde + Phenylethylamine had OR 2.84, 95% CI 1.49–5.40, q=0.035, n11=11; phthalic acid + Phenylethylamine had OR 3.37, 95% CI 1.46–7.75, q=0.071, n11=6. Their Jaccard remained approximately 0.04, and only 25 of 3109 genomes (0.8%) carried both an aromatic and a non-aromatic capacity. The result supports phylogenetic concentration rather than a portable, broadly co-assembled module set. [src: enigma_carbon_census_1]

The callable phenotype was specialist-dominated: 675 genomes carried exactly 1 of the 8 aromatic/alkaloid capacities, whereas 18 carried at least 3, with a maximum of 4. Generalist chassis were concentrated in Paraburkholderia (5), Burkholderia (4), and Hydrogenophaga (2), while high-versatility genera included Polaromonas, Alcaligenes, Burkholderia, Paraburkholderia, Comamonas, and Hydrogenophaga. Compound-specific conservation was observed within the called set, including approximately 100% 3-hydroxybenzoic-acid capacity in Castellaniella and Hylemonella, approximately 92–100% 4-hydroxybenzaldehyde capacity in Novosphingobium and Sphingobium, 100% phthalic-acid capacity in Paenarthrobacter, and 92% and 85% Comamonas capacity for 3-hydroxybenzoic acid and 4-hydroxybenzaldehyde, respectively. [src: enigma_carbon_census_1]

### Source tracking and H3

H3, the groundwater-versus-necromass source-tracking hypothesis, was untestable and confounded. Only 2 of the 8 ENIGMA-isolate-callable compounds were necromass-sourced—terephthalic acid and phthalic acid—and both were phthalate-class aromatics with Actinomycetota-heavy utilizers. Lauric acid was also necromass-sourced but had only a reference-bacterium measured-fitness call, no ENIGMA-isolate rows, and no field data. The project therefore reported an SSO field-occurrence atlas rather than a statistical source contrast. [src: enigma_carbon_census_1]

The SSO field atlas detected 62 of the implicated utilizer genera at genus resolution, with top field prevalences approximately 0.7–0.9; 3-hydroxybenzoic-acid utilizers reached 0.90 field prevalence. [src: enigma_carbon_census_1]

### Tiered isolate and phylogenetic deliverables

Deliverable (a) contained 569 ENIGMA-isolate utilizer prediction rows across the 8 ENIGMA-isolate-callable compounds. Counts were salicylic acid 129 strains, 3-hydroxybenzoic acid 127, 4-hydroxybenzaldehyde 125, phthalic acid 36, terephthalic acid 34, Phenylethylamine 28, xanthine 13, and Abscisic acid 2. Lauric acid had 0 ENIGMA-isolate rows because its call was based only on measured fitness in a reference bacterium. [src: enigma_carbon_census_1]

Deliverable (b) placed 494 strain records representing 359 distinct strains on GTDB taxonomy. The placements included 64 high-certainty records based on gene-complete Tier-2 pathways, 387 medium-certainty records based on Tier-2 pathways, and 43 medium-certainty records based on Tier-3 signature enzymes. Utilizers were concentrated in Pseudomonadota and Burkholderiales, with compound-specific contributions from Pseudomonadales and Sphingomonadales, including 47 Sphingomonadales strains for 4-hydroxybenzaldehyde. H4 was partially supported: it was strongly supported for the 8 ENIGMA-isolate-callable compounds and null for the other 75 compounds lacking isolate-level placement. [src: enigma_carbon_census_1]

Terephthalic acid had 34/34 high-certainty records, but this was a single-reaction-signature artifact rather than strong evidence of pathway completeness. Certainty is based on the raw number of carried signature reactions divided by required reactions, and is not directly comparable across compounds with different signature lengths. [src: enigma_carbon_census_1]

### Environmental abundance atlas

The global environmental atlas covered 86 implicated genera using 3825 taxonomy-bearing NMDC metagenomes and 302 Planet Microbe marine runs. In NMDC, 83/86 genera were detected in 1719 metagenomes, and 99% of samples were labeled through two independent ontology systems. Macro-environment counts were soil 2260, freshwater 723, periphyton 472, plant 119, and sediment 42. The local and global atlases measure organismal abundance or occurrence, not catabolic activity, because no environmental dataset measured the census compounds. [src: enigma_carbon_census_1]

Periphyton, representing freshwater biofilms such as epilithon, epipsammon, and epiphyton, surfaced a strong Burkholderiales/Comamonadaceae reservoir: listed genera reached approximately 96–97% prevalence with mean relative abundance approximately 0.005–0.009. Label-free abundance outliers peaked in periphyton and soil, including Nocardioides at 0.43 in epipsammon, Hydrogenophaga at 0.28 in epiphyton, and Mycobacterium at 0.22 in soil; outliers occurred for 34 genera in periphyton and 32 in soil. [src: enigma_carbon_census_1]

The marine arm was primarily a negative biome contrast. All 68/68 listed genera showed positive abundance across 302 Planet Microbe runs, but terrestrial/freshwater genera generally occurred at approximately 1e-3 to 1e-4 abundance in open ocean. Alteromonas was a genuine marine member, occurring at 0.048 in 240/302 runs with prevalence 0.79; Pseudomonas and Sphingomonas had abundances 0.011 and 0.0063, respectively. [src: enigma_carbon_census_1]

### Physicochemistry and annotation ceiling

With only 9 callable compounds, physicochemical comparisons were directional and underpowered. Callable compounds had median Complexity 133 versus 207 for dark compounds, p=0.034; median MolecularWeight 152 versus 179, p=0.066; and median HeavyAtomCount 11 versus 13, p=0.057. Callable compounds also showed directionally higher polarity, with TPSA 57 versus 41 and hydrogen-bond donors 2 versus 1. The result may reflect an annotation-coverage ceiling as much as biological bioavailability: simple, common, pollutant-adjacent aromatics are also the compounds most likely to be represented in KEGG, ModelSEED, and genome-depot annotations. [src: enigma_carbon_census_1]

## Caveats and Limitations

“Organism-dark” means not linkable through the queried BERDL and curated resources, not unknown to science. Class-level catabolic literature exists for compounds including monoterpenes and nicotine, while the project’s zero literature rescues resulted from a shallow PubMed-title-only screen. A PaperBLAST or abstract-level search could reclassify part of the dark set. [src: enigma_carbon_census_1]

The dark fraction depends on the catabolic-direction filter: the 8 ENIGMA-isolate calls used a genome-prevalence-<10% signature-reaction filter retaining reactions that were catabolic according to KEGG degradation-map membership or a 3-reaction curated allowlist. A different filter could change the callable/dark boundary. Lauric acid was independently callable through measured fitness and was not subject to this filter. [src: enigma_carbon_census_1]

Soil-versus-freshwater enrichment statistics were exploratory and not calibrated. Treating each metagenome as independent in rank tests over compositional, zero-inflated relative abundances can inflate significance; all 83 genera reached q<0.05, with many q values near 1e-70. Direction and rank were considered more trustworthy than the p-values, and label-free outlier discovery was the more defensible signal. [src: enigma_carbon_census_1]

The environmental atlas is a biome-occupancy proxy, not evidence of compound degradation or activity. The H3 contrast was genuinely untestable because only 2 necromass compounds were ENIGMA-isolate-callable and both were phthalate-class aromatics. The marine arm was small and gene-blind, with 302 runs and presence/abundance data only. [src: enigma_carbon_census_1]

The callable-versus-dark physicochemical analysis was descriptive rather than calibrated inference because n=9 callable compounds were available and the Mann–Whitney p-values were uncorrected. Xanthine remains a category error in the carbon census until downstream tables are regenerated after excluding R02107. [src: enigma_carbon_census_1]

The project also identified data-pipeline requirements: NMDC and Planet Microbe inputs were species-level, so genus abundance required species-to-genus aggregation; the NMDC denominator was 3825 taxonomy-bearing covstats files rather than approximately 6700 sample-file-lookup rows; and sample-level environment labels from biosample_set provided 99% coverage across two ontologies, compared with approximately 13% from study-table GOLD labels. [src: enigma_carbon_census_1]

## Recommended Next Analyses

Wet-lab enrichment should prioritize the 74 dark compounds by bucket, beginning with the 29 fully orphan compounds, especially necromass-heavy alkaloids and terpenoids. The 6 biosynthesis-known compounds should first receive MIBiG or biosynthetic-literature consultation. Targeted PaperBLAST and PubMed/abstract mining could promote dark compounds to callable status, while a study-aware mixed model or sample-level permutation would provide more defensible soil-versus-freshwater contrasts. Periphyton-sited enrichment is supported as a practical strategy for accessing the observed Comamonadaceae/Burkholderiales reservoir. [src: enigma_carbon_census_1]

## Slots Into

- [[concepts/pangenome-integration]] — the census links pathway and enzyme annotations across 3109 genomes to ENIGMA-isolate utilizer predictions and GTDB strain placements. [src: enigma_carbon_census_1]
- [[concepts/cross-tenant-data-bridging]] — the project bridges PubChem, KEGG, ModelSEED, Fitness Browser, ENIGMA genome-depot, GTDB, SSO, NMDC, and Planet Microbe resources into a tiered compound-to-environment workflow. [src: enigma_carbon_census_1]
- [[concepts/ecotype-environment-gene-content]] — the environmental atlas compares implicated utilizer genera across soil, freshwater, periphyton, sediment, plant, and marine environments while explicitly separating abundance from catabolic activity. [src: enigma_carbon_census_1]
- [[concepts/metabolic-model-gapfilling]] — the 74 organism-dark compounds, including 33 KEGG-linked/no-reaction cases and 29 fully orphan cases, define pathway-linkage and enrichment targets for metabolic knowledge expansion. [src: enigma_carbon_census_1]
- [[concepts/multi-omics-integration]] — the census combines chemical identity, reaction and genome annotations, measured fitness, taxonomy, field occurrence, and metagenomic abundance into a tiered evidence framework. [src: enigma_carbon_census_1]
