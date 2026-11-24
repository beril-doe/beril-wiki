---
type: "Method"
description: "Gene knockdown approach proposed for essential dark genes that cannot be disrupted by transposon mutagenesis."
sources: ["summaries/functional_dark_matter__REPORT.md", "summaries/truly_dark_genes__REPORT.md"]
aliases: ["CRISPRi", "Mobile-CRISPRi"]
---
# CRISPR interference knockdown

This page covers CRISPR interference knockdown (CRISPRi, Mobile-CRISPRi), the gene knockdown approach proposed for essential dark genes that cannot be disrupted by transposon mutagenesis. The report proposes CRISPRi as an experimental path that transposon mutagenesis cannot provide. [src: functional_dark_matter]

## Key facts

- The top essential dark gene candidates are genes with no viable knockout mutants. Gene neighborhood context, cross-species conservation and domain structure make CRISPRi knockdown experiments possible for them. [src: functional_dark_matter]
- The covering set assigns 8,900 essential genes to specific organisms for CRISPRi-based approaches. [src: functional_dark_matter]

## Experimental designs

Each top candidate has a CRISPRi design that specifies target organism, sgRNA target, growth condition, expected phenotype and validation strategy. [src: functional_dark_matter] The top 50 essential candidates have specific designs in NB07. [src: functional_dark_matter]

The recommended approach is CRISPRi knockdown with growth curves under standard and stress conditions. It uses Mobile-CRISPRi (Peters et al. 2019) for non-model organisms. [src: functional_dark_matter] The truly_dark_genes report likewise suggests that Mobile-CRISPRi could enable rapid functional testing across organisms. [src: truly_dark_genes]

Per-organism plans recommend CRISPRi for essential genes in tractable organisms. They recommend condition-specific TnSeq (transposon sequencing) for fitness-active genes and broad phenotypic screens for true knowledge gaps. [src: functional_dark_matter]

### Escherichia coli example

The #1 candidate is Keio:14796, which has a YbeY domain. Its operon with an annotated ion transport gene predicts an ion transport function. The proposed test is CRISPRi knockdown in *E. coli* Keio on varied carbon and nitrogen sources, with OD600 monitored for growth defects. [src: functional_dark_matter]

The proposed Route A experiment in [[entities/escherichia-coli]] K-12 knocks down the top 20 essential dark genes and measures growth curves. It uses the highest-tractability organism (0.9) and mature CRISPRi tools. Its top target is Keio:14796 (YbeY domain, score 0.875). [src: functional_dark_matter]

See also [[summaries/functional_dark_matter__REPORT]] and [[summaries/truly_dark_genes__REPORT]].
