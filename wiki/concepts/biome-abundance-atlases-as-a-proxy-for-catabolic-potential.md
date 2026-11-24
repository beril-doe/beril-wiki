---
type: "Concept"
description: "Covers using metagenome or 16S abundance of implicated genera across environments to locate potential utilizers, and the limits of inferring degradation from abundance; it stops at occupancy, not activity."
sources: ["summaries/enigma_carbon_census_1__REPORT.md"]
---
# Biome abundance atlases as a proxy for catabolic potential

Genus abundance across environments can show where organisms implicated in carbon-compound utilization live. It cannot show whether they degrade those compounds there. The evidence comes from one project, the ENIGMA Carbon Census ([[summaries/enigma_carbon_census_1__REPORT]]), which placed 86 implicated utilizer genera in a global abundance atlas. [src: enigma_carbon_census_1] The atlas gives coherent biome occupancy, and the report states plainly that it stops short of activity. [src: enigma_carbon_census_1]

## What the atlas covers

The report placed the implicated genera across terrestrial and freshwater environments using NMDC (`kbase.nmdc_arkin`) in the KBase Data Lakehouse. It used Planet Microbe as a marine contrast. [src: enigma_carbon_census_1] See [[entities/nmdc-integrated-collections]] and [[entities/planet-microbe]].

The NMDC arm has 3825 taxonomy-bearing metagenomes, with the denominator defined as covstats files with taxonomy. [src: enigma_carbon_census_1] It detects 83/86 genera in 1719 metagenomes. [src: enigma_carbon_census_1] It is 99% sample-labeled through two independent ontologies, the ENVO (Environment Ontology) MIxS triad and the GOLD ecosystem path. [src: enigma_carbon_census_1] The macro-environment counts are soil 2260, freshwater 723, periphyton 472, plant 119 and sediment 42. [src: enigma_carbon_census_1]

The marine arm has 302 Planet Microbe runs, with presence and abundance only and no gene information. [src: enigma_carbon_census_1] The headline table reports 68 of 68 genera positive in those runs. [src: enigma_carbon_census_1]

## Where potential utilizers sit

The signal is biologically coherent: soil generalists in soil, aquatic Betaproteobacteria in freshwater, a Comamonadaceae periphyton reservoir, and terrestrial taxa rare in open ocean. [src: enigma_carbon_census_1]

- **Spikes.** The largest genus-by-sample relative-abundance spikes are Nocardioides at 0.43 in epipsammon, Hydrogenophaga at 0.28 in epiphyton, and Mycobacterium at 0.22 in soil. [src: enigma_carbon_census_1] Outliers peak in periphyton (34 genera) and soil (32). [src: enigma_carbon_census_1]
- **Soil versus freshwater.** This contrast is exploratory. Soil-enriched genera include Mycobacterium (log2 +5.09), Terriglobus (+5.29) and Nitrobacter (+4.79). [src: enigma_carbon_census_1] Afipia, Streptomyces, Nocardioides and Mesorhizobium are also soil-enriched. [src: enigma_carbon_census_1] Cellvibrio is freshwater-enriched (log2 −2.19). [src: enigma_carbon_census_1] Curvibacter, Rhodoferax, Comamonas and Acidovorax are also freshwater-enriched. [src: enigma_carbon_census_1]
- **Periphyton.** Separating a periphyton class (freshwater biofilms) from bulk freshwater reveals a Comamonadaceae/Burkholderiales reservoir at ~97% prevalence. [src: enigma_carbon_census_1] Rhizobacter, Variovorax, Polaromonas, Methylibium, Sphingomonas and Hydrogenophaga sit at ~96–97% prevalence with mean relative abundance ~0.005–0.009. [src: enigma_carbon_census_1] Bulk-environment labels obscure this reservoir. [src: enigma_carbon_census_1] See [[entities/burkholderiales]].
- **Practical use.** The report suggests freshwater-biofilm inocula for aromatic-utilizer enrichments. [src: enigma_carbon_census_1]
- **Marine contrast.** The marine arm is mostly a negative contrast. Terrestrial and freshwater genera sit at ~1e-3 to 1e-4 in open ocean. [src: enigma_carbon_census_1] Genuine marine members are the exception: Alteromonas at 0.048 in 240/302 runs (prevalence 0.79), cosmopolitan Pseudomonas at 0.011, and Sphingomonas at 0.0063. [src: enigma_carbon_census_1]
- **Local field.** In the SSO field atlas, 62 implicated genera are observed at genus resolution. Top aromatic-utilizer prevalences are ~0.7–0.9, and 3-hydroxybenzoic-acid utilizers reach 0.90. [src: enigma_carbon_census_1]

## Limits of inferring degradation

No environmental dataset measures the census compounds. The atlas therefore reports biome occupancy, not catabolic flux. [src: enigma_carbon_census_1] Genus abundance shows where the organisms live, not where the compounds are degraded. [src: enigma_carbon_census_1] A genus enriched in soil does not necessarily degrade the compound there. [src: enigma_carbon_census_1]

Environmental coherence validates the taxonomic and abundance pipeline, meaning the genus calls and ENVO/GOLD labels. It does not validate the compound→pathway→organism inference. It also cannot show that any genus degrades a census compound in a sampled environment. [src: enigma_carbon_census_1]

The marine arm is small and gene-blind, so it works only as a negative contrast. [src: enigma_carbon_census_1] The periphyton enrichment rests on the project's own abundance data (~97% prevalence in periphyton samples). The report treats it as its own observation pending a targeted literature anchor. [src: enigma_carbon_census_1] For how denominators affect such contrasts, see [[concepts/calibration-and-denominators-in-environmental-abundance-contrasts]].

## Open Directions

- Pair the atlas with metatranscriptomes or metabolite measurements from periphyton and soil samples, to test whether the implicated genera express the relevant pathways. This would close the abundance-versus-activity gap.
- Run enrichment cultures from freshwater-biofilm inocula on the aromatic census compounds. They would test the Comamonadaceae reservoir as a source of utilizers.
- Find a literature anchor for periphyton Burkholderiales prevalence, or replicate it in an independent metagenome collection.
- Add gene-level or pathway-level marine data. This would let the marine arm do more than serve as a negative contrast.
- Re-run the soil-versus-freshwater contrast with a defined statistical test, since it is currently exploratory.
