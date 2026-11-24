---
type: "Finding"
description: "Bacterial core gene clusters have median MSA depth 15,308, 2.89\u00d7 higher than the auxiliary+singleton median of 5,299 and 2.77\u00d7 higher than the auxiliary non-singleton median of 5,527."
finding_id: "alphafold_msa_annotation--164a1689"
result: "observation"
source: "alphafold_msa_annotation"
quantities: [{"value": "15,308", "what": "median MSA depth of core gene clusters", "unit": "", "denominator": "", "scope": ""}, {"value": "5,299", "what": "median MSA depth of auxiliary+singleton clusters", "unit": "", "denominator": "", "scope": ""}, {"value": "5,527", "what": "median MSA depth of auxiliary non-singleton clusters", "unit": "", "denominator": "", "scope": ""}, {"value": "2.89\u00d7", "what": "core vs auxiliary+singleton median ratio", "unit": "", "denominator": "", "scope": ""}]
caveat: "The 293K genomes are not phylogenetically balanced, with Pseudomonas and E. coli over-represented, which influences core gene counts and MSA depth distributions."
first_added: "2026-11-24"
source_hash: "f66f0c9679cde23e009a56a030fe65d0d4efb49b7f8d057511382970661ac7e1"
---
# Core genes have much deeper MSAs than accessory genes

Bacterial core gene clusters have median MSA depth 15,308, 2.89× higher than the auxiliary+singleton median of 5,299 and 2.77× higher than the auxiliary non-singleton median of 5,527. [src: alphafold_msa_annotation]

## Key figures

- **15,308**: median MSA depth of core gene clusters [src: alphafold_msa_annotation]
- **5,299**: median MSA depth of auxiliary+singleton clusters [src: alphafold_msa_annotation]
- **5,527**: median MSA depth of auxiliary non-singleton clusters [src: alphafold_msa_annotation]
- **2.89×**: core vs auxiliary+singleton median ratio [src: alphafold_msa_annotation]

## Evidence

> Core gene clusters have a median MSA depth of **15,308** — 2.89× higher than the auxiliary+singleton median of 5,299 and 2.77× higher than the auxiliary non-singleton median of 5,527. [src: alphafold_msa_annotation]

From the report [[summaries/alphafold_msa_annotation__REPORT]].

## Caveat

The 293K genomes are not phylogenetically balanced, with Pseudomonas and E. coli over-represented, which influences core gene counts and MSA depth distributions. [src: alphafold_msa_annotation]

> **Taxonomic imbalance**: The 293K genomes are not phylogenetically balanced (common taxa like *Pseudomonas* and *E. coli* are over-represented). Core gene counts and MSA depth distributions are influenced by this sampling. [src: alphafold_msa_annotation]

## Other caveats in this report

- The report states that lower hypothetical rates in core than accessory bacterial genes appear to contradict H2 as literally stated, but that the paradox-protein census resolves this tension. [src: alphafold_msa_annotation]
- The bacterial analysis is biased toward better-studied diversity because well-characterised organisms with reference proteomes, including E. coli, Pseudomonas, and Bacillus, are over-represented in UniProt. [src: alphafold_msa_annotation]
- The report suggests the annotation gap for the remaining 70.7% of bacterial clusters is likely larger than in the covered subset. [src: alphafold_msa_annotation]
- The analysis has 29.3% bridge coverage and includes only gene clusters with a non-UPI UniProt accession. [src: alphafold_msa_annotation]
- The 71% of gene clusters without AlphaFold entries skew toward poorly characterised organisms and likely harbour a larger annotation gap than the analysed subset. [src: alphafold_msa_annotation]
