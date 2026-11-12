---
type: "Research direction"
description: "Within a single bacterial class, why do catalase-negative species tend to score higher for predicted metal tolerance than catalase-positive ones, the reverse of the pooled trend?"
hypothesis: "Catalase-negative species in Actinomycetes and Proteobacteria compensate with other peroxide and thiol-based oxidative-stress systems, and these same systems account for their higher metal scores. Measured tolerance of catalase-negative strains will then be no lower than that of catalase-positive relatives."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Enzyme tests and genome annotations are in the catalog, but the catalog did not show the metal-score table, and measured metal tolerance of matched strains has to be generated."
databases: ["kbase.ke_pangenome", "kescience.bacdive"]
tables: ["kescience.bacdive.enzyme", "kescience.bacdive.taxonomy", "kbase.ke_pangenome.eggnog_mapper_annotations", "kbase.ke_pangenome.gtdb_metadata"]
findings: ["bacdive_phenotype_metal_tolerance--a1b67557", "bacdive_phenotype_metal_tolerance--202a67ef", "bacdive_phenotype_metal_tolerance--885a4ca9"]
conflicts: ["conflict--phenotype-database-coverage-bias--40968e6d"]
papers: ["32683159", "17183702", "37290750"]
builds_on: ["findings/bacdive_phenotype_metal_tolerance--a1b67557", "findings/bacdive_phenotype_metal_tolerance--202a67ef", "findings/bacdive_phenotype_metal_tolerance--885a4ca9", "conflicts/conflict--phenotype-database-coverage-bias--40968e6d"]
projects: ["bacdive_metal_validation", "bacdive_phenotype_metal_tolerance"]
topics: ["sampling-coverage-and-statistical-confounding"]
---
# Do catalase-negative bacteria use other oxidative defences that also confer metal tolerance?

Within a single bacterial class, why do catalase-negative species tend to score higher for predicted metal tolerance than catalase-positive ones, the reverse of the pooled trend?

## Hypothesis

Catalase-negative species in Actinomycetes and Proteobacteria compensate with other peroxide and thiol-based oxidative-stress systems, and these same systems account for their higher metal scores. Measured tolerance of catalase-negative strains will then be no lower than that of catalase-positive relatives.

## Why it matters

It would show whether the within-lineage reversal is a real physiological trade-off or an artefact of how genome-based scores are built. It would also tell screeners which phenotype tests are informative within a lineage.

## How to test it

Match catalase-positive and catalase-negative species within the same classes using recorded enzyme tests, then count alternative peroxide-detoxification and thiol-redox genes in their genomes and check whether these account for the score gap. Then grow matched pairs of strains from the three classes where the effect reversed (Actinomycetes, Gammaproteobacteria and Betaproteobacteria) under cadmium and copper, with and without added peroxide, and measure tolerance directly.

## What would support or refute it

Support: alternative defence genes explain the score gap and measured tolerance is similar or higher in catalase-negative strains. Refutation: the gap persists after accounting for these genes, or catalase-negative strains are measurably less tolerant, which would mean the genome-based score, not biology, drives the reversal.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Enzyme tests and genome annotations are in the catalog, but the catalog did not show the metal-score table, and measured metal tolerance of matched strains has to be generated.

## Builds on

- Finding: [[findings/bacdive_phenotype_metal_tolerance--a1b67557|Catalase association reverses within every major class (Simpson's paradox)]] (Insufficient literature evidence)
- Finding: [[findings/bacdive_phenotype_metal_tolerance--202a67ef|Urease positivity associates with lower metal score, driven by Actinomycetes]] (Candidate novel)
- Finding: [[findings/bacdive_phenotype_metal_tolerance--885a4ca9|Phenotype signal is absorbed by taxonomy; gene-cluster count lifts prediction]] (Candidate novel)
- Conflict: [[conflicts/conflict--phenotype-database-coverage-bias--40968e6d|Does the BacDive Evidence Validate Genome-Based Metal-Tolerance Prediction Over Phenotype-Based Screening?]]

## Closest published work

- [PMID 32683159](https://pubmed.ncbi.nlm.nih.gov/32683159/) Distinction between Cr and other heavy-metal-resistant bacteria involved in C/N cycling in contaminated soils of copper producing sites.
- [PMID 17183702](https://pubmed.ncbi.nlm.nih.gov/17183702/) Catalases are NAD(P)H-dependent tellurite reductases.
- [PMID 37290750](https://pubmed.ncbi.nlm.nih.gov/37290750/) Genotypic and Phenotypic Characterization of Antimicrobial and Heavy Metal Tolerance in Salmonella enterica and Escherichia coli Isolates from Swine Feed Mills.

PMID 32683159 links catalase-producing Proteobacteria to multimetal resistance and PMID 17183702 shows catalase-mediated tellurite reduction, but neither tests whether other oxidative-stress systems explain a within-class reversal.
