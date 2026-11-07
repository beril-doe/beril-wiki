---
type: "Research direction"
description: "Does the tendency for soil communities with less complete leucine and arginine synthesis pathways to sit in samples with more free leucine and arginine reflect cheaper uptake by auxotrophs (organisms that cannot make an amino acid)? Or does it only reflect a shared pool of amino acids released by cell breakdown?"
hypothesis: "If the Black Queen mechanism (loss of genes for a leaked public good) is at work, each amino acid's free level should relate to its own pathway independently. If the pattern comes from a shared pool, free levels of different amino acids will rise together and the link to pathway completeness will vanish once total free amino acids are accounted for."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Pathway completeness and metabolite intensities are already joined for the cohort, but pH, temperature and other abiotic covariates were empty and nearly all samples came from one study."
collections: ["nmdc-arkin"]
findings: ["nmdc_community_metabolic_ecology--dcef6254", "nmdc_community_metabolic_ecology--7d46eb90"]
conflicts: []
papers: ["37322284", "35592760", "31316056", "35085485", "33311510"]
builds_on: ["findings/nmdc_community_metabolic_ecology--dcef6254", "findings/nmdc_community_metabolic_ecology--7d46eb90"]
projects: ["nmdc_community_metabolic_ecology"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Do communities short on amino-acid synthesis live where free amino acids are abundant?

Does the tendency for soil communities with less complete leucine and arginine synthesis pathways to sit in samples with more free leucine and arginine reflect cheaper uptake by auxotrophs (organisms that cannot make an amino acid)? Or does it only reflect a shared pool of amino acids released by cell breakdown?

## Hypothesis

If the Black Queen mechanism (loss of genes for a leaked public good) is at work, each amino acid's free level should relate to its own pathway independently. If the pattern comes from a shared pool, free levels of different amino acids will rise together and the link to pathway completeness will vanish once total free amino acids are accounted for.

## Why it matters

It would show whether gene loss in natural communities is actually shaped by dependence on a leaked public good, or whether this is a misreading of sample-wide chemistry. This would change how community amino-acid exchange is modelled.

## How to test it

Using the NMDC Multi-omics collection, take the 13 testable amino acid pathways, 11 of which showed the negative trend, with leucine and arginine strongest and almost all samples from one soil study. Compute, per sample, the total free amino acid pool. Test whether pathway completeness still tracks free leucine or arginine after removing the shared pool, and whether the other nine pathways with the negative trend follow the same pattern. Then run a soil microcosm experiment with leucine added versus not added, and follow the leucine-synthesis-capable fraction of the community by metagenomics over several weeks.

## What would support or refute it

Support: the leucine and arginine link survives removal of the shared pool, and added leucine shifts the community toward fewer synthesis-capable members. Refutation: the link disappears once the shared pool is accounted for, or the amended community does not change.

## Data

Approach: analysis then experiment. Readiness: needs compute. Pathway completeness and metabolite intensities are already joined for the cohort, but pH, temperature and other abiotic covariates were empty and nearly all samples came from one study.

- Collection: [[data/nmdc-arkin|NMDC Multi-omics]]

## Builds on

- Finding: [[findings/nmdc_community_metabolic_ecology--dcef6254|Most amino-acid pathways show negative completeness–metabolite correlations, as Black Queen predicts]] (Candidate novel)
- Finding: [[findings/nmdc_community_metabolic_ecology--7d46eb90|Leucine signal survives soil-only stratification; arginine loses FDR significance]] (Insufficient literature evidence)

## Closest published work

- [PMID 37322284](https://pubmed.ncbi.nlm.nih.gov/37322284/) Bacteriophage-mediated lysis supports robust growth of amino acid auxotrophs.
- [PMID 35592760](https://pubmed.ncbi.nlm.nih.gov/35592760/) Dynamic proteome allocation regulates the profile of interaction of auxotrophic bacterial consortia.
- [PMID 31316056](https://pubmed.ncbi.nlm.nih.gov/31316056/) Predictive metabolomic profiling of microbial communities using amplicon or metagenomic sequences.
- [PMID 35085485](https://pubmed.ncbi.nlm.nih.gov/35085485/) Genomic structure predicts metabolite dynamics in microbial communities.
- [PMID 33311510](https://pubmed.ncbi.nlm.nih.gov/33311510/) Using metacommunity ecology to understand environmental metabolomes.

PMID 37322284 and PMID 35592760 show how auxotrophs are supported in cultures, and PMID 31316056 predicts metabolites from sequences. None of them tests whether natural communities' synthesis completeness follows free amino acid levels once a shared pool is removed.
