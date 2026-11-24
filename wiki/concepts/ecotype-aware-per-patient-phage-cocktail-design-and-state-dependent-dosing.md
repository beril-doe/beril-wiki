---
type: "Concept"
description: "How target lists are turned into per-patient cocktail drafts for a small Crohn's cohort, including hybrid phage plus non-phage strategies, longitudinal ecotype drift and dosing rules; covers the limits of an n=1 trajectory and untested clinical thresholds."
sources: ["summaries/ibd_phage_targeting__REPORT.md"]
---
# Ecotype-aware per-patient phage cocktail design and state-dependent dosing

This page covers ecotype-aware per-patient phage cocktail design and state-dependent dosing. The evidence is exploratory: the cohort has 23 patients and the drift rule rests on one patient. [src: ibd_phage_targeting] See also [[summaries/ibd_phage_targeting__REPORT]] and [[entities/uc-davis-kuehl-wgs-crohn-s-disease-cohort]].

## Literature Context

The candidate papers establish AIEC (adherent-invasive E. coli) as the best-developed phage target in Crohn's disease (CD). Reviews describe AIEC adhesion to epithelial cells via FimH and CEACAM6, survival in macrophages, and links between AIEC and disease location, activity and postoperative recurrence [PMID 29141957](https://pubmed.ncbi.nlm.nih.gov/29141957/) [PMID 36405271](https://pubmed.ncbi.nlm.nih.gov/36405271/). They list phage therapy among several strategies, alongside antibiotics, anti-adhesive molecules and ecological restoration [PMID 42472818](https://pubmed.ncbi.nlm.nih.gov/42472818/). Broader reviews describe phage therapy in gastroenterology as having a favourable safety profile, with trials in CD described as ongoing [PMID 31696976](https://pubmed.ncbi.nlm.nih.gov/31696976/) [PMID 37770177](https://pubmed.ncbi.nlm.nih.gov/37770177/) [PMID 32947790](https://pubmed.ncbi.nlm.nih.gov/32947790/).

The primary studies are preclinical. A three-phage cocktail reduced LF82 AIEC in CEABAC10 transgenic mice and reduced DSS-induced colitis symptoms in conventional LF82-colonised mice. It also targeted LF82 in ileal biopsy homogenates from CD patients [PMID 28130329](https://pubmed.ncbi.nlm.nih.gov/28130329/). A seven-phage cocktail (EcoActive) was effective in vitro against 95% of 210 clinical AIEC strains and lysed none of 43 non-E. coli commensal strains. In mice, a single administration failed to alleviate inflammation, while dosing twice a day for 15 days protected against it [PMID 35997152](https://pubmed.ncbi.nlm.nih.gov/35997152/). Phage HER259 improved colitis in gnotobiotic and CD-microbiota models by switching off FimH through fimS promoter inversion. Colitis reactivated when treatment was withdrawn, and the phage enhanced the effect of subtherapeutic budesonide [PMID 42418560](https://pubmed.ncbi.nlm.nih.gov/42418560/). These findings are from animal and ex vivo work.

The corpus's E. coli component is consistent with this literature. Its NB13 5-phage E. coli cocktail for AIEC matches the multi-phage cocktail approach, and its hybrid strategy fits the reviews' framing of phage as one pillar among several [PMID 42472818](https://pubmed.ncbi.nlm.nih.gov/42472818/). The preclinical dose-dependence (single versus repeated dosing) and the reversion after withdrawal [PMID 35997152](https://pubmed.ncbi.nlm.nih.gov/35997152/) [PMID 42418560](https://pubmed.ncbi.nlm.nih.gov/42418560/) give indirect support to the idea of state-dependent, repeated dosing. They do not test the corpus's ecotype-drift rule, which rests on one patient (6967) and an untested 5-fold M. gnavus qPCR trigger.

Several corpus claims extend or sit outside the candidate papers. The papers frame AIEC as a prominent CD pathobiont. The corpus finds E. coli in only 8 of 23 patients (35%), so the E. coli cocktail applies to a minority. It also finds no patient-specific AIEC strain diagnostic, and the candidate papers do not address this. They contain nothing on the other parts of the hub: the H. hathewayi and F. plautii phage gaps, bile-acid-coupled design, M. gnavus, the calprotectin threshold of 250 μg/g, and ecotype-based per-patient drafts. These remain novel and exploratory, with no support or contradiction from the retrieved literature. The one adjunct finding, HER259 with budesonide [PMID 42418560](https://pubmed.ncbi.nlm.nih.gov/42418560/), suggests that combining phage with non-phage therapy is plausible, but it is a mouse result.

## Cohort and profile inputs

The framework profiles 23 UC Davis CD patients by ecotype, Montreal classification, calprotectin, medication and Kuehl_WGS Tier-A presence. [src: ibd_phage_targeting] Concrete cocktail drafts were produced for 14 of 23 patients (61 %). [src: ibd_phage_targeting] The cohort is small, so the drafts are exemplars or templates, not statistically robust per-patient validation. [src: ibd_phage_targeting] Generalization needs validation in external CD cohorts and multi-center data. [src: ibd_phage_targeting]

Kuehl_WGS used Kaiju rather than MetaPhlAn3, so Tier-A presence calls have lower confidence than CMD analyses. [src: ibd_phage_targeting] Patient 1112's resequencing replicates gave Spearman ρ = 1.000 (p < 0.001) on 6 Tier-A targets. The report treats this as validating Kaiju reliability and the technical-noise floor. [src: ibd_phage_targeting] That is a technical replicate, not a biological-replicate trajectory. [src: ibd_phage_targeting]

## Why the cocktail must be hybrid

All 9 E1 patients carry the full 5-species Tier-A pathobiont module. [src: ibd_phage_targeting] Only 3 of the 5 species have direct lytic phage options: [[entities/escherichia-coli|E. coli]], E. bolteae and E. lenta, when present. [src: ibd_phage_targeting] H. hathewayi and F. plautii are phage gaps. A pure phage cocktail is therefore infeasible for any E1 patient. [src: ibd_phage_targeting]

The report proposes a 3-strategy hybrid:
1. Direct phages for E. coli AIEC (adherent-invasive E. coli), E. bolteae PMBT24 and E. lenta PMBT5.
2. Alternative therapies: H. hathewayi enzyme inhibitors and F. plautii bile-acid-binding co-therapy.
3. Limited or engineered approaches for M. gnavus. [src: ibd_phage_targeting]

F. plautii is present in 78 % of patients, including all 9 E1 patients. [src: ibd_phage_targeting] The report calls its bile-acid-coupling cost the dominant E1 design constraint. It combines the highest coupling cost with a phage gap, so the report deprioritizes the species and adds ursodeoxycholic acid (UDCA) or a bile-acid-binding agent. [src: ibd_phage_targeting] No per-patient bile-acid measurements exist, so this cost is assigned at ecotype level. [src: ibd_phage_targeting]

E. coli is present in only 8 of 23 patients (35 %). The report contrasts this with the literature framing of AIEC as the prototypical CD pathobiont. [src: ibd_phage_targeting] The NB13 5-phage cocktail (DIJ07_P2, LF73_P1, AL505_Ev3, 55989_P2, LF110_P2) is directly applicable to about 35 % of patients. [src: ibd_phage_targeting] Another statement gives this as ~8/23. [src: ibd_phage_targeting] H. hathewayi (universal 83 %) and M. gnavus (universal 91 %) are phage gaps and the unmet need. [src: ibd_phage_targeting] The report ranks external database queries (INPHARED, IMG/VR) for their lytic phages above further E. coli cocktail refinement. [src: ibd_phage_targeting] The 8 E. coli-positive patients have no patient-specific AIEC strain diagnostic. Recommendations assume AIEC subset prevalence from Dogan 2014. [src: ibd_phage_targeting]

## Strategy distribution

The operational distribution is 12 reserve, 4 E1 hybrid, 4 E0 limited, 1 E1 full, 1 E3 and 1 state-dependent. It should be revisited in a larger CD cohort. [src: ibd_phage_targeting]

| Category | Patients | Content |
|---|---|---|
| Reserve for flare (C) | 12 | No active cocktail; calprotectin monitoring plus M. gnavus qPCR [src: ibd_phage_targeting] |
| E1 hybrid, no E. coli | 4 | PMBT24, PMBT5, alternatives for H. hathewayi, F. plautii and M. gnavus, UDCA/bile-acid-binding [src: ibd_phage_targeting] |
| E0 limited (priority targets are gaps) | 4 | Limited cocktail; consider non-phage strategies [src: ibd_phage_targeting] |
| E1 hybrid, full with E. coli AIEC | 1 | NB13 5-phage E. coli, PMBT24, PMBT5, alternatives, UDCA [src: ibd_phage_targeting] |
| E3 focused, with E. coli | 1 | NB13 5-phage E. coli, PMBT5, alternatives [src: ibd_phage_targeting] |
| State-dependent dosing | 1 | Patient 6967: cocktail rebalances on E1↔E3 shifts [src: ibd_phage_targeting] |

The 12 quiescent patients (calprotectin < 250 or unmeasured) get the same Tier-A panel as a reserve for flare, not an active cocktail. [src: ibd_phage_targeting] The 250 μg/g threshold is a clinical convention, not validated against per-patient response. [src: ibd_phage_targeting] Some patients at 41–248 μg/g, now classed quiescent, may benefit from an active cocktail. The threshold should be re-evaluated in a pilot. [src: ibd_phage_targeting]

## Longitudinal drift and state-dependent dosing

Patient 6967 is the only multi-timepoint UC Davis patient with biological replicates. The patient shows E1→E3 ecotype drift across 2 visits. The dominant signature is a 14× M. gnavus expansion (0.53 → 7.45 reads). [src: ibd_phage_targeting] Cocktail Jaccard between visits is 0.60. [src: ibd_phage_targeting] The report reads this as moderate overlap: non-trivial redesign, not a complete rewrite. [src: ibd_phage_targeting] Three targets are shared: H. hathewayi, M. gnavus and E. lenta, the universal Tier-1 trio. Two are visit-1-only and E1-specific: E. bolteae and F. plautii. [src: ibd_phage_targeting]

The dosing framework has 5 rules. It re-tests ecotype every 3-6 months. [src: ibd_phage_targeting] It uses the Tier-1 trio as backbone for any active-disease patient. [src: ibd_phage_targeting] It makes F. plautii E1-specific, dropped on E1→E3. [src: ibd_phage_targeting] It makes E. coli E3-specific, subject to AIEC strain detection. [src: ibd_phage_targeting] It proposes M. gnavus qPCR as a cheap proxy, with a 5-fold change triggering a full ecotype re-test. [src: ibd_phage_targeting]

### Limits

- All drift conclusions rest on n=1. [src: ibd_phage_targeting] The rule is a hypothesis for prospective validation, not established clinical practice. [src: ibd_phage_targeting]
- Visit confidences were 0.64 and 0.41, so the ecotype shift could partly reflect classifier uncertainty. The 14× M. gnavus and 3× E. lenta expansions are quantitative observations independent of the label. [src: ibd_phage_targeting]
- The time between the 2 visits is unknown, which limits timing recommendations. [src: ibd_phage_targeting]
- The 5-fold qPCR trigger comes from one trajectory. [src: ibd_phage_targeting] Validating it needs a prospective cohort with paired qPCR and metagenomics across timepoints. [src: ibd_phage_targeting]

## Can routine data assign ecotype?

A classifier using HC/IBD status, sex and age reached macro AUC 0.80 in pooled cross-validation. Patient-level agreement with the UC Davis metagenomic projection was only 41 %. [src: ibd_phage_targeting] It collapses to "IBD → E1" because is_ibd is constant in an all-CD cohort. Metagenomics is still required for patient-level ecotype assignment. [src: ibd_phage_targeting]

## Open Directions

- Run a prospective cohort with serial samples, paired M. gnavus qPCR and metagenomics. This would test the 5-fold trigger and the n=1 drift rule, and give visit timing.
- Query INPHARED and IMG/VR for H. hathewayi and M. gnavus lytic phages, to close the phage gaps behind the hybrid design.
- Add AIEC strain-resolution diagnostics for E. coli-positive patients, to test the assumed AIEC prevalence.
- Measure per-patient bile acids, to replace the ecotype-level F. plautii cost.
- Compare calprotectin cutoffs around 250 μg/g against pilot clinical response.
- Replicate the strategy distribution in a larger multi-center CD cohort.
