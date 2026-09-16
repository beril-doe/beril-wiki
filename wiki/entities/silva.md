---
type: "Dataset"
description: "SILVA is a ribosomal RNA reference sequence database that BERIL amplicon projects used for 16S rRNA taxonomy assignment."
sources: ["summaries/lignin_community_enrichment__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md"]
---
# SILVA rRNA database

SILVA is a reference database of SSU (small-subunit) ribosomal RNA sequences. In this corpus it is the taxonomy reference for 16S rRNA [[entities/16s-amplicon-sequencing]] pipelines in two projects. [[summaries/lignin_community_enrichment__REPORT]] uses release 138.2, and [[summaries/microbeatlas_metal_ecology__REPORT]] uses release 138 [src: lignin_community_enrichment, microbeatlas_metal_ecology].

- Aliases: SILVA; SILVA 138; SILVA 138.2; SILVA 138.2 NR99 [src: lignin_community_enrichment, microbeatlas_metal_ecology].

## Use in lignin_community_enrichment

The lignin enrichment project processed reads with vsearch. It clustered them into operational taxonomic units (OTUs) at 97% similarity and removed chimeras de novo. It assigned 16S taxonomy with SILVA 138.2, using vsearch sintax at 80% confidence. ITS taxonomy did not use SILVA. It was assigned against NCBI ITS_RefSeq_Fungi with BLASTn (see [[entities/its-amplicon-sequencing]]) [src: lignin_community_enrichment].

The project's reference table lists SILVA 138.2 NR99 as containing 510,495 SSU rRNA reference sequences, used for 16S taxonomy assignment [src: lignin_community_enrichment].

## Use in microbeatlas_metal_ecology

The metal-ecology project reprocessed the PRJNA1084851 amplicon dataset with an end-to-end pipeline. The pipeline downloads reads from the [[entities/european-nucleotide-archive]] (ENA) FTP server, trims primers with cutadapt and merges reads with vsearch. It then clusters OTUs at 97% similarity and assigns SILVA 138 taxonomy to produce an OTU table. The pipeline processed 81 samples via ENA. For recovered samples, it used existing merged FASTQs instead [src: microbeatlas_metal_ecology].

The resulting PRJNA1084851 OTU table holds 133 samples × 24,295 OTUs and was built with 97% OTU clustering and SILVA 138 taxonomy. The raw FASTQs were deleted after processing [src: microbeatlas_metal_ecology].

## Limitations

In microbeatlas_metal_ecology, genus-level SILVA taxonomy could be matched to [[entities/gtdb]] AMR annotations only for OTUs covering 16.8% of reads. The remaining ~83% of reads came from genera without taxonomy matches and were excluded from CWM (community-weighted mean), the project's metal-resistance metric. If the uncovered genera have systematically different metal resistance profiles, CWM could be biased. For example, it would be biased upward if uncovered lineages were mostly metal-sensitive. The report gives 1.01–1.83 as the CWM range, but its coverage caveat calls the same interval the "between-sample variance in CWM (1.01–1.83)". This wiki keeps both labels as reported and does not settle which is meant. The report says this spread and the correlation with known contamination status (FW215/FW216 in the plume) are consistent with a real biological signal. However, robustness to variation in the covered-read fraction has not been formally tested. Before CWM is used in further analyses, the report recommends a diagnostic: correlating per-sample CWM with per-sample covered-read fraction. This caveat about SILVA-to-GTDB name matching comes from a single project (see [[concepts/taxonomic-nomenclature-reconciliation]]) [src: microbeatlas_metal_ecology].

In the same project, *Citrobacter* and *Thermodesulfovibrio* were not detected. The report gives two possible explanations and does not choose between them: abundance below detection, or genus names that do not match under SILVA nomenclature [src: microbeatlas_metal_ecology].

## Version note

The two projects report different SILVA releases: 138.2 (specified as NR99) in lignin_community_enrichment and 138 in microbeatlas_metal_ecology. The sources do not say whether this difference affects taxonomy calls. Cross-project comparisons of SILVA-assigned genera should take this into account (see [[concepts/classifier-database-compatibility-in-taxonomic-quantification]]) [src: lignin_community_enrichment, microbeatlas_metal_ecology].
