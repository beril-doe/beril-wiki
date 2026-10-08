<!-- tension-hash: 478c939d18d6af71 -->
# Universal Within Scope, Narrow Across It: How Far Does a Strong Signal Travel?

Two projects each report a pair of numbers for the same object that differ sharply with the scope the number was taken over: an essentiality count restricted to the organisms where a family occurs versus one taken across all organisms, and a within-pilot association versus a cross-cohort reproducibility score. The disagreement is how much a strong within-scope result licenses beyond that scope. It matters for [[concepts/condition-specific-fitness]], which reads fitness and essentiality as condition-dependent: if within-scope strength does not travel, every "universal" list in this corpus carries an implicit scope clause.

## Evidence Sides

**Within scope, the signal is near-universal.** 859 ortholog families — groups of genes descended from a common ancestor across genomes — were universally essential within every organism in which they occurred [src: essential_genome]. On the community side, the within-pilot taxonomy–metabolite CCA (canonical correspondence analysis, which finds the combination of taxa most aligned with the measured metabolites) axis in the inflammatory bowel disease (IBD) pilot had r=0.964, where r is a correlation coefficient scoring how tightly the paired taxonomy and metabolite axis scores track each other [src: ibd_phage_targeting].

**Across scope, the signal is narrow or null.** Only 15 essential families were essential in all 48 organisms [src: essential_genome]. Pooled metabolomics had cross-cohort LOSO ARI=0.000 — leave-one-study-out validation, in which each cohort is held out in turn, scored by adjusted Rand index, a measure of cluster agreement corrected for chance — and the ecotype framework had mean LOSO ARI=0.113 [src: ibd_phage_targeting]. The null stays null: the pooled-metabolomics cross-cohort cluster agreement was 0.000, not merely small [src: ibd_phage_targeting].

## Possible Reconciliations

- *Hypothesis (different quantities).* The IBD figures may not be two readings of one thing: they measure within-pilot association versus cross-cohort reproducibility [src: ibd_phage_targeting], in which case the pair is no contradiction and must not be averaged into a single reproducibility claim.
- *Hypothesis (context, not error).* Genomic context, paralogs, alternative pathways, and compensation affect essentiality, which would make the 15-versus-859 gap a refinement of condition-specific interpretation rather than a contradiction of it [src: essential_genome].
- *Hypothesis (denominator).* The two essentiality counts differ in denominator — essential in all 48 organisms versus essential within every organism in which the family occurred [src: essential_genome] — so gene presence and absence, not a change in essentiality, could carry most of the gap.

## Resolving Work

- Re-score the 859 occurrence-conditioned families against gene presence/absence calls across the 48 organisms: what share of the gap down to 15 families is explained by absence rather than by non-essentiality where present? [src: essential_genome]
- Re-fit the within-pilot taxonomy–metabolite axis under a leave-one-study-out split and score it on each held-out cohort with the same axis correlation reported within pilot: does r=0.964 hold, drop, or vanish off its training cohort? [src: ibd_phage_targeting]
- Report per-held-out-cohort ARI values with interval estimates for both frameworks and compare them directly: is the ecotype framework's mean LOSO ARI=0.113 separable from the pooled-metabolomics cross-cohort LOSO ARI=0.000, or within the spread across held-out cohorts? [src: ibd_phage_targeting]
- For families essential in some organisms but not others, model paralog copy number and alternative-pathway completeness as predictors of the essentiality call: does compensation account for the loss of universality? [src: essential_genome]
