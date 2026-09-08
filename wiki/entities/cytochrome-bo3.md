---
type: Gene_Or_Pathway
description: Respiratory-chain cytochrome bo3 with carbon-source-specific fitness
  requirements
sources:
- id: respiratory_chain_wiring
  resource: ../summaries/respiratory_chain_wiring__REPORT.md
  title: respiratory chain wiring
title: Cytochrome bo3
---
# Cytochrome bo3

## Identity

**Canonical name:** cytochrome bo3. [^respiratory_chain_wiring]

**Known alias:** cytochrome bo3 ubiquinol oxidase. [^respiratory_chain_wiring]

**Stable external identifier:** not reported in this document. [^respiratory_chain_wiring]

Cytochrome bo3 is a respiratory-chain component of [acinetobacter-baylyi-adp1](acinetobacter-baylyi-adp1.md) whose requirement changes with the carbon source. [^respiratory_chain_wiring]

## Evidence from Condition-Specific Respiratory Chain Wiring

ADP1 has 4 genes assigned to the cytochrome bo3 subsystem within a respiratory-chain inventory of 62 genes across 8 subsystems. [^respiratory_chain_wiring]

Cytochrome bo3 is required on acetate, where the respiratory chain also requires Complex I, ACIAD3522, and additional components. [^respiratory_chain_wiring]

Cytochrome bo3 is specifically required on lactate, while Complex I is mildly important and cytochrome bd is dispensable under that condition. [^respiratory_chain_wiring]

Cytochrome bo3 is dispensable on quinate, whereas Complex I is required. [^respiratory_chain_wiring]

Glucose has no specifically required respiratory component, and all listed components show full redundancy, including cytochrome bo3. [^respiratory_chain_wiring]

Urea is generally demanding across the respiratory chain and requires everything in the reported respiratory-chain profile, including cytochrome bo3. [^respiratory_chain_wiring]

These results support [condition-specific-fitness](../concepts/condition-specific-fitness.md) by showing that cytochrome bo3 fitness depends qualitatively on the growth substrate rather than following a simple uniform respiratory-chain requirement. [^respiratory_chain_wiring]

The report interprets these condition-specific requirements together with gene-phenotype data, flux-balance analysis (FBA), theoretical stoichiometry, cross-species Fitness Browser data, and proteomics. [^respiratory_chain_wiring]

## Related Pages

- [acinetobacter-baylyi-adp1](acinetobacter-baylyi-adp1.md)
- [respiratory_chain_wiring__REPORT](../summaries/respiratory_chain_wiring__REPORT.md)
- [condition-specific-fitness](../concepts/condition-specific-fitness.md)
- [gene-essentiality](../concepts/gene-essentiality.md)
- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md)

[^respiratory_chain_wiring]: [respiratory chain wiring](../summaries/respiratory_chain_wiring__REPORT.md)
