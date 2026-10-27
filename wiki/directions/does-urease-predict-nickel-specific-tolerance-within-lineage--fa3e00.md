---
type: "Research direction"
description: "Is the negative urease association with composite metal tolerance (d = -0.18) a lineage-composition effect masking a nickel-specific benefit within lineages?"
hypothesis: "Within Gammaproteobacteria and Bacilli, urease-positive strains show greater nickel-specific tolerance but not tolerance to other metals. The pooled reversal is driven by Actinomycetes (d = -0.59)."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Composite scores exist but per-metal phenotypes are absent, so tolerance assays are required."
collections: ["kbase-phenotype", "kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["bacdive_phenotype_metal_tolerance--202a67ef", "bacdive_phenotype_metal_tolerance--a1b67557", "bacdive_phenotype_metal_tolerance--885a4ca9"]
conflicts: ["conflict--composite-resistance-score-limitations--6eae70d7"]
papers: ["20380737", "8808930", "37548767", "32683159", "17183702"]
builds_on: ["findings/bacdive_phenotype_metal_tolerance--202a67ef", "findings/bacdive_phenotype_metal_tolerance--a1b67557", "findings/bacdive_phenotype_metal_tolerance--885a4ca9", "conflicts/conflict--composite-resistance-score-limitations--6eae70d7"]
projects: ["bacdive_phenotype_metal_tolerance"]
topics: ["resistance-defense-systems-and-mobile-elements"]
---
# Does urease predict nickel-specific tolerance within lineages despite lowering composite metal scores?

Is the negative urease association with composite metal tolerance (d = -0.18) a lineage-composition effect masking a nickel-specific benefit within lineages?

## Hypothesis

Within Gammaproteobacteria and Bacilli, urease-positive strains show greater nickel-specific tolerance but not tolerance to other metals. The pooled reversal is driven by Actinomycetes (d = -0.59).

## Why it matters

It would test whether phenotype-genotype associations in tolerance data reflect real metal-specific mechanisms or lineage artifacts, and guide how phenotype databases are used to predict tolerance.

## How to test it

Select matched urease-positive and urease-negative strains within Gammaproteobacteria and Bacilli from BacDive-linked species. Measure growth under nickel versus Cu, Zn, Cd and Co with MIC or growth curves. Add RB-TnSeq under nickel in a urease-carrying organism to see whether urease and accessory genes are nickel-fitness determinants. In parallel, compute per-metal Fitness Browser fitness for urease genes in organisms that carry them.

## What would support or refute it

Support: nickel-specific advantage in urease-positive strains within lineages. Refute: no nickel difference within lineages, or equal effects across metals.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Composite scores exist but per-metal phenotypes are absent, so tolerance assays are required.

- Collection: [[data/kbase-phenotype|Phenotype Collection]]
- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/bacdive_phenotype_metal_tolerance--202a67ef|Urease positivity associates with lower metal score, driven by Actinomycetes]] (Candidate novel)
- Finding: [[findings/bacdive_phenotype_metal_tolerance--a1b67557|Catalase association reverses within every major class (Simpson's paradox)]] (Insufficient literature evidence)
- Finding: [[findings/bacdive_phenotype_metal_tolerance--885a4ca9|Phenotype signal is absorbed by taxonomy; gene-cluster count lifts prediction]] (Candidate novel)
- Conflict: [[conflicts/conflict--composite-resistance-score-limitations--6eae70d7|Is metal-resistance gene count a standalone predictor of metal tolerance, or only a conditional one?]]

## Closest published work

- [PMID 20380737](https://pubmed.ncbi.nlm.nih.gov/20380737/) Brucella abortus ure2 region contains an acid-activated urea transporter and a nickel transport system.
- [PMID 8808930](https://pubmed.ncbi.nlm.nih.gov/8808930/) Purification and activation properties of UreD-UreF-urease apoprotein complexes.
- [PMID 37548767](https://pubmed.ncbi.nlm.nih.gov/37548767/) Removal of cadmium and arsenic from water through biomineralization.
- [PMID 32683159](https://pubmed.ncbi.nlm.nih.gov/32683159/) Distinction between Cr and other heavy-metal-resistant bacteria involved in C/N cycling in contaminated soils of copper producing sites.
- [PMID 17183702](https://pubmed.ncbi.nlm.nih.gov/17183702/) Catalases are NAD(P)H-dependent tellurite reductases.

PMIDs 20380737 and 8808930 characterise urease-linked nickel handling in single organisms and PMID 32683159 links catalase/urease-producing Proteobacteria to multimetal resistance. None stratifies by lineage or compares nickel with other metals.
