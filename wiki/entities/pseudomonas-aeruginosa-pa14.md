---
type: "Organism"
description: "Reference strain of Pseudomonas aeruginosa used as the target in inhibition and carbon-utilization assays."
sources: ["summaries/cf_formulation_design__REPORT.md", "summaries/pitfalls.md"]
aliases: ["PA14"]
---
# Pseudomonas aeruginosa PA14

Pseudomonas aeruginosa PA14 (PA14) is a reference strain of Pseudomonas aeruginosa. In the cf_formulation_design report it was the strain used in all inhibition assays [src: cf_formulation_design], and its growth on single carbon sources was measured in a synthetic cystic fibrosis (CF) sputum assay. [src: cf_formulation_design]

## Key facts

- PA14 and PAO1 differ in type III secretion system (T3SS) effectors (ExoU versus ExoS), biofilm polysaccharides (Pel-only versus Pel+Psl), and regulatory state (ladS mutation). [src: cf_formulation_design]
- PA14 is described as ExoU+, Pel-only and a ladS mutant, and represents <5% of CF Pseudomonas aeruginosa isolates by virulence genotype. [src: pitfalls]
- The report calls PA14's psl deletion a rare variant, not representative of the species. [src: cf_formulation_design]
- The report calls PA14's ladS frameshift mutation an extreme outlier that locks the strain in an acute-virulence regulatory state unrepresentative of natural infection dynamics. [src: cf_formulation_design]

## Representativeness for CF

T3SS typing of 6,760 Pseudomonas aeruginosa genomes finds CF isolates are 94% ExoS+, while PA14 is ExoU+. [src: cf_formulation_design] The report states that CF Pseudomonas aeruginosa is 94% ExoS+ and 92% Pel+Psl+ (PAO1-like). [src: pitfalls] Among classifiable isolates of the PROTECT CF collection, 86% are PAO1-like, so PA14 is not representative of that collection. [src: cf_formulation_design]

Consequently, all inhibition assays used PA14, an ExoU+, Pel-only strain representing <5% of CF isolates. [src: cf_formulation_design] The assays tested the formulation against a minority (<5%) CF variant. [src: cf_formulation_design, pitfalls] The report recommends validating PA14-based results against ExoS+ strains before generalizing to CF. [src: pitfalls] See [[concepts/pseudomonas-aeruginosa-strain-diversity-and-representativeness-of-reference-strains]] and [[concepts/generalizability-limits-of-planktonic-single-strain-inhibition-assays]].

## Carbon utilization and competition

PA14 outgrows most commensals on its preferred amino acid substrates; only 13.8% of pairwise comparisons show a commensal rate advantage. [src: cf_formulation_design] The report reads the growth curves (NB02) as showing that catabolic enzyme efficiency, not ribosomal translation rate, drives this advantage despite PA14's larger genome. [src: cf_formulation_design] This is a challenge for competitive exclusion. [src: cf_formulation_design] See [[concepts/community-level-niche-coverage-and-resource-depletion-for-competitive-exclusion]].

In the synthetic CF sputum carbon-source assay, PA14 shows an amino acid preference hierarchy, with optical density (OD) per substrate as below. [src: cf_formulation_design]

| Substrate | OD |
|---|---|
| Proline | 0.60 [src: cf_formulation_design] |
| Histidine | 0.56 [src: cf_formulation_design] |
| Ornithine | 0.46 [src: cf_formulation_design] |
| Glutamate | 0.40 [src: cf_formulation_design] |
| Aspartate | 0.36 [src: cf_formulation_design] |
| Isoleucine | 0.36 [src: cf_formulation_design] |
| Arginine | 0.35 [src: cf_formulation_design] |

Glucose supports only moderate growth (0.22). [src: cf_formulation_design] Threonine, methionine, cysteine, serine and glycine support essentially no growth (<0.07). [src: cf_formulation_design]

The report says the proline > histidine > ornithine > glutamate ranking mirrors the synthetic CF medium (SCFM) composition, validating its assay system. [src: cf_formulation_design] It also reads the profile as consistent with the amino acid-rich composition of CF sputum and as showing that the assay conditions capture the metabolically relevant competitive landscape. [src: cf_formulation_design] See [[entities/cystic-fibrosis-sputum]].

Source summaries: [[summaries/cf_formulation_design__REPORT]], [[summaries/pitfalls]].
