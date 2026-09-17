<!-- tension-hash: 05940aec7c9995a0 -->
# Complex I dependence on aromatic substrates: an ADP1 compensation hypothesis, a null cross-species test, and a model that predicts no essentiality

Three lines of evidence in this corpus disagree about why *Acinetobacter baylyi* ADP1 needs Complex I (NADH:ubiquinone oxidoreductase, the proton-pumping NADH dehydrogenase) to grow on quinate but not on simpler substrates. Flux balance analysis (FBA, a constraint-based method predicting feasible flux distributions) predicts no essentiality; mutant phenotypes say the complex is required; and the architecture-based explanation offered for that gap — compensation by NDH-2, a single-subunit non-pumping NADH dehydrogenase — was not supported when tested across species. The disagreement matters because it determines whether ADP1's respiratory wiring is a general rule that can be ortholog-transferred, or a species-specific arrangement. This page draws on [[concepts/cofitness-network-architecture]], [[concepts/condition-specific-fitness]], [[concepts/cross-species-fitness-transferability]] and [[concepts/metabolic-model-gapfilling]].

## Evidence Sides

**The model side: FBA sees demand but predicts no bottleneck.** FBA predicted 0% Complex I essentiality, and 30/51 network genes lacked FBA reaction mappings entirely. [src: aromatic_catabolism_network] The same analysis found 1.76× higher Complex I flux. [src: aromatic_catabolism_network] FBA also predicts zero flux through NDH-2 and ACIAD3522 on standard media. [src: aromatic_catabolism_network; discoveries; respiratory_chain_wiring]

**The ADP1 phenotype side: measured defects and a substrate-architecture hypothesis.** 10/13 Complex I subunits produced quinate-specific defects. [src: aromatic_catabolism_network] Aromatic and respiratory-chain work associates quinate with greater Complex I dependence despite lower total NADH yield, but that interpretation rests on theoretical stoichiometry and inferred capacity limits. [src: aromatic_catabolism_network; discoveries; respiratory_chain_wiring] Transferred defects were strongest on acetate and succinate rather than exclusively aromatic substrates, with ACIAD3522 ratios of 0.013 on acetate and 1.39 on quinate and glucose. [src: discoveries] NDH-2 compensation remains a substrate- and architecture-based hypothesis. [src: aromatic_catabolism_network]

**The cross-species side: a null result that weakens generalization.** After annotation correction, organisms with validated NDH-2 showed a *larger* mean Complex I aromatic deficit (−0.297) than those without (−0.156), p = 0.52 — the opposite direction from the compensation prediction, and not significant. [src: discoveries] Only 5 of 14 organisms had validated NDH-2 and only 4 lacked it, so the comparison is underpowered and vulnerable to annotation errors; the two results should not be reconciled as a universal rule. [src: respiratory_chain_wiring]

## Possible Reconciliations

- *Hypothesis:* the threshold behaviour of a multi-subunit complex is invisible to linear-programming flux redistribution, so a 0% essentiality prediction and 10/13 subunit defects can both be correct descriptions of different objects. [src: aromatic_catabolism_network]
- *Hypothesis:* ADP1 wiring is species-specific, so the compensation logic holds within ADP1 while failing as a cross-species predictor. [src: aromatic_catabolism_network; discoveries; respiratory_chain_wiring]
- *Hypothesis:* the cross-species null reflects annotation error and low power rather than absence of compensation; it remains a null result, not evidence of a reversed effect. [src: respiratory_chain_wiring]

## Resolving Work

- Direct NDH-2 mutant fitness in ADP1 on quinate, glucose and acetate, by RB-TnSeq (random barcode transposon sequencing) or targeted deletion: does removing NDH-2 make Complex I required on glucose?
- NDH-2 calls from HMM (hidden Markov model profile search) and synteny evidence, replacing text-matched candidates across the same 14 organisms: does the −0.297 versus −0.156 contrast change direction or magnitude?
- Power analysis and organism expansion beyond the 4 organisms lacking NDH-2: how many NDH-2-negative genomes are needed to move p = 0.52 into a decidable range?
- Enzyme-constrained or complex-aware modelling of the 30/51 unmapped network genes: does representing subunit-threshold effects recover the observed quinate-specific essentiality?
- Substrate-resolved NADH flux measurement on acetate versus quinate: does ACIAD3522's 0.013 acetate ratio mark a distinct high-NADH regime rather than an aromatic-specific one?
