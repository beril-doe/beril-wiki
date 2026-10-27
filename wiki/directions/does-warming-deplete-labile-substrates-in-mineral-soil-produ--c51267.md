---
type: "Research direction"
description: "Is the roughly 7% lower count of detectable metabolites in heated mineral soil concentrated in labile compound classes, as expected if warming accelerates substrate depletion?"
hypothesis: "Metabolites lost in heated mineral soil are enriched for labile compound classes (sugars, organic acids, amino acids) relative to recalcitrant ones, even though no single metabolite passes FDR."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Class-level analysis can use existing detections once labels are resolved, but the decisive targeted quantification requires new measurements."
collections: []
findings: ["harvard_forest_warming--664ecd79", "harvard_forest_warming--8f0aae96"]
conflicts: []
papers: ["36448874", "34512564", "27590813"]
builds_on: ["findings/harvard_forest_warming--664ecd79", "findings/harvard_forest_warming--8f0aae96"]
projects: ["harvard_forest_warming"]
topics: ["subsurface-and-soil-community-ecology"]
---
# Does warming deplete labile substrates in mineral soil, producing fewer detectable metabolites?

Is the roughly 7% lower count of detectable metabolites in heated mineral soil concentrated in labile compound classes, as expected if warming accelerates substrate depletion?

## Hypothesis

Metabolites lost in heated mineral soil are enriched for labile compound classes (sugars, organic acids, amino acids) relative to recalcitrant ones, even though no single metabolite passes FDR.

## Why it matters

It would give a mechanism, consistent with the substrate-availability argument in the closest published work, for declining respiration responses under long-term warming, and show how a class-level signal can exist below per-metabolite significance.

## How to test it

Resolve ChEBI labels for Harvard Forest mineral metabolites (left unresolved in the project), assign compound classes, and test class-level enrichment among metabolites lost in heated samples with a permutation test across the full detected set. Mineral samples were all direct and organic all incubated, so keep the analysis within the mineral horizon. Then quantify labile sugars and organic acids in heated versus control mineral soil with a direct (non-incubated) design.

## What would support or refute it

Support: labile classes are significantly over-represented among lost metabolites and targeted quantification shows lower concentrations. Refutation: losses are spread evenly across classes, or the targeted assays show no difference.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Class-level analysis can use existing detections once labels are resolved, but the decisive targeted quantification requires new measurements.

## Builds on

- Finding: [[findings/harvard_forest_warming--664ecd79|Heated mineral soil has fewer detectable metabolites, none individually significant]] (Candidate novel)
- Finding: [[findings/harvard_forest_warming--8f0aae96|No greater warming sensitivity of the transcript pool than the DNA pool]] (Insufficient literature evidence)

## Closest published work

- [PMID 36448874](https://pubmed.ncbi.nlm.nih.gov/36448874/) Substrate availability and not thermal acclimation controls microbial temperature sensitivity response to long-term warming.
- [PMID 34512564](https://pubmed.ncbi.nlm.nih.gov/34512564/) The Transcriptional Response of Soil Bacteria to Long-Term Warming and Short-Term Seasonal Fluctuations in a Terrestrial Forest.
- [PMID 27590813](https://pubmed.ncbi.nlm.nih.gov/27590813/) Long-Term Warming Alters Carbohydrate Degradation Potential in Temperate Forest Soils.

PMID 36448874 attributes warming temperature sensitivity to substrate availability, but no retrieved paper reports a metabolite-class profile of heated mineral soil (PMIDs 34512564 and 27590813 address genes and transcripts).
