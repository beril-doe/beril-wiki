---
type: "Concept"
description: "Why transferred fitness phenotypes depend on species-specific respiratory networks"
sources: ["summaries/aromatic_catabolism_network__REPORT.md"]
---
# Ortholog-transferred fitness phenotypes are constrained by organism-specific network architecture

Ortholog-transferred fitness phenotypes can suggest conserved functional dependencies, but their interpretation is limited when organisms differ in respiratory-chain composition, pathway wiring, or metabolic capacity. [src: aromatic_catabolism_network] This concept refines [[concepts/condition-specific-fitness]] by distinguishing a phenotype caused by a shared substrate-driven demand from one caused by architecture-specific compensation or constraint. [src: aromatic_catabolism_network]

## Evidence from Complex I fitness transfer

The [[entities/kescience-fitnessbrowser]] ortholog-transferred dataset contains 12,241 entries covering 2,005 genes and 13 conditions. [src: aromatic_catabolism_network] In that dataset, Complex I orthologs have significantly worse fitness on aromatic conditions than on comparison conditions, with mean fitness values of -1.35 versus -0.77 and Mann-Whitney p < 0.0001. [src: aromatic_catabolism_network]

This result supports the hypothesis that ortholog-level fitness transfer can recover a substrate-associated respiratory demand, but it does not establish that aromatic catabolism itself causes the dependency in every recipient organism. [src: aromatic_catabolism_network] The largest Complex I defects relative to background occurred on acetate (-1.55) and succinate (-1.39), which are non-aromatic substrates that also generate high NADH flux through the TCA cycle. [src: aromatic_catabolism_network] Thus, the transferred phenotype refines the interpretation from an aromatic-specific effect toward a dependence associated with NADH-generating substrates. [src: aromatic_catabolism_network]

## Why architecture limits transferability

Bacterial respiratory chains can contain both proton-pumping Complex I, also called NDH-1, and non-pumping NDH-2, an alternative NADH dehydrogenase. [src: aromatic_catabolism_network] In the proposed model, NDH-2 can compensate under lower NADH flux but may not match Complex I capacity under high NADH flux. [src: aromatic_catabolism_network] A fitness phenotype transferred between orthologs therefore depends not only on the ortholog's molecular role but also on whether the recipient organism has an alternative route with sufficient capacity. [src: aromatic_catabolism_network]

The transferred evidence is not definitive for [[entities/acinetobacter-baylyi-adp1]] because the dataset mixes organisms with different respiratory-chain architectures. [src: aromatic_catabolism_network] Complex I was reported as dispensable on glucose and lactate, which is consistent with compensation by NDH-2 under lower NADH flux, but this interpretation remains a hypothesis rather than a demonstrated universal rule. [src: aromatic_catabolism_network]

## Relation to direct ADP1 evidence

In *Acinetobacter baylyi* ADP1, the aromatic-catabolism study identified a 51-gene support network surrounding the [[entities/beta-ketoadipate-pathway]], including 21 Complex I genes. [src: aromatic_catabolism_network] FBA, or flux-balance analysis, captured 1.76× higher Complex I flux on aromatic substrates than on the comparison condition, with fluxes of 0.55 versus 0.31, but predicted 0% essentiality for Complex I. [src: aromatic_catabolism_network] Independently, 10/13 Complex I operon subunits produced quinate-specific growth defects. [src: aromatic_catabolism_network]

The direct ADP1 measurements therefore show that a model or transferred phenotype can understate a complex-level dependency when alternative flux routes are available in the representation. [src: aromatic_catabolism_network] They also provide a species-specific anchor for evaluating whether the cross-species Complex I signal reflects aromatic catabolism, high NADH flux, or differences in respiratory-chain architecture. [src: aromatic_catabolism_network]

## Interpretation and limitation

Ortholog-transferred fitness is strongest as evidence for a conserved direction of functional pressure when the compared organisms share relevant pathway and respiratory architectures. [src: aromatic_catabolism_network] It is weaker as evidence for a conserved magnitude of fitness cost or for a universal condition-specific essentiality rule when alternative dehydrogenases, pathway bypasses, or complex capacities differ between organisms. [src: aromatic_catabolism_network] The 12,241-entry dataset provides a comparative signal, whereas direct Complex I fitness measurements on aromatic substrates in a single organism would provide a stronger test of the causal role of aromatic catabolism. [src: aromatic_catabolism_network]

This limitation connects to [[concepts/cross-species-fitness-transferability]] and [[concepts/respiratory-capacity-and-nadh-load]]: transferred phenotypes should be interpreted against recipient-specific network architecture rather than treated as architecture-independent annotations. [src: aromatic_catabolism_network]

## Open Directions

- Measure Complex I and NDH-2 deletion fitness directly in ADP1 on quinate, glucose, acetate, and succinate to test whether the phenotype tracks aromatic catabolism or NADH-generating substrate load. [src: aromatic_catabolism_network]
- Search the ADP1 genome for NDH-2 and combine deletion experiments with respiratory-capacity measurements to determine whether alternative NADH dehydrogenase activity explains the glucose and lactate results. [src: aromatic_catabolism_network]
- Stratify the [[entities/kescience-fitnessbrowser]] ortholog-transferred data by organism and respiratory-chain architecture, then compare effect sizes across architectures to quantify transferability. [src: aromatic_catabolism_network]
- Expand comparative pangenome analysis across aromatic-degrading species to test whether Complex I retention and NDH-2 presence predict transferred fitness phenotypes. [src: aromatic_catabolism_network]
- Rebuild the ADP1 FBA model with PQQ biosynthesis, iron homeostasis, and respiratory-chain capacity constraints, then test whether architecture-aware constraints reduce the gap between predicted 0% essentiality and the observed defects in 10/13 Complex I subunits. [src: aromatic_catabolism_network]
