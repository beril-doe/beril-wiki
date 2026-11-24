---
type: "Finding"
description: "The report resolves the apparent contradiction that core genes have lower hypothetical rates yet harbour 415K structurally unprecedented proteins by distinguishing an MSA-depth-driven gap and a pangenome-class gap."
finding_id: "alphafold_msa_annotation--0d54bd05"
result: "correction"
source: "alphafold_msa_annotation"
quantities: [{"value": "18\u00d7", "what": "span in domain hits explained by the MSA-depth-driven gap", "unit": "", "denominator": "", "scope": ""}]
caveat: "Lower hypothetical rates in core than accessory genes appear to contradict H2 as literally stated, and the paradox protein census resolves the tension."
first_added: "2026-11-24"
source_hash: "f66f0c9679cde23e009a56a030fe65d0d4efb49b7f8d057511382970661ac7e1"
---
# Core genes' lower hypothetical rate coexists with a structurally novel subset

The report resolves the apparent contradiction that core genes have lower hypothetical rates yet harbour 415K structurally unprecedented proteins by distinguishing an MSA-depth-driven gap and a pangenome-class gap. [src: alphafold_msa_annotation]

## Key figures

- **18×**: span in domain hits explained by the MSA-depth-driven gap [src: alphafold_msa_annotation]

## Evidence

> The apparent contradiction in H2 — core genes have lower hypothetical rates yet harbour 415K structurally unprecedented proteins — resolves by recognising two distinct drivers of the annotation gap: - **MSA-depth-driven gap**: applies to all classes, explains the 18× span in domain hits, and is captured by H3. - **Pangenome-class gap**: accessory/singleton genes carry more hypothetical proteins independent of MSA depth, likely due to horizontal transfer, rapid evolution, and taxonomically narrow distribution. [src: alphafold_msa_annotation]

From the report [[summaries/alphafold_msa_annotation__REPORT]].

## Caveat

Lower hypothetical rates in core than accessory genes appear to contradict H2 as literally stated, and the paradox protein census resolves the tension. [src: alphafold_msa_annotation]

> This appears to contradict H2 as literally stated — but the paradox protein census (H4) resolves the tension: within core genes, the subset with msa_depth < 10 has a 68.9% hypothetical rate, versus 3.8% for all core genes. [src: alphafold_msa_annotation]

## Other caveats in this report

- The bacterial analysis is biased toward better-studied diversity because well-characterised organisms with reference proteomes, including E. coli, Pseudomonas, and Bacillus, are over-represented in UniProt. [src: alphafold_msa_annotation]
- The report suggests the annotation gap for the remaining 70.7% of bacterial clusters is likely larger than in the covered subset. [src: alphafold_msa_annotation]
- The analysis has 29.3% bridge coverage and includes only gene clusters with a non-UPI UniProt accession. [src: alphafold_msa_annotation]
- The 71% of gene clusters without AlphaFold entries skew toward poorly characterised organisms and likely harbour a larger annotation gap than the analysed subset. [src: alphafold_msa_annotation]
- MSA depth is obtained only for the gene cluster representative, ignoring within-cluster diversity, so it may be higher or lower than that of the typical cluster member. [src: alphafold_msa_annotation]
