<!-- tension-hash: 6cbe6ebd14c61211 -->
# Do co-occurrence guilds mean shared selection or metabolic complementarity — and should pangenome-wide openness predict either?

This page records two related disagreements raised on [[concepts/gene-cooccurrence-ecological-guilds]], both about what a "guild" inferred from gene co-occurrence actually is and how far the inference should reach. The first is mechanistic: one project reads a strong pairwise gene association plus environmental enrichment as evidence for an ecological guild, while another finds that co-occurring taxa are, if anything, *less* metabolically complementary than random pairs — so the co-occurrence cannot be explained by partners supplying each other missing functions. The second is a scale-and-representation disagreement: a whole-genome summary statistic (pangenome openness) shows no relationship to environment or phylogeny effects, while selected genes within pangenomes show strong environment-associated enrichment. Both matter because guild inference from gene co-occurrence is the main bridge in this corpus between comparative-genomics tables and ecological claims; if co-occurrence means only "same habitat filter," then guild language imports a mechanism the data do not carry. This page covers both disagreements and no others.

## Evidence Sides

### Disagreement 1 — guild as shared selection vs. guild as complementary provisioning

**Side A — co-occurrence plus environmental enrichment indicates an ecological guild.** The plant-growth-promoting (PGP) gene analysis — PGP meaning bacterial traits that benefit host plants — supports a *pqqC*–*acdS* ecological-guild interpretation through strong pairwise association and environmental enrichment. [src: pgp_pangenome_ecology]

**Side B — co-occurring partners are not metabolically complementary.** The plant-microbiome complementarity analysis found co-occurring genus pairs slightly *less* complementary than random pairs, with Cohen's d ≈ −0.4 (a standardized effect size; negative means co-occurring pairs score below the random baseline) and permutation p < 0.001 (significance assessed by reshuffling pair labels rather than by a parametric test). [src: plant_microbiome_ecotypes]

As the source concept page notes, these findings are not mutually exclusive: the tension is whether a guild denotes shared environmental selection or complementary metabolic provisioning, and it should not be resolved without pathway- and activity-level tests. [src: pgp_pangenome_ecology, plant_microbiome_ecotypes]

### Disagreement 2 — whole-pangenome openness vs. gene-subset environmental signal

**Side A — pangenome openness predicts nothing about eco-phylogenetic structure.** The pangenome-openness analysis found no significant relationship between openness (how much a species' gene repertoire keeps growing as genomes are added) and either environment or phylogeny effects: Spearman rho = -0.05, p-value = 0.54 for the environment effect, and Spearman rho = 0.03, p-value = 0.73 for the phylogeny effect (Spearman rho being a rank correlation, insensitive to non-linear but monotone scaling). [src: pangenome_openness]

**Side B — specific genes carry strong environmental association.** The PGP analysis found strong environment-associated enrichment for particular genes, including *acdS* and *pqqC*. [src: pgp_pangenome_ecology]

The source concept page frames this as a scale and representation tension rather than a direct contradiction: a whole-pangenome openness metric may fail to predict broad eco-phylogenetic structure while selected gene subsets retain environmental associations. [src: pangenome_openness, pgp_pangenome_ecology]

## Possible Reconciliations

These are hypotheses, not findings; none is tested in the sources cited above.

*For disagreement 1:*

- **Different definitions of "guild" (hypothesis).** If Side A's guild means "taxa filtered into the same habitat by the same selective pressure," and Side B's complementarity metric asks "do partners' metabolic repertoires fill each other's gaps," the two can both be true at once: habitat filtering selects functionally *similar* organisms, which would depress complementarity below random precisely because co-occurring partners duplicate rather than complement one another.
- **Different units of analysis (hypothesis).** Side A's evidence is a gene-pair association within genomes; Side B's is a genus-pair co-occurrence across communities. A gene pair can be tightly linked inside a lineage without that lineage's community partners being complementary — the two statistics need not move together.
- **Effect-size scale (hypothesis).** Side B's own framing is "slightly less complementary" (Cohen's d ≈ −0.4); a small negative displacement from random is compatible with complementarity being a weak secondary force layered on a stronger habitat filter, rather than being absent.

*For disagreement 2:*

- **Aggregation washout (hypothesis).** Openness is a single per-species summary over the whole accessory genome; if environment-responsive genes are a small minority of accessory content, their signal could be diluted to a rank correlation indistinguishable from zero while remaining strong gene by gene.
- **Different response variables (hypothesis).** Side A correlates openness against *derived effect sizes* (environment and phylogeny effects); Side B tests *gene presence* against environment directly. A null on the former does not constrain the latter if the effect-size estimates are noisy or measure a different quantity.
- **Power (hypothesis).** Both rho values are near zero with large p-values (0.54, 0.73); this is consistent with a true null, but also with an underpowered test, and the input does not report the sample size behind the correlations.

## Resolving Work

*Disagreement 1 — selection vs. provisioning:*
- Recompute the complementarity statistic restricted to the genus pairs that actually carry *pqqC* and *acdS*, and ask whether the ≈ −0.4 Cohen's d holds within the putative guild or is driven by pairs outside it. [src: pgp_pangenome_ecology, plant_microbiome_ecotypes]
- Run the pathway- and activity-level tests the concept page calls for — pathway-completeness comparisons and, where available, measured ACC-deaminase and phosphate-solubilization activity — to test whether co-occurring *pqqC*/*acdS* partners exchange products or merely share a habitat.
- Partition the complementarity test by habitat: if habitat filtering drives the negative effect, controlling for habitat should shrink the −0.4 displacement toward zero; if it does not, an active anti-complementarity mechanism is implicated.
- Test the guild claim against a co-occurrence null that preserves phylogeny, so that shared ancestry rather than shared selection is excluded as the source of the *pqqC*–*acdS* association.

*Disagreement 2 — openness vs. gene-subset signal:*
- Repeat the openness correlation using only environment-responsive gene subsets (e.g. the *acdS*/*pqqC* set) to define a per-species "responsive accessory fraction," and test whether that quantity — unlike global openness — tracks the environment effect. [src: pangenome_openness, pgp_pangenome_ecology]
- Report the n behind the Spearman tests and run a power analysis: state the smallest rho the design could have detected at the observed p-values of 0.54 and 0.73, so the null is distinguished from an underpowered test. [src: pangenome_openness]
- Check whether *acdS* and *pqqC* sit in the core or accessory compartment of the pangenomes analysed; if they are core-encoded, openness (an accessory-genome statistic) could not have registered their environmental signal, which would convert the tension into a definitional non-overlap.
- Re-run the openness correlation with alternative openness metrics to test whether the null is a property of the eco-phylogenetic dynamics or of the particular summary statistic chosen. [src: pangenome_openness]
