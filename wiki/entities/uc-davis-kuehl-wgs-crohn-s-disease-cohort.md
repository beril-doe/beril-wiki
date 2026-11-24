---
type: "Dataset"
description: "Kaiju-classified shotgun metagenomes from 23 UC Davis Crohn's patients used for ecotype projection and per-patient cocktail drafting."
sources: ["summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md"]
aliases: ["Kuehl_WGS", "UC Davis cohort"]
---
# UC Davis Kuehl_WGS Crohn's disease cohort

This page covers Kaiju-classified shotgun metagenomes from 23 UC Davis Crohn's patients, used for ecotype projection and per-patient cocktail drafting. The ibd_phage_targeting project projected the cohort onto a four-ecotype reference. [src: ibd_phage_targeting] See [[summaries/ibd_phage_targeting__REPORT]] and [[summaries/discoveries]].

## Key facts

- The cohort has 26 Kuehl_WGS samples from 23 unique patients. All were projected onto the K = 4 reference through the synonymy layer. [src: ibd_phage_targeting]
- 262 unique Kaiju-classified species were normalized to 97 canonical species in the training feature space. [src: ibd_phage_targeting]
- All patients have IBD, so `is_ibd = 1` is constant in this cohort. [src: discoveries]

## Ecotype projection

Under the LDA projection, the samples fall into E0, E1 and E3, with none in E2. [src: discoveries, ibd_phage_targeting] The report calls these proportions biologically plausible. [src: discoveries]

| Ecotype | Samples |
|---|---|
| E0, diverse commensal | 7 (27 %) [src: ibd_phage_targeting] |
| E1, Bacteroides2 transitional | 11 (42 %) [src: ibd_phage_targeting] |
| E2, *Prevotella copri* enterotype | 0 [src: ibd_phage_targeting] |
| E3, severe Bacteroides-expanded | 8 (31 %) [src: ibd_phage_targeting] |

The distribution differs from uniform, with χ²(3) = 10.0 and p = 0.019. [src: ibd_phage_targeting]

## Method sensitivity

LDA on pseudo-counts is robust to the Kuehl-to-MetaPhlAn3 projection mismatch. It treats the 54 % of Kuehl feature rows outside the training feature space as not-detected. [src: ibd_phage_targeting]

GMM (Gaussian mixture model) on CLR (centered log-ratio) plus PCA (principal component analysis) is fragile under the same sparsity. It forced all 26 samples into E3 at confidence > 0.97, which the report calls an artifact, not biology. [src: discoveries, ibd_phage_targeting]

The ibd_phage_targeting classifier agreed with the metagenomic projection for only 41 % of these patients. [src: discoveries] It predicted E1 for 19/22 patients because its dominant learned rule was "IBD → E1 most of the time", the marginal mode among IBD training samples. [src: discoveries]

## Caveats

Kaiju was used rather than MetaPhlAn3, so Tier-A presence calls have lower confidence than in CMD analyses. [src: ibd_phage_targeting] This mismatch limits confidence in the UC Davis ecotype calls, and LDA is more trustworthy than GMM here. [src: ibd_phage_targeting]

## Related concepts

- [[concepts/gut-microbiome-ecotype-stability-and-cross-study-reproducibility]]
- [[concepts/cross-cohort-portability-and-batch-dominance-in-microbiome-and-metabolomic-stratification]]
- [[concepts/ecotype-aware-per-patient-phage-cocktail-design-and-state-dependent-dosing]]
