---
type: Gene_Or_Pathway
description: Alternative NADH dehydrogenase identified as ACIAD_RS16420 (KO K03885).
sources:
- id: respiratory_chain_wiring
  resource: ../summaries/respiratory_chain_wiring__REPORT.md
  title: respiratory chain wiring
title: NDH-2
---
# NDH-2

## What it is

**Canonical name:** NDH-2. [^respiratory_chain_wiring]  
**Known alias:** ACIAD_RS16420. [^respiratory_chain_wiring]  
**Stable external identifier:** KEGG orthology K03885. [^respiratory_chain_wiring]

NDH-2 is a single-subunit, non-proton-pumping NADH dehydrogenase in [acinetobacter-baylyi-adp1](acinetobacter-baylyi-adp1.md) and is part of the organism’s branched respiratory chain alongside [complex-i](complex-i.md). [^respiratory_chain_wiring]  

## Evidence from respiratory-chain wiring

NDH-2 is a standalone gene rather than part of a respiratory operon, is present in the core genome, and is TnSeq-dispensable. [^respiratory_chain_wiring]  

NDH-2 is absent from the available deletion collection, so its condition-specific growth phenotype has not been directly measured. [^respiratory_chain_wiring]  

Flux-balance analysis (FBA), a computational method that predicts metabolic flux by optimizing a specified objective, predicted zero flux through NDH-2 on all standard carbon sources because the model routed NADH through [complex-i](complex-i.md). [^respiratory_chain_wiring]  

The model’s zero-flux prediction does not establish that NDH-2 is unused in vivo, because the growth-optimization objective preferentially selects the ATP-favorable respiratory route and does not represent pathway capacity constraints. [^respiratory_chain_wiring]  

Under standard growth conditions, NDH-2 had a protein abundance value of 27.0 at the 59th percentile, compared with 27.6 at the 66th percentile for Complex I and 26.2 at the 48th percentile for ACIAD3522. [^respiratory_chain_wiring]  

NDH-2 was therefore not repressed under the measured conditions and was co-expressed with the other NADH dehydrogenases, supporting a passive flux-based wiring model rather than a demonstrated transcriptional switch. [^respiratory_chain_wiring]  

## Cross-species comparison

After filtering likely false positives by retaining organisms with 1–2 NDH-2 hits and excluding organisms with more than 2 hits, 5 of 14 organisms had validated NDH-2. [^respiratory_chain_wiring]  

Organisms with validated NDH-2 had a mean Complex I aromatic deficit of −0.297, compared with −0.156 in organisms without validated NDH-2. [^respiratory_chain_wiring]  

The difference was not statistically significant, with p = 0.52, and it opposed the predicted pattern in which NDH-2 would compensate for reduced Complex I dependence on aromatic substrates. [^respiratory_chain_wiring]  

The comparison included only 4 organisms lacking NDH-2, making it underpowered, and annotation variation may have caused orthologs to be missed. [^respiratory_chain_wiring]

## Interpretation and open tests

The report proposes that NDH-2 may provide an alternative NADH-reoxidation route whose importance depends on substrate-generated NADH flux, but this remains a hypothesis because NDH-2 has no direct growth data and the stoichiometric analysis used theoretical rather than measured flux distributions. [^respiratory_chain_wiring]  

A direct test would be to construct an NDH-2 deletion mutant and measure NADH/NAD⁺ ratios and growth on each tested carbon source. [^respiratory_chain_wiring]  

Additional tests include KO-based searches using K03885 across a larger species set and pangenome co-occurrence analysis with Complex I genes K00330–K00343. [^respiratory_chain_wiring]

## Related pages

- [respiratory_chain_wiring__REPORT](../summaries/respiratory_chain_wiring__REPORT.md) — source report on condition-specific respiratory-chain wiring in ADP1.
- [acinetobacter-baylyi-adp1](acinetobacter-baylyi-adp1.md) — organism in which NDH-2 is characterized.
- [complex-i](complex-i.md) — proton-pumping NADH dehydrogenase used as the principal modeled alternative.
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — context for substrate-dependent respiratory fitness.
- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) — context for limitations of growth-optimized FBA.
- [gene-essentiality](../concepts/gene-essentiality.md) — context for TnSeq dispensability and condition-specific gene fitness.

[^respiratory_chain_wiring]: [respiratory chain wiring](../summaries/respiratory_chain_wiring__REPORT.md)
