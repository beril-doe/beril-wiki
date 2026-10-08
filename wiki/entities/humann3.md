---
type: "Method"
description: "HUMAnN3, the metagenomic functional profiler whose MetaCyc pathway-abundance outputs (unstratified and species-stratified) are analysed in this corpus and whose pathway categories depend on the class hierarchy used to annotate them."
sources: ["summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md"]
---
HUMAnN3 is the metagenomic functional-profiling tool whose pathway-abundance outputs appear in this corpus as [[entities/metacyc]]-keyed tables, used both in an unstratified form (one row per pathway) and in a species-resolved stratified-pathway form written as `PWY-XXX|g__species` [src: ibd_phage_targeting]. Its outputs are also the target of pathway-category annotation that draws on an external MetaCyc class hierarchy [src: discoveries].

## Pathway tables in the IBD phage-targeting analysis

The first Pillar 3 notebook (NB07a) of the IBD phage-targeting project took as its primary contrast a within-IBD-substudy CD-vs-nonIBD meta-analysis on `fact_pathway_abundance` (HUMAnN3 MetaCyc, CMD_IBD only). Substudy meta-viability was re-verified for the pathway modality: 3 robust (HallAB_2017, IjazUZ_2017, NielsenHB_2014) plus 1 boundary (LiJ_2014, nonIBD = 10) — explicitly **not** the "4 meta-viable" framing an earlier plan version had inherited from taxonomic-modality counts — and VilaAV_2018 was excluded (CD = 216, nonIBD = 0). 575 unstratified MetaCyc pathways were reduced to 409 after a 10%-prevalence filter [src: ibd_phage_targeting].

The a-priori category test on those unstratified pathways was structurally underpowered: NB07a's clause (b) failed because only 3 of 52 CD-up unstratified MetaCyc pathways landed in the 7 a-priori IBD categories. NB07b therefore retested the alternative at the species-resolved stratified-pathway form, asking whether per-species CD-up pathways concentrate in those categories [src: ibd_phage_targeting].

## Category annotation of HUMAnN3 output

[[entities/modelseed]]'s ModelSEEDDatabase ships a usable MetaCyc class hierarchy at `/global_share/KBaseUtilities/ModelSEEDDatabase/Biochemistry/Aliases/Provenance/MetaCyc_Pathways.tbl`, with 90 %+ coverage of HUMAnN3 outputs [src: discoveries].

The category schema applied to HUMAnN3 pathway names can change the conclusion on its own: the IBD phage-targeting report records that its v1.7 → v1.8 change was a major scientific reversal driven entirely by category-schema choice — v1.7 "no compositional themes" (FAIL) became v1.8 "iron/heme is the dominant theme" (SUPPORTED, OR 8.1, FDR 7e-6, where FDR is the false-discovery-rate-adjusted p-value) on the same data and the same differential-abundance (DA) analysis. The stated lesson is that regex-on-pathway-names is a poor substitute for a curator-validated ontology or class hierarchy when one is available; the report gives 90 % coverage of HUMAnN3 outputs for the ModelSEEDDatabase MetaCyc hierarchy and recommends it as the default for pathway category-enrichment tests [src: ibd_phage_targeting]. This is the entity-level anchor for [[concepts/ontology-and-category-schema-sensitivity]].
