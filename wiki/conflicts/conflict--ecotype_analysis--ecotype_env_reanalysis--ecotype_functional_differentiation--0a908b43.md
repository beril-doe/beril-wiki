<!-- tension-hash: 5fdeecf0f11662b2 -->
# Does analytic instability indicate outcome leakage? Threshold generality, COG breadth, and cross-pipeline magnitude

Selection-on-outcome leakage — grouping or selecting observations with the same features later tested for differences — is diagnosed in this corpus largely by *instability*: candidate lists that shift under held-out or refit designs, and effect magnitudes that move when the pipeline changes. The tension recorded on [[concepts/selection-on-outcome-leakage]] is that instability is not a specific symptom, so the same observation can be read as leakage, as real biological structure, as annotation coverage and sample size, or as incompatible measurement and sampling choices. This page records three disagreements drawn from that tension text, and it is explicit about how many independent projects contend in each. The first two are **internal interpretive ambiguities within a single project** — a threshold that is used operationally but disclaimed as general [src: pitfalls], and a functional result whose own caveats undercut its breadth [src: ecotype_functional_differentiation] — rather than between-project disputes. Only the third is a genuine cross-project discrepancy, between the original ecotype analysis and its reanalysis [src: ecotype_analysis, ecotype_env_reanalysis]. No disagreement from the input is omitted; the question of which component drives instability is treated below as part of the first block rather than as a separate disagreement, because the input records it as an unattributed gap rather than as two opposed positions [src: pitfalls].

## Evidence Sides

### Disagreement 1 — Operational thresholds versus threshold generality (internal to one project: [src: pitfalls])

Both positions here come from the same source, `pitfalls`. The contention is not between two projects but between a threshold's operational use inside one procedure and its refusal to generalize.

**Position A: the values function as decision thresholds inside the cited procedure.** The values 0.5 and 0.3 were explicitly project-specific decision thresholds for the cited sensitivity procedure. [src: pitfalls] The Jaccard index here measures overlap between candidate lists produced under different held-out partitions; within that procedure the numbers are used to decide, not merely to describe.

**Position B: no universal cutoff is established, and instability does not attribute itself to a component.** The evidence does not establish a universal Jaccard cutoff for detecting leakage. [src: pitfalls] Applying 0.5 and 0.3 unchanged to another dataset or clustering method would be an unsupported extrapolation. [src: pitfalls] Further, the observed instability does not by itself identify whether clustering, differential-abundance modeling, subgroup sample size, or study structure contributed most to the changes. [src: pitfalls] Resolving those components requires analyses that vary the feature partition and validation design while preserving the underlying samples and labels. [src: pitfalls]

### Disagreement 2 — Is broad COG differentiation confirmation or artifact? (internal to one project: [src: ecotype_functional_differentiation])

Both readings below carry the same single citation and come from one report's own result-plus-caveat structure; no second project contends here.

**Reading A: the functional signal is broad.** All 12 analyzed species had at least one differentiated COG (Clusters of Orthologous Groups, a coarse functional annotation of gene families) category. [src: ecotype_functional_differentiation]

**Reading B: breadth is compatible with annotation and sampling effects, or with feature reuse.** Approximately 38% of gene clusters had COG annotations, and the report notes that effect significance may partly reflect large sample sizes. [src: ecotype_functional_differentiation] Widespread COG differences are therefore compatible with real functional structure, annotation and sampling effects, or reuse of related gene-content information; they do not alone quantify leakage. [src: ecotype_functional_differentiation] This result **refines** the leakage tension rather than resolving it.

### Disagreement 3 — Cross-pipeline magnitude: leakage or measurement? (between projects)

**Side A: magnitudes differ 27x between pipelines.** Absolute partial-correlation values (partial correlation = association between two quantities with a third held constant) can differ substantially when genome inclusion and downsampling change: the reanalysis median across 183 species was 0.081 versus 0.003 in the original analysis, described as a 27x difference. [src: ecotype_env_reanalysis]

**Side B: the original pipeline reports a weak environmental signal.** The original ecotype analysis reports a weak environmental signal overall, whereas the reanalysis reports a median partial correlation of 0.081 under a different pipeline. [src: ecotype_analysis, ecotype_env_reanalysis]

The two sides converge on an interpretive rule rather than on a shared magnitude: the discrepancy **supports** treating cross-pipeline magnitude comparisons as a tension in measurement and sampling rather than as evidence that leakage caused either result [src: ecotype_analysis, ecotype_env_reanalysis], and **supports** retaining the existing warning against interpreting instability or magnitude across incompatible methodologies as evidence of leakage alone, while the within-method environmental-versus-human-associated null comparison remains informative. [src: ecotype_env_reanalysis]

## Possible Reconciliations

These are hypotheses, not established findings.

- **Scope hypothesis (Disagreement 1).** Both positions may hold if 0.5 and 0.3 are read as calibrated operating points for one sensitivity procedure on one dataset rather than as statistical guarantees — usable inside the procedure, uninterpretable outside it. [src: pitfalls]
- **Component-confounding hypothesis (Disagreement 1).** The refusal to generalize may follow directly from the unattributed components: if clustering, differential-abundance modeling, subgroup sample size, and study structure each contribute unknown shares of the instability, no single cutoff can transfer across datasets that differ in those factors. [src: pitfalls]
- **Partial-coverage hypothesis (Disagreement 2).** Real functional differentiation and artifact could coexist if the ~38% of gene clusters carrying COG annotations are a non-random slice of gene content, so that per-species differentiation is genuine within annotated families while its breadth across all 12 species is inflated by sample size. [src: ecotype_functional_differentiation]
- **Representation-overlap hypothesis (Disagreement 2).** If the tested COG profiles summarize gene-content variation that also defined the groups, the result would be reproducible and biologically meaningful yet still not independent confirmation — making "real structure" and "reuse" non-exclusive. [src: ecotype_functional_differentiation]
- **Estimator-scale hypothesis (Disagreement 3).** The 27x gap may be a property of the estimator under different genome inclusion and downsampling rather than of the biology, in which case 0.003 and 0.081 are both correct on their own pipelines and simply not on a common scale. [src: ecotype_env_reanalysis]
- **Within-method-validity hypothesis (Disagreement 3).** Both results may stand if only within-method contrasts are treated as comparable, which is the stance the reanalysis takes when it preserves its environmental-versus-human-associated null while disclaiming the absolute magnitudes. [src: ecotype_env_reanalysis]

## Resolving Work

**Disagreement 1 — threshold generality and component attribution**

- Re-run the cited sensitivity procedure across several datasets and clustering methods, recording the Jaccard distribution under a design known to be leakage-free; ask whether any single cutoff separates leaky from clean designs, or whether 0.5 and 0.3 are procedure-bound. [src: pitfalls]
- Hold samples and labels fixed and vary only the feature partition, then only the validation design, in a factorial sweep; ask how much of the instability each factor explains. [src: pitfalls]
- Simulate the same pipeline with subgroup sample sizes and study structure varied independently of feature reuse; ask whether instability of the observed magnitude arises without any reuse at all. [src: pitfalls]
- Report, for each re-run, whether the operational threshold decision would have flipped; ask whether the decision the thresholds encode is stable even where their numeric values are not. [src: pitfalls]

**Disagreement 2 — COG breadth**

- Restrict differentiation tests to the annotated subset and to matched random gene-cluster subsets of equal size; ask whether "at least one differentiated COG category in all 12 species" survives when annotation coverage (~38%) is held constant. [src: ecotype_functional_differentiation]
- Rarefy each species to a common sample size and re-test; ask how much of the breadth is attributable to large sample sizes rather than effect size. [src: ecotype_functional_differentiation]
- Define groups on a feature representation disjoint from the tested COG profiles and re-test; ask whether differentiation persists without reuse of related gene-content information. [src: ecotype_functional_differentiation]

**Disagreement 3 — cross-pipeline magnitude**

- Recompute partial correlations on the same species set under both genome-inclusion and downsampling regimes within one codebase; ask whether the 0.081 versus 0.003 gap (27x) is fully explained by inclusion and downsampling. [src: ecotype_env_reanalysis]
- Report the 183-species reanalysis and the original analysis on a common species intersection with identical preprocessing; ask whether the qualitative claim of a weak environmental signal is pipeline-invariant. [src: ecotype_analysis, ecotype_env_reanalysis]
- Repeat the within-method environmental-versus-human-associated comparison at each genome-count regime; ask whether the null comparison — the part both sides treat as informative — is stable while absolute magnitudes move. [src: ecotype_env_reanalysis]
