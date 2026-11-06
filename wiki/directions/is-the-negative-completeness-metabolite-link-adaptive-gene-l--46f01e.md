---
type: "Research direction"
description: "Does the negative correlation between community amino acid biosynthesis completeness and ambient amino acid level reflect selection favoring biosynthetic gene loss when neighbors supply the amino acid, or other causes such as taxon turnover?"
hypothesis: "If Black Queen loss operates, the correlation persists within taxa, pathway losses in species with variable pathways fall on recent branches in high-amino-acid samples, and an isogenic pathway-deletion mutant gains a fitness advantage over its parent that rises with leucine supplied by neighbors. Persistence of the correlation within taxa is necessary but not sufficient."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "One study supports the current result and abiotic features were NaN in the analysis matrix; the loss-event mapping needs compute and the competition assays are new measurements."
collections: ["nmdc-arkin", "kbase-ke-pangenome"]
findings: ["nmdc_community_metabolic_ecology--dcef6254", "nmdc_community_metabolic_ecology--7d46eb90", "nmdc_community_metabolic_ecology--6853a137"]
conflicts: []
papers: ["37322284", "35592760", "31316056", "35085485"]
builds_on: ["findings/nmdc_community_metabolic_ecology--dcef6254", "findings/nmdc_community_metabolic_ecology--7d46eb90", "findings/nmdc_community_metabolic_ecology--6853a137"]
projects: ["nmdc_community_metabolic_ecology"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Is the negative completeness-metabolite link adaptive gene loss, not just taxon turnover?

Does the negative correlation between community amino acid biosynthesis completeness and ambient amino acid level reflect selection favoring biosynthetic gene loss when neighbors supply the amino acid, or other causes such as taxon turnover?

## Hypothesis

If Black Queen loss operates, the correlation persists within taxa, pathway losses in species with variable pathways fall on recent branches in high-amino-acid samples, and an isogenic pathway-deletion mutant gains a fitness advantage over its parent that rises with leucine supplied by neighbors. Persistence of the correlation within taxa is necessary but not sufficient.

## Why it matters

Replicated correlations cannot separate public-goods dynamics from other processes. Evidence of selection on loss, with a measured fitness benefit of dropping the pathway, would show Black Queen dynamics shape environmental metabolite pools, not just culture co-existence.

## How to test it

Step 1 (lakehouse): decompose completeness variation for the 13 testable pathways into between-taxon and within-taxon parts, using GapMind pathway variability across pangenome genomes within species. Repeat the leucine and arginine tests (r = -0.390 and -0.297) in studies other than nmdc:sty-11-r2h77870, which supplied 125 of 131 samples, with pH, temperature and organic carbon as covariates once the abiotic fields are populated. Step 2: for species with variable pathways, map loss events on the GTDB tree and test whether losses are recent and linked to ambient amino acid, and whether retained pathway genes show relaxed constraint. Step 3: in a leucine-pathway species, compete the isogenic leucine biosynthesis deletion against its parent across graded leucine, with and without a prototroph neighbor supplying leucine, and measure biosynthesis cost.

## What would support or refute it

Support: the association holds within taxa and across studies, losses are recent and tied to ambient levels, and the deletion mutant's advantage rises with leucine, mainly when a neighbor supplies it. Refute: the association is confined to the dominant study or vanishes within taxa, or the deletion confers no advantage at any leucine. Such results would leave taxon turnover, other selection, or measurement limits unresolved; the data alone would not choose among them.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. One study supports the current result and abiotic features were NaN in the analysis matrix; the loss-event mapping needs compute and the competition assays are new measurements.

- Collection: [[data/nmdc-arkin|NMDC Multi-omics]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/nmdc_community_metabolic_ecology--dcef6254|Most amino-acid pathways show negative completeness–metabolite correlations, as Black Queen predicts]] (Candidate novel)
- Finding: [[findings/nmdc_community_metabolic_ecology--7d46eb90|Leucine signal survives soil-only stratification; arginine loses FDR significance]] (Insufficient literature evidence)
- Finding: [[findings/nmdc_community_metabolic_ecology--6853a137|Tyrosine and isoleucine show no Black Queen signal]] (Insufficient literature evidence)

## Closest published work

- [PMID 37322284](https://pubmed.ncbi.nlm.nih.gov/37322284/) Bacteriophage-mediated lysis supports robust growth of amino acid auxotrophs.
- [PMID 35592760](https://pubmed.ncbi.nlm.nih.gov/35592760/) Dynamic proteome allocation regulates the profile of interaction of auxotrophic bacterial consortia.
- [PMID 31316056](https://pubmed.ncbi.nlm.nih.gov/31316056/) Predictive metabolomic profiling of microbial communities using amplicon or metagenomic sequences.
- [PMID 35085485](https://pubmed.ncbi.nlm.nih.gov/35085485/) Genomic structure predicts metabolite dynamics in microbial communities.

PMID 37322284 and PMID 35592760 treat auxotroph provisioning in cultures, and PMID 31316056 and PMID 35085485 predict metabolites from community genes; none tests selection on gene loss against taxon turnover in environmental samples.
