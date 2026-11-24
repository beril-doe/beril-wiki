---
type: "Research direction"
description: "Do communities lose amino acid biosynthesis capacity where the amino acid is freely available, or does the negative link between completeness and ambient amino acid reflect something else, such as consumption of the amino acid?"
hypothesis: "If Black Queen gene loss drives the pattern, the negative link between pathway completeness and ambient amino acid should hold across independent studies and sit mainly in costly pathways. If consumption drives it, the link should vanish once community uptake capacity is accounted for."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The catalog shows NMDC metabolomics, taxonomy and GapMind tables, but the genus-to-pathway bridge and the per-study splits still have to be computed."
databases: ["kbase.ke_pangenome", "kbase.nmdc_arkin"]
tables: ["kbase.nmdc_arkin.metabolomics_gold", "kbase.nmdc_arkin.centrifuge_gold", "kbase.nmdc_arkin.study_table", "kbase.ke_pangenome.gapmind_pathways", "kbase.ke_pangenome.gtdb_taxonomy_r214v1"]
findings: ["nmdc_community_metabolic_ecology--33da3819", "nmdc_community_metabolic_ecology--821653f8", "nmdc_community_metabolic_ecology--ddb1a444", "nmdc_community_metabolic_ecology--55f1c6f8"]
conflicts: []
papers: ["35085485", "31316056", "33311510", "24910088"]
builds_on: ["findings/nmdc_community_metabolic_ecology--33da3819", "findings/nmdc_community_metabolic_ecology--821653f8", "findings/nmdc_community_metabolic_ecology--ddb1a444", "findings/nmdc_community_metabolic_ecology--55f1c6f8"]
projects: ["nmdc_community_metabolic_ecology"]
topics: ["metabolic-traits-auxotrophy-and-community-dependence"]
---
# Does community amino acid biosynthesis completeness fall where ambient amino acids are abundant, as Black Queen dynamics predict?

Do communities lose amino acid biosynthesis capacity where the amino acid is freely available, or does the negative link between completeness and ambient amino acid reflect something else, such as consumption of the amino acid?

## Hypothesis

If Black Queen gene loss drives the pattern, the negative link between pathway completeness and ambient amino acid should hold across independent studies and sit mainly in costly pathways. If consumption drives it, the link should vanish once community uptake capacity is accounted for.

## Why it matters

A community-level signature of gene loss from public goods would show that auxotrophy is shaped by the local chemical environment, not only by lineage. That would change how cross-feeding dependence is predicted from metagenomes.

## How to test it

Using NMDC paired taxonomy and metabolomics, score leucine, arginine and the other testable amino acid pathways from genus-level GapMind completeness in the pangenome. Regress completeness on ambient intensity separately in each NMDC study, adding a covariate for the community's amino acid uptake or catabolism genes. Compare pathways by biosynthetic cost. Add a held-out study not used for the first signal.

## What would support or refute it

Support: negative slopes in most studies, and they persist after the uptake covariate. Refute: slopes that are near zero or that change sign across studies, or that vanish after the uptake covariate. The current signal comes almost entirely from one soil study, so failure to replicate is a real possibility.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The catalog shows NMDC metabolomics, taxonomy and GapMind tables, but the genus-to-pathway bridge and the per-study splits still have to be computed.

## Builds on

- Finding: [[findings/nmdc_community_metabolic_ecology--33da3819|Leucine completeness negatively tracks ambient leucine after FDR correction]] (Candidate novel)
- Finding: [[findings/nmdc_community_metabolic_ecology--821653f8|Arginine completeness negatively tracks ambient arginine after FDR correction]] (Candidate novel)
- Finding: [[findings/nmdc_community_metabolic_ecology--ddb1a444|Most amino acid pathways show negative completeness-metabolite correlations, as Black Queen predicts]] (Candidate novel)
- Finding: [[findings/nmdc_community_metabolic_ecology--55f1c6f8|Arginine signal loses FDR significance in Soil-only test]] (Insufficient literature evidence)

## Closest published work

- [PMID 35085485](https://pubmed.ncbi.nlm.nih.gov/35085485/) Genomic structure predicts metabolite dynamics in microbial communities.
- [PMID 31316056](https://pubmed.ncbi.nlm.nih.gov/31316056/) Predictive metabolomic profiling of microbial communities using amplicon or metagenomic sequences.
- [PMID 33311510](https://pubmed.ncbi.nlm.nih.gov/33311510/) Using metacommunity ecology to understand environmental metabolomes.
- [PMID 24910088](https://pubmed.ncbi.nlm.nih.gov/24910088/) Less is more: selective advantages can explain the prevalent loss of biosynthetic genes in bacteria.

The papers (35085485, 31316056, 33311510) link communities to metabolites by prediction or ecological modelling, and 24910088 argues for selective loss of biosynthetic genes. None tests a Black Queen pattern against measured ambient amino acids across studies.
