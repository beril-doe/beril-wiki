---
type: "Research direction"
description: "Does the lower number of detected metabolites in heated mineral soil reflect depleted metabolite pools, or detection limits?"
hypothesis: "Quantitative metabolomics will show lower abundance of labile compounds in heated mineral soil. This fits depleted substrate and the methanotrophy and glyoxylate RNA signals."
approach: "lakehouse analysis"
readiness: "data in the lakehouse"
readiness_basis: "The source says quantitative metabolomics layers exist in the lakehouse; the original project excluded them."
databases: ["kbase.nmdc_arkin"]
tables: ["kbase.nmdc_arkin.metabolomics_gold", "kbase.nmdc_arkin.omics_files_table", "kbase.nmdc_arkin.study_table"]
findings: ["harvard_forest_warming--228419b2", "harvard_forest_warming--5e3df52e"]
conflicts: []
papers: ["36448874", "28983050", "34512564", "27590813"]
builds_on: ["findings/harvard_forest_warming--228419b2", "findings/harvard_forest_warming--5e3df52e"]
projects: ["harvard_forest_warming"]
topics: ["subsurface-and-soil-community-ecology"]
---
# Does fewer detectable metabolites in heated Harvard Forest mineral soil reflect real depletion?

Does the lower number of detected metabolites in heated mineral soil reflect depleted metabolite pools, or detection limits?

## Hypothesis

Quantitative metabolomics will show lower abundance of labile compounds in heated mineral soil. This fits depleted substrate and the methanotrophy and glyoxylate RNA signals.

## Why it matters

It would link substrate depletion, the leading explanation for warming responses, to measured chemistry in this soil. It would also say whether the unusual RNA signals have a chemical basis.

## How to test it

Use the quantitative metabolomics layer for Harvard Forest samples, with the omics file tables to find samples. Compare compound abundances between heated and control mineral soil, not only detection counts. Examine whether detected compound classes match the methanotrophy and glyoxylate-cycle signals. Treat the RNA signals as a small pre-specified set.

## What would support or refute it

Support: abundance falls for labile compound classes in heated soil, beyond detection counts. Refute: abundances are equal and only detection counts differ, pointing to detection limits.

## Data

Approach: lakehouse analysis. Readiness: data in the lakehouse. The source says quantitative metabolomics layers exist in the lakehouse; the original project excluded them.

## Builds on

- Finding: [[findings/harvard_forest_warming--228419b2|Heated mineral soil has fewer detectable metabolites]] (Candidate novel)
- Finding: [[findings/harvard_forest_warming--5e3df52e|Methanotrophy and glyoxylate genes, not CAZymes, lead RNA warming signals]] (Candidate novel)

## Closest published work

- [PMID 36448874](https://pubmed.ncbi.nlm.nih.gov/36448874/) Substrate availability and not thermal acclimation controls microbial temperature sensitivity response to long-term warming.
- [PMID 28983050](https://pubmed.ncbi.nlm.nih.gov/28983050/) Long-term pattern and magnitude of soil carbon feedback to the climate system in a warming world.
- [PMID 34512564](https://pubmed.ncbi.nlm.nih.gov/34512564/) The Transcriptional Response of Soil Bacteria to Long-Term Warming and Short-Term Seasonal Fluctuations in a Terrestrial Forest.
- [PMID 27590813](https://pubmed.ncbi.nlm.nih.gov/27590813/) Long-Term Warming Alters Carbohydrate Degradation Potential in Temperate Forest Soils.

The warming papers (28983050, 36448874) report reduced carbon availability, and 34512564 reports RNA responses. None measures metabolite detection or abundance in heated mineral soil.
