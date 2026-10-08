<!-- tension-hash: 37cb32ffe5752483 -->
# Does Environment Shape Pangenome Openness? Conflicting Evidence from Openness Analyses

Pangenome openness is the propensity of a species' gene repertoire to remain expandable as additional genomes are sampled [src: discoveries]. Two openness analyses provide conflicting evidence about environmental determinants [src: discoveries]. One reported no significant relationship between openness and environment or phylogeny (evolutionary relationships among species) [src: discoveries]. Another found strong associations between variable metabolic pathways and openness, and between ecological breadth and pathway completeness [src: discoveries]. The disagreement matters because the two results use different predictor sets and are not directly equivalent tests [src: discoveries]. The tension may therefore not be a simple contradiction about whether environment matters [src: discoveries]. This conflict page records the tension from [[concepts/pangenome-openness-determinants]].

## Evidence Sides

**Side 1: No environmental or phylogenetic relationship**

- One openness analysis reported no significant environment or phylogenetic relationship [src: discoveries].
- The new analysis **supports** this null side for its harmonized test of openness against environment and phylogeny effects [src: pangenome_openness].
- It does not directly test the pathway associations or the AlphaEarth association [src: pangenome_openness].
- The pathway_capability_dependency report also cites the pangenome_openness null for openness against environment or phylogeny effect sizes [src: pathway_capability_dependency].

**Side 2: Metabolic and ecological-breadth associations**

- Another analysis found strong associations between variable metabolic pathways and openness, and between ecological breadth and pathway completeness [src: discoveries].
- The digest contrasts the pathway-variability association with the pangenome_openness null and calls metabolic pathway variability a genuine predictor [src: discoveries].
- The pathway_capability_dependency report states that its pathway-variability metric succeeds where broader ecological variables failed [src: pathway_capability_dependency].
  - That framing is the report's own interpretation across different predictor sets, not a harmonized comparison [src: pathway_capability_dependency].
- The digest reports a direct correlation between openness and niche breadth (correlation coefficient r=0.324) [src: discoveries].
  - This links openness to an environmental breadth measure, but only within the coverage-limited AlphaEarth subset [src: discoveries].

## Possible Reconciliations

- **Hypothesis 1, different predictors:** The two results use different predictor sets and are not directly equivalent tests [src: discoveries]. Effect sizes for environment or phylogeny dominance may capture something different from pathway variability or niche breadth. Under this reading, both results could hold at once.
- **Hypothesis 2, analytic design:** The tension may reflect differences in genome-count control, species inclusion, or environmental coverage rather than a simple contradiction about whether environment matters [src: discoveries].
- **Hypothesis 3, subset effect:** The niche-breadth correlation is limited to the AlphaEarth subset [src: discoveries]. A coverage-dependent association could appear in that subset and not in a broader species set. This is untested.

## Resolving Work

- **One species set, all predictors:** Use the same species set with the same genome-count control. Fit openness against environment effect, phylogeny effect, pathway variability and niche breadth in one model. Do the associations survive side by side?
- **Re-run the null test on the AlphaEarth subset:** Repeat the pangenome_openness test of openness against environment and phylogeny effects within the AlphaEarth-covered species. Does the null hold where the niche-breadth correlation was measured?
- **Inclusion sensitivity:** Vary the species-inclusion thresholds and genome-count controls across both analyses. Does either result's direction depend on which species are included?
- **Harmonized predictor definitions:** Define environmental predictors in a way both analyses share, then repeat the pathway-variability comparison against the null. Does pathway variability outperform broader ecological variables in a like-for-like test?
