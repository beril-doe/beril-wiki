<!-- tension-hash: 4d25f7e8ededc524 -->
# Lineage-associated acquisition or uneven lineage sampling: what drives phylogenetic structure and weak environmental signal in AMR profiles?

The [[concepts/environmental-resistome]] page records a positive relationship between antimicrobial resistance (AMR) and phylogenetic distance (evolutionary divergence between strains) in 701/1,261 species [src: amr_strain_variation, ecotype_analysis]. That relationship may reflect lineage-associated acquisition or uneven sampling of lineages across environments, and the available analyses do not separate these explanations [src: amr_strain_variation, ecotype_analysis]. A related limit applies to environmental signal. Where that signal is weak, it cannot distinguish absent adaptation from inadequate environmental representation [src: amr_strain_variation, ecotype_analysis]. The distinction matters because it decides how far the resistome (the collection of AMR genes in a population) can be read as environmentally structured.

## Evidence Sides

**Side 1 (hypothesis): lineage-associated acquisition**

The positive relationship between AMR and phylogenetic distance in 701/1,261 species may reflect lineage-associated acquisition [src: amr_strain_variation, ecotype_analysis]. This reading explains the phylogenetic pattern. It does not by itself establish that environmental adaptation is absent, because weak environmental signal cannot distinguish absent adaptation from inadequate environmental representation [src: amr_strain_variation, ecotype_analysis].

**Side 2: uneven lineage sampling and inadequate environmental representation**

The same relationship may instead reflect uneven sampling of lineages across environments [src: amr_strain_variation, ecotype_analysis]. Geographic coordinates were often missing or imprecise [src: amr_strain_variation, ecotype_analysis]. Partial correlations (correlations between two distance matrices while controlling for a third) assume linear relationships between distance matrices [src: amr_strain_variation, ecotype_analysis]. As a result, weak environmental signal cannot distinguish absent adaptation from inadequate environmental representation [src: amr_strain_variation, ecotype_analysis].

## Possible Reconciliations

- **Hypothesis:** Both processes may operate together. Lineage-associated acquisition and uneven sampling of lineages across environments are both offered as explanations of the relationship, and the available analyses do not separate them [src: amr_strain_variation, ecotype_analysis].
- **Hypothesis:** Environmental effects may be non-linear. Partial correlations assume linear relationships between distance matrices [src: amr_strain_variation, ecotype_analysis], so such effects could be underestimated. In that case the weak signal would partly reflect the method.
- **Hypothesis:** Weak environmental signal may partly reflect metadata quality. Geographic coordinates were often missing or imprecise [src: amr_strain_variation, ecotype_analysis], so genomes with precise coordinates might show stronger structure.

## Resolving Work

- **Data:** genomes per species with environment labels. **Method:** subsample to balance lineages across environments, then re-test the AMR–phylogeny relationship. **Question:** does the positive relationship persist once lineage sampling is even across environments?
- **Data:** the subset of genomes with precise geographic coordinates. **Method:** repeat the environment-versus-phylogeny partial correlations on that subset only. **Question:** does environmental signal strengthen when location is well specified?
- **Data:** the existing AMR and phylogenetic distance matrices. **Method:** rank-based partial correlations, which use ranks rather than raw distances, and multiple regression on distance matrices (MRM, which regresses one distance matrix on others) with non-linear terms. **Question:** is environmental signal hidden by the linearity assumption?
- **Data:** AMR genes split into mobile or acquired versus intrinsic ones. **Method:** compare their phylogenetic signal within the same species. **Question:** is the phylogenetic relationship driven by lineage-associated acquisition rather than by shared ancestry alone?
- **Data:** species with repeated sampling of the same lineage across contrasting environments. **Method:** compare AMR profiles within lineages and between environments. **Question:** do AMR profiles within a lineage differ between environments, which would show an environmental association independent of lineage?
