---
type: "Research direction"
description: "In Acinetobacter baylyi ADP1, is the gene ACIAD3522 needed for acetate growth because it works in respiratory NADH oxidation, or because it acts in acetate catabolism itself, and is Complex I's aromatic requirement real in ADP1?"
hypothesis: "ACIAD3522 is a flavin-dependent enzyme of acetate catabolism, not a respiratory dehydrogenase, and Complex I subunit defects in ADP1 are as strong on acetate and succinate as on quinate."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "Deletion mutants exist in the published ADP1 collection but growth, redox and rescue data on these substrates are not in the lakehouse."
collections: ["kbase-ke-pangenome"]
findings: []
conflicts: ["conflict--metabolic-model-gapfilling--bf4946ce"]
papers: ["18319726", "18840283"]
builds_on: ["conflicts/conflict--metabolic-model-gapfilling--bf4946ce"]
projects: ["aromatic_catabolism_network"]
topics: ["metabolic-models-and-pathway-level-evidence"]
---
# Is the acetate-specific defect of ACIAD3522 a respiratory role or an acetate catabolism role?

In Acinetobacter baylyi ADP1, is the gene ACIAD3522 needed for acetate growth because it works in respiratory NADH oxidation, or because it acts in acetate catabolism itself, and is Complex I's aromatic requirement real in ADP1?

## Hypothesis

ACIAD3522 is a flavin-dependent enzyme of acetate catabolism, not a respiratory dehydrogenase, and Complex I subunit defects in ADP1 are as strong on acetate and succinate as on quinate.

## Why it matters

Higher modelled Complex I flux on aromatics was read as an aromatic-specific bottleneck, while ortholog-transferred defects were strongest on non-aromatic substrates. Settling this decides whether model flux can point to condition-specific essential genes. It would also give a function to a gene the model routes no flux through.

## How to test it

Use the ADP1 single-gene deletion collection to measure growth of the ACIAD3522 deletion and several Complex I subunit deletions on acetate, succinate, quinate and glucose. Add a deletion of a type 2 NADH dehydrogenase if one is found in the genome. Measure NADH to NAD+ balance and test whether acetate-grown deletion strains can be rescued by supplying a downstream intermediate.

## What would support or refute it

Deletions with a defect only on acetate and a rescue by a downstream intermediate would support a catabolic role. Equal Complex I defects across all four substrates would refute an aromatic-specific bottleneck. Defects confined to quinate would support the flux reading and refute the hypothesis.

## Data

Approach: experiment. Readiness: needs new measurements. Deletion mutants exist in the published ADP1 collection but growth, redox and rescue data on these substrates are not in the lakehouse.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Conflict: [[conflicts/conflict--metabolic-model-gapfilling--bf4946ce|Does Model-Predicted Flux Locate Respiratory Bottlenecks in Aromatic Catabolism?]]

## Closest published work

- [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/) A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1.
- [PMID 18840283](https://pubmed.ncbi.nlm.nih.gov/18840283/) Iterative reconstruction of a global metabolic model of Acinetobacter baylyi ADP1 using high-throughput growth phenotype and gene essentiality data.

PMID 18319726 provides the deletion collection and PMID 18840283 the metabolic model; neither tests whether elevated modelled respiratory flux predicts condition-specific essentiality.
