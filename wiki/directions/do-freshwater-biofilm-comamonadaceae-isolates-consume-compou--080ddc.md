---
type: "Research direction"
description: "Most census compounds, notably alkaloids and terpenoids, got no isolate utilizer call in the resources queried, though literature beyond that search may exist. Periphyton samples are rich in Comamonadaceae genera. Do isolates of these genera actually degrade such compounds?"
hypothesis: "Across samples within the same study, the signal of compounds with no utilizer call is weaker where Comamonadaceae genera are abundant than where they are scarce. At least some of these compounds are depleted by pure isolates of those genera, and carbon from the compound ends up in their cells."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The metabolomics, taxonomy and file-bridge tables are in the catalog, but compound identifiers must be matched to the census list and the catalog did not show how many samples have both data types; the isolate and isotope tests need new measurements."
databases: ["kbase.nmdc_arkin"]
tables: ["kbase.nmdc_arkin.metabolomics_gold", "kbase.nmdc_arkin.centrifuge_gold", "kbase.nmdc_arkin.omics_files_table", "kbase.nmdc_arkin.study_table", "kbase.nmdc_arkin.taxonomy_dim"]
findings: ["enigma_carbon_census_1--5022536d", "enigma_carbon_census_1--8512f374", "enigma_carbon_census_1--f8b7ca8b"]
conflicts: []
papers: ["34612321", "40960580", "32961457", "36688698", "19457026"]
builds_on: ["findings/enigma_carbon_census_1--5022536d", "findings/enigma_carbon_census_1--8512f374", "findings/enigma_carbon_census_1--f8b7ca8b"]
projects: ["enigma_carbon_census_1"]
topics: ["metabolic-traits-auxotrophy-and-community-dependence"]
---
# Do freshwater-biofilm Comamonadaceae isolates consume compounds that lack a utilizer call?

Most census compounds, notably alkaloids and terpenoids, got no isolate utilizer call in the resources queried, though literature beyond that search may exist. Periphyton samples are rich in Comamonadaceae genera. Do isolates of these genera actually degrade such compounds?

## Hypothesis

Across samples within the same study, the signal of compounds with no utilizer call is weaker where Comamonadaceae genera are abundant than where they are scarce. At least some of these compounds are depleted by pure isolates of those genera, and carbon from the compound ends up in their cells.

## Why it matters

It would turn a map of unknown degraders into a targeted list of organisms and environments to enrich from. A negative result would favour the view that darkness reflects missing annotation or compounds that are truly recalcitrant. The census pattern by chemical class rests on very few callable compounds and is tangled up with annotation coverage, so a direct test is needed.

## How to test it

Step 1 (lakehouse): use the file-to-sample-and-study bridge to join metabolomics and taxonomic profiles to studies and ecosystem labels. Within each study, compare how strongly detectable census compounds are seen in samples rich versus poor in these genera, contrasting compounds with no utilizer call against callable ones. Compounds not detected in the metabolomics data drop out. Step 2 (experiment): grow isolates of Variovorax, Polaromonas, Hydrogenophaga and Rhizobacter individually on a few such compounds and follow compound loss. Confirm incorporation in a periphyton-inoculated enrichment by stable-isotope tracing, so depletion by another community member is ruled out.

## What would support or refute it

Support: within a study, the compound signal drops as these genera become more abundant, isolates deplete the compound, and the isotope label appears in them. Refutation: no within-study relation, or depletion occurs only in mixed enrichments without isolate-level or isotope evidence.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The metabolomics, taxonomy and file-bridge tables are in the catalog, but compound identifiers must be matched to the census list and the catalog did not show how many samples have both data types; the isolate and isotope tests need new measurements.

## Builds on

- Finding: [[findings/enigma_carbon_census_1--5022536d|Most census compounds lack utilizer calls, biased by chemical class]] (Insufficient literature evidence)
- Finding: [[findings/enigma_carbon_census_1--8512f374|Freshwater biofilm samples show high prevalence of Burkholderiales/Comamonadaceae genera]] (Insufficient literature evidence)
- Finding: [[findings/enigma_carbon_census_1--f8b7ca8b|Uniform class coverage of isolate-callable compounds not rejected, by an underpowered test]] (Insufficient literature evidence)

## Closest published work

- [PMID 34612321](https://pubmed.ncbi.nlm.nih.gov/34612321/) Biosynthesis, evolution and ecology of microbial terpenoids.
- [PMID 40960580](https://pubmed.ncbi.nlm.nih.gov/40960580/) Atranone-an underestimated secondary metabolite?
- [PMID 32961457](https://pubmed.ncbi.nlm.nih.gov/32961457/) Microplastic-associated biofilms in lentic Italian ecosystems.
- [PMID 36688698](https://pubmed.ncbi.nlm.nih.gov/36688698/) Glacier-Fed Stream Biofilms Harbor Diverse Resistomes and Biosynthetic Gene Clusters.
- [PMID 19457026](https://pubmed.ncbi.nlm.nih.gov/19457026/) Polaromonas and Hydrogenophaga species are the predominant bacteria cultured from granular activated carbon filters in water treatment.

PMID 32961457, PMID 36688698 and PMID 19457026 show only that related genera occur in freshwater biofilms; none links their abundance to depletion of compounds without a known degrader.
