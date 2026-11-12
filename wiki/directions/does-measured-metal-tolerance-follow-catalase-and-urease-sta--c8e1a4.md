---
type: "Research direction"
description: "Across species, catalase and urease status line up oddly with genome-predicted metal tolerance, and the sign reverses inside lineages. When tolerance to each metal is measured directly within one lineage, do these traits predict tolerance to particular metals?"
hypothesis: "Within a lineage, catalase-positive strains tolerate copper better and urease-positive strains tolerate nickel better, even though the composite predicted score shows the opposite or no link."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Strain selection can use existing phenotype and genome records, but per-metal inhibitory concentrations are not in the lakehouse."
collections: ["kbase-phenotype", "kbase-ke-pangenome"]
findings: ["bacdive_phenotype_metal_tolerance--202a67ef", "bacdive_phenotype_metal_tolerance--a1b67557", "bacdive_phenotype_metal_tolerance--885a4ca9", "bacdive_metal_validation--2a7f4c05"]
conflicts: ["conflict--phenotype-database-coverage-bias--40968e6d"]
papers: ["32683159", "17183702", "20380737", "37290750"]
builds_on: ["findings/bacdive_phenotype_metal_tolerance--202a67ef", "findings/bacdive_phenotype_metal_tolerance--a1b67557", "findings/bacdive_phenotype_metal_tolerance--885a4ca9", "findings/bacdive_metal_validation--2a7f4c05", "conflicts/conflict--phenotype-database-coverage-bias--40968e6d"]
projects: ["bacdive_metal_validation", "bacdive_phenotype_metal_tolerance"]
topics: ["sampling-coverage-and-statistical-confounding"]
---
# Does measured metal tolerance follow catalase and urease status within single bacterial lineages?

Across species, catalase and urease status line up oddly with genome-predicted metal tolerance, and the sign reverses inside lineages. When tolerance to each metal is measured directly within one lineage, do these traits predict tolerance to particular metals?

## Hypothesis

Within a lineage, catalase-positive strains tolerate copper better and urease-positive strains tolerate nickel better, even though the composite predicted score shows the opposite or no link.

## Why it matters

It would show whether the cross-species reversals come from lineage composition and a coarse genome-based score, or from real biology. It would also say whether cheap phenotype tests can screen metal-tolerant isolates.

## How to test it

Choose pairs of catalase-positive and negative strains, and urease-positive and negative strains, within Actinomycetes and within Gammaproteobacteria from the Phenotype Collection. Match them in genome size using the Pangenome Collection. Measure the lowest inhibitory concentration for nickel, copper, zinc and cadmium. Compare the measured values with the composite predicted score and with the trait.

## What would support or refute it

Support: trait-metal pairings appear in measured data within lineage and the composite score misses them. Refute: measured tolerance is flat with respect to the traits within lineage, so the cross-species patterns come from which lineages were sampled.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Strain selection can use existing phenotype and genome records, but per-metal inhibitory concentrations are not in the lakehouse.

- Collection: [[data/kbase-phenotype|Phenotype Collection]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/bacdive_phenotype_metal_tolerance--202a67ef|Urease positivity associates with lower metal score, driven by Actinomycetes]] (Candidate novel)
- Finding: [[findings/bacdive_phenotype_metal_tolerance--a1b67557|Catalase association reverses within every major class (Simpson's paradox)]] (Insufficient literature evidence)
- Finding: [[findings/bacdive_phenotype_metal_tolerance--885a4ca9|Phenotype signal is absorbed by taxonomy; gene-cluster count lifts prediction]] (Candidate novel)
- Finding: [[findings/bacdive_metal_validation--2a7f4c05|Metal utilization tests show no significant link to predicted score]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--phenotype-database-coverage-bias--40968e6d|Does the BacDive Evidence Validate Genome-Based Metal-Tolerance Prediction Over Phenotype-Based Screening?]]

## Closest published work

- [PMID 32683159](https://pubmed.ncbi.nlm.nih.gov/32683159/) Distinction between Cr and other heavy-metal-resistant bacteria involved in C/N cycling in contaminated soils of copper producing sites.
- [PMID 17183702](https://pubmed.ncbi.nlm.nih.gov/17183702/) Catalases are NAD(P)H-dependent tellurite reductases.
- [PMID 20380737](https://pubmed.ncbi.nlm.nih.gov/20380737/) Brucella abortus ure2 region contains an acid-activated urea transporter and a nickel transport system.
- [PMID 37290750](https://pubmed.ncbi.nlm.nih.gov/37290750/) Genotypic and Phenotypic Characterization of Antimicrobial and Heavy Metal Tolerance in Salmonella enterica and Escherichia coli Isolates from Swine Feed Mills.

PMID 32683159 and PMID 17183702 tie catalase to metal resistance in soil communities and single organisms, and PMID 20380737 covers urease-linked nickel handling in one species; none tests the traits against measured per-metal tolerance within lineages.
