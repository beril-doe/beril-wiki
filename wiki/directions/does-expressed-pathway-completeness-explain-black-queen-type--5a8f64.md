---
type: "Research direction"
description: "Community completeness of amino acid biosynthesis pathways tends to fall as the ambient amino acid rises in NMDC soil samples. Does the signal come from expressed pathways rather than gene presence?"
hypothesis: "Pathway completeness calculated from expressed transcripts shows a stronger negative link to ambient amino acid intensity than completeness calculated from taxonomic gene content."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The catalog lists NMDC metabolomics, file and taxonomy tables, but the shown columns do not confirm which samples have expression data."
databases: ["kbase.ke_pangenome", "kbase.nmdc_arkin"]
tables: ["kbase.nmdc_arkin.metabolomics_gold", "kbase.nmdc_arkin.omics_files_table", "kbase.nmdc_arkin.kraken_gold", "kbase.nmdc_arkin.covstats_taxonomy_rollup", "kbase.ke_pangenome.gapmind_pathways"]
findings: ["nmdc_community_metabolic_ecology--33da3819", "nmdc_community_metabolic_ecology--821653f8", "nmdc_community_metabolic_ecology--ddb1a444"]
conflicts: []
papers: ["31316056", "33311510", "35085485"]
builds_on: ["findings/nmdc_community_metabolic_ecology--33da3819", "findings/nmdc_community_metabolic_ecology--821653f8", "findings/nmdc_community_metabolic_ecology--ddb1a444"]
projects: ["nmdc_community_metabolic_ecology"]
topics: ["metabolic-models-and-pathway-level-evidence"]
---
# Does expressed pathway completeness explain Black Queen-type amino acid signals in soil metabolomes?

Community completeness of amino acid biosynthesis pathways tends to fall as the ambient amino acid rises in NMDC soil samples. Does the signal come from expressed pathways rather than gene presence?

## Hypothesis

Pathway completeness calculated from expressed transcripts shows a stronger negative link to ambient amino acid intensity than completeness calculated from taxonomic gene content.

## Why it matters

It would show whether the Black Queen pattern reflects active gene use in communities. That would justify expression-based metabolic ecology over genome-based prediction.

## How to test it

For NMDC samples with paired metabolomics, compute leucine and arginine pathway completeness two ways: from taxonomy profiles (Kraken, Centrifuge, contig rollups) linked to GapMind pathway calls, and from metatranscriptome-derived abundances where files exist. Compare each against ambient metabolite intensity from the metabolomics table.

## What would support or refute it

Support: the expression-based measure gives a clearly stronger negative association for leucine and arginine. Refute: the two measures agree or the expression measure is weaker. Most current samples come from one study, so cross-study agreement should be reported.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The catalog lists NMDC metabolomics, file and taxonomy tables, but the shown columns do not confirm which samples have expression data.

## Builds on

- Finding: [[findings/nmdc_community_metabolic_ecology--33da3819|Leucine completeness negatively tracks ambient leucine after FDR correction]] (Candidate novel)
- Finding: [[findings/nmdc_community_metabolic_ecology--821653f8|Arginine completeness negatively tracks ambient arginine after FDR correction]] (Candidate novel)
- Finding: [[findings/nmdc_community_metabolic_ecology--ddb1a444|Most amino acid pathways show negative completeness-metabolite correlations, as Black Queen predicts]] (Candidate novel)

## Closest published work

- [PMID 31316056](https://pubmed.ncbi.nlm.nih.gov/31316056/) Predictive metabolomic profiling of microbial communities using amplicon or metagenomic sequences.
- [PMID 33311510](https://pubmed.ncbi.nlm.nih.gov/33311510/) Using metacommunity ecology to understand environmental metabolomes.
- [PMID 35085485](https://pubmed.ncbi.nlm.nih.gov/35085485/) Genomic structure predicts metabolite dynamics in microbial communities.

Studies 31316056, 33311510 and 35085485 link communities to metabolites by prediction or ecological modelling, but not through pathway completeness and ambient amino acids.
