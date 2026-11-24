---
type: "Summary"
description: "Summary of the project Discoveries Log."
doc_type: "short"
full_text: "sources/discoveries.md"
---
# Discoveries Log

This page summarises one entry in the Discoveries Log, the cross-project digest of findings. The entry comes from the ibd_phage_targeting project. It asks whether the choice of category schema, not the biology, decided a test of inflammatory bowel disease (IBD) pathway enrichment. The answer is yes. The same differential-abundance outputs, statistical test and nulls gave opposite verdicts under two schemas. [src: discoveries] The evidence is direct, from one project and one test, and the report turns it into a general rule. [src: discoveries]

## Key Findings

### The verdict flipped with the category schema

The NB07a H3a (b) test asked whether Crohn's disease (CD)-up pathways concentrate in IBD-mechanism themes. A regex schema and a curated-hierarchy schema gave opposite answers. [src: discoveries] The v1.8 schema supported the hypothesis, and the v1.7 schema failed it as structurally degenerate. [src: discoveries]

### v1.7: regex on pathway names failed

- The v1.7 schema used regex on descriptive pathway names. Seven a-priori IBD categories matched 44 of 409 prevalence-filtered pathways. [src: discoveries]
- Only 3 of the 52 CD-up pathways fell in the 7-category set. [src: discoveries]
- The "≤ 3 of 7 categories" test was structurally degenerate, because the null was also at 100 % top-3. The verdict was FAIL: H3a (b) "not supported, structurally degenerate". [src: discoveries]
- The report says regex on "PWY-5920: superpathway of heme biosynthesis from glycine" does not match "iron". That is why v1.7 missed iron biology. [src: discoveries]
- The v1.7 "0_other" bucket hid 15+ heme/iron pathways. [src: discoveries]

### v1.8: a curated hierarchy supported the hypothesis

- v1.8 used the MetaCyc class hierarchy from ModelSEEDDatabase MetaCyc_Pathways.tbl, with a 12-theme IBD overlay. [src: discoveries]
- 357/409 (87 %) of pathways had MetaCyc class data. [src: discoveries] 262/409 (64 %) were assigned to at least one IBD theme. [src: discoveries]
- The test was a per-theme Fisher's exact test (CD-up × in-theme), with Benjamini-Hochberg false discovery rate (BH-FDR) correction across 12 themes. [src: discoveries]
- MetaCyc places PWY-5920 under HEME-SYN, Heme-b-Biosynthesis, Cofactor-Biosynthesis and Tetrapyrrole-Biosynthesis. [src: discoveries]
- Iron/heme acquisition was the dominant CD-up theme (odds ratio 8.1, FDR 7e-6; 15 of 52 CD-up pathways). The verdict was SUPPORTED. [src: discoveries]
- The report describes a four-way convergence: the iron/heme enrichment, NB05 *E. coli* Yersiniabactin/Enterobactin MIBiG matches, NB07a attribution of heme biosynthesis to *E. coli*, and the adherent-invasive *E. coli* (AIEC) iron-acquisition literature. [src: discoveries]

### The generalizable rule

For any pathway, gene or metabolite category-enrichment test, the report prefers a curator-validated ontology or class hierarchy over name-pattern regex when one exists. Regex becomes a sensitivity check. This is now plan norm N17 in ibd_phage_targeting. [src: discoveries] ModelSEEDDatabase ships a usable MetaCyc hierarchy with 90 %+ coverage of HUMAnN3 outputs. [src: discoveries] The report names KEGG BRITE and the Gene Ontology (GO) biological-process subontology as analogous resources for KEGG/EC-level data. [src: discoveries]

## 2026-04: [ibd_phage_targeting] Cross-cohort m/z-bridge metabolomics requires explicit …

### Acquisition-depth signatures in gene_function_ecological_agora

M22 Sankoff parsimony attributed 17M gain events on the GTDB-r214 species tree to 5 acquisition-depth bins: recent, older_recent, mid, older and ancient. [src: discoveries] The recent-to-ancient ratio then separated function classes. CRISPR-Cas had a 24.5× ratio, described as an HGT-active signature. [src: discoveries] Strict housekeeping functions (RNAP core, tRNA-synth, ribosomal) had a ratio of ~1×, described as vertical inheritance. [src: discoveries] Mixed regulatory-plus-metabolic KOs had 2× the Innovator-Exchange rate of pure regulatory or pure metabolic KOs. [src: discoveries] The report treats the per-class ratio as a substantive measure of vertical-versus-horizontal dominance at full bacterial-tree scale, separate from any pre-registered hypothesis test. [src: discoveries] An independent leaf_consistency analysis (LC, the per-(rank × clade × KO) fraction of species carrying the KO) agreed. The fraction fell monotonically across depth bins, from recent 0.34 to ancient 0.20. [src: discoveries]

### Mycolic acid: a population mixture

The family-rank Mycobacteriaceae × mycolic-acid producer-side Cohen's d was d=0.31, supporting H2 Innovator-Isolated. [src: discoveries] Leaf consistency complicated this. Mycolic-acid KOs in Mycobacteriaceae had median LC=0.15, below the atlas reference of 0.20. [src: discoveries] The report reads this as gain events landing in clades where only ~15% of family members carry the KO panel. [src: discoveries] Restricting to the mycolic-positive sub-clade (10 of 13 genera with mean LC ≥ 0.5) raised producer d to +0.394, against +0.309 at family rank. [src: discoveries] The report's rule is that a supported clade-level finding with low within-clade leaf consistency may be a mixture of positive sub-clades and negative members. Sub-clade-restricted recomputation then sharpens the claim. [src: discoveries]

### Convergent evidence across substrates

For the pre-registered mycolic, PSII and Bacteroidota PUL findings, three independent substrates agreed. These were atlas Cohen's d on Sankoff-derived scores, clade-by-biome Fisher's enrichment (p<10⁻¹¹), and BacDive metabolic phenotypes where coverage existed. [src: discoveries] The report argues this makes a clade-level innovation verdict robust against failure of any single substrate. [src: discoveries] The substrates available on the KBase Data Lakehouse have limited coverage:

| Dataset | Coverage |
|---|---|
| kbase_ke_pangenome.ncbi_env | 88.8% biosample geographic [src: discoveries] |
| kescience_mgnify | 28.4% categorical biome [src: discoveries] |
| kescience_bacdive | 32% phenotype, via GCF→GCA fallback [src: discoveries] |
| kescience_fitnessbrowser | ~30 organisms with BBH [src: discoveries] |

### Citation quality and multiple testing

Across 9 adversarial review rounds, the report found two distinct citation failure modes. [src: discoveries] The first is PMID-hijacking. A Mendoza 2020 citation in REVIEW_5 used PMID 32160912, which points to a Persian quality-of-life paper. [src: discoveries] A Burch 2023 citation in REVIEW_7 used PMID 37279472, which points to a COVID sense-of-coherence paper. [src: discoveries] The second is author-list hallucination. In REVIEW_8/9, Burch 2023 was listed with Dykhuizen DE as an author. PubMed verification of DOI 10.1093/gbe/evad089 gives the authors as Burch CL, Romanchuk A, Kelly M, Wu Y and Jones CD. [src: discoveries] Automatic DOI verifiers catch the first mode, but the second needs manual PubMed metadata checks. [src: discoveries] The report recommends that any reviewer-cited paper carrying a claim that could substantially undermine a project finding have its author, title, journal and PMID/DOI verified through PubMed. A DOI that merely resolves is not enough. [src: discoveries] The project-level memory for this is feedback_adversarial_verify_before_acting.md. [src: discoveries] See [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]].

On multiple testing, the NB30 pass found the real hypothesis-test family is 4 pre-registered hypotheses. All 4 survive Bonferroni α=0.0125. [src: discoveries] The M1–M26 methodology revisions are mostly pre-registration corrections. [src: discoveries] Three are genuine post-hoc metric corrections: M14, M21 and M23. [src: discoveries] The report calls family-wise correction across methodology revisions a category mistake. It recommends enumerating the actual test families and applying Bonferroni within each. [src: discoveries]

### ibd_phage_targeting: metabolomic clusters follow cohort

Pooling HMP2 and Franzosa metabolomics on a 122 m/z-bridge metabolite panel, then PCA plus K-means K=4, gave clusters that separated completely by cohort rather than diagnosis. [src: discoveries] PC1 explained 79 % of total variance and was essentially the cohort batch effect. [src: discoveries] Cross-cohort LOSO ARI was 0.000, against a taxonomic-ecotype LOSO baseline of 0.113. [src: discoveries] The report attributes the taxonomic framework's portability to MetaPhlAn3 relative abundances being unitless and sum-to-1 per sample, which normalizes across cohorts. [src: discoveries] Metabolite clustering instead inherits absolute-intensity differences between LC-MS runs. It needs explicit batch correction before PCA and K-means. [src: discoveries] The candidates listed are ComBat, SVA, RUV and within-method quantile normalization. [src: discoveries]

The report generalizes in three ways:
- Compositional feature spaces (taxonomy, pathway fractions, MAG fractions) are usually portable as-is. [src: discoveries]
- Absolute-intensity spaces (mass spectrometry, RNA-seq counts, protein abundance) are not portable without batch correction, and batch will dominate pooled variation. [src: discoveries]
- Within-pooled bootstrap stability can measure batch reproducibility rather than biological reproducibility. [src: discoveries]

One limit applies. The failure concerns cross-cohort portability. Within-cohort metabolite ecotypes may still be useful within a single laboratory's pipeline. [src: discoveries] See [[concepts/cross-cohort-portability-and-batch-dominance-in-microbiome-and-metabolomic-stratification]].

### ibd_phage_targeting: multi-line convergence

The project produced two independent six-line cross-corroboration narratives from one dataset. Each showed the same biological claim at several analytical granularities. [src: discoveries] The iron-acquisition narrative ran from an actionable MIBiG lookup through sample-level pathway–species attribution, cohort-level class enrichment, species–pathway covariation and genomic BGC content to AIEC literature. [src: discoveries] The bile-acid 7α-dehydroxylation narrative ran from within-carrier pathway differential abundance through subject-level metabolite differential abundance, paired substrate–product signatures and an informative strain-level null to mechanism literature. [src: discoveries] The report asserts that such multi-granularity convergence makes a claim robust against single-test failures. [src: discoveries] It says the approach applies to microbiome "is this signal real?" questions where taxonomy, pathway, metabolomics, BGC and strain modalities are available. [src: discoveries]

## 2026-04: [meta] Adversarial review applies at plan-revision scope, not just notebook scope

This part of the report covers ibd_phage_targeting, a project on phage targeting of Crohn's disease (CD) pathobionts. It shows that pathway-level and metabolite-level results can disagree, that a category schema can flip a hypothesis verdict, and that paired standard and adversarial review catches structural flaws. The evidence is project-internal notebook results plus the report's own generalizable rules. [src: discoveries]

### Pool versus flux: polyamines

Pathway differential abundance (DA) and metabolite DA gave opposite directions for polyamines. NB07 v1.8 §9 found the `06_polyamine_urea` pathway theme CD-DOWN (OR=0.42). [src: discoveries] NB09a §12 found polyamines as a metabolite class CD-UP at OR=14.6, the largest theme-level metabolite effect in the project. [src: discoveries] The report says both are correct, because a metabolite pool reflects production minus consumption rates plus dietary and host inputs. [src: discoveries] Its rule is that biosynthesis-pathway DA (production capacity) and untargeted-metabolomics DA (steady-state pool size) are not redundant. Disagreement in direction is informative, not a contradiction. [src: discoveries]

### Three annotation axes for targets

NB09c §13 and NB10a §14 establish three per-target annotation axes alongside the headline Tier-A score. [src: discoveries] See also [[concepts/pathobiont-target-prioritization-for-ibd-phage-therapy]].

- **Iron/AIEC-mediated versus other CD specialization.** This informs whether to target a species broadly or only its adherent-invasive *E. coli* (AIEC) subset. [src: discoveries]
- **Bile-acid coupling cost.** F. plautii, E. lenta and E. bolteae actively 7α-dehydroxylate bile acids. [src: discoveries] M. gnavus and E. coli do not. [src: discoveries] Depleting active 7α-dehydroxylators shifts the bile-acid pool toward inflammatory primary tauro-conjugated forms. [src: discoveries]
- **Species-abundance-mediated versus strain-content-mediated.** Kumbhari showed zero strain-adaptation gene signal. [src: discoveries] The report reads this as species-abundance mediation. It predicts that phage targeting will deplete activity predictably, with no within-species strain-content escape route. [src: discoveries]

The report generalizes this. Depleting the target species should not be the sole optimization criterion for FMT, antibiotics, phage cocktails or diet. Ecological costs, such as losing 7α-dehydroxylation or butyrogenesis, translate into net inflammatory balance. [src: discoveries]

### Category schema reversed the H3a (b) verdict

The NB07a H3a (b) test asked whether CD-up pathways concentrate in IBD-mechanism themes. It gave opposite verdicts under different category schemas, with the same DA outputs, test and nulls. [src: discoveries]

**v1.7 (regex on pathway names).** Seven a-priori IBD categories matched 44 of 409 prevalence-filtered pathways. [src: discoveries] Only 3 of the 52 CD-up pathways were in the 7-category set. [src: discoveries] The "≤ 3 of 7 categories" test was structurally degenerate, because the null was also at 100 % top-3. The verdict was FAIL, "not supported, structurally degenerate". [src: discoveries]

**v1.8 (MetaCyc class hierarchy).** This schema used the MetaCyc class hierarchy from ModelSEEDDatabase MetaCyc_Pathways.tbl plus a 12-theme IBD overlay. [src: discoveries] Of 409 pathways, 357 (87 %) had MetaCyc class data [src: discoveries], and 262 (64 %) were assigned to at least one IBD theme. [src: discoveries] The analysis used per-theme Fisher's exact tests (CD-up × in-theme) with Benjamini-Hochberg false discovery rate (BH-FDR) correction across 12 themes. [src: discoveries] Iron/heme acquisition was the dominant CD-up theme (OR = 8.1, FDR 7e-6; 15 of 52 CD-up pathways), and H3a (b) was SUPPORTED. [src: discoveries] This converged with NB05 *E. coli* Yersiniabactin/Enterobactin MIBiG matches, NB07a attribution of heme biosynthesis to *E. coli*, and AIEC iron-acquisition literature. [src: discoveries]

**Why v1.7 missed it.** The regex on "PWY-5920: superpathway of heme biosynthesis from glycine" does not match "iron". [src: discoveries] MetaCyc's curator-validated hierarchy places PWY-5920 under `HEME-SYN`, `Heme-b-Biosynthesis`, `Cofactor-Biosynthesis` and `Tetrapyrrole-Biosynthesis`. [src: discoveries] The v1.7 "0_other" bucket hid 15+ heme/iron pathways. [src: discoveries]

**Lessons.** The report adopts plan norm N17 in ibd_phage_targeting. For category-enrichment tests, prefer a curator-validated ontology or class hierarchy over name-pattern regex, and keep regex as a sensitivity check. [src: discoveries] ModelSEEDDatabase ships a usable MetaCyc class hierarchy at `/global_share/KBaseUtilities/ModelSEEDDatabase/Biochemistry/Aliases/Provenance/MetaCyc_Pathways.tbl`, with 90 %+ coverage of HUMAnN3 outputs. [src: discoveries] KEGG BRITE and the Gene Ontology (GO) biological-process subontology cover analogous needs for KEGG / EC-level data. [src: discoveries] The v1.7 FAIL was technically correct for its schema but was not a scientific refutation. A "structurally degenerate" verdict is an invitation to fix the schema, not to conclude on the science. [src: discoveries] See [[concepts/ontology-versus-name-pattern-categorization-in-pathway-enrichment-tests]].

### Paired standard and adversarial review of plans

The NB04 → NB04b-h rigor-repair arc established pairing standard review with an adversarial reviewer for notebook commits. The v1.6 → v1.7 plan revision extends the pattern to plan revisions. [src: discoveries] The v1.6 plan was a Pillar 3 refresh after Pillar 2 closure, written by an experienced agent. [src: discoveries] Adversarial review of v1.6 read the plan, report, failure analysis and actual mart parquet. It found 4 critical + 10 important issues, structurally analogous to NB04's failure pattern. [src: discoveries] Named issues:

- Feature leakage in the N14 dual-basis analysis, because the same-axis ecotype basis was leakage-poisoned. [src: discoveries]
- "4-substudy meta-viable" inherited from NB04e without re-verification for pathway data, which actually had 3+1. [src: discoveries]
- H3a thresholds without null distributions. [src: discoveries]
- H3a-new mislabeled "butyrate-producer ↔ pathobiont", with 4 of 6 named anchors not actually butyrate producers. [src: discoveries]
- H3b strain-adaptation collapsing to species-level on cMD by construction. [src: discoveries]
- H3e n=67 across 3 sites, not 130-subject HMP2. [src: discoveries]

The report recommends both reviewers for any plan revision whose notebooks will support clinical, experimental or external claims. Standard review mostly catches surface flaws. Adversarial review catches structural and inferential ones. [src: discoveries] Catching issues at plan scope was cheaper: NB04 → NB04b-h took 7 notebooks, while v1.6 → v1.7 took a single plan-edit pass. [src: discoveries] The operational pattern is `bash tools/review.sh <project> --type plan` for the standard review, and a general-purpose Agent with a find-flaws brief for the adversarial one. Both are reconciled before notebook execution. [src: discoveries]

Both NB04 and v1.6 shared recurring features that adversarial review caught and standard review did not:

- Effect-size thresholds without null distributions (NB04: Jaccard 0.14; v1.6: |ρ| > 0.4). [src: discoveries]
- Substudy or cohort sample-size claims that did not match the data on inspection. [src: discoveries]
- Hypothesis labels that did not match the test. NB04's "H2c RESOLVED" treated a nonsignificant result as positive. [src: discoveries]
- Same-axis feature leakage. NB04 clustered on taxa and tested taxa. v1.6 stratified pathway DA by pathway-feature ecotype. [src: discoveries]
- Falsifiability rules that pass under random data. "≤ 5 categories of 7" is loose enough to pass on random allocation. [src: discoveries]

The report reads these as mostly failures of pre-registration discipline. The questions are the actual sample size given the data, the null distribution behind any positive claim, and what each threshold means under that null. [src: discoveries] See [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]].

## 2026-04: [ibd_phage_targeting] NB04 rigor failure: 33 within-ecotype Tier-A candidates …

This part of the report covers a rigor failure in the ibd_phage_targeting Pillar 2 analysis, in which NB04 reported 33 within-ecotype Tier-A candidates and the repair left 3, all in E3. [src: discoveries] It also covers the review-method lesson drawn from it and a classifier-validation lesson from the same project. The evidence is a set of repair notebooks, an adversarial review and a held-out patient test, all within one project. [src: discoveries]

### The original claim and the repair filters

NB04 originally reported 33 within-ecotype Tier-A species candidates (18 E1, 15 E3). It marked the H2c *Clostridium scindens* paradox "RESOLVED by stratification." [src: discoveries] Two repair notebooks, NB04b and NB04c, applied three evidence filters to every candidate [src: discoveries]:

1. A bootstrap CI (confidence interval) lower bound above 0.3 on within-ecotype CLR-Δ, which repairs the "n.s. → RESOLVED" decision-logic bug. [src: discoveries]
2. LinDA (Zhou et al. 2022, pure-Python) showing CD↑ (Crohn's disease) with FDR (false discovery rate) < 0.10 in the same ecotype, which addresses single-method differential abundance. [src: discoveries]
3. A within-substudy CD-vs-nonIBD meta-analysis across 4 IBD (inflammatory bowel disease) sub-studies. It had to show CD↑ and at least 66 % sign concordance, as a confound-free independent check. [src: discoveries]

Only filter 3 was independent of the ecotype definition that generated NB04. [src: discoveries]

### Outcome by ecotype

No E1 candidate survived: 0 of 18 passed all three filters. [src: discoveries] All 14 E1 candidates that passed filters 1 and 2 had negative effects under the confound-free contrast. The report calls them ecotype-markers, not CD drivers. [src: discoveries] It attributes their apparent CD↑ to feature leakage and compositional bias compounding. [src: discoveries]

In E3, 3 of 15 candidates passed all three filters and are the trustworthy Tier-A [src: discoveries]:

| Species | Within-substudy | LinDA E3 |
|---|---|---|
| *Mediterraneibacter gnavus* | CD↑ +5.13 | +1.64 [src: discoveries] |
| *Flavonifractor plautii* | +1.89 | +2.91 [src: discoveries] |
| *Blautia wexlerae* | +0.91 | +2.00 [src: discoveries] |

Per-ecotype Tier-A therefore drops from "33 candidates across both E1 and E3" to "3 candidates, E3 only." [src: discoveries]

### Hypotheses H2c and H2b

H2c was directly contradicted. Under within-substudy confound-free analysis, *C. scindens* is genuinely CD↑, with pooled CLR-Δ +1.18, FDR 1e-8 and 4/4 sign concordance. [src: discoveries] In NB04b, leave-one-out refitting showed *C. scindens* CD↑ in both E1 and E3 once the ecotype definition excluded the test species. NB04's nonsignificant call was therefore a leakage self-selection artifact. [src: discoveries]

H2b (ecotype divergence) survived strongly. The permutation-null p was 0.000, with observed Jaccard 0.104 against a null mean of 0.785 ± 0.054. [src: discoveries] The report concludes that stratification divergence is real, but NB04's effect-size framing used the wrong statistic. [src: discoveries]

### Scope and next steps

The ecotype framework is still usable for patient stratification, and NB02 H1b stands. Only the within-ecotype differential abundance is invalidated for target selection. [src: discoveries] The repair applies to the next three Pillar 2 deliverables, including Tier-A scoring and cocktail draft preparation for UC Davis patients. [src: discoveries] E1 needs a reformulated approach before NB05, because the current within-ecotype differential abundance is not a usable target list. [src: discoveries] The report proposes three candidate approaches:

- Rebuild ecotypes on a functional (pathway or KEGG) feature matrix to break the taxonomic-feature leakage. [src: discoveries]
- Run within-substudy CD-vs-nonIBD analysis stratified by ecotype as the primary analysis. This needs substudy × ecotype × diagnosis cells with at least 10 samples each, and their availability needs checking. [src: discoveries]
- Combine UC-vs-HC and CD-vs-HC as IBD-vs-control for power. [src: discoveries]

The full arc and methodology lessons are in projects/ibd_phage_targeting/FAILURE_ANALYSIS.md. [src: discoveries] See also [[concepts/pathobiont-target-prioritization-for-ibd-phage-therapy]] and [[concepts/gut-microbiome-ecotype-stability-and-cross-study-reproducibility]].

### Standard versus adversarial review

The same project files received two reviews with opposite verdicts. tools/review.sh, the reviewer behind /berdl-review and /submit, works with a "find-strengths-and-suggestions" framing inherited from .claude/reviewer/SYSTEM_PROMPT.md. [src: discoveries] The standard review (claude-sonnet-4) concluded "exceptional methodological sophistication" and "no critical issues." It recommended proceeding to Pillars 3–5 with the existing Tier-A list. [src: discoveries] An adversarial review, run by a general-purpose agent told to "find flaws, don't be diplomatic," found 5 critical and 6 important issues. [src: discoveries] The five it highlights:

- Feature leakage: samples were clustered on taxon abundances, then the same taxa were tested within clusters. [src: discoveries]
- Hard-coded "RESOLVED" verdict logic that treated n.s. results as positive evidence. [src: discoveries]
- Zero confounder adjustment, despite citing Vujkovic-Cvijin 2020, which calls for it. [src: discoveries]
- Jaccard 0.14 reported as supporting H2b without any null distribution. [src: discoveries]
- An ecotype framework with 48.9 % cross-method agreement and no external replication. [src: discoveries]

The report judges the standard reviewer excellent at surface flaws and appropriate for routine submissions. Its examples are missing sections, undocumented dependencies, broken figures and simple statistical errors. [src: discoveries] It calls the reviewer systematically weak on structural and inferential issues. These include selection-on-outcome confounding, missing null distributions, post-hoc choice of decision rules and narrative-vs-evidence mismatch. [src: discoveries] For any project whose conclusions inform downstream decisions, it recommends pairing /berdl-review with a separately spawned adversarial reviewer and reconciling the two outputs before final synthesis. [src: discoveries] It proposes an optional --adversarial flag for /submit that runs both reviewers and produces a combined report. [src: discoveries] Standard review remains the right default for in-progress or iteration-mode work. [src: discoveries] See [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]].

### Classifier AUC versus patient-level usefulness

The report warns that training-cohort one-versus-rest AUC (area under curve) is a weak proxy for patient-level usefulness. This holds whenever the cohort includes a strong cohort-axis variable that is constant, or nearly so, in the held-out patients. [src: discoveries] In NB03, a classifier was trained on pooled HC (healthy controls) and IBD samples. It used is_ibd, sex and age to predict K=4 ecotypes. It reached macro OvR AUC 0.80 in 5-fold CV (cross-validation), above the 0.70 passing threshold. [src: discoveries] Applied to UC Davis patients, who were 100 % IBD with is_ibd = 1 constant, it agreed with the NB02 metagenomic projection only 41 % of the time. [src: discoveries] It predicted E1 for 19/22 patients. Its dominant learned rule was "IBD → E1 most of the time," the marginal mode among IBD training samples. [src: discoveries]

The report explains the gap this way. The AUC counted HC-vs-IBD separability. The UC Davis test required the harder separation inside IBD, E1 transitional versus E3 severe, and these are not the same problem. [src: discoveries] Its generalizable fix is to apply the classifier to an independent cohort with the cohort-axis variable held fixed before quoting AUC as clinical utility. Agreement on that cohort is the translation-honest metric. [src: discoveries] See [[concepts/cross-cohort-portability-and-batch-dominance-in-microbiome-and-metabolomic-stratification]].

## 2026-04: [ibd_phage_targeting] Historical static collection inventories understated the …

This part of the log covers the ibd_phage_targeting project. It shows that the choice of ecotype method decides whether a projection across taxonomic classifiers works, how K was chosen, what the four ecotypes are, and which Data Lakehouse resources and pitfalls matter for IBD phage work. [src: discoveries]

### Cross-classifier projection

- **LDA is robust.** The report says nondetection does not force a particular projection coordinate. [src: discoveries] UC Davis Kuehl samples projected to E0, E1 and E3 in proportions 27 / 42 / 31 %, which the report calls biologically plausible. [src: discoveries]
- **GMM is fragile.** The report states two figures about Kuehl detection of training species: Kuehl detects only 54 %, and 70 % of training species have no Kuehl detection. [src: discoveries] These two figures do not add up as complements of one population (54 % detected would leave 46 % undetected). The quote does not explain the difference, so each figure is given as the report states it. [src: discoveries] The report attributes the GMM artifact to CLR imputing zeros with a small pseudocount. PCA then places the sparse vectors in the region of one dominant Gaussian cluster, whatever the biology. [src: discoveries] All 26 Kuehl samples projected to E3 at GMM confidence > 0.97, which the report labels an artifact. [src: discoveries]
- **Recommendation.** For projection across classifier namespaces, use pseudo-count or sparse-data-robust methods (LDA, MMvec) as primary. Treat CLR-based methods as advisory at best. [src: discoveries] See [[concepts/cross-cohort-portability-and-batch-dominance-in-microbiome-and-metabolomic-stratification]].

### Choosing K

LDA training perplexity and GMM BIC (on CLR + PCA-20) were monotone with K and always preferred the largest available K. [src: discoveries] Five-fold held-out perplexity gave the same monotone signal at about 8.5K samples. It did not separate overfitting from genuine structure. [src: discoveries]

The report instead proposes cross-method adjusted Rand index (ARI) between LDA and GMM at each K. This signal has peaks and valleys, because the methods agree only on K values that reflect real partitions. [src: discoveries] ARI peaked at K=7 (0.140) and K=4 (0.131). A parsimony rule (smallest K within 0.02 of the peak) selected K=4. [src: discoveries] The report calls K=4 the most interpretable and biologically clean choice. [src: discoveries] It generalizes the advice to any two-model-family ecotype analysis: prefer the K where the models agree most, not the K each prefers. [src: discoveries]

### The four ecotypes

K=4 LDA-GMM consensus on 8,489 curatedMetagenomicData MetaPhlAn3 samples (5,333 HC + 3,156 IBD/other) gave four ecotypes. The report says they align with published enterotype literature and separate disease from healthy samples. [src: discoveries]

| Ecotype | Samples | Defining taxa | Disease/health composition |
|---|---|---|---|
| E0 diverse commensal | 3,604 | F. prausnitzii, R. bromii, B. uniformis and Bifidobacterium, balanced | 66.8 % of HC [src: discoveries] |
| E1 Bacteroides2 transitional | 2,601 | P. vulgatus, B. uniformis, B. dorei | 48 % CD, 58 % UC, 100 % T1D, 97 % T2D, 67 % nonIBD [src: discoveries] |
| E2 Prevotella copri | 920 | P. copri 28 % | 16.9 % of HC, ~0 % disease (non-Western healthy) [src: discoveries] |
| E3 severe Bacteroides-expanded | 1,364 | P. vulgatus 14 % + B. fragilis 3.6 % | 50 % CD, 40 % UC, 67 % IBD acute flare, 38 % CDI [src: discoveries] |

Healthy samples concentrate in E0 + E2 (84 % combined). [src: discoveries] CD and UC patients spread across E1 and E3 instead of one ecotype. The report treats this as the patient-stratification signal for downstream within-ecotype analyses. [src: discoveries] It reads the link of the Bacteroides2 ecotype to both metabolic disease and IBD as echoing the "low-diversity disease state" hypothesis. [src: discoveries] The file data/ecotype_assignments.tsv is the artifact for downstream notebooks. [src: discoveries] See also [[concepts/gut-microbiome-ecotype-stability-and-cross-study-reproducibility]].

### A false C. scindens call

The v2 preliminary IBD report (2026-03-28) called C. scindens CD-enriched at log₂FC = +2.67 using pooled Mann-Whitney differential abundance. The report identifies this as a false call. [src: discoveries] C. scindens is described as protective. It makes secondary bile acids by 7α-dehydroxylation, activates TGR5, occurs at ~79 % prevalence in healthy individuals and inhibits C. difficile. [src: discoveries] The report proposes three likely mechanisms:

- Ruminococcaceae loss in severe patients inflates the relative abundance of surviving C. scindens. [src: discoveries]
- Not all C. scindens strains carry the bai operon, so species presence does not establish functional presence. [src: discoveries]
- Pooled analysis mixes patient subgroups with different microbiomes (ecotype mixing). [src: discoveries]

The proposed fix is compositional-aware differential abundance (ANCOM-BC, MaAsLin2 or LinDA) run within patient ecotypes. [src: discoveries] The report calls this the canonical example for treating pre-computed ref_* tables as starting points that need verification, not ground truth. [src: discoveries] See [[concepts/pathobiont-target-prioritization-for-ibd-phage-therapy]].

### Data resources

Historical static inventories lagged the live [[entities/kbase-data-lakehouse]] catalog. They omitted several databases that matter for gut-microbiome and phage work. [src: discoveries] The helpers get_databases, get_tables and get_table_schema from berdl_notebook_utils support current, access-aware discovery. [src: discoveries]

- kescience_mgnify is EBI MGnify, a metagenomics service relevant to IBD-cohort cross-validation. The report notes the name is mgnify, not the mis-recalled "magnify". [src: discoveries]
- phagefoundry_ecoliphages_genomedepot, with a duplicate _genomedepot variant, holds E. coli phage genomes relevant to targeting adherent-invasive E. coli (AIEC). [src: discoveries] PhageFoundry has 7 databases in the tenant, not the 5 documented. [src: discoveries]
- kescience_interpro holds InterPro domain annotations and is a primary source for virulence-factor classification. [src: discoveries]
- kescience_pubmed supports literature text mining and is a sibling of kescience_paperblast. [src: discoveries]
- pangenome_bakta is a Bakta-pangenome slice separate from kbase_ke_pangenome. [src: discoveries]
- arkinlab_microbeatlas has 464K global 16S samples and serves as a prevalence and biogeography baseline. [src: discoveries]
- protect_integration is a second Protect-tenant database beyond protect_genomedepot. [src: discoveries]
- u_kazakov__klebsiella_genomedepot and u_kazakov__strain_modelling hold user-owned Klebsiella phage-host work, worth checking with the owner. [src: discoveries]

The UC Davis / Arkin CrohnsPhage data mart ships lineage.yaml (ETL provenance, changelog, known gaps) and schema_overview.yaml (table inventory by category). It also ships per-table YAML dictionaries (columns, dtypes, null counts, unique counts, sample values). [src: discoveries] Its ref_missing_data_codes table uses sentinel codes such as PENDING_DAVE_LAB, PENDING_KUEHL and PENDING_HMP2_RAW. These separate real NULLs from known-pending data. [src: discoveries] The report says this pattern makes large local marts agent-readable without live queries. [src: discoveries]

## 2026-04: [enigma_sso_asv_ecology] 16S community similarity maps contamination plume at …

This part of the report covers SSO 16S community results and a plant microbiome analysis. The SSO results come from a 3×3 well grid (~6 m span), and the plume model lacks geochemistry validation data. [src: discoveries] The plant results classify plant-associated bacteria by their growth-promoting and pathogenic gene content. [src: discoveries]

### SSO well grid: community structure and flow paths

The grid shows significant community distance-decay (Mantel ρ=0.323, p=0.029), driven by the east-west axis rather than the hillslope gradient. [src: discoveries] Wells U3-M6-L7 form a diagonal corridor that shares community composition along the NE→SW plume flow path. [src: discoveries] Genus-level functional inference maps the redox ladder of denitrification → iron reduction → fermentation onto the physical grid. [src: discoveries] Well M5 hosts a *Rhodanobacter* denitrification hotspot (7.7%) at the plume mixing zone. [src: discoveries]

Groundwater communities are temporally stable: well explains R²=49.9% and date R²=0.8% over 9 days. [src: discoveries] From these results the report concludes that 16S community data can delineate subsurface contamination flow paths at sub-decameter resolution. [src: discoveries]

### Co-occurring chemolithotrophs

*Candidatus* Nitrosotalea (an archaeal ammonia oxidizer) and *Sideroxydans* (an iron oxidizer) co-occur almost perfectly across the 9 wells (ρ=+0.95), concentrated at U3. [src: discoveries] The report describes both as chemolithotrophs exploiting reduced compounds arriving in the plume. [src: discoveries] It suggests that the tight coupling reflects a shared niche at the oxic plume fringe. [src: discoveries]

### Geochemistry gap

221 METALS/ICTOC/ISOTOPES/NH3NO2 sample tubes from the SSO campaign are registered in ENIGMA CORAL (`sdt_sample`). No `Assay Geochemistry` processes are linked to them, and the analytical measurement values were never ingested into the KBase Data Lakehouse. [src: discoveries] The report calls this the key validation dataset for the plume model. [src: discoveries] See also [[entities/subsurface-observatory-well-grid]] and [[entities/enigma]].

### Plant microbiome ecotypes

**Dual-nature bacteria.** The report states that 60-85% of plant-associated bacteria are dual-nature, carrying both plant growth-promoting (PGP) and pathogenic markers. [src: discoveries] It classified 25,660 species into beneficial, pathogenic, dual-nature and neutral cohorts. Most plant-associated species carry both marker types. [src: discoveries] The report reads this as a challenge to binary beneficial/pathogenic classification, and suggests that most plant-microbe interactions are context-dependent rather than fixed. [src: discoveries]

**Compartment and function.** PERMANOVA (permutational multivariate analysis of variance) shows that plant compartment explains 53% of variance in functional profiles (R²=0.53, pseudo-F=235, p=0.001). [src: discoveries] Root is the most functionally specialized compartment. [src: discoveries] The report concludes that compartment is the dominant driver of functional differentiation. [src: discoveries] ACC (1-aminocyclopropane-1-carboxylate) deaminase (acdS) has the strongest compartment-specific enrichment of any single marker gene, with an odds ratio (OR) of 69.3 in root-associated species. [src: discoveries] The report links this to its role in modulating plant ethylene signaling at the root interface. [src: discoveries]

**Core versus accessory, and selection.** PGP genes are 64.6% core genome versus 45.2% for pathogenic genes (Mann-Whitney p=3.4e-125). [src: discoveries] The report suggests beneficial functions are under stronger purifying selection and more deeply embedded in bacterial evolutionary history than pathogenic capabilities. [src: discoveries] Compare [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]].

**Community assembly.** Co-occurring plant-associated genera show functional redundancy rather than complementarity (permutation p=1.0, Cohen's d=-7.54). [src: discoveries] The report concludes that environmental filtering dominates niche partitioning, so compartments select a common functional toolkit rather than complementary specialists. [src: discoveries]

**Candidate gene families.** After phylogenetic control, 50 novel eggNOG ortholog groups distinguish plant-associated from non-plant species. [src: discoveries] The top hit is COG3569 (OR=6.01 phylo-controlled). [src: discoveries] The report treats these as candidate plant–microbe interaction gene families not confounded by shared evolutionary history. [src: discoveries]

**Mobile elements.** Species carrying singleton marker gene clusters are 16x more likely to also carry transposase/integrase singletons (OR=15.95, p=8.8e-20). [src: discoveries] The report suggests this co-localization reflects recent horizontal acquisition of plant-interaction genes on mobile genetic elements. [src: discoveries]

## 2026-03: [amr_cofitness_networks] AMR support networks enriched for flagellar motility …

This part of the report covers four antimicrobial resistance (AMR) analyses. They are environmental composition, cofitness networks, fitness cost and strain-level variation. Together they report that AMR mechanism mix depends on environment [src: discoveries], that AMR fitness cost does not vary with mechanism [src: discoveries], and that non-core acquired AMR genes show stronger phylogenetic signal than core genes. [src: discoveries]

### Environmental resistome (amr_environmental_resistome)

Resistance mechanism composition is strongly environment-dependent across 14,723 species. [src: discoveries] Efflux pumps make up 21% of AMR in human gut species but 1% in aquatic species (η²=0.127). [src: discoveries] Metal resistance makes up 45% of AMR in soil/aquatic species but 6% in human gut species (η²=0.107). [src: discoveries] Clinical species have 68% accessory (acquired) AMR versus 43% in soil species. [src: discoveries] Within 823 multi-environment species, clinical strain fraction predicts total AMR (rho=0.465, p=2.2e-45). [src: discoveries] Klebsiella pneumoniae has 1,115 AMR clusters, only 7 of them core, across 13,637 genomes. [src: discoveries] All findings survive family-level phylogenetic control, with 20/141 families significant. [src: discoveries] The report calls this the largest genomic AMR-environment analysis to date, extending Gibson et al. (2015, 6K genomes) by 50×. [src: discoveries]

### Cofitness networks (amr_cofitness_networks)

Flagellum assembly (GO:0044780) is enriched in 5 organisms, [src: discoveries] histidine biosynthesis (GO:0000105) in 3, [src: discoveries] and tryptophan biosynthesis (GO:0000162) in 3. [src: discoveries]

The enrichment depends on the annotation source. It is undetectable with old Fitness Browser SEED annotations (0/280 significant). [src: discoveries] Only InterProScan GO annotations, at 68% coverage, reveal it. [src: discoveries] See [[concepts/annotation-coverage-and-resolution-in-genome-wide-cofitness-analysis]] for the wider issue.

Support networks are organism-specific, with cross-mechanism Jaccard 0.375 versus within-mechanism 0.207 (Mann-Whitney U, MWU, p=4.3e-13). [src: discoveries] AMR genes fall in larger-than-average independent component analysis (ICA) modules, with median size 46 versus 27 (p=1.7e-8). [src: discoveries] The report suggests, as an interpretation, that co-regulation with motility and biosynthesis means AMR costs reflect competition for the proton motive force. [src: discoveries]

### Fitness cost (amr_fitness_cost)

A random-effects meta-analysis of 801 AMR genes across 25 organisms gives a pooled fitness shift of +0.086 [+0.074, +0.098] after knockout, with all 25/25 organisms positive. [src: discoveries] The cost does not vary with mechanism (Kruskal-Wallis, KW, p=0.89). [src: discoveries] It does not differ between core and accessory genes (p=0.33). [src: discoveries] It does not differ between bakta_amr and keyword assignment tiers (p=0.26). [src: discoveries] The report suggests that compensatory evolution has equalized costs to an irreducible floor. [src: discoveries]

Mechanism does predict conservation status. Metal resistance genes are 44% accessory versus 13% for efflux genes (χ²=69.3, p=1.4e-13). [src: discoveries] The report concludes that acquisition history, not cost, determines whether AMR genes are core or accessory. [src: discoveries] Broad-spectrum efflux genes show a stronger antibiotic-dependent fitness flip than narrow-spectrum enzymatic inactivation genes (+0.094 vs −0.001, MWU p=0.007). [src: discoveries]

### Strain variation (amr_strain_variation)

**Phylogenetic signal.** Mantel tests across 1,261 species show stronger signal for non-core (acquired) AMR genes (median r=0.222) than for core (intrinsic) genes (median r=0.117), paired t-test p=7.0e-16. [src: discoveries] The report reads this as contradicting the standard model of phylogenetically random acquisition by horizontal gene transfer (HGT). In its reading, acquired elements are stably, vertically inherited and create clonal AMR lineages. [src: discoveries] A caveat limits the comparison. Core genes have near-zero Jaccard variance by definition (≥95% prevalence), which partly suppresses their distance-based signal. [src: discoveries]

**Prevalence.** Across 1,305 species and 180,025 genomes, 51.3% of AMR gene-species occurrences are rare (≤5% prevalence), [src: discoveries] 41.3% are variable (5-95%), [src: discoveries] and only 7.5% are fixed (≥95%). [src: discoveries] Median pairwise Jaccard distance between strains is 0.435, so strains within a species share less than 60% of their AMR repertoire. [src: discoveries] Atlas Core genes are 77% fixed within species. [src: discoveries] Singletons are 79% rare. [src: discoveries] Both figures support the cross-species conservation classification at strain resolution. [src: discoveries]

**Resistance islands.** Resistance islands are reported in 54% of species with a mean of 6.2 genes. [src: discoveries] The analysis detects 1,517 islands across 705/1,305 species, with mean phi coefficient 0.827, which indicates tight co-occurrence. [src: discoveries] 88% contain multiple resistance mechanisms, most often efflux plus enzymatic inactivation. [src: discoveries] The largest island has 43 genes. [src: discoveries] The report states that these islands provide coordinated defense against multiple drug classes. [src: discoveries]

**Pangenome openness.** AMR variability weakly anti-correlates with pangenome openness (Spearman rho = -0.193, p = 2.2e-12). Species with more open pangenomes have slightly lower AMR variability, which the report calls unexpected. [src: discoveries] The report proposes that open-pangenome species accumulate more rare or singleton AMR genes below the 5% threshold. That would deflate the variability index, which measures the 5-95% zone. [src: discoveries] See [[concepts/pangenome-openness-and-its-correlates]].

## 2026-03: [bakta_reannotation] Bakta and eggNOG are complementary annotation sources

This part of the log reports that Bakta can reannotate most Fitness Browser (FB) dark genes that have pangenome links, and that a small residue stays truly dark. [src: discoveries] It then summarizes a genome-scale comparison of Bakta and eggNOG annotation. [src: discoveries]

### Truly dark genes

Bakta v1.12.0 reclassifies 33,105 (83.7%) of 39,532 FB dark genes with pangenome links. [src: discoveries] Just 6,427 are "truly dark", meaning both FB and Bakta call them hypothetical protein. [src: discoveries] Even among these, only 246/6,427 (3.8%) have zero annotation clues. [src: discoveries] Of the truly dark genes, 84.7% have database cross-references and 43.5% have eggNOG hits, though 55% of COG (clusters of orthologous groups) assignments are "S"/unknown. [src: discoveries] Also, 29.3% have cross-organism orthologs and 9.5% are in ICA (independent component analysis) fitness modules. [src: discoveries]

The report describes truly dark genes as structurally distinct from its comparison genes. It does not say here what the comparison set is:
- They are shorter (121 vs 194 aa). [src: discoveries]
- They are less conserved (43% vs 73% core). [src: discoveries]
- They have fewer orthologs (29% vs 64%). [src: discoveries]
- They have higher GC deviation (d=0.247). [src: discoveries]

The report calls these properties consistent with recent HGT (horizontal gene transfer) outpacing annotation databases. [src: discoveries] The report suggests that dark genes concentrate in recently acquired genomic islands rather than being randomly distributed. [src: discoveries] This is an interpretation, not a direct test.

Contrary to expectation, truly dark genes with strong fitness phenotypes are depleted in stress conditions (OR=0.53, p<0.001). [src: discoveries] They are enriched in nutrient, mixed community and iron conditions. [src: discoveries] The report suggests novel metabolic or inter-species interaction functions rather than stress responses. [src: discoveries]

### Bakta versus eggNOG-mapper

The bakta_reannotation project compared Bakta v1.12.0 with eggNOG-mapper across 132.5M gene clusters. [src: discoveries] eggNOG wins on enrichment-style annotations. The table lists coverage as eggNOG vs Bakta:

| Annotation | eggNOG | Bakta |
|---|---|---|
| COG | 51% [src: discoveries] | 8.2% [src: discoveries] |
| KEGG | 38.5% [src: discoveries] | 17.3% [src: discoveries] |
| Pfam | 63% [src: discoveries] | 7.7% [src: discoveries] |

Bakta wins on GO (Gene Ontology) terms (15% vs 7.4%) [src: discoveries] and product descriptions (71.2% vs 70.4%). [src: discoveries] It also uniquely provides UniRef50 links, at 79.2% coverage. [src: discoveries] The union raises "any functional annotation" coverage from ~70% to 77.3%. [src: discoveries] Bakta rescues 11.2M clusters (of 39.2M) that eggNOG misses entirely. [src: discoveries]

The report treats Bakta's lower COG/KEGG/Pfam coverage as design-driven. It attributes confirmation to developer Oliver Schwengers across GitHub issues #350, #385, #391 and #393. [src: discoveries] The stated reasons are:
- Bakta's PSC database is optimized for product descriptions, not functional categories. Only ~14% of PSC entries have COG and ~19% have KEGG. [src: discoveries]
- COG 2024 no longer provides representative sequences, which forces a lossy indirect WP accession→IPS→PSC mapping. [src: discoveries]
- HMMER runs only on hypotheticals (~7.7%), so the 92% with PSC matches never get Pfam searched. [src: discoveries]
- PSC uses DIAMOND fast mode, while eggNOG uses HMM-based ortholog assignment. [src: discoveries]
- The developer planned to integrate eggNOG into PSC representatives (issue #325). This may have partly happened in DB v6.0, with limited impact. [src: discoveries]

The Arche benchmark paper (Alonso-Reyes & Albarracin 2025, PMID 40811208) is reported to have independently confirmed Bakta's conservative annotation transfer relative to other tools. [src: discoveries]

### UniRef50 bridge to the KBase Data Lakehouse

Only 33.3% of Bakta's 17.6M distinct UniRef50 IDs exist in `kbase_uniprot.uniprot_identifier`. [src: discoveries] For the matched IDs, the bridge reaches RefSeq (71%), OrthoDB (46%), STRING (40%) and KEGG (36%). [src: discoveries] GO, EC (Enzyme Commission), InterPro and Pfam are missing from the bridge, and importing full UniProt would unlock them. [src: discoveries] For now, the report considers eggNOG the better source for COG/KEGG/Pfam enrichment analysis. [src: discoveries]

See also [[concepts/reannotation-lag-versus-genuinely-unannotatable-dark-genes]] and [[concepts/annotation-source-disagreement-and-coverage]].

## 2026-03; 2026-01

This part of the report covers a Spark join pitfall on the UniProt tables [src: discoveries], an ecotype analysis that compares environment and phylogeny effects and includes two nonsignificant tests [src: discoveries], and a clusters of orthologous groups (COG) analysis. The COG analysis reports a consistent functional partitioning across 32 species. [src: discoveries]

### Spark join pitfall on UniProt (bakta_reannotation)

The report identifies kbase_uniprot.uniprot_identifier as a 2.5B-row table. [src: discoveries] Any join that touches it can exceed spark.driver.maxResultSize (1GB) through broadcast exchange. [src: discoveries] The recommended fix is `SET spark.sql.autoBroadcastJoinThreshold = -1`, which forces sort-merge joins. [src: discoveries]

### Environment versus phylogeny (ecotype_analysis)

Across 172 species with sufficient data, the median partial correlation was higher for phylogeny than for environment. It was 0.0025 for environment [src: discoveries] and 0.0143 for phylogeny. [src: discoveries] Phylogeny dominated in 60.5% of species [src: discoveries] and environment dominated in 39.5%. [src: discoveries] These values bear on [[concepts/environmental-versus-phylogenetic-drivers-of-gene-content]].

- Environmental bacteria, where latitude/longitude is meaningful, did not differ significantly from host-associated bacteria (p=0.66). [src: discoveries]
- Pangenome openness, measured as low core fraction, was unrelated to the environment effect (rho=-0.05, p=0.54) [src: discoveries] and to the phylogeny effect (rho=0.03, p=0.73). [src: discoveries] See [[concepts/pangenome-openness-and-its-correlates]].

Practical notes: querying average nucleotide identity (ANI) for all 13K+ genomes in one IN clause fails or times out, so ANI must be queried species by species. [src: discoveries] The pangenome table already holds no_core, no_aux_genome, no_singleton_gene_clusters and no_gene_clusters, so these need not be recomputed from gene_cluster. [src: discoveries]

### Pangenomes without species clades

The 12 pangenomes without matching species clades are mostly obligate symbionts. [src: discoveries] They include Portiera aleyrodidarum, a whitefly symbiont, [src: discoveries] and Profftella armatura, a psyllid symbiont. [src: discoveries] They also include uncultivated lineages with UBA, TMED and SCGC prefixes. [src: discoveries] These are valid pangenomes that were filtered from species metadata because they have a single genome. [src: discoveries]

### Two-speed genome (cog_analysis)

The analysis covers 32 species across 9 phyla and 357,623 genes. [src: discoveries] It reports a consistent "two-speed genome": novel/singleton genes are enriched in mobile, defense and unknown-function categories, and core genes are enriched in metabolic and translation categories. The values below are as the report gives them. See [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]].

| COG category | Enrichment | Consistency | Group |
|---|---|---|---|
| L (mobile elements) | +10.88% (strongest signal) | 100% | novel [src: discoveries] |
| V (defense mechanisms) | +2.83% | 100% | novel [src: discoveries] |
| S (unknown function) | +1.64% | 69% | novel [src: discoveries] |
| J (translation) | -4.65% (strongest depletion in novel genes) | 97% | core [src: discoveries] |
| F (nucleotide metabolism) | -2.09% | 100% | core [src: discoveries] |
| H (coenzyme metabolism) | -2.06% | 97% | core [src: discoveries] |
| E (amino acid metabolism) | -1.81% | 81% | core [src: discoveries] |
| C (energy production) | -1.75% | 88% | core [src: discoveries] |

All 8 predictions from the initial N. gonorrhoeae analysis were confirmed across the 32 species. [src: discoveries]

Composite COG assignments are reported as genuine multifunctional genes, not annotation artifacts. Examples are LV (mobile+defense) and EGP (amino acid+carbohydrate+inorganic ion). [src: discoveries] LV shows +0.34% enrichment with 76% consistency. [src: discoveries] The report suggests this reflects functional modules such as mobile defense islands. [src: discoveries]

### Interpretations the report draws

These statements are the report's interpretations, not separate measurements:
- Core genes are an ancient, conserved "metabolic engine" covering translation, energy and biosynthesis. [src: discoveries]
- Novel genes are recent acquisitions for ecological adaptation, including mobile elements, defense and niche-specific functions. [src: discoveries]
- Horizontal gene transfer (HGT), not vertical inheritance, is the primary innovation mechanism. [src: discoveries]
- The +10.88% L enrichment suggests that most genomic novelty comes from mobile elements. [src: discoveries]
- The patterns hold universally across bacterial phyla, which suggests deep evolutionary constraint. [src: discoveries]

## 2026-02: [adp1_deletion_phenotypes] 625 condition-specific genes map precisely to …

Each of ADP1's 8 carbon sources requires a distinct set of respiratory-chain components. [src: discoveries] The report explains this by NADH flux, and much of that explanation is inference. [src: discoveries] See [[entities/acinetobacter-baylyi-adp1]].

### Substrate-specific respiratory wiring

Quinate requires only Complex I, and all other components are dispensable. [src: discoveries] Acetate is the most demanding source, requiring Complex I, cytochrome bo3, ACIAD3522 and more. [src: discoveries] Glucose requires no specific component because of full redundancy. [src: discoveries] The report calls this qualitatively different wiring per substrate class, not a quantitative gradient. [src: discoveries]

The three NADH dehydrogenases divide the work as follows:

- Complex I has 13 subunits and pumps protons. It is quinate-essential and glucose-dispensable. [src: discoveries]
- NDH-2 has 1 subunit and does not pump protons. It has no growth data and is only predicted to back up glucose. [src: discoveries]
- ACIAD3522 is an NADH-FMN oxidoreductase. It is acetate-lethal (0.013) and fine on quinate (1.39). [src: discoveries]

The report describes this as a division of labor in electron transport. [src: discoveries]

### NADH flux explanation

Quinate yields fewer NADH per carbon (0.57) than glucose (1.50), yet Complex I matters more on quinate. [src: discoveries] The report resolves this by proposing that β-ketoadipate pathway products, succinyl-CoA and acetyl-CoA, enter the tricarboxylic acid (TCA) cycle together. This would create an NADH burst beyond what NDH-2 can reoxidize. [src: discoveries] Glucose spreads its NADH over Entner-Doudoroff and TCA steps, where NDH-2 suffices. [src: discoveries]

Proteomics under standard conditions shows similar expression of the three dehydrogenases. Complex I mean is 27.6 (66th percentile), NDH-2 is 27.0 (59th) and ACIAD3522 is 26.2 (48th). [src: discoveries] All lie within 1.4 units of each other around the genome median (26.4). [src: discoveries] The report concludes that the cell does not switch configurations by regulating expression. All three run at once, and the limiting one depends on NADH flux from the carbon source. [src: discoveries] It calls this a passive, flux-based system, not an active regulatory switch. [src: discoveries]

### The quinate support network

The β-ketoadipate pathway has 8 core genes, but 51 genes show quinate-specific growth defects. The report gives this as a 7:1 support-to-pathway ratio. [src: discoveries] The support genes fall into three subsystems:

- Complex I: 21 genes for NADH reoxidation. [src: discoveries]
- Iron acquisition: 7 genes supplying Fe²⁺ for the ring-cleavage dioxygenase. [src: discoveries]
- PQQ (pyrroloquinoline quinone) biosynthesis: 2 genes for the cofactor of quinate dehydrogenase. [src: discoveries]

The report interprets the "aromatic support network" as a high-NADH-flux bottleneck network, not one specific to aromatic chemistry. [src: discoveries] The aromatic_catabolism_network report hypothesized that ADP1's quinate specificity reflects NDH-2 compensation on substrates with lower NADH flux. [src: discoveries]

**Limit from the cross-species test.** The first test seemed to support compensation, with 10/14 organisms identified as having NDH-2. That result came from misannotated Complex I subunits that passed the text filter in 5 organisms. [src: discoveries] After filtering to organisms with ≤2 hits per genome, organisms with validated NDH-2 had larger Complex I aromatic deficits (mean -0.297) than those without (-0.156, p=0.52). This fails to support cross-species compensation. [src: discoveries] Ortholog-transferred fitness data also show the largest Complex I defects on acetate (-1.55 vs background) and succinate (-1.39), not on aromatics. [src: discoveries]

### Limits of flux balance analysis

Of the 51 quinate-specific genes, 30 (59%) have no flux balance analysis (FBA) reaction mappings. These include PQQ biosynthesis, iron acquisition, transcriptional regulators and respiratory-chain components. [src: discoveries] For Complex I, FBA predicts 1.76× higher flux on aromatics but 0% essentiality. [src: discoveries] The report attributes this to FBA's linear programming, which cannot represent the threshold effect of losing one subunit of a multi-subunit complex. [src: discoveries]

### Unannotated genes and ACIAD3522

ACIAD3137 (UPF0234/YitK) and ACIAD2176 (DUF2280) correlate at r > 0.98 with Complex I genes across 8 growth conditions. [src: discoveries] Neither has an FBA reaction mapping or an assigned metabolic function. [src: discoveries] The report suggests that this near-perfect cofitness with the nuo operon points to a physical or regulatory association with Complex I. [src: discoveries]

ACIAD3522 has a growth ratio of 0.013 on acetate, which is essentially lethal. It shows no defect on quinate (1.39) or glucose (1.39). [src: discoveries] This is the largest condition-specific effect of any single gene in the 2,034-gene growth matrix. [src: discoveries] FBA predicts zero flux through it in all conditions. [src: discoveries] Its biological role is unknown. Its acetate specificity suggests an NADH-linked reaction uniquely required for acetate catabolism. [src: discoveries]

### Condition-specific genes in the deletion-phenotype data

The adp1_deletion_phenotypes report identifies 625 condition-specific genes that map to expected metabolic pathways. [src: discoveries] Of the dispensable genes, 31% have condition-specificity scores ≥ 1.0. [src: discoveries] The top genes for each carbon source are the enzymes biochemically predicted to be required:

- Urea: urease subunits. [src: discoveries]
- Quinate: protocatechuate 3,4-dioxygenase. [src: discoveries]
- Glucose: Entner-Doudoroff enzymes. [src: discoveries]
- Acetate: the glyoxylate shunt. [src: discoveries]
- Lactate: a lactate-responsive regulator. [src: discoveries]

## 2026-02: [fitness_modules] PFam domains are essential for module enrichment — KEGG KOs …

This part of the Discoveries Log covers two lines of work. The first is the phenotype landscape and deletion-collection coverage of [[entities/acinetobacter-baylyi-adp1]] (ADP1). The second is the fitness_modules analysis across 32 bacteria, with notes on Fitness Browser schema and tooling. The ADP1 results come from clustering and coverage comparisons. The module results come from reported validation metrics, with before/after comparisons for each methodological fix. [src: discoveries]

### ADP1 phenotype landscape

ADP1 gene phenotypes form a continuum, not discrete modules, with one exception. Hierarchical clustering of 2,034 genes by 8-condition growth profiles gave an optimal K=3 with silhouette=0.24, so there were no discrete functional modules. [src: discoveries] The exception is a tight quinate-specific module of 24 genes, the aromatic degradation pathway. [src: discoveries] The report concludes that gene essentiality varies continuously across conditions, which supports the Guzman et al. (2018) adaptive-flexibility framework. [src: discoveries]

### Deletion-collection coverage bias

Of 2,593 TnSeq-dispensable genes, 272 (10.5%) lack deletion-collection growth data. [src: discoveries] The missing genes differ systematically from the represented ones:

- They are shorter (813 vs 981 bp). [src: discoveries]
- They are less annotated (91% vs 100% RAST). [src: discoveries]
- They are less conserved in the pangenome (76.5% core vs 93.3%, p=1.4e-20). [src: discoveries]
- They are enriched for hypothetical proteins (q=2.4e-25). [src: discoveries]

The report concludes that the deletion collection is biased toward well-characterized, conserved genes. [src: discoveries]

### Robust ICA fitness modules

Robust independent component analysis (ICA), using 30-50 FastICA runs plus DBSCAN clustering, finds 17-52 stable modules per organism across 32 bacteria. [src: discoveries] Of these modules, 94.2% have significantly elevated within-module cofitness (Mann-Whitney U, p < 0.05; mean |r| = 0.34 vs background 0.12). [src: discoveries] Average genomic adjacency enrichment is 22.7× across organisms, which the report reads as evidence that modules capture operon-like co-regulated groups. [src: discoveries] See also [[entities/independent-component-analysis-fitness-modules]] and [[concepts/fitness-modules-essential-genes-and-condition-specific-gene-function]].

The initial membership rule failed, and a threshold change fixed it. D'Agostino K² normality-based thresholding gave 100-280 genes per module, which the report calls biologically meaningless. [src: discoveries] The report places the fault in deciding which genes belong to a module, not in the ICA components. [src: discoveries] An absolute threshold (|Pearson r| ≥ 0.3 with the module profile, max 50 genes) reduced modules to 5-50 genes. [src: discoveries] It raised cofitness enrichment from 59% to 94.2%. [src: discoveries] It also raised within-module |r| from 0.047 to 0.34, as a mean across 32 organisms. [src: discoveries]

Experiment count affected pilot signal strength, but stable modules still appeared with few experiments. Caulo (198 experiments) had the weakest pilot signal, with 2.9x correlation enrichment vs 31x for DvH. [src: discoveries] Organisms down to 104 experiments (Ponti) still produced stable modules. [src: discoveries] The report recommends capping components at 40% of experiments, because higher ratios cause FastICA convergence failures and extreme slowness. [src: discoveries]

### Cross-organism module families

Aligning modules with bidirectional best hit (BBH) ortholog fingerprints revealed 156 module families spanning 2+ organisms. [src: discoveries] Of these, 28 span 5+ organisms. [src: discoveries] The largest spans 21 of 32 organisms across Proteobacteria, Bacteroidetes, Firmicutes, and Archaea, which the report interprets as evidence of deeply conserved fitness regulons. [src: discoveries]

Ortholog scope strongly changed this result. The comparison was between BBH pairs from 5 organisms (10K pairs, 1,861 ortholog groups, OGs) and from all 32 organisms (1.15M pairs, 13,402 OGs). [src: discoveries] Using only 5-organism orthologs initially gave just 27 families, none spanning more than 4 organisms. [src: discoveries] Expanding to all organisms changed the results as follows:

- Module families went from 27 to 156 (6x). [src: discoveries]
- Families spanning 5+ organisms went from 0 to 28. [src: discoveries]
- Family-backed predictions went from 31 (4%) to 493 (56%). [src: discoveries]

The report's lesson is to extract orthologs for all organisms in the analysis, not a pilot subset. The ortholog graph is not additive, because adding organisms creates new transitive connections. [src: discoveries]

### Functional enrichment of modules

The initial enrichment pipeline (KEGG + SEED + TIGRFam, min_annotated=3) annotated only 8.2% of modules (92/1,116). [src: discoveries] The report's stated root cause is that KEGG ortholog (KO) groups average ~1.2 genes per term. Modules of 5-50 members therefore almost never have 3+ genes sharing a KO. [src: discoveries] Adding PFam domains (814 terms with 2+ genes vs TIGRFam's 88) and lowering the overlap threshold to 2 raised annotation to 79.7% (890/1,116). [src: discoveries] PFam is the dominant annotation source, and it provides domain-level labels that match module granularity. [src: discoveries]

These changes had further effects:

- Predictions rose from 878 to 6,691 (7.6×), now covering all 32 organisms. [src: discoveries]
- Annotated families rose from 32 to 145 out of 156 (93%). [src: discoveries]
- Caulo, Methanococcus_S2, and Korea went from 0 enrichments to 24-29 enriched modules. [src: discoveries]

### Fitness Browser schema and tooling notes

The report records these schema deviations from the documentation:

- `keggmember` uses `keggOrg`/`keggId`, not `orgId`/`locusId`, and must be joined through `besthitkegg`. [src: discoveries]
- `kgroupec` uses `ecnum`, not `ec`. [src: discoveries]
- `seedclass` has `orgId, locusId, type, num`, not a subsystem/category hierarchy. [src: discoveries]
- `fitbyexp_*` tables are long format, not pre-pivoted as documented. [src: discoveries]

On tooling, `get_spark_session` from `berdl_notebook_utils.setup_spark_session` works in regular Python scripts on JupyterHub, not just notebook kernels. This allows command-line analysis pipelines without `jupyter nbconvert`. [src: discoveries] The auto-import in `/configs/ipython_startup/00-notebookutils.py` affects only notebook kernels. [src: discoveries]

## 2026-02: [conservation_vs_fitness] SEED functional categories distinguish essential from …

Module-based methods predict biological process, not specific KOs, and essential and fitness-important genes are modestly but consistently enriched in the core genome. [src: discoveries] Some results come from single projects, and the report flags several as modest or limited. [src: discoveries] See also [[concepts/essential-genes-and-core-genome-conservation]] and [[concepts/fitness-modules-essential-genes-and-condition-specific-gene-function]].

### Modules versus ortholog transfer

Ortholog transfer works far better than fitness modules for gene-level function prediction. In a held-out KEGG ortholog (KO) prediction benchmark across 32 organisms, ortholog transfer reached 95.8% precision and 91.2% coverage. [src: discoveries] Module-ICA (independent component analysis) had <1% precision at the KO level. [src: discoveries] The report calls this expected, not a failure. It says modules capture process-level co-regulation, validated by 94.2% cofitness enrichment and 22.7× adjacency enrichment, not specific molecular function. [src: discoveries] An ABC (ATP-binding cassette) transporter module groups binding, permease and ATPase subunits that each have a different KO. The report therefore frames module predictions as "involved in [biological process]", not "has function [specific KO]". [src: discoveries]

### Enrichment parameter calibration

The min_annotated parameter is the minimum number of overlapping genes needed to test for enrichment. It must be calibrated to the granularity of the annotation database. [src: discoveries] For gene-specific KEGG KOs (about 1 gene per term), min_annotated=3 eliminates nearly all tests. [src: discoveries] For domain-level PFam annotations, min_annotated=2 works well with false discovery rate (FDR) correction. [src: discoveries] Fisher's exact test handles small counts correctly. Statistical validity comes from FDR correction across all tests, not from requiring large overlaps per test. [src: discoveries]

### Essential genes and the core genome (conservation_vs_fitness)

Essential genes are modestly enriched in the core genome. Across 33 diverse bacteria, putative essential genes (no transposon insertions in random barcode transposon sequencing, RB-TnSeq) were 86.1% core versus 81.2% for non-essential genes. The median odds ratio (OR) was 1.56, and 18/33 organisms were significant after Benjamini-Hochberg false discovery rate (BH-FDR) correction. [src: discoveries] The report calls the enrichment real but modest, because most genes in well-characterized bacteria are core regardless of essentiality. [src: discoveries] The signal is strongest in organisms with larger clades, which give more reliable core classification. [src: discoveries]

Essential genes fall into classes with different annotation profiles:

- Essential genes mapping to core clusters are 41.9% enzymes and 13.0% hypothetical. They form a well-characterized backbone of ribosomes, DNA replication, cell wall and cofactor biosynthesis. [src: discoveries]
- Essential-auxiliary genes (essential but absent from some strains) are 13.4% enzymes and 38.2% hypothetical. [src: discoveries]
- Essential-unmapped genes (strain-specific, no pangenome match) are 44.7% hypothetical. The report calls them prime targets for functional discovery. [src: discoveries]

Relative to non-essential genes, essential-core genes differ in SEED functional categories as follows:

| SEED category | Difference (pp) |
|---|---|
| Protein Metabolism | +13.7 [src: discoveries] |
| Cofactors/Vitamins | +6.2 [src: discoveries] |
| Cell Wall | +3.9 [src: discoveries] |
| Carbohydrates | -7.9 [src: discoveries] |
| Amino Acids | -5.6 [src: discoveries] |
| Membrane Transport | -4.0 [src: discoveries] |

The report describes the depleted categories as conditionally important rather than universally essential. [src: discoveries] It says this aligns with Rosconi et al. (2022), who found that pan-genome composition influences essentiality in *S. pneumoniae*. [src: discoveries]

### A data-join pitfall

The Fitness Browser (FB) aaseqs download uses RefSeq-style locus tags (e.g., ABZR86_RS*) for some organisms. The FB gene table uses the original annotation tags (e.g., N515DRAFT_*). [src: discoveries] This caused a complete join failure for Dyella79 (0% merge rate). Only 1 of 34 organisms was affected. The report advises that any pipeline joining aaseqs-derived data with gene-table data should verify locus-tag consistency. [src: discoveries]

### Fitness effects and conservation (fitness_effects_conservation)

Conservation rises quantitatively with fitness importance. Across 194,216 protein-coding genes in 43 bacteria, core fraction fell from 82% for essential genes to 66% for always-neutral genes, a 16-percentage-point gradient. [src: discoveries] The same pattern held when genes were binned by strongest negative fitness effect. Genes with min_fit < -3 were 78% core, against 66% for min_fit near 0. [src: discoveries] It also held for fitness breadth. Genes important in 20+ conditions were 79% core, against 66% for 0 conditions. [src: discoveries] The report concludes the essentiality–conservation link is quantitative, not binary. [src: discoveries]

Core genes also show more beneficial deletion effects. This runs counter to the expectation that accessory genes carry a cost. 24.4% of core genes were ever beneficial when deleted, versus 19.9% of auxiliary genes (OR=0.77 for auxiliary vs core, p=5.5e-48). [src: discoveries] The report attributes this to core genes' participation in more pathways and trade-offs. It says this challenges the "streamlining" model of accessory genes as metabolic burdens. [src: discoveries]

Condition-specific phenotypes follow the same direction. Genes with strong condition-specific phenotypes (from the FB specificphenotype table) were 77.3% core versus 70.3% for genes without them (OR=1.78, p=1.8e-97). [src: discoveries] The report says this contradicts the intuition that condition-specific fitness means niche-specific accessory genes. It proposes that core genes show detectable effects because they sit in well-characterized, essential pathways. [src: discoveries]

### Modules and conservation (module_conservation)

Fitness modules are enriched in the core genome. ICA fitness modules were 86.0% core versus 81.5% baseline across 29 organisms. Fisher OR=1.46 (p=1.6e-87), and the per-organism paired Wilcoxon test gave p=1.0e-03, with 22/29 organisms showing enrichment. [src: discoveries] 59% of modules are >90% core genes. [src: discoveries] The report concludes that the core genome is functionally coherent at the module level as well as structurally conserved. [src: discoveries]

One gradient is absent. The report calls it surprising that module families spanning more organisms do not have higher core fractions (Spearman rho=-0.01, p=0.914). [src: discoveries] The report reads this as a ceiling effect from the ~82% baseline core rate, not as evidence against the conservation–function relationship. [src: discoveries]

A structural limit applies. No essential genes appear in any of the 1,116 fitness modules across 32 organisms. [src: discoveries] ICA decomposes fitness variation, and essential genes lack insertions and fitness data. Fitness modules therefore capture only the non-essential part of the genome's functional architecture. [src: discoveries]

### Trade-off genes (core_gene_tradeoffs)

In core_gene_tradeoffs, 25,271 genes (17.8%) are true trade-offs. They are important (fit < -1) in some conditions and burdensome (fit > 1) in others. [src: discoveries] These genes are 1.29x more likely to be core (OR=1.29, p=1.2e-44). [src: discoveries] The report explains this by core genes' participation in more pathways with condition-dependent costs and benefits. On its account, this is why core genes are both more burdensome and more essential than accessory genes. [src: discoveries]

## 2026-02: [env_embedding_explorer] AlphaEarth embeddings encode geographic signal, but …

### Core-burden paradox by function (core_gene_tradeoffs)

The report says the paradox is not a uniform property of the core genome. It reflects the trade-off architecture of specific functional systems. [src: discoveries] Core genes are more burdensome in RNA Metabolism (+12.9pp), Motility/Chemotaxis (+7.8pp) and Protein Metabolism (+6.2pp). [src: discoveries] Cell Wall reverses the pattern: non-core cell wall genes are more burdensome (-14.1pp). [src: discoveries]

The report also reads genes that are burdensome in the lab yet core in the pangenome as a natural-selection signature. It counts 28,017 "costly + conserved" genes. [src: discoveries] It calls them the strongest evidence for purifying selection in natural environments. The reasoning is that every strain keeps them despite their cost, so nature must require them under conditions the lab does not capture. [src: discoveries] Two other classes are 5,526 costly and dispensable genes, which are candidates for ongoing gene loss, and 21,886 neutral and dispensable genes, which are described as niche-specific. [src: discoveries]

### Essential genes across 48 bacteria (essential_genome)

Few ortholog families are essential everywhere, and most essential families vary between organisms. The analysis covers 48 bacteria, 221,005 genes and 17,222 ortholog families. [src: discoveries] Of the 17,222 families, 859 (5.0%) are essential in every organism where the family has members. [src: discoveries] A further 4,799 (27.9%) are variably essential, and 11,564 (67.1%) are never essential. [src: discoveries] The report takes variable essentiality as showing that genomic context strongly shapes which genes an organism needs to survive. [src: discoveries]

Fifteen families are essential in every organism. They are the ribosomal proteins rpsC, rplW, rplK, rplB, rplA, rplF, rps11, rpsJ, rpsI and rpsM. The others are chaperonin groEL, CTP synthase pyrG, translation elongation factor G fusA, valyl-tRNA synthetase valS and geranyltranstransferase SelGGPS. [src: discoveries] The report calls these the irreducible essential core of bacterial life. [src: discoveries]

Orphan essentials are essential genes with no orthologs in any other Fitness Browser (FB) organism. There are 7,084 of them. [src: discoveries] Of these, 58.7% are annotated as hypothetical proteins, against 8.2% of universally essential genes. [src: discoveries] The report calls orphan essentials prime candidates for novel biology. [src: discoveries]

Conservation within species differs by group. Universally essential genes are 91.7% core, compared with 80.7% for non-essential genes. [src: discoveries] Also, 71% of universally essential families are 100% core across all genomes in their species. [src: discoveries] Orphan essentials are only 49.5% core. The report describes them as strain-specific essential functions that are not conserved across species. [src: discoveries]

Non-essential orthologs that sit in independent component analysis (ICA) fitness modules gave 1,382 function predictions for hypothetical essential genes across 48 organisms. [src: discoveries] All of these predictions are backed by cross-organism module family conservation. [src: discoveries] The report concludes that module context from non-essential orthologs can reveal functions of essential genes that fitness-based methods cannot see. [src: discoveries]

### Clinical sampling bias (ecotype_env_reanalysis, env_embedding_explorer)

**Ecotype reanalysis.** This is a null result. The authors hypothesized that clinical sampling bias explained the weak environment effect in the ecotype analysis (median partial correlation 0.003). [src: discoveries] Stratifying 213 species by dominant environment type (47% human-associated, 21% environmental) showed the opposite. Human-associated species had higher median partial correlations (0.084) than environmental species (0.051), with Mann-Whitney p=0.83. [src: discoveries] The report concludes that phylogeny dominates regardless of sample environment. It also says the geographic signal in embeddings and the environment-gene content relationship are distinct phenomena. [src: discoveries]

The classification harmonized isolation_source from 5,774 values into 12 categories. [src: discoveries] Of the 224 ecotype species, 106 are majority human-associated (gut + clinical). [src: discoveries] Only 47 (21%) are majority environmental (Soil, Marine, Freshwater, Extreme, Plant). [src: discoveries] The report calls this more systematic than the earlier manual species-level categorization. It says the result confirms the clinical bias but shows it does not confound the ecotype results. [src: discoveries]

**Embedding explorer.** Here the bias does matter for the geographic signal in AlphaEarth embeddings. Among 83,287 genomes with embeddings, 38% are human-associated (clinical 20%, gut 16%, other 2%). Soil, marine and freshwater are 7% each. [src: discoveries] The report attributes this to NCBI's bias toward pathogen sequencing. Clinical isolates have good geographic metadata from epidemiological tracking, so they disproportionately have embeddings. [src: discoveries]

Environmental genome pairs show a 3.4x ratio in embedding cosine distance between nearby (<100 km, mean=0.27) and far (>10K km, mean=0.90) pairs. [src: discoveries] Human-associated samples show only a 2.0x ratio (0.37 vs 0.75). [src: discoveries] The report explains this by saying hospitals worldwide have similar satellite imagery, so human-associated genomes have homogeneous embeddings regardless of geography. [src: discoveries]

### Caveats

- The pooled all-samples curve (2.0x ratio) is dominated by the 38% human-associated fraction. The report says it substantially underestimates the true geographic signal. [src: discoveries]
- The report recommends that analyses using AlphaEarth embeddings as environment proxies stratify by sample type, or at minimum exclude human-associated samples. [src: discoveries]
- The embedding explorer entry proposed that clinical bias may partly explain the weak environment signal in ecotype_analysis (median partial correlation 0.0025). [src: discoveries] The reanalysis did not support this. [src: discoveries]
- The reading of costly-and-conserved genes as evidence of purifying selection is the report's interpretation. [src: discoveries]

## 2026-02: [nmdc_community_metabolic_ecology] Black Queen Hypothesis is detectable at …

This part of the log covers three projects. The AlphaEarth embedding check found coordinate clustering and missing values. The ENIGMA contamination-functional project found mostly null confirmatory results, with a positive signal that the report frames as exploratory. The NMDC community metabolic ecology analysis found a modest Black Queen Hypothesis (BQH) signal in amino acid pathways. [src: discoveries]

### AlphaEarth embeddings: institutional clustering and missing values

In the AlphaEarth genome dataset, 30,469 genomes (36.6%) cluster at coordinates with >50 genomes of >10 species. [src: discoveries] Some flagged locations are legitimate research field sites: Rifle, CO (1,883 genomes, a DOE field site), Saanich Inlet (1,529 genomes, an oceanographic time series) and Siberian soda lakes (812 genomes, extremophile campaigns). [src: discoveries] The report says the institutional-address heuristic needs refinement. It proposes checking isolation_source homogeneity at each location to separate field sites from institutional addresses. [src: discoveries]

Separately, 3,838 of 83,287 genomes have NaN (not a number) in at least one of the 64 embedding dimensions. [src: discoveries] The cause is unclear. It may be missing satellite imagery or coordinates outside satellite coverage, and affected genomes must be filtered before embedding-based analysis. [src: discoveries]

### ENIGMA contamination and function: a conditional signal

Primary univariate associations were non-significant for defense, stress, metabolism and mobilome outcomes in both mapping modes (108 overlap samples). [src: discoveries] Adding mapped-coverage-aware sensitivity models made the contamination-defense association significant. Coverage-adjusted ordinary least squares (OLS) gave contamination p = 3.98e-4 (relaxed) and 3.54e-3 (strict). The high-coverage subset Spearman test gave p = 0.0207 (relaxed) and 0.0098 (strict). [src: discoveries] The report concludes the strongest signal depends on mapping coverage and model specification, not on a broad effect across outcomes. [src: discoveries]

Mapping mode matters. When strict and relaxed modes were computed independently in NB02, 1,140 of 1,590 genus-feature pairs differed (~71.7%). Site stress scores differed for all 108 samples. [src: discoveries] The report therefore says strict-versus-relaxed sensitivity should not be approximated by copied feature tables. [src: discoveries]

Taxonomy limits a species-level test. The table enigma_coral.ddt_brick0000454 provides taxonomy only through Genus. [src: discoveries] A species-proxy mode (species_proxy_unique_genus) kept 150 genera with unique genus-to-single-GTDB-clade mappings. Mean mapped abundance fell to 0.031, against 0.343 in strict and relaxed genus modes. [src: discoveries] In this mode the defense trend was positive but non-significant (rho=0.169, p=0.081). [src: discoveries] The report says true species-level gains likely need higher-resolution taxonomy or metagenomic mapping. [src: discoveries]

After explicit confirmatory and exploratory labels and global Benjamini-Hochberg false discovery rate (BH-FDR) correction in NB03, the confirmatory genus-level defense Spearman tests stayed null (p=0.546/0.483; q=0.862/0.849). [src: discoveries] The strongest surviving signal was exploratory: the relaxed coverage-adjusted defense model kept q=0.046. [src: discoveries] Strict and other sensitivity signals attenuated above q<0.1. [src: discoveries] The report recommends prioritizing the null confirmatory evidence and framing positive results as exploratory. [src: discoveries]

The null is not specific to one contamination index. Four index constructions were tested: all-metals composite, uranium-only, top-3 variance metals and principal component 1 (PC1) of a principal component analysis (PCA). None gave significant confirmatory associations after FDR correction (all q=0.546 across 8 confirmatory-variant tests). [src: discoveries] See also [[entities/enigma]].

### NMDC community metabolic ecology: Black Queen signal in amino acids

The analysis correlated community-weighted GapMind amino acid biosynthesis completeness with ambient amino acid metabolomics across 131 NMDC soil samples, using Spearman correlation. [src: discoveries] Of 13 tested amino acid pathways, 11 trend in the BQH-predicted negative direction (binomial sign test p = 0.011). [src: discoveries] Two pathways reach BH-corrected significance (q < 0.05). Leucine has r = −0.390, q = 0.022, n = 62. Arginine has r = −0.297, q = 0.049, n = 80. [src: discoveries] The report notes that both are among the most energetically expensive pathways to synthesize (leucine 37 ATP (adenosine triphosphate) equivalents, arginine 26). It calls this consistent with BQH. [src: discoveries] The report describes the work as the first demonstration that community-weighted pangenome completeness correlates with measured metabolite pools at landscape scale using public multi-omics data. [src: discoveries] See [[entities/gapmind]] and [[entities/nmdc-integrated-collections]].

Two amino acids are not significant. Methionine has the largest effect (r = −0.496) but is underpowered (n = 18, q = 0.117). [src: discoveries] Tyrosine is a non-significant anti-BQH outlier (r = +0.42). The report suggests phenylalanine hydroxylation may provide an alternative tyrosine source. [src: discoveries] The leucine signal holds under soil-only stratification (q = 0.022 unchanged) and study-level blocking. [src: discoveries]

### Carbon substrate range as a confounder

In a PCA of the 220-sample × 80-pathway GapMind completeness matrix, PC1 explains 49.4% of variance. It nearly separates Soil from Freshwater (Mann-Whitney p < 0.0001; median PC1 Soil = +3.86, Freshwater = −6.28). [src: discoveries] PC1 loadings are dominated by carbon utilization pathways (glucuronate, fumarate, succinate, cellobiose, galactose), not amino acid pathways. [src: discoveries] Amino acid pathways load more on PC2 (16.6%), which separates sub-clusters within Soil. [src: discoveries] Of 18 amino acid pathways, 17 differ significantly across ecosystem types (q < 0.05, Kruskal-Wallis). The report names carbon substrate availability, not biosynthesis capacity, as the primary driver. [src: discoveries] It warns that carbon substrate range will confound amino acid pathway analyses unless controlled. It recommends PC1-residualized or ecosystem-stratified BQH tests. [src: discoveries]

### Study composition of the NMDC dataset

In the 131-sample dataset, 95% of samples (125/131) come from one NMDC study (nmdc:sty-11-r2h77870). The other 6 come from a second study. [src: discoveries] The report concludes that cross-study liquid chromatography-mass spectrometry (LC-MS) protocol heterogeneity is effectively absent as a confounder. [src: discoveries] It also says the leucine signal is internally consistent within one analytical protocol. [src: discoveries] The report recommends counting study-level sample representation before treating aggregate NMDC metabolomics as cross-study data. [src: discoveries]

## 2026-02: [pangenome_pathway_geography] Ecological niche breadth strongly predicts …

This part of the log covers three projects: NMDC metabolomics annotation limits, pangenome pathway geography across 1,872 bacterial species, and functional dark matter prioritization. The pangenome section reports correlations, and the report's explanations of them are interpretation. The dark gene results combine counts, a concordance test and organism-selection analyses. [src: discoveries]

### NMDC metabolomics annotation limits

Only ~2% of compounds in `nmdc_arkin.metabolomics_gold` have KEGG compound IDs (identifiers) populated. [src: discoveries] The report states that pathway matching must rely on compound-name substring patterns rather than KEGG-based ontologies. [src: discoveries] See [[concepts/ontology-versus-name-pattern-categorization-in-pathway-enrichment-tests]] and [[entities/nmdc-integrated-collections]].

Several caveats apply to the name-pattern approach:
- Substring matching risks collisions, for example 'leucine' matches inside 'isoleucine'. The report recommends first-match-wins ordering, with longer and more specific patterns first. [src: discoveries]
- Chorismate is rarely detected. Shikimic acid and 3-dehydroshikimic acid serve as upstream proxies, but they reflect precursor availability, not chorismate pool size. [src: discoveries]
- Three amino acid pathways (cys, his, lys) remain untestable in the 175-sample overlap cohort because their compounds were not detected. [src: discoveries]

### Pangenome pathway geography

The analysis covers 1,872 bacterial species with complete pangenome, GapMind pathway and AlphaEarth embedding data. [src: discoveries] Niche breadth, measured from embedding diversity, links to pathway completeness much more strongly than pangenome openness does. See [[concepts/pangenome-openness-and-its-correlates]], [[entities/gapmind]] and [[entities/alphaearth-environmental-embeddings]]. [src: discoveries]

| Relationship | Result |
|---|---|
| Pangenome openness vs pathway completeness | r=0.107, p=3.6e-6, weak positive [src: discoveries] |
| Pangenome openness vs pathway variability (std dev) | r=0.066, p=0.004 [src: discoveries] |
| Niche breadth (AlphaEarth embedding diversity) vs pathway completeness | r=0.392, p=7.1e-70, the strongest hypothesis signal [src: discoveries] |
| Embedding variance vs pathway completeness | r=0.412, p=1.8e-77 [src: discoveries] |
| Geographic distance alone vs pathway completeness | r=0.360, p=1.8e-58, weaker than embedding-based metrics [src: discoveries] |
| Pangenome openness vs niche breadth | r=0.324, p=5.6e-47 [src: discoveries] |
| Core fraction vs niche breadth | r=-0.445, p=1.4e-91 [src: discoveries] |

The report suggests that accessory genes enable metabolic heterogeneity within species. [src: discoveries] It asserts that species with broader niches need more complete metabolic toolkits, and that pangenome flexibility enables adaptation to diverse environments. [src: discoveries] It attributes the advantage of embeddings over geography to their capture of ecological context (soil, marine, clinical). [src: discoveries]

Coverage limits the results. Only 6.8% of species (1,872/27,690) have at least 5 genomes with embeddings. Most NCBI genomes, especially clinical isolates, lack latitude/longitude metadata. [src: discoveries] See [[concepts/clinical-sampling-bias-in-environment-embedding-analyses]].

### Functional dark matter

The report concludes that targeted experimental validation, not computational inference, is the key bottleneck for most dark genes. [src: discoveries] Its counts show both broad conservation of dark ortholog groups and substantial evidence for many dark genes. [src: discoveries]

- **Conservation:** 55.9% of dark gene ortholog groups (OGs) are kingdom-level, present across multiple phyla. [src: discoveries] Across 27,690 species (NB11b), species counts per OG range from 1 to 27,482 (median 135). [src: discoveries] COG0468, COG0443 and COG0491 are top-ranked unknowns present in virtually all sequenced bacterial genomes, with zero functional evidence. [src: discoveries]
- **Darkness spectrum:** Of 57,011 dark genes, only 4,273 (7.5%) are T1 Void with zero evidence. [src: discoveries] T4 Penumbra holds 22,500 (39.5%), with 3-4 converging evidence lines from fitness phenotype, domain annotation, ortholog group and module membership. [src: discoveries]

### Ecological concordance and validation

- Across 47 testable dark gene clusters, 29 (61.7%) show directional concordance between laboratory fitness condition and carrier-genome environment (Fisher's combined p=0.031). [src: discoveries]
- NMDC validation confirmed all 4 pre-registered abiotic predictions (nitrogen, pH, and anaerobic vs dissolved oxygen) and all 7 pre-registered trait predictions. [src: discoveries]
- The report presents this as the first systematic evidence that Fitness Browser laboratory phenotypes reflect ecological function, validating fitness as a proxy for in situ importance. [src: discoveries]
- 65 dark gene OGs show conserved fitness effects across 3+ organisms. [src: discoveries]
- Null result: dark gene concordance is statistically indistinguishable from annotated genes (Mann-Whitney p=0.17). [src: discoveries]
- Motility-related dark genes show the strongest cross-organism concordance, suggesting conserved but incompletely annotated chemotaxis machinery. [src: discoveries]

### Organism prioritization

Two covering routes pick largely the same organisms but rank them differently. See [[concepts/organism-selection-and-taxonomic-coverage-bias-for-experimental-characterization-of-dark-genes]]. [src: discoveries]

- Shewanella MR-1 contributes 25/100 top fitness-active candidates, has 587 scored dark genes, and covers 20.8% of the top-500 in just 3 experiments (stress, nitrogen, carbon). [src: discoveries] The report attributes this to deep coverage of 121 conditions, a large dark gene complement, and 142 genes with |fit| >= 4. [src: discoveries]
- Under conservation-weighted Route B, Sinorhizobium meliloti ranks first (1,630 OGs, 195 kingdom-level gaps) because it covers more conserved unknowns. [src: discoveries]
- Evidence-weighted Route A (NB09) and Route B (NB11) covering sets each select 42 organisms covering ~95% of priority, and share 39. [src: discoveries] Route A puts MR-1 first for deep condition evidence, and Route B puts S. meliloti first for the most kingdom-level gaps. [src: discoveries] The report says this complementarity enables targeted hypothesis testing (Route A) and novel function discovery (Route B). [src: discoveries]
- Adding 25 non-Fitness Browser organisms (Bacillota, Actinomycetota, Campylobacterota) yields 50 selected organisms spanning 6 phyla, versus 4 for Fitness Browser-only selection. [src: discoveries] In this extended set, Pseudomonas aeruginosa PAO1 ranks #1 (3,713 OGs) and Mycobacterium tuberculosis ranks #6, the first Actinomycetota. [src: discoveries]
- Null result: B. subtilis and S. aureus are not selected, because their kingdom-level OGs are already covered by selected Pseudomonadota. [src: discoveries] They remain valuable for studying dark genes in a native Gram-positive context, but add no unique OG coverage. [src: discoveries]

## 2026-02: [pseudomonas_carbon_ecology] Host-associated Pseudomonas show dramatic loss of …

This part of the Discoveries Log covers Pseudomonas carbon catabolism, pathway completeness versus fitness and pangenome openness, and whether shared NaCl stress confounds metal-fitness results. [src: discoveries] The report also offers interpretations; I mark those where they appear.

### Pseudomonas carbon catabolism

A GapMind analysis of 433 Pseudomonas species (12,732 genomes) found that the *P. aeruginosa* group has almost completely lost plant-derived sugar catabolism, compared with the *P. fluorescens/putida* group. [src: discoveries] Of 62 carbon pathways, 43 differ significantly (FDR < 0.05, false discovery rate). [src: discoveries] The largest differences are in these pathways:

| Pathway | Effect |
|---|---|
| xylose | +74 pp [src: discoveries] |
| ribose | +64 pp [src: discoveries] |
| arabinose | +63 pp [src: discoveries] |
| galacturonate | +60 pp [src: discoveries] |
| myo-inositol | +59 pp [src: discoveries] |

Amino acid catabolism stays near-universal (>99.5%) in both groups. The report calls this consistent with Palmer et al. (2007), who described cystic fibrosis (CF) sputum as amino acid-dominated. [src: discoveries]

Among free-living species, carbon profiles are significantly associated with isolation environment (PERMANOVA p = 0.006, permutational multivariate analysis of variance). [src: discoveries] The predictive accuracy is modest: random-forest balanced accuracy is 0.41, against 0.25 expected by chance. [src: discoveries] D-serine, arabinose, rhamnose and fucose are the most discriminating pathways. [src: discoveries]

### Pathway completeness versus fitness

Seven Fitness Browser organisms were crossed with 23 GapMind pathways and sorted into four categories. [src: discoveries] Of these, 35.4% were Active Dependencies (complete and fitness-important). [src: discoveries] 41.0% were Latent Capabilities (complete but fitness-neutral in rich media). [src: discoveries] 14.9% were Incomplete but Important, and 8.7% were Missing. [src: discoveries]

All Latent Capabilities became fitness-important under condition-specific analysis (nitrogen limitation, stress or carbon source shifts). [src: discoveries] The report reads this as validating the core_gene_tradeoffs finding that laboratory fitness underestimates natural selection on metabolic genes. That is the report's interpretation. [src: discoveries]

The report gives the chain as besthitkegg → keggmember → kgroupec → keggconf → GapMind pathway. [src: discoveries] It describes this as simpler than the DIAMOND blastp pipeline that conservation_vs_fitness used, and as covering more organisms. [src: discoveries]

### Metabolic variability and pangenome openness

Pathway variability correlated with pangenome openness across bacteria. [src: discoveries] In 2,810 species with at least 10 genomes each, variable pathways correlated with openness at Spearman rho=0.327 (p=7.2e-71). [src: discoveries] After controlling for genome count, the partial Spearman rho was 0.530 (p=2.83e-203). [src: discoveries] The signal held in 18 of 21 phylogenetic groups tested. [src: discoveries] Amino acid biosynthesis pathways (leu, val, arg, lys, thr) showed the largest accessory dependence gap, about 0.14. [src: discoveries] The report calls this much stronger than the null result for environmental and phylogenetic predictors in pangenome_openness, and concludes that metabolic pathway variability is a genuine predictor. [src: discoveries] See [[concepts/pangenome-openness-and-its-correlates]].

Clustering of 225 species (at least 50 genomes and at least 3 variable pathways) by GapMind profiles gave a median of 4 metabolic ecotypes per species, with a maximum of 8. [src: discoveries] More ecotypes correlated with greater openness (partial rho=0.322, p=8.0e-07). [src: discoveries] *Alistipes onderdonkii* and *Barnesiella intestinihominis* each had 8 ecotypes. [src: discoveries]

### Metal fitness and shared NaCl stress

The report concludes that the original [[entities/metal-fitness-atlas]] core-enrichment result (OR=2.08, odds ratio) is not an artifact of shared sodium chloride (NaCl) stress. [src: discoveries] Across 19 organisms and 14 metals, 39.8% of metal-important genes were also NaCl-important. The report attributes this to shared stress biology (cell envelope, ion homeostasis, DNA repair) rather than chloride counter-ion contamination. [src: discoveries] Zinc sulfate, which delivers 0 mM Cl⁻, showed 44.6% NaCl overlap and the highest DvH profile correlation (r=0.715). That correlation exceeds most chloride-delivered metals. [src: discoveries]

After removing the roughly 40% of metal-important genes that overlap NaCl stress, core-genome enrichment persisted for 12 of 14 metals. [src: discoveries] The metals the report calls essential (Mo, W, Se, Hg) showed stronger enrichment after correction, for example Mo delta +0.132 → +0.145. [src: discoveries]

In DvH, whole-genome fitness correlation with NaCl ranked as follows: Zn (r=0.72) > Mn (0.55) > Cu (0.53) > Co (0.50) > Hg (0.48) > Ni (0.45) > Al (0.42) > Mo (0.40) > U (0.35) > Se (0.34) > Cr (0.32) > W (0.30) > Fe (0.09). [src: discoveries] The report interprets this as follows. Metals that broadly displace cofactors share more genes with ionic stress. Metals that target specific pathways are distinct from general stress: Mo and W target molybdopterin, and Fe targets iron-sulfur clusters. [src: discoveries] See [[concepts/metal-tolerance-determinants-and-shared-stress-confounding]].

### Experiment-count caveat

*Synechococcus elongatus* had 12 NaCl dose-response experiments (0.5–250 mM), against 1–6 in other organisms. [src: discoveries] This made the n_sick >= 1 threshold much easier to meet and produced an 88.6% shared-stress rate. [src: discoveries] Excluding it lowered overall metal–NaCl overlap from 39.8% to 36.7%. [src: discoveries] The report recommends that NaCl fitness analyses account for experiment count when setting importance thresholds. [src: discoveries]

## 2026-02: [fw300_metabolic_consistency] Tryptophan overflow: converging evidence from four …

This part of the Discoveries Log covers tryptophan overflow in *Pseudomonas fluorescens* FW300-N2E3, database concordance for that strain, and Metal Fitness Atlas checks. The tryptophan argument rests on one strain and is interpretive. [src: discoveries] The metal checks use counts and tests across 24 organisms. [src: discoveries]

### Tryptophan overflow in FW300-N2E3

Four independent lines of evidence converge on a non-catabolic role for the tryptophan the strain releases. Web of Microbes (WoM) recorded FW300-N2E3 as producing tryptophan (Increased). [src: discoveries] Fitness Browser (FB) showed 231 genes with significant fitness on tryptophan. [src: discoveries] GapMind predicted a complete tryptophan biosynthesis pathway. [src: discoveries] In BacDive, 0/52 *P. fluorescens* strains could use tryptophan as a carbon source. [src: discoveries] The report calls this convergence a compelling case for overflow serving cross-feeding or signaling rather than catabolism. [src: discoveries] It says the finding is consistent with Fritts et al. (2021) and Ramoneda et al. (2023), who showed widespread soil-community amino acid cross-feeding and particularly common tryptophan auxotrophy. [src: discoveries]

### Database concordance for FW300-N2E3

Agreement between databases was high, but the report argues much of it was built in. All 13 WoM-produced metabolites that mapped to GapMind pathways had complete predictions, and all 13 also showed growth in FB experiments. [src: discoveries] The report reads this as validating GapMind for this strain, consistent with Price et al. (2022, 2024). [src: discoveries] The matched metabolites were common amino acids and organic acids with well-characterized pathways. [src: discoveries]

The reported 94% mean concordance across four databases breaks down as FB 21/21 = 100% (structural), GapMind 13/13 = 100% (structural) and BacDive 3/7 = 43% (informative). [src: discoveries] Overall, 37/41 comparisons were concordant (90.2%). [src: discoveries] A binomial test found no significant difference between BacDive utilization of WoM-produced metabolites (43%) and the species baseline (27.5%), p=0.40. [src: discoveries] The report calls the high concordance largely inevitable. FB always shows growth for metabolites used as sole C/N sources, and GapMind predicts complete pathways for common amino acids. [src: discoveries]

The 18 genes significant across all 21 FB metabolite conditions were amino acid biosynthesis enzymes, not substrate-specific genes. [src: discoveries] They include homoserine O-acetyltransferase, ATP (adenosine triphosphate) phosphoribosyltransferase, dihydroxy-acid dehydratase, isopropylmalate dehydrogenase, shikimate dehydrogenase and imidazoleglycerol-phosphate dehydratase. The report says these are essential on any minimal medium. [src: discoveries] It identifies the ~370 genes significant in only 1-2 conditions as the truly substrate-specific ones. [src: discoveries]

### Metal specificity and core enrichment

Most metal-important genes in the Metal Fitness Atlas appear to be specific to metals, not general stress genes. Of 7,609 metal-important gene records across 24 organisms, 4,177 (55%) were sick under metal stress but had a <5% sick rate across 5,945 non-metal experiments. [src: discoveries] Another 38% were "general sick", important across many conditions. [src: discoveries] The remaining 7% were "metal+stress", shared with other stresses. [src: discoveries] The report concludes that the gene set is not dominated by general stress response and that most are genuine metal tolerance determinants. [src: discoveries]

Core-genome enrichment partly supports the Atlas's two-tier model. Metal-specific genes were 84.8% core (pooled) versus 90.2% for general sick genes (Cochran-Mantel-Haenszel p=0.011). [src: discoveries] Both categories were enriched above the 79.8% baseline. [src: discoveries] General stress response (Tier 1) is more core than specialized metal resistance (Tier 2), but both are predominantly core. [src: discoveries] The report concludes that the accessory genome contributes only modestly to metal resistance machinery. [src: discoveries]

### Candidate genes

Three novel candidates stand out as metal-specific rather than pleiotropic:

- UCP030820/OG01015: oxidoreductase, 67% metal-specific, 7 metals. [src: discoveries]
- YebC/OG01383: transcriptional regulator/translation factor, 58%, 6 metals, 11 organisms. [src: discoveries]
- DUF1043-YhcB/OG03264: cell division protein, 50%, 5 metals. [src: discoveries]

In contrast, YfdZ (15%) and the Mla/Yrb system (0-25%) are pleiotropic. [src: discoveries] DUF39 is a general fitness factor (0% metal-specific, sick rate 0.64) despite spanning 8 metals. [src: discoveries]

The report cites Ignatov et al. 2025 as showing YebC is a translation factor for proline-rich proteins. [src: discoveries] Many metal homeostasis proteins, including the P-type ATPases CopA/ZntA and CDF transporters, contain proline-rich cytoplasmic loops. [src: discoveries] The report offers a hypothesis, not a result. Metal stress upregulates proline-rich transporters and creates a translation bottleneck that YebC resolves. Under non-metal conditions those transporters are not highly expressed, so YebC is dispensable. [src: discoveries]

### Correction: essential-metal specificity

An early analysis was wrong, and the corrected figures stand. A locusId type mismatch silently excluded DvH. This produced a misleading 0% specificity for Mo, W, Se and Mn, apparently because DvH's 608 non-metal experiments made specificity look impossible. [src: discoveries] After the fix, the metal-specificity values were manganese 61% [src: discoveries], molybdenum 61% [src: discoveries], tungsten 57% [src: discoveries] and selenium 46%. [src: discoveries] The report concludes the experiment-count bias is real but less severe than first thought. [src: discoveries]

### BacDive isolation-ecology validation

Bacteria isolated from heavy metal contamination sites had metal tolerance scores a full standard deviation above the environmental baseline (Cohen's d = +1.00, Mann-Whitney p=0.006, n=10). [src: discoveries] The effect is dose-dependent: heavy metal (+1.00) > waste/sludge (+0.57) > all contamination (+0.43) > industrial (+0.20). [src: discoveries] The report reads this as validating the Atlas's genome-based prediction method against real-world isolation ecology. [src: discoveries] The signal holds within Pseudomonadota and Actinomycetota after phylogenetic stratification. [src: discoveries]

## 2026-02; 2026-03

This part of the Discoveries Log covers a BacDive-to-pangenome species bridge, a metal-tolerance comparison for host-associated bacteria, and a survey of the phage-defense protein [[entities/snipe|SNIPE]]. The bridge and the SNIPE survey report counts and database lookups. [src: discoveries]

### BacDive-to-pangenome bridge and metal tolerance

Species-name matching (exact match plus GTDB suffix removal) links 42,227 BacDive strains (43.4% of 97K) to 6,426 GTDB pangenome species. [src: discoveries] The bridge lets users cross-reference BacDive phenotypic data with pangenome-derived predictions without Spark queries. [src: discoveries] The report attributes the 56.6% of strains that stay unmatched to GTDB's species boundaries differing from LPSN/DSMZ taxonomy. [src: discoveries]

BacDive host-associated bacteria (n=12,086) have slightly but significantly higher metal tolerance scores than environmental bacteria (d=+0.14, p<0.0001). This contradicts the expectation that host niches have lower metal exposure. [src: discoveries] The report proposes genome-size confounding as the likely cause. Host-associated strains are dominated by large-genome Pseudomonadota pathogens with more KEGG-annotated gene clusters, which would inflate the normalized metal score. [src: discoveries] See [[concepts/metal-tolerance-determinants-and-shared-stress-confounding]].

### SNIPE distribution and domain identity

A survey of DUF4041 (PF13250) in the KBase Data Lakehouse 293K-genome pangenome found 4,572 gene clusters across 1,696 species and 33 phyla. That far exceeds the >500 homologues reported in Saxton et al. 2026. [src: discoveries] Of the surveyed SNIPE-associated genes, 86.7% are accessory or singleton, which is consistent with mobile defense island carriage. [src: discoveries] The report reads the patchy distribution across many phyla and families as support for horizontal gene transfer. [src: discoveries]

The SNIPE nuclease domain belongs to Pfam PF13455 (Mug113), not PF01541 (canonical GIY-YIG restriction enzymes and DNA repair). Both families sit in the GIY-YIG clan CL0418 but are distinct. [src: discoveries] The report says this explains why zero gene clusters show DUF4041 + PF01541 co-occurrence, and calls it biological truth, not an annotation artifact. [src: discoveries] The SNIPE paper names the nuclease only as "GIY-YIG" at the superfamily level and cites no Pfam accessions. [src: discoveries] InterPro/UniProt analysis of the *E. coli* SNIPE protein A0A0A1A5Z2 verified PF13250 at positions 232–333 and PF13455 at positions 443–520. [src: discoveries]

### Phage infection data and the ManXYZ receptor

The `phagefoundry_strain_modelling` database is separate from the GenomeDepot annotation browsers. It holds experimental data from Gaborieau et al. 2024: 188 *E. coli* strains × 96 phages, giving 17,672 binary infection outcomes. [src: discoveries] It also holds an ML model (AUC, area under curve, =0.883) with SHAP (Shapley additive explanations) importances for 1,582 gene cluster features. [src: discoveries]

Lambdavirus 411_P1 (phage lambda) infects only 1/188 strains (0.5%), against 43.4% for Myoviridae. The report calls this consistent with widespread ManYZ receptor loss making lambda infection rare. [src: discoveries]

Fitness Browser data (168 experiments, *E. coli* K-12 Keio collection) show severe ManXYZ knockout defects on D-mannose (fit = -3.93) [src: discoveries] and D-glucosamine (fit = -2.75). [src: discoveries] ManXYZ is dispensable for D-fructose (fit = +0.18 to +0.66). [src: discoveries] This contradicts the UniProt annotation of ManX as "fructose import across plasma membrane" (GO:0005354, Gene Ontology). [src: discoveries] The report states that SNIPE targets the ManYZ pore. This is the mannose transporter that phage lambda exploits for DNA injection, not a general sugar transporter. [src: discoveries]

### Further SNIPE homologues

The Fitness Browser contains one archaeal SNIPE protein, in *Methanococcus maripaludis* JJ (locus MMJJ_RS01635). It carries PF13250 (DUF4041) and PF13455 (Mug113/GIY-YIG nuclease), plus PF10544 (DUF2525). [src: discoveries] This full two-domain protein has 129 fitness experiments. The report calls it the first SNIPE homologue with genome-wide knockout phenotypes available for analysis. [src: discoveries]

The PhageFoundry *Klebsiella* genome browser contains 1 DUF4041 annotation, representing 3 proteins at 558 aa (the same length as *E. coli* SNIPE). It also contains 4,619 PTS_EIIC (PF02378/ManY family) annotations. [src: discoveries] *Klebsiella* is the only PhageFoundry species with both SNIPE and the ManX-family PTS domain PF00358. [src: discoveries] The report proposes that SNIPE could affect phage therapy efficacy in this key pathogen. [src: discoveries]

## Template; 2026-03

This part of the log records several findings from different projects. They cover how Web of Microbes encodes metabolite actions, a cystic fibrosis (CF) formulation analysis, a BacDive metal-tolerance test, plant growth promoting (PGP) gene patterns, and subsurface genome size. It also records one notebook-execution pitfall. [src: discoveries]

### Web of Microbes encoding and linkage

Web of Microbes (WoM) records metabolite production but not consumption, and some of its organisms link directly to Fitness Browser (FB) strains. [src: discoveries]

- For organisms, action E (Emerged) means a metabolite was absent from the control medium and is now detected, which the report reads as de novo biosynthesis. [src: discoveries]
- Action I (Increased) means the metabolite was present in the control and its level went up. [src: discoveries]
- E and I are mutually exclusive, with 0 overlap across 10,744 observations. [src: discoveries]
- For the control, "The Environment", D means Detected in medium and N means Not detected. [src: discoveries]
- The 2018 snapshot has no organism "Decreased" (consumption) action. All 742 D observations belong to the control, so the database records only production. [src: discoveries]
- Two WoM organisms are exact FB strain matches. Pseudomonas sp. FW300-N2E3 matches `pseudo3_N2E3` (5,854 genes, 211 experiments), and Pseudomonas sp. GW456-L13 matches `pseudo13_GW456_L13` (5,243 genes, 106 experiments). [src: discoveries]
- E. coli BW25113 is the same strain as Keio, which allows direct metabolite-to-gene-fitness linking. [src: discoveries]
- FB carbon-source experiments for these organisms test metabolites that WoM detects as produced, with 109 metabolite-condition name overlaps. [src: discoveries]
- Of 257 identified (non-unknown) WoM compounds, 69 match ModelSEED molecules by exact name and 107 by formula. That totals 176 (68.5%), which enables reaction-level annotation for most WoM metabolites. [src: discoveries]

### CF airway formulation

Metabolic overlap with PA14 predicts commensal inhibition in part, and the strongest FDA-safe inhibitors inhibit more than overlap predicts, which the report reads as direct antagonism. [src: discoveries]

- Across 142 CF airway isolates, overlap with PA14's amino-acid preferences (proline, histidine, ornithine, glutamate, aspartate) predicts planktonic inhibition (r=0.384, p=2.3e-6, R²=27.4%). [src: discoveries]
- The strongest FDA-safe inhibitors (S. salivarius, N. mucosa, G. sanguinis) show 57-74% more inhibition than overlap predicts. The report concludes that dual-mechanism organisms (metabolic plus direct antagonism) are the best formulation candidates. [src: discoveries]
- PA14 is a metabolic generalist. It outgrows the average commensal on all 20 tested amino acids plus glucose and lactate, with selectivity ratio <1.0 for all. [src: discoveries]
- The report asserts that competitive exclusion requires community-level niche coverage by 3+ organisms, not individual superiority. [src: discoveries]
- A [[entities/gapmind]] pathway comparison finds 6 carbon sources with 100% pathway completeness in formulation commensals but 0% in PA14. They are xylitol, myoinositol, xylose, arabinose, fucose and rhamnose. [src: discoveries]
- The report describes these as FDA-GRAS and notes that xylitol is already used in CF airway products. [src: discoveries]
- Patient metatranscriptomics confirms commensal-specific PTS sugar transport expression in vivo. [src: discoveries]
- In the [[entities/kbase-data-lakehouse]] pangenome, 38% of R. dentocariosa genomes and 33% of N. mucosa genomes come from respiratory sources. The report calls both species disproportionately lung-associated relative to other formulation species. [src: discoveries]
- The report concludes that these two anchor the FDA-safe formulation, citing highest inhibition, highest engraftability and lung tropism. [src: discoveries]

### BacDive phenotypes and metal tolerance

Classical phenotypes carry real signal for metal tolerance, but phylogeny fully accounts for it. [src: discoveries]

- BacDive phenotypes (Gram stain, oxygen tolerance, enzyme activities) alone give R²=0.16, with 7/10 significant after false discovery rate (FDR) correction. [src: discoveries]
- Adding phenotype features to a taxonomy-based model gives zero improvement (delta R²=-0.009). [src: discoveries]
- The report names genome metal-resistance gene count as the true predictor, with full model R²=0.63. [src: discoveries]
- Urease-positive bacteria have lower metal tolerance (d=-0.18), which the report attributes to Actinomycetes lineage composition. [src: discoveries]
- The report says this validates genome-based prediction ([[entities/metal-fitness-atlas]]) over phenotype-based screening. [src: discoveries]

### Plant growth promoting genes

Across 27K GTDB species, pqqC (phosphate solubilization) and acdS (ACC deaminase; ACC is 1-aminocyclopropane-1-carboxylate) co-occur at OR = 7.24 (odds ratio). This is far stronger than any other PGP gene pair. [src: discoveries]

- Both genes are strongly enriched in soil/rhizosphere environments, with acdS at OR = 7.0 and pqqC at OR = 2.9. [src: discoveries]
- All 13 PGP genes are predominantly core, with 29.7% mean accessory versus 53.2% genome-wide. The report reads this as rejecting the horizontal gene transfer (HGT) hypothesis and indicating vertical inheritance. [src: discoveries]
- nifH forms a separate ecological guild. It is negatively associated with pqqC and hcnC and depleted in soil relative to aquatic environments. [src: discoveries]
- The trp→ipdC coupling (OR = 2.81) holds in non-soil species but reverses in soil species. The report suggests soil PGPB acquire tryptophan exogenously from root exudates. [src: discoveries]

### Subsurface genome size

The report finds that the "small is mighty" streamlining pattern documented by Tian et al. 2020 for Patescibacteria/CPR (candidate phyla radiation) does not generalize to cultivable subsurface Firmicutes. [src: discoveries]

- The within-Bacillota_B comparison uses an anchor of n=10 deep-clay organisms, including Mont Terri Opalinus and Ca. Desulforudis audaxviator. The baseline is n=62 phylum-matched soil organisms. [src: discoveries]
- CheckM-rescaled genome size is 4.3 Mbp in the anchor versus 3.2 Mbp in the baseline (Cohen's d = +1.37, Mann–Whitney p=0.013), so the anchor is 35% larger. [src: discoveries]
- eggNOG ortholog group (OG) count is 2,771 versus 2,233 (d=+1.32, p=0.009). [src: discoveries]
- CheckM completeness is identical (94.7 vs 94.3, p=0.93), so the report concludes the expansion is not a MAG-quality artefact. [src: discoveries]
- The report interprets streamlining as a Patescibacteria/CPR-specific adaptation to episymbiotic life. Cultivable subsurface Firmicutes show the opposite pattern, which it calls consistent with Beaver & Neufeld 2024 and Becraft 2021. [src: discoveries]

### Notebook execution pitfall

Running `jupyter nbconvert --execute` on notebooks that call `spark.sql(...).toPandas()` on large result sets kills the kernel (DeadKernelError). [src: discoveries] The report's workaround is cache-check logic in Spark cells. Local nbconvert then runs from cached CSVs after the first JupyterHub run, and live Spark outputs are captured interactively on JupyterHub. [src: discoveries]

## 2026-03: [bacillota_b_subsurface_accessory] clay_confined_subsurface H3 IR-side analysis …

This part of the Discoveries Log records corrections to marker choices and annotation sources. They affect the clay-confined subsurface H3 test, a Bacillota_B phylogenetic control, and lanmodulin and xoxJ/xoxF annotation. The main result is that a wrong iron-reduction marker set voided one clay interpretation, while the sulfate-reduction finding stood. [src: discoveries]

### Clay H3: wrong iron-reduction markers

The merged clay_confined_subsurface project (PR #231) used K07811, K17324 and K17323 as iron-reduction markers in its H3 porewater-versus-rock-attached test. [src: discoveries] They are not iron-reduction markers. K07811 is TMAO reductase (KOfam threshold 1336). The other two are glycerol ABC (ATP-binding cassette) transport ATP-binding (363) and permease (318) proteins. [src: discoveries] KEGG has no canonical KO (KEGG ortholog) for the Geobacter omcS or Shewanella mtr multi-heme outer-surface cytochromes. [src: discoveries]

The corrected detector combines PFAM PF02085 Cytochrom_CIII, PFAM PF22678 Cytochrom_c_NrfB-like, and at least 4 CXXCH heme-binding motifs on gene_cluster.faa_sequence. [src: discoveries] It changes the per-cohort rates as follows:

- anchor_deep: 56% corrected, previously 11%. [src: discoveries]
- anchor_shallow: 40% corrected, previously 50%. [src: discoveries]
- soil_baseline: 41% corrected, previously 20%. [src: discoveries]

With the corrected markers, none of the cohort comparisons is significant (all Fisher p ≥ 0.46). [src: discoveries] The earlier reading of a rock-attached, iron-reduction-rich pattern in shallow clay was an artefact. The sulfate-reduction-side H3 finding remains intact. It uses markers K11180/K11181/K00394/K00395/K00958 and gives p=4×10⁻¹² against the Mitzscherling rock-attached null. [src: discoveries]

### Porewater versus rock-attached cultivation bias

At the same Mont Terri Opalinus clay site, the Bagnoud (2016) porewater paradigm describes sulfate-reducer dominance. The Mitzscherling (2023) rock-attached paradigm describes Geobacter/Geothrix iron-reducer dominance. [src: discoveries] In the [[entities/kbase-data-lakehouse]], 5 of 9 anchor_deep clay genomes are sulfate-reduction positive (p=4×10⁻¹²). [src: discoveries] The report reads this as direct, quantitative evidence that the cultured cohort represents the porewater fraction, not the rock-attached fraction. It also says the framework generalizes to any future cultured cohort drawn from the KBase Data Lakehouse or similar pangenome resources. [src: discoveries]

### Phylum-level confounding in Bacillota_B

Cohort-level toolkit-score enrichment looked like a strong deep-clay versus soil signal (deep 1.89 vs baseline 0.39). [src: discoveries] Bacillota_B contains Desulfosporosinus, BRH-c4a and BRH-c8a, the lineages that dominate cultured clay isolates. [src: discoveries] The phylum carries Wood-Ljungdahl and group 1 [NiFe]-hydrogenase at high background rates even in soil samples (baseline mean toolkit 1.65). [src: discoveries]

Within Bacillota_B, deep-clay isolates are not enriched beyond their phylum congeners for Wood-Ljungdahl (5/5 vs 15/19, p=0.54) or NiFe-hydrogenase (5/5 vs 14/19, p=0.54). [src: discoveries] Only sulfate reduction survives the phylogenetic control (5/5 vs 4/19, p_BH=0.04). [src: discoveries] The report warns that an apparent habitat signal at cohort level may be a phylum-level signature picked up by biased habitat sampling. [src: discoveries] See [[concepts/environmental-versus-phylogenetic-drivers-of-gene-content]].

### Lanmodulin annotation sources disagree

An NB01 calibration on 134K genomes in the KBase Data Lakehouse pangenome found that the two lanmodulin annotation sources disagree completely. [src: discoveries] Bakta product='Lanmodulin' flags 62 genomes, all in α-Proteobacterial methylotroph clades: Beijerinckiaceae *Methylobacterium*, Acetobacteraceae BOG-930 and Hyphomicrobiaceae. [src: discoveries] eggNOG Preferred_name='lanM' flags 505 additional genomes, none of them bakta-validated. They concentrate in unrelated gut Bacillota: *Streptococcus pneumoniae* 10, *Blautia_A wexlerae* 9, *Enterococcus faecalis* 8 and *Ruminococcus_B gnavus* 8. [src: discoveries] The report suggests the eggNOG name is a stale or seed-ortholog mislabeling, not a true homology call. [src: discoveries] Its guidance is to use bakta product='Lanmodulin' exclusively and to treat eggNOG Preferred_name='lanM' as zero-information. [src: discoveries] See [[concepts/annotation-source-disagreement-and-coverage]].

### xoxJ and xoxF annotation

K02030 is the KEGG ortholog for the generic amino acid ABC transporter substrate-binding protein family. [src: discoveries] Filtering eggNOG by KEGG_ko LIKE '%K02030%' returns 46,369 hits across nearly every phylum, almost none of them xoxJ. [src: discoveries] The specific bakta product call for XoxJ ("rare earth element methanol dehydrogenase accessory protein XoxJ") matches just 61 genomes. [src: discoveries] The report recommends the bakta product or eggNOG Preferred_name='xoxJ' for xoxJ analyses, and says K02030 should never be a proxy. [src: discoveries]

For xoxF, NB01 found 5,092 genomes carrying any marker, and only 418 (8%) hit both eggNOG K00114 and bakta Lanthanide-dependent methanol dehydrogenase-family products. [src: discoveries] The eggNOG-only set (3,272 genomes) appears to include bakta "Putative dehydrogenase XoxF" entries that the report's regex missed, plus other generic dehydrogenases hitting K00114. [src: discoveries] The bakta-only set (1,402) includes lanthanide-dependent ethanol dehydrogenase variants that the KEGG KO filter excludes. [src: discoveries] The report recommends reporting downstream xoxF results with eggNOG-K00114 as the primary set and either-source as the inclusive set, disclosing the gap, and naming the source for any xoxF count. [src: discoveries]

## Caveats and Open Work

- The v1.7 FAIL was technically correct for its schema but was not a scientific refutation. The report says a "structurally degenerate" verdict is an invitation to fix the schema, not to conclude on the science. [src: discoveries]
- The v1.7 failure is attributed to name-regex missing iron in heme pathway names, so the lesson rests on this one project and test. [src: discoveries]

## Slots Into

- [[concepts/ontology-versus-name-pattern-categorization-in-pathway-enrichment-tests]]: the same test flipped from FAIL to SUPPORTED when regex was replaced by the MetaCyc hierarchy. [src: discoveries]
- [[concepts/pathobiont-target-prioritization-for-ibd-phage-therapy]]: iron/heme acquisition was the dominant CD-up theme, consistent with AIEC iron-acquisition literature. [src: discoveries]
- [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]]: a degenerate verdict should prompt schema revision, not a scientific conclusion. [src: discoveries]
