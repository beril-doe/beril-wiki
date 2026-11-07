---
type: "Research direction"
description: "Within the dominant phylum Pseudomonadota, do isolates from heavy-metal-contaminated sites score higher on predicted metal tolerance because they carry more accessory (not present in most genomes of the species) metal-resistance gene clusters, rather than more of the shared core clusters?"
hypothesis: "The score difference between contamination and environmental isolates comes mainly from accessory metal-resistance clusters, and the difference grows with contamination intensity. Core metal clusters will not differ between the two groups when species are matched."
approach: "lakehouse analysis"
readiness: "data in the lakehouse"
readiness_basis: "The metal scores and isolation-source bridge already exist; the heavy-metal group is only 10 matched isolates, the score is a genome-based prediction, and the two name-based bridges disagree on coverage, so the size of the advantage is only roughly known."
collections: ["kbase-ke-pangenome", "kbase-phenotype", "kescience-fitnessbrowser"]
findings: ["bacdive_metal_validation--09db2bda", "bacdive_metal_validation--1ac30de6", "bacdive_metal_validation--60f073d0", "bacdive_metal_validation--894e1826", "field_vs_lab_fitness--296eadf6"]
conflicts: ["conflict--taxonomic-nomenclature-reconciliation--2208cd83", "conflict--taxonomic-nomenclature-reconciliation--a209158c"]
papers: ["41601069", "33540257", "35107332", "37065130"]
builds_on: ["findings/bacdive_metal_validation--09db2bda", "findings/bacdive_metal_validation--1ac30de6", "findings/bacdive_metal_validation--60f073d0", "findings/bacdive_metal_validation--894e1826", "findings/field_vs_lab_fitness--296eadf6", "conflicts/conflict--taxonomic-nomenclature-reconciliation--2208cd83", "conflicts/conflict--taxonomic-nomenclature-reconciliation--a209158c"]
projects: ["bacdive_metal_validation", "bacdive_phenotype_metal_tolerance", "cf_formulation_design", "field_vs_lab_fitness"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Is the metal-tolerance advantage of contaminated-site bacteria carried by variable accessory gene clusters?

Within the dominant phylum Pseudomonadota, do isolates from heavy-metal-contaminated sites score higher on predicted metal tolerance because they carry more accessory (not present in most genomes of the species) metal-resistance gene clusters, rather than more of the shared core clusters?

## Hypothesis

The score difference between contamination and environmental isolates comes mainly from accessory metal-resistance clusters, and the difference grows with contamination intensity. Core metal clusters will not differ between the two groups when species are matched.

## Why it matters

If correct, tolerance in polluted habitats tracks variable gene content rather than a fixed species-wide trait, which changes how contamination-site isolates should be screened and how tolerance scores are built. Accessory status alone does not show the genes were horizontally transferred; that would be a follow-up question.

## How to test it

Using the Pangenome Collection linked to isolation sources in the Phenotype Collection, split each isolate's metal-resistance clusters into core and accessory for its species. Compare contamination versus environmental isolates within Pseudomonadota, separately for heavy-metal, waste or sludge, and industrial contamination, and for host-associated isolates, with species matched. Check whether the stepwise ordering by contamination category holds for accessory clusters only. Repeat using genome-accession matching instead of species-name matching, because the two bridges between the strain database and the pangenome give different coverage and suffix-stripping of species names may merge distinct clades. Compare against Fitness Browser metal-important genes in Desulfovibrio vulgaris Hildenborough, which showed no clear deficit in core share relative to baseline.

## What would support or refute it

Support: the difference sits in accessory clusters and rises with contamination intensity, with core clusters similar in both groups, under both matching routes. Refutation: the difference appears equally in core clusters, or disappears when species are matched or when accession matching replaces name matching.

## Data

Approach: lakehouse analysis. Readiness: data in the lakehouse. The metal scores and isolation-source bridge already exist; the heavy-metal group is only 10 matched isolates, the score is a genome-based prediction, and the two name-based bridges disagree on coverage, so the size of the advantage is only roughly known.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-phenotype|Phenotype Collection]]
- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/bacdive_metal_validation--09db2bda|Heavy-metal contamination isolates score higher on predicted metal tolerance than baseline]] (Insufficient literature evidence)
- Finding: [[findings/bacdive_metal_validation--1ac30de6|Contamination signal persists within the dominant phylum Pseudomonadota]] (Extends retrieved work)
- Finding: [[findings/bacdive_metal_validation--60f073d0|Metal-tolerance score effect appears to grade with contamination category]] (Insufficient literature evidence)
- Finding: [[findings/bacdive_metal_validation--894e1826|Host-associated bacteria scored higher, reversing the predicted direction]] (Insufficient literature evidence)
- Finding: [[findings/field_vs_lab_fitness--296eadf6|Heavy-metal fitness genes are not significantly less core than baseline]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--taxonomic-nomenclature-reconciliation--2208cd83|BacDive-to-pangenome coverage: does strain matching reach 43.4% or 38.4%?]]
- Conflict: [[conflicts/conflict--taxonomic-nomenclature-reconciliation--a209158c|Does GTDB suffix removal reconcile species names or merge distinct clades?]]

## Closest published work

- [PMID 41601069](https://pubmed.ncbi.nlm.nih.gov/41601069/) Co-selection for heavy metal and multidrug resistance: Cadmium primes bacterial antibiotic resistance by enhancing intrinsic oxidative stress tolerance.
- [PMID 33540257](https://pubmed.ncbi.nlm.nih.gov/33540257/) Heavy metal pollution promotes antibiotic resistance potential in the aquatic environment.
- [PMID 35107332](https://pubmed.ncbi.nlm.nih.gov/35107332/) Genomic Features and Pervasive Negative Selection in Rhodanobacter Strains Isolated from Nitrate and Heavy Metal Contaminated Aquifer.
- [PMID 37065130](https://pubmed.ncbi.nlm.nih.gov/37065130/) Large-scale genetic characterization of the model sulfate-reducing bacterium, Desulfovibrio vulgaris Hildenborough.

PMID 41601069 and PMID 33540257 link contamination to resistance at community level. PMID 37065130 reports Desulfovibrio fitness genes. None splits an isolate-level contamination signal into core versus accessory clusters.
