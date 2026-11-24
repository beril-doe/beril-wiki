---
type: "Summary"
description: "Summary of the project Ecotype Correlation Analysis."
doc_type: "short"
full_text: "sources/ecotype_analysis__REPORT.md"
---
# Ecotype Correlation Analysis

The Ecotype Correlation Analysis asked whether environmental similarity or phylogenetic history better predicts gene content across bacterial species. It analysed 172 species with sufficient environmental and phylogenetic data. [src: ecotype_analysis] The report also lists several limits on the environmental signal, including low AlphaEarth embedding coverage. [src: ecotype_analysis]

## Key Findings

### Phylogeny usually dominates gene content

Phylogeny dominated in 60.5% of species and environment in 39.5%. [src: ecotype_analysis] The report concludes that for most bacterial species, phylogenetic history predicts gene content better than environmental similarity does. [src: ecotype_analysis] See [[entities/partial-correlation-of-environment-and-gene-content-distance]] and [[concepts/environmental-versus-phylogenetic-drivers-of-gene-content]].

### Significance of the environment effect

Few species showed a significant environment effect. Twelve species (7.0%) had a significant positive effect (p<0.05), and 4 species (2.3%) had a significant negative effect. [src: ecotype_analysis] In 156 species (90.7%) the effect was not significant. [src: ecotype_analysis]

### Free-living versus host-associated bacteria

The report tested whether free-living "environmental" bacteria, where latitude and longitude are meaningful, show stronger environment effects than host-associated bacteria. It found no significant difference (p=0.66). [src: ecotype_analysis]

### Interpretation

The report reads these results as suggesting that vertical inheritance dominates the gene-content signal. [src: ecotype_analysis] It hypothesizes that environmental adaptation may act on specific gene subsets rather than the whole genome. [src: ecotype_analysis] It also suggests that AlphaEarth embeddings may not fully capture ecologically relevant environmental variation. [src: ecotype_analysis] See [[entities/alphaearth-environmental-embeddings]].

The report regards the phylogenetic dominance as consistent with Garud et al. (2019) and Shapiro et al. (2012). It describes those studies as showing that clonal ancestry shapes genome-wide variation more than ecological niche does. [src: ecotype_analysis] It relates the weak environmental effects to Polz et al. (2013). It describes that work as arguing that horizontal gene transfer shapes population structure at specific loci rather than genome-wide. [src: ecotype_analysis] See [[concepts/phylogenetic-structure-versus-ecological-adaptation-in-gene-content-patterns]].

## Data and Methods

The analysis queried the [[entities/kbase-ke-pangenome]] database (`kbase_ke_pangenome`). [src: ecotype_analysis] The tables used were:
- `alphaearth_embeddings`, which gave environmental embeddings for geographic coordinates. [src: ecotype_analysis]
- `genome`, which gave genome metadata and taxonomy. [src: ecotype_analysis]
- `ncbi_env`, which gave NCBI environmental and isolation-source metadata. [src: ecotype_analysis]
- `pangenome`, which gave pangenome composition per species. [src: ecotype_analysis]
- `gene_cluster`, which gave gene-cluster presence/absence profiles. [src: ecotype_analysis]

The expanded target set held 13,381 genomes across 224 species with metadata. [src: ecotype_analysis] Correlation results were produced for all 172 species. [src: ecotype_analysis]

## Caveats and Open Work

- AlphaEarth embeddings have only 28.4% genome coverage, which limits the environmental signal available. [src: ecotype_analysis]
- Geographic coordinates from NCBI metadata are often missing or imprecise, which reduces the quality of environmental associations. [src: ecotype_analysis] See [[concepts/coordinate-quality-and-institutional-address-artifacts-in-genome-geolocation]].
- Partial correlations assume linear relationships between distance matrices, so they may miss nonlinear ecological effects. [src: ecotype_analysis]
- For host-associated organisms, the coordinates reflect the collection site rather than the organism's actual microenvironment. Latitude and longitude are therefore less meaningful for them, which limits the free-living versus host-associated comparison. [src: ecotype_analysis]

The report proposes three next analyses:
1. Test whether specific COG (clusters of orthologous groups) categories, such as V-Defense and L-Mobile, show stronger environment effects. [src: ecotype_analysis]
2. Try alternative embedding distances, or use environmental metadata directly. [src: ecotype_analysis]
3. For species with identified ecotypes, compare gene content between ecotype clusters. [src: ecotype_analysis]

## Slots Into

- [[concepts/environmental-versus-phylogenetic-drivers-of-gene-content]]: phylogeny dominated in 60.5% of the 172 species, and the median environment partial correlation was 0.0025. [src: ecotype_analysis]
- [[concepts/phylogenetic-structure-versus-ecological-adaptation-in-gene-content-patterns]]: the report reads the pattern as vertical inheritance dominating, with environmental adaptation possibly confined to gene subsets. [src: ecotype_analysis]
- [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]]: the 28.4% embedding coverage and the missing or imprecise coordinates limit the environmental signal. [src: ecotype_analysis]
- [[concepts/functional-differentiation-of-gene-content-ecotypes-across-cog-categories]]: the report proposes testing COG categories for stronger environment effects. [src: ecotype_analysis]
- [[concepts/defense-and-mobile-element-gene-content-as-drivers-of-ecotype-differences]]: V-Defense and L-Mobile are the example categories the report proposes testing. [src: ecotype_analysis]
