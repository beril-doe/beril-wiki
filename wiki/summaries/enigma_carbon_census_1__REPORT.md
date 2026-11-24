---
type: "Summary"
description: "Summary of the project ENIGMA Carbon Census — A Tiered Knowledge Census of 83 Enrichment Compounds."
doc_type: "short"
full_text: "sources/enigma_carbon_census_1__REPORT.md"
---
# ENIGMA Carbon Census — A Tiered Knowledge Census of 83 Enrichment Compounds

Summary of the project ENIGMA Carbon Census — A Tiered Knowledge Census of 83 Enrichment Compounds.

## Key Findings

### Callability and darkness

The census holds 83 compounds, 59 from SSO groundwater and 24 from necromass. All 83 resolved to structures through PubChem InChIKeys, and 54 linked to KEGG. Only 9 are "callable". [src: enigma_carbon_census_1] Eight of these are callable through at least one ENIGMA-isolate prediction with a catabolic, compound-degrading reaction in a genome. [src: enigma_carbon_census_1] The ninth is lauric acid. It qualifies only on measured RB-TnSeq (random barcode transposon sequencing) fitness in a reference bacterium, not an ENIGMA isolate. It has no ENIGMA-isolate prediction rows, and the ENIGMA-isolate deliverable is unchanged. [src: enigma_carbon_census_1]

The post-I1 organism-dark breakdown covers 74 compounds. It includes 6 biosynthesis-known/catabolism-unknown compounds: tyramine, guanidineacetic acid, cinnamic acid, caffeic acid, palmitic acid and farnesol. These have biosynthetic-direction signatures but no catabolic call. [src: enigma_carbon_census_1] All callable evidence is catabolic-direction by construction of the NB03 filter. That evidence comprises 846 Tier-2 pathway calls and 102 Tier-3 signature genome-compound calls. Biosynthetic-only signatures are excluded and land in the dark set. [src: enigma_carbon_census_1]

Darkness means a lack of resources, not absence from science. Class-level catabolic literature exists for several of these compounds, such as monoterpenes and nicotine. [src: enigma_carbon_census_1] The dark list is stratified by reason and chemical class. It separates candidate discovery targets from the small characterize-known set, and the report expects a literature/PaperBLAST pass to reclassify some dark compounds. [src: enigma_carbon_census_1]

### Chemical class (H1)

The dark set is dominated by the predicted classes: Alkaloids, Shikimates/Phenylpropanoids, Terpenoids and Fatty acids. [src: enigma_carbon_census_1] The callable compounds are mostly pollutant-adjacent aromatics. Salicylic acid, 3-hydroxybenzoic acid, 4-hydroxybenzaldehyde, phthalic acid and terephthalic acid are Shikimates/Phenylpropanoids. The others are phenylethylamine and xanthine (Alkaloids), abscisic acid (a Terpenoid, with a single 2-strain call) and lauric acid (a Fatty acid). [src: enigma_carbon_census_1] ENIGMA-isolate callable coverage by class is Shikimates 5/25, Terpenoids 1/17 and Polyketides 0/2. [src: enigma_carbon_census_1] Adding measured-fitness lauric acid (Fatty acids 1/10) does not change the verdict. [src: enigma_carbon_census_1] The report's verdict is that H1 is not formally supported. The per-class Tier-0 list remains a descriptive enrichment-design deliverable. [src: enigma_carbon_census_1] The concentration in aromatics and phthalates is unaffected by the xanthine caveat. It directionally matches curated biodegradation knowledge and KEGG coverage. [src: enigma_carbon_census_1]

### Co-occurrence and phylogeny

NB05 first reported co-occurrence with the φ coefficient. φ compresses toward zero for rare capacities, which are present in tens to hundreds of 3109 genomes, and so can hide real multiplicative enrichment. [src: enigma_carbon_census_1] With odds ratios (OR), within-aromatic pairs have median OR 1.12, 3/10 pairs with the confidence interval (CI) entirely above 1, and median Jaccard 0.026. [src: enigma_carbon_census_1] Cross-block pairs from distinct lower pathways have median OR 2.28, with 4/15 CI above 1 and median Jaccard ≈ 0. [src: enigma_carbon_census_1] The phenylethylamine link to aromatic acids is mechanistically coherent. Phenylethylamine is deaminated to phenylacetate and then routed through the paa/phenylacetyl-CoA route. [src: enigma_carbon_census_1] Only 25 of 3109 genomes (0.8%) carry both an aromatic and a non-aromatic capacity. [src: enigma_carbon_census_1]

What is supported is phylogenetic concentration. Burkholderiales dominate utilizer counts, and the high-versatility genera cluster in the order Polaromonas, Alcaligenes, Burkholderia, Paraburkholderia, Comamonas, Hydrogenophaga. [src: enigma_carbon_census_1] Among genomes carrying at least one of the 8 aromatic/alkaloid capacities, 675 are specialists with exactly 1 capacity. [src: enigma_carbon_census_1] Generalist chassis concentrate in Paraburkholderia (5) and the wider Burkholderiaceae. The report reads this as versatility being a clade trait, not a widely portable module. [src: enigma_carbon_census_1] Per-clade conservation shows compound-specific clade specialization, not a shared generalist toolkit. [src: enigma_carbon_census_1] Those conservation fractions are denominated over depot genomes that already carry some catabolic call. They describe within-called-set specialization, not absolute prevalence. [src: enigma_carbon_census_1] For example, Comamonas carries 3-hydroxybenzoate capacity at 92% of such genomes. [src: enigma_carbon_census_1]

### Source and chemistry

Lauric acid is necromass-sourced but has no ENIGMA-isolate utilizers or field data, so it adds nothing to the source contrast. [src: enigma_carbon_census_1] Groundwater and necromass compounds show no physicochemical separation (all contrasts p>0.14). [src: enigma_carbon_census_1] Callable compounds are directionally smaller than dark ones, with median MolecularWeight 152 versus 179 (p=0.066). They have directionally higher H-bond donors (2 versus 1). [src: enigma_carbon_census_1] With only n=9 callable compounds, this comparison is directional, not inferential. It uses Mann–Whitney tests reported as direction plus uncorrected p. [src: enigma_carbon_census_1]

### Isolate predictions and placements (H4)

The report considers H4 partially supported: strongly for the 8 ENIGMA-isolate-callable compounds, and null for the other 75. [src: enigma_carbon_census_1] Strain counts in the utilizer prediction set are 127 for 3-hydroxybenzoic acid, 34 for terephthalic acid and 13 for xanthine. [src: enigma_carbon_census_1] The "34 all high-certainty" for terephthalic acid is a single-reaction-signature artifact, not a strength. [src: enigma_carbon_census_1] GTDB placements include 64 high-certainty gene-complete-pathway Tier 2 placements and 43 medium-certainty Tier 3 signature-enzyme placements. [src: enigma_carbon_census_1] Across the genome chassis, capacity breadth is led by 3-hydroxybenzoic acid (296 genomes, 53 genera). Abscisic acid is a 2-genome edge case. [src: enigma_carbon_census_1]

### Field and global atlases

The SSO field atlas observes 62 implicated utilizer genera at genus resolution. Top aromatic-utilizer field prevalences are ~0.7–0.9, and 3-hydroxybenzoic-acid utilizers reach 0.90. [src: enigma_carbon_census_1] The global atlas covers 86 implicated genera. [src: enigma_carbon_census_1] It is a biome-abundance proxy, not catabolic activity. Genus abundance indicates where the organisms live, not where the compounds are degraded. [src: enigma_carbon_census_1] The NMDC atlas detects 83/86 genera in 1719 metagenomes. Its macro-environments include 723 freshwater and 119 plant metagenomes. [src: enigma_carbon_census_1] The soil-versus-freshwater contrast is exploratory. Terriglobus is soil-enriched (log2 +5.29) and Cellvibrio is freshwater-enriched (log2 −2.19). [src: enigma_carbon_census_1] Periphyton is a strong reservoir for Rhizobacter, Variovorax, Polaromonas, Methylibium, Sphingomonas and Hydrogenophaga, at ~96–97% prevalence. [src: enigma_carbon_census_1] The marine atlas is mostly a negative biome contrast, with terrestrial and freshwater genera at ~1e-3 to 1e-4 in open ocean. Cosmopolitan Pseudomonas has abundance 0.011. [src: enigma_carbon_census_1]

## Key Findings: H1 (coverage gradient by chemical class) — not formally supported …

This part of the report shows that most census compounds are dark at the organism level. Only 9 of 83 are callable, and the class-gradient and modularity hypotheses were not formally supported. [src: enigma_carbon_census_1]

### Callable and dark compounds

The census has 83 compounds (59 from SSO groundwater and 24 from necromass). All 83 resolved to structures through PubChem InChIKeys, and 54 linked to KEGG. [src: enigma_carbon_census_1] "Callable" means an ENIGMA-isolate utilizer call or a Tier-1 measured carbon-source fitness experiment from random barcode transposon sequencing (RB-TnSeq). [src: enigma_carbon_census_1] Eight compounds are callable through at least one ENIGMA-isolate prediction with a catabolic, compound-degrading reaction in a genome. [src: enigma_carbon_census_1] The ninth, lauric acid, is callable only on measured fitness. It has a Tier-1 carbon-source growth experiment in the Fitness Browser, confirmed by an InChIKey re-match. [src: enigma_carbon_census_1] Its organism is a reference bacterium, not an ENIGMA isolate, so the ENIGMA-isolate deliverable does not change. [src: enigma_carbon_census_1]

The other 74 of 83 (89%) are organism-dark. Their genetic determinants are not linkable through the queried the KBase Data Lakehouse and curated resources. [src: enigma_carbon_census_1] See [[concepts/resource-darkness-of-compound-catabolism]]. The report calls this resource-darkness, not absence from science. Class-level catabolic literature exists for compounds such as monoterpenes and nicotine. [src: enigma_carbon_census_1] The literature-rescue channel (NB02b) returned zero only because it used a shallow PubMed-title screen, which the report calls a method floor. [src: enigma_carbon_census_1] The report expects a literature/PaperBLAST pass to reclassify some dark compounds. It stratifies the dark list by reason and chemical class to separate candidate discovery targets from a small characterize-known set. [src: enigma_carbon_census_1]

The post-I1 dark breakdown (74 compounds) is below. [src: enigma_carbon_census_1]

| Bucket | Compounds |
|---|---|
| KEGG-linked, no reaction in genomes | 33 |
| Fully orphan (no KEGG) | 29 |
| Biosynthesis-known, catabolism-unknown | 6 |
| Only generic reactions | 6 |

Alkaloids, Shikimates/Phenylpropanoids, Terpenoids and Fatty acids dominate the dark set, as predicted. [src: enigma_carbon_census_1] The dark fraction is nearly identical across sources: groundwater 53/59 = 90% and necromass 21/24 = 88%. The report reads this as a chemical-class property, not a sampling-source artifact. [src: enigma_carbon_census_1] See [[concepts/confounding-of-compound-source-with-chemical-class]].

### What the callable compounds are

The callables are mostly pollutant-adjacent aromatics. The Shikimates/Phenylpropanoids are salicylic acid, 3-hydroxybenzoic acid, 4-hydroxybenzaldehyde, phthalic acid and terephthalic acid. [src: enigma_carbon_census_1] The Alkaloids are Phenylethylamine and xanthine. [src: enigma_carbon_census_1] Abscisic acid is a Terpenoid with a single 2-strain call. [src: enigma_carbon_census_1]

Xanthine is mis-scored as carbon-catabolic. Its allowlisted reaction R02107 (xanthine to urate, xanthine oxidase) is purine-pathway nitrogen acquisition, so the carbon-callable set is effectively 8, not 9. [src: enigma_carbon_census_1] See [[concepts/catabolic-direction-filtering-and-mis-scored-carbon-calls]]. The aromatic/phthalate concentration is unaffected. It directionally matches curated biodegradation knowledge and KEGG coverage. [src: enigma_carbon_census_1]

### Class gradient (H1): not supported

The pre-registered null of uniform coverage across classes is not rejected. A χ² test on the 8 enigma_isolate_call callables gives χ²=5.07, p=0.53 (df=6). [src: enigma_carbon_census_1] Coverage by class:

| Class | Callable |
|---|---|
| Shikimates | 5/25 [src: enigma_carbon_census_1] |
| Alkaloids | 2/26 [src: enigma_carbon_census_1] |
| Terpenoids | 1/17 [src: enigma_carbon_census_1] |
| Fatty acids | 0/10 [src: enigma_carbon_census_1] |
| Polyketides | 0/2 [src: enigma_carbon_census_1] |
| AA/Peptides | 0/2 [src: enigma_carbon_census_1] |
| mixed | 0/1 [src: enigma_carbon_census_1] |

Adding the measured-fitness lauric acid (Fatty acids 1/10) does not change the verdict. [src: enigma_carbon_census_1] With about 9 callables across 83 compounds, the design is underpowered. The directional pattern is also confounded with annotation coverage (which classes KEGG/ModelSEED/genome_depot annotate) rather than a clean degradability gradient. [src: enigma_carbon_census_1] See [[concepts/annotation-coverage-bias-in-chemical-class-callability]]. The report's verdict is that H1 is not formally supported. The per-class Tier-0 list remains a descriptive enrichment-design deliverable. [src: enigma_carbon_census_1]

### Versatility and co-occurrence

Among genomes carrying at least one of the 8 enigma_isolate_call capacities, versatility is right-skewed. The mean is about 1.19, the median is 1, and the maximum is 4 capacities per genome. [src: enigma_carbon_census_1]

NB05 first used the φ coefficient. φ compresses toward zero for rare capacities, most of which occur in tens to hundreds of 3109 genomes, and this can hide multiplicative enrichment. [src: enigma_carbon_census_1] NB05b therefore recomputed Haldane-corrected odds ratios (OR) with 95% confidence intervals (CI) and Jaccard indices from saved 2×2 counts, with no Spark re-run. [src: enigma_carbon_census_1] See [[concepts/co-occurrence-and-modularity-of-catabolic-capacities-across-genomes]].

- Within-aromatic pairs: median OR 1.12, 3/10 pairs with CI entirely > 1, median Jaccard 0.026. [src: enigma_carbon_census_1]
- Within-other pairs: median OR 7.43 (1/3 positive), driven by Haldane correction on near-zero counts. [src: enigma_carbon_census_1]
- Cross-block pairs (distinct lower pathways), the real modularity test: median OR 2.28, 4/15 with CI > 1, median Jaccard ≈ 0. [src: enigma_carbon_census_1]

Two pairs stand out. 4-hydroxybenzaldehyde with phenylethylamine has OR 2.84 (95% CI 1.49–5.40, q=0.035, n11=11). [src: enigma_carbon_census_1] Phthalic acid with phenylethylamine has OR 3.37 (95% CI 1.46–7.75, q=0.071, n11=6). [src: enigma_carbon_census_1] The report calls this coherent, because phenylethylamine is an aromatic-derived substrate. It is deaminated to phenylacetate and then routed through the paa/phenylacetyl-CoA route. [src: enigma_carbon_census_1] Even for these pairs Jaccard stays about 0.04, so only about 4% of genomes with either capacity carry both. [src: enigma_carbon_census_1] Only 25 of 3109 genomes (0.8%) carry both an aromatic and a non-aromatic capacity. [src: enigma_carbon_census_1]

The verdict is no broad cross-module modularity. The one positive signal lies within the broad aromatic-catabolism phenotype, not in co-assembly of mechanistically distinct modules. [src: enigma_carbon_census_1]

### Phylogenetic concentration

Phylogenetic concentration is supported. Burkholderiales dominate utilizer counts. High-versatility genera cluster in the order Polaromonas, Alcaligenes, Burkholderia, Paraburkholderia, Comamonas, Hydrogenophaga. [src: enigma_carbon_census_1] See [[entities/burkholderiales]] and [[concepts/taxonomic-distribution-of-aromatic-compound-catabolism]].

## Key Findings: Deliverable (c), global arm: a cross-environment abundance atlas for the 86 …

This part of the report shows that source tracking (groundwater versus necromass) cannot be tested, because source is confounded with chemical class. [src: enigma_carbon_census_1] Instead of a confounded result, NB07 was reframed as an SSO field-occurrence atlas. [src: enigma_carbon_census_1] The report also gives ENIGMA isolate deliverables that bear on H4, and a separate global abundance atlas of implicated utilizer genera. [src: enigma_carbon_census_1]

### Why source tracking is untestable

Of the 8 ENIGMA-isolate-callable compounds, only 2 are necromass-sourced: terephthalic and phthalic acid. Both are phthalate-class aromatics with Actinomycetota-heavy utilizers. [src: enigma_carbon_census_1] Lauric acid, the 9th callable compound, is also necromass-sourced. It has no ENIGMA-isolate utilizers and no field data, so it adds nothing to the source contrast. [src: enigma_carbon_census_1] It qualifies as callable only through measured RB-TnSeq (random barcode transposon sequencing) fitness in a reference bacterium. [src: enigma_carbon_census_1] The report concludes that source is inseparable from chemical class at n=2, so no honest statistical contrast exists. [src: enigma_carbon_census_1] See [[concepts/confounding-of-compound-source-with-chemical-class]].

### Reframed field atlas (NB07)

NB07 became an SSO field-occurrence atlas built from Zhou Lab 16S `enigma_coral` bricks. [src: enigma_carbon_census_1] The atlas observes 62 implicated utilizer genera in the SSO field at genus resolution. Top field prevalences are about 0.7–0.9 for aromatic utilizers, and 3-hydroxybenzoic-acid utilizers reach 0.90. [src: enigma_carbon_census_1]

### ENIGMA isolate deliverables and H4

The report calls H4 (tier-stratified, phylogenetically concentrated isolate predictions) partially supported: strongly for the 8 ENIGMA-isolate-callable compounds. [src: enigma_carbon_census_1] H4 is null for the other 75 compounds, which are Tier 0 with no isolate-level placement. [src: enigma_carbon_census_1] Lauric acid sits outside both arms. [src: enigma_carbon_census_1]

Deliverable (a) is 569 ENIGMA-isolate utilizer prediction rows across the 8 callable compounds. Lauric acid has none, because it is callable only on measured fitness. [src: enigma_carbon_census_1] Aromatics carry most of the strains:

| Compound | Predicted strains |
|---|---|
| salicylic acid | 129 [src: enigma_carbon_census_1] |
| 3-hydroxybenzoic acid | 127 [src: enigma_carbon_census_1] |
| 4-hydroxybenzaldehyde | 125 [src: enigma_carbon_census_1] |
| phthalic acid | 36 [src: enigma_carbon_census_1] |
| terephthalic acid | 34 [src: enigma_carbon_census_1] |
| Phenylethylamine | 28 [src: enigma_carbon_census_1] |
| xanthine | 13 [src: enigma_carbon_census_1] |
| Abscisic acid | 2 [src: enigma_carbon_census_1] |

The report calls the "all high-certainty" status of terephthalic acid a single-reaction-signature artifact, not a strength. [src: enigma_carbon_census_1]

Deliverable (b) is 494 placements on the GTDB taxonomy, covering 359 distinct strains. Each carries a tier × certainty score. [src: enigma_carbon_census_1] There are 64 high-certainty placements (gene-complete pathway, Tier 2) [src: enigma_carbon_census_1], 387 medium placements (Tier 2 pathway) [src: enigma_carbon_census_1] and 43 medium placements (Tier 3 signature enzyme). [src: enigma_carbon_census_1] Utilizers concentrate in Pseudomonadota/Burkholderiales. Pseudomonadales and Sphingomonadales add to specific compounds, for example 47 Sphingomonadales strains for 4-hydroxybenzaldehyde. [src: enigma_carbon_census_1] The work used notebooks 04_enigma_utilizers and 06_phylo_maps. [src: enigma_carbon_census_1]

### Global abundance atlas (deliverable c)

The global arm is an additional atlas, beyond the local SSO field atlas, and covers 86 implicated genera. [src: enigma_carbon_census_1] It places them across terrestrial/freshwater NMDC environments using kbase.nmdc_arkin in the KBase Data Lakehouse. It uses marine Planet Microbe data as a contrast. [src: enigma_carbon_census_1] This is a biome-abundance proxy, not catabolic activity. No environmental dataset measures the census compounds, so abundance shows where the organisms live, not where the compounds are degraded. [src: enigma_carbon_census_1] See [[concepts/biome-abundance-atlases-as-a-proxy-for-catabolic-potential]].

**NMDC scale.** The atlas has 3825 taxonomy-bearing metagenomes, with the denominator defined as covstats files with taxonomy. [src: enigma_carbon_census_1] 83 of the 86 genera are detected in 1719 metagenomes. [src: enigma_carbon_census_1] 99% of samples are labeled, using two independent ontologies: the ENVO (Environment Ontology) MIxS triad and the GOLD ecosystem path. [src: enigma_carbon_census_1] The macro-environment counts are soil 2260 [src: enigma_carbon_census_1], freshwater 723 [src: enigma_carbon_census_1], periphyton 472 [src: enigma_carbon_census_1], plant 119 [src: enigma_carbon_census_1] and sediment 42. [src: enigma_carbon_census_1]

**Soil versus freshwater.** This contrast is labeled exploratory. [src: enigma_carbon_census_1] It recovers textbook biogeography. Soil-enriched genera are Mycobacterium (log2 +5.09) [src: enigma_carbon_census_1], Terriglobus (+5.29) [src: enigma_carbon_census_1] and Nitrobacter (+4.79). [src: enigma_carbon_census_1] Afipia, Streptomyces, Nocardioides and Mesorhizobium are also soil-enriched. [src: enigma_carbon_census_1] Freshwater-enriched genera include Cellvibrio (log2 −2.19) [src: enigma_carbon_census_1], Curvibacter, Rhodoferax, Comamonas and Acidovorax. [src: enigma_carbon_census_1]

**Periphyton and outliers.** Periphyton is freshwater biofilm (epilithon/epipsammon/epiphyton). It is a strong reservoir for Rhizobacter, Variovorax, Polaromonas, Methylibium, Sphingomonas and Hydrogenophaga, at ~96–97% prevalence and mean relative abundance ~0.005–0.009. [src: enigma_carbon_census_1] The report calls label-free outlier discovery its most defensible signal, robust to label noise. [src: enigma_carbon_census_1] The top genus×sample spikes are Nocardioides at 0.43 in epipsammon [src: enigma_carbon_census_1], Hydrogenophaga at 0.28 in epiphyton [src: enigma_carbon_census_1] and Mycobacterium at 0.22 in soil. [src: enigma_carbon_census_1] Outliers peak in periphyton (34 genera) and soil (32). [src: enigma_carbon_census_1]

## Key Findings: The callable phenotype is a specialist clade trait, not a portable …

### Marine arm of the global atlas

The global atlas is implemented in notebook 07b_environmental_atlas_global. [src: enigma_carbon_census_1] In [[entities/planet-microbe]]'s 302 marine runs, 68/68 listed genera show positive abundance. [src: enigma_carbon_census_1] The report calls marine "mostly a negative biome contrast", with terrestrial/freshwater genera at ~1e-3 to 1e-4 in open ocean. [src: enigma_carbon_census_1] Genuine marine members are the exception. Alteromonas has abundance 0.048 in 240/302 runs and prevalence 0.79. [src: enigma_carbon_census_1] Cosmopolitan Pseudomonas has abundance 0.011 [src: enigma_carbon_census_1], and Sphingomonas 0.0063. [src: enigma_carbon_census_1] See [[concepts/biome-abundance-atlases-as-a-proxy-for-catabolic-potential]].

### Physicochemistry of callable versus dark compounds

NB09 Part 1 resolves PubChem physicochemical descriptors for all 83 census compounds and contrasts callable with dark compounds. [src: enigma_carbon_census_1] The analysis sits in notebook 09_deepening. [src: enigma_carbon_census_1] Callable compounds are smaller and structurally simpler than dark ones. The tests are Mann–Whitney with uncorrected p values, reported as directions. [src: enigma_carbon_census_1]

| Descriptor (median) | Callable | Dark | p |
|---|---|---|---|
| Complexity | 133 | 207 | 0.034 [src: enigma_carbon_census_1] |
| MolecularWeight | 152 | 179 | 0.066 [src: enigma_carbon_census_1] |
| HeavyAtomCount | 11 | 13 | 0.057 [src: enigma_carbon_census_1] |

Callable compounds are directionally more polar, with TPSA 57 versus 41 [src: enigma_carbon_census_1] and H-bond donors 2 versus 1. [src: enigma_carbon_census_1]

The report reads this as at least as much an annotation-coverage ceiling as a biological-bioavailability effect. KEGG, ModelSEED and genome_depot annotate simple, common, pollutant-adjacent aromatics. [src: enigma_carbon_census_1] See [[concepts/annotation-coverage-bias-in-chemical-class-callability]]. Groundwater and necromass compounds show no physicochemical separation (all contrasts p>0.14). [src: enigma_carbon_census_1]

### Genome chassis: specialists dominate

Among genomes carrying ≥1 of the 8 aromatic/alkaloid capacities, 675 are specialists with exactly 1 capacity. [src: enigma_carbon_census_1] Only 18 are generalists with ≥3 capacities, and the maximum is 4. [src: enigma_carbon_census_1] Generalist chassis concentrate in Paraburkholderia (5) [src: enigma_carbon_census_1], Burkholderia (4) [src: enigma_carbon_census_1] and Hydrogenophaga (2), plus scattered Burkholderiaceae. [src: enigma_carbon_census_1] This is the same clade that dominates the versatility ranking. The report concludes that versatility is a clade trait, not a widely portable module. [src: enigma_carbon_census_1] See [[entities/burkholderiales]].

Capacity breadth is led by 3-hydroxybenzoic acid (296 genomes, 53 genera) [src: enigma_carbon_census_1] and salicylic acid (197 genomes, 28 genera). [src: enigma_carbon_census_1] Abscisic acid is a 2-genome edge case. [src: enigma_carbon_census_1]

### Per-clade conservation

Per-clade conservation shows compound-specific clade specialization, not a shared generalist toolkit. [src: enigma_carbon_census_1] The fractions are denominated over depot genomes that already carry some catabolic call. They describe within-called-set specialization, not absolute genus prevalence. [src: enigma_carbon_census_1] Examples:

- Castellaniella and Hylemonella carry 3-hydroxybenzoic-acid capacity in ~100% of such genomes. [src: enigma_carbon_census_1]
- Novosphingobium/Sphingobium carry 4-hydroxybenzaldehyde capacity at ~92–100%. [src: enigma_carbon_census_1]
- Paenarthrobacter carries phthalic-acid capacity at 100%. [src: enigma_carbon_census_1]
- Comamonas carries 3-hydroxybenzoate capacity at 92% [src: enigma_carbon_census_1] and 4-hydroxybenzaldehyde capacity at 85%. [src: enigma_carbon_census_1]

### Catabolic direction and the dark set

All callable evidence is catabolic-direction by construction of the NB03 filter. It yields 846 Tier-2 pathway [src: enigma_carbon_census_1] and 102 Tier-3 signature genome-compound calls. [src: enigma_carbon_census_1] Biosynthetic-only signatures are excluded and land in the dark set. [src: enigma_carbon_census_1] See [[concepts/catabolic-direction-filtering-and-mis-scored-carbon-calls]].

### Taxonomy of the 74 organism-dark compounds

NB09 Part 4 partitions the 74 organism-dark compounds into four buckets. [src: enigma_carbon_census_1]

- 33 are KEGG-linked but have no reaction in any queried genome. [src: enigma_carbon_census_1]
- 29 are fully orphan. [src: enigma_carbon_census_1]
- 6 are biosynthesis-known and catabolism-unknown. [src: enigma_carbon_census_1]
- 6 have only generic reactions. [src: enigma_carbon_census_1]

The six biosynthesis-known compounds are tyramine, guanidineacetic acid, cinnamic acid, caffeic acid, palmitic acid and farnesol. They have biosynthetic-direction signatures but no catabolic call. [src: enigma_carbon_census_1] The report recommends an external MIBiG/biosynthetic-literature consultation before discovery enrichment. MIBiG was not queried in the KBase Data Lakehouse. [src: enigma_carbon_census_1] The 29 orphan compounds have no KEGG link and are the hardest discovery targets. They skew toward necromass: 13/24 necromass compounds are orphan, against 16/59 groundwater compounds. [src: enigma_carbon_census_1] See [[concepts/resource-darkness-of-compound-catabolism]].

## Discoveries; Performance Notes; Results

This part of the report gives the census's headline counts, the callable-compound table, and the data-handling lessons from the NMDC and Planet Microbe work. The census is mostly dark: darkness follows chemical class, and callable capacity is a specialist, clade-level trait. [src: enigma_carbon_census_1]

### Headline counts

The census covers 83 compounds, all structure-resolved by InChIKey, and 54 of them are KEGG-linked. [src: enigma_carbon_census_1] Nine compounds are callable: 8 by enigma_isolate_call and 1 by measured_fitness. [src: enigma_carbon_census_1] The report states the census is ~89% organism-dark, with 74/83 compounds lacking an isolate utilizer call. [src: enigma_carbon_census_1] The table places 359 utilizer strains, 64 of them high-certainty, and 62 utilizer genera in the SSO field. [src: enigma_carbon_census_1] In the global atlas, 83/86 implicated genera are detected in NMDC across 1719 metagenomes. [src: enigma_carbon_census_1] Planet Microbe gives 302 runs, with 68 of 68 genera positive. [src: enigma_carbon_census_1]

### What predicts darkness and capacity

Darkness follows chemical class, not sampling source. Alkaloids and terpenoids are dark and aromatics are callable. Groundwater compounds are 90% dark and necromass compounds 88%. [src: enigma_carbon_census_1]

Callable capacity is concentrated in Burkholderiales and is a specialist trait. There are 675 single-capacity genomes against 18 generalists with ≥3 capacities. [src: enigma_carbon_census_1]

Cross-module co-occurrence is near zero in share terms. Jaccard is ≈ 0, and only 25/3109 genomes carry both an aromatic and a non-aromatic capacity. [src: enigma_carbon_census_1] A Haldane odds ratio (OR) finds a modest phenylethylamine×aromatic enrichment of OR ≈ 2.8–3.4. The report calls this itself aromatic-derived, so versatility is a clade trait and not a portable module set. [src: enigma_carbon_census_1]

The report finds a directional association between callability and structural simplicity. The n=9 callable compounds have median Complexity 133 against 207 for dark compounds (Mann–Whitney p=0.034, uncorrected). [src: enigma_carbon_census_1] The report attributes at least part of this to an annotation-coverage ceiling, since curated catabolism resources cover simple pollutant-adjacent aromatics. [src: enigma_carbon_census_1]

A periphyton (freshwater-biofilm) class from the Environment Ontology (ENVO) and GOLD, separated from bulk freshwater, shows a Comamonadaceae/Burkholderiales reservoir at ~97% prevalence. The report says this is relevant to siting SSO enrichments. [src: enigma_carbon_census_1]

### Callable-compound table

The table lists, per compound, origin, class, tier, strains, high-certainty strains, genera, field genera and top field prevalence. [src: enigma_carbon_census_1]

| Compound | Origin | Class | Tier | Strains | High-cert. | Genera | Field genera | Top prevalence |
|---|---|---|---|---|---|---|---|---|
| salicylic acid [src: enigma_carbon_census_1] | groundwater | Shikimates/Phenylpropanoids | T2_3_reaction | 129 | 2 | 24 | 20 | 0.86 |
| 3-hydroxybenzoic acid [src: enigma_carbon_census_1] | groundwater | Shikimates/Phenylpropanoids | T2_3_reaction | 127 | 18 | 42 | 33 | 0.90 |
| 4-hydroxybenzaldehyde [src: enigma_carbon_census_1] | groundwater | Shikimates/Phenylpropanoids | T2_3_reaction | 125 | 10 | 34 | 25 | 0.86 |
| phthalic acid [src: enigma_carbon_census_1] | necromass | Shikimates/Phenylpropanoids | T2_3_reaction | 36 | 0 | 15 | 12 | 0.75 |
| terephthalic acid [src: enigma_carbon_census_1] | necromass | Shikimates/Phenylpropanoids | T2_3_reaction | 34 | 34 | 17 | 10 | 0.67 |
| phenylethylamine [src: enigma_carbon_census_1] | groundwater | Alkaloids | T2_3_reaction | 28 | 0 | 11 | 7 | 0.61 |
| xanthine [src: enigma_carbon_census_1] | groundwater | Alkaloids | T3_kegg | 13 | 0 | 6 | 4 | 0.75 |
| abscisic acid [src: enigma_carbon_census_1] | groundwater | Terpenoids | T2_3_reaction | 2 | 0 | 1 | 1 | 0.02 |
| lauric acid [src: enigma_carbon_census_1] | necromass | Fatty acids | T1_measured | 0 | 0 | 0 | 0 | none |

Two rows carry caveats. Xanthine was mis-scored as carbon-callable. Its allowlisted reaction R02107 (xanthine→urate) belongs to the purine nitrogen pathway, not carbon catabolism, so the carbon-callable set is effectively 8. [src: enigma_carbon_census_1] The NB03 carbon allowlist now excludes R02107. The committed tables still list xanthine because they predate the fix and were not regenerated. [src: enigma_carbon_census_1]

Lauric acid is callable on measured_fitness evidence only. The evidence is a Tier-1 Fitness Browser carbon-source fitness experiment in a reference bacterium, not an ENIGMA isolate. It therefore has no isolate or field rows and does not appear in deliverable (a). [src: enigma_carbon_census_1]

### Data-handling lessons for NMDC and Planet Microbe

NMDC covstats and Planet Microbe `taxonomy.name` are species-level. Any genus-level abundance claim needs species-to-genus aggregation first. [src: enigma_carbon_census_1] Filtering on bare genus names matches only near-zero genus-rank reference rows. This bug first showed 0/68 marine genera. [src: enigma_carbon_census_1] Any project doing genus-level abundance over `covstats_taxonomy_rollup` or Planet Microbe `run_to_taxonomy` needs this rollup. [src: enigma_carbon_census_1]

The NMDC abundance denominator is the 3825 covstats files that carry taxonomy, not the ~6700 `sample_file_lookup` rows. Using the lookup count deflates relative abundances by ~1.75×. [src: enigma_carbon_census_1]

Sample-level environment labels come from `nmdc_metadata.biosample_set`, joined to covstats `sample_id` via `kbase.nmdc_arkin.sample_file_lookup`. [src: enigma_carbon_census_1] This gives 99% coverage across two ontologies, against ~13% for `study_table` GOLD alone. [src: enigma_carbon_census_1]

## Interpretation: Limitations

This part of the report places the census results against the literature. It reads catabolic knowledge in the queried resources as deep for aromatics and phthalates and absent for most alkaloids and terpenoids. [src: enigma_carbon_census_1] It also lists the limits on what the atlas and the statistics can support.

### Aromatic catabolism is well characterized

Six of the eight callable compounds route through well-characterized aromatic catabolism. Salicylate, the hydroxybenzoates/-aldehyde and the two phthalates converge on protocatechuate/catechol and the β-ketoadipate pathway. [src: enigma_carbon_census_1] The report calls this funnel the canonical bacterial route for hydroxybenzoates, salicylate and phthalates. [src: enigma_carbon_census_1] See [[entities/ketoadipate-pathway]]. Because the six share one lower pathway, they co-occur within the aromatic block. [src: enigma_carbon_census_1]

The other two callables do not use this funnel. [src: enigma_carbon_census_1] Phenylethylamine goes by amine oxidation to phenylacetate and then the phenylacetyl-CoA (paa) pathway. That route is mechanistically separate, so its cross-block co-occurrence signal is not part of the β-ketoadipate funnel. [src: enigma_carbon_census_1] Xanthine is a purine (nitrogen) pathway compound mis-included here. [src: enigma_carbon_census_1]

### Phthalate and terephthalate, and Burkholderiales

The report calls terephthalate/phthalate catabolism the best-characterized necromass aromatic catabolism in the census. [src: enigma_carbon_census_1] Terephthalate goes via terephthalate dioxygenase to protocatechuate. Degraders are concentrated in Pseudomonadota (Ideonella/Comamonas) and in actinobacterial degraders. [src: enigma_carbon_census_1] Literature support for Burkholderiales/Comamonadaceae dominance is strongest for phthalate/terephthalate catabolism, which matches the report's versatility ranking. [src: enigma_carbon_census_1] See [[entities/burkholderiales]].

The periphyton enrichment of this clade rests mainly on the project's own abundance data, at ~97% prevalence in periphyton samples. [src: enigma_carbon_census_1] The report says this is the project's own observation, pending a targeted literature anchor. [src: enigma_carbon_census_1]

### Dark compounds and literature gaps

The report says the dark compounds are a deliverable, not a failure of method. The interpretation text names 75 dark compounds [src: enigma_carbon_census_1], while the contribution summary gives a dark fraction of 89% (74/83). [src: enigma_carbon_census_1] The report does not explain this one-compound difference, so both figures are given as stated. The dark compounds name where genetic determinants of carbon use cannot be linked in these resources, and where enrichment is the candidate discovery route. [src: enigma_carbon_census_1] "Organism-dark" means not linkable through the queried the KBase Data Lakehouse and curated resources. It does not mean unknown to science. [src: enigma_carbon_census_1] Class-level catabolic literature exists for monoterpenes (Marmulla & Harder, *Front. Microbiol.* 2014) and for alkaloids such as nicotine (Huang et al., *Front. Microbiol.* 2020). [src: enigma_carbon_census_1] The census found zero literature rescues, but that reflects a PubMed-title-only screen, not absence of evidence. A PaperBLAST/abstract-level pass would likely reclassify part of the dark set. [src: enigma_carbon_census_1] See [[concepts/resource-darkness-of-compound-catabolism]].

The report lists three contributions:
- a tier-stratified linkage from 83 named compounds through structures, pathways, ENIGMA isolate strains, GTDB phylogeny, SSO field occurrence and global biome abundance, with the Tier 0 gap treated as a result [src: enigma_carbon_census_1];
- a quantified dark fraction of 89% (74/83), with per-class and per-reason structure to guide enrichment prioritization [src: enigma_carbon_census_1];
- a periphyton-resolved abundance reservoir for the implicated genera that bulk-environment labels obscure. [src: enigma_carbon_census_1]

### Limits of the global atlas

No environmental dataset measures the census compounds. The atlas therefore reports biome occupancy of the implicated genera, not catabolic flux. [src: enigma_carbon_census_1] It is a biome-occupancy proxy, and enrichment of a genus in soil does not mean it degrades the compound there. [src: enigma_carbon_census_1] The signal is biologically coherent: soil generalists in soil, aquatic Betaproteobacteria in freshwater, a Comamonadaceae periphyton reservoir, and terrestrial taxa rare in the open ocean. [src: enigma_carbon_census_1] This validates the taxonomic/abundance pipeline and the ENVO (Environment Ontology)/GOLD labels. It does not validate the compound→pathway→organism inference. It also cannot show that any genus degrades a census compound in a sampled environment. [src: enigma_carbon_census_1] The marine arm has 302 PM runs with presence/abundance only and no gene information, so it suits only a negative biome contrast. [src: enigma_carbon_census_1] See [[concepts/biome-abundance-atlases-as-a-proxy-for-catabolic-potential]].

The soil-versus-freshwater enrichment p/q-values are exploratory and not calibrated. Each metagenome is treated as independent in a rank test over compositional, zero-inflated abundances. [src: enigma_carbon_census_1] All 83 genera reach q<0.05, many at q~1e-70, which the report attributes to massively inflated significance. [src: enigma_carbon_census_1] The direction and rank of the contrast are trustworthy, but the p-values should not be quoted as calibrated significance. [src: enigma_carbon_census_1] The label-free outlier mode (Arm B) is the more defensible discovery signal. [src: enigma_carbon_census_1] See [[concepts/calibration-and-denominators-in-environmental-abundance-contrasts]].

### Callability, filters and the xanthine error

The 8 ENIGMA isolate-call callables rest on a genome-prevalence-<10% signature-reaction filter. It keeps a reaction only if it is catabolic for the compound, by KEGG degradation map membership or a 3-reaction curated allowlist. [src: enigma_carbon_census_1] A different filter would move the callable/dark boundary, so the dark fraction is conditional on this choice. [src: enigma_carbon_census_1] The 9th callable, lauric acid, rests on an independent measured-fitness basis and is not subject to this filter. [src: enigma_carbon_census_1] See [[concepts/catabolic-direction-filtering-and-mis-scored-carbon-calls]].

Xanthine's allowlisted reaction R02107 (xanthine→urate, xanthine oxidase) is the purine pathway, which is nitrogen acquisition and not carbon catabolism. [src: enigma_carbon_census_1] A bacterial carbon route for purines exists, but it is a distinct anaerobic gene cluster that the project does not score. [src: enigma_carbon_census_1] The carbon-callable set is therefore effectively 8 of the 9 callable. [src: enigma_carbon_census_1] R02107 has been removed from the carbon allowlist in build_nb03.py. The committed deliverable tables still include xanthine because they were not regenerated, and rerunning NB03→NB04→NB08 would drop it. [src: enigma_carbon_census_1]

With only n=9 callable compounds, the physicochemical contrasts (callable compounds smaller/simpler) are directional only. They use uncorrected Mann–Whitney p-values and are descriptive, not calibrated significance. [src: enigma_carbon_census_1]

### Completeness scores and taxonomy bridging

The sig_completeness metric is the fraction of each compound's own signature reactions that a genome carries. [src: enigma_carbon_census_1] High-certainty calls are not comparable across compounds. Terephthalic acid has a single required reaction, so any carrier scores 1.0 ("high"). Phthalic acid has a 3-reaction signature, which cannot score that way. [src: enigma_carbon_census_1] The "terephthalic 34/34 high" headline is therefore the weakest completeness call, not the strongest. The report advises reading certainty as the raw n_sig_carried / n_required in phylo_utilizer_map.tsv. [src: enigma_carbon_census_1]

The pangenome↔ENIGMA taxonomic bridge is genus-level at best. The report avoids isolate-specific transfer of pangenome Tier-2 reconstructions and uses direct genome_depot annotation instead. [src: enigma_carbon_census_1] See [[concepts/genus-level-taxonomy-bridging-to-pangenome-clades-and-its-coverage-limits]].

### Untestable source hypothesis

The source-tracking hypothesis H3 is genuinely untestable with these compounds. The n=2 necromass callables are fully confounded with phthalate chemistry, and the report states this rather than forcing a result. [src: enigma_carbon_census_1] See [[concepts/confounding-of-compound-source-with-chemical-class]].

## Data; Supporting Evidence; Future Directions

This part of the report lists the census's data sources, output tables and recommended follow-up work. The sources span PubChem, ModelSEED, the pangenome, Fitness Browser, ENIGMA, NMDC and Planet Microbe. [src: enigma_carbon_census_1] The follow-up items are the report's own proposals, not measured results. [src: enigma_carbon_census_1]

### Data sources

Each source feeds a specific step of the census.

| Source | Content used | Role |
|---|---|---|
| PubChem (external) PUG-REST | Name → CID → InChIKey/SMILES, with KEGG/ChEBI/ModelSEED cross-references | Identity resolution [src: enigma_carbon_census_1] |
| [[entities/modelseed-biochemistry]] | Compound, reaction and enzyme data | Compound → reaction → enzyme linkage at Tier 2/3 [src: enigma_carbon_census_1] |
| `kbase_ke_pangenome` ([[entities/kbase-ke-pangenome]]) | KEGG/EC (Enzyme Commission)/eggNOG functional annotations | Enzyme presence across GTDB species pangenomes, with a null denominator of 3109 genomes [src: enigma_carbon_census_1] |
| `kescience_fitnessbrowser` ([[entities/fitness-browser]]) | RB-TnSeq (random barcode transposon sequencing) carbon-source experiments | Measured utilization, the Tier 1 channel [src: enigma_carbon_census_1] |
| `enigma_genome_depot_enigma` | Protein-to-reaction, ortholog and EC annotations; gene → genome → strain → taxon links | Catabolic annotations directly on ENIGMA isolate proteins, and an isolate → strain → NCBI-taxid crosswalk (deliverables a, b) [src: enigma_carbon_census_1] |
| `enigma` (SSO field) | Zhou Lab 16S data and `enigma_coral` bricks | Local SSO field genus occurrence (deliverable c) [src: enigma_carbon_census_1] |
| `kbase.nmdc_arkin` and `nmdc_metadata` | `covstats_taxonomy_rollup`, `sample_file_lookup`, `biosample_set` | Terrestrial and freshwater genus abundance, plus ENVO (Environment Ontology)/GOLD environmental labels (deliverable c, global) [src: enigma_carbon_census_1] |
| `planetmicrobe.planetmicrobe` | Taxonomy and run/experiment/sample/project/campaign tables | Marine genus abundance contrast (deliverable c, global) [src: enigma_carbon_census_1] |

### Output tables

The census wrote the following tables, with these row counts.

- Identity and linkage: `resolved_compounds.tsv` has 83 rows resolving compounds to InChIKey/SMILES and database cross-references. [src: enigma_carbon_census_1] `compound_linkage.tsv` and its deepened version have 83 rows of per-compound pathway/enzyme linkage and tier. [src: enigma_carbon_census_1] `compound_physicochem.tsv` has 83 rows of PubChem descriptors, including MW (molecular weight), XLogP, TPSA and complexity. [src: enigma_carbon_census_1]
- Organism predictions: `compound_organism_predictions.tsv` has 948 rows of pathway/enzyme-to-organism predictions. [src: enigma_carbon_census_1] `compound_organism_dark.tsv` has 75 pre-I1 organism-dark compounds with reasons. Lauric acid was later reclassified callable, which leaves 74 dark in the master table. [src: enigma_carbon_census_1] `dark_matter_taxonomy.tsv` has 74 post-I1 dark compounds, bucketed as orphan, no-reaction, biosynthesis-known or generic. [src: enigma_carbon_census_1]
- Fitness match: `fb_inchikey_matches.tsv` has 1 structural (InChIKey) match to a Fitness Browser carbon-source Tier-1 experiment, for lauric acid. [src: enigma_carbon_census_1]
- Deliverables (a) and (b): `enigma_utilizer_predictions.tsv` has 569 rows of per-compound ENIGMA isolate utilizers. [src: enigma_carbon_census_1] `phylo_utilizer_map.tsv` has 494 rows of strain placements and certainty. [src: enigma_carbon_census_1]
- H2 co-occurrence: `cooccurrence_matrix.tsv` has 28 rows with φ, p and q. [src: enigma_carbon_census_1] `cooccurrence_effects.tsv` has 28 rows of effect sizes from review I4, including Haldane OR (odds ratio) with 95% CI (confidence interval), and Jaccard. [src: enigma_carbon_census_1]
- Deliverable (c) environment: `environmental_atlas.tsv` has 156 rows of local SSO field genus occurrence. [src: enigma_carbon_census_1] `env_atlas_global.tsv` has 400 rows of genus × biome abundance from NMDC and Planet Microbe. [src: enigma_carbon_census_1] `env_enrichment_soil_fresh.tsv` has 83 rows of exploratory soil-vs-freshwater abundance contrasts. [src: enigma_carbon_census_1] `env_outlier_samples.tsv` has 249 rows of label-free top genus×sample abundance spikes. [src: enigma_carbon_census_1]
- Master table: `census_master_summary.tsv` has 83 rows, one per compound. [src: enigma_carbon_census_1]

### Analysis stages

- Profiling and identity: notebook 00 profiles the 83 compounds by class, source and MW/LogP. [src: enigma_carbon_census_1] Notebook 01 resolves names through PubChem CID to InChIKey/SMILES and cross-references. [src: enigma_carbon_census_1]
- Linkage: notebooks 02 and 02b link compounds to pathways and enzymes through multiple channels and a Phase-1 gate. [src: enigma_carbon_census_1] Notebook 02c is the review I1 structural re-match of Fitness Browser (FB) Tier-1 carbon-source experiments, going name → PubChem → InChIKey. [src: enigma_carbon_census_1]
- Organisms and utilizers: notebook 03 maps pathways and enzymes to organisms with a catabolic-direction filter. [src: enigma_carbon_census_1] Notebook 04 produces the ENIGMA isolate utilizer table for deliverable (a). [src: enigma_carbon_census_1]
- Co-occurrence: notebook 05 analyzes H2 within-block and cross-block co-occurrence and versatility. [src: enigma_carbon_census_1] Notebook 05b computes the review I4 Haldane OR, CI and Jaccard effect sizes from saved counts. [src: enigma_carbon_census_1]
- Maps and atlases: notebook 06 gives GTDB strain placements and certainty for deliverable (b). [src: enigma_carbon_census_1] Notebook 07 builds the local SSO field atlas. [src: enigma_carbon_census_1] Notebook 07b builds the global NMDC and Planet Microbe atlas. [src: enigma_carbon_census_1]
- Synthesis: notebook 08 assembles the three deliverables, the gap map and the master table, defining callable as an isolate call OR measured fitness, under I1. [src: enigma_carbon_census_1] Notebook 09 covers physicochemistry and bioavailability, chassis specialists and generalists, per-clade conservation, and dark-matter taxonomy. [src: enigma_carbon_census_1]

### Future directions

- **Rank the dark compounds by cause.** The 74 organism-dark compounds are treated as discovery-mode enrichment targets, ranked by why they are dark. [src: enigma_carbon_census_1] See [[concepts/resource-darkness-of-compound-catabolism]].
- **Start with the hardest cases.** The report would begin the 29 fully-orphan (no-KEGG) compounds, especially the necromass-heavy alkaloids and terpenoids, with anonymous community enrichment and metagenomics. [src: enigma_carbon_census_1]
- **Consult the literature first for biosynthesis-known compounds.** The 6 biosynthesis-known compounds are Tyramine, guanidineacetic acid, cinnamic acid, caffeic acid, palmitic acid and farnesol. The report would treat them as a separate MIBiG/biosynthetic-literature consult before committing wet-lab effort. [src: enigma_carbon_census_1]
- **Promote compounds by literature mining.** Targeted PaperBLAST/PubMed mining for alkaloid and terpenoid catabolic enzymes, searched back into the genomes, would convert some dark compounds from Tier 5 to Tier 3 (callable) without new experiments. [src: enigma_carbon_census_1]
- **Replace the environmental test.** The current environmental contrast is an exploratory ranking. The report recommends replacing the per-sample rank test with a study-aware mixed model, or a sample-level permutation that respects study structure, to get defensible enrichment statistics. [src: enigma_carbon_census_1] See [[concepts/calibration-and-denominators-in-environmental-abundance-contrasts]].
- **Choose inocula for aromatic utilizers.** The Comamonadaceae periphyton reservoir suggests freshwater-biofilm inocula for the aromatic-utilizer enrichments. [src: enigma_carbon_census_1]

## Caveats and Open Work

- Darkness is resource-darkness, and a literature/PaperBLAST pass would reclassify some dark compounds. [src: enigma_carbon_census_1]
- Lauric acid sits outside both arms, since it has measured fitness but no isolate prediction. [src: enigma_carbon_census_1]
- The terephthalic-acid high-certainty figure is a single-signature artifact. [src: enigma_carbon_census_1]
- Physicochemical comparisons are directional because n=9. [src: enigma_carbon_census_1]
- The soil-versus-freshwater contrast is exploratory. The global atlas measures organism abundance, not catabolism. [src: enigma_carbon_census_1]
- Conservation fractions describe within-called-set specialization only. [src: enigma_carbon_census_1]

## Slots Into

- [[concepts/resource-darkness-of-compound-catabolism]]: most of the 83 compounds are organism-dark, which is resource-darkness and not absence from science. [src: enigma_carbon_census_1]
- [[concepts/taxonomic-distribution-of-aromatic-compound-catabolism]]: callable aromatics concentrate in Burkholderiales and related clades. [src: enigma_carbon_census_1]
- [[concepts/co-occurrence-and-modularity-of-catabolic-capacities-across-genomes]]: the φ coefficient hides enrichment for rare capacities, and OR gives within-aromatic median 1.12. [src: enigma_carbon_census_1]
- [[concepts/biome-abundance-atlases-as-a-proxy-for-catabolic-potential]]: the global atlas is an organism-abundance proxy only. [src: enigma_carbon_census_1]
- [[concepts/measured-fitness-as-independent-evidence-of-carbon-utilization]]: lauric acid is callable only through measured fitness. [src: enigma_carbon_census_1]
- [[concepts/confounding-of-compound-source-with-chemical-class]]: no physicochemical separation by source. [src: enigma_carbon_census_1]
- [[concepts/catabolic-direction-filtering-and-mis-scored-carbon-calls]]: the NB03 filter keeps only catabolic-direction evidence. [src: enigma_carbon_census_1]
