---
type: "Concept"
description: "Whether root, rhizosphere and phyllosphere bacteria differ in functional marker content, including effect size, location-versus-dispersion decomposition and sensitivity to dominant genome-rich species."
sources: ["summaries/discoveries.md", "summaries/plant_microbiome_ecotypes__REPORT.md"]
---
# Compartment-specific functional differentiation of plant-associated bacteria

Root, rhizosphere and phyllosphere bacteria do differ in functional marker content, but the effect is small. An early headline of R²=0.53 was inflated by the marker panel and a few genome-rich species. [src: plant_microbiome_ecotypes] The refined analysis gives a compartment effect of about 6% of variance, and most of it is a real centroid shift. [src: plant_microbiome_ecotypes] See [[summaries/plant_microbiome_ecotypes__REPORT]] for the report behind these results.

## Literature Context

The one candidate paper is a field study of tomato, and it bears on the hub's question only partly. It used high-throughput amplicon sequencing of field-grown tomato plants. It reported a three-microhabitat partition (phyllosphere, rhizosphere and root interior) that separated host-associated communities from the environmental microbiota [PMID 41537582](https://pubmed.ncbi.nlm.nih.gov/41537582/). It then applied shotgun metagenomics to rhizosphere specimens only. That analysis identified a "microhabitat effect", defined by a set of rhizosphere-enriched functions [PMID 41537582](https://pubmed.ncbi.nlm.nih.gov/41537582/). The abstract gives no effect size, variance fraction or dispersion test for either result.

The same paper describes an Acinetobacter sp. that emerged as a dominant member of the microbiota at the plant-soil continuum. A metagenome-assembled genome (MAG, a genome reconstructed from metagenomic reads) of Acinetobacter calcoaceticus was retrieved. Reads associated with that species pointed to plant-growth-promotion traits: phosphate solubilization, siderophore production and reactive oxygen species detoxification. These traits were similarly represented across tomato genotypes [PMID 41537582](https://pubmed.ncbi.nlm.nih.gov/41537582/). The abstract reports this enrichment alongside the functional signal. It does not show that the one organism produced the compartment-level functional profile, so the two should be read as associated and not as causally linked. The functions it lists as rhizosphere-enriched are mineral nutrient mobilization, adaptation to salinity and polymicrobial communities, and antimicrobial resistance genes [PMID 41537582](https://pubmed.ncbi.nlm.nih.gov/41537582/).

The corpus finding is that root, rhizosphere and phyllosphere bacteria differ in functional marker content, but only slightly. The refined PERMANOVA gave R² = 0.071, and the location-only db-RDA gave R² = 0.060, about 84% of that. This is **consistent in direction** with the tomato study. Both find that compartment or microhabitat structures community composition and function. The comparison is qualitative only. The tomato paper is a single crop, rests on amplicon and rhizosphere shotgun data, and gives no variance partition in its abstract. The corpus instead used genome-based marker panels across 607 species. The tomato result therefore cannot confirm or refute the 6% effect size.

The tomato paper does bear on the corpus's sensitivity result, but only as a loose parallel. The corpus found that R² fell from 0.527 to 0.072 when the top-3 genome-rich species per compartment were dropped. The tomato abstract describes one dominant, enriched taxon next to a functional signal. That is the kind of situation where dominant organisms might matter, but the abstract did not test whether removing Acinetobacter changes the microhabitat effect. This remains an open question. The corpus's other claims have no support in the candidate paper. These are the PERMDISP dispersion heterogeneity, the per-marker Fisher enrichments (ACC deaminase, T3SS, nitrogen fixation) and the 3 of 15 markers that passed the within-genus permutation null. For these the corpus is novel relative to the retrieved evidence.

## The original headline and its correction

The first analysis reported that compartment explains 53% of variance in functional profiles (R²=0.53, pseudo-F=235, p=0.001). It also called compartment the dominant driver of differentiation and root the most specialized compartment. [src: discoveries] The study's interpretation section read this as consistent with plant compartments acting as ecological filters. [src: plant_microbiome_ecotypes]

The later analyses revise this. The original PERMANOVA (permutational multivariate analysis of variance) on the Phase 1 25-marker panel gave R² = 0.527. [src: plant_microbiome_ecotypes] The NB14 sensitivity analysis dropped the top-3 genome-rich species per compartment, and R² fell to 0.072, an 86% loss. The result stayed significant at p = 0.001. [src: plant_microbiome_ecotypes] The report calls the original value an inflated-magnitude artifact of the panel and a few genome-rich species. [src: plant_microbiome_ecotypes] It says most of the 0.527 was a taxonomic-sampling artifact rather than a community-wide signal. [src: plant_microbiome_ecotypes]

The full 607-species analysis with the refined panel gave R² = 0.071, which matches NB14's 0.072. The report attributes the gap from 0.527 to the marker panel and the genome-count distribution, not to sample size. [src: plant_microbiome_ecotypes]

## Location versus dispersion

The report ran PERMDISP (permutational analysis of multivariate dispersions) and db-RDA on all 607 root, rhizosphere and phyllosphere species. It used the refined 17-marker panel and Jaccard distance. The aim was to separate location shift from dispersion heterogeneity, which PERMANOVA conflates. [src: plant_microbiome_ecotypes]

- PERMANOVA gave pseudo-F = 23.2, p = 0.001 and R² = 0.071. [src: plant_microbiome_ecotypes]
- PERMDISP detected dispersion heterogeneity, with F = 15.6 and p = 0.001. [src: plant_microbiome_ecotypes]
- db-RDA on PCoA (principal coordinates analysis) scores gave a location-only R² = 0.060 (p = 0.001, 999 permutations). [src: plant_microbiome_ecotypes] A second statement of the same test gives 0.0595. [src: plant_microbiome_ecotypes]
- The location fraction was 0.060 / 0.071 = 84%. [src: plant_microbiome_ecotypes]

The report concludes that the residual effect is real. About 84% is genuine centroid shift and 16% is dispersion heterogeneity. [src: plant_microbiome_ecotypes] Root species clustered most tightly (mean centroid distance 0.452). Phyllosphere was intermediate (0.503) and rhizosphere was most variable (0.528). [src: plant_microbiome_ecotypes] The report judged hypothesis H1 weakly supported: significant location shifts of only ~6% of variance, alongside dispersion heterogeneity. [src: plant_microbiome_ecotypes]

Because PERMDISP was significant, the report treats PERMANOVA R² as an upper bound. [src: plant_microbiome_ecotypes] An earlier cohort-level PERMDISP (NB08) also found heterogeneity (H=33.12, p=3.0e-7). That result means the R²=0.53 may partly reflect variance differences. [src: plant_microbiome_ecotypes]

## Per-function enrichments

The report says the revised decomposition does not contradict the per-function enrichments. Only the headline multivariate R² was inflated. [src: plant_microbiome_ecotypes] In NB04, Fisher's exact tests found 69 of 96 marker×compartment combinations significant (q<0.05). [src: plant_microbiome_ecotypes] The report treats these tests as still supporting a compartment effect. [src: plant_microbiome_ecotypes] See [[entities/fisher-s-exact-test-with-benjamini-hochberg-fdr]].

In the original NB04 Fisher-test framework, root species were enriched in:
- ACC (1-aminocyclopropane-1-carboxylate) deaminase (OR = 69.3), the strongest single marker. OR means odds ratio. [src: discoveries, plant_microbiome_ecotypes]
- T3SS (type III secretion system) (OR = 65.6). [src: plant_microbiome_ecotypes]
- Quorum sensing (OR = 24.1). [src: plant_microbiome_ecotypes]
- Nitrogen fixation (OR = 14.5). [src: plant_microbiome_ecotypes]

Phyllosphere species were enriched in T3SS (OR=10.7). [src: plant_microbiome_ecotypes] See [[entities/acc-deaminase-acds]] and bacterial nitrogen fixation nif genes.

A within-genus label-shuffling test (NB14) found that only 3 of 15 markers survived the strict permutation null. These were nitrogen fixation, ACC deaminase and T3SS. [src: plant_microbiome_ecotypes] A Random Forest using 25 binary markers predicted compartment with 64.4% accuracy, against a 33% random baseline. The report calls this far from deterministic. [src: plant_microbiome_ecotypes] A separate cohort-prediction Random Forest reached 99.9% accuracy, but the report calls this trivial because cohorts are defined by marker presence. [src: plant_microbiome_ecotypes]

## Taxonomic composition and sampling

The genome census assigned species and genomes to compartments as follows. The report describes 1,136 plant-associated species classified across four compartments (root 292, rhizosphere 160, phyllosphere 157, endophyte 29). [src: plant_microbiome_ecotypes]
- Root: 292 species, 2,446 genomes. [src: plant_microbiome_ecotypes]
- Rhizosphere: 160 species, 941 genomes. [src: plant_microbiome_ecotypes]
- Phyllosphere: 157 species, 1,334 genomes. [src: plant_microbiome_ecotypes]
- Endophyte: 29 species, 291 genomes. [src: plant_microbiome_ecotypes]
- Plant_other: 498 species, 2,983 genomes. [src: plant_microbiome_ecotypes]
- Total plant: 1,136 species, 7,995 genomes. [src: plant_microbiome_ecotypes]

Root is dominated by rhizobia: Rhizobium (47 species), Mesorhizobium (45) and Bradyrhizobium (41). [src: plant_microbiome_ecotypes] See [[entities/bradyrhizobium]]. The report says these well-characterized nitrogen fixers validate the compartment classification pipeline. [src: plant_microbiome_ecotypes] Phyllosphere is dominated by Sphingomonas (16), Methylobacterium (13) and Pseudomonas_E (13). [src: plant_microbiome_ecotypes] The report links the Sphingomonas and Methylobacterium dominance to Knief et al.'s identification of methylotrophy as the defining phyllosphere function. [src: plant_microbiome_ecotypes] Pseudomonas_E was the only genus with significant presence in all compartments. [src: plant_microbiome_ecotypes] See [[entities/pseudomonas]]. The report says its signatures align with Trivedi et al. (2020) and Knief et al. (2012) and extend them to 1,136 species. [src: plant_microbiome_ecotypes]

## Caveats

- Compartment labels come from NCBI isolation_source metadata of variable quality and coverage. [src: plant_microbiome_ecotypes] See [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]].
- Endophyte species (n=29) fell below the 30-species threshold. [src: plant_microbiome_ecotypes] The report proposes that more targeted isolation could expand this compartment enough for a full four-way comparison. [src: plant_microbiome_ecotypes]
- The planned genus-level logistic-regression phylogenetic control failed because of an undefined `logit` import. The H1 enrichments are therefore not phylogenetically controlled beyond the PERMANOVA test itself. [src: plant_microbiome_ecotypes]

## Open Directions

- Re-run the Fisher enrichments with the genus-level logistic-regression phylogenetic control. This would test which of the 69 significant combinations survive beyond the 3 of 15 markers that passed the label-shuffling null.
- Repeat the location-versus-dispersion decomposition on each marker separately. This would show which functions drive the 84% location share.
- Validate compartment labels against metagenomic evidence. This would limit the effect of weak isolation_source metadata. See [[concepts/isolation-metadata-versus-metagenomic-cross-validation-of-plant-associated-taxa]].
- Add more endophyte genomes to pass the 30-species threshold. This would allow a four-compartment decomposition.
