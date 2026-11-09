---
type: "Research direction"
description: "In Desulfovibrio vulgaris Hildenborough, the 21 ecological fitness modules contain 239 genes, of which 52 are unannotated. Do these unannotated genes affect growth under groundwater-like metal, pH and nitrate stress that standard lab-medium screens do not capture?"
hypothesis: "Mutants in the unannotated module genes show growth defects in groundwater-like conditions that are absent or weaker in standard lab medium, more often than annotated module members."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "The modules and gene lists exist, but fitness data under groundwater-like chemistry are not in the lakehouse."
collections: ["kescience-fitnessbrowser", "enigma-coral"]
findings: ["field_vs_lab_fitness--252d6ff5", "field_vs_lab_fitness--571f3f78", "field_vs_lab_fitness--296eadf6"]
conflicts: []
papers: ["37065130", "39259908", "29769716", "38323821"]
builds_on: ["findings/field_vs_lab_fitness--252d6ff5", "findings/field_vs_lab_fitness--571f3f78", "findings/field_vs_lab_fitness--296eadf6"]
projects: ["field_vs_lab_fitness"]
topics: ["resistance-defense-systems-and-mobile-elements"]
---
# Do unannotated genes in field-relevant conserved modules matter for survival in contaminated groundwater?

In Desulfovibrio vulgaris Hildenborough, the 21 ecological fitness modules contain 239 genes, of which 52 are unannotated. Do these unannotated genes affect growth under groundwater-like metal, pH and nitrate stress that standard lab-medium screens do not capture?

## Hypothesis

Mutants in the unannotated module genes show growth defects in groundwater-like conditions that are absent or weaker in standard lab medium, more often than annotated module members.

## Why it matters

Lab nutrient genes were as core-enriched as field-stress genes, so conservation does not tell field-relevant genes apart. Direct phenotypes for unannotated members would show whether these modules encode real environmental adaptations and would give functions to unannotated genes.

## How to test it

Grow the existing Desulfovibrio vulgaris Hildenborough transposon library, or targeted mutants of the 52 genes, in a medium built from Oak Ridge groundwater chemistry with uranium, low pH and nitrate, and in standard lab medium. Measure barcode-based fitness for the unannotated and annotated module members and for heavy-metal genes. Compare defect rates between conditions and between gene groups.

## What would support or refute it

Support: unannotated module genes show defects specific to groundwater-like conditions at a higher rate than annotated members. Refutation: defects are equally common in lab medium, or absent in both, so module activity classed as field-relevant does not imply field-specific function.

## Data

Approach: experiment. Readiness: needs new measurements. The modules and gene lists exist, but fitness data under groundwater-like chemistry are not in the lakehouse.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/enigma-coral|ENIGMA CORAL]]

## Builds on

- Finding: [[findings/field_vs_lab_fitness--252d6ff5|Field-active conserved modules hold many unannotated candidate adaptation genes]] (Insufficient literature evidence)
- Finding: [[findings/field_vs_lab_fitness--571f3f78|Field-stress, field-core and lab-nutrient genes are enriched in the core genome]] (Extends retrieved work)
- Finding: [[findings/field_vs_lab_fitness--296eadf6|Heavy-metal fitness genes are not significantly less core than baseline]] (Insufficient literature evidence)

## Closest published work

- [PMID 37065130](https://pubmed.ncbi.nlm.nih.gov/37065130/) Large-scale genetic characterization of the model sulfate-reducing bacterium, Desulfovibrio vulgaris Hildenborough.
- [PMID 39259908](https://pubmed.ncbi.nlm.nih.gov/39259908/) Fitness factors impacting survival of a subsurface bacterium in contaminated groundwater.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 38323821](https://pubmed.ncbi.nlm.nih.gov/38323821/) Machine learning analysis of RB-TnSeq fitness data predicts functional gene modules in Pseudomonas putida KT2440.

PMID 37065130 maps genome-wide fitness of this organism across many lab conditions, and PMID 39259908 identifies groundwater survival genes in a different subsurface bacterium; neither tests unannotated conserved-module genes in this organism under groundwater-like conditions.
