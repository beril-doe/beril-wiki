---
type: "Finding"
description: "Bacterial paradox proteins have a 68.9% hypothetical rate compared with 3.8% for core genes overall."
finding_id: "alphafold_msa_annotation--3d2c7388"
result: "observation"
source: "alphafold_msa_annotation"
quantities: [{"value": "68.9%", "what": "hypothetical rate in paradox subset", "unit": "", "denominator": "", "scope": ""}, {"value": "3.8%", "what": "hypothetical rate in all core genes", "unit": "", "denominator": "", "scope": ""}]
caveat: "Well-characterised organisms such as E. coli, Pseudomonas and Bacillus are over-represented in UniProt, so the analysis is biased toward better-studied diversity."
first_added: "2026-11-24"
source_hash: "f66f0c9679cde23e009a56a030fe65d0d4efb49b7f8d057511382970661ac7e1"
---
# Paradox subset differs sharply from core genes overall in hypothetical rate

Bacterial paradox proteins have a 68.9% hypothetical rate compared with 3.8% for core genes overall. [src: alphafold_msa_annotation]

## Key figures

- **68.9%**: hypothetical rate in paradox subset [src: alphafold_msa_annotation]
- **3.8%**: hypothetical rate in all core genes [src: alphafold_msa_annotation]

## Evidence

> The paradox proteins are qualitatively different from core genes overall: while the global core hypothetical rate is 3.8%, within the paradox subset it is 68.9%. [src: alphafold_msa_annotation]

From the report [[summaries/alphafold_msa_annotation__REPORT]].

## Caveat

Well-characterised organisms such as E. coli, Pseudomonas and Bacillus are over-represented in UniProt, so the analysis is biased toward better-studied diversity. [src: alphafold_msa_annotation]

> This 29.3% coverage is not random: well-characterised organisms with established reference proteomes (e.g., *E. coli*, *Pseudomonas*, *Bacillus*) are over-represented in UniProt. The analysis is therefore biased toward the better-studied portion of bacterial diversity, and the annotation gap for the remaining 70.7% is likely larger. [src: alphafold_msa_annotation]

## Other caveats in this report

- The report states that lower hypothetical rates in core than accessory bacterial genes appear to contradict H2 as literally stated, but that the paradox-protein census resolves this tension. [src: alphafold_msa_annotation]
- The report suggests the annotation gap for the remaining 70.7% of bacterial clusters is likely larger than in the covered subset. [src: alphafold_msa_annotation]
- The analysis has 29.3% bridge coverage and includes only gene clusters with a non-UPI UniProt accession. [src: alphafold_msa_annotation]
- The 71% of gene clusters without AlphaFold entries skew toward poorly characterised organisms and likely harbour a larger annotation gap than the analysed subset. [src: alphafold_msa_annotation]
- MSA depth is obtained only for the gene cluster representative, ignoring within-cluster diversity, so it may be higher or lower than that of the typical cluster member. [src: alphafold_msa_annotation]
