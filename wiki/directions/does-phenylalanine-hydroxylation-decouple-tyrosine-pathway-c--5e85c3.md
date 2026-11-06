---
type: "Research direction"
description: "Is the non-significant positive tyrosine completeness-metabolite association (r = +0.419, ns) caused by tyrosine supply from phenylalanine hydroxylation, which the tyr completeness score does not capture, or does tyrosine follow a different exchange regime?"
hypothesis: "Communities that can hydroxylate phenylalanine maintain tyrosine pools independently of the scored biosynthesis route. Once a hydroxylation-route term is added to the tyrosine score, the completeness-pool correlation will move toward the negative direction seen in the 11 of 13 testable pathways."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Rescoring runs on existing NMDC tables, but the decisive isotope-tracing test needs new microcosm measurements."
collections: ["nmdc-arkin", "kbase-ke-pangenome"]
findings: ["nmdc_community_metabolic_ecology--6853a137", "nmdc_community_metabolic_ecology--4a766ba0"]
conflicts: ["conflict--community-metabolic-interdependence--e7db3c77"]
papers: ["10766779", "31316056", "35085485", "4562397"]
builds_on: ["findings/nmdc_community_metabolic_ecology--6853a137", "findings/nmdc_community_metabolic_ecology--4a766ba0", "conflicts/conflict--community-metabolic-interdependence--e7db3c77"]
projects: ["nmdc_community_metabolic_ecology"]
topics: ["metabolic-traits-auxotrophy-and-community-dependence"]
---
# Does phenylalanine hydroxylation decouple tyrosine pathway completeness from ambient tyrosine in soil communities?

Is the non-significant positive tyrosine completeness-metabolite association (r = +0.419, ns) caused by tyrosine supply from phenylalanine hydroxylation, which the tyr completeness score does not capture, or does tyrosine follow a different exchange regime?

## Hypothesis

Communities that can hydroxylate phenylalanine maintain tyrosine pools independently of the scored biosynthesis route. Once a hydroxylation-route term is added to the tyrosine score, the completeness-pool correlation will move toward the negative direction seen in the 11 of 13 testable pathways.

## Why it matters

The positive sign is currently an unexplained outlier to the Black Queen prediction. Showing that it comes from an unscored supply route would mean pathway-specific exceptions can be predicted from enzyme biochemistry. It would also tell users whether completeness scores are interpretable for amino acids with alternative sources.

## How to test it

In nmdc-arkin samples with paired taxonomy and metabolomics, annotate phenylalanine hydroxylase-route genes in the same communities. Rescore tyrosine with and without that route and recompute the Spearman correlation against tyrosine intensity. Compare with phenylalanine intensity. Then run soil microcosms with isotope-labelled phenylalanine and measure labelled tyrosine appearance against community hydroxylase gene content.

## What would support or refute it

Support: the correlation becomes negative or loses its positive sign with the hydroxylation term, and labelled tyrosine appears in proportion to hydroxylase gene content. Refute: the correlation stays positive after rescoring and no labelled conversion is detected. The original association is non-significant, so only a significant positive sign that replicates would argue for a distinct regime.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Rescoring runs on existing NMDC tables, but the decisive isotope-tracing test needs new microcosm measurements.

- Collection: [[data/nmdc-arkin|NMDC Multi-omics]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/nmdc_community_metabolic_ecology--6853a137|Tyrosine and isoleucine show no Black Queen signal]] (Insufficient literature evidence)
- Finding: [[findings/nmdc_community_metabolic_ecology--4a766ba0|Nearly all amino-acid pathways differ in community completeness across ecosystem types]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--community-metabolic-interdependence--e7db3c77|Does Community Provisioning Produce a Common Negative Amino-Acid Pattern, or Does Tyrosine Follow a Different Regime?]]

## Closest published work

- [PMID 10766779](https://pubmed.ncbi.nlm.nih.gov/10766779/) D-tyrosyl-tRNA(Tyr) metabolism in Saccharomyces cerevisiae.
- [PMID 31316056](https://pubmed.ncbi.nlm.nih.gov/31316056/) Predictive metabolomic profiling of microbial communities using amplicon or metagenomic sequences.
- [PMID 35085485](https://pubmed.ncbi.nlm.nih.gov/35085485/) Genomic structure predicts metabolite dynamics in microbial communities.
- [PMID 4562397](https://pubmed.ncbi.nlm.nih.gov/4562397/) Isoleucine auxotrophy due to feedback hypersensitivity of biosynthetic threonine deaminase.

PMID 10766779 and PMID 4562397 concern tyrosine and isoleucine metabolism in single organisms, and PMID 31316056 and PMID 35085485 predict metabolites from community sequences. None examines tyrosine as an outlier to community-scale provisioning.
