---
type: "Summary"
description: "Summary of the project Plant Microbiome Ecotypes — Compartment-Specific Functional Guilds and Their Genetic Architecture."
doc_type: "short"
full_text: "sources/plant_microbiome_ecotypes__REPORT.md"
---
# Plant Microbiome Ecotypes — Compartment-Specific Functional Guilds and Their Genetic Architecture

Summary of the project Plant Microbiome Ecotypes — Compartment-Specific Functional Guilds and Their Genetic Architecture.

## Key Findings

### Compartment signal

The report says most of the original compartment R² of 0.527 was a taxonomic-sampling artifact of a few genome-rich species, not a community-wide signal. [src: plant_microbiome_ecotypes] The refined analysis is a separate measurement. In 607 plant-compartment species, db-RDA (distance-based redundancy analysis) on PCoA scores of Jaccard distance over the refined 17-marker panel gave location-only R² = 0.060 (permutation p = 0.001, 999 permutations). [src: plant_microbiome_ecotypes] PERMANOVA on the refined analysis measures location plus dispersion. It gave pseudo-F = 23.2, p = 0.001 and R² = 0.071. [src: plant_microbiome_ecotypes] Rhizosphere species had the most variable functional profiles, with mean centroid distance 0.528. [src: plant_microbiome_ecotypes] In NB04, 69 of 96 marker × compartment pairs were significant. [src: plant_microbiome_ecotypes] See [[concepts/compartment-specific-functional-differentiation-of-plant-associated-bacteria]].

### Plant-association markers under confounder controls

The report ran several tests of plant-association markers. In the genus-cluster-robust GLM (cluster = genus), 8/14 markers survived at q<0.05 with proper Wald CIs. iaa_biosynthesis was identified as one L1 false positive. [src: plant_microbiome_ecotypes] In that GLM, ACC deaminase had OR 8.01 (95% CI [4.19, 15.32], q 2.1×10⁻⁹). [src: plant_microbiome_ecotypes] T3SS and nitrogen fixation each had OR=2.71. [src: plant_microbiome_ecotypes] Pectinase had OR 1.59 (q 3.4×10⁻⁴). [src: plant_microbiome_ecotypes] IAA biosynthesis was not significant (OR 0.91, 95% CI [0.40, 2.06], q 0.96). [src: plant_microbiome_ecotypes] Within-genus label shuffling, the strictest species-level null, retained 3/15 markers: nitrogen fixation, ACC deaminase and T3SS. [src: plant_microbiome_ecotypes] T3SS had perm p = 0.005 in that shuffle. [src: plant_microbiome_ecotypes] The report says this three-tier interpretation supersedes the earlier "9/17 survive L1" framing. [src: plant_microbiome_ecotypes] Separately, attenuation from Fisher OR to phylogenetically controlled OR (for example COG3569: 8.92→6.01) indicates partial phylogenetic confounding, though the report says substantial ecological signal persists. [src: plant_microbiome_ecotypes] See [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]].

### Dual-nature classification

About 33% of dual-nature species shift to neutral when genome size is normalized. The headline 78.7% dual-nature rate therefore masks a genome-size gradient that is observational, not model-dependent. [src: plant_microbiome_ecotypes] NB07 composite scoring is more stringent and classifies 38.0% of species as neutral. [src: plant_microbiome_ecotypes] It is more discriminating but also more assumption-laden than NB02. [src: plant_microbiome_ecotypes] The refined marker cohorts misclassified neutral *Escherichia coli* K-12 as dual-nature. [src: plant_microbiome_ecotypes] In novel-OG regressions, the genome-size and plant-association coefficients stayed simultaneously large and positive. [src: plant_microbiome_ecotypes] See [[concepts/dual-nature-plant-associated-bacteria-and-the-validity-of-marker-based-cohorts]].

### Within-species segregation

After the genome-ID fix, 1306/1306 genomes matched (previously 0), recovering 599 plant-associated genomes across the 5 originally tested species. [src: plant_microbiome_ecotypes] Of 17 testable species, 5 passed Bonferroni-corrected Fisher's exact testing at α = 0.05/17 = 0.0029, and 3 of those also satisfied Cochran's rule. [src: plant_microbiome_ecotypes] Twelve testable species showed no clustering. [src: plant_microbiome_ecotypes] *Xanthomonas vasicola* segregated to *Zea mays* (47/52 in subclade 0). [src: plant_microbiome_ecotypes] See [[concepts/within-species-subclade-segregation-of-plant-association-and-host-specialization]].

### Annotation, mobilome and complementarity

Pfam recovery added CWDE pectinase markers to 1,082 species. [src: plant_microbiome_ecotypes] Plant-associated genera had higher mobilome burden than non-plant genera (median 3.7 vs 2.8 mobile elements per genome, Mann-Whitney U p=1.49×10⁻⁵). [src: plant_microbiome_ecotypes] Co-occurring genus pairs were slightly less complementary than random pairs (permutation p < 0.001). [src: plant_microbiome_ecotypes] The Phase 1 NB06 Cohen's d = −7.54 was largely a formula error. [src: plant_microbiome_ecotypes] See [[concepts/domain-based-marker-detection-and-annotation-method-bias]] and [[concepts/functional-redundancy-versus-complementarity-among-co-occurring-genera]].

## Key Findings: Plant compartments impose a small but real functional shift on microbial …

This part of the report shows that plant compartments shift microbial functional profiles only slightly after correction. An earlier, much larger compartment effect was largely a sampling artifact. Per-function enrichments, core versus accessory architecture, a corrected complementarity result and a genome-wide plant-association scan are also covered. [src: plant_microbiome_ecotypes]

### Compartment effect size: revised downward

In 607 plant-compartment species, a db-RDA (constrained ordination on principal coordinates analysis, PCoA, scores of Jaccard distance over the refined 17-marker panel) gave location-only R² = 0.060 (permutation p = 0.001, 999 permutations). [src: plant_microbiome_ecotypes] The permutational analysis of multivariate dispersions (PERMDISP) confirmed heterogeneous dispersion among compartments (F = 15.6, p = 0.001). Root was tightest (mean centroid distance 0.452), phyllosphere intermediate (0.503) and rhizosphere most variable (0.528). [src: plant_microbiome_ecotypes] About 84% of the total permutational multivariate analysis of variance (PERMANOVA) R² was real centroid shift and 16% was dispersion. [src: plant_microbiome_ecotypes] Root, rhizosphere and phyllosphere are therefore functionally distinct in centroid terms, at a small effect size of ~6% of variance. [src: plant_microbiome_ecotypes]

This **corrects** the original NB04 PERMANOVA on the Phase 1 25-marker panel, which reported R² = 0.527 (pseudo-F = 235.1, p = 0.001). NB14's exclude-top-3-species sensitivity left a residual R² of only 0.072 once dominant rhizobial and Pseudomonas clades were removed. [src: plant_microbiome_ecotypes] The report concludes that most of the 0.527 was a taxonomic-sampling artifact of a few genome-rich species, not a community-wide signal. [src: plant_microbiome_ecotypes]

### Per-function enrichments still stand

The report covers 1,136 plant-associated species classified across four compartments: root 292, rhizosphere 160, phyllosphere 157 and endophyte 29. [src: plant_microbiome_ecotypes] In the original NB04 Fisher-test framework, root species were enriched for ACC (1-aminocyclopropane-1-carboxylate) deaminase (OR = 69.3), type III secretion system (T3SS, OR = 65.6), nitrogen fixation (OR = 14.5) and quorum sensing (OR = 24.1). OR is odds ratio. [src: plant_microbiome_ecotypes] In NB04, 69 of 96 marker × compartment pairs were significant. [src: plant_microbiome_ecotypes] The report states that the revised decomposition does not contradict these per-function enrichments. Only the headline magnitude of the multivariate R² was inflated. [src: plant_microbiome_ecotypes]

### Core versus accessory architecture

Beneficial plant growth promoting (PGP) gene clusters were predominantly core genome, with a 64.6% core fraction. This significantly exceeded the genome-wide baseline of 46.8% and the 45.2% of pathogenic gene clusters. [src: plant_microbiome_ecotypes] The Mann-Whitney comparison of per-species core fractions gave U=83,567,419 (p=3.38e-125), with a bootstrap 95% confidence interval for the beneficial-pathogenic difference of [0.089, 0.106]. [src: plant_microbiome_ecotypes]

Core fractions were highest for these functions:

| Function | Core fraction |
|---|---|
| Biofilm | 83.3% [src: plant_microbiome_ecotypes] |
| IAA biosynthesis | 78.1% [src: plant_microbiome_ecotypes] |
| Nitrogen fixation | 72.3% [src: plant_microbiome_ecotypes] |
| Phosphate solubilization | 70.9% [src: plant_microbiome_ecotypes] |

In contrast, type IV secretion system (T4SS, 48.5% singleton), coronatine toxin (45.2%) and effector (39.8%) clusters were strongly accessory/singleton-enriched. [src: plant_microbiome_ecotypes]

### Mobility and horizontal transfer

Among 1,136 plant-associated species, those carrying singleton marker gene clusters were 16× more likely to carry transposase/integrase singletons (Fisher's exact OR=15.95, p=8.8e-20). [src: plant_microbiome_ecotypes] The overall singleton enrichment ratio for markers was 0.78, so markers are less mobile than the genomic average (Wilcoxon p<1e-300). [src: plant_microbiome_ecotypes] The report reads this mixed signal as follows. Individual horizontal gene transfer (HGT) events appear common. Plant-interaction markers as a class appear under stronger purifying selection than the genomic average, likely because they are functionally important once acquired. This is an interpretation, not a direct measurement. [src: plant_microbiome_ecotypes]

Cross-species context variation means the same ortholog group is core in one species and singleton in another. [src: plant_microbiome_ecotypes] It was higher for pathogenic markers (0.534) than beneficial markers (0.450), but not significantly so (Kruskal-Wallis p=0.122). [src: plant_microbiome_ecotypes]

### Complementarity: a corrected, small effect

Co-occurring plant-associated genera in NMDC soil communities were slightly less complementary than random genus pairs (Cohen's d ≈ −0.4, permutation p < 0.001). This supports functional redundancy, at a small effect size. [src: plant_microbiome_ecotypes] The Phase 1 NB06 value of d = −7.54 was largely a formula error. NB06 divided the mean difference by the SD of permutation means, not by the raw pair-level SD. [src: plant_microbiome_ecotypes] Recomputing NB06's species-max aggregation with a consistent formula gave d ≈ −0.43. [src: plant_microbiome_ecotypes] Switching to species-prevalence aggregation (the I1 fix in NB14) reduced |d| further to 0.39. [src: plant_microbiome_ecotypes] Of the apparent 20× reduction in the early Phase 2b draft, ~90% was attributed to formula correction and ~10% to aggregation correction. [src: plant_microbiome_ecotypes] The direction of the result was robust under both aggregation methods. [src: plant_microbiome_ecotypes] The report states that this corrected result is consistent with Louca et al. (2018), who argued that functional redundancy is an emergent property of microbial systems. [src: plant_microbiome_ecotypes]

As a reliability check, BacDive metabolite utilization cross-validated GapMind predictions at 83.1% consistency. The report reads this as confirming that the pathway completeness scores are reliable. [src: plant_microbiome_ecotypes]

### Genome-wide plant-association scan

Of 5,671 eggNOG ortholog groups (OGs) tested, 5,341 were significantly associated with plant versus non-plant species (q<0.05). [src: plant_microbiome_ecotypes] Of these, 3,840 showed strong enrichment (OR>2). [src: plant_microbiome_ecotypes] After phylogenetic control by phylum-level logistic regression, 50 novel OGs retained significance (all p<0.05, OR>1). [src: plant_microbiome_ecotypes] The top hit was COG3569 (Fisher OR=8.92, phylo-controlled OR=6.01, q=7.7e-242). It occurred in 54% of plant-associated species and 12% of non-plant species. [src: plant_microbiome_ecotypes] The drop from Fisher OR to phylo-controlled OR indicates partial phylogenetic confounding, because plant-associated species cluster taxonomically. The report states that a substantial ecological signal persists after correction. [src: plant_microbiome_ecotypes]

## Key Findings: Most plant-associated bacteria carry both PGP and pathogenic markers, but …

This part of the report shows that most plant-associated bacteria carry both plant growth-promoting (PGP) and pathogenic markers, and that the size of this "dual-nature" group depends on the classification method. A species-level validation found the categorical label uninformative, while a continuous ratio gave a weak signal. The evidence is genomic marker presence, and the validation panel is small. [src: plant_microbiome_ecotypes]

### How common is the dual-nature class?

The report states that 65–85% of plant-associated species per compartment carry both PGP and pathogenic marker genes. [src: plant_microbiome_ecotypes] The two classification schemes give very different totals, as the table shows. The report ties the 35 percentage point gap to the difference between carrying both marker types and scoring highly on both axes. [src: plant_microbiome_ecotypes]

| Scheme | Rule | Result |
|---|---|---|
| NB02 binary marker presence | at least 1 PGP and at least 1 pathogenic marker [src: plant_microbiome_ecotypes] | 15,474/25,660 species (60.3%) dual-nature [src: plant_microbiome_ecotypes] |
| NB07 composite scoring | weights of 40% PGP markers, 20% core fraction, 15% complementarity, 10% metabolic breadth and 15% pathogen penalty, with adaptive thresholds at the median of non-zero scores [src: plant_microbiome_ecotypes] | neutral 38.0%, pathogenic 29.5%, dual-nature 25.2%, beneficial 7.3% [src: plant_microbiome_ecotypes] |

The report attributes the inclusive NB02 result to general bacterial functions such as flagella, chemotaxis and type VI secretion system (T6SS). These functions span both marker categories. [src: plant_microbiome_ecotypes] It describes NB07 as more discriminating but more assumption-laden. [src: plant_microbiome_ecotypes] Key dual-nature genera include the following:
- *Pseudomonas_E*: 358 species, with PGP markers HCN, phenazine and phosphate solubilization, and pathogenic markers T2SS, T3SS, T6SS and effectors. [src: plant_microbiome_ecotypes]
- *Bradyrhizobium*: 73 species, with PGP markers nitrogen fixation and ACC deaminase, and pathogenic markers T3SS, T4SS and CWDE. [src: plant_microbiome_ecotypes]
- *Streptomyces*: 261 species, with PGP markers phenazine and phosphate solubilization, and pathogenic markers CWDE and T3SS. [src: plant_microbiome_ecotypes]

See [[concepts/dual-nature-plant-associated-bacteria-and-the-validity-of-marker-based-cohorts]].

### Is the dual-nature rate a marker artifact?

The Phase 1 91-marker panel included ubiquitous functions (flagella, chemotaxis, T6SS, biofilm, quorum sensing, T2SS). It classified even *Escherichia* and *Salmonella* as 100% dual-nature. [src: plant_microbiome_ecotypes] Phase 2 used 17 plant-specific markers (9 PGP and 8 pathogenic) and gated multi-gene systems on KEGG module completeness. [src: plant_microbiome_ecotypes]

Gating had different effects by system:
- **T3SS (M00332):** requiring ≥3 module genes cut positive species from 10,300 to 1,661 (−8,855 false positives, an 86% reduction). [src: plant_microbiome_ecotypes]
- **Nitrogen fixation (M00175):** requiring ≥2 module genes cut nif-positive species by 346 (14% reduction). [src: plant_microbiome_ecotypes]
- **T4SS (M00333):** gating had minimal impact, because most hits were already multi-gene. [src: plant_microbiome_ecotypes]

Despite the stricter panel, dual-nature prevalence among plant-associated species rose from 60.3% to 78.7% (878/1,115 species). [src: plant_microbiome_ecotypes] The report explains this by the remaining markers co-occurring in plant-associated genomes. Their prevalences were phosphate solubilization 57.9%, CWDE cellulase 63%, phenazine 63% and T4SS 45.8%. [src: plant_microbiome_ecotypes] It concludes that the high rate is biologically real and not an artifact of over-broad markers. [src: plant_microbiome_ecotypes] This is the report's interpretation, not a separate test.

### Validation against model organisms (NB13)

The categorical cohort label failed this validation, and only a continuous ratio gave a weak signal. NB13 tested a curated 18-species panel with experimentally confirmed phenotypes: 7 known beneficial species, 7 known pathogens and 4 neutral non-plant controls. [src: plant_microbiome_ecotypes] The beneficial species were *P. simiae* WCS417, *P. protegens* CHA0, *B. velezensis* FZB42, *A. brasilense* Sp245, *R. leguminosarum*, *P. phytofirmans* PsJN and *S. meliloti*. [src: plant_microbiome_ecotypes] The pathogens were *P. syringae*, *R. solanacearum*, *X. campestris*, *A. tumefaciens*, *E. amylovora*, *P. carotovorum* and *C. michiganensis*. [src: plant_microbiome_ecotypes]

All 14 beneficial and pathogenic species were assigned to the dual-nature class. The categorical label therefore could not separate beneficial from pathogenic ground truth at species level. [src: plant_microbiome_ecotypes] The continuous pathogenicity ratio n_pathogen / (n_pgp + n_pathogen) was lower in known beneficial species (median 0.50) than in known pathogens (median 0.60). The test gave Mann-Whitney U = 9, p = 0.027, with N = 7 vs 7. [src: plant_microbiome_ecotypes] The report calls this a small effect at small sample size, though statistically consistent. [src: plant_microbiome_ecotypes]

The report rejects the earlier Phase 1 figure of 92.7% genus-level agreement as tautological, because cohorts are defined from marker presence. The species-level Mann-Whitney test replaces it. [src: plant_microbiome_ecotypes] It recommends treating the four cohort labels as a coarse screen and using the continuous ratio within the dual-nature class. [src: plant_microbiome_ecotypes]

### Functional annotation of plant-enriched ortholog groups

All 50 plant-enriched OGs from Phase 1 were fully annotated with eggNOG descriptions, InterProScan domains, GO terms (48/50) and MetaCyc pathways (39/50). None were hypothetical proteins. [src: plant_microbiome_ecotypes] See [[concepts/functional-characterization-of-plant-enriched-gene-families]].

- **Electron transport and energy metabolism:** 7/50 (14%) OGs. They include cytochrome c oxidase subunits, NADH dehydrogenase COG0649 and ubiquinol-cytochrome c reductase COG0723. [src: plant_microbiome_ecotypes] COG1845/ctaE has OR=14.5 and occurs in 93.2% of plant vs 48.7% of non-plant species. [src: plant_microbiome_ecotypes] COG0843/ctaD has OR=13.7. [src: plant_microbiome_ecotypes] The report considers this consistent with Preisig et al. (1996), who showed that cbb3-type oxidases enable respiration in microaerobic root nodules. [src: plant_microbiome_ecotypes]
- **Iron-sulfur cluster biosynthesis:** COG0316/iscA occurs in 94.3% of plant species. [src: plant_microbiome_ecotypes] The report calls Fe-S clusters essential cofactors for nitrogenase, respiratory chain complexes and oxidative stress defense. [src: plant_microbiome_ecotypes] It cites Fuangthong et al. (2015) linking IscR-mediated regulation to pathogenicity and oxidative stress resistance. [src: plant_microbiome_ecotypes]
- **Inorganic ion transport:** 6/50 (12%) OGs, which the report regards as consistent with nutrient-acquisition demands of rhizosphere colonization. [src: plant_microbiome_ecotypes]
- **Unknown function:** 19/50 (38%) OGs have characterized domains but no clear plant-interaction mechanism. The report treats them as candidates for experimental characterization. [src: plant_microbiome_ecotypes]

All 50 OGs had core gene fractions of 60.1–83.1% against a baseline of 46.8%. The report reads this as stable core-genome inheritance of plant-enriched functions. [src: plant_microbiome_ecotypes] Cross-referencing novel OGs with MGnify rhizosphere KEGG modules confirmed that 8 modules from novel OGs are present in rhizosphere species. [src: plant_microbiome_ecotypes]

### Host assignments

Host extraction identified 1,307 species with plant host assignments across 19 testable hosts (≥10 species each). [src: plant_microbiome_ecotypes] The most common hosts were rice (*Oryza sativa*, 286 species), *Arabidopsis thaliana* (184) and wheat (122). [src: plant_microbiome_ecotypes]

## Key Findings: MGnify cross-validation reveals mobilome enrichment but low classification …

This part of the report tests whether plant-association markers survive phylogenetic control, cross-checks plant-associated genera against the MGnify genome catalogue, and looks for plant-associated subclades within species. Three markers are robust at species level. MGnify supports T3SS (type III secretion system) as a plant marker but agrees only weakly on which genera are plant-associated. Subclade segregation is real but limited to a few species. [src: plant_microbiome_ecotypes]

### Phylogenetic control of plant-association markers

Standard logistic regression could not be fitted. NB10's statsmodels logit with genus fixed effects failed to converge for 0/14 markers, because plant association is heavily confounded with genus-level taxonomy. [src: plant_microbiome_ecotypes] The report therefore applied two other tests. A cluster-robust GLM (generalized linear model) with genus clusters, Wald inference and no L1 shrinkage found 8/14 markers significant at q<0.05 BH-FDR (Benjamini-Hochberg false discovery rate), with 95% Wald CIs (confidence intervals) excluding zero. [src: plant_microbiome_ecotypes] Within-genus label shuffling, described as the strictest species-level null, retained 3/15 markers: nitrogen fixation, ACC (1-aminocyclopropane-1-carboxylate) deaminase and T3SS. [src: plant_microbiome_ecotypes]

The GLM odds ratios (OR) are listed below.

| Marker | OR |
|---|---|
| ACC deaminase | 8.01 [src: plant_microbiome_ecotypes] |
| T3SS | 2.71 [src: plant_microbiome_ecotypes] |
| Nitrogen fixation | 2.71 [src: plant_microbiome_ecotypes] |
| Phenazine | 2.12 [src: plant_microbiome_ecotypes] |
| CWDE (cell wall degrading enzyme) cellulase | 1.87 [src: plant_microbiome_ecotypes] |
| Phosphate solubilization | 1.68 [src: plant_microbiome_ecotypes] |
| CWDE pectinase | 1.59 [src: plant_microbiome_ecotypes] |
| Effector | 1.35 [src: plant_microbiome_ecotypes] |

The combined three-tier verdict classed 3 markers as species-level robust. It classed 5 as cassette-level, meaning genus-acquired but not species-distinguishing. [src: plant_microbiome_ecotypes] It classed 6 as not robust under any test, a null result for those markers. [src: plant_microbiome_ecotypes]

### MGnify cross-validation

The cross-validation used the MGnify genome catalogue, which has 20,473 species across 4 biomes. [src: plant_microbiome_ecotypes] It gave independent support for some findings but showed low agreement on genus lists.

- **Mobilome burden.** Plant-associated genera carried a higher mobilome burden than non-plant genera. The medians were 3.7 vs 2.8 mobile elements per genome (Mann-Whitney U p=1.49×10⁻⁵). [src: plant_microbiome_ecotypes] The report notes that this contrasts with genome-level studies finding fewer mobile elements in plant-associated bacteria. It suggests the cause is rhizosphere/soil genera versus endosphere-focused comparisons. [src: plant_microbiome_ecotypes]
- **T3SS.** Prevalence was roughly 2× higher in crop rhizosphere biomes than in bulk soil (12.3%). The rhizosphere values were tomato 24.0%, maize 21.6% and barley 22.3%. The report treats this as independent confirmation of T3SS as a plant-association marker. [src: plant_microbiome_ecotypes] It aligns with Gonzalez-Vallina et al. (2024), who found family-specific T3SS/T6SS enrichment in rhizosphere metagenomes. [src: plant_microbiome_ecotypes]
- **Host specificity.** 17 genera occurred in all 3 crop rhizospheres, including Pseudomonas_E, Streptomyces, Variovorax, Telluria and Acidovorax. [src: plant_microbiome_ecotypes] 117 genera were unique to tomato [src: plant_microbiome_ecotypes], 54 to maize [src: plant_microbiome_ecotypes] and 5 to barley. [src: plant_microbiome_ecotypes] The report proposes host-specific genera as candidates for crop-specific biocontrol formulations. [src: plant_microbiome_ecotypes]
- **Concordance.** Pangenome-derived plant genera (487) and MGnify rhizosphere genera (438) overlapped by only 11.7% Jaccard. [src: plant_microbiome_ecotypes] The report attributes this to isolation metadata versus metagenomic detection and to sampling biases, not to classification error. [src: plant_microbiome_ecotypes] MGnify held 93 pangenome plant genera in soil but not rhizosphere, which suggests broader environmental associations. [src: plant_microbiome_ecotypes]
- **BGCs (biosynthetic gene clusters).** 84 plant-associated genera produce NRP/siderophore BGCs. This is consistent with the importance of siderophore-mediated iron acquisition in plant colonization. [src: plant_microbiome_ecotypes] The top producers were Mycobacterium (406) [src: plant_microbiome_ecotypes], Pseudomonas_E (125) [src: plant_microbiome_ecotypes] and Streptomyces (113). [src: plant_microbiome_ecotypes]

For host reference, maize had 98 species assigned as plant-host associates. [src: plant_microbiome_ecotypes]

### Within-species subclade segregation

Phylogenetic-tree coverage limits this analysis. Only 18 (28%) of 65 plant-associated species with ≥20 genomes have tree distance data in kbase_ke_pangenome.phylogenetic_tree_distance_pairs. [src: plant_microbiome_ecotypes] The other 47 lack tree coverage. They include Bradyrhizobium japonicum, Bradyrhizobium diazoefficiens, Mesorhizobium ciceri, Sinorhizobium medicae, Burkholderia glumae, Methylobacterium extorquens, Streptomyces scabiei, Xylella taiwanensis and Clavibacter michiganensis. [src: plant_microbiome_ecotypes]

Of 17 testable species (≥3 plant and ≥3 non-plant genomes), 5 (29%) passed Bonferroni-corrected Fisher's exact at α = 0.05/17 = 0.0029. [src: plant_microbiome_ecotypes] The species and p-values are below.

| Species | p |
|---|---|
| Xanthomonas vasicola | 1.6×10⁻⁴ [src: plant_microbiome_ecotypes] |
| Mesorhizobium sp002294985 | 1.1×10⁻⁴ [src: plant_microbiome_ecotypes] |
| Agrobacterium pusense | 4.5×10⁻⁴ [src: plant_microbiome_ecotypes] |
| Pseudomonas_E avellanae | 7.3×10⁻⁴ [src: plant_microbiome_ecotypes] |
| Xanthomonas campestris | 1.0×10⁻³ [src: plant_microbiome_ecotypes] |

Three of these (X. vasicola, P. avellanae, X. campestris) also satisfy Cochran's rule for chi² and are the most robust. [src: plant_microbiome_ecotypes] The other 2 pass only via Fisher's exact, which is exact and not subject to the small-cell constraint. [src: plant_microbiome_ecotypes] The report notes that the pattern is concentrated in Xanthomonas and Pseudomonas, genera known for pathovar-level host specialization. [src: plant_microbiome_ecotypes] See [[concepts/within-species-subclade-segregation-of-plant-association-and-host-specialization]].

### Subclade by host

Of 9 species with sufficient host annotation (≥5 host-annotated genomes, ≥2 hosts, ≥2 subclades), 2 passed both within-species and across-species Bonferroni. [src: plant_microbiome_ecotypes] Xanthomonas campestris segregates to Brassica hosts. 46/47 genomes in subclade 2 are on Brassica, with p = 2.7×10⁻¹² raw and 3.3×10⁻¹¹ after within-species pair-search Bonferroni. [src: plant_microbiome_ecotypes] Xanthomonas vasicola segregates to Zea mays. 47/52 genomes are in subclade 0, with p = 1.4×10⁻¹¹ raw and 1.7×10⁻¹⁰ after Bonferroni. [src: plant_microbiome_ecotypes] The report interprets both as canonical pathovar-host specializations confirmed at the genomic level. [src: plant_microbiome_ecotypes] X. campestris pv. campestris is the textbook Brassica pathogen. [src: plant_microbiome_ecotypes]

### Provenance

The refined-marker and phylogenetic-control analyses are in 10_refined_markers_host_species.ipynb, 14_deferred_controls.ipynb and notebooks/_run_c1_cluster_robust.py. The three-tier framing was finalized 2026-04-25. [src: plant_microbiome_ecotypes] The MGnify integration is in 11_mgnify_integration.ipynb. [src: plant_microbiome_ecotypes]

## Key Findings: Phase 2b: Adversarial-review corrections (H0, H1, H3, H5, H7 revised)

This part of the report shows that a genome-identifier mismatch had produced a false null for within-species plant-association subclades. After the fix, 5 of 17 testable species show weak support. It also reports that the species-level validation of the marker cohorts found categorical labels uninformative. [src: plant_microbiome_ecotypes]

### The NB12 null and its correction

NB12 first reported no significant within-species plant-associated subclade segregation (0/5 species). [src: plant_microbiome_ecotypes] The cause was a join failure, not biology. `phylogenetic_tree_distance_pairs` stores bare NCBI accessions, while `genome_environment.csv` uses GTDB-prefixed identifiers. After merging, `is_plant_associated` was entirely NaN (not a number). [src: plant_microbiome_ecotypes] See [[concepts/join-key-validity-and-identifier-format-mismatches]].

NB13 fixed the mismatch by prepending GB_ to GCA_ accessions and RS_ to GCF_ accessions. [src: plant_microbiome_ecotypes] After the fix, 1306/1306 genomes matched (previously 0). This recovered 599 plant-associated genomes across the 5 tested species that NB12 had silently dropped. [src: plant_microbiome_ecotypes] The original 5-species set then shows 1/5 significant under all metrics. [src: plant_microbiome_ecotypes] The report also concludes that a 5-species subset chosen by genome count was too small for honest conclusions. [src: plant_microbiome_ecotypes] The report says the genome-ID mismatch was one of three review issues resolved in NB13–NB15. [src: plant_microbiome_ecotypes] It also completed four statistical controls that its research plan had specified but Phase 1 had not run: C1, C4, I1 and within-genus label shuffling. [src: plant_microbiome_ecotypes]

### Full scan and its coverage limit

The analysis was re-run on all 65 plant-associated species with ≥20 genomes. [src: plant_microbiome_ecotypes] Only 18 of the 65 had any pairwise phylogenetic-distance data in `kbase_ke_pangenome.phylogenetic_tree_distance_pairs`. [src: plant_microbiome_ecotypes] The other 47 lacked tree coverage. They include Bradyrhizobium japonicum, B. diazoefficiens, Mesorhizobium ciceri, Sinorhizobium medicae, Burkholderia glumae, Methylobacterium extorquens, Streptomyces scabiei, Xylella taiwanensis and Clavibacter michiganensis. [src: plant_microbiome_ecotypes] The report states this limit bounds power regardless of methodology. [src: plant_microbiome_ecotypes] The true effect across all 65 species cannot be estimated until the GTDB tree is more completely populated in the KBase Data Lakehouse. [src: plant_microbiome_ecotypes] The scan on the 18-species set raised the count of significant species to 5/17 by including the broader candidate pool. [src: plant_microbiome_ecotypes]

Among 17 testable species (≥3 plant and ≥3 non-plant genomes and ≥2 subclades), 5 passed Bonferroni-corrected Fisher's exact testing at α = 0.05/17 = 0.0029. Three of those also satisfied Cochran's rule for the parametric chi² test. [src: plant_microbiome_ecotypes] BH-FDR is the Benjamini-Hochberg false discovery rate.

| Species | N | Plant genomes | Best subclade plant | Fisher p | BH-FDR q | Chi² |
|---|---|---|---|---|---|---|
| Xanthomonas vasicola | 101 | 30 | 71% | 1.6×10⁻⁴ | 0.0013 | Cochran-valid [src: plant_microbiome_ecotypes] |
| Mesorhizobium sp002294985 | 84 | 78 | 97% | 1.1×10⁻⁴ | 0.0013 | small cells, Fisher only [src: plant_microbiome_ecotypes] |
| Agrobacterium pusense | 80 | 13 | 100% | 4.5×10⁻⁴ | 0.0026 | small cells, Fisher only [src: plant_microbiome_ecotypes] |
| Pseudomonas_E avellanae | 319 | 68 | 31% | 7.3×10⁻⁴ | 0.0031 | Cochran-valid [src: plant_microbiome_ecotypes] |
| Xanthomonas campestris | 128 | 42 | 42% | 1.0×10⁻³ | 0.0034 | Cochran-valid [src: plant_microbiome_ecotypes] |

All five pass Bonferroni. [src: plant_microbiome_ecotypes] Pseudomonas amygdali's borderline chi² p = 0.031 from the 5-species subset does not survive Bonferroni in the larger scan and stays invalid under Cochran's rule. [src: plant_microbiome_ecotypes] The final verdict is weak support in 5 of 17 testable species (29%). X. vasicola, P. avellanae and X. campestris show the strongest signal across both tests. [src: plant_microbiome_ecotypes] X. vasicola pv. vasculorum is a known maize/sugarcane pathogen. [src: plant_microbiome_ecotypes]

### Subclade–host association

The 18-species scan was extended on 2026-04-25 to test subclade × host associations. It used within-species Bonferroni correction for the pair search and across-species correction for multiple species. [src: plant_microbiome_ecotypes] Two species passed both corrections, and Xanthomonas campestris segregates to Brassica hosts. [src: plant_microbiome_ecotypes] Ralstonia solanacearum passes BH-FDR but not across-species Bonferroni. [src: plant_microbiome_ecotypes]

### Interpretation

The report reads these results as follows. Within-species plant adaptation is predominantly accessory-driven. In specific genera, notably Xanthomonas, accessory cassettes have stratified onto core-phylogenetic subclades. [src: plant_microbiome_ecotypes] It infers that pathovar designations in those genera have a real phylogenetic basis at the within-species level. [src: plant_microbiome_ecotypes] This is an interpretation, not a direct measurement. It cites Melnyk et al. (2019), who found that Pseudomonas plant-lifestyle transitions are driven by convergent gain/loss of accessory genomic islands rather than core-genome phylogeny. [src: plant_microbiome_ecotypes] It also cites Satterwhite & Bergelson (2025), who found local host adaptation in 3/5 P. syringae pathovars but only 1/5 locally dominant. [src: plant_microbiome_ecotypes]

### Species-level validation of marker cohorts

The report replaced its 92.7% genus-level agreement, which was circular because cohorts are defined from marker presence. The new check is a curated panel of 18 model organisms with experimentally confirmed phenotypes: 7 beneficial, 7 pathogenic and 4 neutral. [src: plant_microbiome_ecotypes] All 18 were present in the refined cohort data. [src: plant_microbiome_ecotypes]

Categorical assignment was uninformative at species level. All 14 beneficial and pathogenic species were assigned to the single dual-nature class. [src: plant_microbiome_ecotypes] All 4 neutral controls were misclassified: E. coli K-12 as dual-nature [src: plant_microbiome_ecotypes], M. tuberculosis as dual-nature [src: plant_microbiome_ecotypes], D. radiodurans as beneficial [src: plant_microbiome_ecotypes] and T. thermophilus as pathogenic. [src: plant_microbiome_ecotypes] The report attributes the neutral errors to marker generality. Flagella, secretion, chemotaxis and biofilm markers overlap with beneficial or pathogenic markers in all bacteria. [src: plant_microbiome_ecotypes] An earlier 77.8% relaxed accuracy (14/18) is rejected as tautological. Counting dual-nature as correct for both classes cannot fail for dual-nature assignments. [src: plant_microbiome_ecotypes]

The only discriminative signal is continuous. The pathogenicity ratio n_pathogen / (n_pgp + n_pathogen) is lower in known beneficial species (median 0.50) than in known pathogenic species (median 0.60). The test gave Mann-Whitney U = 9, p = 0.027, on N = 7 vs 7. [src: plant_microbiome_ecotypes] PGP is plant growth promoting. The report calls this a small effect at a small sample size, though statistically consistent. [src: plant_microbiome_ecotypes] It advises treating the cohort labels as a coarse screen, not a species-level classifier. [src: plant_microbiome_ecotypes] See [[concepts/dual-nature-plant-associated-bacteria-and-the-validity-of-marker-based-cohorts]]. A stronger follow-up panel would add near-pure beneficial organisms (Methylobacterium extorquens) and near-pure pathogens (Xylella fastidiosa). [src: plant_microbiome_ecotypes]

### Provenance

The 5-species notebook 12_subclade_og_analysis.ipynb is kept for figure provenance. 13_validation_pfam_subclade.ipynb holds the genome-ID fix. [src: plant_microbiome_ecotypes] The full scan (item 19) is implemented in `notebooks/_run_subclade_full_scan.py`. [src: plant_microbiome_ecotypes] The host × subclade analysis is in `notebooks/_run_h6_host_subclade.py`. [src: plant_microbiome_ecotypes] Both are dated 2026-04-25. Outputs are `data/subclade_full_scan.csv`, `data/h6_host_subclade_full.csv` and `data/species_subclade_definitions_full.csv`. [src: plant_microbiome_ecotypes]

## Key Findings: Phase 2b: Adversarial-review corrections (H0, H1, H3, H5, H7 revised) (2)

This part of the report covers Phase 2b, where an adversarial review forced re-tests of the host-specificity (H6/H7), phylogenetic-control and genome-size claims. Within-species subclade segregation exists but is limited to a few genera. [src: plant_microbiome_ecotypes] The phylogenetic re-analysis leaves three markers robust at species level. [src: plant_microbiome_ecotypes] The novel ortholog-group (OG) associations survive genome-size control. [src: plant_microbiome_ecotypes]

### Within-species subclade segregation and host

Segregation of plant association by subclade occurs in *Xanthomonas* and *Pseudomonas*, plus *Mesorhizobium* and *Agrobacterium*. Twelve testable species show no such clustering. [src: plant_microbiome_ecotypes] The full scan is stored in data/h6_host_subclade_full.csv and underlies the revised H6 verdict. [src: plant_microbiome_ecotypes] Genome-level subclade assignments exist for the 18 species with phylogenetic data. [src: plant_microbiome_ecotypes] See [[concepts/within-species-subclade-segregation-of-plant-association-and-host-specialization]].

- *Xanthomonas campestris*: 46/47 of genomes in subclade 2 are on Brassica, p = 2.7×10⁻¹² raw / 3.3×10⁻¹¹ Bonferroni-within / Bonferroni-across. [src: plant_microbiome_ecotypes]
- *Xanthomonas vasicola*: 47/52 in subclade 0 are on *Zea mays*, p = 1.4×10⁻¹¹ / 1.7×10⁻¹⁰. [src: plant_microbiome_ecotypes]
- The report calls both results biologically expected. It describes *X. campestris* pv. campestris as the canonical Brassica pathogen and *X. vasicola* pv. vasculorum as a known maize/sugarcane pathogen. [src: plant_microbiome_ecotypes]
- *Ralstonia solanacearum* passes BH-FDR (Benjamini-Hochberg false discovery rate) but not Bonferroni-across: p = 5.9×10⁻³ within / 1.8×10⁻² q-BH. [src: plant_microbiome_ecotypes]

The limit: 47 species lack phylogenetic-tree coverage. The report says the true effect across all 65 plant-associated species with ≥20 genomes cannot be estimated until GTDB tree coverage in the KBase Data Lakehouse improves. [src: plant_microbiome_ecotypes]

### Phylogenetic control of plant-association markers

Three methods gave a three-tier result for 14 markers. The original NB10 statsmodels genus-level logit failed to converge for 0/14 markers. [src: plant_microbiome_ecotypes] NB14 used an L1-penalized Logit (scikit-learn, saga, C=1.0) with top-20 genus dummies, log₁₀(genome_size) and a 100-replicate bootstrap. [src: plant_microbiome_ecotypes] In it, 9/14 markers had bootstrap 95% CIs (confidence intervals) excluding zero. [src: plant_microbiome_ecotypes] The report cautions that L1 bootstrap CIs are biased near zero and that 100 replicates is small. [src: plant_microbiome_ecotypes]

The review flagged the L1 result as suggestive rather than confirmatory. Issue C1 was closed with a genus-cluster-robust GLM (generalized linear model), described as a pragmatic frequentist analogue of a species-scale phylogenetic generalized linear mixed model. [src: plant_microbiome_ecotypes] It was an unpenalized binomial GLM with top-10 phylum dummies, log₁₀(genome_size) and 7,555 genus clusters across 24,554 species. [src: plant_microbiome_ecotypes] 8/14 markers survived BH-FDR q < 0.05 with |coef| > 0.2, and 13 of 14 agreed with the L1 verdict. [src: plant_microbiome_ecotypes] The one disagreement was IAA biosynthesis: L1 coef = 0.61 was significant, while the cluster-robust coef = −0.09, p = 0.82 was not. The report calls this an L1 shrinkage-near-zero artifact. [src: plant_microbiome_ecotypes]

Within-genus shuffling permutes plant labels within each genus. It preserves genus-level plant-association rates and compares the observed Fisher odds ratio with the null distribution. [src: plant_microbiome_ecotypes] Results are stored in data/regularized_phylo_control.csv, data/sensitivity_shuffle.csv and data/c1_cluster_robust.csv. [src: plant_microbiome_ecotypes]

The cluster-robust GLM results follow, as coefficient, odds ratio (OR), 95% CI and BH-FDR q [src: plant_microbiome_ecotypes]:

- acc_deaminase: coef 2.08, OR 8.01, CI [4.19, 15.32], q 2.1×10⁻⁹ [src: plant_microbiome_ecotypes]
- t3ss: coef 1.00, OR 2.71, CI [1.94, 3.80], q 2.6×10⁻⁸ [src: plant_microbiome_ecotypes]
- nitrogen_fixation: coef 1.00, OR 2.71, CI [1.54, 4.78], q 1.3×10⁻³ [src: plant_microbiome_ecotypes]
- phenazine: coef 0.75, OR 2.12, CI [1.69, 2.64], q 5.9×10⁻¹⁰ [src: plant_microbiome_ecotypes]
- cwde_cellulase: coef 0.63, OR 1.87, CI [1.46, 2.40], q 2.5×10⁻⁶ [src: plant_microbiome_ecotypes]
- phosphate_solubilization: coef 0.52, OR 1.68, CI [1.20, 2.35], q 4.8×10⁻³ [src: plant_microbiome_ecotypes]
- cwde_pectinase: coef 0.46, OR 1.59, CI [1.25, 2.01], q 3.4×10⁻⁴ [src: plant_microbiome_ecotypes]
- effector: coef 0.30, OR 1.35, CI [1.09, 1.67], q 1.2×10⁻² [src: plant_microbiome_ecotypes]
- Not significant: dapg_biocontrol, coef −0.02, OR 0.98, CI [0.41, 2.33], q 0.96 [src: plant_microbiome_ecotypes]
- Not significant: t4ss, coef −0.02, OR 0.98, CI [0.72, 1.34], q 0.96 [src: plant_microbiome_ecotypes]
- Not significant: hydrogen_cyanide, coef −0.04, OR 0.96, CI [0.52, 1.76], q 0.96 [src: plant_microbiome_ecotypes]
- Not significant (labeled an L1 false positive): iaa_biosynthesis, coef −0.09, OR 0.91, CI [0.40, 2.06], q 0.96 [src: plant_microbiome_ecotypes]
- Not significant: siderophore, coef −0.33, OR 0.72, CI [0.44, 1.17], q 0.26 [src: plant_microbiome_ecotypes]
- Not significant: acetoin_butanediol, coef −0.38, OR 0.69, CI [0.46, 1.03], q 0.11 [src: plant_microbiome_ecotypes]

The report groups these into tiers:

- **Tier 1 (3 markers):** nitrogen fixation, ACC (1-aminocyclopropane-1-carboxylate) deaminase and T3SS (type III secretion system) are robust at species level. They survive cluster-robust inference and within-genus permutation. [src: plant_microbiome_ecotypes]
- **Tier 2 (5 markers):** phenazine, CWDE (cell wall degrading enzyme) cellulase, CWDE pectinase, phosphate solubilization and effector pass the cluster-robust GLM but fail within-genus shuffling. The report reads them as genus-acquired cassette-level signals, not species-level distinguishers. [src: plant_microbiome_ecotypes]
- **Tier 3 (6 markers):** DAPG biocontrol, T4SS (type IV secretion system), hydrogen cyanide, IAA biosynthesis, siderophore and acetoin/butanediol are not significant in any test. [src: plant_microbiome_ecotypes]

This three-tier breakdown supersedes the earlier "9/17 survive L1" framing. [src: plant_microbiome_ecotypes] A full phylogenetic GLMM on the GTDB tree would be stronger. Its 25K × 25K dense covariance matrix is intractable in memory. [src: plant_microbiome_ecotypes] See [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]].

### Genome-size control of novel OGs

The earlier Phase 2b novel-OG control used a prevalence-based Bernoulli simulation. The adversarial review flagged it as circular, and a real per-species OG matrix from NB03 replaced it. [src: plant_microbiome_ecotypes] Each of 50 per-species presence vectors was regressed on is_plant, log₁₀(genome_size) and top-10 phylum dummies. The regression covered 22,384 species with complete covariates: 1,134 plant-associated and 21,250 non-plant. [src: plant_microbiome_ecotypes] It used unpenalized statsmodels Logit with Wald inference and BH-FDR across 50 OGs. [src: plant_microbiome_ecotypes]

After control, 48 of 50 OGs (96%) kept a positive plant-association coefficient with |coef| > 0.2 and BH-FDR q < 0.05. [src: plant_microbiome_ecotypes] Controlled odds ratios for the top 10 ranged from 4.4 (COG5516) to 6.6 (COG1845, cytochrome oxidase ctaE). q-values were as small as 10⁻⁹⁶ (COG3569). [src: plant_microbiome_ecotypes] The genome-size coefficient was strongly positive (median 3.4 on the log₁₀ scale). It did not explain away the plant effect, and both coefficients were large and positive together. [src: plant_microbiome_ecotypes] The report therefore closes C4: novel OGs survive genome-size confounding. [src: plant_microbiome_ecotypes]

The limit: models converged for 48/50 OGs. COG2351 and COG5343 had singular design matrices, likely from perfect separation by a phylum dummy. Their raw prevalence gaps were 62% vs 23% and 64% vs 21%. [src: plant_microbiome_ecotypes] The report reads these failures as numerical, not biological, because the raw plant signal is 3× higher. [src: plant_microbiome_ecotypes]

### Genome-size gradient in dual-nature species

Among plant-associated species in the refined cohort, the dual-nature rate was 54% in the bottom genome-size quartile versus 87% in the top three quartiles. [src: plant_microbiome_ecotypes] The report states that ~33% of dual-nature species shift to neutral under genome-size normalization. It concludes that the headline 78.7% dual-nature rate masks a real, observational genome-size gradient. [src: plant_microbiome_ecotypes] See [[concepts/dual-nature-plant-associated-bacteria-and-the-validity-of-marker-based-cohorts]].

## Key Findings: Phase 2b: Adversarial-review corrections (H0, H1, H3, H5, H7 revised) (3)

This part of the report shows how adversarial-review controls changed several earlier results. Most marker-level plant-association signals did not survive a within-genus shuffle. [src: plant_microbiome_ecotypes] The Phase 1 compartment effect shrank from R² = 0.527 to 0.071, and the report judges the residual effect real. [src: plant_microbiome_ecotypes] The genus-pair complementarity effect size was mostly a formula artifact. [src: plant_microbiome_ecotypes] A Pfam-versioning query failure returned zero rows for exact IDs, and an audit found 12 of 22 marker Pfams absent from bakta_pfam_domains. [src: plant_microbiome_ecotypes]

### Within-genus plant-label shuffle

Only 3 of 15 testable markers survived the shuffle: nitrogen fixation (perm p < 0.001) [src: plant_microbiome_ecotypes], ACC (1-aminocyclopropane-1-carboxylate) deaminase (perm p < 0.001) [src: plant_microbiome_ecotypes], and T3SS (type III secretion system; perm p = 0.005). [src: plant_microbiome_ecotypes] The other 12 failed: phenazine, IAA biosynthesis, CWDE (cell wall degrading enzyme) cellulase, CWDE pectinase, effector, DAPG biocontrol, hydrogen cyanide, siderophore, acetoin/butanediol, phosphate solubilization, T4SS (type IV secretion system) and phytotoxin. Their enrichments are consistent with reshuffling labels within genus. [src: plant_microbiome_ecotypes]

The report reads most marker-level signals as genus-scale, not species-scale. Marker presence does not reliably separate plant-associated from non-plant species within genera. [src: plant_microbiome_ecotypes] The three species-level markers are the nif nitrogen-fixation operon, the ACC deaminase enzyme and the hrp/hrc T3SS structural cluster. [src: plant_microbiome_ecotypes] The report says this does not invalidate the H1/H2 compartment and architecture findings. It does mean the 78.7% dual-nature rate and the compartment-specific marker enrichments should be read as genus-level genomic backgrounds, not species-level evidence of plant adaptation. [src: plant_microbiome_ecotypes]

Two caveats limit the shuffle. It used n = 200 permutations, which is under-resolved for p ≤ 0.005, so T3SS is marginal. [src: plant_microbiome_ecotypes] No multiple-testing correction was applied across 15 markers. A Bonferroni α = 0.0033 would demote T3SS but keep nitrogen fixation and ACC deaminase significant. [src: plant_microbiome_ecotypes] The report relates the approach to phylogenetic permulations, which combine phylogenetic simulation and permutation to get unbiased empirical p-values when standard nulls are confounded. [src: plant_microbiome_ecotypes] It names a permulation-style test against the full GTDB tree as the stricter follow-up. [src: plant_microbiome_ecotypes]

### H1: compartment effect after sensitivity and decomposition

Excluding the top-3 genome-rich species per compartment cut the original NB04 Phase 1 25-marker PERMANOVA (permutational multivariate analysis of variance) R² from 0.527 to 0.072, an 86% loss. [src: plant_microbiome_ecotypes] The report then separated location shift from dispersion heterogeneity. It ran PERMDISP (permutational analysis of multivariate dispersions) and db-RDA on all 607 root, rhizosphere and phyllosphere species, with the refined 17-marker v2 panel and Jaccard distance. [src: plant_microbiome_ecotypes]

PERMANOVA gave pseudo-F = 23.2, p = 0.001 (999 permutations) and R² = 0.071. [src: plant_microbiome_ecotypes] PERMDISP detected dispersion heterogeneity, F = 15.6, p = 0.001. [src: plant_microbiome_ecotypes] db-RDA gave a location-only R² of 0.0595 (permutation p = 0.001), which is 84% of the total PERMANOVA R². [src: plant_microbiome_ecotypes]

| Compartment | Mean centroid distance |
|---|---|
| Root (tightest) | 0.452 [src: plant_microbiome_ecotypes] |
| Phyllosphere (intermediate) | 0.503 [src: plant_microbiome_ecotypes] |
| Rhizosphere (most variable) | 0.528 [src: plant_microbiome_ecotypes] |

The full 607-species v2 result (0.071) matches NB14's exclude-top-3 result (0.072). The report therefore attributes the gap from 0.527 to the marker panel and genome-count distribution, not to sample size. [src: plant_microbiome_ecotypes] It calls the original 0.527 an inflated-magnitude artifact of the Phase 1 panel and a few genome-rich species that dominated the distance matrix. [src: plant_microbiome_ecotypes] The residual 0.071 is judged real: about 84% genuine centroid shift and 16% dispersion heterogeneity. [src: plant_microbiome_ecotypes] The H1 verdict is "weakly supported", because the location shifts are significant but small (~6% of variance). [src: plant_microbiome_ecotypes] Results are in data/sensitivity_results.csv, data/h1_dbrda_results.csv and data/h1_compartment_dispersions.csv. [src: plant_microbiome_ecotypes]

### H3: complementarity effect size corrected

NB06's Cohen's d = −7.54 for co-occurring versus random genus pairs was implausibly large. Its denominator was the SD (standard deviation) of permutation means, which shrinks toward zero. NB14 instead divides by the raw pair-level SD. [src: plant_microbiome_ecotypes] Recomputing NB06's max-aggregated complementarity with NB14's formula gave d ≈ −0.43, essentially identical to the prevalence-weighted d = −0.39. [src: plant_microbiome_ecotypes] The report attributes the 20× reduction in apparent magnitude to ~90% formula change and ~10% aggregation change. [src: plant_microbiome_ecotypes]

Max-aggregation scores binary pathway presence per genus. Prevalence-weighting uses the fraction of species with the pathway. [src: plant_microbiome_ecotypes] Switching between them reduced |d| from ≈0.43 to 0.39, a ≈10% effect. [src: plant_microbiome_ecotypes] Co-occurring genus pairs remain slightly less complementary than random pairs (permutation p < 0.001). This is consistent with redundancy-driven assembly (Louca et al. 2018). [src: plant_microbiome_ecotypes] H3 therefore remains not supported, since the redundancy conclusion is robust to aggregation choice. [src: plant_microbiome_ecotypes] The real effect is small but stable (|d| ≈ 0.4), not dramatic. [src: plant_microbiome_ecotypes] The analysis is in 14_deferred_controls.ipynb and data/complementarity_v2.csv. [src: plant_microbiome_ecotypes]

### Pfam versioning and the silent-gap audit

The Phase 1 NB02 query used exact Pfam IDs and returned zero rows, because bakta_pfam_domains stores versioned IDs such as PF00771.22. [src: plant_microbiome_ecotypes] Re-running with LIKE patterns on the 10 Phase 2b marker Pfams recovered 19,364 domain hits across 7,962 species. [src: plant_microbiome_ecotypes] Five of the 10 produced hits. [src: plant_microbiome_ecotypes]

| Pfam | Hits | Species | % core |
|---|---|---|---|
| Nitrogenase NifH PF00142 | 6,632 [src: plant_microbiome_ecotypes] | 4,040 | 32.4% |
| Cellulase GH5 PF00150 | 6,898 [src: plant_microbiome_ecotypes] | 3,234 | 25.9% |
| Pectate lyase 3 PF12708 | 4,149 [src: plant_microbiome_ecotypes] | 2,283 | 24.6% |
| Pectate lyase PF00544 | 1,115 [src: plant_microbiome_ecotypes] | 546 | 20.8% |
| T6SS VgrG PF05943 | 570 [src: plant_microbiome_ecotypes] | 343 | 10.9% |

The remaining five returned 0 hits. [src: plant_microbiome_ecotypes]

A full audit of all 22 marker Pfams queried across NB02 and NB10 was stored in data/pfam_bakta_ips_audit.csv. [src: plant_microbiome_ecotypes] It found 12 of the 22 completely absent from bakta_pfam_domains despite being abundant in interproscan_domains. [src: plant_microbiome_ecotypes] The silent-gap set includes T3SS Pfams with these InterProScan hit counts: PF00771 (18.6K) [src: plant_microbiome_ecotypes], PF01313 (13.6K) [src: plant_microbiome_ecotypes], PF01514 (15.0K) [src: plant_microbiome_ecotypes], PF02579 (16.8K) [src: plant_microbiome_ecotypes] and PF04610 (15.6K). [src: plant_microbiome_ecotypes]

## Key Findings: Phase 2b: Adversarial-review corrections (H0, H1, H3, H5, H7 revised) (4)

This part of the report covers the adversarial-review corrections of Phase 2b. It audits Pfam annotation coverage, re-tests statistical controls, and closes gaps between the research plan and what was executed. [src: plant_microbiome_ecotypes]

### Pfam annotation gap in bakta_pfam_domains

The audit found 12/22 project marker Pfams silently missing from `bakta_pfam_domains`, mostly secretion-system T3SS/T4SS/T6SS markers. InterProScan has them all. [src: plant_microbiome_ecotypes] See [[entities/bakta-pfam-domains]], [[entities/interproscan-domain-annotation]] and [[concepts/reference-database-table-choice-and-pfam-versioning-in-lakehouse-queries]].

The silent-gap Pfams, with their InterProScan hit counts, were:

| System | Pfam (InterProScan hits) |
|---|---|
| T3SS | PF07916 (8.4K) [src: plant_microbiome_ecotypes]; PF09599 (0.3K) [src: plant_microbiome_ecotypes]; PF01312 (22.0K) [src: plant_microbiome_ecotypes] |
| T4SS | PF03135 (11.0K) [src: plant_microbiome_ecotypes]; PF03743 (17.5K) [src: plant_microbiome_ecotypes] |
| T6SS | PF05936, Hcp tube (7.5K) [src: plant_microbiome_ecotypes]; PF04183 (7.5K) [src: plant_microbiome_ecotypes] |

The 10 marker Pfams that are present in bakta, mostly nitrogen fixation, CWDEs and a few others, returned only 10–35% of the InterProScan hit count. They are therefore systematically undercounted but non-zero. [src: plant_microbiome_ecotypes] The report proposes that bakta uses a reduced "core" Pfam HMM profile set, while InterProScan uses the full Pfam-A release. [src: plant_microbiome_ecotypes]

The gap did not affect the main pipelines. NB10 already used `interproscan_domains` (`signature_acc`) for T3SS, T4SS, T6SS and CWDE markers. The report therefore treats its 280,193-hit recovery as correct and the refined cohort assignments as unaffected. [src: plant_microbiome_ecotypes] Phase 1 NB02's bakta-only Pfam query had returned zero hits and fell back to gene-name keyword matching, which is also unaffected. [src: plant_microbiome_ecotypes]

NB13 Cell 3's Pfam LIKE recovery confirmed, rather than expanded, the InterProScan numbers for secretion-system Pfams. [src: plant_microbiome_ecotypes] For nitrogen fixation and CWDEs it did add markers: 4,217 species gained at least one new marker. [src: plant_microbiome_ecotypes] These were 2,872 species for nitrogen fixation [src: plant_microbiome_ecotypes], 1,082 for CWDE pectinase [src: plant_microbiome_ecotypes] and 811 for CWDE cellulase. [src: plant_microbiome_ecotypes] These are cases where bakta and InterProScan diverge and InterProScan missed some that bakta found. [src: plant_microbiome_ecotypes] The report notes that NifH's higher core-genome fraction (32.4%) versus the CWDEs (21–26%) is consistent with the H2 pattern. [src: plant_microbiome_ecotypes] See [[entities/bacterial-nitrogen-fixation-nif-genes]].

For future work, the report recommends treating `bakta_pfam_domains` as a supplement to, not a substitute for, `interproscan_domains`. It also recommends cross-checking any Pfam-based query against the InterProScan table before concluding that functions are missing. [src: plant_microbiome_ecotypes] The analysis is in notebook 13_validation_pfam_subclade.ipynb. [src: plant_microbiome_ecotypes]

### Statistical validity checks

Several corrections were made. Some of them narrowed claims.

- **Marker associations.** A genus-cluster-robust GLM kept 8/14 markers at q<0.05 with proper Wald CIs. One marker, iaa_biosynthesis, was an L1 false positive. [src: plant_microbiome_ecotypes] Combined with the within-genus shuffle (3/15), the report sorted markers into 3 species-level, 5 cassette-level and 6 not-robust associations. [src: plant_microbiome_ecotypes]
- **PERMANOVA.** PERMDISP was significant, so the report treats PERMANOVA R² as an upper bound. [src: plant_microbiome_ecotypes] In NB14, excluding the top-3 species per compartment reduced R² from 0.527 to 0.072 (86% loss), leaving a small residual effect. [src: plant_microbiome_ecotypes] See [[entities/permanova]].
- **Validation.** NB13 replaced a tautological relaxed-accuracy validation with a continuous pathogen-ratio Mann-Whitney test, p=0.027 (N=7+7). [src: plant_microbiome_ecotypes] The categorical cohort was uninformative at species level. [src: plant_microbiome_ecotypes] Species-level validation superseded the earlier genus-level validation. [src: plant_microbiome_ecotypes]
- **Plant-enriched OGs.** After controlling for phylum and log₁₀(genome_size), 48/50 OGs kept a positive plant coefficient at BH-FDR q<0.05. The top-10 controlled OR was 4.4–6.6. [src: plant_microbiome_ecotypes] The 2 that did not fit failed from singular matrices, not biological rejection. [src: plant_microbiome_ecotypes] The dual-nature rate was 54% in the bottom genome-size quartile and 87% in the top. The report calls this an observational genome-size gradient. [src: plant_microbiome_ecotypes]
- **Complementarity.** Prevalence-weighted aggregation with a consistent Cohen's d formula reduced the effect size by about 10%, with direction unchanged. Most of the change from −7.54 to −0.39 came from the formula change, not the aggregation change. [src: plant_microbiome_ecotypes]
- **Genome-ID fix.** The NB13 plumbing fix matched 1306/1306 genomes and recovered 599 plant genomes. [src: plant_microbiome_ecotypes] Downstream H7 support remained weak, in 1/5 species, after these checks. [src: plant_microbiome_ecotypes]

### Terminology and documented limits

"Novel OGs" was overstated and was reframed as "enriched gene families". [src: plant_microbiome_ecotypes] The report documents T3SS's dual interpretation through context-dependent classification [src: plant_microbiome_ecotypes], and scale-dependent mobilome signals through genus-versus-genome discussion. [src: plant_microbiome_ecotypes] Only 80.7% of NMDC genera matched. Sensitivity analysis of that loss is deferred to future work. [src: plant_microbiome_ecotypes] The issue dispositions are tied to notebooks 13_validation_pfam_subclade, 14_deferred_controls and 15_final_synthesis. [src: plant_microbiome_ecotypes]

### Closing plan-versus-execution gaps

Four planned-versus-executed gaps from the original research plan were closed in commit `8f9086e`. [src: plant_microbiome_ecotypes] The report states that all four are formally closed and the plan is fully reconciled with execution. [src: plant_microbiome_ecotypes]

- NB04's genus-level logistic-regression cell called bare `logit` although the import was `statsmodels.formula.api as smf`. The cell was rerouted to a markdown note pointing to NB14's cluster-robust GLM as the canonical Phase 2b answer, and the original code was preserved. [src: plant_microbiome_ecotypes]
- The formal re-check of the target of ≥5 PGP-only genera in NMDC for the C-score analysis gave 0 PGP-dominant, 3 pathogen-dominant and 66 dual-or-mixed genera. Verification #12 was not met, and H3 is unchanged. [src: plant_microbiome_ecotypes]
- The NB15 deliverable `genus_dossiers_v2.csv` was produced with 30 top plant-associated genera × 23 columns. It integrates refined cohorts, cluster-robust marker survivors, MGnify mobilome/BGC and species-level H7/H6 significance. [src: plant_microbiome_ecotypes] *Xanthomonas* was the lone genus with both H7 phylogenetic segregation and H6 host specialization at the genomic level. [src: plant_microbiome_ecotypes]
- NB13 was re-scoped from co-occurrence network expansion to validation, Pfam and subclade fixes. Adversarial review had found higher-priority methodological issues. [src: plant_microbiome_ecotypes] The `complementarity_v2.csv` item was run in NB14 Cell 5, closing H3's I1 issue. [src: plant_microbiome_ecotypes] The remaining sub-items were deferred as exploratory enhancements on which the H3 verdict does not depend. [src: plant_microbiome_ecotypes]

See also [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]] and [[concepts/domain-based-marker-detection-and-annotation-method-bias]].

## Results: Genome Census (NB01)

This part of the report covers the first three notebooks. NB01 built the genome census, NB02 searched for marker genes, and NB03 tested ortholog-group (OG) associations with plant status. Together they define the plant cohort and show that raw OG associations are close to saturated by taxonomy. [src: plant_microbiome_ecotypes]

### Plant-association census (NB01)

Plant association was assigned to 293,059 GTDB r214 genomes from three sources. NCBI isolation_source regex matching was the primary source. [src: plant_microbiome_ecotypes] Cross-validation against the ncbi_env EAV table upgraded 695 genomes. [src: plant_microbiome_ecotypes] BacDive isolation records identified 2,482 plant strains but gave 0 new upgrades. [src: plant_microbiome_ecotypes] Species-level classification used majority vote with mean confidence 0.88. [src: plant_microbiome_ecotypes]

The census found 1,136 plant-associated species and 7,995 plant-associated genomes. It also found 25,375 known non-plant species and 285,064 known non-plant genomes. [src: plant_microbiome_ecotypes]

| Compartment | Species | Genomes |
|---|---|---|
| Root | 292 [src: plant_microbiome_ecotypes] | 2,446 [src: plant_microbiome_ecotypes] |
| Rhizosphere | 160 [src: plant_microbiome_ecotypes] | 941 [src: plant_microbiome_ecotypes] |
| Phyllosphere | 157 [src: plant_microbiome_ecotypes] | 1,334 [src: plant_microbiome_ecotypes] |
| Endophyte | 29 [src: plant_microbiome_ecotypes] | 291 [src: plant_microbiome_ecotypes] |
| Plant_other | 498 [src: plant_microbiome_ecotypes] | 2,983 [src: plant_microbiome_ecotypes] |

Rhizobia dominate the root compartment: Rhizobium has 47 species, Mesorhizobium 45 and Bradyrhizobium 41. [src: plant_microbiome_ecotypes] The phyllosphere is dominated by Sphingomonas (16 species), Methylobacterium (13) and Pseudomonas_E (13). [src: plant_microbiome_ecotypes] Pseudomonas_E is the only genus with significant presence across all compartments. [src: plant_microbiome_ecotypes]

### Marker-gene search (NB02)

NB02 searched a curated set of 91 marker genes (39 plant growth promoting (PGP), 44 pathogenic, 9 colonization). It used bakta annotations, Pfam domains, KEGG orthologs (KOs) and product descriptions. [src: plant_microbiome_ecotypes] The search found 588,098 marker gene clusters across 25,660 species. [src: plant_microbiome_ecotypes]

No Pfam domain hits were found, likely because of the query format in bakta_pfam_domains. Classification therefore relied on gene name, KO and product keyword matches. [src: plant_microbiome_ecotypes]

The most prevalent functional categories, by cluster count, were:
- type VI secretion system (T6SS) products: 80,324 [src: plant_microbiome_ecotypes]
- chemotaxis: 69,986 [src: plant_microbiome_ecotypes]
- quorum sensing: 57,201 [src: plant_microbiome_ecotypes]
- type III secretion system (T3SS) products: 52,247 [src: plant_microbiome_ecotypes]
- type IV secretion system (T4SS): 48,145 [src: plant_microbiome_ecotypes]

Among PGP functions, the most common were phosphate solubilization (23,876 clusters), phenazine (12,727), biofilm (7,512) and nitrogen fixation (6,139). [src: plant_microbiome_ecotypes]

### OG enrichment (NB03)

Server-side aggregation of 93M eggNOG annotations gave OG-level prevalence for 5,671 OGs that passed a 5% prevalence filter. [src: plant_microbiome_ecotypes] Fisher's exact tests with Benjamini-Hochberg false discovery rate (BH-FDR) correction found 94.2% of tested OGs (5,341/5,671) significantly associated with plant status. [src: plant_microbiome_ecotypes]

The report reads this near-saturation as genome-wide compositional differences between plant-associated and non-plant bacteria. It does not read it as plant-specific functional enrichment, because the test effectively detects taxonomic divergence. It treats the phylum-controlled subset as the meaningful signal. [src: plant_microbiome_ecotypes]

The top enriched OGs, with odds ratios (OR), were COG3569 (8.92), COG1764 (9.29), COG5343 (7.74), COG0654 (12.66) and COG1845 (14.47). [src: plant_microbiome_ecotypes] All 50 top OGs survived phylum-level logistic regression with 28 large phyla as fixed effects. [src: plant_microbiome_ecotypes] However, all of these models showed convergence warnings, likely from quasi-separation when some phyla are entirely plant-associated or entirely non-plant. The report therefore treats the p-values and odds ratios as approximate. [src: plant_microbiome_ecotypes]

## Results: Cohort Synthesis (NB07)

This part of the report profiles plant compartments, the genomic architecture of marker cohorts, co-occurrence complementarity, and 30 plant-associated genus dossiers. [src: plant_microbiome_ecotypes] Compartment enrichment was significant in 69 of 96 tests, but it lacks genus-level phylogenetic control. [src: plant_microbiome_ecotypes] The PGP–pathogen exclusion test could not be run with useful power. [src: plant_microbiome_ecotypes]

### Compartment enrichment and GapMind

Fisher's exact tests across 96 marker×compartment combinations found 69 significant (q<0.05). [src: plant_microbiome_ecotypes] The planned genus-level logistic-regression phylogenetic control was not completed because of a code error (an undefined `logit` import). The H1 compartment enrichments are therefore not phylogenetically controlled beyond the PERMANOVA (permutational multivariate analysis of variance) test itself. [src: plant_microbiome_ecotypes] See [[concepts/compartment-specific-functional-differentiation-of-plant-associated-bacteria]].

GapMind gave 0% core-level pathway completeness across all compartments. The report suggests its core-level threshold is too stringent for this broad taxonomic comparison. [src: plant_microbiome_ecotypes]

### Genomic architecture of cohorts

The report defines the genome-wide baseline as the fraction of all gene clusters, across all pangenome species, classified as core by their own species pangenomes. [src: plant_microbiome_ecotypes] All chi-square tests against the baseline were significant (p≈0). [src: plant_microbiome_ecotypes]

| Cohort | Core % | Singleton % | Clusters |
|---|---|---|---|
| Beneficial | 64.6 [src: plant_microbiome_ecotypes] | 20.7 [src: plant_microbiome_ecotypes] | 60,590 [src: plant_microbiome_ecotypes] |
| Colonization | 66.6 [src: plant_microbiome_ecotypes] | 20.8 [src: plant_microbiome_ecotypes] | 153,092 [src: plant_microbiome_ecotypes] |
| Pathogenic | 45.2 [src: plant_microbiome_ecotypes] | 31.0 [src: plant_microbiome_ecotypes] | 374,416 [src: plant_microbiome_ecotypes] |
| Genome-wide baseline | 46.8 [src: plant_microbiome_ecotypes] | 35.3 [src: plant_microbiome_ecotypes] | — |

A per-species Mann-Whitney U test of beneficial versus pathogenic core fractions, for species with ≥3 markers of each type, gave a complementary species-level view. [src: plant_microbiome_ecotypes] The report used 986,464 transposase/integrase singleton clusters (722,674 transposase + 263,790 integrase) as its horizontal gene transfer (HGT) co-occurrence proxy. [src: plant_microbiome_ecotypes] See [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]] and [[concepts/mobile-elements-and-horizontal-transfer-of-plant-interaction-genes]].

### Co-occurrence complementarity and the C-score test

The NMDC taxonomy bridge matched 260 of 322 genera (80.7%) to GTDB. [src: plant_microbiome_ecotypes] All 69 genera in 348 soil/rhizosphere samples had GapMind data across 80 pathways. [src: plant_microbiome_ecotypes] The 1,048 co-occurring genus pairs had mean complementarity of 10.72. A richness-preserving permutation null (1,000 iterations) gave 12.74±0.27, so observed complementarity was below the null. [src: plant_microbiome_ecotypes] See [[concepts/functional-redundancy-versus-complementarity-among-co-occurring-genera]].

The C-score analysis of PGP (plant growth promoting) versus pathogen exclusion was not feasible. The NMDC co-occurrence data held 0 PGP-dominant and 2 pathogen-dominant genera, and the other 67 were dual-nature. [src: plant_microbiome_ecotypes] The Phase 2b re-test on refined cohorts found 0 PGP-dominant, 3 pathogen-dominant and 66 dual-or-mixed genera among the 69. [src: plant_microbiome_ecotypes] Dual-nature genera dominate under both the Phase 1 25-marker and Phase 2 17-marker panels. The report therefore concludes the test is structurally underpowered in this dataset, not a marker-panel artifact. [src: plant_microbiome_ecotypes] Verification #12 (≥5 PGP-only genera) is documented as NOT MET. [src: plant_microbiome_ecotypes] See [[concepts/dual-nature-plant-associated-bacteria-and-the-validity-of-marker-based-cohorts]].

### Cohort scoring

The composite score weighted PGP markers (40%), core fraction (20%), complementarity (15%), metabolic breadth (10%) and a pathogen penalty (15%). [src: plant_microbiome_ecotypes] Adaptive thresholds, defined as the median of non-zero scores, classified species into four cohorts. [src: plant_microbiome_ecotypes]

### Genus dossiers

Thirty plant-associated genera were profiled in detail. [src: plant_microbiome_ecotypes] The dossiers show that these genera nearly universally carry both PGP and pathogenic markers. [src: plant_microbiome_ecotypes] The refreshed dossier file has 30 top genera × 23 columns. It includes refined cohorts, the continuous PGP ratio, top-3 PGP and pathogen markers, genus-scale cluster-robust GLM (generalized linear model) survivors, MGnify profiles, and species-level H7/H6 significance. [src: plant_microbiome_ecotypes] Soil-biome MGnify data were available for 19/30 genera. [src: plant_microbiome_ecotypes]

The PGP ratio is sum(n_pgp) / sum(n_pgp + n_pathogen) across plant-associated species. Values <0.5 indicate a genus richer in pathogen markers, such as Xanthomonas at 0.28 and Chryseobacterium at 0.23. [src: plant_microbiome_ecotypes] Cluster-robust markers survive the cluster-robust GLM at q < 0.05 BH-FDR (Benjamini-Hochberg false discovery rate). [src: plant_microbiome_ecotypes] MGnify BGC (biosynthetic gene cluster) counts come only from the soil biome, and "—" means the genus is absent from MGnify soil. [src: plant_microbiome_ecotypes]

Four of the 30 genera contain at least one species with significant subclade × plant-association segregation: Pseudomonas_E (P. avellanae), Mesorhizobium (sp002294985), Xanthomonas (X. campestris and X. vasicola) and Agrobacterium (A. pusense). [src: plant_microbiome_ecotypes] Xanthomonas is the only genus with species showing both H7 subclade and H6 host segregation (X. campestris × Brassica, X. vasicola × Zea mays). The report concludes that strain-level plant adaptation there is both phylogenetically structured and host-specialized. [src: plant_microbiome_ecotypes] See [[concepts/within-species-subclade-segregation-of-plant-association-and-host-specialization]]. Each dossier genus in the table is assigned a dual-nature cohort. [src: plant_microbiome_ecotypes]

| Genus | Plant-assoc. species | PGP ratio | MGnify soil BGCs | H7 species | H6 pair |
|---|---|---|---|---|---|
| Pseudomonas_E | 82 [src: plant_microbiome_ecotypes] | 0.53 [src: plant_microbiome_ecotypes] | 424 [src: plant_microbiome_ecotypes] | P. avellanae [src: plant_microbiome_ecotypes] | — |
| Rhizobium | 52 [src: plant_microbiome_ecotypes] | 0.34 [src: plant_microbiome_ecotypes] | 39 [src: plant_microbiome_ecotypes] | — | — |
| Mesorhizobium | 47 [src: plant_microbiome_ecotypes] | 0.52 [src: plant_microbiome_ecotypes] | 14 [src: plant_microbiome_ecotypes] | M. sp002294985 [src: plant_microbiome_ecotypes] | — |
| Bradyrhizobium | 44 [src: plant_microbiome_ecotypes] | 0.49 [src: plant_microbiome_ecotypes] | 488 [src: plant_microbiome_ecotypes] | — | — |
| Streptomyces | 35 [src: plant_microbiome_ecotypes] | 0.44 [src: plant_microbiome_ecotypes] | 593 [src: plant_microbiome_ecotypes] | — | — |
| Microbacterium | 19 [src: plant_microbiome_ecotypes] | 0.50 [src: plant_microbiome_ecotypes] | 84 [src: plant_microbiome_ecotypes] | — | — |
| Sphingomonas | 19 [src: plant_microbiome_ecotypes] | 0.42 [src: plant_microbiome_ecotypes] | 33 [src: plant_microbiome_ecotypes] | — | — |
| Methylobacterium | 17 [src: plant_microbiome_ecotypes] | 0.41 [src: plant_microbiome_ecotypes] | unavailable [src: plant_microbiome_ecotypes] | — | — |
| Paraburkholderia | 14 [src: plant_microbiome_ecotypes] | 0.49 [src: plant_microbiome_ecotypes] | 61 [src: plant_microbiome_ecotypes] | — | — |
| Curtobacterium | 13 [src: plant_microbiome_ecotypes] | 0.40 [src: plant_microbiome_ecotypes] | 10 [src: plant_microbiome_ecotypes] | — | — |
| Xanthomonas | 12 [src: plant_microbiome_ecotypes] | 0.28 [src: plant_microbiome_ecotypes] | unavailable [src: plant_microbiome_ecotypes] | X. campestris; X. vasicola [src: plant_microbiome_ecotypes] | X. campestris × Brassica; X. vasicola × Zea mays [src: plant_microbiome_ecotypes] |
| Rathayibacter | 11 [src: plant_microbiome_ecotypes] | 0.43 [src: plant_microbiome_ecotypes] | unavailable [src: plant_microbiome_ecotypes] | — | — |
| Chryseobacterium | 11 [src: plant_microbiome_ecotypes] | 0.23 [src: plant_microbiome_ecotypes] | 8 [src: plant_microbiome_ecotypes] | — | — |
| Frankia | 10 [src: plant_microbiome_ecotypes] | 0.60 [src: plant_microbiome_ecotypes] | unavailable [src: plant_microbiome_ecotypes] | — | — |
| Agrobacterium | 10 [src: plant_microbiome_ecotypes] | 0.32 [src: plant_microbiome_ecotypes] | unavailable [src: plant_microbiome_ecotypes] | A. pusense [src: plant_microbiome_ecotypes] | — |

Cluster-robust markers differ by genus. Pseudomonas_E, Mesorhizobium, Bradyrhizobium and Paraburkholderia carry ACC, cellulase, pectinase, effector, phenazine, phosphate-sol and T3SS. Mesorhizobium, Bradyrhizobium and Paraburkholderia also carry N-fix. [src: plant_microbiome_ecotypes] Rhizobium has the same set plus N-fix. [src: plant_microbiome_ecotypes] Curtobacterium has only cellulase, pectinase and phenazine. [src: plant_microbiome_ecotypes] Xanthomonas has cellulase, pectinase, effector, phenazine, phosphate-sol and T3SS. [src: plant_microbiome_ecotypes]

### Mechanism hypotheses

The report rates nitrogen fixation (nifHDK) and siderophore iron acquisition as high-confidence mechanism hypotheses for the beneficial cohort. [src: plant_microbiome_ecotypes] It rates T3SS effector injection and cell wall degradation (CWDE, cell wall degrading enzyme) as high confidence for the pathogenic cohort. [src: plant_microbiome_ecotypes] ACC deaminase stress relief and biocontrol antimicrobials (DAPG/phenazine) are medium confidence for the beneficial cohort. [src: plant_microbiome_ecotypes]

## Results; Interpretation

This part of the report interprets its results against the literature. It treats the plant-association signal as real but partly confounded by phylogeny. [src: plant_microbiome_ecotypes] It also flags where its results conflict with earlier studies, as the sections below show.

### Phylogenetic confounding

The report partially rejects the null that functional differences between plant-associated and non-plant species are explained by phylogeny alone. [src: plant_microbiome_ecotypes] In NB03, all 50 top-enriched orthologous groups (OGs) kept significance after controlling for 28 phyla as fixed effects, though odds ratios (OR) fell. [src: plant_microbiome_ecotypes] For COG3569 the OR fell from 8.92 to 6.01. [src: plant_microbiome_ecotypes] See [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]].

Finer control failed. Family-level logistic regression (NB08) found too little within-family variation for all 10 OGs tested, which the report reads as plant association being clustered by family. [src: plant_microbiome_ecotypes] The planned genus-level fixed effects were not run because of computational constraints. [src: plant_microbiome_ecotypes] The report concludes that enrichment is real but partly confounded by phylogeny. It cannot say whether the genes cause plant association or whether plant-associated clades simply retain them. [src: plant_microbiome_ecotypes] It proposes phylogenetic independent contrasts or phylogenetically informed mixed models to resolve this. [src: plant_microbiome_ecotypes]

### Compartment filtering and known biology

The report reads the compartment-specific enrichment (R²=0.53) as consistent with plant compartments acting as ecological filters. [src: plant_microbiome_ecotypes] Several specific results match known biology:

- Root species were enriched in ACC deaminase (OR=69), which the report links to ethylene modulation in root colonization. [src: plant_microbiome_ecotypes]
- T3SS was enriched in root species (OR=65.6) and phyllosphere species (OR=10.7). [src: plant_microbiome_ecotypes]
- Sphingomonas and Methylobacterium dominated the phyllosphere, matching Knief et al.'s identification of methylotrophy as its defining function. [src: plant_microbiome_ecotypes]
- Rhizobium, Mesorhizobium and Bradyrhizobium were root-dominant, well-characterized nitrogen fixers. The report says this validates its compartment classification pipeline. [src: plant_microbiome_ecotypes]

### Core versus accessory genes

Plant growth-promoting (PGP) genes were 64.6% core versus 45.2% for pathogenic genes (p=3.4e-125). The report says this supports H2 and aligns with Levy et al. (2018), who found plant-associated bacteria enriched in core metabolic functions but depleted in mobile elements. [src: plant_microbiome_ecotypes] The report suggests beneficial functions become fixed in the core genome under strong positive selection once acquired. [src: plant_microbiome_ecotypes] It reads pathogenic functions (T3SS, effectors, toxins) as more dynamic, consistent with host-pathogen arms-race coevolution. [src: plant_microbiome_ecotypes]

This contrasts with Loper et al. (2012), who found Pseudomonas biocontrol traits largely accessory. [src: plant_microbiome_ecotypes] The report suggests taxonomic scope may explain it: its analysis spans 25,660 species, while Loper et al. studied 10 strains within a single species group. [src: plant_microbiome_ecotypes]

### Redundancy rather than complementarity

The report rejects H3: co-occurring genera show functional redundancy, not complementarity. It calls this consistent with Louca et al. (2018). [src: plant_microbiome_ecotypes] It reads the Cohen's d of -7.54 as strong redundancy. [src: plant_microbiome_ecotypes] It proposes that environmental filtering for the same functions, not niche partitioning, is likely the dominant assembly mechanism. [src: plant_microbiome_ecotypes]

Puente-Sanchez et al. (2024) found that complementarity can drive genome streamlining in some contexts. [src: plant_microbiome_ecotypes] The report says its result does not contradict this, because complementarity may exist at finer metabolic resolution than its 80 GapMind pathway categories can detect. [src: plant_microbiome_ecotypes]

### Dual nature

The report calls it perhaps the most striking finding that 60–85% of plant-associated bacteria carry both PGP and pathogenic markers. [src: plant_microbiome_ecotypes] It relates this to Drew et al.'s parasite-mutualist continuum, which rests on shared molecular machinery, and to Etesami's (2025) documentation of the paradoxical dual nature of PGP bacteria. [src: plant_microbiome_ecotypes] T3SS serves both pathogenic injection and beneficial symbiotic signaling, such as rhizobial Nod factor delivery. [src: plant_microbiome_ecotypes] The same T3SS delivers pathogenic effectors in Pseudomonas syringae and facilitates beneficial nodulation signaling in Rhizobium. [src: plant_microbiome_ecotypes] The report therefore says that classifying bacteria as beneficial or pathogenic from genomic markers alone is insufficient. [src: plant_microbiome_ecotypes] It says host genotype, environmental conditions and community composition determine the outcome (Osayande et al. 2025). [src: plant_microbiome_ecotypes]

The report rates two mechanism hypotheses for the dual-nature cohort at medium confidence: context-dependent T6SS, and PGP plus secretion-system co-occurrence. [src: plant_microbiome_ecotypes]

### Plant-enriched gene families

The report presents the 50 OGs enriched after phylogenetic control as candidates for previously unrecognized plant-interaction functions. [src: plant_microbiome_ecotypes] It cites Saati-Santamaria et al. (2025), who found numerous uncharacterized genes upregulated during root colonization. [src: plant_microbiome_ecotypes] It also cites Zhou et al. (2025), who reported that >99% of phyllosphere antimicrobial peptides were previously uncharacterized. [src: plant_microbiome_ecotypes] However, Phase 2 annotation (NB09) found all 50 OGs to be well-characterized proteins, none hypothetical. [src: plant_microbiome_ecotypes]

The report reads the dominant themes (electron transport, iron-sulfur biosynthesis, ion transport) as enhanced metabolic competitiveness in the rhizosphere rather than plant-specific signaling. [src: plant_microbiome_ecotypes] It singles out the high-affinity cytochrome oxidases COG1845 and COG0843. It says cbb3-type terminal oxidases enable respiration in microaerobic root nodules and xylem, which explains why energy metabolism genes are among the strongest plant-association signals. [src: plant_microbiome_ecotypes]

### Mobilome: an apparent contradiction

The MGnify mobilome analysis (NB11) found significantly more mobile elements per genome in plant-associated genera than in non-plant genera (3.7 vs 2.8, p=1.49×10⁻⁵). [src: plant_microbiome_ecotypes] The report says this genus-level result appears to contradict the genome-level findings of Levy et al. (2018) and Bograd et al. (2025), who report fewer mobile elements in plant-associated genomes. [src: plant_microbiome_ecotypes]

The report hypothesizes a scale-dependent resolution. At the genome level, plant-adapted strains may shed mobile elements as beneficial functions stabilize into the core genome, consistent with the 64.6% core fraction for PGP genes. At the genus level, the diversity of accessory elements across strains inflates the aggregate count. [src: plant_microbiome_ecotypes] It notes that Rajabal et al. (2024) describe the rhizosphere as a hotspot for horizontal gene transfer (HGT), consistent with its genus-level enrichment. [src: plant_microbiome_ecotypes]

## Interpretation: Limitations

This part of the report compares pangenome-derived plant classifications with MGnify metagenomic detection. It also places the Phase 2 results against the literature and states the limits that remain. The cross-validation shows low agreement between the two sources, and the report treats the subclade null result as support for accessory-gene-driven plant adaptation. [src: plant_microbiome_ecotypes]

### Cross-validation against MGnify

Agreement between the two sources was low: 11.7% Jaccard between pangenome isolation-source plant classification and MGnify metagenomic rhizosphere detection. [src: plant_microbiome_ecotypes] The sources measure different things. Pangenome classification uses cultivation metadata about where a strain was isolated, whereas MGnify captures where a genome is detected metagenomically. [src: plant_microbiome_ecotypes] See [[concepts/isolation-metadata-versus-metagenomic-cross-validation-of-plant-associated-taxa]].

The report suggests that the 390 pangenome-only plant genera likely include opportunistic soil bacteria isolated from plants rather than rhizosphere specialists. [src: plant_microbiome_ecotypes] It also suggests that the 341 MGnify-only rhizosphere genera may include uncultured lineages absent from GTDB. [src: plant_microbiome_ecotypes] Both are interpretations, not tested results.

Seventeen genera were consistently present across tomato, maize and barley rhizospheres, including Pseudomonas_E, Streptomyces, Variovorax and Acidovorax. The report proposes them as a candidate core rhizosphere microbiome for crop-agnostic biocontrol. [src: plant_microbiome_ecotypes] The report states that integrating the KBase Data Lakehouse pangenome data (293K genomes) with the MGnify catalogue (20,473 species, 4 biomes) independently validates T3SS (type III secretion system) enrichment in rhizosphere, mobilome patterns and core rhizosphere genera. [src: plant_microbiome_ecotypes]

### Subclade null result and accessory genome

The report found no subclade-level segregation of plant-associated genomes (H7). [src: plant_microbiome_ecotypes] It calls this consistent with Melnyk et al. (2019), who showed that plant-lifestyle transitions in Pseudomonas are driven by convergent gain and loss of accessory genomic islands rather than core-genome phylogeny. [src: plant_microbiome_ecotypes] The report reads this as support for plant adaptation through horizontal acquisition of accessory gene clusters in any phylogenetic background, rather than vertical inheritance along clonal lineages. [src: plant_microbiome_ecotypes] Its practical conclusion is that strain-level prediction of plant-association potential needs accessory genome profiling, not core-genome phylotyping. [src: plant_microbiome_ecotypes] See [[concepts/within-species-subclade-segregation-of-plant-association-and-host-specialization]].

### Agreement with the literature

- H1 compartment-specific signatures align with Trivedi et al. (2020) and Knief et al. (2012). The report extends them to a genome-scale analysis of 1,136 species. [src: plant_microbiome_ecotypes]
- The H2 core/accessory pattern is consistent with Levy et al. (2018). It contradicts Loper et al. (2012) for biocontrol traits, likely because of the report's broader taxonomic scope. [src: plant_microbiome_ecotypes]
- The functional redundancy result (H3 rejected) is consistent with Louca et al. (2018) and Puente-Sanchez et al. (2024). [src: plant_microbiome_ecotypes]
- The partial H4 HGT (horizontal gene transfer) proxy results align with Ghaly et al. (2024), who found integrons as HGT hotspots in plant-associated bacteria. [src: plant_microbiome_ecotypes] They also align with Pinto-Carbo et al. (2016), who demonstrated HGT between obligate plant symbionts. [src: plant_microbiome_ecotypes]
- Dual-nature prevalence corroborates Drew et al. (2021) and Etesami (2025). The report calls its analysis the first genome-scale quantification, across 25,660 species. [src: plant_microbiome_ecotypes]
- Phase 2 mobilome enrichment in plant-associated genera aligns with Rajabal et al. (2024). It contrasts with the genome-level findings of Levy et al. (2018) and Bograd et al. (2025). The report says the resolution likely depends on scale, genus versus genome. [src: plant_microbiome_ecotypes]
- MGnify shows 2× T3SS enrichment in rhizosphere versus soil. [src: plant_microbiome_ecotypes] The report calls this consistent with Gonzalez-Vallina et al. (2024) and Tampakaki (2022), who found T3SS widespread in both beneficial and pathogenic plant bacteria. [src: plant_microbiome_ecotypes]
- Cytochrome oxidase is enriched in plant-associated species. [src: plant_microbiome_ecotypes] The report calls this consistent with Preisig et al. (1996), who characterized high-affinity cbb3 oxidase as essential for symbiotic nitrogen fixation in microaerobic root nodules. [src: plant_microbiome_ecotypes]

### Claimed contributions

The report calls its classification of 25,660 bacterial species into plant-interaction cohorts, by pangenome-scale marker-gene analysis, the first systematic one at this scale. Earlier studies examined tens to hundreds of genomes. [src: plant_microbiome_ecotypes] Across the full bacterial tree of life, the beneficial gene core fraction (64.6%) exceeds the pathogenic one (45.2%), with bootstrap confidence intervals. [src: plant_microbiome_ecotypes] Phase 2 extended this to 50 novel OGs (ortholog groups) with 60.1–83.1% core fractions. [src: plant_microbiome_ecotypes]

The report finds that 60–85% of plant-associated species carry both PGP (plant growth promoting) and pathogenic markers. It says this challenges the binary classification used in most PGPB screening programs. [src: plant_microbiome_ecotypes] The refined 17-marker panel with KEGG module gating kept the pattern at 78.7% after removing ubiquitous bacterial functions. [src: plant_microbiome_ecotypes] See [[concepts/dual-nature-plant-associated-bacteria-and-the-validity-of-marker-based-cohorts]].

The report reports genus-level mobilome enrichment in MGnify (p=1.49×10⁻⁵) and contrasts it with genome-level mobile element depletion in the literature. [src: plant_microbiome_ecotypes] It suggests that plant adaptation involves HGT-mediated accessory gene acquisition followed by core genome stabilization. [src: plant_microbiome_ecotypes]

### Caveats

- **Compartment metadata:** Classification relies on NCBI isolation_source metadata of variable quality and coverage. [src: plant_microbiome_ecotypes] Only 7,995 of 293,059 genomes (2.7%) had plant-associated annotations. [src: plant_microbiome_ecotypes] Endophyte species (n=29) fell below the 30-species threshold. [src: plant_microbiome_ecotypes]
- **Pfam versioning:** The bakta_pfam_domains table stores versioned Pfam IDs (identifiers) such as PF13629.12 rather than bare accessions such as PF00771. This caused zero hits in the original NB02 query. [src: plant_microbiome_ecotypes] NB13 Cell 3 fixed it with a LIKE 'PF00771%' pattern. [src: plant_microbiome_ecotypes] The marker set remains literature-curated. [src: plant_microbiome_ecotypes]
- **GapMind:** Core-level completeness scoring gave 0% across all compartments, which suggests the threshold is too stringent for broad taxonomic comparisons. [src: plant_microbiome_ecotypes] The threshold remains an open question. [src: plant_microbiome_ecotypes] NB06's max-aggregated species-to-genus scores inflated the complementarity Cohen's d to -7.54. [src: plant_microbiome_ecotypes] The NB14 prevalence-weighted re-test gave d = -0.39, credible in magnitude and in the same direction. [src: plant_microbiome_ecotypes]
- **Confounder control:** The plan specified genus-level fixed effects. Phase 1 used phylum-level control because of computational cost, and NB10's statsmodels genus-level logit failed for 0/14 markers. [src: plant_microbiome_ecotypes] NB14's scikit-learn L1-regularized logit, with top-20 genus dummies and log₁₀(genome size) covariates, converged. For 9/17 markers the bootstrap 95% CIs (confidence intervals) excluded zero. [src: plant_microbiome_ecotypes]
- **Sensitivity and permutation:** Excluding the top-3 species per compartment cut PERMANOVA (permutational multivariate analysis of variance) R² from 0.527 to 0.072, still significant at p = 0.001. [src: plant_microbiome_ecotypes] Within-genus label shuffling left only 3/15 markers (nitrogen fixation, ACC deaminase, T3SS) surviving the strict permutation null. [src: plant_microbiome_ecotypes] ACC is 1-aminocyclopropane-1-carboxylate. Phylogeny versus ecology variance decomposition remains future work. [src: plant_microbiome_ecotypes] The NB04 code-error issue is documented. Compartment profiling uses PERMANOVA rather than logit as the primary test. [src: plant_microbiome_ecotypes]
- **HGT proxies:** Without GeNomad mobile-element annotations, HGT was assessed indirectly. Strong transposase co-occurrence but lower-than-baseline singleton enrichment shows the limits of proxies. [src: plant_microbiome_ecotypes]
- **Dual nature:** Presence of both PGP and pathogenic markers does not confirm simultaneous expression. Transcriptomic or experimental validation is needed to separate lifestyle flexibility from annotation artifacts, such as T6SS serving inter-bacterial competition. [src: plant_microbiome_ecotypes] Negative controls (NB08) classified non-plant Escherichia, Salmonella and Clostridioides as 100% dual-nature. [src: plant_microbiome_ecotypes]

## Interpretation: Limitations (2)

This part of the report lists the limits on its results. These include confounding by non-specific markers and genome size, dispersion effects, model convergence failures, database coverage gaps and identifier mismatches. It also records which limits later notebooks resolved and which remain open. [src: plant_microbiome_ecotypes]

### Marker specificity and dual-nature rates

The dual-nature classification is inflated by markers that are not plant-specific. Negative controls (NB08) classified *Staphylococcus* as 98% dual-nature. [src: plant_microbiome_ecotypes] The report explains that flagella, chemotaxis, biofilm, quorum sensing and secretion-system markers are ubiquitous across bacteria. [src: plant_microbiome_ecotypes] Together with a genome-size confound, this means the NB02 dual-nature rate of 60.3% substantially overestimates genuine plant-adapted duality. [src: plant_microbiome_ecotypes] The NB07 composite score gave 25.2% dual-nature, but that rate depends on arbitrary scoring weights. [src: plant_microbiome_ecotypes] See [[concepts/dual-nature-plant-associated-bacteria-and-the-validity-of-marker-based-cohorts]].

### Genome size

Genome size, measured as gene cluster count, correlates moderately with total marker count (r=0.44, p<1e-300), so larger genomes accumulate more markers by chance. [src: plant_microbiome_ecotypes] Plant species in the bottom genome-size quartile were 54% dual-nature, against 87% in the top three quartiles. The 78.7% figure therefore masks a gradient. [src: plant_microbiome_ecotypes] In NB14, all 50 novel OGs (ortholog groups) kept positive plant-association coefficients with genome size as a covariate. [src: plant_microbiome_ecotypes] See [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]].

### Compartment effect: location versus dispersion

The compartment effect is supported, but its PERMANOVA effect size may be inflated by dispersion differences. NB08 PERMDISP (permutational analysis of multivariate dispersions) found significant dispersion heterogeneity between cohorts (H=33.12, p=3.0e-7). The PERMANOVA R²=0.53 may therefore partly reflect variance differences. [src: plant_microbiome_ecotypes] Fisher enrichment tests still support the compartment effect (69/96 significant), but the PERMANOVA effect size should be treated as an upper bound. [src: plant_microbiome_ecotypes]

A later db-RDA on plant-compartment functional profiles gave a location-only R² of 0.060, which is 84% of total PERMANOVA R² (0.071). [src: plant_microbiome_ecotypes] PERMDISP confirmed dispersion heterogeneity (F=15.6, p=0.001). [src: plant_microbiome_ecotypes] The report concludes that the residual effect is small but real and mostly location, not dispersion. [src: plant_microbiome_ecotypes] See [[concepts/compartment-specific-functional-differentiation-of-plant-associated-bacteria]].

### Phylogenetic confounding and model fitting

Of the tested OGs, 94.2% (5,341/5,671) were significantly associated with plant status. This reflects genome-wide compositional differences rather than plant-specific enrichment. [src: plant_microbiome_ecotypes] Only the 50 OGs that survive phylogenetic control are candidate plant-interaction genes. [src: plant_microbiome_ecotypes] Separately, among plant-enriched OGs, 48/50 survive per-species phylum plus genome-size regression at q<0.05. [src: plant_microbiome_ecotypes]

NB10 genus-level fixed-effects logistic regression for the 14 refined markers failed to converge in every model (0/14). [src: plant_microbiome_ecotypes] NB14 resolved this with L1-penalized logistic regression (scikit-learn, saga solver) using top-20 genus dummies and log₁₀(genome size). [src: plant_microbiome_ecotypes] A genus-cluster-robust GLM (generalized linear model) gave proper Wald CIs (confidence intervals), and 8/14 markers were significant at q<0.05. [src: plant_microbiome_ecotypes] It agrees with L1 on 13/14 markers and disconfirms one L1 false positive, iaa_biosynthesis. [src: plant_microbiome_ecotypes] This supports separate tiers of species-level, cassette-level and not-robust signal. [src: plant_microbiome_ecotypes]

A full PGLMM with GTDB-tree-derived random-effect covariance remains theoretically stronger. Its 25K x 25K dense covariance matrix is intractable, so genus-level cluster-robust GLM serves as the practical analogue. [src: plant_microbiome_ecotypes] PGLMMs with the full GTDB tree remain future work. [src: plant_microbiome_ecotypes]

### Cross-validation and data coverage

The NMDC taxonomy bridge matched 260/322 genera (80.7%) and lost 62 (19.3%). [src: plant_microbiome_ecotypes] The effect on the complementarity hypothesis (H3) is unknown. If the lost genera include key complementary partners, the observed redundancy signal could be artifactual. [src: plant_microbiome_ecotypes] See [[concepts/functional-redundancy-versus-complementarity-among-co-occurring-genera]].

Pangenome-derived and MGnify-derived plant-associated genera overlap by only 11.7% (Jaccard). [src: plant_microbiome_ecotypes] The report attributes this to isolation metadata versus metagenomic detection rather than classification error. It says the low concordance still limits the strength of the cross-validation. [src: plant_microbiome_ecotypes] See [[concepts/isolation-metadata-versus-metagenomic-cross-validation-of-plant-associated-taxa]].

BacDive cross-validation found 2,482 plant-related strains but added 0 genome upgrades beyond ncbi_env. This indicates complete overlap between the two metadata sources for the plant-associated genome set. [src: plant_microbiome_ecotypes]

MGnify BGC (biosynthetic gene cluster), mobilome and defense annotations exist only for the soil biome, not for the tomato, maize or barley rhizosphere biomes. [src: plant_microbiome_ecotypes] The mobilome and BGC analyses therefore compare soil-dwelling plant-associated genera with soil-dwelling non-plant genera, not rhizosphere with bulk soil. [src: plant_microbiome_ecotypes]

### Subclade analyses and identifier plumbing

NB12's null H7 result came from genome identifier (ID) format mismatches. The phylogenetic tree table used bare NCBI accessions, and the environment metadata used GTDB-prefixed IDs. [src: plant_microbiome_ecotypes] NB13 fixed this by prepending GB_ to GCA_ accessions and RS_ to GCF_ accessions. This gave 100% overlap (1306/1306 genomes) and recovered 599 plant-associated genomes. [src: plant_microbiome_ecotypes] See [[concepts/join-key-validity-and-identifier-format-mismatches]].

The full 65-species H7 scan found 5/17 testable species significant after Bonferroni correction. [src: plant_microbiome_ecotypes] Three of those five were also Cochran-valid. [src: plant_microbiome_ecotypes] The H6 host × subclade extension found robust pathovar-host segregation in 2/9 species: *X. campestris* × Brassica and *X. vasicola* × *Zea mays*. [src: plant_microbiome_ecotypes] Coverage limits this scan. 47/65 candidate species lack phylogenetic tree coverage in the KBase Data Lakehouse, which the report calls a database limitation rather than a methodology issue. [src: plant_microbiome_ecotypes] Only 18 species have tree data. [src: plant_microbiome_ecotypes] See [[concepts/within-species-subclade-segregation-of-plant-association-and-host-specialization]].

### Annotation audit and review status

The Pfam audit found 12/22 marker Pfams absent from bakta_pfam_domains but present in interproscan_domains, mostly secretion-system components. [src: plant_microbiome_ecotypes] NB10 already uses InterProScan, so the report says its biological claims are unaffected. [src: plant_microbiome_ecotypes]

The report says the five issues from the 2026-04-24 adversarial review, which were only partly addressed in Phase 2b, were all closed on 2026-04-25. [src: plant_microbiome_ecotypes] See [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]].

## Interpretation: Adversarial Revision Results (NB08)

NB08 reports twelve additional analyses run to address concerns raised in adversarial review. [src: plant_microbiome_ecotypes] The sections below group them by question. In the secretion-system and genome-size checks, the dual-nature pattern persisted. Two caveats are stated next to those results. [src: plant_microbiome_ecotypes]

### Robustness of the dual-nature classification

Reclassifying T3SS (type III secretion system), T6SS (type VI secretion system) and T2SS from "pathogenic" to "colonization" markers changed 16.4% of dual-nature species to PGP-only (plant growth promoting). [src: plant_microbiome_ecotypes] Plant-associated species still remained 86.0% dual-nature under the revised classification. The report concludes that the finding is not driven solely by secretion-system annotations. [src: plant_microbiome_ecotypes] See [[concepts/dual-nature-plant-associated-bacteria-and-the-validity-of-marker-based-cohorts]].

In the marker-driver analysis, the most prevalent pathogenic markers in dual-nature species were T6SS products (64%), T2SS (55%), T3SS products (50%) and chemotaxis (52%). [src: plant_microbiome_ecotypes] The most prevalent PGP markers were quorum sensing (49%), phenazine (34%) and flagella (40%). [src: plant_microbiome_ecotypes] Chemotaxis and flagella are general motility functions, and the report notes that they contribute substantially to the dual-nature classification. [src: plant_microbiome_ecotypes]

### Validation, genome size and prediction

In the PGP-versus-pathogen score scatter, the model organisms *B. subtilis*, *R. leguminosarum*, *B. japonicum* and *S. meliloti* cluster in the expected quadrants. [src: plant_microbiome_ecotypes] Genome size and marker count correlate moderately (r=0.44). [src: plant_microbiome_ecotypes] Genome-size normalization shifts 33% of dual-nature species to neutral. The report reads this as a meaningful effect that does not eliminate the dual-nature pattern. [src: plant_microbiome_ecotypes] See [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]].

A Random Forest classifier predicted compartment (root, rhizosphere or phyllosphere) with 64.4% accuracy from 25 binary markers. That is above the 33% random baseline but far from deterministic. [src: plant_microbiome_ecotypes] Cohort prediction reached 99.9% accuracy, but this is trivial because cohorts are defined by marker presence. [src: plant_microbiome_ecotypes]

### Horizontal transfer signal

Per-marker transposase co-occurrence showed the strongest horizontal gene transfer (HGT) signal for PGP markers. The odds ratios (OR) were DAPG biocontrol 8.75, ACC deaminase 6.43 and nitrogen fixation 3.76. [src: plant_microbiome_ecotypes] Among pathogenic markers, T4SS (OR=3.23), T6SS (OR=2.66) and effectors (OR=2.67) also showed significant enrichment. [src: plant_microbiome_ecotypes] See [[concepts/mobile-elements-and-horizontal-transfer-of-plant-interaction-genes]].

Contig co-location analysis found 498,677 marker-transposase pairs on shared contigs across 18,569 species. [src: plant_microbiome_ecotypes] T4SS had the most co-located pairs (84,411) and the closest median distance (238 genes). [src: plant_microbiome_ecotypes] Fifteen pairs were immediately adjacent at gene-number distance 1. They spanned effectors, T6SS, T3SS, quorum sensing, cellulase and T4SS, in species including *Rhizobium ecuadorense*, *Phytobacter ursingii* and *Burkholderia puraquae*. [src: plant_microbiome_ecotypes]

### Annotation of plant-enriched ortholog groups (NB09)

NB09 annotated all 50 Phase 1 plant-enriched ortholog groups (OGs) using eggNOG descriptions, InterProScan domain hits across 18 databases, Gene Ontology (GO) terms and MetaCyc pathways. [src: plant_microbiome_ecotypes] Coverage was 50/50 for eggNOG descriptions, 50/50 for InterProScan domains, 48/50 for GO terms (699 unique) and 39/50 for MetaCyc pathways. [src: plant_microbiome_ecotypes] The 1,206,652 gene clusters carrying these OGs span 14,329–16,166 species per OG. [src: plant_microbiome_ecotypes] See [[concepts/functional-characterization-of-plant-enriched-gene-families]].

By COG (clusters of orthologous groups) category, the OGs were:

- S, unknown function: 19/50 (38%). [src: plant_microbiome_ecotypes]
- C, energy production: 7/50 (14%). [src: plant_microbiome_ecotypes]
- P, inorganic ion transport: 6/50 (12%). [src: plant_microbiome_ecotypes]
- G, carbohydrate metabolism: 4/50 (8%). [src: plant_microbiome_ecotypes]
- Q, secondary metabolite biosynthesis: 3/50 (6%). [src: plant_microbiome_ecotypes]

The report suggests that the predominance of energy and ion-transport functions points to enrichment for rhizosphere nutrient-competition capabilities rather than plant-specific signaling. This is an interpretation, not a direct test. [src: plant_microbiome_ecotypes]

### Refined marker panel

The Phase 1 91-marker panel was reduced to 17 plant-specific markers. Six ubiquitous categories were removed because they had only 1.2–2.4× enrichment in plant versus non-plant species. [src: plant_microbiome_ecotypes] The removed categories were flagella, chemotaxis, T6SS, biofilm, quorum sensing and T2SS. [src: plant_microbiome_ecotypes] Module-completeness gating was applied to multi-gene systems: nitrogen fixation M00175 at ≥2 genes, T3SS M00332 at ≥3 genes and T4SS M00333 at ≥3 genes. [src: plant_microbiome_ecotypes]

InterProScan found 280,193 marker domain hits across 24,595 species. It recovered 2,804 additional species with CWDE (cell wall degrading enzyme) cellulase/pectinase domains (PF00150, PF00544) that the Phase 1 bakta-only search missed. [src: plant_microbiome_ecotypes] See [[entities/interproscan-domain-annotation]].

The refined cohort distribution covered 25,660 species. [src: plant_microbiome_ecotypes] Its cohorts were:

- Dual-nature: 12,463 species (48.6%). [src: plant_microbiome_ecotypes]
- Pathogenic: 6,272 species (24.4%). [src: plant_microbiome_ecotypes]
- Beneficial: 3,394 species (13.2%). [src: plant_microbiome_ecotypes]
- Neutral: 3,531 species (13.8%). [src: plant_microbiome_ecotypes]

Among the 1,115 plant-associated species, 878 (78.7%) were dual-nature under the refined panel. [src: plant_microbiome_ecotypes]

## Interpretation: Refined Marker Panel and Host Species (NB10)

This part of the report classifies 1,115 plant-associated species with the refined marker panel and checks it against control genera. It also parses host-plant metadata and bridges to MGnify metagenomic biomes. [src: plant_microbiome_ecotypes]

### Refined panel classification and controls

Under the refined marker panel, most plant-associated species were dual-nature. Among 1,115 plant-associated species, 108 (9.7%) were pathogenic [src: plant_microbiome_ecotypes], 94 (8.4%) were beneficial [src: plant_microbiome_ecotypes] and 35 (3.1%) were neutral. [src: plant_microbiome_ecotypes] See [[concepts/dual-nature-plant-associated-bacteria-and-the-validity-of-marker-based-cohorts]].

Positive controls behaved as expected. The share classed as beneficial or dual-nature was 97% for Rhizobium [src: plant_microbiome_ecotypes], 100% for Bradyrhizobium [src: plant_microbiome_ecotypes], 100% for Azospirillum [src: plant_microbiome_ecotypes] and 99% for Mesorhizobium. [src: plant_microbiome_ecotypes]

Negative controls improved over Phase 1. Escherichia was ubiquitously dual-nature in Phase 1 and fell to 25% PGP-only in the refined analysis. [src: plant_microbiome_ecotypes] Salmonella was 0% PGP-only [src: plant_microbiome_ecotypes], Staphylococcus 18% [src: plant_microbiome_ecotypes] and Mycobacterium 6%. [src: plant_microbiome_ecotypes]

### Host species

The report parsed 11,852 genomes with identifiable plant hosts from NCBI isolation_source. [src: plant_microbiome_ecotypes] Species-level aggregation gave 1,307 species across 19 testable hosts, each with at least 10 species. [src: plant_microbiome_ecotypes] The species counts per host were:

| Host | Species |
|---|---|
| rice | 286 [src: plant_microbiome_ecotypes] |
| Arabidopsis | 184 [src: plant_microbiome_ecotypes] |
| wheat | 122 [src: plant_microbiome_ecotypes] |
| maize | 98 [src: plant_microbiome_ecotypes] |
| soybean | 84 [src: plant_microbiome_ecotypes] |
| potato | 58 [src: plant_microbiome_ecotypes] |
| tomato | 57 [src: plant_microbiome_ecotypes] |
| sugarcane | 47 [src: plant_microbiome_ecotypes] |
| lettuce | 34 [src: plant_microbiome_ecotypes] |
| banana | 30 [src: plant_microbiome_ecotypes] |
| pepper | 25 [src: plant_microbiome_ecotypes] |
| cotton | 24 [src: plant_microbiome_ecotypes] |
| grape | 22 [src: plant_microbiome_ecotypes] |
| strawberry | 18 [src: plant_microbiome_ecotypes] |
| peanut | 17 [src: plant_microbiome_ecotypes] |
| citrus | 14 [src: plant_microbiome_ecotypes] |
| tea | 13 [src: plant_microbiome_ecotypes] |
| tobacco | 12 [src: plant_microbiome_ecotypes] |
| apple | 10 [src: plant_microbiome_ecotypes] |

### MGnify metagenomic bridge

The taxonomy bridge linked 20,473 MGnify species across 4 biomes to 1,185 pangenome genera. Of these, 9,603 MGnify species fell in matched genera. [src: plant_microbiome_ecotypes] The biomes were soil with 19,472 species in 4,229 genera [src: plant_microbiome_ecotypes], tomato rhizosphere with 579 species in 309 genera [src: plant_microbiome_ecotypes], maize rhizosphere with 336 species in 212 genera [src: plant_microbiome_ecotypes] and barley rhizosphere with 86 species in 52 genera. [src: plant_microbiome_ecotypes] See [[entities/kescience-mgnify]].

The soil mobilome analysis covered 563 pangenome genera with data. It detected 17,323 mobilome entries using ISEScan, ICEfinder and geNomad. [src: plant_microbiome_ecotypes] Element types included IS110, IS701, IS1634, IS256 and IS3 elements, plasmids, prophages, terminal inverted repeats and viral sequences. [src: plant_microbiome_ecotypes] See [[concepts/mobile-elements-and-horizontal-transfer-of-plant-interaction-genes]].

The soil biosynthetic gene cluster (BGC) analysis classified 17,608 BGCs into MiBIG categories across 579 pangenome genera with data. [src: plant_microbiome_ecotypes] The shares were:

- Polyketide, 23.1% [src: plant_microbiome_ecotypes]
- NRP, 13.9% [src: plant_microbiome_ecotypes]
- Saccharide, 13.2% [src: plant_microbiome_ecotypes]
- RiPP, 12.6% [src: plant_microbiome_ecotypes]
- Terpene, 12.7% [src: plant_microbiome_ecotypes]

Average BGC-to-MiBIG similarity scores ranged from 0.38–0.89. [src: plant_microbiome_ecotypes]

KEGG module enrichment pointed to the rhizosphere. Module M00332 (type III secretion system, T3SS) was enriched in all 3 rhizosphere biomes (22–24%) relative to soil (12.3%). [src: plant_microbiome_ecotypes]

## Interpretation; Data

### MGnify module enrichment

Five KEGG modules were 2–3× enriched in rhizosphere in the MGnify catalogue. These were M00238, M00769, M00136, M00615 and M00438. [src: plant_microbiome_ecotypes]

### Within-species subclade analysis

The initial analysis picked five species with ≥175 genomes and high plant-associated fractions. It clustered them by phylogenetic distance with agglomerative clustering. [src: plant_microbiome_ecotypes] The distance matrices came from phylogenetic_tree_distance_pairs (22.6M rows). They were used for MDS visualization and clustering. [src: plant_microbiome_ecotypes]

| Species | Genomes | Plant-associated | Subclades |
|---|---|---|---|
| X. euvesicatoria | 332 | 169 (51%) | 3 [src: plant_microbiome_ecotypes] |
| P. avellanae | 319 | 68 (21%) | 3 [src: plant_microbiome_ecotypes] |
| S. meliloti | 241 | 191 (79%) | 2 [src: plant_microbiome_ecotypes] |
| P. amygdali | 239 | 32 (13%) | 3 [src: plant_microbiome_ecotypes] |
| R. laguerreae | 175 | 139 (79%) | 2 [src: plant_microbiome_ecotypes] |

The Phase 2 pass found 0 testable subclade × plant-association enrichments in all 5 species. Bare NCBI accessions did not match GTDB-prefixed IDs, and this reduced the plant-associated subset to zero. [src: plant_microbiome_ecotypes] The Phase 2b revision (NB13) prepended `GB_`/`RS_` prefixes. This recovered 599 plant-associated genomes across the 5 species. [src: plant_microbiome_ecotypes] See [[concepts/join-key-validity-and-identifier-format-mismatches]] for the general pattern.

The full 18-species scan found that 5 of 17 testable species passed Bonferroni-corrected Fisher's exact testing. The three most robust were P. avellanae (Fisher p = 7.3×10⁻⁴), X. campestris (p = 1.0×10⁻³) and X. vasicola (p = 1.6×10⁻⁴). [src: plant_microbiome_ecotypes] The earlier 5-species draft had also flagged P. amygdali on chi² alone. That result fails Cochran's rule and the Fisher 2×2 collapse, so the Phase 2b verdict is the one that stands. [src: plant_microbiome_ecotypes] See [[concepts/within-species-subclade-segregation-of-plant-association-and-host-specialization]].

### Lakehouse tables used

- `kbase_ke_pangenome`: genome, gene_cluster, pangenome, gtdb_taxonomy_r214v1, gtdb_metadata, bakta_annotations, bakta_pfam_domains, eggnog_mapper_annotations and gapmind_pathways. These supplied core pangenome data, functional annotations and pathway predictions. [src: plant_microbiome_ecotypes]
- `kbase_ke_pangenome`: ncbi_env, for environmental metadata for genome classification. [src: plant_microbiome_ecotypes]
- `kbase_ke_pangenome`: interproscan_domains, interproscan_go and interproscan_pathways, for InterProScan domain hits, GO terms and MetaCyc pathways used in novel OG annotation (Phase 2). [src: plant_microbiome_ecotypes]
- `kbase_ke_pangenome`: phylogenetic_tree and phylogenetic_tree_distance_pairs, for within-species phylogenetic distances used in subclade clustering (Phase 2). [src: plant_microbiome_ecotypes]
- `kescience_mgnify`: species, genome, gene_mobilome, gene_bgc, genome_kegg_module and genome_cog. This is the MGnify rhizosphere/soil genome catalogue, used for mobilome, BGC and KEGG profiles (Phase 2). [src: plant_microbiome_ecotypes]
- `kescience_bacdive`: isolation, sequence_info and metabolite_utilization, for strain-level isolation source and metabolic phenotypes. [src: plant_microbiome_ecotypes]
- `nmdc_arkin`: taxonomy_features and study_table, for community ecology co-occurrence data. [src: plant_microbiome_ecotypes]

### Derived data files

The report's derived files, with row counts, are listed here.

| File | Rows | Content |
|---|---|---|
| genome_environment.csv | 293,059 | Per-genome compartment classification [src: plant_microbiome_ecotypes] |
| species_compartment.csv | 26,511 | Species-level compartment assignments by majority vote [src: plant_microbiome_ecotypes] |
| compartment_census_summary.csv | 9 | Compartment species counts [src: plant_microbiome_ecotypes] |
| ncbi_env_pivot.csv | 279,547 | NCBI environment cross-validation pivot [src: plant_microbiome_ecotypes] |
| bacdive_isolation.csv | 23,988 | BacDive isolation source records [src: plant_microbiome_ecotypes] |
| bakta_marker_hits.csv | 387,822 | Bakta gene-name marker hits [src: plant_microbiome_ecotypes] |
| pfam_marker_hits.csv | 0 | Pfam domain hits (none found) [src: plant_microbiome_ecotypes] |
| kegg_marker_hits.csv | 39,640 | KEGG KO marker hits [src: plant_microbiome_ecotypes] |
| product_marker_hits.csv | 256,269 | Product keyword marker hits [src: plant_microbiome_ecotypes] |
| marker_gene_clusters.csv | 588,098 | Consolidated marker gene clusters [src: plant_microbiome_ecotypes] |
| species_marker_matrix.csv | 25,660 | Species × functional category matrix [src: plant_microbiome_ecotypes] |
| species_cohort_markers.csv | 25,660 | Species cohort assignments (NB02) [src: plant_microbiome_ecotypes] |
| enrichment_results.csv | 5,671 | OG-level enrichment results [src: plant_microbiome_ecotypes] |
| logistic_phylo_controlled.csv | 50 | Phylo-controlled logistic regression results [src: plant_microbiome_ecotypes] |
| top50_og_species.csv | varies | Top-50 OG species distributions [src: plant_microbiome_ecotypes] |
| novel_plant_markers.csv | 50 | Novel plant-enriched OGs [src: plant_microbiome_ecotypes] |
| compartment_profiles.csv | 96 | Per-compartment marker enrichment [src: plant_microbiome_ecotypes] |
| genus_profiles.csv | 30 | Top plant-associated genus profiles [src: plant_microbiome_ecotypes] |
| gapmind_plant_species.csv | 2,213,340 | GapMind pathway predictions (plant species) [src: plant_microbiome_ecotypes] |
| pangenome_stats.csv | 27,702 | Pangenome core/singleton statistics [src: plant_microbiome_ecotypes] |
| transposase_singletons.csv | 986,464 | Transposase/integrase singleton clusters [src: plant_microbiome_ecotypes] |
| genomic_architecture.csv | 23 | Per-function genomic architecture summary [src: plant_microbiome_ecotypes] |
| nmdc_genus_abundance.csv | 40,271 | NMDC genus-level abundances [src: plant_microbiome_ecotypes] |
| nmdc_soil_file_ids.csv | 25,547 | NMDC soil/rhizosphere sample IDs [src: plant_microbiome_ecotypes] |
| gapmind_genus_pathways.csv | 658,712 | Genus-level GapMind pathway aggregation [src: plant_microbiome_ecotypes] |
| complementarity_network.csv | 2,346 | Genus-pair complementarity scores [src: plant_microbiome_ecotypes] |

## Data: Generated Data

This part of the report lists the data files the project generated. They are grouped below by the notebook (NB) stage that produced them. Row counts are as the report gives them. [src: plant_microbiome_ecotypes]

### Cohort assignments and genus dossiers

The final composite cohort assignments (`cohort_assignments.csv`) have 25,660 rows. [src: plant_microbiome_ecotypes] The refined 17-marker species matrix with KEGG gating (`species_marker_matrix_v2.csv`, NB10) and the refined cohort assignments with taxonomy and host data (`species_cohort_refined.csv`, NB10) also have 25,660 rows each. [src: plant_microbiome_ecotypes] Genus dossiers come in three versions of 30 rows each. These are the detailed dossiers, the plant/soil-filtered dossiers (NB08), and the Phase 2 refreshed dossiers (`genus_dossiers_v2.csv`). The refreshed version combines refined cohorts, cluster-robust markers, MGnify mobilome and biosynthetic gene cluster (BGC) data, and H7/H6 significance (2026-04-25, NB15 gap-2 close). [src: plant_microbiome_ecotypes] The c-score test of PGP-pathogen mutual exclusion on refined cohorts has 69 rows. It gave 0 PGP-only, 3 pathogen-only and 66 dual-or-mixed, the same pattern as Phase 1. [src: plant_microbiome_ecotypes] See [[concepts/dual-nature-plant-associated-bacteria-and-the-validity-of-marker-based-cohorts]].

### Taxonomy, BacDive and Pfam files (NB06, NB08)

The BacDive metabolite utilization records per genus (NB06 GapMind cross-validation) have 137,599 rows. [src: plant_microbiome_ecotypes] The species-level GTDB family assignments (NB08) have 27,690 rows. [src: plant_microbiome_ecotypes] The Pfam domain investigation results (NB08) have 36 rows. [src: plant_microbiome_ecotypes]

### Novel plant-enriched OGs (NB09)

NB09 produced annotation tables for the 50 plant-enriched OGs. The tables are listed below. [src: plant_microbiome_ecotypes] See [[concepts/functional-characterization-of-plant-enriched-gene-families]].

| File | Rows | Content |
|---|---|---|
| `novel_og_annotations.csv` | 50 | Aggregate functional annotations [src: plant_microbiome_ecotypes] |
| `novel_og_eggnog_annotations.csv` | 1,206,652 | eggNOG per-gene-cluster annotations [src: plant_microbiome_ecotypes] |
| `novel_og_bakta.csv` | 12,580 | Bakta gene/product annotations [src: plant_microbiome_ecotypes] |
| `novel_og_interproscan.csv` | 4,455 | InterProScan domain hits per OG [src: plant_microbiome_ecotypes] |
| `novel_og_domains.csv` | 4,455 | Consolidated per-OG domain assignments [src: plant_microbiome_ecotypes] |
| `novel_og_go_terms.csv` | 1,544 | Gene Ontology (GO) term annotations per OG [src: plant_microbiome_ecotypes] |
| `novel_og_pathways.csv` | 2,317 | MetaCyc / KEGG pathway annotations per OG [src: plant_microbiome_ecotypes] |

### Host assignment, markers and phylogenetic control (NB10)

NB10 has per-genome plant host species assignments (11,852 rows). [src: plant_microbiome_ecotypes] It also has InterProScan domain hits for marker recovery (280,193 rows) and KEGG module gene counts per species (19,665 rows). [src: plant_microbiome_ecotypes] The phylogenetic control logistic regression (`phylo_control_results.csv`, 15 rows) is recorded as 0/14 converged. [src: plant_microbiome_ecotypes] See [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]].

### MGnify files (NB11)

| File | Rows | Content |
|---|---|---|
| `mgnify_pangenome_bridge.csv` | 20,473 | MGnify species-to-GTDB taxonomy bridge [src: plant_microbiome_ecotypes] |
| `mgnify_host_specificity.csv` | 266 | Genus × rhizosphere biome presence matrix [src: plant_microbiome_ecotypes] |
| `mgnify_mobilome.csv` | 17,323 | Mobile element annotations in pangenome genera [src: plant_microbiome_ecotypes] |
| `mgnify_bgc_profiles.csv` | 8,089 | BGC profiles by genus [src: plant_microbiome_ecotypes] |
| `mgnify_kegg_biome_profiles.csv` | 2,630 | KEGG module distribution across biomes [src: plant_microbiome_ecotypes] |
| `mgnify_rhizo_vs_soil_cog.csv` | 96 | COG-category counts per biome for the rhizosphere-vs-soil contrast [src: plant_microbiome_ecotypes] |
| `mgnify_soil_bgc_summary.csv` | 13,584 | Per-genus BGC summaries from the MGnify soil biome [src: plant_microbiome_ecotypes] |

See [[concepts/mobile-elements-and-horizontal-transfer-of-plant-interaction-genes]].

### Subclade analyses (NB12, NB13, 2026-04-25)

The first subclade analysis (NB12) gave 1,306 genome-level subclade assignments and 6 subclade × plant-association enrichment tests. [src: plant_microbiome_ecotypes] The host × subclade mapping has 0 rows because the data were insufficient. [src: plant_microbiome_ecotypes] NB13 reran the analysis after a genome-ID fix. This gave 5 subclade × plant enrichment rows and 2 subclade × host rows. [src: plant_microbiome_ecotypes] The 2026-04-25 full scan covers 65 species with Bonferroni and Benjamini-Hochberg false discovery rate (BH-FDR) correction (18 rows). [src: plant_microbiome_ecotypes] It comes with genome-level subclade assignments for 18 species with phylogenetic tree data (2,414 rows) and a subclade × host plant scan for those 18 species (18 rows). [src: plant_microbiome_ecotypes] See [[concepts/within-species-subclade-segregation-of-plant-association-and-host-specialization]].

### Validation and Pfam recovery (NB13)

Species-level ground-truth validation has 18 rows. [src: plant_microbiome_ecotypes] The recovered Pfam domain hits come from a LIKE query and need Spark. The cohort impact of the recovered hits is a second file. Both have variable row counts. [src: plant_microbiome_ecotypes] A bakta_pfam_domains versus interproscan_domains coverage audit (2026-04-25) has 22 rows. [src: plant_microbiome_ecotypes] See [[concepts/domain-based-marker-detection-and-annotation-method-bias]].

### Robustness and sensitivity (NB14 and 2026-04-25)

- The L1-regularized logit for 17 markers with bootstrap confidence interval (CI) has 17 rows. [src: plant_microbiome_ecotypes]
- The cluster-robust generalized linear model (GLM), clustered by genus, for the 17 markers has 17 rows. It gives Wald CIs without L1 shrinkage. [src: plant_microbiome_ecotypes]
- The genome-size-controlled coefficients for the 50 novel OGs have 50 rows. [src: plant_microbiome_ecotypes]
- The sensitivity results (permutational multivariate analysis of variance (PERMANOVA) on a reduced marker set plus alpha-class statistics) have 1 row. The within-genus label shuffling results have 15 rows. [src: plant_microbiome_ecotypes]
- The prevalence-weighted complementarity table has 2,346 rows. [src: plant_microbiome_ecotypes]
- The H1 decomposition has 1 row. It combines PERMANOVA, permutational analysis of multivariate dispersions (PERMDISP) and db-RDA. The per-compartment mean centroid distances have 3 rows. [src: plant_microbiome_ecotypes]

### Final verdicts (NB15)

The final H0–H7 verdict table, with Phase 2b evidence, has 8 rows. [src: plant_microbiome_ecotypes]

## Supporting Evidence; Future Directions

This part of the report gives the Phase 2b closure of earlier controls, the coverage limits that remain, and the report's proposed future work. The Phase 2b controls are direct results. The future directions are proposals, not findings. [src: plant_microbiome_ecotypes]

### Phase 2b control closures

Phase 2b closed concern C1 with the genus-level cluster-robust generalized linear model (GLM), which used Wald inference and no L1 shrinkage. In it 8/14 markers were significant. [src: plant_microbiome_ecotypes] The within-genus permutation complemented it, and 3/15 markers were significant at species level. [src: plant_microbiome_ecotypes] The report calls a full phylogenetic GLMM, with random-effect covariance from the GTDB tree, the gold standard. The 25K × 25K dense covariance is intractable in memory, so sparse approximations or species subsampling are the practical path. [src: plant_microbiome_ecotypes]

The prevalence-weighted re-test (NB14) and a Cohen's d formula correction reduced the original implausible metabolic-complementarity effect from |d|=7.54 to |d|≈0.4. The redundancy direction held at pathway resolution. [src: plant_microbiome_ecotypes] The Phase 2b 65-species subclade scan resolved the genome-ID linkage and ran the 18 species that were available. [src: plant_microbiome_ecotypes]

### Coverage limits

Only 18 of 65 plant-associated species with ≥20 genomes have phylogenetic-tree distance pairs in `kbase_ke_pangenome.phylogenetic_tree_distance_pairs`. [src: plant_microbiome_ecotypes] Missing major plant-associated taxa include Bradyrhizobium japonicum, B. diazoefficiens, Mesorhizobium ciceri, Sinorhizobium medicae, Burkholderia glumae, Methylobacterium extorquens, Streptomyces scabiei, Xylella taiwanensis and Clavibacter michiganensis. [src: plant_microbiome_ecotypes] The report says expanding tree coverage would directly increase the power of within-species phylogenetic analyses. [src: plant_microbiome_ecotypes]

The endophyte compartment currently has 29 species. The report suggests more targeted isolation could allow a full four-way compartment comparison. [src: plant_microbiome_ecotypes] The horizontal gene transfer (HGT) analysis uses proxies, namely transposase/integrase singletons and MGnify mobilome aggregates. It does not use direct mobile-element annotations. [src: plant_microbiome_ecotypes]

The dual-nature classification rests on gene presence, not demonstrated expression. [src: plant_microbiome_ecotypes] All 50 novel ortholog groups (OGs) have annotated function from NB09 but lack mechanism-level proposals. [src: plant_microbiome_ecotypes] The GapMind level of 80 pathways may be too coarse for complementarity analysis. [src: plant_microbiome_ecotypes]

### Future directions proposed by the report

**Dual nature and novel OGs.** RNAseq under beneficial versus pathogenic conditions would show whether the two gene sets are co-expressed or differentially regulated. [src: plant_microbiome_ecotypes] The 17-genera core rhizosphere set (NB11) and the species-level Tier-1 markers (nitrogen fixation, ACC deaminase, type III secretion system) offer candidate organisms and gene targets. [src: plant_microbiome_ecotypes] For the top novel OGs COG3569, COG1845, COG0843 and COG0316, AlphaFold structural prediction or cross-referencing with biochemical pathway databases could give testable mechanisms. [src: plant_microbiome_ecotypes] Enrichment of the high-affinity cytochrome oxidases COG1845 and COG0843 in plant-associated species suggests microaerobic adaptation as a key niche axis. [src: plant_microbiome_ecotypes] The report proposes measuring oxygen tolerance ranges in plant-associated versus non-plant strains to test this. [src: plant_microbiome_ecotypes]

**Subclades, HGT and complementarity.** Accessory-gene presence/absence profiling as an alternative subclade definition is still outstanding, because the current method is core-phylogeny-based. [src: plant_microbiome_ecotypes] Comparing gene-content trees with species trees would identify HGT-driven incongruences. [src: plant_microbiome_ecotypes] Both need larger gene-cluster-by-genome data pulls than this project ran. [src: plant_microbiome_ecotypes] When GeNomad mobile-element predictions become available in the KBase Data Lakehouse, the report would replace the proxy-based HGT analysis with direct annotations. This would strengthen H4 conclusions and resolve the genus-versus-genome scale-dependent mobilome signal. [src: plant_microbiome_ecotypes] Reaction-level or substrate-specific complementarity analysis could reveal patterns masked by pathway-level aggregation. [src: plant_microbiome_ecotypes]

**Applications.** Genus dossiers, core rhizosphere genera and biosynthetic gene cluster profiles could inform synthetic community design for plant growth promotion, following Song et al. (2026) for Bacillus SynComs. [src: plant_microbiome_ecotypes] NB11 identified 84 NRP/siderophore-producing plant genera as prime candidates. [src: plant_microbiome_ecotypes] The NB11 host-specificity matrix identified 117 tomato-specific, 54 maize-specific and 5 barley-specific genera. [src: plant_microbiome_ecotypes] The H6 subclade × host scan also found X. campestris × Brassica and X. vasicola × maize as canonical pathovar-host segregations. [src: plant_microbiome_ecotypes] Targeted isolation of crop-specific protective genera, optionally screened against the matching H6 pathovars, would yield more effective biocontrol agents than generalist approaches. [src: plant_microbiome_ecotypes]

## Caveats and Open Work

- The 47 species without phylogenetic-tree coverage leave the true within-species effect across all 65 candidate species unestimable until the GTDB tree is more completely populated in the KBase Data Lakehouse. [src: plant_microbiome_ecotypes]
- Only 80.7% of NMDC genera matched, and sensitivity analysis of this loss was deferred to future work. [src: plant_microbiome_ecotypes]
- The 2 enriched OGs that did not fit the genome-size-controlled analysis failed from singular matrices, not biological rejection. [src: plant_microbiome_ecotypes]
- That bakta uses a reduced core Pfam HMM set is the report's proposed explanation of the annotation gap, not a tested result. [src: plant_microbiome_ecotypes]

## Slots Into

- [[concepts/compartment-specific-functional-differentiation-of-plant-associated-bacteria]]: the refined db-RDA gives location-only R² = 0.060, while most of the original 0.527 was a sampling artifact. [src: plant_microbiome_ecotypes]
- [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]]: only 3/15 markers survive within-genus shuffling. [src: plant_microbiome_ecotypes]
- [[concepts/within-species-subclade-segregation-of-plant-association-and-host-specialization]]: 5 of 17 testable species pass Bonferroni. [src: plant_microbiome_ecotypes]
- [[concepts/domain-based-marker-detection-and-annotation-method-bias]]: the proposed bakta Pfam gap. [src: plant_microbiome_ecotypes]
