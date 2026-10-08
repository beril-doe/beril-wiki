---
type: "Concept"
description: "Whether clinical covariates or a small targeted qPCR panel can replace shotgun metagenomics for assigning gut samples to IBD ecotypes, and the evidence that they cannot yet."
sources: ["summaries/ibd_phage_targeting__REPORT.md"]
---
# Cheap Proxies Do Not Yet Substitute for Metagenomic Community-State Assignment

Assigning a sample to a community state (an "ecotype") currently requires shotgun metagenomics, and one project tested two cheaper candidate substitutes for that assignment: clinical covariates already recorded in the chart, and a small targeted qPCR (quantitative PCR of selected taxa) panel [src: ibd_phage_targeting]. The covariate route returned an explicit negative result and the qPCR route remains an unvalidated proposal [src: ibd_phage_targeting].

## Clinical covariates alone do not reproduce metagenomic calls

The reference labels under test were four reproducible IBD ecotypes derived from 8,489 cMD ([[entities/curatedmetagenomicdata]]) [[entities/metaphlan3]] samples; a classifier using clinical covariates passed AUC 0.80 in cross-validation but reached only 41 % agreement with metagenomics on UC Davis, and the report's revised reading is that metagenomics remains required [src: ibd_phage_targeting]. For what those strata are see [[concepts/gut-microbiome-ecotypes-as-patient-strata]], for how firmly they are delimited see [[concepts/ecotype-clustering-validity]], and for the project itself see [[summaries/ibd_phage_targeting__REPORT]].

The two headline numbers are not measured on the same scale, and the difference matters. The AUC figures are macro one-versus-rest (OvR: each ecotype scored against all others pooled) AUCs on pooled cross-validation — 0.799 for the minimal classifier on {`is_ibd`, `sex`, `age`} at n = 8,489 and 0.810 for the extended classifier on an n = 1,675 subset, both above the project's 0.70 threshold — whereas the 41 % is patient-level agreement (9/22) of the minimal classifier with the metagenomic call in the UC Davis cohort, against 36 % (8/22) for the extended classifier, with 12 / 22 patients disagreeing under both [src: ibd_phage_targeting]. Figure `NB03_h1c_auc.png` reports the per-ecotype OvR AUCs against that 0.70 threshold [src: ibd_phage_targeting].

The source attributes the failure to cohort structure, not to an unspecified modelling accident: the dominant learned rule is "`is_ibd = 1` → E1", and in UC Davis, which is all-CD so that `is_ibd` is constant, the rule collapses to the marginal mode and the minimal classifier predicts E1 for 19/22 patients [src: ibd_phage_targeting]. The project's verdict is therefore an explicit null — clinical-covariate-only ecotype assignment was judged nonviable [src: ibd_phage_targeting] — which **contradicts** any reading of the cross-validated AUC on its own as evidence that covariates suffice [src: ibd_phage_targeting].

Figure `NB03_feature_importance.png` compares classifier feature importance between the minimal and extended classifiers [src: ibd_phage_targeting]. Read beside the revised interpretation — that clinical covariates distinguish HC vs IBD trivially, dominated by `is_ibd`, but do not separate the IBD ecotypes E1 and E3 — such a comparison is diagnostic of where the signal sat rather than a route to assignment [src: ibd_phage_targeting].

Figure `NB02_ucdavis_ecotype_x_clinical.png` cross-tabulates UC Davis ecotype against Montreal location and against medication class [src: ibd_phage_targeting]. These are not the covariates used by the failed minimal classifier, which was trained on {`is_ibd`, `sex`, `age`}, so the 41 % patient-level agreement is not evidence about them; whether Montreal location or medication class carries per-patient ecotype information is not established by the figure description alone [src: ibd_phage_targeting].

## Targeted qPCR as a candidate cheaper proxy

The remaining proxy on the table is abundance-based rather than covariate-based: a proposed targeted qPCR ecotype panel of 4–6 species, named as *F. prausnitzii*, *P. copri* (prevotella copri), *P. vulgatus*, *B. fragilis* and *M. gnavus* ([[entities/mediterraneibacter-gnavus]]) [src: ibd_phage_targeting]. The panel is a design proposal in the report, not a validated assay [src: ibd_phage_targeting].

Its supporting observation is a single patient trajectory: the 14× *M. gnavus* expansion in patient 6967's E3 transition suggests the hypothesis that qPCR could substitute for full metagenomics in clinical follow-up, and validation requires a prospective cohort with paired qPCR + metagenomics across timepoints [src: ibd_phage_targeting]. Because the support is one patient and the stated scope is clinical follow-up, this is marked as a hypothesis rather than a finding [src: ibd_phage_targeting].

## Tensions

Within this one project the covariate classifier's two performance measurements point in opposite directions: macro OvR AUC 0.80 on pooled cross-validation clears the 0.70 threshold, while 41 % patient-level agreement with the metagenomic call on UC Davis does not, and the report resolves the gap by revising toward "metagenomics remains required" rather than by splitting the difference [src: ibd_phage_targeting]. The source's own account of the gap is that OvR AUC on a pooled cohort containing a strong cohort-axis feature overstates per-patient classifier usefulness [src: ibd_phage_targeting]. Both numbers are kept here exactly as stated, and because the discrepancy is internal to a single project it is recorded as a tension rather than promoted to a conflict page [src: ibd_phage_targeting].

## Open Directions

- Run the proposed 4–6-species qPCR panel (*F. prausnitzii*, *P. copri*, *P. vulgatus*, *B. fragilis*, *M. gnavus*) and metagenomics on the same specimens in a prospective cohort across timepoints, reporting per-patient agreement on the same footing as the 41 % (9/22) covariate figure — this closes the gap that the panel currently rests on a single patient's 14× *M. gnavus* expansion [src: ibd_phage_targeting].
- Refit the covariate classifier with an all-CD cohort held out before training rather than scored after pooled cross-validation, to test directly whether the AUC 0.80 / 41 % gap is fully accounted for by `is_ibd` becoming constant and predictions collapsing to E1 for 19/22 patients [src: ibd_phage_targeting].
- Test whether Montreal location and medication class — cross-tabulated in `NB02_ucdavis_ecotype_x_clinical.png` but absent from the minimal classifier's {`is_ibd`, `sex`, `age`} — carry per-patient ecotype signal within an all-CD cohort, and whether the covariates ranked in `NB03_feature_importance.png` retain importance once `is_ibd` is dropped [src: ibd_phage_targeting].
- Ask whether the individual panel species behave as per-patient markers under the criteria used in [[concepts/functional-marker-validation]], since a marker that tracks ecotype only in group averages would reproduce the covariate failure mode in which an E1-vs-E3 distinction is what goes missing [src: ibd_phage_targeting].
