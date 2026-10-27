---
type: "Research direction"
description: "Do genera enriched (Herbaspirillum) or depleted (Caulobacter) at high-uranium Oak Ridge sites respond to uranium itself, or to co-varying pH, oxygen and carbon, and can laboratory metal fitness predict that field response?"
hypothesis: "The uranium associations of Herbaspirillum and Caulobacter weaken or vanish after conditioning on pH and oxygen, whereas uranium-specific laboratory fitness predicts field response better than the aggregate tolerance score."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The abundance-fitness comparison exists in lab_field_ecology, but conditioning needs covariate modelling and the isolate gradient assays need new laboratory measurements."
collections: ["enigma-coral", "kescience-fitnessbrowser"]
findings: ["lab_field_ecology--7268dc9b", "lab_field_ecology--c4028be7", "lab_field_ecology--0a8de054", "lab_field_ecology--94b20be5", "lab_field_ecology--20abf7b5"]
conflicts: []
papers: ["26676055", "30523276", "29769716", "25968645"]
builds_on: ["findings/lab_field_ecology--7268dc9b", "findings/lab_field_ecology--c4028be7", "findings/lab_field_ecology--0a8de054", "findings/lab_field_ecology--94b20be5", "findings/lab_field_ecology--20abf7b5"]
projects: ["lab_field_ecology"]
topics: ["subsurface-and-soil-community-ecology"]
---
# Does uranium itself select Herbaspirillum and Caulobacter, or do covarying pH and redox?

Do genera enriched (Herbaspirillum) or depleted (Caulobacter) at high-uranium Oak Ridge sites respond to uranium itself, or to co-varying pH, oxygen and carbon, and can laboratory metal fitness predict that field response?

## Hypothesis

The uranium associations of Herbaspirillum and Caulobacter weaken or vanish after conditioning on pH and oxygen, whereas uranium-specific laboratory fitness predicts field response better than the aggregate tolerance score.

## Why it matters

It would show whether laboratory fitness assays can predict field community response to contamination, or whether pH and other covariates mostly decide which taxa persist.

## How to test it

Using the 108-site Oak Ridge abundance data with uranium, pH, redox and carbon measures, fit CCA/RDA (constrained ordination) or partial correlations per genus, with uranium conditioned on pH and oxygen. Then correlate uranium-specific Fitness Browser fitness with field uranium response, rather than the aggregate score (rho=0.503, p=0.095, n=12 genera). Desulfovibrio (maximum 0.09% relative abundance) is too rare for a reliable correlation, so exclude it from the test. The field data are genus-level while Fitness Browser fitness comes from particular strains, so treat genus-to-strain transfer as a limitation. Test Caulobacter and Herbaspirillum isolates in uranium gradients crossed with pH.

## What would support or refute it

Support: associations weaken or vanish under pH conditioning, and uranium-specific fitness predicts field response better than the aggregate. Refutation: associations persist after conditioning, or per-metal scores perform no better.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The abundance-fitness comparison exists in lab_field_ecology, but conditioning needs covariate modelling and the isolate gradient assays need new laboratory measurements.

- Collection: [[data/enigma-coral|ENIGMA CORAL]]
- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/lab_field_ecology--7268dc9b|Caulobacter is depleted at high-uranium sites]] (In tension with retrieved work)
- Finding: [[findings/lab_field_ecology--c4028be7|Herbaspirillum is enriched at high-uranium sites]] (Extends retrieved work)
- Finding: [[findings/lab_field_ecology--0a8de054|Aggregate lab metal tolerance does not significantly predict field uranium response]] (Insufficient literature evidence)
- Finding: [[findings/lab_field_ecology--94b20be5|Desulfovibrio and Pseudomonas show no uranium correlation despite being ENIGMA model organisms]] (Insufficient literature evidence)
- Finding: [[findings/lab_field_ecology--20abf7b5|Fitness Browser genera show significant uranium correlations at Oak Ridge]] (Insufficient literature evidence)

## Closest published work

- [PMID 26676055](https://pubmed.ncbi.nlm.nih.gov/26676055/) The long-term effect of uranium and pH on the community composition of an artificial consortium.
- [PMID 30523276](https://pubmed.ncbi.nlm.nih.gov/30523276/) The selective pressures on the microbial community in a metal-contaminated aquifer.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 25968645](https://pubmed.ncbi.nlm.nih.gov/25968645/) Natural bacterial communities serve as quantitative geochemical biosensors.

PMID 26676055 shows Caulobacter OR37 persisting with uranium in a synthetic consortium and PMID 30523276 links Rhodanobacter to uranium and low pH, but neither tests whether Fitness Browser-derived tolerance predicts field response while conditioning on pH.
