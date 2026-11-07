---
type: "Research direction"
description: "Catalase-negative species score higher on predicted metal tolerance inside several classes, though the pooled trend is the opposite, and urease positivity lowers the score only in Actinomycetes. Is that reversal real tolerance, or an artefact of the genome-based score?"
hypothesis: "Measured tolerance to individual metals does not follow catalase or urease status within a class. Where a phenotype appears to matter, its effect is explained by the number of metal-resistance gene clusters."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "Strain pairs can be chosen from the lakehouse, but no independent per-metal tolerance measurements exist for them."
collections: ["kbase-phenotype", "kbase-ke-pangenome", "kescience-fitnessbrowser"]
findings: ["bacdive_phenotype_metal_tolerance--a1b67557", "bacdive_phenotype_metal_tolerance--202a67ef", "bacdive_phenotype_metal_tolerance--885a4ca9"]
conflicts: ["conflict--phenotype-database-coverage-bias--40968e6d"]
papers: ["32683159", "17183702", "20380737", "37290750"]
builds_on: ["findings/bacdive_phenotype_metal_tolerance--a1b67557", "findings/bacdive_phenotype_metal_tolerance--202a67ef", "findings/bacdive_phenotype_metal_tolerance--885a4ca9", "conflicts/conflict--phenotype-database-coverage-bias--40968e6d"]
projects: ["bacdive_metal_validation", "bacdive_phenotype_metal_tolerance"]
topics: ["sampling-coverage-and-statistical-confounding"]
---
# Do catalase and urease status predict measured metal tolerance within a bacterial class?

Catalase-negative species score higher on predicted metal tolerance inside several classes, though the pooled trend is the opposite, and urease positivity lowers the score only in Actinomycetes. Is that reversal real tolerance, or an artefact of the genome-based score?

## Hypothesis

Measured tolerance to individual metals does not follow catalase or urease status within a class. Where a phenotype appears to matter, its effect is explained by the number of metal-resistance gene clusters.

## Why it matters

The score is a genome-based prediction, so lineage structure could be producing these phenotype associations. Measured data would show whether phenotype screening of metal tolerance has any use beyond lineage identity.

## How to test it

From the Phenotype Collection and Pangenome Collection, pick strain pairs within Gammaproteobacteria and Actinomycetes that differ in catalase or urease status, without matching on metal-resistance cluster number, so that cluster number varies across the set. Measure growth-inhibiting concentrations of copper, nickel, zinc and cadmium for each strain. Model measured tolerance with phenotype status and cluster number together, and compare with predicted scores. Also check against measured metal fitness in the Fitness Browser where an organism overlaps.

## What would support or refute it

Support: once cluster number is in the model, phenotype status adds nothing to measured tolerance within classes. Refutation: catalase-negative or urease-positive strains show reproducibly different measured tolerance for specific metals, such as nickel for urease, beyond what cluster number explains.

## Data

Approach: experiment. Readiness: needs new measurements. Strain pairs can be chosen from the lakehouse, but no independent per-metal tolerance measurements exist for them.

- Collection: [[data/kbase-phenotype|Phenotype Collection]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/bacdive_phenotype_metal_tolerance--a1b67557|Catalase association reverses within every major class (Simpson's paradox)]] (Insufficient literature evidence)
- Finding: [[findings/bacdive_phenotype_metal_tolerance--202a67ef|Urease positivity associates with lower metal score, driven by Actinomycetes]] (Candidate novel)
- Finding: [[findings/bacdive_phenotype_metal_tolerance--885a4ca9|Phenotype signal is absorbed by taxonomy; gene-cluster count lifts prediction]] (Candidate novel)
- Conflict: [[conflicts/conflict--phenotype-database-coverage-bias--40968e6d|Does the BacDive Evidence Validate Genome-Based Metal-Tolerance Prediction Over Phenotype-Based Screening?]]

## Closest published work

- [PMID 32683159](https://pubmed.ncbi.nlm.nih.gov/32683159/) Distinction between Cr and other heavy-metal-resistant bacteria involved in C/N cycling in contaminated soils of copper producing sites.
- [PMID 17183702](https://pubmed.ncbi.nlm.nih.gov/17183702/) Catalases are NAD(P)H-dependent tellurite reductases.
- [PMID 20380737](https://pubmed.ncbi.nlm.nih.gov/20380737/) Brucella abortus ure2 region contains an acid-activated urea transporter and a nickel transport system.
- [PMID 37290750](https://pubmed.ncbi.nlm.nih.gov/37290750/) Genotypic and Phenotypic Characterization of Antimicrobial and Heavy Metal Tolerance in Salmonella enterica and Escherichia coli Isolates from Swine Feed Mills.

PMIDs 32683159 and 17183702 link catalase to metal resistance in single settings, and PMID 20380737 links urease to nickel transport in one organism; none tests the phenotype across paired strains within a class.
