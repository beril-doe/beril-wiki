---
type: "Gene_Or_Pathway"
description: "Refined T3SS markers linked to plant association, but sensitive to analytical scale."
sources: ["summaries/plant_microbiome_ecotypes__REPORT.md"]
---
# Type III secretion system markers

## What this entity is

The canonical name is Type III secretion system markers, referring to genomic markers for the Type III secretion system, a plant-interaction feature abbreviated T3SS. [src: plant_microbiome_ecotypes]

Known aliases are T3SS markers and Type III secretion system (T3SS). [src: plant_microbiome_ecotypes]

No stable external identifier is specified for this marker set in the report. [src: plant_microbiome_ecotypes]

## Key facts from the document

The report reduced an initial 91-marker panel to 17 plant-specific markers and required at least three genes for a species to be called T3SS-positive. [src: plant_microbiome_ecotypes]

Under this refined definition, the number of T3SS-positive species decreased from 10,300 to 1,661, a reduction of 8,855 species or 86%. [src: plant_microbiome_ecotypes]

In the original compartment analysis, root-associated species showed T3SS enrichment with odds ratio (OR) = 65.6, and 69 of 96 marker-by-compartment tests were significant. [src: plant_microbiome_ecotypes]

The refined compartment analysis found statistically significant but weak functional separation overall, with PERMANOVA R² = 0.071 and db-RDA location-only R² = 0.060; these values describe the broader marker panel rather than T3SS alone. [src: plant_microbiome_ecotypes]

A cluster-robust generalized linear model with genus clustering across 7,555 genus clusters and 24,554 species found T3SS associated with plant status at OR = 2.71, with an absolute coefficient greater than 0.2 and Benjamini–Hochberg false-discovery-rate q < 0.05. [src: plant_microbiome_ecotypes]

Within-genus label shuffling retained T3SS as one of only three markers with an association signal, alongside nitrogen fixation and ACC deaminase. [src: plant_microbiome_ecotypes]

The report states that Bonferroni correction at α = 0.0033 would demote the T3SS association, whereas nitrogen fixation and ACC deaminase would remain significant. [src: plant_microbiome_ecotypes]

These results indicate that the T3SS plant-association signal is scale-dependent: it is strong in the original compartment-level analysis, weaker in the refined genus-clustered analysis, and less robust under stricter multiple-testing correction. [src: plant_microbiome_ecotypes]

T3SS marker presence does not establish expression or phenotype, because secretion functions can support colonization, interbacterial competition, beneficial symbiosis, or pathogenicity. [src: plant_microbiome_ecotypes]

The report therefore treats T3SS as a refined plant-interaction feature rather than a categorical pathogenicity classifier. [src: plant_microbiome_ecotypes]

## Data and annotation considerations

An annotation audit found that the marker Pfam set missing from bakta_pfam_domains was dominated by T3SS, T4SS, and T6SS components. [src: plant_microbiome_ecotypes]

The refined cohort pipeline used [[entities/interproscan]] for secretion-system detection, so the report states that these annotation-table limitations did not affect its biological assignments. [src: plant_microbiome_ecotypes]

## Relations to other pages

The scale-dependent association of T3SS markers supports [[concepts/ecotype-environment-gene-content]], which addresses how plant compartments and host contexts relate to genomic features. [src: plant_microbiome_ecotypes]

The distinction between T3SS marker presence and context-dependent activity supports [[concepts/condition-specific-fitness]]. [src: plant_microbiome_ecotypes]

The refined marker panel and its core/accessory interpretation connect to [[concepts/pangenome-integration]]. [src: plant_microbiome_ecotypes]

The source summary is [[summaries/plant_microbiome_ecotypes__REPORT]]. [src: plant_microbiome_ecotypes]

## Evidence limits

The marker set is literature-curated, and the report requires transcriptomic or experimental validation to determine whether PGP and pathogenic marker sets are co-expressed under the same conditions. [src: plant_microbiome_ecotypes]

The cluster-robust generalized linear model is described as a practical genus-level analogue rather than a full phylogenetic generalized linear mixed model, and the within-genus shuffle used only 200 permutations. [src: plant_microbiome_ecotypes]
