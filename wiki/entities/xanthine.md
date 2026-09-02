---
type: "Compound"
description: "Xanthine, an enrichment compound misclassified as carbon-catabolic"
sources: ["summaries/enigma_carbon_census_1__REPORT.md"]
---
# Xanthine

## Identity

Xanthine is the canonical name used here for an enrichment compound in the ENIGMA Carbon Census. [src: enigma_carbon_census_1]

- **Known aliases:** None specified in the source report. [src: enigma_carbon_census_1]
- **Stable external identifier:** None specified in the source report; the compound was structure-resolved through [[entities/pubchem]]. [src: enigma_carbon_census_1]

## Evidence from the ENIGMA Carbon Census

Xanthine was one of the 8 compounds with an ENIGMA-isolate utilizer call. [src: enigma_carbon_census_1]

The census recorded 13 xanthine utilizer strains among the 569 ENIGMA-isolate utilizer prediction rows. [src: enigma_carbon_census_1]

Xanthine was initially included among the 9 callable compounds, but its call was mis-scored as carbon-catabolic because allowlisted reaction R02107, xanthine→urate, represents purine nitrogen acquisition rather than carbon catabolism. [src: enigma_carbon_census_1]

After removing R02107 from the carbon allowlist, the effective carbon-callable set was 8 compounds rather than 9, although committed tables still contained xanthine because they had not been regenerated. [src: enigma_carbon_census_1]

This classification issue makes xanthine a data-quality example for [[concepts/metabolic-model-gapfilling]] and [[concepts/multi-omics-integration]], where reaction direction and evidence tier must be distinguished from a generic pathway annotation. [src: enigma_carbon_census_1]

## Related resources

The xanthine call was derived within a cross-resource workflow involving compound identity, reaction annotations, genome data, and ENIGMA-isolate predictions, linking it to [[entities/kegg]], [[entities/kescience-fitnessbrowser]], [[entities/kbase-msd-biochemistry]], and [[concepts/cross-tenant-data-bridging]]. [src: enigma_carbon_census_1]

The complete project context is summarized in [[summaries/enigma_carbon_census_1__REPORT]]. [src: enigma_carbon_census_1]
