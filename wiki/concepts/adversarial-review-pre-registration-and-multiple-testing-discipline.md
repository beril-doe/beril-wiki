---
type: "Concept"
description: "How adversarial versus standard review, post-hoc revisions, multiple-testing correction, exploratory versus confirmatory status and citation checks affect trust in conclusions; stops at the biology of any one project."
sources: ["summaries/amr_pangenome_atlas__REPORT.md", "summaries/clay_confined_subsurface__REPORT.md", "summaries/discoveries.md", "summaries/functional_dark_matter__REPORT.md", "summaries/gene_function_ecological_agora__REPORT.md", "summaries/ibd_phage_targeting__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md", "summaries/pitfalls.md", "summaries/plant_microbiome_ecotypes__REPORT.md"]
---
# Adversarial review, pre-registration and multiple-testing discipline

This page covers how adversarial versus standard review, post-hoc revisions, multiple-testing correction, exploratory versus confirmatory status and citation checks affect trust in conclusions. The strongest evidence is a paired comparison on one project, ibd_phage_targeting, where standard review found no critical issues and adversarial review found 5 critical and 6 important ones. [src: discoveries, ibd_phage_targeting] The other evidence comes from a few projects summarised in [[summaries/discoveries]], [[summaries/pitfalls]], [[summaries/amr_pangenome_atlas__REPORT]], [[summaries/clay_confined_subsurface__REPORT]], [[summaries/functional_dark_matter__REPORT]], [[summaries/gene_function_ecological_agora__REPORT]], [[summaries/microbeatlas_metal_ecology__REPORT]] and [[summaries/plant_microbiome_ecotypes__REPORT]]. In gene_function_ecological_agora, a family-wise correction pass found 14 of 16 formal tests surviving Bonferroni, and the two that did not were already reported as nulls. [src: gene_function_ecological_agora] In microbeatlas_metal_ecology, a primary confirmatory result survived both Bonferroni and FDR correction across a 47-test family, although the analysis was not preregistered. [src: microbeatlas_metal_ecology] In plant_microbiome_ecotypes, adversarial review led to replaced circular validations and a corrected effect-size formula. [src: plant_microbiome_ecotypes]

## Literature Context

Two candidate papers bear on this page, and both come from outside microbial biology. They are general statements about research practice, not studies of adversarial review. A review of developmental cognitive neuroscience argues that confidence in inferences depends on separating confirmatory from exploratory analysis [PMID 32759026](https://pubmed.ncbi.nlm.nih.gov/32759026/). For confirmatory work, it names three problems: analytic flexibility, how hypotheses are instantiated, and error-rate control when data are thresholded and corrected for multiple comparisons. As a counterweight, it recommends that exploratory work estimate and report effect sizes and use specification curve analyses. It also recommends transparent, reproducible null hypothesis significance testing [PMID 32759026](https://pubmed.ncbi.nlm.nih.gov/32759026/). Only the abstract was available, so the specific recommendations are not checked here.

A consensus position paper on transcranial direct current stimulation (tDCS) and motor learning makes a similar point from a different field. It reports that reproducibility remains to be fully tested and that effect sizes vary over a wide range [PMID 28231477](https://pubmed.ncbi.nlm.nih.gov/28231477/). It recommends that studies state in the Methods whether a design is exploratory (hypothesis-generating) or confirmatory (hypothesis-driven). It also recommends prospective pre-registration of hypothesis-based work, detailed method descriptions, and open data repositories [PMID 28231477](https://pubmed.ncbi.nlm.nih.gov/28231477/). This too is based on the abstract only.

The corpus's practices are **consistent with** this guidance. microbeatlas_metal_ecology labels its analyses confirmatory or exploratory. Its primary result also survives Bonferroni correction across the full 47-test family. The corpus also records that the labelling was done post-hoc and the plan was not preregistered, and it recommends preregistration in future. That matches the position paper's call for prospective pre-registration [PMID 28231477](https://pubmed.ncbi.nlm.nih.gov/28231477/). The same logic appears in the ENIGMA work, where null confirmatory tests were prioritised and positive results were framed as exploratory. The gene_function_ecological_agora family-wise pass enumerates test families and applies Bonferroni and FDR within each. This fits the neuroscience review's concern with error-rate control [PMID 32759026](https://pubmed.ncbi.nlm.nih.gov/32759026/). The corpus's admission that post-hoc metric revisions (M14, M21, M23) weaken pre-registration discipline is the analytic-flexibility problem that review describes.

The corpus **extends** this literature in places the candidates do not address. These include the paired comparison of standard and adversarial review on ibd_phage_targeting, where standard review found no critical issues and adversarial review found 5 critical and 6 important ones. They also include the documented fabricated and hijacked citations in reviewer output. Neither candidate speaks to these, so on these points the corpus is novel relative to the candidates. The paired comparison comes from a single project, so it is not evidence that the gap is general.

## Standard versus adversarial review

The standard reviewer, tools/review.sh, runs behind /berdl-review and /submit. It uses a find-strengths-and-suggestions framing inherited from its system prompt. [src: discoveries] On ibd_phage_targeting, it called the project methodologically exceptional, found no critical issues, and recommended proceeding to Pillars 3–5. [src: discoveries] Two independent standard runs on the pre-repair NB04 concluded "no critical issues". An adversarial reviewer with explicit "find flaws" framing found 5 critical and 6 important issues, all empirically confirmed by NB04b and NB04c. [src: ibd_phage_targeting] An adversarial review of the same files, with an explicit "find flaws, don't be diplomatic" framing, found 5 critical and 6 important issues. [src: discoveries]

The critical issues were these:
- Feature leakage in within-cluster differential abundance: samples were clustered on taxon abundances, then the same taxa were tested within clusters. [src: discoveries]
- Hard-coded "RESOLVED" verdict logic that treated nonsignificant results as positive evidence. [src: discoveries]
- No confounder adjustment, although the project cited Vujkovic-Cvijin 2020, which calls for it. [src: discoveries]
- A Jaccard of 0.14 reported as supporting H2b with no null distribution. [src: discoveries]
- An ecotype framework with 48.9 % cross-method agreement and no external replication. [src: discoveries]

The report judges the standard reviewer excellent at surface flaws: missing sections, undocumented dependencies, broken figures and simple statistical errors. It calls it appropriate for routine submissions. [src: discoveries] It calls the same reviewer systematically weak at structural and inferential problems, such as selection-on-outcome confounding, missing null distributions, post-hoc decision rules and narrative–evidence mismatch. [src: discoveries]

The report recommends that any project whose conclusions inform downstream decisions pair /berdl-review with a separately spawned adversarial reviewer. The two outputs should be reconciled before final synthesis. [src: discoveries] It proposes an optional --adversarial flag on /submit that would run both reviewers and produce a combined report. [src: discoveries] Standard review stays the right default for in-progress or iteration-mode work. [src: discoveries]

### Consequences of the review for the ibd_phage_targeting analysis

The original NB04 analysis, committed 2026-04-24 early, was superseded by a seven-notebook pipeline (NB04b to NB04h) after the adversarial review. [src: ibd_phage_targeting] The report retracts two of the three headline claims of that within-ecotype CD-vs-HC CLR Mann–Whitney analysis. (CD is Crohn's disease; CLR is centered log-ratio.) [src: ibd_phage_targeting] The two retractions were:
- The claim that within-ecotype stratification resolves the pooled-CLR CD↑ *C. scindens* result. The report instead uses a within-IBD-substudy CD-vs-nonIBD meta-analysis, which controls HC-study versus IBD-study nesting in cMD. [src: ibd_phage_targeting]
- The H2c paradox resolution. The NB04 within-ecotype "n.s." call was an artifact of feature leakage. With leave-one-species-out refitting, *C. scindens* is CD↑ in both E1 and E3. In the confound-free meta-analysis it has pooled CLR-Δ = +1.18, FDR = 1e-8 and 4/4 sign concordance across sub-studies. [src: ibd_phage_targeting]

Separately, the report withdrew the "Jaccard = 0.14 supports H2b" framing, because the value was near the random-overlap baseline and had no null distribution. The conclusion survives; the statistic did not. [src: ibd_phage_targeting]

One caveat limits the repaired analysis. The plan required at least 2 of 3 of ANCOM-BC, MaAsLin2 and LinDA to agree, but the implemented multi-method consensus is partial. [src: ibd_phage_targeting] The NB04c bootstrap-CI and NB04e within-substudy-meta outputs are extra evidence streams, not drop-in ANCOM-BC or MaAsLin2 substitutes. A full three-method R-native consensus remains a publication-grade follow-up. [src: ibd_phage_targeting]

### Plan revisions

The report presents the NB04 → NB04b-h rigor-repair arc as establishing this pairing for notebook commits. It says the v1.6 → v1.7 plan revision extends the pattern to plan revisions. [src: discoveries] The v1.6 plan was a careful Pillar 3 refresh written by an experienced agent. [src: discoveries] Adversarial inspection of the plan, report, failure analysis and mart parquet still found 4 critical and 10 important issues, structurally analogous to the NB04 failures. [src: discoveries] Among them:
- Feature leakage in the N14 dual-basis analysis, because the same-axis ecotype basis was leakage-poisoned. [src: discoveries]
- A "4-substudy meta-viable" claim inherited from NB04e without re-verification; the pathway data actually had 3+1. [src: discoveries]
- H3a thresholds set without null distributions. [src: discoveries]
- H3a-new mislabeled "butyrate-producer ↔ pathobiont", although 4 of 6 named anchors were not butyrate producers. [src: discoveries]

The discoveries digest generalizes the rule: a plan revision whose downstream notebooks will carry clinical, experimental or external claims should get both a standard and a paired adversarial review, because standard review mostly catches surface flaws and adversarial review catches structural and inferential ones. [src: discoveries] Its operational pattern is `tools/review.sh <project> --type plan` for the standard review and a general-purpose Agent with a find-flaws brief for the adversarial one, reconciled before notebook execution. [src: discoveries] It argues that catching issues at plan scope is cheaper: NB04 → NB04b-h took 7 notebooks, while v1.6 → v1.7 was a single plan-edit pass. [src: discoveries]

Features that adversarial review caught in both NB04 and v1.6, and standard review did not, were:
- Effect-size thresholds without null distributions (NB04: Jaccard 0.14; v1.6: |ρ| > 0.4). [src: discoveries]
- Substudy or cohort sample-size claims that did not match the data on inspection. [src: discoveries]
- Hypothesis labels that did not match the operationalized test; in NB04, "H2c RESOLVED" treated a nonsignificant result as positive. [src: discoveries]
- Same-axis feature leakage: NB04 clustered on taxa and tested taxa, and v1.6 stratified pathway differential abundance by pathway-feature ecotype. [src: discoveries]
- A falsifiability rule, "≤ 5 categories of 7", loose enough to pass under random allocation. [src: discoveries]

The report reads this pattern as mostly a failure of pre-registration discipline about actual sample sizes, null distributions and what each threshold means given that null. [src: discoveries] Two plan caveats of the same kind: H3b strain-adaptation collapses to species level on cMD by construction, and H3e has n=67 across 3 sites, not the 130-subject HMP2. [src: discoveries]

See [[concepts/substudy-nesting-and-feature-leakage-in-pooled-cohort-microbiome-comparisons]] for the leakage and nesting issues.

## Adversarial review in plant_microbiome_ecotypes

A paired adversarial review dated 2026-04-24 identified five issues that were only partly addressed in Phase 2b. The report says all five were closed on 2026-04-25. [src: plant_microbiome_ecotypes] Three of the issues were fixable and were resolved in notebooks NB13–NB15: the tautological genus-level validation, the original zero-hit Pfam query (documented as a limitation) and the NB12 subclade genome-ID mismatch. [src: plant_microbiome_ecotypes] NB08 reports twelve further analyses that address concerns raised in adversarial review. [src: plant_microbiome_ecotypes]

### Replaced or corrected analyses

Review led to several analyses being replaced rather than patched.
- The 92.7% genus-level agreement was circular, because cohorts are defined from marker presence. A curated panel of 18 model organisms with experimentally confirmed phenotypes (7 beneficial, 7 pathogenic, 4 neutral) replaces it. [src: plant_microbiome_ecotypes]
- The three-tier phylogenetic-control interpretation supersedes the earlier "9/17 survive L1" framing. [src: plant_microbiome_ecotypes]
- An earlier Phase 2b draft of the novel-OG (ortholog group) genome-size control used a prevalence-based Bernoulli simulation, which the paired review flagged as circular by construction. It was replaced by the real per-species OG matrix from NB03 and re-run. [src: plant_microbiome_ecotypes]
- The Phase 1 NB06 complementarity result of Cohen's d = −7.54 was largely a formula error. NB06 divided the mean difference by the SD of permutation means, which shrinks toward zero, when the correct denominator is the raw pair-level SD. [src: plant_microbiome_ecotypes]
- NB04's genus-level logistic-regression cell called bare `logit` although the import was `statsmodels.formula.api as smf`. It was rerouted to a markdown note pointing to NB14's cluster-robust GLM (generalized linear model) as the canonical answer, with the original code preserved. [src: plant_microbiome_ecotypes]

### Plan-versus-execution gaps

Four statistical controls specified in RESEARCH_PLAN.md but not run in Phase 1 were completed: C1, C4, I1 and within-genus label shuffling. [src: plant_microbiome_ecotypes] The report says these four planned-versus-executed gaps were closed in commit 8f9086e. It states that all four DESIGN-plan gaps are formally closed and the plan is fully reconciled with execution. [src: plant_microbiome_ecotypes] The originally planned NB13 (co-occurrence network expansion) was re-scoped to validation, Pfam and subclade fixes because review found higher-priority methodological issues. [src: plant_microbiome_ecotypes] The remaining NB13 sub-items are deferred as exploratory enhancements, and the H3 verdict does not depend on them. [src: plant_microbiome_ecotypes]

### Limits that remain

- The within-genus shuffle used n = 200 permutations, which is under-resolved for p ≤ 0.005, so the T3SS (type III secretion system) result is marginal. [src: plant_microbiome_ecotypes]
- No multiple-testing correction was applied across the 15 shuffle markers. A Bonferroni α = 0.0033 would demote T3SS but retain significance for nitrogen fixation and ACC (1-aminocyclopropane-1-carboxylate) deaminase. [src: plant_microbiome_ecotypes]
- The planned genus-level logistic-regression phylogenetic control for H1 was not completed because of the undefined `logit` import. The H1 compartment enrichments are therefore not phylogenetically controlled beyond the PERMANOVA (permutational multivariate analysis of variance) test itself. [src: plant_microbiome_ecotypes] The report documents the issue and uses PERMANOVA as the primary compartment-profiling test. [src: plant_microbiome_ecotypes]

## Pre-registration omissions and focused diagnostics

In gene_function_ecological_agora, three pre-registration omissions surfaced across Phases 1A and 1B and were corrected. [src: gene_function_ecological_agora] Each had the same structure: a criterion or framing that seemed well-grounded, data that did not behave as predicted, a post-hoc diagnostic showing the criterion and not the methodology was wrong, and a corrected criterion in the next phase. [src: gene_function_ecological_agora] The report's rule is to run a focused diagnostic first when a result deviates from pre-registered expectations, before invoking substrate, methodology or "we need more data" explanations. [src: gene_function_ecological_agora]

The diagnostics were cheap. NB04b (Phase 1A power analysis), NB08b (Phase 1B discrimination diagnostic) and NB08c (Phase 1B Sankoff diagnostic) took about 3 hours to write and ran in seconds to minutes. They distinguished metric or criterion problems from methodology failures. [src: gene_function_ecological_agora] The report says each saved the project from a wrong conclusion. [src: gene_function_ecological_agora]

The report also concedes a limit. Most revisions came from genuine biology engagement (M2 dosage cost, M14 Alm 2006 close-reading, M17 Pseudomonadota AMR bias) and not from data accommodation. Even so, the cumulative count indicates that pre-registration was insufficiently calibrated against substrate-resolution behavior. [src: gene_function_ecological_agora]

## Citation checks on reviewer output

Adversarial reviewers can themselves err, and the report documents this for gene_function_ecological_agora. In the fourth review, two critical findings trace to reviewer-side errors. [src: gene_function_ecological_agora] The missing-Alm-reference allegation arose because the reviewer's literature-scan subagent did not read `references.md` or hallucinated its absence. [src: gene_function_ecological_agora] Reviewer item I8, which compared a natural-expansion +64.5% above cohort with a recomputed +39.4%, is a phase-mixing error. [src: gene_function_ecological_agora] More broadly, one important finding rests on a fabricated citation, three critical findings restate concerns already addressed in REPORT v1.5–v1.8 and plan v2.7–v2.9, and two findings misframe defensible methodology. [src: gene_function_ecological_agora]

Across 9 adversarial review rounds in gene_function_ecological_agora, two citation failure modes appeared. [src: discoveries] The first is PMID-hijacking, where a PMID (PubMed identifier) points to an unrelated paper:
- In REVIEW_5, a Mendoza 2020 citation used PMID 32160912, which points to a Persian quality-of-life paper. [src: discoveries]
- In REVIEW_7, a Burch 2023 citation used PMID 37279472, which points to a COVID sense-of-coherence paper. [src: discoveries]

The report lists three reviewer-side fabrications: Mendoza 2020 at REVIEW_5, Koech 2025 at REVIEW_7 and the Burch 2023 PMID error at REVIEW_7. [src: gene_function_ecological_agora]

The Mendoza et al. 2020 "Hologenome evolution: mathematical model with horizontal gene transfer" citation (*Microbiome* 8:1) is identified as fabricated. [src: gene_function_ecological_agora] PubMed searches for "Mendoza Hologenome horizontal gene transfer" and for "Mendoza horizontal gene transfer regulatory metabolic mathematical model" each returned 0 results. [src: gene_function_ecological_agora] The citation carried a specific quantitative claim, that regulatory genes show 50-fold lower transfer rates than metabolic genes. The report rejects that claim as fabricated. It was the cornerstone of finding I1 and of the "partially supported" verdict for H1. (HGT is horizontal gene transfer.) [src: gene_function_ecological_agora] The report calls plausible-looking fabricated citations a stable failure mode of the adversarial_project.v1 prompt under standard depth. [src: gene_function_ecological_agora] It recommends treating all reviewer-cited papers that carry quantitative claims as needing PubMed verification before any project change is made on their basis. [src: gene_function_ecological_agora]

The second failure mode is author-list hallucination. In REVIEW_8/9, Burch 2023 was listed with "Dykhuizen DE" as an author. PubMed verification of DOI 10.1093/gbe/evad089 shows the authors are Burch CL, Romanchuk A, Kelly M, Wu Y and Jones CD. [src: discoveries]

Automatic DOI verifiers catch the PMID-hijack mode. Author-list hallucination needs manual PubMed article-metadata verification. [src: discoveries, gene_function_ecological_agora] Later rounds improved. Round 8 had severity 9, 7 citations, 0 fabrications and 7/7 DOIs auto-verified. [src: gene_function_ecological_agora] The report says reviewer quality improved monotonically: REVIEW_4/5/7 had fabricated citations verified via PubMed, and REVIEW_8 had 0 fabrications and 7/7 DOIs auto-verified. [src: gene_function_ecological_agora] The report calls REVIEW_8 its highest-quality round to date. [src: gene_function_ecological_agora] Round 9 had severity 9 and 8 citations, with 0 DOI fabrications and 1 author-list hallucination (Burch authors) carried over from the consolidator. [src: gene_function_ecological_agora]

The report's general rule is that a reviewer-cited paper carrying a load-bearing claim needs author, title, journal and PMID/DOI all verified through PubMed. A load-bearing claim is one that, if true, would substantially undermine a project finding. Checking only that the DOI resolves is not enough. [src: discoveries] The project-level memory for this is feedback_adversarial_verify_before_acting.md. [src: discoveries]

## Multiple testing and what counts as a test family

Projects handled correction differently. amr_pangenome_atlas applied no Bonferroni or FDR (false discovery rate) correction across the many tests under six hypotheses. It argued that the primary p-values were extreme (many < 1e-100) and correction would not change any conclusion. [src: amr_pangenome_atlas] It also says the per-gene and per-phylum tests are exploratory and hypothesis-generating. [src: amr_pangenome_atlas] clay_confined_subsurface treats marginal p-values, such as H1 within-Bacillota_B p=0.07, as descriptive. [src: clay_confined_subsurface]

Implementation can also defeat correction. In enigma_contamination_functional_potential, correction limited to columns ending in `_p` misses p-values such as `adj_cov_p_contamination` and `adj_frac_p_contamination`. [src: pitfalls] The recommended fix is to detect p-value columns by a substring pattern that excludes derived q-value columns, or by an explicit allowlist, before applying BH-FDR. [src: pitfalls] Denominators can mislead too: in conservation_fitness_synthesis, inconsistent core-percentage denominators caused a critical review issue because figures showed 86%/78% while prose said 82%/66%. [src: pitfalls]

### gene_function_ecological_agora

In gene_function_ecological_agora, a reviewer asked for family-wise correction across the M1–M26 methodology revisions. The report calls this a known category mistake: methodology transparency penalized as if it were multiple testing. It recommends enumerating the actual hypothesis-test families and applying Bonferroni within each, showing survival explicitly. [src: discoveries] The report says M1–M26 are not 26 independent tests on the same data. [src: gene_function_ecological_agora] They are mostly pre-registration corrections, such as M2 dosage biology added after the first review, or M14 Sankoff-parsimony replacing dispersion after the NB08c diagnostic. [src: discoveries, gene_function_ecological_agora] The report documents 25 revisions (M1–M25) in RESEARCH_PLAN.md with rationale and triggering observation. [src: gene_function_ecological_agora] Three are genuine post-hoc metric corrections on already-collected data: M14, M21 (strict-class housekeeping) and M23 (n_neg ≥ 20). [src: discoveries, gene_function_ecological_agora] Each was triggered by a failed diagnostic and reported with it. [src: gene_function_ecological_agora]

Limits on this defence are stated openly. Three pre-registration omissions were surfaced and corrected: M2 dosage biology, M12 absolute-zero criterion and M14 misreading of Alm 2006. [src: gene_function_ecological_agora] The report accepts that revising the negative-control criterion from "near zero" to "≤ 0 with CI not strongly positive" after seeing data weakens pre-registration discipline. [src: gene_function_ecological_agora] The dosage biology was anticipated, but its quantitative consequence, negative rather than zero producer z, was not put into the pre-registered criterion. [src: gene_function_ecological_agora] The reported p-values are not corrected specifically for the M14/M21/M23 changes. The report advises weighing effect size, ecological grounding and phenotype-anchor convergence rather than treating individual p-values as corrected. [src: gene_function_ecological_agora]

The NB30 correction pass enumerates formal significance claims, groups them into test families and applies family-wise Bonferroni and Benjamini-Hochberg FDR. [src: gene_function_ecological_agora] The real pre-registered family was 4 hypotheses, with Bonferroni α = 0.0125. NB12 mycolic-acid p<10⁻⁶, NB16 PSII (photosystem II) class p<10⁻⁵ and P4-D1 enrichments all p<10⁻¹¹ survive. [src: discoveries, gene_function_ecological_agora] All 4 pre-registered tests survive and keep their verdicts. [src: gene_function_ecological_agora]

| Family | Tests | Surviving Bonferroni |
|---|---|---|
| Pre-registered hypotheses | 4 | 4 (100%) [src: gene_function_ecological_agora] |
| P4-D1 biome enrichment | 6 | 5 (83%) [src: gene_function_ecological_agora] |
| P4-D5 residualization replication | 6 | 5 (83%) [src: gene_function_ecological_agora] |
| Total formal tests | 16 | 14 (88%) [src: gene_function_ecological_agora] |

The non-surviving tests are the Mycobacteriaceae × soil result ("0.88× — NOT enriched") and the NB11 regulatory-versus-metabolic null, which the project reframed toward a small-effect complexity hypothesis. Both were already reported as nulls, not false positives. [src: gene_function_ecological_agora] Two layers are descriptive, so no correction applies: leaf_consistency is a point estimate, with medians mycolic 0.15, PSII 0.88 and PUL (polysaccharide utilization locus) 0.41, [src: gene_function_ecological_agora] and tree-based donor inference is an exploratory classification under plan v2.16. [src: gene_function_ecological_agora]

## Confirmatory and exploratory status in microbeatlas_metal_ecology

This project labels its analyses as confirmatory or exploratory, but its analysis plan was not preregistered, and the confirmatory/exploratory distinction was documented post-hoc. [src: microbeatlas_metal_ecology] The primary confirmatory result survives the corrections described below, while several robustness results do not. The report recommends that future studies preregister the primary hypothesis, analysis plan and sample size before collecting data. [src: microbeatlas_metal_ecology]

The primary confirmatory hypothesis asks whether metal AMR (antimicrobial resistance) trait diversity predicts bacterial niche breadth after phylogenetic correction. It was tested before residuals and interaction effects were examined. [src: microbeatlas_metal_ecology] The confirmatory analyses are the 6 simple PGLS (phylogenetic generalized least squares) models in NB05 with Bonferroni correction, plus Pagel's λ for niche and AMR traits in NB04. [src: microbeatlas_metal_ecology] The report says the robustness analyses were run after the main analysis, in response to anticipated reviewer concerns. Readers should take them as reassurance, not confirmatory evidence. [src: microbeatlas_metal_ecology] It also says the five robustness analyses only partially address its main caveats. [src: microbeatlas_metal_ecology] All robustness and sensitivity analyses are labelled exploratory, and the primary confirmatory result (6 PGLS plus Bonferroni) stands independently. [src: microbeatlas_metal_ecology] The archaeal PGLS results were moved to a Supplementary section, with only a summary pointer left in the main robustness section. [src: microbeatlas_metal_ecology]

The multiple-testing inventory lists these families:

| Family | Tests | Correction |
|---|---|---|
| Simple PGLS (confirmatory) | 6 | Bonferroni (α/6 = 0.0083) [src: microbeatlas_metal_ecology] |
| Pagel's λ (confirmatory) | 6 | LRT (likelihood ratio test), no additional correction [src: microbeatlas_metal_ecology] |
| Multi-predictor PGLS | 3 predictors in 1 model | not corrected beyond model [src: microbeatlas_metal_ecology] |
| Robustness R1–R2, R4–R6 | 9 coefficients | exploratory only [src: microbeatlas_metal_ecology] |
| Archaeal PGLS R3 (supplementary) | 3 coefficients | exploratory only [src: microbeatlas_metal_ecology] |
| Sensitivity S1–S5 | 24 coefficients | exploratory only [src: microbeatlas_metal_ecology] |
| OTU abundance filter S5 (Pagel's λ) | 1 | exploratory only [src: microbeatlas_metal_ecology] |

The primary confirmatory result (metal types → B_std, p = 1.5×10⁻⁴, Bonferroni-corrected) stands regardless of the robustness analyses. [src: microbeatlas_metal_ecology] It also survives a Bonferroni correction for the full 47-test family (threshold 0.05/47 ≈ 0.0011). That was not the stated correction method, but the report treats it as an upper bound on conservatism. [src: microbeatlas_metal_ecology] At q < 0.05, 23 of 47 tests are significant. [src: microbeatlas_metal_ecology] The full FDR table is supplied in data/all_tests_fdr.csv. [src: microbeatlas_metal_ecology]

Across 606 bacterial genera, simple PGLS (B_std ~ metal_types_z) gave metal-types β = +0.0215 (SE = 0.0056, p = 1.5×10⁻⁴, BH-FDR q = 0.003). [src: microbeatlas_metal_ecology] Multi-predictor PGLS gave β = +0.0231 (SE = 0.0067, p = 5.5×10⁻⁴, BH-FDR q = 0.004). [src: microbeatlas_metal_ecology] Both are significant after BH-FDR adjustment. [src: microbeatlas_metal_ecology]

The bacterial metal-type-diversity effect survives FDR in these models:
- Simple PGLS B_std, q = 0.0028. [src: microbeatlas_metal_ecology]
- Multi-predictor PGLS, q = 0.0037. [src: microbeatlas_metal_ecology]
- R1 covariate models, q < 0.004. [src: microbeatlas_metal_ecology]
- R5 genome size covariate, q = 0.0028. [src: microbeatlas_metal_ecology]
- 3-covariate PGLS, q = 0.0028. [src: microbeatlas_metal_ecology]
- S3 within-genus SD (standard deviation), q = 0.007. [src: microbeatlas_metal_ecology]
- S4 log(n_species), q = 0.0037. [src: microbeatlas_metal_ecology]

Some results do not survive, and these limit the robustness claim. The S2 leave-one-environment-out models are significant at q < 0.05 for 12 of 13 environments. [src: microbeatlas_metal_ecology] The exception is excluding aquatic environments: q = 0.061, nominally significant at p = 0.031. [src: microbeatlas_metal_ecology] The S1 leave-one-metal-out models do not survive FDR, which the report attributes to reduced predictor variance when one metal is excluded. [src: microbeatlas_metal_ecology] The archaeal PGLS stays non-significant (q = 0.55). [src: microbeatlas_metal_ecology] The report also states that its cross-sectional design cannot distinguish 3 causal-direction scenarios, so causal phrasing was removed from Key Findings and Interpretation. [src: microbeatlas_metal_ecology] See [[concepts/robustness-and-replication-of-niche-breadth-associations]] and [[concepts/metal-resistance-repertoire-breadth-and-ecological-niche-breadth]].

## Partial null controls in functional_dark_matter

functional_dark_matter shows how partial null controls bound a claim. The plan had 7 condition–environment mappings, [src: functional_dark_matter] and the implementation used 6: stress (metal, osmotic and oxidative consolidated), carbon source, nitrogen source, pH, motility and anaerobic. [src: functional_dark_matter] Stress was consolidated because the Fitness Browser (FB) expGroup field only records broad stress. [src: functional_dark_matter] Motility and anaerobic were added because they were prominent among dark genes with strong fitness effects. [src: functional_dark_matter] This is a plan departure that readers should see.

For the NMDC (metagenome) validation, NB10 gave partial null approximations. A sign test on 7/7 pre-registered trait directions gave p = 0.0078, and on 4/4 abiotic directions p = 0.0625. [src: functional_dark_matter] Fisher's combined probability over all 11 pre-registered tests gave p ≈ 0. [src: functional_dark_matter] Exploratory tests showed an inflation factor of ~20× (441/449 significant vs. 22.5 expected), which quantifies compositional coupling. [src: functional_dark_matter] Equivalent null controls were not run for the biogeographic and lab-field concordance analyses. [src: functional_dark_matter] A full annotated-accessory-gene null through the biogeographic pipeline would strengthen the H0 rejection but needs Spark carrier-genome queries. [src: functional_dark_matter]

Lab-field concordance is weaker. A binomial test of 29/47 against p = 0.5 gave one-sided p = 0.072, with Wilson score 95% CI [0.474, 0.742], marginally above chance. [src: functional_dark_matter] The CI includes 0.50. [src: functional_dark_matter] Fisher's combined probability over all 47 individual tests gave p = 0.031, which the report calls stronger aggregate evidence of non-random concordance. [src: functional_dark_matter] See [[concepts/concordance-between-laboratory-fitness-phenotypes-and-field-environments-of-gene-carriers]] and [[concepts/compositional-coupling-in-metagenomic-validation-of-carrier-abundance]].

## Confirmatory and exploratory labelling in ENIGMA

In ENIGMA NB03, confirmatory and exploratory tests were labelled explicitly. Global BH-FDR (Benjamini-Hochberg false discovery rate) was applied across all reported p-values. Confirmatory genus-level defense Spearman tests stayed null (p=0.546/0.483; q=0.862/0.849). [src: discoveries] The strongest surviving signal was exploratory: the relaxed coverage-adjusted defense model kept q=0.046. [src: discoveries] Strict and other sensitivity signals attenuated above q<0.1. [src: discoveries] The report therefore advises prioritizing null confirmatory evidence and framing positive results as exploratory. [src: discoveries]

Re-testing the confirmatory defense endpoint under four contamination-index constructions gave no significant association after FDR correction (all q=0.546 across 8 confirmatory-variant tests). The constructions were all-metals composite, uranium-only, top-3 variance metals and PCA-PC1. [src: discoveries] The report concludes the null is not an artifact of one index formulation. [src: discoveries] See [[entities/enigma]] and [[concepts/robustness-of-exploratory-associations-to-coverage-fraction-and-site-covariate-specification]].

## Withdrawn results and degenerate verdicts

Corrections should be declared openly. The clay_confined_subsurface correction notice says the H3 iron-reduction analysis used misidentified markers. It compared anchor_deep (1/9 IR-positive) with anchor_shallow (15/30). [src: clay_confined_subsurface] Before correction, the report had claimed 3.7-fold IR (iron reduction) enrichment in shallow clay against the broader soil baseline (p=0.0025). The marker correction invalidates this. [src: clay_confined_subsurface] The narrative that the clay cohort diverges from the Mitzscherling rock-attached community because shallow clay is IR-rich is withdrawn. [src: clay_confined_subsurface] See [[concepts/reliability-of-kegg-ortholog-markers-for-multi-heme-cytochrome-iron-reduction]].

A failing verdict can also come from the test design. In ibd_phage_targeting, the NB07a H3a (b) test gave opposite verdicts under different category schemas, with identical differential-abundance outputs, statistical test and nulls. [src: discoveries] Under v1.7, regex categorization into 7 a-priori IBD categories matched 44 of 409 prevalence-filtered pathways. [src: discoveries] Only 3 of 52 CD-up pathways fell in that set. [src: discoveries] The "≤ 3 of 7 categories" test was structurally degenerate, with the null also at 100 % top-3, and gave a FAIL verdict. [src: discoveries]

The v1.8 schema used a MetaCyc class hierarchy with a 12-theme IBD overlay. [src: discoveries] There, 357/409 (87 %) of pathways had class data [src: discoveries], and 262/409 (64 %) were assigned to at least one theme. [src: discoveries] Per-theme Fisher's exact tests with BH-FDR across 12 themes were used. [src: discoveries] Iron/heme acquisition was the dominant CD-up theme (OR = 8.1, FDR 7e-6; 15 of 52 CD-up pathways), which supported H3a (b). [src: discoveries] The report says v1.7 missed this because regex on the name of PWY-5920 did not match "iron". [src: discoveries] The v1.7 "0_other" bucket hid 15+ heme/iron pathways. [src: discoveries] The report's lesson is that a "structurally degenerate" verdict was technically correct for v1.7 but is not a scientific refutation. It is an invitation to fix the schema. [src: discoveries] See [[concepts/ontology-versus-name-pattern-categorization-in-pathway-enrichment-tests]] and [[entities/metacyc-pathway-class-hierarchy]].

## Tensions

- The count of adversarial review rounds differs within gene_function_ecological_agora. One statement says 8 adversarial review rounds were integrated. [src: gene_function_ecological_agora] Another refers to 9 adversarial review rounds, including REVIEW_9. [src: discoveries, gene_function_ecological_agora]
- Post-hoc revision is defended and conceded at once. The report says most revisions came from biology engagement and not data accommodation. [src: gene_function_ecological_agora] It also says the cumulative count shows pre-registration was insufficiently calibrated. [src: gene_function_ecological_agora]
- microbeatlas_metal_ecology calls its confirmatory result independent of the robustness analyses, yet its analysis plan was not preregistered. [src: microbeatlas_metal_ecology]
- plant_microbiome_ecotypes reports that all five adversarial-review issues were closed, yet it also reports that H1 lacks the planned phylogenetic control and that the 15-marker shuffle had no multiple-testing correction. [src: plant_microbiome_ecotypes]

## Open Directions

- Run paired standard and adversarial reviews on several more projects, and record issue counts by type. This would show whether the gap on ibd_phage_targeting is typical.
- Add a PubMed metadata check (author, title, journal, PMID/DOI) as an automated step for reviewer-cited, load-bearing papers. This targets the author-list hallucinations that DOI checks miss.
- For amr_pangenome_atlas, compute FDR-adjusted q-values for the per-gene and per-phylum tests. This would test the claim that correction changes no conclusion, and it would show which exploratory tests survive.
- Log every post-hoc metric change, as in M14, M21 and M23, in a registry separate from pre-registration corrections. Test families could then be enumerated automatically.
- Re-run other degenerate or FAIL verdicts under an ontology-based schema. This would show how many are schema artefacts, as with v1.7 versus v1.8.
- Run null controls for functional_dark_matter's biogeographic and lab-field concordance analyses, as NB10 did for NMDC. This would test whether the marginal 29/47 result exceeds chance once compositional coupling is controlled.
- Re-run the gene_function_ecological_agora M14/M21/M23 metrics with the original and revised definitions side by side. This would show how much those post-hoc changes moved the p-values.
- Repeat the microbeatlas_metal_ecology metal-diversity test on a held-out or newly collected dataset with the hypothesis and analysis plan preregistered. This would turn the post-hoc confirmatory label into a true confirmation.
- Complete the three-method R-native differential-abundance consensus (ANCOM-BC, MaAsLin2, LinDA) for ibd_phage_targeting. This would close the partial-consensus gap.
- Re-run the plant_microbiome_ecotypes within-genus shuffle with many more permutations and a correction across all 15 markers. This would settle whether T3SS survives.
- Add a column-detection check to multiple-testing code so that all p-value columns are corrected. This would prevent the enigma_contamination_functional_potential miss.
