---
type: "Research direction"
description: "Across bacteria with fitness data, is a gene's pangenome conservation better predicted by how large its fitness effect is or by what kind of condition revealed it?"
hypothesis: "Fitness magnitude predicts core status better than condition type in most organisms, so the DvH result is general and not a feature of one small pangenome."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Fitness and pangenome tables are in the catalog, but linking Fitness Browser genes to pangenome clusters needs a mapping step not shown in the catalog."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.genefitness", "kescience.fitnessbrowser.experiment", "kescience.fitnessbrowser.organism", "kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.gtdb_species_clade"]
findings: ["field_vs_lab_fitness--6def5903", "field_vs_lab_fitness--18b97ff6", "field_vs_lab_fitness--133f8382"]
conflicts: []
papers: ["37065130", "29769716", "36097170", "25848053"]
builds_on: ["findings/field_vs_lab_fitness--6def5903", "findings/field_vs_lab_fitness--18b97ff6", "findings/field_vs_lab_fitness--133f8382"]
projects: ["field_vs_lab_fitness"]
topics: ["gene-essentiality-and-perturbation-assay-validity"]
---
# Does the size of a gene's fitness effect predict conservation better than the condition tested?

Across bacteria with fitness data, is a gene's pangenome conservation better predicted by how large its fitness effect is or by what kind of condition revealed it?

## Hypothesis

Fitness magnitude predicts core status better than condition type in most organisms, so the DvH result is general and not a feature of one small pangenome.

## Why it matters

It would show that the core genome reflects general functional importance rather than niche-specific selection, and that environment-matched assays add little for predicting conservation.

## How to test it

For Fitness Browser organisms linked to pangenome clades, compute each gene's strongest fitness effect and its condition class (stress, nutrient, carbon source) from the experiment table. Fit models of core versus accessory status with magnitude alone, condition class alone, and both. Compare them within each organism, especially those with many genomes, and include the DvH field-stress genes.

## What would support or refute it

Support: magnitude beats condition class in most organisms. Refute: condition class adds clear predictive value in several organisms, which would indicate niche-specific selection.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Fitness and pangenome tables are in the catalog, but linking Fitness Browser genes to pangenome clusters needs a mapping step not shown in the catalog.

## Builds on

- Finding: [[findings/field_vs_lab_fitness--6def5903|Fitness magnitude predicted conservation more than condition type in DvH]] (Candidate novel)
- Finding: [[findings/field_vs_lab_fitness--18b97ff6|Field-stress genes are more core than baseline in DvH]] (Candidate novel)
- Finding: [[findings/field_vs_lab_fitness--133f8382|No significant field-specific versus lab-specific conservation difference detected in DvH]] (Candidate novel)

## Closest published work

- [PMID 37065130](https://pubmed.ncbi.nlm.nih.gov/37065130/) Large-scale genetic characterization of the model sulfate-reducing bacterium, Desulfovibrio vulgaris Hildenborough.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 36097170](https://pubmed.ncbi.nlm.nih.gov/36097170/) A bacterial pan-genome makes gene essentiality strain-dependent and evolvable.
- [PMID 25848053](https://pubmed.ncbi.nlm.nih.gov/25848053/) General and condition-specific essential functions of Pseudomonas aeruginosa.

37065130 gives DvH fitness data and 29769716 gives multi-organism fitness data; neither compares magnitude with condition type for predicting conservation.
