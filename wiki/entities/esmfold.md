---
type: "Method"
description: "Protein structure predictor that does not use MSA depth, proposed as an orthogonal structural novelty signal; does not cover Foldseek structure search."
sources: ["summaries/alphafold_msa_annotation__REPORT.md", "summaries/truly_dark_genes__REPORT.md"]
aliases: ["ESM pLDDT", "Foldseek"]
---
# ESMFold

This page is about ESMFold, a protein structure predictor, also known as ESM pLDDT. The evidence here is proposals from two reports, not measured ESMFold results. [src: alphafold_msa_annotation, truly_dark_genes]

## Key facts

- The alphafold_msa_annotation report describes ESMFold as not using MSA (multiple sequence alignment) depth. It therefore provides an orthogonal structural novelty signal. [src: alphafold_msa_annotation]
- That report proposes comparing ESM pLDDT with AlphaFold MSA depth for the same bacterial clusters. The comparison would identify proteins that are novel in sequence space but potentially foldable without homologs. [src: alphafold_msa_annotation] See [[concepts/shallow-alphafold-msa-depth-and-annotation-of-conserved-core-genes]] and [[summaries/alphafold_msa_annotation__REPORT]].

## Use for truly dark genes

The truly_dark_genes report proposes running AlphaFold2/ESMFold on its top-100 truly dark gene candidates. It would then search Foldseek for remote structural homologs. [src: truly_dark_genes]

The report calls this the most promising path to functional annotation for sequences with no detectable sequence homology. [src: truly_dark_genes] It names structure prediction (AlphaFold2/ESMFold plus Foldseek) as the next frontier for these candidates. [src: truly_dark_genes] See [[summaries/truly_dark_genes__REPORT]] and [[concepts/census-and-evidence-depth-classification-of-functionally-dark-genes]].
