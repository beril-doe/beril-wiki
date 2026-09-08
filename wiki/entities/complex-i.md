---
type: Gene_Or_Pathway
description: Respiratory Complex I links NADH flux to condition-specific fitness in
  ADP1
sources:
- id: aromatic_catabolism_network
  resource: ../summaries/aromatic_catabolism_network__REPORT.md
  title: aromatic catabolism network
- id: respiratory_chain_wiring
  resource: ../summaries/respiratory_chain_wiring__REPORT.md
  title: respiratory chain wiring
title: Complex I
---
# Complex I

## Identity

**Canonical name:** Complex I. [^aromatic_catabolism_network]

**Known aliases:** NADH:ubiquinone oxidoreductase; NDH-1; nuoA–N respiratory complex. [^aromatic_catabolism_network]

**Stable external identifier:** No stable external identifier was specified in the source. [^aromatic_catabolism_network]

Complex I is a multi-subunit respiratory subsystem that oxidizes NADH and supports high-flux catabolism by transferring reducing power into the respiratory chain. [^aromatic_catabolism_network] In ADP1 it is a 13-subunit, proton-pumping complex that translocates 4 H⁺/NADH. [^respiratory_chain_wiring]

## Evidence from the aromatic-catabolism network

Complex I is the largest support subsystem in the 51-gene quinate-catabolism network, containing 21/51 quinate-specific genes, or 41% of the network. [^aromatic_catabolism_network]

The network analysis links Complex I to oxidation of NADH generated when aromatic-catabolism products enter the TCA cycle. [^aromatic_catabolism_network]

[Flux-balance analysis](flux-balance-analysis.md) predicts 1.76× higher Complex I flux on aromatic substrates than on the comparison condition, with fluxes of 0.55 versus 0.31. [^aromatic_catabolism_network]

Despite this increased predicted flux, the model predicts 0% Complex I essentiality, indicating a gap between modeled respiratory demand and gene-level dependency. [^aromatic_catabolism_network]

A total of 30/51 quinate-specific genes have no FBA reaction mappings, including newly identified Complex I-associated functions. [^aromatic_catabolism_network]

The source interprets this discrepancy as an [FBA model gap](../concepts/metabolic-model-gapfilling.md): growth-optimizing linear programming can redistribute flux through alternative routes, whereas disruption of a multi-subunit Complex I can eliminate complex function. [^aromatic_catabolism_network] The respiratory-chain wiring analysis **supports and refines** this interpretation: FBA routes NADH through Complex I because it produces more ATP per NADH, predicting zero flux through alternative dehydrogenases and missing capacity constraints that can force suboptimal respiratory routes. [^respiratory_chain_wiring]

Observed phenotypes support Complex I dependence more strongly than the model prediction: 10/13 Complex I operon subunits independently produce quinate-specific growth defects. [^aromatic_catabolism_network]

## Organization and candidate components

The Complex I operon lies at 714–729 kb and contains 13 nuoA–N subunits on the same strand, with <100 bp intergenic distances. [^aromatic_catabolism_network]

Two DUF-domain proteins, [ACIAD3137](aciad3137.md) (UPF0234) and [ACIAD2176](aciad2176.md) (DUF2280), correlate with Complex I genes at r > 0.98 and are candidate uncharacterized Complex I accessory factors. [^aromatic_catabolism_network]

The 11 Complex I-associated assignments beyond the core nuo operon are based on phenotypic correlation and may represent indirect connections rather than physical association. [^aromatic_catabolism_network]

## Condition-specific and cross-species fitness

The [KBase Fitness Browser](kescience-fitnessbrowser.md) ortholog-transferred dataset contains 12,241 entries covering 2,005 genes and 13 conditions. [^aromatic_catabolism_network]

Complex I orthologs have significantly worse fitness on aromatic conditions than on comparison conditions, with mean fitness values of -1.35 versus -0.77 and Mann–Whitney p < 0.0001. [^aromatic_catabolism_network]

The largest Complex I defects relative to background occur on acetate (-1.55) and succinate (-1.39), which are non-aromatic substrates that also generate high NADH flux through the TCA cycle. [^aromatic_catabolism_network]

Complex I is reported as dispensable on glucose and lactate, consistent with the hypothesis that an alternative NADH dehydrogenase, [NDH-2](ndh-2.md), compensates under lower NADH flux. [^aromatic_catabolism_network] The new ADP1 analysis **supports** substrate-dependent wiring but **refines** the mechanism: Complex I growth ratios are 0.37 on quinate, 1.44 on glucose, and 0.49 on acetate, while quinate requires Complex I, lactate specifically requires cytochrome bo3, and glucose has no specifically required respiratory component. [^respiratory_chain_wiring] The report proposes that quinate’s concentrated TCA-cycle NADH burst exceeds alternative dehydrogenase capacity, whereas glucose distributes NADH production; this is a biochemical interpretation based on theoretical stoichiometry rather than measured flux distributions. [^respiratory_chain_wiring]

Because the transferred data mixes organisms with different respiratory-chain architectures, the cross-species evidence does not definitively establish the cause of Complex I dependence in [Acinetobacter baylyi](acinetobacter-baylyi-adp1.md) ADP1. [^aromatic_catabolism_network] The new comparison **contradicts** the predicted general compensation pattern: among filtered organisms, those with validated NDH-2 had a mean Complex I aromatic deficit of −0.297 versus −0.156 without validated NDH-2 (p = 0.52), although only 4 organisms lacked NDH-2. [^respiratory_chain_wiring]

## Interpretation and open directions

The report's novel finding is a proposed relationship between Complex I dependence and high NADH flux rather than aromatic chemistry alone. [^aromatic_catabolism_network] Proteomics **supports** a passive, flux-based rather than transcriptionally switched model: Complex I, NDH-2, and ACIAD3522 had protein levels of 27.6, 27.0, and 26.2, respectively, compared with a genome median of 26.4. [^respiratory_chain_wiring]

This interpretation remains a hypothesis because direct Complex I fitness measurements on aromatic substrates in a single organism are not yet available in the source analysis. [^aromatic_catabolism_network] NDH-2 is a core, standalone gene identified as ACIAD_RS16420 (KO K03885), but it has no growth data; ACIAD3522 is dispensable on quinate and glucose and has a 0.013 growth ratio on acetate, where its function may not be respiratory. [^respiratory_chain_wiring]

Specific tests include searching the ADP1 genome for NDH-2, testing NDH-2 deletion on quinate versus glucose, validating ACIAD3137 and ACIAD2176 by protein-interaction or co-purification experiments, and adding respiratory-chain capacity constraints to the ADP1 FBA model. [^aromatic_catabolism_network] The first search is now resolved, while deletion experiments, NADH/NAD⁺ measurements, ACIAD3522 characterization, expanded KO-based cross-species analysis, and quinate-versus-succinate respiratory proteomics remain tests of the wiring hypothesis. [^respiratory_chain_wiring]

## Related pages

- [aromatic_catabolism_network__REPORT](../summaries/aromatic_catabolism_network__REPORT.md) — source summary for the Complex I support-network analysis.
- [respiratory_chain_wiring__REPORT](../summaries/respiratory_chain_wiring__REPORT.md) — source summary for condition-specific respiratory-chain configuration in ADP1.
- [gene-essentiality](../concepts/gene-essentiality.md) — contrasts observed Complex I defects with 0% model-predicted essentiality.
- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) — covers unmapped support functions and respiratory blind spots in FBA.
- [cofitness-network-architecture](../concepts/cofitness-network-architecture.md) — covers co-fitness assignment of Complex I-associated genes and candidate accessory factors.
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — covers substrate-dependent Complex I fitness patterns.
- [multi-omics-integration](../concepts/multi-omics-integration.md) — covers integration of fitness, FBA, genomic organization, and transcriptomic evidence.

[^aromatic_catabolism_network]: [aromatic catabolism network](../summaries/aromatic_catabolism_network__REPORT.md)
[^respiratory_chain_wiring]: [respiratory chain wiring](../summaries/respiratory_chain_wiring__REPORT.md)
