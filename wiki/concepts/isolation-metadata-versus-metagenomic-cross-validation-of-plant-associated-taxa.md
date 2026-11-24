---
type: "Concept"
description: "How pangenome-based plant classification from isolation metadata compares with metagenome-derived rhizosphere and soil catalogues, including concordance, T3SS enrichment and host-specific genera."
sources: ["summaries/plant_microbiome_ecotypes__REPORT.md"]
---
# Isolation-metadata versus metagenomic cross-validation of plant-associated taxa

Pangenome-based plant classification (from isolation metadata) and metagenome-derived rhizosphere and soil catalogues agree only weakly at genus level, but they agree well on T3SS (type III secretion system) enrichment in rhizosphere. The evidence comes from one report, plant_microbiome_ecotypes, which cross-validated its census against the MGnify genome catalogue. [src: plant_microbiome_ecotypes] See also [[summaries/plant_microbiome_ecotypes__REPORT]] and [[entities/kescience-mgnify]].

## Literature Context

The candidate papers show that rhizosphere communities differ from bulk soil, but they do not test how isolation metadata compare with metagenomic catalogues. A saline-soil study of three salt-tolerant plant species found bacterial and fungal taxa enriched in rhizosphere versus non-rhizosphere soil. It also found plant growth-promoting and salt-adaptation genes more abundant in the rhizosphere, with Pseudomonas and Woeseia as core genera [PMID 41242205](https://pubmed.ncbi.nlm.nih.gov/41242205/). A transcriptome-guided study of a rhizosphere Pseudomonas found genes induced during root colonization that were more abundant in rhizosphere communities than in bulk soils. Some of these genes were more prevalent in plant-associated Pseudomonas genomes than in genomes from other environments [PMID 41345977](https://pubmed.ncbi.nlm.nih.gov/41345977/). That combination of comparative genomics and metagenomes is the same logic the corpus applies to plant-association markers.

Host and context dependence also appears in the candidates. Wheat domestication and host genotype co-shaped rhizosphere microbiomes and their metabolic functions [PMID 37004105](https://pubmed.ncbi.nlm.nih.gov/37004105/). Sugarcane tissues and rhizosphere soil carried distinct microbial communities, with Burkholderia varying across four sugarcane species [PMID 39560390](https://pubmed.ncbi.nlm.nih.gov/39560390/). In squash, 199 of 1009 bacterial genera were exclusively associated with roots under arid conditions. That result came from a small shotgun set (N = 6 rhizospheres) [PMID 34818799](https://pubmed.ncbi.nlm.nih.gov/34818799/). A pomegranate study found comparable diversity in bulk and rhizosphere soil, so rhizosphere enrichment is not universal [PMID 38805323](https://pubmed.ncbi.nlm.nih.gov/38805323/). Finally, a study of IAA (indole-3-acetic acid) degraders found 21 of 183 root isolates able to degrade IAA. It also used metagenome-assembled genomes from different habitats to show increased colonization preference from soil to root [PMID 39591453](https://pubmed.ncbi.nlm.nih.gov/39591453/). That is a case where isolate genomics and metagenomes were combined.

Against this background, the corpus's host-specific genera are consistent in direction with the host-dependent assembly reported above. It found 117 genera unique to tomato, 54 to maize and 5 to barley rhizosphere. The corpus's low genus-level concordance (11.7% Jaccard overlap between 487 pangenome plant genera and 438 MGnify rhizosphere genera) has no direct counterpart in these candidates. None of them compares isolation-metadata classification with a metagenomic catalogue, so this result is novel relative to the retrieved literature. The corpus's own explanations, opportunistic isolates and uncultured lineages, remain untested.

The corpus's T3SS result is also not directly supported or contradicted by the candidates. It reported T3SS prevalence of 24.0% in tomato, 21.6% in maize and 22.3% in barley rhizosphere, against 12.3% in bulk soil. The candidates report functional enrichment in the rhizosphere, but none of them examines T3SS. They therefore give only general context. The core 17-genus set, which includes Pseudomonas_E and Streptomyces, overlaps taxonomically with genera highlighted in the Pseudomonas, Streptomyces and Burkholderia work above. That overlap is suggestive only, and these studies are single-crop or single-site.

## The two data sources

The census determined plant association among 293,059 GTDB r214 genomes using NCBI isolation_source regex matching, ncbi_env EAV cross-validation, and BacDive isolation records. [src: plant_microbiome_ecotypes] The ncbi_env step upgraded 695 genomes. [src: plant_microbiome_ecotypes] BacDive identified 2,482 plant strains but gave 0 new upgrades, indicating complete overlap between these metadata sources for the plant-associated genome set. [src: plant_microbiome_ecotypes] Only 7,995 of 293,059 genomes (2.7%) had plant-associated annotations. [src: plant_microbiome_ecotypes] Compartment classification relies on NCBI isolation_source metadata of variable quality and coverage. [src: plant_microbiome_ecotypes] See [[entities/ncbi-env-environmental-metadata]] and [[entities/bacdive]].

The MGnify catalogue holds 20,473 species across 4 biomes. [src: plant_microbiome_ecotypes] The taxonomy bridge linked these to 1,185 pangenome genera, with 9,603 MGnify species in matched genera. [src: plant_microbiome_ecotypes] Pangenome classification uses cultivation metadata (where a strain was isolated), while MGnify captures where a genome is detected. [src: plant_microbiome_ecotypes]

The soil biome contained 19,472 species in 4,229 genera. [src: plant_microbiome_ecotypes] The tomato rhizosphere contained 579 species in 309 genera. [src: plant_microbiome_ecotypes] The maize rhizosphere contained 336 species in 212 genera. [src: plant_microbiome_ecotypes] The barley rhizosphere contained 86 species in 52 genera. [src: plant_microbiome_ecotypes]

## Low genus-level concordance

Pangenome-derived plant genera (487) and MGnify rhizosphere genera (438) had only 11.7% Jaccard overlap. [src: plant_microbiome_ecotypes] The report attributes this to isolation metadata versus metagenomic detection and to sampling biases, not classification error. [src: plant_microbiome_ecotypes] It also says this limits the strength of the cross-validation conclusions. [src: plant_microbiome_ecotypes]

The report offers two explanations, which it does not test. The 390 pangenome-only plant genera likely include opportunistic soil bacteria isolated from plants but not rhizosphere specialists. [src: plant_microbiome_ecotypes] The 341 MGnify-only rhizosphere genera may include uncultured lineages absent from GTDB. [src: plant_microbiome_ecotypes] MGnify soil held 93 pangenome plant genera that were absent from the rhizosphere, which suggests broader environmental associations. [src: plant_microbiome_ecotypes]

## T3SS enrichment agrees

T3SS prevalence was roughly 2× higher in crop rhizosphere biomes (tomato 24.0%, maize 21.6%, barley 22.3%) than in bulk soil (12.3%). [src: plant_microbiome_ecotypes] KEGG module M00332 (T3SS) showed the same pattern, at 22–24% in all 3 rhizosphere biomes against 12.3% in soil. [src: plant_microbiome_ecotypes] Modules M00238, M00769, M00136, M00615 and M00438 were 2–3× enriched in rhizosphere. [src: plant_microbiome_ecotypes] The report calls this independent confirmation of T3SS as a plant-association marker. [src: plant_microbiome_ecotypes] It says the result is consistent with Gonzalez-Vallina et al. (2024), who found family-specific T3SS/T6SS (type VI secretion system) enrichment in rhizosphere metagenomes. [src: plant_microbiome_ecotypes] It also cites Tampakaki (2022), who found T3SS widespread in both beneficial and pathogenic plant bacteria. [src: plant_microbiome_ecotypes] The report also states that integrating the KBase Data Lakehouse pangenome data with MGnify validates mobilome patterns and core rhizosphere genera. [src: plant_microbiome_ecotypes] See [[concepts/mobile-elements-and-horizontal-transfer-of-plant-interaction-genes]].

## Core and host-specific genera

MGnify detected 17 genera across all 3 crop rhizospheres, including Pseudomonas_E, Streptomyces, Variovorax, Telluria and Acidovorax. [src: plant_microbiome_ecotypes] The report proposes these as a candidate core rhizosphere microbiome for crop-agnostic biocontrol. [src: plant_microbiome_ecotypes] MGnify detected 117 genera unique to tomato, 54 to maize and 5 to barley rhizosphere. [src: plant_microbiome_ecotypes] The NB11 host-specificity matrix reports the same counts. [src: plant_microbiome_ecotypes] The report regards host-specific genera as candidates for crop-specific biocontrol formulations. [src: plant_microbiome_ecotypes] See [[entities/pseudomonas]] and [[entities/streptomyces]].

## Biosynthetic gene clusters

In the MGnify integration, 84 plant-associated genera produce NRP/siderophore BGCs (biosynthetic gene clusters), consistent with the importance of siderophore-mediated iron acquisition in plant colonization. [src: plant_microbiome_ecotypes] Top producers were Mycobacterium (406), Pseudomonas_E (125) and Streptomyces (113). [src: plant_microbiome_ecotypes] The report regards these 84 genera as prime candidates for synthetic community design. [src: plant_microbiome_ecotypes] The soil BGC analysis classified 17,608 BGCs into MiBIG categories across 579 pangenome genera with data. [src: plant_microbiome_ecotypes]

## Limits of the cross-validation

BGC, mobilome and defense annotations in MGnify exist only for the soil biome, not for the tomato, maize or barley rhizosphere. [src: plant_microbiome_ecotypes] These analyses therefore compare soil-dwelling plant-associated genera with soil-dwelling non-plant genera, not rhizosphere with bulk soil. [src: plant_microbiome_ecotypes] See [[concepts/compartment-specific-functional-differentiation-of-plant-associated-bacteria]] and [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]].

## Open Directions

- Test whether the 390 pangenome-only plant genera are opportunists. Compare their detection in MGnify soil with their isolation_source categories. This would check the explanation offered for the 11.7% Jaccard overlap.
- Check whether the 341 MGnify-only rhizosphere genera lack GTDB representatives. This would test the uncultured-lineage explanation.
- Recompute concordance with a stricter plant definition, such as rhizosphere-only isolation terms. This would show how much the low overlap depends on how plant association is defined. See [[concepts/harmonizing-free-text-isolation-source-and-environment-metadata]].
- Obtain rhizosphere BGC, mobilome and defense annotations for MGnify. This would allow a direct rhizosphere versus bulk soil comparison.
- Test the 17 core genera and the host-specific genera in additional crops. This would show whether they hold beyond tomato, maize and barley.
