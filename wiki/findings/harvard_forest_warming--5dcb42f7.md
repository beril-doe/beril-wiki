---
type: "Finding"
description: "In 14 control and 14 heated direct samples, organic-horizon Actinobacteria rose from 0.249 to 0.315 (log2 FC +0.341, BH q=0.049) while Acidobacteria fell from 0.035 to 0.024 (log2 FC \u22120.549, BH q=0.049); Cyanobacteria, Proteobacteria and Verrucomicrobia had q=0.072, 0.088 and 0.088."
finding_id: "harvard_forest_warming--5dcb42f7"
result: "observation"
source: "harvard_forest_warming"
quantities: [{"value": "+0.341", "what": "log2 fold change of Actinobacteria relative abundance, heated vs control", "unit": "log2 FC", "denominator": "kraken2 read-based relative abundance", "scope": "organic horizon, 14 control + 14 heated direct samples"}, {"value": "\u22120.549", "what": "log2 fold change of Acidobacteria relative abundance, heated vs control", "unit": "log2 FC", "denominator": "kraken2 read-based relative abundance", "scope": "organic horizon, 14 control + 14 heated direct samples"}, {"value": "0.049", "what": "BH q-value for both the Actinobacteria and Acidobacteria changes", "unit": "", "denominator": "BH-FDR across phyla \u00d7 horizon", "scope": "Welch t-test, organic horizon"}]
caveat: "All samples came from a single timepoint (2017-05-24), so seasonal effects cannot be detected."
first_added: "2026-10-27"
source_hash: "d4043571b26bef25b8a3ca32dbd57a1ba8196ebed694062c96fb769ca1a9e273"
---
# Organic-horizon Actinobacteria rise and Acidobacteria fall under long-term warming

In 14 control and 14 heated direct samples, organic-horizon Actinobacteria rose from 0.249 to 0.315 (log2 FC +0.341, BH q=0.049) while Acidobacteria fell from 0.035 to 0.024 (log2 FC −0.549, BH q=0.049); Cyanobacteria, Proteobacteria and Verrucomicrobia had q=0.072, 0.088 and 0.088. [src: harvard_forest_warming]

## Key figures

- **+0.341 log2 FC**: log2 fold change of Actinobacteria relative abundance, heated vs control (denominator kraken2 read-based relative abundance; scope organic horizon, 14 control + 14 heated direct samples) [src: harvard_forest_warming]
- **−0.549 log2 FC**: log2 fold change of Acidobacteria relative abundance, heated vs control (denominator kraken2 read-based relative abundance; scope organic horizon, 14 control + 14 heated direct samples) [src: harvard_forest_warming]
- **0.049**: BH q-value for both the Actinobacteria and Acidobacteria changes (denominator BH-FDR across phyla × horizon; scope Welch t-test, organic horizon) [src: harvard_forest_warming]

## Evidence

> Per-phylum Welch t-test on kraken2 read-based relative abundance (n=14 control + 14 heated direct samples, BH-FDR across phyla × horizon): | Phylum | Horizon | Control mean | Heated mean | log2 FC | q (BH) | |--------|---------|--------------|-------------|---------|--------| | Actinobacteria | organic | 0.249 | 0.315 | **+0.341** | **0.049** | | Acidobacteria | organic | 0.035 | 0.024 | **−0.549** | **0.049** | | Cyanobacteria | organic | 0.0032 | 0.0026 | −0.305 | 0.072 | | Proteobacteria | organic | 0.654 | 0.605 | −0.111 | 0.088 | | Verrucomicrobia | organic | 0.0058 | 0.0041 | −0.513 | 0.088 | [src: harvard_forest_warming]

From the report [[summaries/harvard_forest_warming__REPORT]].

## Caveat

All samples came from a single timepoint (2017-05-24), so seasonal effects cannot be detected. [src: harvard_forest_warming]

> - **Single timepoint** (2017-05-24). Cannot detect seasonal effects (which Shinfuku et al. 2024 show are substantial at this site). [src: harvard_forest_warming]

## Other caveats in this report

- The analyses used nmdc_metadata and nmdc_results, excluding nmdc_arkin. [src: harvard_forest_warming]
- The paired n=25 analysis appeared to favor DNA (pseudo-F 3.12, R²=11.9%, p=0.020) over RNA (pseudo-F 0.76, R²=3.2%, p=0.60), but organic samples were all incubated and mineral samples all direct, confounding horizon with incubation; H1 was not supported. [src: harvard_forest_warming]
- The report proposes, rather than demonstrates, long-term compositional turnover as a possible reason DNA and RNA warming sensitivities converge after roughly 25 years of heating. [src: harvard_forest_warming]
- The single collection date, 2017-05-24, may leave RNA subject to diurnal and microspatial variation, weakening its signal of chronic +5°C warming. [src: harvard_forest_warming]
- The metatranscriptome recovered 14,302 distinct KOs versus 12,863 in the metagenome; the report proposes that this richer repertoire could dilute treatment signals under relative-abundance analysis. [src: harvard_forest_warming]
