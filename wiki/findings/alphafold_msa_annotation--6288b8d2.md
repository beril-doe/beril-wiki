---
type: "Finding"
description: "Across 38,051,842 bacterial gene cluster\u2013UniProt pairs, MSA depth and domain hit count are strongly positively correlated (Spearman \u03c1 = 0.756)."
finding_id: "alphafold_msa_annotation--6288b8d2"
result: "observation"
source: "alphafold_msa_annotation"
quantities: [{"value": "0.756", "what": "Spearman correlation between MSA depth and domain hit count", "unit": "", "denominator": "", "scope": ""}, {"value": "38,051,842", "what": "gene cluster\u2013UniProt pairs", "unit": "pairs", "denominator": "", "scope": ""}]
caveat: "The Spearman \u03c1 = 0.756 is computed on the full 38M-pair dataset without subgroup stratification."
first_added: "2026-11-24"
source_hash: "f66f0c9679cde23e009a56a030fe65d0d4efb49b7f8d057511382970661ac7e1"
---
# MSA depth tracks domain annotation richness across bacterial clusters

Across 38,051,842 bacterial gene cluster–UniProt pairs, MSA depth and domain hit count are strongly positively correlated (Spearman ρ = 0.756). [src: alphafold_msa_annotation]

## Key figures

- **0.756**: Spearman correlation between MSA depth and domain hit count [src: alphafold_msa_annotation]
- **38,051,842 pairs**: gene cluster–UniProt pairs [src: alphafold_msa_annotation]

## Evidence

> Across 38,051,842 gene cluster–UniProt pairs, MSA depth and domain hit count are strongly positively correlated (Spearman ρ = 0.756). [src: alphafold_msa_annotation]

From the report [[summaries/alphafold_msa_annotation__REPORT]].

## Caveat

The Spearman ρ = 0.756 is computed on the full 38M-pair dataset without subgroup stratification. [src: alphafold_msa_annotation]

> **H3 quantification**: Spearman ρ = 0.756 is computed on the full 38M-pair dataset without subgroup stratification. [src: alphafold_msa_annotation]

## Other caveats in this report

- The report states that lower hypothetical rates in core than accessory bacterial genes appear to contradict H2 as literally stated, but that the paradox-protein census resolves this tension. [src: alphafold_msa_annotation]
- The bacterial analysis is biased toward better-studied diversity because well-characterised organisms with reference proteomes, including E. coli, Pseudomonas, and Bacillus, are over-represented in UniProt. [src: alphafold_msa_annotation]
- The report suggests the annotation gap for the remaining 70.7% of bacterial clusters is likely larger than in the covered subset. [src: alphafold_msa_annotation]
- The analysis has 29.3% bridge coverage and includes only gene clusters with a non-UPI UniProt accession. [src: alphafold_msa_annotation]
- The 71% of gene clusters without AlphaFold entries skew toward poorly characterised organisms and likely harbour a larger annotation gap than the analysed subset. [src: alphafold_msa_annotation]
