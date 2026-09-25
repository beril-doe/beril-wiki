<!-- tension-hash: 80c3f5a33970a217 -->
# Tension: Does Environment Structure Gene Content Strongly or Not at All?

Two projects in this corpus reach opposite-looking conclusions about whether environmental context shapes microbial gene content, a tension carried here from [[concepts/ecotype-environment-gene-content]]. One reports a large, highly structured environmental signal; the other reports a null. The disagreement matters because much of the corpus's reasoning about ecotypes — the idea that lineages differentiate functionally along environmental gradients — depends on whether environment is a first-order driver of gene content or a weak one. The two results, however, are not measured on the same thing: these use different units, environments, and response variables [src: harvard_forest_warming; ecotype_env_reanalysis], so the conflict may be one of comparability rather than of biology. Recording it here keeps both directions intact rather than collapsing them into a single verdict.

## Evidence Sides

**Strong environmental structuring (Harvard Forest).** In the Harvard Forest soil-warming system, treatment × horizon explained 41% of genus-level variance [src: harvard_forest_warming]. The unit here is the genus, the environmental contrast is an experimental warming treatment crossed with soil horizon, and the response variable is community-level taxonomic composition.

**Null environmental comparison (ecotype reanalysis).** The species-level environmental comparison was null [src: ecotype_env_reanalysis]. This is a null result, not a weak-but-positive one, and it stays null: the analysis found no difference where an environmental effect was expected. Its unit is the species, its contrast is between environmental categories rather than an imposed treatment, and its response variable is gene content rather than community composition.

## Possible Reconciliations

*Hypothesis 1 — unit mismatch.* Environment may restructure which genera are present in a community while leaving within-species gene content largely unchanged; a genus-level variance partition and a species-level gene-content comparison would then both be correct and non-contradictory.

*Hypothesis 2 — contrast strength.* An imposed experimental treatment crossed with a sharp physical stratum (horizon) may generate a far steeper environmental gradient than the categorical environmental labels used in the species-level comparison, so the null could reflect a weak contrast rather than a weak mechanism.

*Hypothesis 3 — response-variable mismatch.* Taxonomic composition and gene content need not co-vary; compositional turnover can be large while functional gene repertoires are conserved. This remains a hypothesis; neither project measured both response variables in the same system.

## Resolving Work

- Run the species-level environmental comparison's design on Harvard Forest samples, holding unit and response variable fixed, to ask whether the null survives inside a system with a demonstrated 41% genus-level treatment × horizon effect [src: harvard_forest_warming].
- Compute gene-content variance partitions alongside taxonomic ones in the same Harvard Forest samples, to test Hypothesis 3: does composition move without gene content moving?
- Re-run the ecotype reanalysis at genus rather than species level, to test whether the null is a property of the unit (Hypothesis 1) or of the data.
- Stratify the environmental comparison by contrast strength — experimental versus observational environmental labels — to test Hypothesis 2 directly.
- Assemble the shared covariates each analysis conditions on, and report whether the two designs even admit a common denominator before any further comparison is attempted.
