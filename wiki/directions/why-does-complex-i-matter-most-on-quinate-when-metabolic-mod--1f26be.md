---
type: "Research direction"
description: "In Acinetobacter baylyi ADP1, Complex I is more essential on quinate than on glucose or acetate even though quinate gives fewer NADH per carbon, and flux balance analysis predicts no Complex I essentiality. Which model gaps explain the mismatch?"
hypothesis: "Adding reactions for the quinate-specific genes the model cannot map, including PQQ and iron supply steps, will make the model predict Complex I as more needed on quinate than on glucose."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "The catalog shows the reaction table and Fitness Browser tables; the ADP1 model and growth data were not shown, so the model rerun needs compute."
databases: ["kbase.msd_biochemistry", "kescience.fitnessbrowser"]
tables: ["kbase.msd_biochemistry.reaction", "kescience.fitnessbrowser.experiment", "kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.organism"]
findings: ["aromatic_catabolism_network--7d6bd2aa", "respiratory_chain_wiring--4e28db67", "aromatic_catabolism_network--3128e9e3", "aromatic_catabolism_network--3a51f6c6"]
conflicts: ["conflict--concordance-of-genome-scale-metabolic-model-predictions-with-experimental-data--c0666023"]
papers: ["18319726", "25374488"]
builds_on: ["findings/aromatic_catabolism_network--7d6bd2aa", "findings/respiratory_chain_wiring--4e28db67", "findings/aromatic_catabolism_network--3128e9e3", "findings/aromatic_catabolism_network--3a51f6c6", "conflicts/conflict--concordance-of-genome-scale-metabolic-model-predictions-with-experimental-data--c0666023"]
projects: ["acinetobacter_adp1_explorer", "adp1_triple_essentiality", "aromatic_catabolism_network", "respiratory_chain_wiring"]
topics: ["metabolic-models-and-pathway-level-evidence"]
---
# Why does Complex I matter most on quinate when metabolic models predict no need?

In Acinetobacter baylyi ADP1, Complex I is more essential on quinate than on glucose or acetate even though quinate gives fewer NADH per carbon, and flux balance analysis predicts no Complex I essentiality. Which model gaps explain the mismatch?

## Hypothesis

Adding reactions for the quinate-specific genes the model cannot map, including PQQ and iron supply steps, will make the model predict Complex I as more needed on quinate than on glucose.

## Why it matters

If the mismatch comes from missing cofactor-supply and regulatory content, model-based essentiality calls on aromatic substrates can be repaired. If not, the cause lies outside the network structure.

## How to test it

Take the 30 of 51 quinate-specific ADP1 genes with no reaction mapping. Add reactions for the PQQ and iron supply steps and for known regulators as constraints, using the ModelSEED reaction table. Rerun the model on quinate, glucose and acetate and compare predicted Complex I essentiality with the measured growth ratios. Then compare with ortholog-transferred Complex I fitness in the Fitness Browser on aromatic versus non-aromatic conditions. Follow with single-organism growth tests of Complex I and PQQ-pathway mutants on quinate if the model is improved.

## What would support or refute it

Support: predicted Complex I essentiality rises on quinate relative to glucose after the additions, in line with measured ratios. Refute: predicted essentiality stays near zero after the additions, or rises equally on acetate and succinate, where measured Complex I defects are also large.

## Data

Approach: analysis then experiment. Readiness: needs compute. The catalog shows the reaction table and Fitness Browser tables; the ADP1 model and growth data were not shown, so the model rerun needs compute.

## Builds on

- Finding: [[findings/aromatic_catabolism_network--7d6bd2aa|FBA predicts no Complex I essentiality despite higher flux]] (Candidate novel)
- Finding: [[findings/respiratory_chain_wiring--4e28db67|Complex I is most needed on the lowest-NADH-yield substrate]] (Candidate novel)
- Finding: [[findings/aromatic_catabolism_network--3128e9e3|Complex I orthologs are more defective on aromatics across Fitness Browser organisms]] (Candidate novel)
- Finding: [[findings/aromatic_catabolism_network--3a51f6c6|Complex I defects are largest on non-aromatic high-NADH substrates]] (Candidate novel)
- Conflict: [[conflicts/conflict--concordance-of-genome-scale-metabolic-model-predictions-with-experimental-data--c0666023|Concordance of Metabolic Model Predictions: 73.8% Database Agreement Versus Moderate Knockout Agreement]]

## Closest published work

- [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/) A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1.
- [PMID 25374488](https://pubmed.ncbi.nlm.nih.gov/25374488/) Novel metabolic features in Acinetobacter baylyi ADP1 revealed by a multiomics approach.

The ADP1 deletion collection (18319726) and the succinate-to-quinate multiomics study (25374488) cover the organism and substrates but not Complex I essentiality or model blind spots.
