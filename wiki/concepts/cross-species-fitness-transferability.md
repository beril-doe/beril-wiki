---
type: Concept
description: Ortholog fitness transfer depends on recipient-specific network architecture
sources:
- id: aromatic_catabolism_network
  resource: ../summaries/aromatic_catabolism_network__REPORT.md
  title: aromatic catabolism network
- id: pathway_capability_dependency
  resource: ../summaries/pathway_capability_dependency__REPORT.md
  title: pathway capability dependency
- id: respiratory_chain_wiring
  resource: ../summaries/respiratory_chain_wiring__REPORT.md
  title: respiratory chain wiring
- id: metabolic_capability_dependency
  resource: ../summaries/metabolic_capability_dependency__REPORT.md
  title: metabolic capability dependency
title: Ortholog-transferred fitness phenotypes are constrained by organism-specific
  network architecture
---
# Ortholog-transferred fitness phenotypes are constrained by organism-specific network architecture

Ortholog-transferred fitness phenotypes can suggest conserved functional dependencies, but their interpretation is limited when organisms differ in respiratory-chain composition, pathway wiring, or metabolic capacity. [^aromatic_catabolism_network] This concept refines [condition-specific-fitness](condition-specific-fitness.md) by distinguishing a phenotype caused by a shared substrate-driven demand from one caused by architecture-specific compensation or constraint. [^aromatic_catabolism_network]

## Evidence from Complex I fitness transfer

The [kescience-fitnessbrowser](../entities/kescience-fitnessbrowser.md) ortholog-transferred dataset contains 12,241 entries covering 2,005 genes and 13 conditions. [^aromatic_catabolism_network] In that dataset, Complex I orthologs have significantly worse fitness on aromatic conditions than on comparison conditions, with mean fitness values of -1.35 versus -0.77 and Mann-Whitney p < 0.0001. [^aromatic_catabolism_network]

This result supports the hypothesis that ortholog-level fitness transfer can recover a substrate-associated respiratory demand, but it does not establish that aromatic catabolism itself causes the dependency in every recipient organism. [^aromatic_catabolism_network] The largest Complex I defects relative to background occurred on acetate (-1.55) and succinate (-1.39), which are non-aromatic substrates that also generate high NADH flux through the TCA cycle. [^aromatic_catabolism_network] Thus, the transferred phenotype refines the interpretation from an aromatic-specific effect toward a dependence associated with NADH-generating substrates. [^aromatic_catabolism_network]

The metabolic capability–dependency analysis supports this caution: among 1,695 complete pathway-organism pairs from 48 organisms, 267 (15.8%) were classified as latent capabilities, meaning complete pathways with fitness-neutral measurements under the study thresholds, while 881 (51.9%) were active and 547 (32.3%) intermediate. [^metabolic_capability_dependency] Pathway category strongly predicted dependency class (χ²=163.6, df=4, p=2.5×10⁻³⁴), and carbon-source pathways were more often latent than amino-acid biosynthesis pathways (24.3% versus 6.5%). [^metabolic_capability_dependency] This **supports** interpreting transferred phenotypes as condition-dependent evidence of pressure rather than permanent pathway essentiality. The related pathway-capability report's finding that, across 161 organism-pathway pairs, complete pathway capability and observed fitness dependency were distinct classifications, with 66 complete but non-important “Latent Capability” pairs, remains relevant; all 66 became fitness-important under at least one tested condition type, although the median-based reclassification threshold is partly circular. [^pathway_capability_dependency]

## Why architecture limits transferability

Bacterial respiratory chains can contain both proton-pumping Complex I, also called NDH-1, and non-pumping NDH-2, an alternative NADH dehydrogenase. [^aromatic_catabolism_network] In the proposed model, NDH-2 can compensate under lower NADH flux but may not match Complex I capacity under high NADH flux. [^aromatic_catabolism_network] A fitness phenotype transferred between orthologs therefore depends not only on the ortholog's molecular role but also on whether the recipient organism has an alternative route with sufficient capacity. [^aromatic_catabolism_network]

The new ADP1 respiratory-chain analysis **supports** the architecture-aware interpretation: it found qualitatively different carbon-source wiring, with Complex I required on quinate but dispensable on glucose, and attributed the contrast to substrate-dependent NADH flux and capacity constraints rather than total reducing-equivalent yield. [^respiratory_chain_wiring] Proteomics further found similar standard-condition protein levels for Complex I, NDH-2, and ACIAD3522—27.6, 27.0, and 26.2, respectively—supporting simultaneous availability rather than a transcriptional switch. [^respiratory_chain_wiring] However, the interpretation remains partly model-based: the proposed quinate NADH burst and capacity limit use theoretical pathway stoichiometry rather than measured flux distributions. [^respiratory_chain_wiring]

The transferred evidence is not definitive for Acinetobacter baylyi ADP1 because the dataset mixes organisms with different respiratory-chain architectures. [^aromatic_catabolism_network] Complex I was reported as dispensable on glucose and lactate, which is consistent with compensation by NDH-2 under lower NADH flux, but this interpretation remains a hypothesis rather than a demonstrated universal rule. [^aromatic_catabolism_network] The ADP1 analysis **refines** that hypothesis: NDH-2 had no growth data, and its FBA-predicted flux was zero on all standard carbon sources because growth optimization routed NADH through Complex I. [^respiratory_chain_wiring]

The metabolic capability–dependency analysis **supports** the need for caution when generalizing across organisms: only 7 of 48 Fitness Browser organisms had matching GapMind genome data, and only 48 organisms were fitness-tested among 293,000 genomes with pathway predictions. [^metabolic_capability_dependency] Its clade-level result also linked latent-capability rate to pangenome openness (Spearman ρ = 0.69, p = 0.0004, n = 22 clades), suggesting that genome dynamics and community context can shape whether encoded capabilities become dependencies. [^metabolic_capability_dependency] This **refines** the architecture argument by placing respiratory alternatives within a broader organism-specific network and pangenome context, rather than treating transferred effects as properties of orthologs alone. The earlier comparison remains: matched Tier 1 organisms had near-complete, well-annotated core genomes, with mean core-gene completeness of 0.986 for Active Dependencies and 0.975 for Latent Capabilities. [^pathway_capability_dependency]

## Relation to direct ADP1 evidence

In *Acinetobacter baylyi* ADP1, the aromatic-catabolism study identified a 51-gene support network surrounding the [beta-ketoadipate-pathway](../entities/beta-ketoadipate-pathway.md), including 21 Complex I genes. [^aromatic_catabolism_network] FBA, or flux-balance analysis, captured 1.76× higher Complex I flux on aromatic substrates than on the comparison condition, with fluxes of 0.55 versus 0.31, but predicted 0% essentiality for Complex I. [^aromatic_catabolism_network] Independently, 10/13 Complex I operon subunits produced quinate-specific growth defects. [^aromatic_catabolism_network]

The direct ADP1 measurements therefore show that a model or transferred phenotype can understate a complex-level dependency when alternative flux routes are available in the representation. [^aromatic_catabolism_network] They also provide a species-specific anchor for evaluating whether the cross-species Complex I signal reflects aromatic catabolism, high NADH flux, or differences in respiratory-chain architecture. [^aromatic_catabolism_network] The respiratory-chain analysis **supports** this reading by identifying FBA's growth optimization and ATP-favorable Complex I routing as reasons it misses alternative, capacity-limited respiratory requirements. [^respiratory_chain_wiring]

The pathway-capability results **refine** this comparison by showing that an apparently complete pathway can remain fitness-silent under standard conditions yet become important under stress, nitrogen limitation, or carbon limitation. [^pathway_capability_dependency] Conversely, an Incomplete but Important classification can reflect annotation gaps or salvage routes rather than absence of function. [^pathway_capability_dependency] These categories reinforce that pathway completeness, transferred fitness, and direct organism-level dependency are related but non-equivalent evidence layers. The metabolic analysis further found that the latent fraction varied from 0–31.6% across organisms and from 4.7% to 21.1% across tested threshold combinations, **supporting** the conclusion that the inferred capability–dependency boundary is condition- and threshold-sensitive. [^metabolic_capability_dependency]

## Tensions

The aromatic-catabolism analysis proposes that NDH-2 compensation can explain lower Complex I dependence on some substrates, while the cross-species respiratory-chain comparison found no supporting compensation pattern: among organisms retained after filtering, validated NDH-2 organisms had a larger mean Complex I aromatic deficit (-0.297 versus -0.156), with p = 0.52. [^respiratory_chain_wiring] The comparison included only 4 organisms lacking NDH-2 and may therefore be underpowered; the two results should not be reconciled as a universal rule. [^respiratory_chain_wiring] The former remains a substrate- and architecture-based hypothesis [^aromatic_catabolism_network], whereas the latter weakens its generalization across species. [^respiratory_chain_wiring]

The metabolic capability analysis introduces a related limitation rather than resolving this tension: pathway-level conservation did not distinguish latent capabilities from active dependencies, with mean conservation of 0.869 for 248 latent capabilities versus 0.829 for 755 active dependencies and Mann–Whitney U p = 0.94 for active > latent. [^metabolic_capability_dependency] Thus, conserved pathway presence alone does not establish conserved fitness dependence, **supporting** the caution that ortholog transfer cannot substitute for recipient-specific network and condition measurements. [^metabolic_capability_dependency]

## Interpretation and limitation

Ortholog-transferred fitness is strongest as evidence for a conserved direction of functional pressure when the compared organisms share relevant pathway and respiratory architectures. [^aromatic_catabolism_network] It is weaker as evidence for a conserved magnitude of fitness cost or for a universal condition-specific essentiality rule when alternative dehydrogenases, pathway bypasses, or complex capacities differ between organisms. [^aromatic_catabolism_network] The 12,241-entry dataset provides a comparative signal, whereas direct Complex I fitness measurements on aromatic substrates in a single organism would provide a stronger test of the causal role of aromatic catabolism. [^aromatic_catabolism_network]

This limitation connects to [cross-species-fitness-transferability](cross-species-fitness-transferability.md) and [respiratory-capacity-and-nadh-load](respiratory-capacity-and-nadh-load.md): transferred phenotypes should be interpreted against recipient-specific network architecture rather than treated as architecture-independent annotations. [^aromatic_catabolism_network] The metabolic capability study **supports** this interpretation while showing that environment-linked metabolic clusters are not universal: all 10 target species formed clusters, but significant environment–cluster associations were reported only for *Salmonella enterica* and *Phenylobacterium* sp.; the ecological interpretation was observational and lacked explicit phylogenetic correction. [^metabolic_capability_dependency] The full ADP1 evidence and its limitations are summarized in [respiratory_chain_wiring__REPORT](../summaries/respiratory_chain_wiring__REPORT.md), while the capability–dependency evidence is summarized in [metabolic_capability_dependency__REPORT](../summaries/metabolic_capability_dependency__REPORT.md).

## Open Directions

- Measure Complex I and NDH-2 deletion fitness directly in ADP1 on quinate, glucose, acetate, and succinate to test whether the phenotype tracks aromatic catabolism or NADH-generating substrate load. [^aromatic_catabolism_network]
- Search the ADP1 genome for NDH-2 and combine deletion experiments with respiratory-capacity measurements to determine whether alternative NADH dehydrogenase activity explains the glucose and lactate results. [^aromatic_catabolism_network]
- Stratify the [kescience-fitnessbrowser](../entities/kescience-fitnessbrowser.md) ortholog-transferred data by organism and respiratory-chain architecture, then compare effect sizes across architectures to quantify transferability. [^aromatic_catabolism_network]
- Expand comparative pangenome analysis across aromatic-degrading species to test whether Complex I retention and NDH-2 presence predict transferred fitness phenotypes. [^aromatic_catabolism_network]
- Rebuild the ADP1 FBA model with PQQ biosynthesis, iron homeostasis, and respiratory-chain capacity constraints, then test whether architecture-aware constraints reduce the gap between predicted 0% essentiality and the observed defects in 10/13 Complex I subunits. [^aromatic_catabolism_network]
- Reanalyze transferred fitness alongside pathway completeness and condition-specific fitness across organisms with matched GapMind and Fitness Browser data to test whether architecture-aware transfer predicts Active Dependency, Latent Capability, or Incomplete but Important classifications. [^pathway_capability_dependency]
- Use KO-based K03885 and K00330–K00343 searches across the planned 27K-species comparison, then test whether NDH-2 presence predicts Complex I fitness only within matched respiratory architectures. [^respiratory_chain_wiring]
- Measure NADH/NAD⁺ ratios and respiratory-chain protein abundances across ADP1 carbon sources to distinguish the proposed flux-capacity mechanism from transcriptional regulation. [^respiratory_chain_wiring]
- Use direct GapMind per-step gene assignments and matched fitness assays across multiple organisms to test whether architecture-aware ortholog transfer predicts latent versus active pathway dependency; this addresses the current SEED-proxy mapping limitation and the 4.7%–21.1% threshold sensitivity range. [^metabolic_capability_dependency]

[^aromatic_catabolism_network]: [aromatic catabolism network](../summaries/aromatic_catabolism_network__REPORT.md)
[^metabolic_capability_dependency]: [metabolic capability dependency](../summaries/metabolic_capability_dependency__REPORT.md)
[^pathway_capability_dependency]: [pathway capability dependency](../summaries/pathway_capability_dependency__REPORT.md)
[^respiratory_chain_wiring]: [respiratory chain wiring](../summaries/respiratory_chain_wiring__REPORT.md)
