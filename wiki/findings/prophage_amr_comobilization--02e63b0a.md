---
type: "Finding"
description: "Across 4,770 species, species with higher prophage marker density carry significantly broader AMR gene repertoires (Spearman rho=0.572, p<10^-300), and the association remains after controlling for genome count (partial Spearman rho=0.464, p=1.0\u00d710^-253)."
finding_id: "prophage_amr_comobilization--02e63b0a"
result: "observation"
source: "prophage_amr_comobilization"
quantities: [{"value": "0.572", "what": "Spearman rho between prophage marker density and AMR repertoire breadth", "unit": "", "denominator": "4,770 species", "scope": "n=4,770 species"}, {"value": "0.823", "what": "log-log regression slope of AMR breadth on prophage density (R\u00b2=0.30)", "unit": "", "denominator": "4,770 species", "scope": "4,770 species"}, {"value": "0.464", "what": "partial Spearman rho after controlling for genome count", "unit": "", "denominator": "4,770 species", "scope": "4,770 species"}]
caveat: "The H2 association does not prove phage-mediated AMR transfer; species with open pangenomes may independently accumulate both prophages and AMR genes."
first_added: "2026-10-27"
source_hash: "f58710893c456806b9a06f5e9bd3687468082c34ffcf93be308e037eb59268b5"
---
# Prophage density predicts AMR repertoire breadth across species

Across 4,770 species, species with higher prophage marker density carry significantly broader AMR gene repertoires (Spearman rho=0.572, p<10^-300), and the association remains after controlling for genome count (partial Spearman rho=0.464, p=1.0×10^-253). [src: prophage_amr_comobilization]

## Key figures

- **0.572**: Spearman rho between prophage marker density and AMR repertoire breadth (denominator 4,770 species; scope n=4,770 species) [src: prophage_amr_comobilization]
- **0.823**: log-log regression slope of AMR breadth on prophage density (R²=0.30) (denominator 4,770 species; scope 4,770 species) [src: prophage_amr_comobilization]
- **0.464**: partial Spearman rho after controlling for genome count (denominator 4,770 species; scope 4,770 species) [src: prophage_amr_comobilization]

## Evidence

> Species with higher prophage marker density carry significantly broader AMR gene repertoires (Spearman rho=0.572, p<10^-300, n=4,770 species). A log-log regression reveals that a 10-fold increase in prophage density predicts a ~6.6-fold increase in AMR breadth (slope=0.823, R²=0.30). The association is robust after controlling for genome count (partial Spearman rho=0.464, p=1.0×10^-253). [src: prophage_amr_comobilization]

From the report [[summaries/prophage_amr_comobilization__REPORT]].

## Caveat

The H2 association does not prove phage-mediated AMR transfer; species with open pangenomes may independently accumulate both prophages and AMR genes. [src: prophage_amr_comobilization]

> - **Correlation vs causation**: The H2 association does not prove phage-mediated AMR transfer; species with open pangenomes may independently accumulate both prophages and AMR genes. [src: prophage_amr_comobilization]

## Other caveats in this report

- The proximity–accessory association depends on the distance threshold and is heterogeneous across species: only 33 of 74 testable species had OR>1. [src: prophage_amr_comobilization]
- The fitness dataset covered only 48 model organisms with RB-TnSeq data and poorly overlapped the analyzed GTDB species. [src: prophage_amr_comobilization]
- The species-level association is consistent with two non-exclusive explanations—direct prophage transduction and shared gene-acquisition propensity—but does not distinguish them. [src: prophage_amr_comobilization]
- H1's aggregate difference was 2.1 percentage points and varied among species. Proposed explanations for the near-range reversal and broad-range strengthening are interpretations, not demonstrated mechanisms. [src: prophage_amr_comobilization]
- Reported gene distances are ordinal positions parsed from gene identifiers, not base-pair distances. [src: prophage_amr_comobilization]
