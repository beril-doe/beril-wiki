---
type: "Concept"
description: "Whether Complex I (NADH:ubiquinone oxidoreductase) is needed specifically on aromatics or on any high-NADH-flux substrate, and the hypothesis that NDH-2 compensates elsewhere; stops at the evidence from ADP1 and ortholog-transferred fitness."
sources: ["summaries/adp1_deletion_phenotypes__REPORT.md", "summaries/aromatic_catabolism_network__REPORT.md", "summaries/discoveries.md", "summaries/respiratory_chain_wiring__REPORT.md"]
---
# Substrate-dependent Complex I requirement and NDH-2 compensation

This page covers whether Complex I (NADH:ubiquinone oxidoreductase) is needed specifically on aromatic substrates or on any high-NADH-flux substrate, and the hypothesis that NDH-2 compensates elsewhere. The cross-species data point to high NADH flux rather than aromatics alone. [src: aromatic_catabolism_network] NDH-2 compensation is a hypothesis for ADP1, and the cross-species data do not support it as a general predictor. [src: aromatic_catabolism_network, respiratory_chain_wiring] See also [[concepts/ndh-2-compensation-for-complex-i-loss-across-species]] and [[concepts/nadh-flux-rate-versus-nadh-yield-as-determinant-of-complex-i-dependence]].

## ADP1: an apparent quinate-specific requirement

The ADP1 quinate-specific gene set has 51 genes at spec > 0.5, z < -1. It extends beyond core degradation genes to Complex I subunits, which suggests that aromatic catabolism places unique demands on electron transport. [src: adp1_deletion_phenotypes] Disrupting any one subunit eliminates the whole complex. The report gives this as the reason 10/13 subunits independently give quinate-specific growth defects. [src: aromatic_catabolism_network]

## Cross-species data: high-NADH substrates, not aromatics alone

The report concludes that Complex I dependency is on high-NADH substrates, not aromatics specifically. [src: aromatic_catabolism_network] The ortholog-transferred Fitness Browser (FB) data contain 12,241 entries, 2,005 genes and 13 conditions. [src: aromatic_catabolism_network] Complex I orthologs have significantly worse fitness on aromatic than non-aromatic conditions (mean = -1.35 vs -0.77, Mann-Whitney p < 0.0001). [src: aromatic_catabolism_network]

Per condition, the largest Complex I defects relative to background are on acetate (-1.55) and succinate (-1.39). Both are non-aromatic substrates that also generate high NADH flux through the tricarboxylic acid (TCA) cycle. [src: aromatic_catabolism_network, discoveries] The report reads the "aromatic support network" as a high-NADH-flux bottleneck network. [src: discoveries] It states that Complex I is dispensable on glucose and lactate, where NDH-2 suffices. It states that Complex I is essential on aromatics, acetate and succinate. [src: aromatic_catabolism_network]

## The NDH-2 compensation hypothesis

Bacteria typically have branched respiratory chains with proton-pumping Complex I (NDH-1) and non-pumping NDH-2. [src: aromatic_catabolism_network] NDH-2 can substitute for Complex I at low NADH flux but cannot match its capacity at high flux. [src: aromatic_catabolism_network] On this basis the report proposes that ADP1's quinate-specificity reflects NDH-2 compensating on simpler or lower-NADH-flux substrates. [src: aromatic_catabolism_network, discoveries] In ADP1, glucose distributes NADH across Entner-Doudoroff and TCA steps where NDH-2 suffices. [src: discoveries] On lactate, Complex I matters only mildly (0.77), which the report takes to suggest partial NDH-2 compensation. [src: respiratory_chain_wiring]

A second report adds a rate-versus-yield argument. Quinate gives fewer NADH per carbon atom (0.57) than glucose (1.50) or acetate (1.50), yet Complex I is more essential on quinate. [src: respiratory_chain_wiring] It resolves this by NADH flux rate. β-ketoadipate ring cleavage yields succinyl-CoA and acetyl-CoA together, which creates a concentrated TCA NADH burst beyond NDH-2 reoxidation capacity. [src: respiratory_chain_wiring] It proposes the principle should apply to any substrate whose catabolism produces concentrated reducing equivalents. [src: respiratory_chain_wiring]

## Tensions

- **Compensation supported versus not supported.** The aromatic_catabolism_network report says its cross-species data support NDH-2 compensation on glucose and lactate. [src: aromatic_catabolism_network] The respiratory_chain_wiring report says NDH-2 presence does not predict Complex I dispensability on aromatics. [src: respiratory_chain_wiring] Organisms with NDH-2 have larger mean Complex I aromatic deficits (-0.297) than those without (-0.156), the opposite of the compensation prediction, but not significantly (p = 0.52). [src: respiratory_chain_wiring] That report considers compensation likely ADP1-specific, not a general cross-species pattern. [src: respiratory_chain_wiring]
- **Direct test missing.** The ADP1 dataset has no NDH-2 growth data, so the central prediction that NDH-2 compensates on glucose cannot be tested directly. [src: respiratory_chain_wiring]

## Caveats

Ortholog-transferred fitness mixes signals from several FB organisms with different respiratory-chain architectures. Direct Complex I measurements on aromatics in a single organism would be more definitive. [src: aromatic_catabolism_network]

## Proposed tests

The report proposes searching the ADP1 genome for NDH-2 genes and testing their deletion phenotypes on quinate versus glucose, to test compensation for Complex I on non-aromatic substrates. [src: aromatic_catabolism_network] It also proposes using `eggnog_mapper_annotations` in the KBase Data Lakehouse to test whether Acinetobacter species carrying the pca pathway more often retain Complex I (KEGG ortholog (KO) IDs K00330–K00343) than species lacking aromatic degradation. [src: aromatic_catabolism_network]

## Open Directions

- Search the ADP1 genome for NDH-2 genes and compare their deletion phenotypes on quinate and glucose. This closes the gap that ADP1 has no NDH-2 growth data.
- Run the `eggnog_mapper_annotations` test of Complex I retention in pca-carrying versus non-aromatic-degrading Acinetobacter species, to ask whether Complex I tracks aromatic catabolism across genomes.
- Measure Complex I fitness on aromatics, acetate, succinate, glucose and lactate within a single organism. This avoids the mixed-architecture problem of ortholog transfer.
- Re-run the NDH-2 presence comparison with more organisms, to see whether the non-significant result (p = 0.52) reflects low power.
