---
type: "Organism"
description: "GTDB Pseudomonas_E clade retaining broad carbon-use pathways"
sources: ["summaries/pseudomonas_carbon_ecology__REPORT.md"]
---
# GTDB Pseudomonas_E clade with broad carbon-pathway retention

## What this entity is

**Canonical name:** GTDB *Pseudomonas_E* clade. [src: pseudomonas_carbon_ecology]

**Known aliases:** *Pseudomonas_E*; *P. fluorescens/putida* group. [src: pseudomonas_carbon_ecology]

The clade is a GTDB r214 species grouping that includes the *Pseudomonas fluorescens* and *Pseudomonas putida* groups. [src: pseudomonas_carbon_ecology]

No stable external identifier for this clade was reported in the document. [src: pseudomonas_carbon_ecology]

## Key facts

The analysis included 398 *Pseudomonas_E* species and 5,687 genomes from the KBase Data Lakehouse `kbase_ke_pangenome` collection. [src: pseudomonas_carbon_ecology]

Among species with at least 5 genomes, *Pseudomonas_E* was compared with 7 *Pseudomonas* s.s. species using standardized [[entities/gapmind]] predictions for 62 carbon pathways. [src: pseudomonas_carbon_ecology]

Relative to the *P. aeruginosa* group, the *P. fluorescens/putida* group retained substantially more plant-derived sugar and sugar-alcohol pathways: xylose was 74.4% complete versus 0.0%, ribose was 92.0% versus 27.9%, arabinose was 62.6% versus 0.0%, galacturonate was 88.4% versus 28.6%, myo-inositol was 58.8% versus 0.0%, mannitol was 77.5% versus 25.9%, and sorbitol was 77.4% versus 25.9%, respectively. [src: pseudomonas_carbon_ecology]

These differences were among 43 of 62 pathways that differed significantly between the two groups by Mann–Whitney U testing with Benjamini–Hochberg false-discovery-rate correction at q < 0.05. [src: pseudomonas_carbon_ecology]

Within *Pseudomonas_E*, plant-associated species averaged 56.7 complete pathways, free-living species averaged 56.1, and host-associated species averaged 55.2. [src: pseudomonas_carbon_ecology]

Lifestyle categories substantially overlapped within *Pseudomonas_E*, while the dominant principal-component axis separated *Pseudomonas* s.s. from *Pseudomonas_E* and was driven by sugar-pathway loss. [src: pseudomonas_carbon_ecology]

Among 54 free-living and plant-associated species meeting the filtering criteria, carbon-pathway profiles were significantly associated with isolation environment in a 999-permutation test, with p = 0.006, a between-group mean distance of 2.054, a within-group mean distance of 1.890, and a between/within ratio of 1.087. [src: pseudomonas_carbon_ecology]

A Random Forest classifier distinguishing soil, freshwater, plant-surface, and rhizosphere environments achieved balanced accuracy of 0.408 +/- 0.169 in 5-fold stratified cross-validation, compared with a 0.250 chance baseline. [src: pseudomonas_carbon_ecology]

The report interprets these results as evidence that *Pseudomonas_E* carbon profiles contain an ecological signal, but that carbon pathways alone are insufficient for fine-grained environment prediction. [src: pseudomonas_carbon_ecology]

## Interpretation and limitations

The broad pathway retention in *Pseudomonas_E* supports the hypothesis that the deep subgenus division is a stronger source of carbon-pathway variation than lifestyle differences within *Pseudomonas_E*. [src: pseudomonas_carbon_ecology]

The analysis did not explicitly control for phylogenetic non-independence, so phylogenetic generalized least squares or phylogenetic logistic regression using the GTDB species tree was proposed as follow-up work. [src: pseudomonas_carbon_ecology]

The 62 [[concepts/metabolic-model-gapfilling]] pathways omit genus-specific capabilities, including aromatic degradation pathways relevant to *Pseudomonas putida* ecology, so adding KEGG or other aromatic-pathway modules was proposed. [src: pseudomonas_carbon_ecology]

Within-species analyses of *Pseudomonas fluorescens* and *Pseudomonas putida* metabolic ecotypes, together with experimental validation using [[entities/kescience-fitnessbrowser]] RB-TnSeq data, were proposed as next steps. [src: pseudomonas_carbon_ecology]

## Related pages

- [[summaries/pseudomonas_carbon_ecology__REPORT]] — source report on carbon-pathway profiles, ecology, and lifestyle in *Pseudomonas*. [src: pseudomonas_carbon_ecology]
- [[concepts/ecotype-environment-gene-content]] — connects carbon-pathway variation with ecological niche and metabolic ecotypes. [src: pseudomonas_carbon_ecology]
- [[concepts/environment-embedding-geography]] — covers environment association in pathway-profile space. [src: pseudomonas_carbon_ecology]
- [[concepts/pangenome-integration]] — covers genome- and species-scale pathway matrices and metadata integration. [src: pseudomonas_carbon_ecology]
- [[entities/gtdb]] — database framework used for the GTDB r214 species-clade assignments. [src: pseudomonas_carbon_ecology]
- [[entities/pseudomonas-fluorescens]] — organism group represented within the *Pseudomonas_E* comparison. [src: pseudomonas_carbon_ecology]
- [[entities/pseudomonas-putida]] — organism group represented within the *Pseudomonas_E* comparison. [src: pseudomonas_carbon_ecology]
