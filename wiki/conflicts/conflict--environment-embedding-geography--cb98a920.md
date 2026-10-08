<!-- tension-hash: cb98a920d2d32f72 -->
# Does controlling for genome size explain embedding-derived niche-breadth associations?

Two projects test whether a genomic trait tracks environmental niche breadth after controlling for genome size. Niche breadth is measured from AlphaEarth satellite-derived environmental embeddings, which are vector summaries of the places genomes were sampled. The outcomes diverge. For prophage modules, a partial association with niche breadth remains after the control. [src: prophage_ecology, phb_granule_ecology] For PHB (polyhydroxybutyrate, a carbon-storage granule), only a small negative partial association remains. [src: prophage_ecology, phb_granule_ecology] This matters for [[concepts/environment-embedding-geography]] because it bears on whether genome size can be read as a uniform explanation of embedding-derived niche-breadth associations.

## Evidence Sides

**Side 1: Prophage associations persist after genome-size control**

After genome-size control, prophage module count kept a partial Spearman rho=0.468 with AlphaEarth niche breadth. Partial Spearman rho is a rank correlation computed after removing the covariate's effect. [src: prophage_ecology, phb_granule_ecology] Prophage module effects also remained significant within genome-size quartiles. [src: prophage_ecology]

The same project reports caveats that limit this side:
- Genome size dominated PERMANOVA with F=212.99. PERMANOVA (permutational multivariate analysis of variance) tests how much among-sample variation groups explain, using permutations to judge significance. Its F-statistic is the ratio of between-group to within-group variation. [src: prophage_ecology]
- Prophage calls were annotation-based. [src: prophage_ecology]
- Only 28% of genomes had embeddings. [src: prophage_ecology]
- NMDC (National Microbiome Data Collaborative) prophage burden was genus-inferred. [src: prophage_ecology]

Human-associated module enrichments contrasted with 0/500 significant TerL-lineage enrichments. TerL is the terminase large subunit, used as a phage lineage marker. This supports modular exchange, but not independent adaptation of complete phage lineages. [src: prophage_ecology]

**Side 2: The PHB–niche-breadth association is reduced to a small negative partial correlation after genome-size control**

After the same kind of control, the PHB–niche-breadth partial rho was -0.047. [src: prophage_ecology, phb_granule_ecology] Genome size therefore cannot be treated as a uniform explanation of embedding-derived niche-breadth associations. [src: prophage_ecology, phb_granule_ecology]

## Possible Reconciliations

- **Hypothesis A:** Prophage module count may scale with genome size differently than PHB presence does. A count-type trait could retain residual variance after the control, while a binary trait does not. This is untested.
- **Hypothesis B:** The prophage result may partly reflect the embedded subsample, since only 28% of genomes had embeddings. [src: prophage_ecology] In that case, the two partial correlations would not be estimated on comparable populations. This is untested.
- **Hypothesis C:** The two traits may simply differ biologically in how they relate to niche breadth. Under this reading the divergence is real, not an artifact. This is untested.

## Resolving Work

- Rerun both partial Spearman analyses on the same intersected set of embedded species with an identical genome-size covariate. Question: does the divergence persist on a shared denominator?
- Convert prophage module count to presence/absence and PHB to a graded score, then repeat the genome-size-controlled correlation. Question: does trait encoding (count versus binary) drive the difference?
- Add a phylogeny-aware regression, such as PGLS (phylogenetic generalized least squares), with genome size and family as covariates for both traits. Question: do both associations hold once shared ancestry is modeled?
- Use non-annotation prophage calls on genomes with embeddings, compared with the annotation-based calls. Question: does the prophage–niche-breadth association depend on how prophages are detected?
- Test PHB within genome-size quartiles, the stratified design the prophage work used, and match it to the prophage analysis. Question: does the choice of control method (stratification versus partial correlation) change either conclusion?
