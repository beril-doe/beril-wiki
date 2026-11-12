---
type: "Research direction"
description: "Carbon-utilization pathway completeness separates soil from freshwater communities along the main axis of variation, with amino acid pathways secondary. Is that axis driven by plant-derived carbon input rather than by the habitat label itself?"
hypothesis: "Freshwater samples with high plant-derived organic carbon signals show carbon-pathway completeness like soil, while soil samples with little plant signal look like typical freshwater."
approach: "lakehouse analysis"
readiness: "unknown"
readiness_basis: "The needed tables are in the catalog, but the overlap of samples with both metabolomics and taxonomy, especially for freshwater, and the sample-level environment fields were not shown."
databases: ["kbase.ke_pangenome", "kbase.nmdc_arkin", "nmdc.metadata"]
tables: ["kbase.nmdc_arkin.centrifuge_gold", "kbase.nmdc_arkin.metabolomics_gold", "kbase.nmdc_arkin.omics_files_table", "kbase.nmdc_arkin.study_table", "kbase.nmdc_arkin.taxonomy_dim", "nmdc.metadata.biosample_set", "kbase.ke_pangenome.gapmind_pathways", "kbase.ke_pangenome.gtdb_taxonomy_r214v1"]
findings: ["nmdc_community_metabolic_ecology--fb740bf4"]
conflicts: ["conflict--community-metabolic-interdependence--e7db3c77"]
papers: ["35085485", "31316056", "33311510"]
builds_on: ["findings/nmdc_community_metabolic_ecology--fb740bf4", "conflicts/conflict--community-metabolic-interdependence--e7db3c77"]
projects: ["nmdc_community_metabolic_ecology"]
topics: ["metabolic-traits-auxotrophy-and-community-dependence"]
---
# Does plant-derived carbon input, not ecosystem label, set community carbon-pathway completeness?

Carbon-utilization pathway completeness separates soil from freshwater communities along the main axis of variation, with amino acid pathways secondary. Is that axis driven by plant-derived carbon input rather than by the habitat label itself?

## Hypothesis

Freshwater samples with high plant-derived organic carbon signals show carbon-pathway completeness like soil, while soil samples with little plant signal look like typical freshwater.

## Why it matters

It would show that community metabolic configuration follows substrate supply, which would also sharpen the Black Queen amino-acid tests that currently confound habitat and carbon supply. The original axis is consistent with habitat physicochemistry but does not demonstrate it.

## How to test it

Estimate community pathway completeness by mapping genus-level taxonomic profiles to per-genome pathway calls through the genome taxonomy table. Relate it to plant-derived compound signals in the metabolomics data, comparing within each ecosystem label from study and sample metadata. Join metabolomics and taxonomy through the file-to-sample bridge. Freshwater samples may lack metabolomics, so start with samples that have both and flag the gap. Land-cover or vegetation layers were not located for these samples in the catalog.

## What would support or refute it

Support: completeness tracks plant-carbon indicators within each ecosystem label. Refutation: the soil–freshwater separation persists unchanged among samples matched on plant-carbon indicators.

## Data

Approach: lakehouse analysis. Readiness: unknown. The needed tables are in the catalog, but the overlap of samples with both metabolomics and taxonomy, especially for freshwater, and the sample-level environment fields were not shown.

## Builds on

- Finding: [[findings/nmdc_community_metabolic_ecology--fb740bf4|Carbon-utilization pathways dominate the soil–freshwater separation axis, with amino acids secondary]] (Candidate novel)
- Conflict: [[conflicts/conflict--community-metabolic-interdependence--e7db3c77|Does Community Provisioning Produce a Common Negative Amino-Acid Pattern, or Does Tyrosine Follow a Different Regime?]]

## Closest published work

- [PMID 35085485](https://pubmed.ncbi.nlm.nih.gov/35085485/) Genomic structure predicts metabolite dynamics in microbial communities.
- [PMID 31316056](https://pubmed.ncbi.nlm.nih.gov/31316056/) Predictive metabolomic profiling of microbial communities using amplicon or metagenomic sequences.
- [PMID 33311510](https://pubmed.ncbi.nlm.nih.gov/33311510/) Using metacommunity ecology to understand environmental metabolomes.

PMID 35085485 and PMID 31316056 link community gene content to metabolites, and PMID 33311510 addresses environmental metabolomes; none tests whether plant-carbon supply explains habitat differences in pathway completeness.
