<!-- tension-hash: 538e5b1b3fdfe665 -->
# Conflict: does environment shape gene content weakly, strongly, or only at specific loci?

Three overlapping disagreements sit under the same question — how much of within-species gene-content variation environment explains — and the corpus does not settle any of them. First, a single dataset both reports that environment *dominates* the gene-content signal in a large minority of species and that environment is *statistically significant* in almost none. Second, one source offers two competing interpretations of the same weak genome-wide environmental signal — that adaptation is locus-specific (acting on gene subsets), or that the environmental measurements are too poor to detect a real genome-wide effect — with a second project supporting only the locus-specific reading; the disagreement is between readings derived from that evidence, not between projects taking opposing positions. Third, a reanalysis of the same underlying question reports partial-correlation magnitudes that differ from the original analysis, and the two cannot be read as a replication. All three are recorded on [[concepts/genome-wide-versus-locus-specific-ecological-adaptation]]; this page treats each in turn. Throughout, "partial correlation" means the correlation between environmental distance and gene-content distance after conditioning on the other predictor, and "pangenome openness" is a summary metric of how much a species' gene repertoire keeps growing as genomes are added.

## Evidence Sides

### Disagreement 1 — dominance versus significance within one dataset

**Environment dominates in a large minority of species.** The dataset indicates that environment dominated the gene-content signal in 39.5% of species. [src: ecotype_analysis]

**Environment is significant in almost no species.** In the same dataset, significant positive or negative environmental effects were detected in only 12 species (7.0%) and 4 species (2.3%), respectively. [src: ecotype_analysis] The source itself flags that this apparent tension may reflect differences between dominance in comparative effect sizes and statistical significance, but does not resolve that distinction. [src: ecotype_analysis]

### Disagreement 2 — locus-specific adaptation versus measurement artifact

**The weak genome-wide signal reflects locus-specific adaptation.** The absence of a strong genome-wide environmental signal may indicate that ecological adaptation is locus-specific. [src: ecotype_analysis] The ecotype study adds functional differentiation without environmental assignment or phylogenetic control, so it supports the locus-specific hypothesis while leaving the ecological interpretation unresolved. [src: ecotype_functional_differentiation]

**The weak genome-wide signal is an artifact of the environmental data.** The same source offers this alternative reading of the same absence: it may instead result from incomplete AlphaEarth coverage, imprecise metadata, or environmental embeddings that do not capture biologically relevant variation. [src: ecotype_analysis]

**A third result constrains but does not decide between them.** The null relationship between pangenome openness and environment or phylogeny effects qualifies the interpretation that broad pangenome structure can explain genome-wide versus locus-specific ecological dynamics: openness did not predict either effect, but this test did not directly compare individual loci or functional categories. [src: pangenome_openness] It therefore does not contradict the evidence for functional differentiation, while leaving unresolved whether openness metrics conceal category-specific ecological associations. [src: pangenome_openness, ecotype_functional_differentiation]

### Disagreement 3 — correlation magnitudes that cannot be read as a replication

**Reanalysis magnitudes.** The reanalysis reports a median of 0.081 across 183 species versus 0.003 in the original analysis. [src: ecotype_env_reanalysis]

**Original-analysis magnitude as recorded.** The original page reports 0.0025 across its 172-species analysis. [src: ecotype_env_reanalysis, ecotype_analysis] The original and reanalysis correlation magnitudes therefore cannot be treated as a directly replicated effect. [src: ecotype_env_reanalysis, ecotype_analysis] The reanalysis attributes the discrepancy to different genome sets and downsampling procedures and explicitly preserves only the within-method group comparison. [src: ecotype_env_reanalysis]

## Possible Reconciliations

These are hypotheses, not findings; none is established by the cited evidence.

*Disagreement 1.* **Hypothesis: the two statistics answer different questions.** "Dominance" is a within-species comparison of two effect sizes and will assign a winner even when both effects are near zero and neither is distinguishable from noise; significance testing asks whether one effect is distinguishable from zero. Under this hypothesis, 39.5% environment-dominant and 7.0% significantly positive are compatible: most of the 39.5% would be coin-flips between two negligible correlations. The source explicitly raises this distinction without resolving it. [src: ecotype_analysis] **Hypothesis: power varies by species.** If per-species sample sizes differ widely, dominance could be stable while significance tracks sample size rather than biology.

*Disagreement 2.* **Hypothesis: both are true at different scales.** Environmental measurement error could suppress a genuine genome-wide signal *and* adaptation could still be concentrated at specific loci; the two explanations are additive, not exclusive, and nothing in the cited evidence separates them. **Hypothesis: the functional-differentiation result is orthogonal, not confirmatory.** Because that study carries no environmental assignment and no phylogenetic control, its differentiation could arise from population structure rather than ecology — which would leave the artifact side untouched. [src: ecotype_functional_differentiation] **Hypothesis: openness is the wrong aggregate.** A single openness metric may average over gene categories whose ecological associations point in opposite directions, so a null at the whole-pangenome level is compatible with category-specific environmental effects. [src: pangenome_openness, ecotype_functional_differentiation]

*Disagreement 3.* **Hypothesis: the gap is entirely methodological.** The reanalysis itself attributes the discrepancy to different genome sets and downsampling procedures, which would make 0.081 and 0.003/0.0025 estimates of different estimands rather than conflicting estimates of one. [src: ecotype_env_reanalysis] **Hypothesis: the 0.003 / 0.0025 mismatch is a reporting-precision difference** between the reanalysis's restatement and the original page's own figure, across 183 versus 172 species — but the corpus gives no statement confirming this, so it must remain a hypothesis and not be used to reconcile the numbers.

## Resolving Work

**Disagreement 1 (dominance vs significance)**
- Recompute, for the same species set, the joint distribution of (environment effect, phylogeny effect) with per-species confidence intervals, and report what fraction of the 39.5% environment-dominant species have intervals excluding zero. [src: ecotype_analysis]
- Simulate null gene-content matrices with no environmental structure, run the same dominance rule, and ask what dominance fraction the pipeline returns by chance — a null near 50% would explain 39.5% without biology.
- Stratify dominance and significance by per-species genome count to test whether significance is power-limited rather than effect-limited.

**Disagreement 2 (locus-specific vs artifact)**
- Repeat the functional-differentiation analysis with explicit environmental assignment and phylogenetic control, so the differentiation it reports can be attributed to ecology rather than shared ancestry. [src: ecotype_functional_differentiation]
- Run the environment-versus-gene-content test per functional category rather than genome-wide, and test whether pangenome openness predicts environment effects within categories — the specific gap the openness null leaves open. [src: pangenome_openness, ecotype_functional_differentiation]
- Restrict the analysis to the subset of genomes with high-quality coordinates and complete AlphaEarth coverage; if the genome-wide effect strengthens there, the artifact explanation gains support, and if it does not, the locus-specific hypothesis does. [src: ecotype_analysis]
- Substitute an independent environmental descriptor (curated isolation-source categories) for the embeddings and ask whether the genome-wide null survives the change of measurement.

**Disagreement 3 (magnitude discrepancy)**
- Rerun both pipelines on one frozen genome set with downsampling as the only varied factor, to quantify how much of the 0.081-versus-0.003 gap downsampling alone produces. [src: ecotype_env_reanalysis]
- Report the full per-species distributions, not medians, for the 183-species and 172-species analyses side by side, and compute the paired difference over the species present in both. [src: ecotype_env_reanalysis, ecotype_analysis]
- Audit the 0.003 versus 0.0025 restatement against the original analysis output to establish which figure is the analysis's own and at what precision. [src: ecotype_env_reanalysis, ecotype_analysis]
- Until the above is done, keep using only within-method comparisons, as the reanalysis requires. [src: ecotype_env_reanalysis]
