---
type: "Concept"
description: "Candidate analyses that use idle bridges between collections (subsurface prophages and metal resistance, pathogen environmental ecology, GTDB versus pangenome taxonomy, ontology coverage of biosamples) and the validation they need; stops at executed results."
sources: ["summaries/berdl_data_atlas__REPORT.md"]
---
# Untapped cross-program synergy use cases for environmental and clinical microbiology

This page collects candidate analyses that use bridges between data collections which nobody had used at audit time. The source is the [[summaries/berdl_data_atlas__REPORT|berdl_data_atlas report]], which presents five untapped use cases (UC1–UC5). They cover structure and fitness, subsurface prophages and metal resistance, GTDB harmonization, pathogen ecology and ontology coverage. The evidence is a bridge audit plus a sample validation of UC1 only. UC2–UC5 are proposals, not results. [src: berdl_data_atlas]

## Literature Context

The candidate papers bear mainly on UC3, the proposed comparison of GTDB clades with KBase species pangenomes, and on the taxonomy that the other use cases rely on. They do not address subsurface prophages, pathogen ecology, ENVO coverage or AlphaFold-based structure and fitness work. The Genome Taxonomy Database (GTDB) gives a phylogenetically consistent, rank-normalized genome-based taxonomy for prokaryotic genomes taken from NCBI Assembly. It uses average nucleotide identity (ANI) as a pragmatic way to delineate species [PMID 34520557](https://pubmed.ncbi.nlm.nih.gov/34520557/). Release 10 (R10-RS226) spans 715 230 bacterial and 17 245 archaeal genomes, grouped into 136 646 bacterial and 6968 archaeal species clusters. Its authors project that more than 95% of bacterial and archaeal species remain to be genomically elucidated [PMID 41123020](https://pubmed.ncbi.nlm.nih.gov/41123020/). GTDB has also been described as lumping and splitting pre-existing phyla. Whether phyla still reflect significant evolutionary and ecological partitions remains debated [PMID 39250184](https://pubmed.ncbi.nlm.nih.gov/39250184/).

Several papers support using GTDB as a harmonizing layer. GTDB-Tk assigns taxonomy to bacterial and archaeal genomes. It was evaluated on a phylogenetically diverse set of 10,156 metagenome-assembled genomes [PMID 31730192](https://pubmed.ncbi.nlm.nih.gov/31730192/). Version 2 cut the memory requirement, which had been about 320 GB, with minimal impact on classification [PMID 36218463](https://pubmed.ncbi.nlm.nih.gov/36218463/). A GUNC screen of release 07-RS207 flagged 35,723 genomes as putatively contaminated, 11.25% of 317,542. The authors then made clean versions of 34,846 flagged bacterial genomes by removing the most contaminated half of each genome. Only 77 (0.22%) of the genomes were inconsistent with their original classification, so taxon delineation was robust to this contamination [PMID 38809778](https://pubmed.ncbi.nlm.nih.gov/38809778/). This matters for UC3. Disagreements between GTDB clades and pangenome species are less likely to come from contamination of the genomes. Other tools already anchor to GTDB, including iTOL v6, which supports GTDB-based taxonomy assignment [PMID 38613393](https://pubmed.ncbi.nlm.nih.gov/38613393/). GARNET links RNA sequences to optimal growth temperatures of GTDB reference organisms [PMID 39638800](https://pubmed.ncbi.nlm.nih.gov/39638800/). General reviews place GTDB among the core bacterial metagenomics databases [PMID 37258857](https://pubmed.ncbi.nlm.nih.gov/37258857/). The AlphaFold Protein Structure Database, the resource behind UC1's AlphaFold IDs, is noted as a stand-out new arrival in the 2022 NAR database issue [PMID 34986604](https://pubmed.ncbi.nlm.nih.gov/34986604/).

The BERDL Data Atlas findings are consistent with this literature on one point. GTDB is a widely adopted, stable reference, so the kbase ↔ refdata bridge, which includes gtdb_taxonomy, is a sensible place for a harmonization project. The report's claim that this bridge had zero realized use at audit time is about the KBase Data Lakehouse. The literature neither supports nor contradicts it. The papers do not test whether GTDB clades and KBase species pangenomes disagree, or what any disagreement implies for gene flow. UC3 therefore extends the literature and remains a proposal. The same applies to UC2, UC4 and UC5, which have no support among these candidates. The report validated only UC1, in a sample, and found no tension with the cited work.

## Why these bridges

Five high-leverage bridges had zero realized use at audit time. They are kescience ↔ refdata (12 keys, including AlphaFold IDs), enigma ↔ phagefoundry (11), kbase ↔ refdata (11, including gtdb_taxonomy), nmdc ↔ protect (10) and nmdc ↔ refdata (9). [src: berdl_data_atlas] The report ships data/untapped_bridges.csv, which lists 20 highest-leverage unrealized bridges. Each has at least one shared key and no realized projects. [src: berdl_data_atlas] For the wider context, see [[concepts/realized-versus-theoretical-cross-collection-data-reuse]]. The report expects these bridges to extend into refdata, nmdc_arkin, PhageFoundry / PROTECT and ENIGMA. [src: berdl_data_atlas]

## The five use cases

| Use case | Bridge | Shared keys | Question |
|---|---|---|---|
| UC1 | kescience ↔ refdata | 12 | Do high-fitness-impact genes have structural signatures detectable in AlphaFold? [src: berdl_data_atlas] |
| UC2 | enigma ↔ phagefoundry | 11 | Do subsurface prophages mobilize metal-resistance along the Oak Ridge contamination gradient? [src: berdl_data_atlas] |
| UC3 | kbase ↔ refdata | 11 | Where do GTDB clades and KBase species pangenomes disagree, and what does that imply for gene flow? [src: berdl_data_atlas] |
| UC4 | nmdc ↔ protect | 10 | Where do clinically relevant pathogens live in the environment, and what biogeochemistry tracks them? [src: berdl_data_atlas] |
| UC5 | nmdc ↔ refdata | 9 | What fraction of NMDC biosamples carry well-formed ENVO (Environment Ontology) terms, and where does coverage break? [src: berdl_data_atlas] |

UC4 and UC5 both rely on the NMDC multi-omics layer. [src: berdl_data_atlas] See [[entities/enigma]], [[entities/phagefoundry]], [[entities/nmdc-integrated-collections]] and [[entities/protect-genome-depot]] for the collections involved.

## Status and validation

UC1 is the biggest single untapped opportunity in the report. Its bridge is intra-DOE-BER, has 99.5% join coverage and is sample-validated. The report calls it ready to scope as a standalone project. [src: berdl_data_atlas] UC1 has been completed. UC2–UC5 each still need a first sample execution before publication. [src: berdl_data_atlas] The UC1 topic is developed in [[concepts/structure-fitness-integration-of-mutant-fitness-data-with-predicted-protein-structures]]. Join-key problems that UC2–UC5 could hit are covered in [[concepts/join-key-validity-and-identifier-format-mismatches]].

The report calls for validating UC2–UC5 against the live cluster, at about 15–30 min of structured query language (SQL) probing each, to confirm value-space overlap and surface join-recipe corrections. [src: berdl_data_atlas] It names UC3 (kbase ↔ refdata, GTDB harmonization) as the next lowest-friction case, because it is intra-DOE-BER and both tenants are well documented. [src: berdl_data_atlas] It also proposes promoting UC1 into its own project, with the validated 55,454-gene cohort as the seed dataset. [src: berdl_data_atlas]

The report ranks shared sample and ENVO ontology investment (UC5) as the highest-leverage scoping bet. [src: berdl_data_atlas] It notes, from agent memory and not from a measurement, that NMDC metabolomics (3.1M), proteomics (346K) and lipidomics (1.4M) layers are largely untapped. [src: berdl_data_atlas]

## Open Directions

- Validate UC2–UC5 against the live cluster with short SQL probes. This would confirm value-space overlap and expose join-recipe corrections, and UC3 is the cheapest to start.
- Promote UC1 into its own project, seeded with the validated 55,454-gene cohort, to test structural signatures of high-fitness-impact genes.
- Run UC5 as a coverage census of ENVO terms on NMDC biosamples. It would show where ontology coverage breaks and would support UC4's environmental context.
- Check the "largely untapped" NMDC multi-omics claim with a direct usage count, since it now rests on agent memory.
