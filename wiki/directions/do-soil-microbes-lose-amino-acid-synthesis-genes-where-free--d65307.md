---
type: "Research direction"
description: "In soil communities, is the lower leucine and arginine synthesis capacity seen where those amino acids are abundant caused by gene loss driven by free amino acids, or by some other factor such as which community members are present?"
hypothesis: "Adding free leucine or arginine to soil lowers the community's synthesis gene content for that amino acid over time, relative to unamended and glucose-amended soil. The natural-sample association is a single-study correlation and should be read as a lead only."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Metabolite intensities, sample-to-study links, community taxonomy and genome pathway scores are in the catalog, but the taxonomy-to-genome mapping and per-sample completeness must be computed; the catalog did not show how many studies have paired data, and the amendment needs new measurements."
databases: ["kbase.ke_pangenome", "kbase.nmdc_arkin"]
tables: ["kbase.nmdc_arkin.metabolomics_gold", "kbase.nmdc_arkin.study_table", "kbase.nmdc_arkin.omics_files_table", "kbase.nmdc_arkin.centrifuge_gold", "kbase.ke_pangenome.gapmind_pathways", "kbase.ke_pangenome.genome", "kbase.ke_pangenome.gtdb_metadata"]
findings: ["nmdc_community_metabolic_ecology--dcef6254", "nmdc_community_metabolic_ecology--7d46eb90", "nmdc_community_metabolic_ecology--6853a137"]
conflicts: ["conflict--metabolic-model-gapfilling--cf98e361"]
papers: ["37322284", "35592760", "31316056", "35085485"]
builds_on: ["findings/nmdc_community_metabolic_ecology--dcef6254", "findings/nmdc_community_metabolic_ecology--7d46eb90", "findings/nmdc_community_metabolic_ecology--6853a137", "conflicts/conflict--metabolic-model-gapfilling--cf98e361"]
projects: ["enigma_carbon_census_1", "nmdc_community_metabolic_ecology"]
topics: ["metabolic-models-and-pathway-level-evidence"]
---
# Do soil microbes lose amino-acid synthesis genes where free amino acids are plentiful?

In soil communities, is the lower leucine and arginine synthesis capacity seen where those amino acids are abundant caused by gene loss driven by free amino acids, or by some other factor such as which community members are present?

## Hypothesis

Adding free leucine or arginine to soil lowers the community's synthesis gene content for that amino acid over time, relative to unamended and glucose-amended soil. The natural-sample association is a single-study correlation and should be read as a lead only.

## Why it matters

A cause-and-effect link would show that dependence on shared metabolites arises inside natural communities, not only in two-species cultures. The present evidence is a correlation in which nearly all samples, and all leucine samples, come from one soil study, so it cannot say which variable moves first or whether it holds elsewhere.

## How to test it

Step 1 (lakehouse): in the soil samples with untargeted metabolite data, estimate each community's synthesis completeness for leucine and arginine by combining its taxonomic profile with genome-level pathway scores for the matched species. Relate this to the measured amino acid signal within the dominant study, and look for any other study with paired metabolite and sequence data to see whether the direction repeats. Use tyrosine, which showed an opposite weak association, and isoleucine, which showed none, as pathways where no negative association is expected. Step 2 (experiment): add leucine or arginine to soil microcosms and follow synthesis gene content by shotgun sequencing, against unamended and glucose-amended controls.

## What would support or refute it

Support: amino acid amendment lowers synthesis gene content for the added amino acid relative to both controls, and the negative association also appears in at least one further study. Refute: amendment changes nothing, or the association vanishes when taxonomic composition is accounted for.

## Data

Approach: analysis then experiment. Readiness: needs compute. Metabolite intensities, sample-to-study links, community taxonomy and genome pathway scores are in the catalog, but the taxonomy-to-genome mapping and per-sample completeness must be computed; the catalog did not show how many studies have paired data, and the amendment needs new measurements.

## Builds on

- Finding: [[findings/nmdc_community_metabolic_ecology--dcef6254|Most amino-acid pathways show negative completeness–metabolite correlations, as Black Queen predicts]] (Candidate novel)
- Finding: [[findings/nmdc_community_metabolic_ecology--7d46eb90|Leucine signal survives soil-only stratification; arginine loses FDR significance]] (Insufficient literature evidence)
- Finding: [[findings/nmdc_community_metabolic_ecology--6853a137|Tyrosine and isoleucine show no Black Queen signal]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--metabolic-model-gapfilling--cf98e361|Community-Scale Signals Versus Flux-Level Inference in NMDC-Based Metabolic Ecology]]

## Closest published work

- [PMID 37322284](https://pubmed.ncbi.nlm.nih.gov/37322284/) Bacteriophage-mediated lysis supports robust growth of amino acid auxotrophs.
- [PMID 35592760](https://pubmed.ncbi.nlm.nih.gov/35592760/) Dynamic proteome allocation regulates the profile of interaction of auxotrophic bacterial consortia.
- [PMID 31316056](https://pubmed.ncbi.nlm.nih.gov/31316056/) Predictive metabolomic profiling of microbial communities using amplicon or metagenomic sequences.
- [PMID 35085485](https://pubmed.ncbi.nlm.nih.gov/35085485/) Genomic structure predicts metabolite dynamics in microbial communities.

PMID 37322284 and PMID 35592760 study provisioning and cross-feeding of amino acid auxotrophs in cultures, and PMID 31316056 and PMID 35085485 predict metabolites from community sequences. None tests, in natural samples or in an amendment, whether free amino acids drive loss of synthesis genes.
