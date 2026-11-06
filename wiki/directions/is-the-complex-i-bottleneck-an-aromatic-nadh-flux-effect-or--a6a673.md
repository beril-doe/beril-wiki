---
type: "Research direction"
description: "In Acinetobacter baylyi ADP1, are Complex I defects driven by high NADH flux on aromatic substrates, or by a separate requirement on acetate and succinate involving an unannotated gene such as ACIAD3522?"
hypothesis: "Native Complex I defects are stronger on aromatic substrates than on glucose because aromatic catabolism loads the NADH pool, while ACIAD3522's acetate-specific defect (ratio 0.013 on acetate versus 1.39 on quinate and glucose) reflects a distinct acetate function that the model does not capture."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Mutant construction and NADH/NAD+ measurement are not in the lakehouse; only the pangenome co-occurrence search is computable now."
collections: ["kbase-ke-pangenome"]
findings: ["acinetobacter_adp1_explorer--886c47ff"]
conflicts: ["conflict--metabolic-model-gapfilling--bf4946ce"]
papers: ["18319726", "18840283"]
builds_on: ["findings/acinetobacter_adp1_explorer--886c47ff", "conflicts/conflict--metabolic-model-gapfilling--bf4946ce"]
projects: ["acinetobacter_adp1_explorer", "aromatic_catabolism_network"]
topics: ["metabolic-models-and-pathway-level-evidence"]
---
# Is the Complex I bottleneck an aromatic NADH-flux effect or a separate acetate-specific requirement?

In Acinetobacter baylyi ADP1, are Complex I defects driven by high NADH flux on aromatic substrates, or by a separate requirement on acetate and succinate involving an unannotated gene such as ACIAD3522?

## Hypothesis

Native Complex I defects are stronger on aromatic substrates than on glucose because aromatic catabolism loads the NADH pool, while ACIAD3522's acetate-specific defect (ratio 0.013 on acetate versus 1.39 on quinate and glucose) reflects a distinct acetate function that the model does not capture.

## Why it matters

The two readings predict opposite uses of model flux: whether elevated predicted flux (1.76x for Complex I) can prioritise condition-specific essential genes. They also bear on how respiratory wiring is organised across carbon sources.

## How to test it

In ADP1, construct Complex I subunit, NDH-2 and ACIAD3522 deletions and measure growth on quinate, glucose, acetate, succinate, lactate and urea, with NADH/NAD+ ratios. Compare native defects with the transferred-ortholog pattern (10/13 operon-subunit defects). Test whether the earlier compensation null (Complex I aromatic deficits of -0.297 with validated NDH-2 versus -0.156 without, p = 0.52, direction opposite to compensation) holds when NDH-2 status is established by gene deletion rather than text-based annotation. Search the Pangenome Collection for co-occurrence of NDH-2 (K03885) and Complex I (K00330-K00343) across species.

## What would support or refute it

Support: native Complex I defects are larger on aromatic than non-aromatic substrates, NADH/NAD+ is higher on quinate, and ACIAD3522 deletion reproduces the acetate-specific defect independently of Complex I. Refute: Complex I defects are as strong on acetate and succinate as on quinate, or NDH-2 deletion changes nothing. The earlier p = 0.52 null does not show compensation is absent.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Mutant construction and NADH/NAD+ measurement are not in the lakehouse; only the pangenome co-occurrence search is computable now.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/acinetobacter_adp1_explorer--886c47ff|ADP1 is absent from the Fitness Browser]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--metabolic-model-gapfilling--bf4946ce|Does Model-Predicted Flux Locate Respiratory Bottlenecks in Aromatic Catabolism?]]

## Closest published work

- [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/) A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1.
- [PMID 18840283](https://pubmed.ncbi.nlm.nih.gov/18840283/) Iterative reconstruction of a global metabolic model of Acinetobacter baylyi ADP1 using high-throughput growth phenotype and gene essentiality data.

PMID 18319726 and 18840283 provide the ADP1 deletion collection and a model refined against essentiality data, but not respiratory-chain wiring across carbon sources or the acetate-specific effect of ACIAD3522.
