---
type: "Method"
description: "Sequence-derived indicator of translational efficiency correlated with maximum growth rate, proposed as a feature for continuous growth prediction; does not cover specific predictor tools."
sources: ["summaries/genotype_to_phenotype_enigma__REPORT.md", "summaries/pitfalls.md"]
aliases: ["CUB", "gRodon"]
---
# Codon usage bias

Codon usage bias (CUB; also computed as gRodon scores) is a sequence-derived indicator of translational efficiency. It correlates with maximum growth rate and is proposed as a feature for continuous growth prediction. The evidence here is a proposal plus caveats: the ENIGMA project did not compute it [src: genotype_to_phenotype_enigma], and a separate pitfalls digest warns about GC-content confounding. [src: pitfalls]

## Key facts

- The genotype_to_phenotype_enigma report says growth rate depends on enzyme kinetics (Kcat, Km), expression levels and ribosome efficiency, and that CUB captures ribosome efficiency. [src: genotype_to_phenotype_enigma]
- CUB correlates with maximum growth rate via ribosomal protein optimization. The report calls it the natural next feature for ENIGMA growth-rate prediction. [src: genotype_to_phenotype_enigma]
- The report cites Xu et al. (2025, Phydon) as showing this is the natural next feature for continuous-rate prediction. [src: genotype_to_phenotype_enigma]

## Why it was not computed

CUB was planned but not computed. It needs nucleotide sequences, and these were not accessible from JupyterHub. [src: genotype_to_phenotype_enigma] GC% (available for only 32/727 genomes) and Morgan molecular fingerprints (which need RDKit) were also omitted. The report says these would be needed for continuous growth-rate prediction. [src: genotype_to_phenotype_enigma]

The needed GenBank files sit on the CGCMS server at `/data/www/CGCMS/static/enigma1/genomes/gbff/`. They are not currently accessible from JupyterHub. [src: genotype_to_phenotype_enigma] Predicting continuous growth parameters would require CUB computed from these files, or expression data. [src: genotype_to_phenotype_enigma]

## Proposed use

The report proposes computing CUB as a gRodon S-value or ENC from CDS nucleotide sequences. The aim is to test whether ribosomal efficiency explains the µmax variation that KO (KEGG ortholog) presence cannot. [src: genotype_to_phenotype_enigma] See [[concepts/predictability-of-continuous-growth-kinetics-from-gene-content]] and [[summaries/genotype_to_phenotype_enigma__REPORT]].

## Caveats on interpretation

Organisms with extreme GC composition have inflated CUB scores regardless of growth optimization. [src: pitfalls] In cf_formulation_design, cross-species CUB comparisons, such as PA versus commensals, were confounded by GC content variation (31–73%). [src: pitfalls] The pitfalls digest therefore treats CUB as meaningful only within species or across species with similar GC content. [src: pitfalls] For cross-species growth rate comparisons, it recommends lab growth data as ground truth. [src: pitfalls] See [[summaries/pitfalls]].
