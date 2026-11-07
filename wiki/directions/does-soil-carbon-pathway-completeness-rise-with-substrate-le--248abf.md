---
type: "Research direction"
description: "Soil communities have broadly higher carbon-use pathway completeness than freshwater ones. Within soil, does completeness for each carbon pathway rise with the ambient level of its own substrate, the opposite of the mostly negative trend seen for amino acid biosynthesis?"
hypothesis: "Within soil, community completeness for carbon-use pathways such as cellobiose, galactose and glucuronate rises with the ambient intensity of the matching substrate, and this holds in more than one independent study, because catabolism is retained where the substrate is available."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Paired data exist for these samples, but 125 of 131 come from a single study and abiotic data are missing, so testing generality likely requires metabolomics from other studies."
collections: ["nmdc-arkin", "nmdc-ncbi-biosamples", "kbase-ke-pangenome"]
findings: ["nmdc_community_metabolic_ecology--fb740bf4", "nmdc_community_metabolic_ecology--dcef6254", "nmdc_community_metabolic_ecology--7d46eb90"]
conflicts: []
papers: ["35085485", "31316056", "33311510"]
builds_on: ["findings/nmdc_community_metabolic_ecology--fb740bf4", "findings/nmdc_community_metabolic_ecology--dcef6254", "findings/nmdc_community_metabolic_ecology--7d46eb90"]
projects: ["nmdc_community_metabolic_ecology"]
topics: ["metabolic-models-and-pathway-level-evidence"]
---
# Does soil carbon-pathway completeness rise with substrate level, unlike amino acid pathways?

Soil communities have broadly higher carbon-use pathway completeness than freshwater ones. Within soil, does completeness for each carbon pathway rise with the ambient level of its own substrate, the opposite of the mostly negative trend seen for amino acid biosynthesis?

## Hypothesis

Within soil, community completeness for carbon-use pathways such as cellobiose, galactose and glucuronate rises with the ambient intensity of the matching substrate, and this holds in more than one independent study, because catabolism is retained where the substrate is available.

## Why it matters

A split between catabolic genes kept where substrate is supplied and biosynthetic genes lost where product is supplied would give a general rule linking habitat chemistry to community metabolic configuration. A missing or reversed pattern would mean the soil-freshwater carbon difference reflects which taxa live there, not substrate supply. The amino acid result it is contrasted with rests on one study: 125 of 131 samples, including all 62 leucine samples, came from a single NMDC study, so generality beyond it is untested.

## How to test it

Step 1: count how many NMDC studies have paired taxonomy and metabolomics for soil; in the amino acid analysis 125 of 131 samples, and all 62 leucine samples, came from one study, and the 33 freshwater samples had no paired metabolomics. Step 2: compute community completeness for each carbon-use pathway from species-level pathway calls in the Pangenome Collection and correlate it with the matching metabolite intensity within each study separately, alongside amino acid pathways in the same samples. A result from the dominant study alone cannot show generality. Step 3: if fewer than two studies have paired data, generate metabolomics for soils from other studies or for the freshwater samples.

## What would support or refute it

Positive correlations for most carbon pathways in the dominant study and in at least one independent study would support the hypothesis. Absent or negative correlations in the dominant study would refute it. A pattern seen only in the dominant study would leave generality open and would not count as support.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Paired data exist for these samples, but 125 of 131 come from a single study and abiotic data are missing, so testing generality likely requires metabolomics from other studies.

- Collection: [[data/nmdc-arkin|NMDC Multi-omics]]
- Collection: [[data/nmdc-ncbi-biosamples|NMDC BioSamples]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/nmdc_community_metabolic_ecology--fb740bf4|Carbon-utilization pathways dominate the soil–freshwater separation axis, with amino acids secondary]] (Candidate novel)
- Finding: [[findings/nmdc_community_metabolic_ecology--dcef6254|Most amino-acid pathways show negative completeness–metabolite correlations, as Black Queen predicts]] (Candidate novel)
- Finding: [[findings/nmdc_community_metabolic_ecology--7d46eb90|Leucine signal survives soil-only stratification; arginine loses FDR significance]] (Insufficient literature evidence)

## Closest published work

- [PMID 35085485](https://pubmed.ncbi.nlm.nih.gov/35085485/) Genomic structure predicts metabolite dynamics in microbial communities.
- [PMID 31316056](https://pubmed.ncbi.nlm.nih.gov/31316056/) Predictive metabolomic profiling of microbial communities using amplicon or metagenomic sequences.
- [PMID 33311510](https://pubmed.ncbi.nlm.nih.gov/33311510/) Using metacommunity ecology to understand environmental metabolomes.

PMIDs 35085485 and 31316056 link community gene content to metabolite dynamics, and PMID 33311510 treats environmental metabolomes; none contrasts carbon-use and amino acid pathways against ambient substrate levels.
