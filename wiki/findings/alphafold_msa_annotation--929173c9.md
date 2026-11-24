---
type: "Finding"
description: "Among bacterial paradox proteins, 286,439 (68.9%) are hypothetical, with no functional annotation."
finding_id: "alphafold_msa_annotation--929173c9"
result: "observation"
source: "alphafold_msa_annotation"
quantities: [{"value": "286,439", "what": "hypothetical paradox proteins", "unit": "", "denominator": "", "scope": ""}, {"value": "68.9%", "what": "share hypothetical among paradox proteins", "unit": "", "denominator": "", "scope": ""}]
caveat: "The 71% of gene clusters without AlphaFold entries skews toward poorly characterised organisms and likely harbours a larger annotation gap than the analysed subset."
first_added: "2026-11-24"
source_hash: "f66f0c9679cde23e009a56a030fe65d0d4efb49b7f8d057511382970661ac7e1"
---
# Structurally novel conserved core proteins are mostly hypothetical

Among bacterial paradox proteins, 286,439 (68.9%) are hypothetical, with no functional annotation. [src: alphafold_msa_annotation]

## Key figures

- **286,439**: hypothetical paradox proteins [src: alphafold_msa_annotation]
- **68.9%**: share hypothetical among paradox proteins [src: alphafold_msa_annotation]

## Evidence

> | Hypothetical (no functional annotation) | 286,439 (**68.9%**) | [src: alphafold_msa_annotation]

From the report [[summaries/alphafold_msa_annotation__REPORT]].

## Caveat

The 71% of gene clusters without AlphaFold entries skews toward poorly characterised organisms and likely harbours a larger annotation gap than the analysed subset. [src: alphafold_msa_annotation]

> The 71% without AlphaFold entries skews toward poorly characterised organisms and likely harbours a larger annotation gap than the analysed subset. [src: alphafold_msa_annotation]

## Other caveats in this report

- The report states that lower hypothetical rates in core than accessory bacterial genes appear to contradict H2 as literally stated, but that the paradox-protein census resolves this tension. [src: alphafold_msa_annotation]
- The bacterial analysis is biased toward better-studied diversity because well-characterised organisms with reference proteomes, including E. coli, Pseudomonas, and Bacillus, are over-represented in UniProt. [src: alphafold_msa_annotation]
- The report suggests the annotation gap for the remaining 70.7% of bacterial clusters is likely larger than in the covered subset. [src: alphafold_msa_annotation]
- The analysis has 29.3% bridge coverage and includes only gene clusters with a non-UPI UniProt accession. [src: alphafold_msa_annotation]
- MSA depth is obtained only for the gene cluster representative, ignoring within-cluster diversity, so it may be higher or lower than that of the typical cluster member. [src: alphafold_msa_annotation]
