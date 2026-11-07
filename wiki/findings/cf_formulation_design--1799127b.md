---
type: "Finding"
description: "Across 6,760 PA genomes, with environmental metadata for 4,769, T3SS effector typing shows ExoS+ in 94% and ExoU+ in 5% of CF patient isolates (n = 291)."
finding_id: "cf_formulation_design--1799127b"
result: "observation"
source: "cf_formulation_design"
quantities: [{"value": "94%", "what": "ExoS+ fraction of CF patient PA genomes", "unit": "%", "denominator": "291 CF patient genomes", "scope": "CF patient"}, {"value": "5%", "what": "ExoU+ fraction of CF patient PA genomes", "unit": "%", "denominator": "291 CF patient genomes", "scope": "CF patient"}, {"value": "4,769", "what": "PA genomes with environmental metadata", "unit": "genomes", "denominator": "6,760 PA genomes", "scope": "pangenome"}]
caveat: "All inhibition assays used PA14, which is ExoU+ and Pel-only, and the inhibition measurements have not been validated against ExoS+/PAO1-type strains."
first_added: "2026-10-27"
source_hash: "06931c95e1ee4b3b3a4a95563e11b057ffbada9817b91426fd15b4be9ef75bfe"
---
# Cystic fibrosis P. aeruginosa is mostly ExoS+, unlike the PA14 assay strain

Across 6,760 PA genomes, with environmental metadata for 4,769, T3SS effector typing shows ExoS+ in 94% and ExoU+ in 5% of CF patient isolates (n = 291). [src: cf_formulation_design]

## Key figures

- **94%**: ExoS+ fraction of CF patient PA genomes (denominator 291 CF patient genomes; scope CF patient) [src: cf_formulation_design]
- **5%**: ExoU+ fraction of CF patient PA genomes (denominator 291 CF patient genomes; scope CF patient) [src: cf_formulation_design]
- **4,769 genomes**: PA genomes with environmental metadata (denominator 6,760 PA genomes; scope pangenome) [src: cf_formulation_design]

## Evidence

> Across 6,760 PA genomes with environmental metadata for 4,769, T3SS effector typing reveals a striking gradient: | Environment | ExoS+ | ExoU+ | Both | n | |---|---|---|---|---| | CF patient | **94%** | **5%** | 0% | 291 | | Lung/Respiratory | 82% | 16% | 1% | 1,505 | | Other Clinical | 63% | 33% | 3% | 1,731 | | Environmental | 62% | 35% | 1% | 370 | [src: cf_formulation_design]

From the report [[summaries/cf_formulation_design__REPORT]].

## Caveat

All inhibition assays used PA14, which is ExoU+ and Pel-only, and the inhibition measurements have not been validated against ExoS+/PAO1-type strains. [src: cf_formulation_design]

> - **PA14 reference strain bias**: All inhibition assays used PA14, which is ExoU+ and Pel-only — representing <5% of CF PA isolates. While our pangenome analysis confirms AA catabolism is identical across ExoU+ and ExoS+ strains, the inhibition measurements themselves have not been validated against ExoS+/PAO1-type strains. Proposed Experiment 4.6 (PAO1 and clinical strain extension) directly addresses this gap. [src: cf_formulation_design]

## Other caveats in this report

- Competitive metabolic exclusion is the study's working theory; the listed CF-sputum amino acids are proposed shared resources. [src: cf_formulation_design]
- Selective prebiotic biomass pre-loading is explicitly a hypothesis. [src: cf_formulation_design]
- GTDB taxonomy is used; Pseudomonas_E is a non-aeruginosa clade and should not be merged with P. aeruginosa. [src: cf_formulation_design]
- The three named organisms have the largest reported isolate counts; pathogen oversampling limits interpretation of collection frequencies as natural prevalence. [src: cf_formulation_design]
- Acinetobacter baumannii and Klebsiella pneumoniae are other named reporter pathogens; their distinct profiles limit generalization of the PA14-targeted formulation. [src: cf_formulation_design]
