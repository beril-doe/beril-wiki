---
type: "Research direction"
description: "Is the within-class advantage of catalase-negative species in predicted metal tolerance driven by metal-resistance gene content, and does it appear as measured tolerance to specific metals?"
hypothesis: "The within-class sign reversal for catalase (Actinomycetes, Gammaproteobacteria, Betaproteobacteria) disappears once the number of metal resistance gene clusters is controlled. In measured per-metal fitness data, catalase and urease status predict tolerance to a particular metal only in a few lineage-matched comparisons."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Per-metal scores for the 27K species are not computed, and the existing direct Fitness Browser\u2013BacDive set lacks balanced phenotype contrasts, so measured tolerance in balanced organism sets must be generated."
collections: ["kbase-phenotype", "kbase-ke-pangenome", "kescience-fitnessbrowser"]
findings: ["bacdive_phenotype_metal_tolerance--a1b67557", "bacdive_phenotype_metal_tolerance--202a67ef", "bacdive_phenotype_metal_tolerance--885a4ca9", "bacdive_phenotype_metal_tolerance--9b04bc8d"]
conflicts: ["conflict--phenotype-database-coverage-bias--40968e6d"]
papers: ["32683159", "17183702", "20380737", "37548767", "37290750"]
builds_on: ["findings/bacdive_phenotype_metal_tolerance--a1b67557", "findings/bacdive_phenotype_metal_tolerance--202a67ef", "findings/bacdive_phenotype_metal_tolerance--885a4ca9", "findings/bacdive_phenotype_metal_tolerance--9b04bc8d", "conflicts/conflict--phenotype-database-coverage-bias--40968e6d"]
projects: ["bacdive_metal_validation", "bacdive_phenotype_metal_tolerance"]
topics: ["sampling-coverage-and-statistical-confounding"]
---
# Catalase-negative species may score higher on metal tolerance because of metal-gene content, not catalase

Is the within-class advantage of catalase-negative species in predicted metal tolerance driven by metal-resistance gene content, and does it appear as measured tolerance to specific metals?

## Hypothesis

The within-class sign reversal for catalase (Actinomycetes, Gammaproteobacteria, Betaproteobacteria) disappears once the number of metal resistance gene clusters is controlled. In measured per-metal fitness data, catalase and urease status predict tolerance to a particular metal only in a few lineage-matched comparisons.

## Why it matters

Metal Fitness Atlas scores are genome-based predictions, so the BacDive associations show only phenotype-to-genome correlations. Showing which traits track measured tolerance within lineages would decide whether phenotype-based screening is informative at all.

## How to test it

Step 1: with BacDive-linked species, refit within-class models on per-metal scores (catalase vs copper, urease vs nickel, H2S vs zinc, copper and cadmium) with and without n_metal_clusters. Step 2: assemble Fitness Browser organisms with balanced trait-positive and trait-negative members within the same class, and measure fitness under the matching metals with RB-TnSeq (random barcode transposon sequencing), adding organisms where the browser lacks balanced contrasts. Compare measured effects with predicted scores.

## What would support or refute it

Support: within-class reversals vanish when metal cluster count is controlled, and measured per-metal effects appear only for the predicted metal. Refute: within-class associations persist after the control and match measured tolerance. The Gram-negative advantage cannot be tested within classes.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Per-metal scores for the 27K species are not computed, and the existing direct Fitness Browser–BacDive set lacks balanced phenotype contrasts, so measured tolerance in balanced organism sets must be generated.

- Collection: [[data/kbase-phenotype|Phenotype Collection]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/bacdive_phenotype_metal_tolerance--a1b67557|Catalase association reverses within every major class (Simpson's paradox)]] (Insufficient literature evidence)
- Finding: [[findings/bacdive_phenotype_metal_tolerance--202a67ef|Urease positivity associates with lower metal score, driven by Actinomycetes]] (Candidate novel)
- Finding: [[findings/bacdive_phenotype_metal_tolerance--885a4ca9|Phenotype signal is absorbed by taxonomy; gene-cluster count lifts prediction]] (Candidate novel)
- Finding: [[findings/bacdive_phenotype_metal_tolerance--9b04bc8d|Gram-negative advantage is the largest effect but is a between-lineage signal]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--phenotype-database-coverage-bias--40968e6d|Does the BacDive Evidence Validate Genome-Based Metal-Tolerance Prediction Over Phenotype-Based Screening?]]

## Closest published work

- [PMID 32683159](https://pubmed.ncbi.nlm.nih.gov/32683159/) Distinction between Cr and other heavy-metal-resistant bacteria involved in C/N cycling in contaminated soils of copper producing sites.
- [PMID 17183702](https://pubmed.ncbi.nlm.nih.gov/17183702/) Catalases are NAD(P)H-dependent tellurite reductases.
- [PMID 20380737](https://pubmed.ncbi.nlm.nih.gov/20380737/) Brucella abortus ure2 region contains an acid-activated urea transporter and a nickel transport system.
- [PMID 37548767](https://pubmed.ncbi.nlm.nih.gov/37548767/) Removal of cadmium and arsenic from water through biomineralization.
- [PMID 37290750](https://pubmed.ncbi.nlm.nih.gov/37290750/) Genotypic and Phenotypic Characterization of Antimicrobial and Heavy Metal Tolerance in Salmonella enterica and Escherichia coli Isolates from Swine Feed Mills.

PMID 32683159 and 17183702 tie catalase to metal resistance, PMID 20380737 ties urease-linked nickel transport to a single organism, and PMID 37548767 covers urease activity under Cd/As stress in one strain; none tests within-class sign reversal or per-metal scores against measured tolerance.
