---
type: Compound
description: Xanthine, an enrichment compound misclassified as carbon-catabolic
sources:
- id: enigma_carbon_census_1
  resource: ../summaries/enigma_carbon_census_1__REPORT.md
  title: enigma carbon census 1
title: Xanthine
---
# Xanthine

## Identity

Xanthine is the canonical name used here for an enrichment compound in the ENIGMA Carbon Census. [^enigma_carbon_census_1]

- **Known aliases:** None specified in the source report. [^enigma_carbon_census_1]
- **Stable external identifier:** None specified in the source report; the compound was structure-resolved through [pubchem](pubchem.md). [^enigma_carbon_census_1]

## Evidence from the ENIGMA Carbon Census

Xanthine was one of the 8 compounds with an ENIGMA-isolate utilizer call. [^enigma_carbon_census_1]

The census recorded 13 xanthine utilizer strains among the 569 ENIGMA-isolate utilizer prediction rows. [^enigma_carbon_census_1]

Xanthine was initially included among the 9 callable compounds, but its call was mis-scored as carbon-catabolic because allowlisted reaction R02107, xanthine→urate, represents purine nitrogen acquisition rather than carbon catabolism. [^enigma_carbon_census_1]

After removing R02107 from the carbon allowlist, the effective carbon-callable set was 8 compounds rather than 9, although committed tables still contained xanthine because they had not been regenerated. [^enigma_carbon_census_1]

This classification issue makes xanthine a data-quality example for [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) and [multi-omics-integration](../concepts/multi-omics-integration.md), where reaction direction and evidence tier must be distinguished from a generic pathway annotation. [^enigma_carbon_census_1]

## Related resources

The xanthine call was derived within a cross-resource workflow involving compound identity, reaction annotations, genome data, and ENIGMA-isolate predictions, linking it to [kegg](kegg.md), [kescience-fitnessbrowser](kescience-fitnessbrowser.md), [kbase-msd-biochemistry](kbase-msd-biochemistry.md), and [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md). [^enigma_carbon_census_1]

The complete project context is summarized in [enigma_carbon_census_1__REPORT](../summaries/enigma_carbon_census_1__REPORT.md). [^enigma_carbon_census_1]

[^enigma_carbon_census_1]: [enigma carbon census 1](../summaries/enigma_carbon_census_1__REPORT.md)
