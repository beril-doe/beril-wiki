---
type: "Summary"
description: "Summary of the project Core Gene Paradox -- Why Are Core Genes More Burdensome?."
doc_type: "short"
full_text: "sources/core_gene_tradeoffs__REPORT.md"
---
# Core Gene Paradox -- Why Are Core Genes More Burdensome?

This page summarises the project "Core Gene Paradox -- Why Are Core Genes More Burdensome?". It asks why core genes show more lab burden than non-core genes in the [[entities/fitness-browser]]. The report's answer is that core genes encode functions that are energetically expensive in the lab but essential in natural environments. [src: core_gene_tradeoffs] That ecological explanation is the report's interpretation, and the report notes that lab conditions capture only a fraction of the conditions bacteria face in nature. [src: core_gene_tradeoffs]

## Key Findings

### Burden excess differs by function

Core genes are not uniformly more burdensome. The excess depends on function, and one category reverses. See [[concepts/function-specific-burden-of-core-genes]]. [src: core_gene_tradeoffs]

- Protein Metabolism: core genes show a burden excess of +6.2pp. [src: core_gene_tradeoffs]
- Motility: +7.8pp. [src: core_gene_tradeoffs]
- RNA (ribonucleic acid) Metabolism: +12.9pp. [src: core_gene_tradeoffs]
- Cell Wall: reversed, with non-core genes more burdensome (-14.1pp). [src: core_gene_tradeoffs]

The report explains the core-gene excess by their encoding energetically expensive functions (motility, ribosomal components, RNA metabolism) that are essential in natural environments. [src: core_gene_tradeoffs] It says flagella are expensive but essential for chemotaxis, and ribosomal components are costly but required for rapid growth responses. [src: core_gene_tradeoffs] Motility is its example of the burden paradox. [src: core_gene_tradeoffs]

### Trade-off genes

In the Fitness Browser analysis, 25,271 genes (17.8%) are true trade-off genes. They are important (fit < -1) in some conditions and burdensome (fit > 1) in others. [src: core_gene_tradeoffs] These genes are 1.29x more likely to be core (OR, odds ratio, = 1.29, p=1.2e-44). [src: core_gene_tradeoffs] The report attributes this to core genes participating in more pathways with condition-dependent costs and benefits. [src: core_gene_tradeoffs] It also reads the finding that genes with strong condition-specific effects are more likely core as showing the conserved genome is functionally active. [src: core_gene_tradeoffs] See [[concepts/condition-dependent-fitness-trade-offs-of-core-versus-accessory-genes]].

### Selection signature matrix

The report sorts genes by burden and conservation. [src: core_gene_tradeoffs]

| Class | Genes | Report's interpretation |
|---|---|---|
| Costly + Conserved | 28,017 | Maintained by natural selection, as they are essential in natural environments absent from lab experiments [src: core_gene_tradeoffs] |
| Costly + Dispensable | 5,526 | Candidates for ongoing gene loss [src: core_gene_tradeoffs] |
| Neutral + Conserved | 86,761 | Classic housekeeping genes [src: core_gene_tradeoffs] |
| Neutral + Dispensable | 21,886 | Niche-specific genes [src: core_gene_tradeoffs] |

The report calls the 28,017 costly-but-conserved genes its strongest evidence for purifying selection maintaining genes despite metabolic cost. [src: core_gene_tradeoffs] See [[concepts/costly-but-conserved-genes-laboratory-burden-versus-conservation]] and [[concepts/gene-loss-and-black-queen-hypothesis-tests]].

### Literature context

- Price et al. (2018) generated the Fitness Browser data, which gives genome-wide mutant fitness measurements across diverse bacteria. [src: core_gene_tradeoffs]
- Rosconi et al. (2022) showed strain-dependent gene essentiality across *S. pneumoniae* pangenomes. The report says this supports its view that conservation reflects selection across diverse environments, not universal essentiality. [src: core_gene_tradeoffs]
- Koskiniemi et al. (2012) showed that dispensable genes impose fitness costs in *Salmonella*. The report calls this consistent with higher lab burden of core genes due to maintaining active pathways. [src: core_gene_tradeoffs]

## Data and Methods

The inputs are RB-TnSeq (random barcode transposon sequencing) mutant fitness data from the Fitness Browser [src: core_gene_tradeoffs], a KBase pangenome link table mapping genes to clusters [src: core_gene_tradeoffs], per-gene fitness summaries [src: core_gene_tradeoffs], and SEED functional category assignments. [src: core_gene_tradeoffs] The project generates figures only. It computes intermediate results inside one notebook from upstream data. [src: core_gene_tradeoffs]

## Caveats and Open Work

- Lab conditions capture only a fraction of the environmental conditions bacteria face in nature. [src: core_gene_tradeoffs]
- Fitness Browser condition types are biased toward experimental convenience, not ecological relevance. [src: core_gene_tradeoffs]
- Burden (fit > 1) may reflect trade-offs rather than true dispensability. [src: core_gene_tradeoffs]
- The 90% identity threshold for DIAMOND matching may miss rapidly evolving genes. [src: core_gene_tradeoffs]

## Slots Into

- [[concepts/function-specific-burden-of-core-genes]]: the per-category burden excesses and the Cell Wall reversal. [src: core_gene_tradeoffs]
- [[concepts/condition-dependent-fitness-trade-offs-of-core-versus-accessory-genes]]: 17.8% trade-off genes, enriched among core genes. [src: core_gene_tradeoffs]
- [[concepts/costly-but-conserved-genes-laboratory-burden-versus-conservation]]: the 28,017 costly, conserved genes. [src: core_gene_tradeoffs]
- [[concepts/gene-loss-and-black-queen-hypothesis-tests]]: the 5,526 costly, dispensable genes as candidates for gene loss. [src: core_gene_tradeoffs]
