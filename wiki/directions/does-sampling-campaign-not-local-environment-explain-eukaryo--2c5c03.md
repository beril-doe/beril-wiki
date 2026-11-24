---
type: "Research direction"
description: "Within the NEON soil study, does local environment and geography still predict the eukaryotic read fraction once sampling campaign or batch is accounted for?"
hypothesis: "The within-study predictive power of local environment and geography for eukaryotic fraction is mostly carried by sampling campaign; with campaign held out, predictive power falls to near zero, as it does across studies."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Biosample and run tables appear in the catalog, but the GOTTCHA2 output table was not shown and models must be fitted."
databases: ["kbase.nmdc_arkin", "nmdc.metadata"]
tables: ["nmdc.metadata.biosample_set", "nmdc.metadata.study_set", "nmdc.metadata.data_generation_set", "kbase.nmdc_arkin.kraken_gold", "kbase.nmdc_arkin.centrifuge_gold"]
findings: ["euk_in_prok_correlates--d08fdf8f", "euk_in_prok_correlates--c74ec1ab", "euk_in_prok_correlates--6bab0d6d"]
conflicts: []
papers: ["41854267", "41373768", "40708004"]
builds_on: ["findings/euk_in_prok_correlates--d08fdf8f", "findings/euk_in_prok_correlates--c74ec1ab", "findings/euk_in_prok_correlates--6bab0d6d"]
projects: ["euk_in_prok_correlates"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Does sampling campaign, not local environment, explain eukaryotic read fraction within a single soil study?

Within the NEON soil study, does local environment and geography still predict the eukaryotic read fraction once sampling campaign or batch is accounted for?

## Hypothesis

The within-study predictive power of local environment and geography for eukaryotic fraction is mostly carried by sampling campaign; with campaign held out, predictive power falls to near zero, as it does across studies.

## Why it matters

If true, apparent environmental drivers of eukaryotic contamination in prokaryote-targeted metagenomes are batch effects, and metagenome users should model campaign before interpreting environment.

## How to test it

Take the eukaryotic fraction per run from the GOTTCHA2 taxonomy output, the only classifier reported to give a usable fraction, treated as relative rather than absolute. Join to NMDC biosample, study and data-generation tables for NEON soil runs, with Kraken and Centrifuge outputs used only as predictors if suitable. Compare models using environment and geography alone against models holding out whole collection dates or campaigns. The catalog did not show the GOTTCHA2 table, so its location must be confirmed.

## What would support or refute it

Support: held-out-campaign predictive power drops to about zero or below while campaign-labelled models keep the earlier within-study gain. Refute: environment and geography keep their predictive power when campaigns are held out.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Biosample and run tables appear in the catalog, but the GOTTCHA2 output table was not shown and models must be fitted.

## Builds on

- Finding: [[findings/euk_in_prok_correlates--d08fdf8f|Environment predicts eukaryotic fraction within one soil study but not across studies]] (Candidate novel)
- Finding: [[findings/euk_in_prok_correlates--c74ec1ab|Environment does not generalize across studies beyond study identity]] (Candidate novel)
- Finding: [[findings/euk_in_prok_correlates--6bab0d6d|Platform and sequencing depth metadata add no out-of-study predictive power]] (Candidate novel)

## Closest published work

- [PMID 41854267](https://pubmed.ncbi.nlm.nih.gov/41854267/) Large-scale estimation of bacterial and archaeal DNA prevalence in metagenomes reveals biome-specific patterns.
- [PMID 41373768](https://pubmed.ncbi.nlm.nih.gov/41373768/) Benchmarking Cost-Effective DNA Extraction Kits for Diverse Metagenomic Samples.
- [PMID 40708004](https://pubmed.ncbi.nlm.nih.gov/40708004/) First island-wide, single-day soil collection study on Crete reveals environmental drivers of microbial diversity.

41854267 estimates prokaryotic fractions by biome across metagenomes but does not test whether campaign explains within-study environmental signal.
