---
type: "Research direction"
description: "Do substrates missing from the 22 tested carbon sources give selective growth to protective commensals over P. aeruginosa?"
hypothesis: "At least one substrate class predicted by genomic pathway analysis but not yet tested, such as a sugar alcohol or polyamine, supports growth of candidate commensals at a clearly higher rate than P. aeruginosa."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Pathway predictions are in the catalog; the growth assays are new measurements."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.gapmind_pathways", "kbase.ke_pangenome.gtdb_taxonomy_r214v1", "kbase.ke_pangenome.genome"]
findings: ["cf_formulation_design--32945b8a", "cf_formulation_design--87394070"]
conflicts: []
papers: ["17873029", "23707554", "34588194", "35174108"]
builds_on: ["findings/cf_formulation_design--32945b8a", "findings/cf_formulation_design--87394070"]
projects: ["cf_formulation_design"]
topics: ["translational-microbiome-and-phage-therapeutics"]
---
# Can untested nutrients such as mucins, polyamines or sugar alcohols favor commensals over Pseudomonas aeruginosa?

Do substrates missing from the 22 tested carbon sources give selective growth to protective commensals over P. aeruginosa?

## Hypothesis

At least one substrate class predicted by genomic pathway analysis but not yet tested, such as a sugar alcohol or polyamine, supports growth of candidate commensals at a clearly higher rate than P. aeruginosa.

## Why it matters

No selective prebiotic was found among the tested substrates. A selective one would let a formulation be paired with a feeding strategy that does not depend on engraftment alone.

## How to test it

Score pathway completeness for sugar-alcohol, polyamine and mucin-derived sugar catabolism across genomes of P. aeruginosa and the candidate commensals using the pangenome pathway predictions. Then run sole-carbon growth assays for the top predicted substrates on the candidate commensals and on P. aeruginosa strains of both ExoU+ and ExoS+ types.

## What would support or refute it

Support: a substrate where commensals grow and P. aeruginosa grows poorly. Refute: all predicted substrates are used equally well by the pathogen, extending the null result.

## Data

Approach: analysis then experiment. Readiness: needs compute. Pathway predictions are in the catalog; the growth assays are new measurements.

## Builds on

- Finding: [[findings/cf_formulation_design--32945b8a|No selective amino acid or sugar prebiotic among tested substrates]] (Candidate novel)
- Finding: [[findings/cf_formulation_design--87394070|PA14 assay strain is unrepresentative of cystic fibrosis isolates]] (Extends retrieved work)

## Closest published work

- [PMID 17873029](https://pubmed.ncbi.nlm.nih.gov/17873029/) Nutritional cues control Pseudomonas aeruginosa multicellular behavior in cystic fibrosis sputum.
- [PMID 23707554](https://pubmed.ncbi.nlm.nih.gov/23707554/) Probiotic strategies for treatment of respiratory diseases.
- [PMID 34588194](https://pubmed.ncbi.nlm.nih.gov/34588194/) R othia mucilaginosa is an anti-inflammatory bacterium in the respiratory tract of patients with chronic lung disease.
- [PMID 35174108](https://pubmed.ncbi.nlm.nih.gov/35174108/) Commensal Bacteria in the Cystic Fibrosis Airway Microbiome Reduce P. aeruginosa Induced Inflammation.

17873029 describes sputum nutrition and P. aeruginosa substrate preferences, but no retrieved paper screens substrates for selectivity toward commensals.
