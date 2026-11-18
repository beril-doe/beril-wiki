---
type: "Research direction"
description: "Heated mineral soil had about 7% fewer detectable metabolites, though no single metabolite clearly differed once the many metabolites tested were taken into account. Are the lost metabolites concentrated in labile compound classes such as sugars, amino acids and organic acids?"
hypothesis: "Across warming studies, metabolites detected in control but not heated mineral soil are overrepresented in labile classes, as expected if warming speeds microbial use of easy substrates."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Metabolite tables with identifiers and names are listed, but the catalog did not show which samples are warming-treatment mineral soil or what share of identifiers resolve to chemical classes."
databases: ["kbase.nmdc_arkin", "nmdc.metadata"]
tables: ["kbase.nmdc_arkin.metabolomics_gold", "nmdc.metadata.workflow_execution_set_has_metabolite_identifications", "nmdc.metadata.biosample_set", "nmdc.metadata.study_set"]
findings: ["harvard_forest_warming--664ecd79"]
conflicts: []
papers: ["36448874", "25762989", "27590813"]
builds_on: ["findings/harvard_forest_warming--664ecd79"]
projects: ["harvard_forest_warming"]
topics: ["subsurface-and-soil-community-ecology"]
---
# Does long-term warming remove labile compound classes from mineral soil metabolomes?

Heated mineral soil had about 7% fewer detectable metabolites, though no single metabolite clearly differed once the many metabolites tested were taken into account. Are the lost metabolites concentrated in labile compound classes such as sugars, amino acids and organic acids?

## Hypothesis

Across warming studies, metabolites detected in control but not heated mineral soil are overrepresented in labile classes, as expected if warming speeds microbial use of easy substrates.

## Why it matters

A consistent class-level pattern would show a substrate-limitation signature of warming that no single-metabolite test could detect, and would bear on whether microbial warming sensitivity is limited by substrate supply.

## How to test it

Resolve chemical identifiers and names in the national metabolomics tables to compound classes, since the Harvard Forest labels were left unresolved. Identify the warming studies and mineral samples through the study and sample tables. Compare the share of lost metabolites in labile classes against all detected metabolites, within each study.

## What would support or refute it

Support: lost metabolites are overrepresented in labile classes in more than one warming study. Refutation: losses are spread evenly across classes or sit in recalcitrant classes. Many identifiers may not resolve to a class, which limits the test.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Metabolite tables with identifiers and names are listed, but the catalog did not show which samples are warming-treatment mineral soil or what share of identifiers resolve to chemical classes.

## Builds on

- Finding: [[findings/harvard_forest_warming--664ecd79|Heated mineral soil has fewer detectable metabolites, none individually significant]] (Candidate novel)

## Closest published work

- [PMID 36448874](https://pubmed.ncbi.nlm.nih.gov/36448874/) Substrate availability and not thermal acclimation controls microbial temperature sensitivity response to long-term warming.
- [PMID 25762989](https://pubmed.ncbi.nlm.nih.gov/25762989/) Long-term forest soil warming alters microbial communities in temperate forest soils.
- [PMID 27590813](https://pubmed.ncbi.nlm.nih.gov/27590813/) Long-Term Warming Alters Carbohydrate Degradation Potential in Temperate Forest Soils.

PMID 36448874 argues that substrate availability controls microbial temperature sensitivity under long-term warming, but it does not profile which compound classes disappear from heated mineral soil.
