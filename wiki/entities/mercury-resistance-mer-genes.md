---
type: "Gene_Or_Pathway"
description: "mer gene family (merA, merP, merC and others) conferring mercury resistance, prominent in AMR annotations."
sources: ["summaries/amr_pangenome_atlas__REPORT.md", "summaries/comprehensive_metal_ecology__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md"]
aliases: ["mer operon", "merD", "merE", "mercury resistance genes"]
---
# Mercury resistance mer genes

This page covers the mercury resistance mer genes (mer operon; merA, merP, merC, merD, merE and others). They are prominent in antimicrobial resistance (AMR) annotations of bacterial pangenomes. [src: amr_pangenome_atlas] A plasmid-enrichment signal for merD is marginal and underpowered. [src: comprehensive_metal_ecology] See also [[entities/metal-resistance-genes]] and [[concepts/metal-resistance-genes-within-amr-catalogs]].

## Key facts

- merA (mercury reductase) is among the dominant bacterial AMR gene families, with 4,506 hits. [src: amr_pangenome_atlas]
- merP (mercury binding protein) is also among them, with 2,222 hits. [src: amr_pangenome_atlas]
- Mercury resistance genes merA, merP, merC, merE, merF, merR, merD, merB and merT collectively account for ~15,000 hits, or 18% of all AMR annotations. [src: amr_pangenome_atlas]
- Mer and ars (arsenic resistance) families are prominent because the NCBI Reference Gene Catalog defines AMR broadly and includes stress response genes. [src: amr_pangenome_atlas] See [[entities/arsenic-resistance-ars-genes]] and [[summaries/amr_pangenome_atlas__REPORT]].

## Annotation support

Spot checks of prevalent arsD and merP gene families showed biologically expected distributions: high in contaminated-environment genera and lower in strict aerobes. The report calls this informal support. [src: microbeatlas_metal_ecology] See [[concepts/validity-of-curated-metal-gene-annotation]] and [[summaries/microbeatlas_metal_ecology__REPORT]].

## Horizontal transfer signals

In the metal-gene horizontal-transfer candidate analysis, merE (K19059, Resistance) has genome-level D = 0.728, genus-level λ = 0.102, and n = 154 genomes. [src: comprehensive_metal_ecology] merD (K19057, Resistance) has genome-level D = 0.701, genus-level λ = 0.165, and n = 156 genomes. [src: comprehensive_metal_ecology] See [[concepts/horizontal-transfer-signatures-of-metal-resistance-genes]] and [[summaries/comprehensive_metal_ecology__REPORT]].

### Plasmid enrichment

Among resistance KOs (KEGG orthologs) with n_total ≥ 50, double-signal resistance KOs had higher NCBI Entrez plasmid fractions than background resistance KOs (n=51). The double-signal KOs were merD 4.3%, aoxB 0.4% and norB 0.1%. The Mann-Whitney U (MWU) test gave p = 0.045. [src: comprehensive_metal_ecology] An independent BV-BRC validation with 84,446 plasmid accessions gave p = 0.044 (n_double = 2: merD 7.2%, norB 0.3%; n_background = 48 after arsC KO deduplication). [src: comprehensive_metal_ecology]

The report calls the two-database result marginally significant. It is driven primarily by merD in the Tn21-family mer operon, and it is underpowered because few double-signal resistance KOs have n ≥ 50. [src: comprehensive_metal_ecology]
