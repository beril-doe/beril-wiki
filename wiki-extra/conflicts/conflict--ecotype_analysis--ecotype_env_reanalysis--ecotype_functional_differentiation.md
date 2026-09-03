<!-- tension-hash: 538e5b1b3fdfe665 -->
# Genome-Wide Environmental Dominance Versus Locus-Specific Ecological Adaptation

The tension in [[concepts/genome-wide-versus-locus-specific-ecological-adaptation]] is whether ecological adaptation is expressed broadly across gene content or concentrated in particular loci and functional categories. One analysis reports that environment dominated the gene-content signal in 39.5% of species, yet detected significant positive environmental effects in only 12 species (7.0%) and significant negative effects in only 4 species (2.3%). This matters because the two patterns imply different biological interpretations: widespread environmental influence on genome-wide composition versus more localized ecological differentiation that may not produce a strong whole-genome signal.

## Evidence Sides

**Genome-wide environmental effects**

The dataset indicates that environment dominated the gene-content signal in 39.5% of species. However, significant positive or negative environmental effects were detected in only 12 species (7.0%) and 4 species (2.3%), respectively. [src: ecotype_analysis] This side treats environmental influence on comparative effect sizes as evidence that ecological variables can shape broad gene-content patterns, even when formal significance is uncommon. The original analysis reports a correlation magnitude of 0.0025 across its 172-species analysis. [src: ecotype_analysis]

**Locus-specific adaptation and limited genome-wide evidence**

The absence of a strong genome-wide environmental signal may indicate that ecological adaptation is locus-specific. [src: ecotype_analysis] The ecotype study adds functional differentiation without environmental assignment or phylogenetic control, supporting the locus-specific hypothesis while leaving the ecological interpretation unresolved. [src: ecotype_functional_differentiation] Pangenome openness did not predict either environment or phylogeny effects, although the test did not directly compare individual loci or functional categories. [src: pangenome_openness] The reanalysis reports a median correlation of 0.081 across 183 species versus 0.003 in the original analysis. [src: ecotype_env_reanalysis, ecotype_analysis] It attributes this discrepancy to different genome sets and downsampling procedures and preserves only the within-method group comparison. [src: ecotype_env_reanalysis]

## Possible Reconciliations

- **Measurement-versus-significance hypothesis:** Environment may dominate comparative effect sizes in 39.5% of species while only a smaller subset reaches significance because effect-size ranking and statistical testing answer different questions.
- **Scope hypothesis:** Ecological adaptation may be concentrated in individual loci or functional categories, so genome-wide summaries could dilute biologically meaningful associations.
- **Coverage and metadata hypothesis:** The weak genome-wide signal may reflect incomplete AlphaEarth coverage, imprecise metadata, or environmental embeddings that omit relevant variation. [src: ecotype_analysis]
- **Method-comparison hypothesis:** The correlation discrepancy may result from different genome sets and downsampling rather than a directly replicated effect. [src: ecotype_env_reanalysis]

## Resolving Work

- Reanalyze the same species and genome sets with identical downsampling, asking whether the 0.081, 0.003, and 0.0025 correlation magnitudes converge.
- Test environmental associations separately for individual loci and functional categories, asking whether category-specific effects are hidden by genome-wide aggregation.
- Expand and harmonize AlphaEarth coverage and metadata, asking whether improved environmental measurement increases the number of significant species.
- Add environmental assignment and phylogenetic control to the functional-differentiation analysis, asking whether the observed differentiation is ecological rather than non-environmental structure.
- Compare effect-size dominance with formally adjusted significance using the same model, asking whether 39.5% and the 12-species and 4-species counts reflect distinct statistical quantities.
