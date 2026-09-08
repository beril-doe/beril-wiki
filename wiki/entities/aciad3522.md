---
type: Gene_Or_Pathway
description: ACIAD3522 is an NADH-FMN oxidoreductase with acetate-specific fitness
  effects in ADP1.
sources:
- id: respiratory_chain_wiring
  resource: ../summaries/respiratory_chain_wiring__REPORT.md
  title: respiratory chain wiring
title: ACIAD3522
---
# ACIAD3522

## What this entity is

**Canonical name:** ACIAD3522. [^respiratory_chain_wiring]  
**Known aliases:** No aliases are reported in the source document. [^respiratory_chain_wiring]  
**Stable external identifier:** No stable external identifier is reported in the source document. [^respiratory_chain_wiring]

ACIAD3522 is described as a single-subunit NADH-FMN oxidoreductase and is analyzed as one of three parallel NADH dehydrogenase activities in [acinetobacter-baylyi-adp1](acinetobacter-baylyi-adp1.md). [^respiratory_chain_wiring] The report cautions that ACIAD3522 may not be a respiratory NADH dehydrogenase in the strict sense and could instead have another metabolic function. [^respiratory_chain_wiring]

## Evidence from respiratory-chain wiring

ACIAD3522 is dispensable on quinate and glucose but has a growth ratio of 0.013 on acetate, where the report describes its phenotype as lethal. [^respiratory_chain_wiring] Acetate therefore specifically requires ACIAD3522 in the reported respiratory-chain profile, alongside Complex I, cytochrome bo3, and additional components. [^respiratory_chain_wiring]

Flux-balance analysis (FBA), a computational optimization method for predicting metabolic fluxes, predicts zero flux through ACIAD3522 on all standard media because the model routes NADH through Complex I, which produces more ATP per NADH. [^respiratory_chain_wiring] This result illustrates how growth optimization in [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) can miss alternative or conditionally required respiratory pathways. [^respiratory_chain_wiring]

Under standard growth conditions, ACIAD3522 had a mean protein level of 26.2 at the 48th percentile, compared with a genome median of 26.4. [^respiratory_chain_wiring] Its similar abundance to Complex I and NDH-2 supports the report's passive, flux-based wiring interpretation rather than a transcriptional switch, although this interpretation does not establish ACIAD3522's biochemical function. [^respiratory_chain_wiring]

## Interpretation and open tests

The acetate-specific fitness effect supports a condition-specific respiratory requirement in [condition-specific-fitness](../concepts/condition-specific-fitness.md) and adds evidence to [gene-essentiality](../concepts/gene-essentiality.md) that gene importance can change with carbon source. [^respiratory_chain_wiring] The source identifies characterization of ACIAD3522 as a needed test because its NADH-FMN oxidoreductase annotation may represent a function other than respiratory NADH dehydrogenation. [^respiratory_chain_wiring]

## Related pages

- [respiratory_chain_wiring__REPORT](../summaries/respiratory_chain_wiring__REPORT.md) — source summary containing the ACIAD3522 fitness, flux, and proteomics evidence. [^respiratory_chain_wiring]
- [acinetobacter-baylyi-adp1](acinetobacter-baylyi-adp1.md) — organism in which ACIAD3522 is studied. [^respiratory_chain_wiring]
- [complex-i](complex-i.md) — alternative NADH dehydrogenase used by the model for NADH oxidation. [^respiratory_chain_wiring]
- [ndh-2](ndh-2.md) — other NADH dehydrogenase included in the respiratory-chain comparison. [^respiratory_chain_wiring]
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — concept covering substrate-dependent gene fitness. [^respiratory_chain_wiring]
- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) — concept addressing limitations of growth-optimized metabolic models. [^respiratory_chain_wiring]
- [gene-essentiality](../concepts/gene-essentiality.md) — concept receiving the acetate-specific ACIAD3522 fitness evidence. [^respiratory_chain_wiring]
- [multi-omics-integration](../concepts/multi-omics-integration.md) — concept receiving the integrated fitness, FBA, stoichiometric, and proteomic interpretation. [^respiratory_chain_wiring]

[^respiratory_chain_wiring]: [respiratory chain wiring](../summaries/respiratory_chain_wiring__REPORT.md)
