---
type: "Organism"
description: "Human gut commensal that defines the E2 \"Prevotella copri enterotype\" \u2014 a near-exclusively healthy, largely non-Western ecotype absent from a UC Davis clinical cohort \u2014 and a named marker species for proposed qPCR ecotype panels."
sources: ["summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md"]
---
# Prevotella copri

*Prevotella copri* (abbreviated *P. copri* in the source reports) is a human gut bacterial species whose relative abundance names one of four reference gut microbiome ecotypes (K = 4) — community states used as patient strata — derived from stool metagenomes: E2, the *Prevotella copri* enterotype, holds 920 samples, with the defining species reported as mean abundance per ecotype (*P. copri* 28 %, *F. prausnitzii* 6 %) [src: ibd_phage_targeting].

## Health association

The central discoveries digest tabulates the same stratum as "E2 — Prevotella copri enterotype | 920 | P. copri 28 % | 16.9 % of HC, ~0 % disease (non-Western healthy)", i.e. 16.9 % of healthy controls (HC) and approximately none of the disease samples fall in this ecotype [src: discoveries]. The project report restates this reading directly, describing E2 as the *P. copri* enterotype, "almost entirely non-Western healthy", and pairs it with E0 (diverse commensal) at 66.8 % of healthy controls as the two healthy-cohort ecotypes [src: ibd_phage_targeting]. These are prevalence counts over a reference clustering of cohort samples, so the healthy skew of E2 is an observation about the composition of the clustered cohorts and not, in the reported analysis, a test of whether *P. copri* carriage is protective [src: discoveries, ibd_phage_targeting].

## Position among the reference ecotypes

Defining-species abundances (means per ecotype) and diagnosis patterns of the four consensus ecotypes, with E2 the only *Prevotella*-defined stratum [src: ibd_phage_targeting]:

| Ecotype | Samples | Defining species (mean abundance per ecotype) | Diagnosis pattern [src: ibd_phage_targeting] |
| --- | --- | --- | --- |
| **E0** — Diverse commensal | 3,604 | *F. prausnitzii* 6.8 %, *R. bromii* 4.5 %, *B. uniformis* 4.6 %, *P. vulgatus* 4.4 % | **66.8 % of HC** |
| **E1** — Bacteroides2 transitional | 2,601 | *P. vulgatus* 9.8 %, *B. uniformis* 7.2 %, *Phocaeicola dorei* 3.5 % | **48 % CD, 58 % UC, 100 % T1D, 97 % T2D, 67 % nonIBD** |
| **E2** — *Prevotella copri* enterotype | 920 | *P. copri* 28 %, *F. prausnitzii* 6 % | 16.9 % HC, ~0 % disease (non-Western healthy) |
| **E3** — Severe Bacteroides-expanded | 1,364 | *P. vulgatus* 14.2 %, *B. fragilis* 3.6 % | **50 % CD, 40 % UC, 67 % IBD acute, 38 % CDI, donor 2708** |

## Absence in the UC Davis validation cohort

All 26 Kuehl_WGS samples (23 unique patients) were projected onto the K = 4 reference through a species-name synonymy layer, which normalized 262 unique [[entities/kaiju]]-classified species to 97 canonical species in the training feature space; the UC Davis cohort distributed as E0 — diverse commensal: 7 samples (27 %), E1 — Bacteroides2 transitional: 11 samples (42 %), E2 — *Prevotella copri* enterotype: 0 samples, and E3 — severe Bacteroides-expanded: 8 samples (31 %) [src: ibd_phage_targeting].

That E2 drew zero samples is **consistent with** the characterization of the *P. copri* enterotype as almost entirely non-Western healthy [src: ibd_phage_targeting], but the observation rests on a single clinical cohort of 26 samples from 23 patients and on a feature space reduced from 262 classified species to 97 canonical ones, so it is best read as an expectation-matching null for this one cohort rather than as a test of *P. copri* geography [src: ibd_phage_targeting].

The caveat the report itself documents on this projection is a classifier mismatch, not a *Prevotella*-specific one: the Kuehl samples were classified with [[entities/kaiju]] while the reference embedding was trained on [[entities/metaphlan3]] profiles, and the two ecotype methods differ in robustness to that mismatch — LDA, the latent-factor topic model fitted on species pseudo-counts (sklearn `LatentDirichletAllocation`, scored by training perplexity) [src: discoveries], is robust, handling the 54 % of Kuehl feature rows outside the training feature space by treating absence as not-detected, whereas GMM (Gaussian mixture model) on CLR (centered log-ratio) + PCA is fragile, the same sparsity forcing all 26 Kuehl samples into a single Gaussian (E3) at confidence > 0.97, which the report calls an artifact, not biology; LDA is therefore the primary Kuehl projection call and GMM advisory [src: ibd_phage_targeting]. Any further explanation specific to *Prevotella* — for example that name normalization selectively erased *Prevotella* signal — is an untested hypothesis that the reported projection does not evaluate [src: ibd_phage_targeting].

## Use as a proxy marker

*P. copri* is one of the species named for a proposed targeted qPCR (quantitative PCR) ecotype panel of 4–6 species — *F. prausnitzii*, *P. copri*, *P. vulgatus*, *B. fragilis*, [[entities/mediterraneibacter-gnavus]] (*M. gnavus*) — intended to assign ecotype without full metagenomic sequencing; the report presents it as a panel design, with no assay validation reported [src: ibd_phage_targeting].

## Related pages

- [[concepts/gut-microbiome-ecotypes-as-patient-strata]]
- [[concepts/ecotype-clustering-validity]]
- [[concepts/cross-cohort-microbiome-portability]]
- [[concepts/proxy-assays-for-community-state-assignment]]
- [[concepts/classifier-database-compatibility-in-taxonomic-quantification]]
- [[summaries/ibd_phage_targeting__REPORT]]
- [[summaries/discoveries]]
