---
type: "Method"
description: "Kaiju, the NCBI-NR read-based taxonomic classifier used for the Kuehl_WGS (UC Davis) IBD cohort, and the reliability and classifier-mismatch limits that follow from using it alongside MetaPhlAn3-trained references."
sources: ["summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md"]
---
Kaiju is a taxonomic classification method applied to sequencing reads; the cross-project digest names the specific configuration in use as "Kaiju NCBI-NR read classification", i.e. read classification against the NCBI non-redundant protein database [src: discoveries]. Within this corpus it appears as the taxonomic profiler for the Kuehl_WGS (UC Davis) whole-genome-shotgun cohort of the IBD phage-targeting project, where it supplies both ecotype-projection features and pathobiont presence calls [src: ibd_phage_targeting]. Because the reference embedding it is projected onto was built from a different profiler, Kaiju is also the pivot case for [[concepts/classifier-database-compatibility-in-taxonomic-quantification]] and [[concepts/cross-cohort-microbiome-portability]].

## Aliases and identifiers

- "Kaiju NCBI-NR read classification" — the fuller form used in the cross-project digest for the configuration projected onto the reference embedding [src: discoveries]
- Contrasted throughout with [[entities/metaphlan3]], the marker-gene relative-abundance profiler used for the reference/training data [src: discoveries]
- No external accession or version identifier for the tool is recorded in the sources [src: ibd_phage_targeting]

## Use in the Kuehl_WGS (UC Davis) cohort

All 26 Kuehl_WGS samples (23 unique patients) were projected onto the K = 4 reference via the synonymy layer, with 262 unique Kaiju-classified species normalized to 97 canonical species in the training feature space; the resulting UC Davis distribution was [src: ibd_phage_targeting]:
- E0 — diverse commensal: 7 samples (27 %)
- E1 — Bacteroides2 transitional: 11 samples (42 %)
- E2 — *prevotella copri* enterotype: 0 samples
- E3 — severe Bacteroides-expanded: 8 samples (31 %) [src: ibd_phage_targeting]

These calls feed [[concepts/gut-microbiome-ecotypes-as-patient-strata]] [src: ibd_phage_targeting].

For per-patient target selection, Kuehl_WGS Kaiju Tier-A pathobiont presence was called at a threshold of ≥0.001 relative abundance, alongside ecotype, demographics (Montreal, calprotectin, medication), a Tier-A score, a mechanism profile, and phage availability [src: ibd_phage_targeting].

## Technical reliability

Kaiju repeatability was checked directly rather than assumed: patient 1112 contributed two resequencing replicates of the same biological sample, used as a technical Kaiju reliability validation and explicitly not as a longitudinal comparison [src: ibd_phage_targeting]. Those replicates gave a [[entities/spearman-correlation]] ρ = 1.000 on Tier-A, reported as evidence that Kaiju is reliable across reseq replicates and as a validation of the technical-noise floor [src: ibd_phage_targeting]. This rests on a single replicate pair, so it is best read as a case-specific rank-repeatability check for those two libraries rather than a cohort-wide bound on technical noise, and it carries no information about agreement with other classifiers [src: ibd_phage_targeting].

## Classifier mismatch with MetaPhlAn3

The structural problem is a mismatch of profilers across cohorts: a held-out cohort processed with Kaiju NCBI-NR read classification was projected onto a reference embedding trained on MetaPhlAn3 marker-gene relative abundance, and under that mismatch the two ecotype assignment methods — LDA (latent Dirichlet allocation, implemented as sklearn `LatentDirichletAllocation`) on pseudo-counts, and GMM (Gaussian mixture model) on CLR (centered log-ratio) transformed data followed by [[entities/principal-component-analysis]] — behave very differently [src: discoveries].

The project report states the asymmetry plainly: LDA on pseudo-counts is robust, because the out-of-training-space sparsity is handled by treating absence as not-detected, whereas GMM on CLR + PCA is fragile, the same sparsity forcing all 26 Kuehl samples into a single Gaussian (E3) at confidence > 0.97 — "an artifact, not biology"; LDA was therefore taken as the primary Kuehl projection call and GMM as advisory [src: ibd_phage_targeting]. The same asymmetry is flagged as a transferable finding relevant to any multi-classifier microbiome pipeline, LDA robust and CLR+GMM fragile [src: ibd_phage_targeting]. This **refines** [[concepts/ecotype-clustering-validity]] narrowly, at the single point of cross-classifier projection: the failure documented here is the projection artifact produced when Kaiju features are pushed through a CLR + PCA representation built on MetaPhlAn3 data, and nothing broader about the reference clustering is established by it [src: ibd_phage_targeting].

The 54 % sparsity figure should be quoted with care, because the two sources attach it to incompatible denominators. The project report describes "54 % of Kuehl feature rows outside the training feature space" as what LDA absorbs by treating absence as not-detected [src: ibd_phage_targeting]. The cross-project digest instead states that Kuehl detects only 54 % of training species, and separately that 70 % of training species have no Kuehl detection [src: discoveries]. These descriptions are not reconciled in the sources and are not combined here.

The consequence is a graded, not binary, trust level for Kaiju-derived calls. The Kaiju vs MetaPhlAn3 classifier mismatch limits confidence in the UC Davis ecotype calls, with LDA more trustworthy than GMM in this setting [src: ibd_phage_targeting]; and because Kuehl_WGS uses Kaiju rather than MetaPhlAn3, its Tier-A presence calls have lower confidence than the [[entities/curatedmetagenomicdata]] (CMD) analyses [src: ibd_phage_targeting].

## Resolution limits in this cohort

The Kaiju-based calls used here are species-presence calls, and the cohort has no strain-level companion assay: there is no per-patient AIEC (adherent-invasive *[[entities/escherichia-coli]]*) strain-resolution diagnostic in the current cohort, and while the 8 / 23 *E. coli*-positive patients carry detectable *E. coli* by Kaiju, the 5-phage AIEC cocktail recommendation (NB13) assumes AIEC-subset prevalence per Dogan 2014 / Dubinsky 2022; per-patient AIEC genotyping (pks-island + Yersiniabactin + Enterobactin) is listed as a near-term clinical-translation prerequisite [src: ibd_phage_targeting]. This is a gap in the cohort's assay panel as described, not a measured statement about what the classifier can or cannot distinguish [src: ibd_phage_targeting].
