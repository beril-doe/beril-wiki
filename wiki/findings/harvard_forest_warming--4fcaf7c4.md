---
type: "Finding"
description: "Nominal RNA signals include pmoA K10944 in organic (+0.730, p=0.009) and mineral (+0.743, p=0.029), pmoB K10945 in organic (+0.669, p=0.012) and mineral (+0.880, p=0.054), and mineral aceA/icl K01637 (+0.460, p=0.037) and aceB/glcB K01638 (+0.268, p=0.037)."
finding_id: "harvard_forest_warming--4fcaf7c4"
result: "observation"
source: "harvard_forest_warming"
quantities: [{"value": "+0.730", "what": "log2 FC of pmoA (K10944)", "unit": "log2 FC", "denominator": "", "scope": "RNA pool, organic horizon, p=0.009"}, {"value": "+0.743", "what": "log2 FC of pmoA (K10944)", "unit": "log2 FC", "denominator": "", "scope": "RNA pool, mineral horizon, p=0.029"}, {"value": "+0.460", "what": "log2 FC of aceA/icl (K01637)", "unit": "log2 FC", "denominator": "", "scope": "RNA pool, mineral horizon, p=0.037"}]
caveat: "The carbon-cycling RNA-pool p-values are nominal and do not survive FDR across 14K KOs."
first_added: "2026-10-27"
source_hash: "d4043571b26bef25b8a3ca32dbd57a1ba8196ebed694062c96fb769ca1a9e273"
---
# Nominal RNA signals: methane oxidation and glyoxylate genes up under warming

Nominal RNA signals include pmoA K10944 in organic (+0.730, p=0.009) and mineral (+0.743, p=0.029), pmoB K10945 in organic (+0.669, p=0.012) and mineral (+0.880, p=0.054), and mineral aceA/icl K01637 (+0.460, p=0.037) and aceB/glcB K01638 (+0.268, p=0.037). [src: harvard_forest_warming]

## Key figures

- **+0.730 log2 FC**: log2 FC of pmoA (K10944) (scope RNA pool, organic horizon, p=0.009) [src: harvard_forest_warming]
- **+0.743 log2 FC**: log2 FC of pmoA (K10944) (scope RNA pool, mineral horizon, p=0.029) [src: harvard_forest_warming]
- **+0.460 log2 FC**: log2 FC of aceA/icl (K01637) (scope RNA pool, mineral horizon, p=0.037) [src: harvard_forest_warming]

## Evidence

> | KO | Gene | Function | Horizon | log2 FC | p | |----|------|----------|---------|---------|---| | K10944 | pmoA | particulate methane monooxygenase α | organic | +0.730 | 0.009 | | K10945 | pmoB | particulate methane monooxygenase β | organic | +0.669 | 0.012 | | K10944 | pmoA | particulate methane monooxygenase α | mineral | +0.743 | 0.029 | | K10945 | pmoB | particulate methane monooxygenase β | mineral | +0.880 | 0.054 | | K01637 | aceA / icl | isocitrate lyase (glyoxylate cycle) | mineral | +0.460 | 0.037 | | K01638 | aceB / glcB | malate synthase (glyoxylate cycle) | mineral | +0.268 | 0.037 | | K01183 | chiA | chitinase | organic | +0.236 | 0.074 | | K00382 | lpdA | dihydrolipoyl dehydrogenase (TCA/PDH) | organic | −0.161 | 0.021 | [src: harvard_forest_warming]

From the report [[summaries/harvard_forest_warming__REPORT]].

## Caveat

The carbon-cycling RNA-pool p-values are nominal and do not survive FDR across 14K KOs. [src: harvard_forest_warming]

> Specific carbon-cycling RNA-pool signals (nominal p, do not survive FDR across 14K KOs): [src: harvard_forest_warming]

## Other caveats in this report

- The analyses used nmdc_metadata and nmdc_results, excluding nmdc_arkin. [src: harvard_forest_warming]
- The paired n=25 analysis appeared to favor DNA (pseudo-F 3.12, R²=11.9%, p=0.020) over RNA (pseudo-F 0.76, R²=3.2%, p=0.60), but organic samples were all incubated and mineral samples all direct, confounding horizon with incubation; H1 was not supported. [src: harvard_forest_warming]
- The report proposes, rather than demonstrates, long-term compositional turnover as a possible reason DNA and RNA warming sensitivities converge after roughly 25 years of heating. [src: harvard_forest_warming]
- The single collection date, 2017-05-24, may leave RNA subject to diurnal and microspatial variation, weakening its signal of chronic +5°C warming. [src: harvard_forest_warming]
- The metatranscriptome recovered 14,302 distinct KOs versus 12,863 in the metagenome; the report proposes that this richer repertoire could dilute treatment signals under relative-abundance analysis. [src: harvard_forest_warming]
