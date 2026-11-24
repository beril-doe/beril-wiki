---
type: "Concept"
description: "Covers whether regulatory genes are transferred less or more than metabolic genes across the bacterial tree, and the role of architectural promiscuity; stops at mobile-element mechanisms."
sources: ["summaries/discoveries.md", "summaries/gene_function_ecological_agora__REPORT.md"]
---
# Complexity hypothesis: regulatory versus metabolic gene transfer asymmetry

This page asks whether regulatory genes are transferred less or more than metabolic genes across the bacterial tree, and what architectural promiscuity adds. In the gene_function_ecological_agora project, the answer at GTDB scale is a small effect in the direction the complexity hypothesis predicts: regulatory KOs (KEGG orthologs) are somewhat more vertically inherited than metabolic KOs. It falls well short of the pre-registered strong-form threshold. [src: gene_function_ecological_agora] The evidence comes from one project, with an external literature analog (Burch 2023) used as support.

## The pre-registered test (NB11)

NB11 compared regulatory KOs (Genetic IP ko03xxx plus Environmental IP ko02010-ko02065) with metabolic KOs (Metabolism ko00xxx-ko019xx) for different innovation and acquisition signatures. [src: gene_function_ecological_agora] The pre-registered criterion was Cohen's d ≥ 0.3 with a 95% CI (confidence interval) excluding zero, and Mann-Whitney p < α/4 = 0.0125, Bonferroni-corrected for 4 headline tests. [src: gene_function_ecological_agora] No test reached d ≥ 0.3. Two of four showed small signals that survived Bonferroni correction, and two were null. [src: gene_function_ecological_agora]

- T1 producer_z_median (n_reg 1,554, n_met 4,970): d +0.059, 95% bootstrap CI [−0.011, +0.124], MW p 0.71; no signal. [src: gene_function_ecological_agora]
- T2 consumer_z_median (n_reg 1,552, n_met 4,964): d −0.211, CI [−0.288, −0.150], MW p <10⁻¹⁵; a small effect in the opposite direction, failing the combined criteria. [src: gene_function_ecological_agora]
- T3 recent_acquisition_pct (n_reg 1,554, n_met 4,970): d +0.141, CI [+0.092, +0.189], MW p 3.0×10⁻⁶; a small effect with weak direction match, failing the combined criteria. [src: gene_function_ecological_agora]
- T4 n_clades_with_max (n_reg 1,552, n_met 4,964): d +0.020, CI [−0.045, +0.082], MW p 0.12; no signal. [src: gene_function_ecological_agora]

A later check (P4-D5) gave the same picture. Producer_z had d = +0.06 (D2-residualized +0.06, residualized p = 0.69). [src: gene_function_ecological_agora] Consumer_z had d = −0.21 (D2-residualized −0.21, residualized p <10⁻¹⁰). [src: gene_function_ecological_agora]

The verdict was H1 REFRAMED, with the H0-atlas fallback. [src: gene_function_ecological_agora] The report says this falsifies the strong-form asymmetry prior at GTDB scale and at d ≥ 0.3. [src: gene_function_ecological_agora] Sample size is not the limit, since the pools are large. The report concludes the effects are genuinely small. [src: gene_function_ecological_agora] It calls d=0.14-0.21 statistically significant but biologically small. [src: gene_function_ecological_agora] It treats the small signals as descriptive, not as evidence for strong asymmetry. [src: gene_function_ecological_agora]

## Direction: less transfer of regulatory genes

Regulatory KOs were more phyletically clumped than metabolic KOs at the function-class pool level (d=−0.21 at p<10⁻¹⁵). [src: gene_function_ecological_agora] This means less horizontal gene transfer (HGT), as the complexity hypothesis predicts. [src: gene_function_ecological_agora] The report notes this runs contrary to the strong prior that regulatory genes flow more. [src: gene_function_ecological_agora] It therefore calls NB11 direction-consistent with Jain 1999 and not a contradiction. [src: gene_function_ecological_agora] It also says the effect is real and detectable across the full tree. It is too small to dominate per-clade × per-function-class innovation patterns at the pre-registered threshold. [src: gene_function_ecological_agora]

The picture has qualifications:
- T3 weakly favors a softer opposite hypothesis. Regulatory KOs show slightly more recent acquisitions (47.3% vs 45.9% recent), but d = 0.14 is below the biological-significance threshold. [src: gene_function_ecological_agora]
- Sink/Broker-Exchange is 7.16% for regulatory versus 5.20% for metabolic KOs. The report suggests regulatory KOs join more cross-clade exchange events when direction is unclear. [src: gene_function_ecological_agora]
- The two-component system (TCS) histidine-kinase (HK) signal is real, with TCS-HK versus tRNA-synthetase d = 0.65 in the NB10 M21 sanity rail. It does not generalize across the whole regulatory category. [src: gene_function_ecological_agora]
- The null does not invalidate the four pre-registered clade × function hypotheses. It only removes regulatory/metabolic asymmetry as a way to predict them. [src: gene_function_ecological_agora]

## External support: Burch 2023

The report treats Burch et al. 2023 (PMID:37232518) as genomic-level empirical validation of the complexity hypothesis. It treats NB11 as the GTDB-scale instantiation. [src: gene_function_ecological_agora] Burch et al. used 74-prokaryote-genome shotgun libraries into Escherichia coli. They found that transferability declines as connectivity increases, with translational proteins showing the strongest effect. [src: gene_function_ecological_agora] The report says the two studies recover the same signal at different scales. Burch measures donor-by-E. coli HGT rate against connectivity. NB11 measures clade-by-KO phyletic clumping against the regulatory/metabolic split. [src: gene_function_ecological_agora] It also cites Burch as validating the direction at Lactobacillaceae scale. [src: gene_function_ecological_agora] It says this strengthens the NB11 reframing and that NB11 contributes to the empirical complexity-hypothesis literature. [src: gene_function_ecological_agora] These are the report's own interpretations. NB11 and Burch use different measures. [src: gene_function_ecological_agora]

## Mixed-category KOs and architectural promiscuity

KOs in both regulatory and metabolic pathways were the most exchange-active. They had 2× the Innovator-Exchange rate (0.57%) of pure regulatory (0.27%) or pure metabolic (0.28%) KOs. [src: discoveries, gene_function_ecological_agora] The report reads this as fewer constraints than either pure category. [src: gene_function_ecological_agora]

Separately, the report finds that higher architectural diversity per KO correlates with elevated atlas-level cross-clade exchange. [src: gene_function_ecological_agora] Mixed-category KOs show a median of 46 architectures per KO versus 1 for PSII (photosystem II). [src: gene_function_ecological_agora] The report claims novelty for framing exchange propensity through within-KO architectural promiscuity. [src: gene_function_ecological_agora] It also links this to Denise 2019, where systems encoded in fewer loci were exchanged more often. It calls that a genome-organization analog and recasts the finding as an instance of an established modular-gene-family pattern. [src: gene_function_ecological_agora] The proposed mechanism is a hypothesis. KOs with many domain combinations may be more modular and less constrained by host-specific protein-protein interaction networks, which would extend the Jain complexity hypothesis to architecture. [src: gene_function_ecological_agora] The report flags the architecture finding as exploratory and not pre-registered. Independent structural validation is deferred. [src: gene_function_ecological_agora]

## Boundary with mobile elements

Regulatory KOs have a ~10× higher mobile-genetic-element (MGE) machinery rate (4.13%) than metabolic (0.37%) or mixed (0.27%) KOs. The report ties this to transposon-bound and phage-bound regulators. [src: gene_function_ecological_agora] See [[concepts/mobile-genetic-element-context-of-horizontally-acquired-gene-families]] for mechanisms. Related: [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]] and [[summaries/gene_function_ecological_agora__REPORT]].

## Tensions

- Consumer_z shows regulatory KOs as less transferred (d=−0.21). [src: gene_function_ecological_agora] Recent acquisition shows slightly more recent regulatory acquisitions (d=+0.141). [src: gene_function_ecological_agora] The report treats the latter as weak and below threshold. [src: gene_function_ecological_agora]
- The pre-registered strong asymmetry is falsified [src: gene_function_ecological_agora], yet the report presents the small direction-consistent effect as support for the complexity hypothesis. [src: gene_function_ecological_agora]

## Open Directions

- Test the architecture-to-exchange link with an independent structural check. This could use AlphaFold confidence scores or domain-shuffling literature, which would close the gap that the finding is exploratory.
- Split the regulatory category by sub-class (TCS-HK, transcription factors, translation-related). This would show which sub-classes drive the d=−0.21 signal and which drive the TCS-HK d = 0.65 signal.
- Run the regulatory/metabolic comparison within MGE-excluded KOs. This would show whether the 4.13% MGE rate in regulatory KOs masks a stronger vertical-inheritance signal.
- Model exchange rate jointly on architectural promiscuity and the regulatory/metabolic/mixed class. This would separate the mixed-class effect from the promiscuity effect.
- Compare NB11 clumping with Burch-style connectivity values for the same KOs. This would test whether the two scales rank genes alike.
