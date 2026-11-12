---
type: "Research direction"
description: "Why can growth on amino acids, nucleosides and some carbon sources be predicted from the presence of gene families, while metal, antibiotic and nitrogen conditions cannot?"
hypothesis: "Tolerance phenotypes depend on gene copy number or regulatory variants of resistance genes rather than their presence, so adding copy number and promoter variants for efflux and detoxification genes will improve prediction for these conditions where presence alone fails."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "The existing genome-to-growth corpus lacks graded-dose tolerance measurements and copy-number or promoter-variant data, so these must be measured."
databases: []
tables: []
findings: ["genotype_to_phenotype_enigma--602fd76d", "genotype_to_phenotype_enigma--ccab2bff"]
conflicts: []
papers: []
builds_on: ["findings/genotype_to_phenotype_enigma--602fd76d", "findings/genotype_to_phenotype_enigma--ccab2bff"]
projects: ["genotype_to_phenotype_enigma"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Is metal and antibiotic tolerance unpredictable from gene content because of gene dosage?

Why can growth on amino acids, nucleosides and some carbon sources be predicted from the presence of gene families, while metal, antibiotic and nitrogen conditions cannot?

## Hypothesis

Tolerance phenotypes depend on gene copy number or regulatory variants of resistance genes rather than their presence, so adding copy number and promoter variants for efflux and detoxification genes will improve prediction for these conditions where presence alone fails.

## Why it matters

If tolerance depends on dosage and regulation, genome-based prediction of resistance and metal tolerance needs different features than metabolic growth prediction, and presence-based surveys of resistance genes will mislead.

## How to test it

Choose a panel of strains from the Oak Ridge isolate collection spanning several genera, and measure growth with graded doses of several metals and antibiotics. Sequence them to determine copy number and promoter variants of known resistance and efflux genes. Compare models using presence alone with models adding copy number and promoter variants, holding out whole genera.

## What would support or refute it

Support: dosage and regulatory features raise held-out prediction for metals and antibiotics while leaving presence-only models unimproved. Refute: prediction stays poor with these features, pointing to unmeasured factors such as plasmids or physiology.

## Data

Approach: experiment. Readiness: needs new measurements. The existing genome-to-growth corpus lacks graded-dose tolerance measurements and copy-number or promoter-variant data, so these must be measured.

## Builds on

- Finding: [[findings/genotype_to_phenotype_enigma--602fd76d|Binary growth is predictable from gene content only for some condition classes]] (Insufficient literature evidence)
- Finding: [[findings/genotype_to_phenotype_enigma--ccab2bff|Continuous growth parameters are not predictable across genera from gene content]] (Insufficient literature evidence)
