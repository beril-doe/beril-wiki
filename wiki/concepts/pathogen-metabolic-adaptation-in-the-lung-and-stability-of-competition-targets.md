---
type: "Concept"
description: "Whether Pseudomonas aeruginosa amino acid catabolism is conserved across lung, CF and virulence variants, and how in vivo expression changes; stops at assay design."
sources: ["summaries/cf_formulation_design__REPORT.md", "summaries/discoveries.md", "summaries/pitfalls.md"]
---
# Pathogen metabolic adaptation in the lung and stability of competition targets

The in vivo evidence is patient metatranscriptomics, which measured large expression changes during acute exacerbation. [src: cf_formulation_design] The report's inference from those changes, that the pathogen is more vulnerable to competitive exclusion, is only a suggestion. [src: cf_formulation_design] The evidence is mostly one report, [[summaries/cf_formulation_design__REPORT]], plus two digest statements. See also [[entities/pseudomonas-aeruginosa]] and [[concepts/host-adaptation-pathway-loss-in-pseudomonas-carbon-catabolism]].

## Background and working theory

The report describes established airway P. aeruginosa as switching to amino acid catabolism as its primary carbon source, forming biofilms and becoming increasingly antibiotic-resistant. [src: cf_formulation_design] It cites Palmer et al. (2005, 2007) as establishing that amino acids are the primary carbon sources in [[entities/cystic-fibrosis-sputum]]. [src: cf_formulation_design] Its working theory is that commensal communities can exclude P. aeruginosa by consuming those carbon sources, mainly proline, histidine, ornithine, glutamate, aspartate and arginine. [src: cf_formulation_design] See [[concepts/community-level-niche-coverage-and-resource-depletion-for-competitive-exclusion]].

## Conservation across lung genomes

Amino acid catabolism is conserved across lung genomes, while sugar catabolism is lost. The pangenome analysis covered 6,760 genomes, 5,199 with metadata, of which 1,796 were from lung/respiratory or CF sources. [src: cf_formulation_design] Across the 1,796 lung genomes, amino acid catabolic pathways were 97.4% conserved (mean completeness). [src: cf_formulation_design] Proline, PA14's top substrate, was complete in 97% of lung isolates. [src: cf_formulation_design] A separate digest statement reports amino acid catabolism above 99.5% in both the P. aeruginosa group and the P. fluorescens/putida group. [src: discoveries]

Seven [[entities/gapmind]] pathways differed significantly (false discovery rate, FDR, < 0.05) between lung and non-lung genomes. All were carbon source pathways lost in lung isolates: sorbitol (−0.165), mannitol (−0.204) and gluconate (−0.185). [src: cf_formulation_design] The report reads this as metabolic streamlining under relaxed selection in amino acid-rich sputum, and as showing that amino acid dependence is an evolutionary adaptation. [src: cf_formulation_design] This is an interpretation, not a direct test of selection. The main variation among lung genomes (principal component 1, PC1 = 79%) lay in sorbitol, mannitol and gluconate pathways, which the formulation does not target. [src: cf_formulation_design] The report concludes that competitive exclusion targets are evolutionarily stable. [src: cf_formulation_design]

Two metabolic subpopulations exist. A major cluster of 1,743 genomes (97%) has full metabolic capacity. [src: cf_formulation_design] A minor cluster of 53 genomes (3%) lacks tricarboxylic acid (TCA) cycle intermediates. [src: cf_formulation_design] The minor cluster is CF-enriched (25% CF vs 16%). [src: cf_formulation_design] The report suggests it may be chronically adapted and more dependent on external metabolites, so possibly more vulnerable to competitive exclusion. [src: cf_formulation_design]

## CF and virulence variants

CF-derived genomes showed 6 FDR-significant differences from non-CF lung genomes, all in sugar-related pathways. [src: cf_formulation_design] There were zero amino acid pathway differences. [src: cf_formulation_design] The report predicts that formulations designed for general lung P. aeruginosa should work equivalently for CF isolates. [src: cf_formulation_design]

Amino acid catabolic pathways were identical between ExoU+ and ExoS+ strains. GapMind score differences were <0.03 on a 1–5 scale, with zero FDR-significant pathways. [src: cf_formulation_design, pitfalls] The report takes this as showing that the mechanism is independent of virulence genotype. [src: cf_formulation_design] All 15 PROTECT strain groups retain the same core pathways with 97%+ conservation. [src: cf_formulation_design] This is a genome-based prediction. The inhibition measurements have not been validated against ExoS+/PAO1-type strains [src: cf_formulation_design], and the digest says direct validation is needed. [src: pitfalls]

## In vivo expression

Patient metatranscriptomics showed P. aeruginosa downregulating 170 of 207 measured pathways during acute exacerbation. [src: cf_formulation_design] Cysteine and methionine biosynthesis expression was 10× lower. [src: cf_formulation_design] OprD, described as imipenem resistance, was 13× lower. [src: cf_formulation_design] Only phosphate transport was upregulated, by 64×. [src: cf_formulation_design] The report suggests that this quiescent, host-amino-acid-scavenging state may leave the pathogen more vulnerable to competitive exclusion during acute episodes. [src: cf_formulation_design] That vulnerability is a hypothesis, not a tested result.

## Assay support and limits

In the synthetic CF sputum carbon source assay, [[entities/pseudomonas-aeruginosa-pa14]] showed this optical density (OD) hierarchy: proline 0.60, histidine 0.56, ornithine 0.46, glutamate 0.40, aspartate 0.36, isoleucine 0.36, arginine 0.35. [src: cf_formulation_design] Glucose supported only moderate growth (0.22). [src: cf_formulation_design] Threonine, methionine, cysteine, serine and glycine supported essentially no growth (<0.07). [src: cf_formulation_design] The report says this profile fits amino acid-rich sputum and validates its assay conditions. [src: cf_formulation_design]

The limit is that A. baumannii and K. pneumoniae show distinct profiles. PA14's amino acid specialization is therefore not universal among CF pathogens, and formulations may need to be pathogen-specific. [src: cf_formulation_design]

## Open Directions

- Test the inhibition assay against ExoS+/PAO1-type strains. This would close the gap between genome-predicted and measured transfer across virulence types.
- Culture representatives of the 53-genome TCA-deficient cluster in synthetic CF sputum medium. This would test whether they depend more on external metabolites and are more easily excluded.
- Measure expression of amino acid catabolic genes, not only biosynthesis, in the exacerbation metatranscriptomes. The reported down-regulation covers pathways broadly, so this would show whether the exclusion targets stay expressed in vivo.
- Run the same GapMind lung versus non-lung comparison for A. baumannii and K. pneumoniae. This would test whether pathogen-specific formulations are needed.
