<!-- tension-hash: fdbf2939c398016e -->
# Does environmental signal live in whole-pangenome openness or in selected gene subsets?

Two projects in this corpus reach different-looking conclusions about how strongly gene content tracks environment. One finds no significant relationship between pangenome openness (how far a species' total gene repertoire keeps expanding as more genomes are sampled) and either environment or phylogeny effects [src: pangenome_openness]. The other finds strong environment-associated enrichment for particular plant-growth-promoting (PGP) genes [src: pgp_pangenome_ecology]. The disagreement matters for [[concepts/gene-cooccurrence-ecological-guilds]], which uses recurring gene combinations as evidence of shared environmental selection. If a whole-pangenome metric shows no significant relationship to environment effects while targeted gene sets show enrichment, the level of representation chosen may determine whether ecological structure is detected at all. The source wiki frames this as a scale and representation tension rather than a direct contradiction.

## Evidence Sides

**Side A: pangenome openness shows no significant environment or phylogeny relationship**

The pangenome-openness analysis found no significant relationship between openness and environment effects (Spearman rho = -0.05, p-value = 0.54) [src: pangenome_openness]. Spearman rho is a rank-based correlation coefficient; the p-value is the probability of observing a correlation at least this strong if no true association existed. The same analysis found no significant relationship between openness and phylogeny effects (Spearman rho = 0.03, p-value = 0.73) [src: pangenome_openness]. Both results are nulls: they show no detected association, not that environment is irrelevant to gene content.

**Side B: selected PGP genes show strong environment-associated enrichment**

The PGP analysis found strong environment-associated enrichment for particular genes, including acdS and pqqC [src: pgp_pangenome_ecology]. This is a gene-targeted result concerning a selected functional subset, not a whole-pangenome summary statistic.

## Possible Reconciliations

- **Hypothesis 1 (scale):** A single whole-pangenome openness value may average over many genes with no environmental signal, diluting the signal carried by a small number of environmentally selected genes. On this view, both findings could hold at once.
- **Hypothesis 2 (representation):** Openness may capture how much a gene repertoire expands rather than which functions are present. Environment might then shape which genes are carried without shaping how open a pangenome is, so the two analyses would measure different properties rather than conflict on the same one.
- **Hypothesis 3 (definition of "environment effect"):** The environment variables used in the openness correlation may differ in kind or resolution from the habitat contrast used for PGP gene enrichment. That difference alone could produce a null in one analysis and a signal in the other.

## Resolving Work

- **Gene-level openness:** Using the pangenome-openness species set, recompute openness restricted to the PGP gene families, and test whether the subset-level metric correlates with environment effects where the whole-pangenome metric did not. This would test Hypothesis 1.
- **Shared environment definitions:** Re-run the openness-versus-environment Spearman correlation using the same soil/rhizosphere habitat contrast as the PGP enrichment analysis. This would show whether the null persists under a matched definition (Hypothesis 3).
- **Accessory-genome partitioning:** Split pangenomes into core (genes shared by nearly all genomes of a species) and accessory (genes present in only some genomes) fractions, and test which fraction carries the environment-associated PGP signal. This would show whether openness is the wrong axis for the environmental signal (Hypothesis 2).
- **Random gene-subset controls:** Draw random gene subsets of the same size as the PGP panel and test their environmental enrichment. This would ask whether strong subset-level signals arise generally or are specific to ecologically selected genes.
