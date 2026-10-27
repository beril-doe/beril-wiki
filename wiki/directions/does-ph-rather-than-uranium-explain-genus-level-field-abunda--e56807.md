---
type: "Research direction"
description: "Is Caulobacter depletion (and Herbaspirillum enrichment) at high-uranium Oak Ridge sites a response to uranium, or to co-varying pH, oxygen and carbon, given Caulobacter's tolerance of uranium in a synthetic consortium?"
hypothesis: "Caulobacter and Herbaspirillum 16S abundance associations with uranium shrink toward zero once pH, oxygen and carbon are modelled. Caulobacter uranium tolerance in isolates depends on pH."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The covariate model needs geochemistry linkage that is reported incomplete, and the isolate pH-tolerance assays are new measurements."
collections: ["enigma-coral"]
findings: ["lab_field_ecology--7268dc9b", "lab_field_ecology--c4028be7", "lab_field_ecology--20abf7b5"]
conflicts: []
papers: ["26676055", "30523276", "35107332"]
builds_on: ["findings/lab_field_ecology--7268dc9b", "findings/lab_field_ecology--c4028be7", "findings/lab_field_ecology--20abf7b5"]
projects: ["lab_field_ecology"]
topics: ["laboratory-fitness-versus-natural-selection-and-gene-conservation"]
---
# Does pH rather than uranium explain genus-level field abundance patterns at Oak Ridge?

Is Caulobacter depletion (and Herbaspirillum enrichment) at high-uranium Oak Ridge sites a response to uranium, or to co-varying pH, oxygen and carbon, given Caulobacter's tolerance of uranium in a synthetic consortium?

## Hypothesis

Caulobacter and Herbaspirillum 16S abundance associations with uranium shrink toward zero once pH, oxygen and carbon are modelled. Caulobacter uranium tolerance in isolates depends on pH.

## Why it matters

It would clarify whether genus-level field correlations carry causal information about metal selection, and whether lab metal tolerance should be expected to predict field abundance.

## How to test it

Analysis: using ENIGMA CORAL 16S abundance and site geochemistry, fit partial-correlation or CCA models for Caulobacter (rho -0.411, FDR q=1.1e-4) and Herbaspirillum (rho +0.336, FDR q=0.001) with uranium, pH, oxygen and carbon source as covariates. Geochemistry-to-sample linkage was reported incomplete. Experiment: test uranium tolerance of Caulobacter isolates across pH levels. The field result is genus-level 16S abundance, so isolate growth can show plausible mechanism but cannot directly explain the genus-level association.

## What would support or refute it

Support: uranium coefficients lose significance after covariates and isolate tolerance varies with pH. Refute: uranium remains a significant predictor after adjustment and isolate sensitivity does not depend on pH.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The covariate model needs geochemistry linkage that is reported incomplete, and the isolate pH-tolerance assays are new measurements.

- Collection: [[data/enigma-coral|ENIGMA CORAL]]

## Builds on

- Finding: [[findings/lab_field_ecology--7268dc9b|Caulobacter is depleted at high-uranium sites]] (In tension with retrieved work)
- Finding: [[findings/lab_field_ecology--c4028be7|Herbaspirillum is enriched at high-uranium sites]] (Extends retrieved work)
- Finding: [[findings/lab_field_ecology--20abf7b5|Fitness Browser genera show significant uranium correlations at Oak Ridge]] (Insufficient literature evidence)

## Closest published work

- [PMID 26676055](https://pubmed.ncbi.nlm.nih.gov/26676055/) The long-term effect of uranium and pH on the community composition of an artificial consortium.
- [PMID 30523276](https://pubmed.ncbi.nlm.nih.gov/30523276/) The selective pressures on the microbial community in a metal-contaminated aquifer.
- [PMID 35107332](https://pubmed.ncbi.nlm.nih.gov/35107332/) Genomic Features and Pervasive Negative Selection in Rhodanobacter Strains Isolated from Nitrate and Heavy Metal Contaminated Aquifer.

PMID 26676055 shows Caulobacter OR37 dominating with uranium in a synthetic consortium and PMID 30523276 correlates Rhodanobacter with uranium and low pH; neither models pH jointly with uranium for Caulobacter and Herbaspirillum in the field.
