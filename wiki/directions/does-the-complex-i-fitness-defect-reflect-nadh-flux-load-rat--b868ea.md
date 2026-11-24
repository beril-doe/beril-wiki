---
type: "Research direction"
description: "Is Complex I needed on aromatics because of the NADH flux they produce, with the defect tracking NADH yield across carbon sources?"
hypothesis: "Complex I fitness defects scale with the NADH generated per carbon source, so acetate and succinate defects equal or exceed those on aromatics, and the DUF proteins ACIAD3137 and ACIAD2176 share this pattern."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The cross-organism analysis uses catalog tables, but the NADH and mutant growth measurements are not in the catalog."
databases: ["kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.ortholog", "kescience.fitnessbrowser.cofit", "kescience.fitnessbrowser.experiment", "kescience.fitnessbrowser.gene"]
findings: ["aromatic_catabolism_network--3128e9e3", "aromatic_catabolism_network--3a51f6c6", "aromatic_catabolism_network--7b656f0f", "aromatic_catabolism_network--7d6bd2aa"]
conflicts: []
papers: ["18319726", "25374488", "25968644"]
builds_on: ["findings/aromatic_catabolism_network--3128e9e3", "findings/aromatic_catabolism_network--3a51f6c6", "findings/aromatic_catabolism_network--7b656f0f", "findings/aromatic_catabolism_network--7d6bd2aa"]
projects: ["aromatic_catabolism_network"]
topics: ["gene-fitness-landscapes-and-cofitness-modules"]
---
# Does the Complex I fitness defect reflect NADH flux load rather than aromatic substrate?

Is Complex I needed on aromatics because of the NADH flux they produce, with the defect tracking NADH yield across carbon sources?

## Hypothesis

Complex I fitness defects scale with the NADH generated per carbon source, so acetate and succinate defects equal or exceed those on aromatics, and the DUF proteins ACIAD3137 and ACIAD2176 share this pattern.

## Why it matters

It would replace an aromatic-specific explanation with a general redox-load one, and flag candidate accessory factors of Complex I.

## How to test it

Using Fitness Browser nuo orthologs and cofitness across organisms, regress Complex I fitness on estimated NADH yield per carbon source, controlling for organism. Check whether homologs of ACIAD3137 and ACIAD2176 cofit with nuo genes in other organisms. Then measure NADH/NAD+ ratio and nuo or NDH-2 mutant growth on quinate, acetate and glucose in ADP1.

## What would support or refute it

Support: defect size tracks NADH yield, and DUF homologs cofit with nuo elsewhere. Refute: aromatics remain worse after controlling for yield, or DUF homologs show no cofitness.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The cross-organism analysis uses catalog tables, but the NADH and mutant growth measurements are not in the catalog.

## Builds on

- Finding: [[findings/aromatic_catabolism_network--3128e9e3|Complex I orthologs are more defective on aromatics across Fitness Browser organisms]] (Candidate novel)
- Finding: [[findings/aromatic_catabolism_network--3a51f6c6|Complex I defects are largest on non-aromatic high-NADH substrates]] (Candidate novel)
- Finding: [[findings/aromatic_catabolism_network--7b656f0f|Two DUF proteins are candidate Complex I accessory factors]] (Candidate novel)
- Finding: [[findings/aromatic_catabolism_network--7d6bd2aa|FBA predicts no Complex I essentiality despite higher flux]] (Candidate novel)

## Closest published work

- [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/) A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1.
- [PMID 25374488](https://pubmed.ncbi.nlm.nih.gov/25374488/) Novel metabolic features in Acinetobacter baylyi ADP1 revealed by a multiomics approach.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.

18319726 and 25374488 phenotype ADP1 on quinate but do not report Complex I fitness or flux-load dependence.
