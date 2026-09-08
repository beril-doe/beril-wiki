---
type: Concept
description: Respiratory-chain dependence tracks reducing-equivalent load, not substrate
  identity
sources:
- id: aromatic_catabolism_network
  resource: ../summaries/aromatic_catabolism_network__REPORT.md
  title: aromatic catabolism network
- id: respiratory_chain_wiring
  resource: ../summaries/respiratory_chain_wiring__REPORT.md
  title: respiratory chain wiring
- id: metabolic_capability_dependency
  resource: ../summaries/metabolic_capability_dependency__REPORT.md
  title: metabolic capability dependency
- id: pathway_capability_dependency
  resource: ../summaries/pathway_capability_dependency__REPORT.md
  title: pathway capability dependency
title: Respiratory-chain dependence tracks reducing-equivalent load rather than substrate
  identity
---
# Respiratory-chain dependence tracks reducing-equivalent load rather than substrate identity

Respiratory-chain dependence may be driven more by reducing-equivalent load—particularly NADH generated during substrate oxidation—than by whether a substrate is chemically aromatic. [^aromatic_catabolism_network] The [aromatic_catabolism_network__REPORT](../summaries/aromatic_catabolism_network__REPORT.md) supports this interpretation by combining condition-specific fitness data with metabolic flux analysis and by comparing aromatic and non-aromatic substrates. [^aromatic_catabolism_network] New ADP1 wiring evidence **supports** this interpretation by showing that carbon sources select qualitatively different respiratory configurations through NADH flux rate and capacity constraints, rather than simply changing total reducing-equivalent yield. [^respiratory_chain_wiring]

The [metabolic_capability_dependency__REPORT](../summaries/metabolic_capability_dependency__REPORT.md) **supports** separating encoded metabolic capability from experimentally measured dependency: across 161 organism–pathway pairs, complete pathways could be either fitness-important or fitness-neutral, and all 66 pairs classified as Latent Capability became fitness-important under at least one tested condition type. [^pathway_capability_dependency] This **refines** the respiratory interpretation by showing that pathway presence or substrate category alone does not establish functional dependence; the relevant condition-specific reducing-equivalent burden still requires measurement. [^metabolic_capability_dependency] The condition-specific reclassification is partly sensitive to the report’s median-based importance threshold, so it is evidence for conditional dependence rather than independent confirmation of every individual pathway call. [^pathway_capability_dependency]

## Core interpretation

The report identifies [complex-i](../entities/complex-i.md) as the largest support subsystem in the ADP1 quinate-catabolism network: 21/51 quinate-specific genes belong to Complex I, or NADH:ubiquinone oxidoreductase. [^aromatic_catabolism_network] This association initially appears substrate-specific because Complex I fitness is strongly impaired under aromatic conditions, but the strongest condition-level defects occur on acetate and succinate, which are non-aromatic substrates that also generate high NADH flux through the TCA cycle. [^aromatic_catabolism_network] Thus, the evidence supports the hypothesis that respiratory-chain demand tracks reducing-equivalent production rather than aromatic chemistry itself. [^aromatic_catabolism_network]

The new wiring analysis **refines** this interpretation: in ADP1, quinate requires Complex I, acetate requires Complex I plus cytochrome bo3, ACIAD3522, and additional components, lactate specifically requires cytochrome bo3, glucose has no specifically required respiratory component, and urea is broadly demanding across the reported respiratory profile. [^respiratory_chain_wiring] These qualitative configurations support a capacity-limited model in which the relevant determinant is how NADH is generated and reoxidized under each condition, not substrate identity alone. [^respiratory_chain_wiring]

The capability–dependency comparison **supports** this distinction at broader scale: pathway category predicted dependency class (χ²=163.6, df=4, p=2.5×10⁻³⁴), but complete pathways could remain fitness-neutral, especially carbon pathways. [^metabolic_capability_dependency] The newer analysis **supports** the same distinction with a separate four-way classification of complete and incomplete pathways against fitness importance, including 57 Active Dependency and 66 Latent Capability pairs among 161 combinations. [^pathway_capability_dependency] Neither analysis identifies respiratory load directly, but both reinforce that chemical or genomic pathway identity is an imperfect proxy for condition-specific physiological demand. [^metabolic_capability_dependency] [^pathway_capability_dependency]

## Evidence from transferred fitness data

Ortholog-transferred data from the [kescience-fitnessbrowser](../entities/kescience-fitnessbrowser.md) contains 12,241 entries covering 2,005 genes and 13 conditions. [^aromatic_catabolism_network] Complex I orthologs have mean fitness values of -1.35 on aromatic conditions and -0.77 on comparison conditions, with Mann-Whitney p < 0.0001. [^aromatic_catabolism_network] This result supports a strong condition-dependent Complex I effect, but it does not by itself establish that aromatic substrates are the causal driver. [^aromatic_catabolism_network]

Per-condition results refine that association: the largest Complex I defects relative to background are -1.55 on acetate and -1.39 on succinate. [^aromatic_catabolism_network] Because acetate and succinate are non-aromatic substrates that generate high NADH flux through the TCA cycle, these observations support reducing-equivalent load as an alternative explanation for the apparent aromatic association. [^aromatic_catabolism_network] Complex I is reported as dispensable on glucose and lactate, which is consistent with the hypothesis that [ndh-2](../entities/ndh-2.md) can compensate under lower NADH flux. [^aromatic_catabolism_network]

The wiring analysis **qualifies** that compensation hypothesis rather than confirming it. Complex I growth ratios are 0.37 on quinate, 1.44 on glucose, and 0.49 on acetate, while ACIAD3522 has a growth ratio of 0.013 on acetate. [^respiratory_chain_wiring] NDH-2 is present as ACIAD_RS16420 (KO K03885), but has no growth data; cross-species analysis found validated NDH-2 in 5 of 14 organisms, with no significant support for the predicted compensation pattern (p = 0.52). [^respiratory_chain_wiring]

## Evidence from metabolic flux and gene phenotypes

Flux-balance analysis (FBA), a growth-optimizing constraint-based model of metabolism, predicts 1.76× higher Complex I flux on aromatic substrates than on the comparison condition, with fluxes of 0.55 versus 0.31. [^aromatic_catabolism_network] This supports increased respiratory demand during aromatic growth, but the same model predicts 0% essentiality for Complex I. [^aromatic_catabolism_network] The contrast indicates that modeled flux capacity and gene essentiality are not equivalent: the model can redistribute flux through alternative routes, whereas disruption of a multi-subunit complex can eliminate complex function. [^aromatic_catabolism_network]

Observed phenotypes provide direct support for a complex-level dependency: 10/13 Complex I operon subunits independently produce quinate-specific growth defects. [^aromatic_catabolism_network] However, the quinate-specific phenotype does not distinguish aromatic substrate chemistry from the reducing-equivalent burden associated with processing that substrate. [^aromatic_catabolism_network]

The new analysis **supports** the capacity interpretation but **refines** the mechanism: theoretical stoichiometry gives quinate 4 NADH (0.57 NADH/carbon) and glucose 9 NADH (1.50 NADH/carbon), while concentrated TCA-cycle NADH production is proposed to exceed alternative dehydrogenase capacity on quinate. [^respiratory_chain_wiring] This is a biochemical interpretation based on theoretical pathway stoichiometry, not measured flux distributions. [^respiratory_chain_wiring] FBA predicts zero NDH-2 flux on standard carbon sources because growth optimization routes NADH through the ATP-favorable Complex I pathway, illustrating why capacity constraints and alternative suboptimal routes can be missed. [^respiratory_chain_wiring]

## Limits of the inference

The cross-species fitness evidence is not definitive for ADP1 because the transferred data mixes organisms with different respiratory-chain architectures. [^aromatic_catabolism_network] The conclusion that NADH load, rather than substrate identity, is the primary driver is therefore a hypothesis rather than an established general rule. [^aromatic_catabolism_network] Direct Complex I fitness measurements on aromatic and non-aromatic substrates in the same organism would provide a stronger test.

The capability–dependency study **supports** this caution because its latent fraction varied from 0–31.6% across organisms and from 4.7% to 21.1% across tested classification thresholds; it also notes that Fitness Browser experiments are biased toward laboratory conditions. [^metabolic_capability_dependency] The newer analysis further **supports** this caution: only 7 of 48 Fitness Browser organisms had matching GapMind data, and its condition-specific latent reclassification used a median-based threshold that can cause pathways to cross the threshold by construction. [^pathway_capability_dependency] Thus, an apparently latent respiratory or metabolic capability may reflect untested environmental conditions or calibration choices rather than true dispensability. [^metabolic_capability_dependency] [^pathway_capability_dependency]

The proposed compensation by NDH-2 also requires direct testing because the report recommends searching the ADP1 genome for NDH-2 and comparing its deletion phenotype on quinate versus glucose. [^aromatic_catabolism_network] The new evidence **refines** this open test by identifying NDH-2 in ADP1 while confirming that it is TnSeq-dispensable but absent from the deletion collection and has no direct growth data. [^respiratory_chain_wiring] Proteomics further supports a passive, flux-based model: Complex I, NDH-2, and ACIAD3522 had similar protein levels under standard growth conditions, with means of 27.6, 27.0, and 26.2, respectively. [^respiratory_chain_wiring]

## Tensions

The earlier transferred-fitness interpretation reports Complex I as dispensable on glucose and lactate and treats this as consistent with NDH-2 compensation. [^aromatic_catabolism_network] The new ADP1-specific analysis reports a Complex I growth ratio of 1.44 on glucose, predicts zero NDH-2 flux under standard FBA conditions, and finds no significant cross-species compensation pattern (p = 0.52). [^respiratory_chain_wiring] These results do not establish that the earlier interpretation is false: they may reflect different fitness metrics, model assumptions, or species-level respiratory architectures. Resolving the tension requires matched ADP1 deletion assays and direct NADH/NAD⁺ measurements across carbon sources. [^respiratory_chain_wiring]

## Relation to other concepts

This concept **refines** [condition-specific-fitness](condition-specific-fitness.md) by separating the observed condition effect from the chemical identity of the substrate. [^aromatic_catabolism_network] It **supports** [metabolic-model-gapfilling](metabolic-model-gapfilling.md) because the model captures increased Complex I flux but misses the corresponding essentiality and leaves respiratory-support functions incompletely represented. [^aromatic_catabolism_network] The wiring analysis **strengthens** this connection by showing that FBA preferentially routes NADH through the ATP-favorable pathway and can therefore miss condition-specific capacity constraints. [^respiratory_chain_wiring] The capability–dependency results **refine** this connection by demonstrating that completeness predictions and measured fitness dependence can diverge, with the divergence sensitive to pathway mapping and laboratory condition coverage. [^metabolic_capability_dependency] [^pathway_capability_dependency] It also **connects** [respiratory-capacity-and-nadh-load](respiratory-capacity-and-nadh-load.md) to [complex-i](../entities/complex-i.md) and [ndh-2](../entities/ndh-2.md) as candidate components of the capacity limit. [^aromatic_catabolism_network]

## Open Directions

- Measure Complex I and NDH-2 deletion fitness in ADP1 on quinate, acetate, succinate, glucose, and lactate, using matched growth assays to ask whether fitness loss follows NADH-generating load rather than aromatic substrate identity. [^aromatic_catabolism_network]
- Measure NADH/NAD⁺ ratios across those carbon sources and test whether an NDH-2 deletion changes the predicted condition-specific respiratory requirement. [^respiratory_chain_wiring]
- Expand the condition panel with benzoate, catechol, vanillate, iron limitation, and respiratory inhibitors, then recompute co-fitness and condition-specific fitness to separate aromatic chemistry, iron demand, and respiratory load. [^aromatic_catabolism_network]
- Add PQQ biosynthesis, iron homeostasis, and respiratory-chain capacity constraints to the ADP1 FBA model, then compare predicted essentiality and flux with the observed defects in 10/13 Complex I operon subunits. [^aromatic_catabolism_network]
- Compare Complex I retention and NDH-2 complements across aromatic-degrading species using pangenome data and KO-based searches to test whether respiratory architecture predicts transferability of the NADH-load hypothesis. [^aromatic_catabolism_network] [^respiratory_chain_wiring]
- Reanalyze pathway capability and fitness dependence with direct GapMind per-step gene assignments and matched non-laboratory conditions, testing whether respiratory-pathway completeness predicts NADH-load-dependent fitness rather than substrate category. [^metabolic_capability_dependency]
- Calibrate condition-specific pathway-importance thresholds against independently defined essentials, then test whether the resulting respiratory classifications reproduce NADH-load-dependent fitness in matched ADP1 assays. [^pathway_capability_dependency]

[^aromatic_catabolism_network]: [aromatic catabolism network](../summaries/aromatic_catabolism_network__REPORT.md)
[^respiratory_chain_wiring]: [respiratory chain wiring](../summaries/respiratory_chain_wiring__REPORT.md)
[^pathway_capability_dependency]: [pathway capability dependency](../summaries/pathway_capability_dependency__REPORT.md)
[^metabolic_capability_dependency]: [metabolic capability dependency](../summaries/metabolic_capability_dependency__REPORT.md)
