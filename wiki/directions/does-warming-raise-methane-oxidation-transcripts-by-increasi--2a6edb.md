---
type: "Research direction"
description: "In Harvard Forest warmed soil, do the higher methane monooxygenase (pmoA, pmoB) transcript levels come from existing methanotrophs expressing more, or from more methanotroph cells?"
hypothesis: "The ratio of transcripts to gene copies for methane monooxygenase genes rises under warming while gene abundance stays flat, indicating regulation within existing populations; glyoxylate-cycle transcripts instead trace to the Actinobacteria that rise in warmed organic soil."
approach: "lakehouse analysis"
readiness: "unknown"
readiness_basis: "Annotation, read-classification and genome tables are listed, but the catalog did not show whether gene-level DNA and RNA abundances are paired for the warming samples or available for other warming studies."
databases: ["kbase.nmdc_mags", "nmdc.metadata", "nmdc.results"]
tables: ["nmdc.results.annotation_kegg_orthology", "nmdc.results.kraken2_classification_report", "nmdc.metadata.biosample_set", "kbase.nmdc_mags.mag_catalog"]
findings: ["harvard_forest_warming--4fcaf7c4", "harvard_forest_warming--5dcb42f7", "harvard_forest_warming--d1815e53", "harvard_forest_warming--8f0aae96"]
conflicts: []
papers: ["34512564", "38561130", "25762989", "27590813"]
builds_on: ["findings/harvard_forest_warming--4fcaf7c4", "findings/harvard_forest_warming--5dcb42f7", "findings/harvard_forest_warming--d1815e53", "findings/harvard_forest_warming--8f0aae96"]
projects: ["harvard_forest_warming"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Does warming raise methane-oxidation transcripts by increasing expression rather than methanotroph abundance?

In Harvard Forest warmed soil, do the higher methane monooxygenase (pmoA, pmoB) transcript levels come from existing methanotrophs expressing more, or from more methanotroph cells?

## Hypothesis

The ratio of transcripts to gene copies for methane monooxygenase genes rises under warming while gene abundance stays flat, indicating regulation within existing populations; glyoxylate-cycle transcripts instead trace to the Actinobacteria that rise in warmed organic soil.

## Why it matters

The transcript increases were weak and did not survive correction for testing thousands of gene families at once, so it is unclear whether warming reshapes who is present or what they do. A clear answer would show whether warmed forest soil methane uptake should be modelled from community composition or from regulation.

## How to test it

Using the paired DNA and RNA data for the heated and control organic and mineral samples, compute per-gene transcript-to-DNA ratios for methane monooxygenase and glyoxylate-cycle genes. Assign the genes to taxa through read classification and the assembled genomes from the same site. Then look for the same pattern in other warming or thaw studies in the national microbiome collection (peatland, permafrost). Because the original signals are weak, treat any recurrence as the key evidence.

## What would support or refute it

Support: higher transcript-to-DNA ratio for methane monooxygenase genes under warming with unchanged DNA, glyoxylate transcripts mapping mostly to Actinobacteria, and recurrence at another warming site. Refute: ratios unchanged, increases fully explained by more methanotroph DNA, or no recurrence.

## Data

Approach: lakehouse analysis. Readiness: unknown. Annotation, read-classification and genome tables are listed, but the catalog did not show whether gene-level DNA and RNA abundances are paired for the warming samples or available for other warming studies.

## Builds on

- Finding: [[findings/harvard_forest_warming--4fcaf7c4|Nominal RNA signals: methane oxidation and glyoxylate genes up under warming]] (Candidate novel)
- Finding: [[findings/harvard_forest_warming--5dcb42f7|Organic-horizon Actinobacteria rise and Acidobacteria fall under long-term warming]] (Extends retrieved work)
- Finding: [[findings/harvard_forest_warming--d1815e53|Carbon-cycling genes enriched among warming-increased DNA functions in organic horizon only]] (Extends retrieved work)
- Finding: [[findings/harvard_forest_warming--8f0aae96|No greater warming sensitivity of the transcript pool than the DNA pool]] (Insufficient literature evidence)

## Closest published work

- [PMID 34512564](https://pubmed.ncbi.nlm.nih.gov/34512564/) The Transcriptional Response of Soil Bacteria to Long-Term Warming and Short-Term Seasonal Fluctuations in a Terrestrial Forest.
- [PMID 38561130](https://pubmed.ncbi.nlm.nih.gov/38561130/) Soil warming-induced reduction in water content enhanced methane uptake at different soil depths in a subtropical forest.
- [PMID 25762989](https://pubmed.ncbi.nlm.nih.gov/25762989/) Long-term forest soil warming alters microbial communities in temperate forest soils.
- [PMID 27590813](https://pubmed.ncbi.nlm.nih.gov/27590813/) Long-Term Warming Alters Carbohydrate Degradation Potential in Temperate Forest Soils.

PMID 34512564 profiles warming-responsive RNA at the same site, and PMID 38561130 finds higher methane uptake without a rise in pmoA gene copies; this direction separates expression from abundance for these genes.
