<!-- tension-hash: 6afa1ce05978fbdf -->
# Do Phylogenetic Corrections Strengthen, Remove, or Retain Pangenome Associations?

Projects in this corpus applied formal phylogenetic corrections to pangenome association analyses, and the corrected results did not move in one consistent direction. In one project a corrected estimate grew stronger than the naive pooled estimate. In another, correction removed the enrichments. In a third, a positive but small effect remained [src: lanthanide_methylotrophy_atlas, clay_confined_subsurface, microbeatlas_metal_ecology]. The projects also used different controls, so their outcomes are not directly comparable [src: pathway_capability_dependency, pgp_pangenome_ecology, lanthanide_methylotrophy_atlas, microbeatlas_metal_ecology, gene_function_ecological_agora]. This matters for [[concepts/phylogenetic-confounding-of-pangenome-associations]]. If the direction of the correction depends on the trait or on the control chosen, then no single corrected or uncorrected result can be taken as the default reading of a pangenome association.

## Evidence Sides

**Side 1: correction strengthened the association.** The lanthanide atlas fitted a mixed model, a regression combining fixed effects with random effects for grouping levels, here phylum and family. This model gave a stronger estimate of xoxF dominance than naive pooling did. xoxF is the gene for the lanthanide-dependent methanol dehydrogenase [src: lanthanide_methylotrophy_atlas, clay_confined_subsurface, microbeatlas_metal_ecology].

**Side 2: correction removed the association.** The clay study controlled for phylum by comparing genomes within each phylum. Under this control, the enrichments of the Wood–Ljungdahl pathway (anaerobic CO₂ fixation via acetyl-CoA) and of [NiFe]-hydrogenase (a hydrogen-cycling enzyme with a nickel–iron active site) disappeared [src: lanthanide_methylotrophy_atlas, clay_confined_subsurface, microbeatlas_metal_ecology].

**Side 3: correction retained a small association.** The metal ecology project used PGLS (phylogenetic generalized least squares, a regression whose error structure follows the phylogeny). PGLS kept a positive but small coefficient linking metal-type diversity to niche breadth [src: lanthanide_methylotrophy_atlas, clay_confined_subsurface, microbeatlas_metal_ecology].

**Cross-cutting caveat: the controls differ.** Across projects, the controls were:
- genus grouping;
- phylum fixed effects (a separate model term estimated for each phylum);
- family equal weighting;
- mixed models;
- PGLS;
- Sankoff parsimony, a method that reconstructs ancestral states by minimizing weighted change costs on a tree.

These controls make different assumptions, so the three outcomes above are not directly comparable [src: pathway_capability_dependency, pgp_pangenome_ecology, lanthanide_methylotrophy_atlas, microbeatlas_metal_ecology, gene_function_ecological_agora].

## Possible Reconciliations

- **Hypothesis A: trait-specific confounding.** Phylogenetic structure may hide a real signal for some traits, as with xoxF. For other traits it may create apparent signal, as with the Wood–Ljungdahl pathway and [NiFe]-hydrogenase. On this reading, the opposite directions reflect the biology of each trait, not the methods.
- **Hypothesis B: method dependence.** The direction may follow from the control used. Within-phylum stratification, mixed models and PGLS partition variance differently, so the same data could shift differently under each.
- **Hypothesis C: grouping rank matters.** Controls at the genus, family or phylum rank absorb different amounts of between-lineage variance. This could explain divergent outcomes without any real difference in biology.

## Resolving Work

- Re-run the lanthanide xoxF dominance analysis with within-phylum stratification. This would test whether the strengthening survives the control that removed the clay enrichments.
- Fit phylum-and-family mixed models and PGLS to the clay study's Wood–Ljungdahl and [NiFe]-hydrogenase enrichments. This would test whether their removal is specific to within-phylum control.
- Apply family equal weighting and genus grouping to the metal-type versus niche-breadth association. This would ask whether the small PGLS coefficient is stable across control choices.
- Build a shared benchmark that applies every control in the list above to the same set of traits. This would separate trait-driven differences from method-driven ones.
