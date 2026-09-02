<!-- tension-hash: cad34cc630fab898 -->
# Whole-Genome Ecotypes Versus Localized Environmental Structure

The disagreement concerns whether environmental or host-associated structure is a general property of bacterial genomes, or whether it appears only in particular markers, prophage modules, or host-associated lineages. The [[concepts/ecotype-clustering-validity]] evidence shows that the estimated correlation magnitude changes substantially with sampling and analysis choices, while plant-compartment and prophage analyses detect narrower forms of ecological structure despite weak or null whole-genome environmental associations.

## Evidence Sides

**Whole-genome analyses support weak or unresolved environmental structure**

The original ecotype analysis reported a median partial correlation of 0.003, while the reanalysis reported 0.081, characterized as a 27x difference. [src: ecotype_env_reanalysis] The reanalysis used all genomes with embeddings, including up to 3,505 genomes per species, rather than diversity-maximizing downsampling with a maximum of 250 genomes, and used different genome sets and distance distributions. [src: ecotype_env_reanalysis] Because the absolute values are not comparable across methodologies, the magnitude of the relationship remains unresolved, although the Environmental versus Human-associated comparison remains valid within one consistent method. [src: ecotype_env_reanalysis] The original coarse classification yielded p=0.66, whereas the genome-level harmonized reanalysis yielded p=0.83; both support a null environmental-group comparison. [src: ecotype_analysis, ecotype_env_reanalysis]

Whole-genome comparisons also found weak or usually nonsignificant environment–gene-content relationships. [src: ecotype_analysis, ecotype_env_reanalysis] This evidence argues against treating broad environmental grouping as a validated, generalizable ecotype structure. [src: prophage_ecology]

**Targeted analyses detect ecological structure in restricted genomic or host-associated scopes**

Prophage-module composition showed an environmental effect after genome-size and family-level comparisons. [src: prophage_ecology] Refined plant-marker data detected significant compartment separation with PERMANOVA pseudo-F = 23.2, p = 0.001, and R² = 0.071. [src: plant_microbiome_ecotypes] However, db-RDA location-only R² = 0.060, and the effect was highly sensitive to genome-rich taxa. [src: plant_microbiome_ecotypes] These results indicate that ecological structure may be detectable in selected functional markers or particular host-associated lineages without producing strong, generalizable whole-genome ecotypes. [src: plant_microbiome_ecotypes]

## Possible Reconciliations

- **Hypothesis — measurement and sampling effects:** The 0.003 versus 0.081 estimates may differ because the analyses used different genome sets, distance distributions, and sampling strategies, rather than because the underlying biological association changed. [src: ecotype_env_reanalysis]
- **Hypothesis — scope concentration:** Ecological adaptation may be concentrated in prophage modules or selected plant-associated markers, producing localized signals that are diluted in whole-genome comparisons. [src: ecotype_analysis, ecotype_env_reanalysis, prophage_ecology, plant_microbiome_ecotypes]
- **Hypothesis — lineage composition and confounding:** The prophage and plant-compartment effects may reflect annotation, sampling, genome-rich taxa, or residual lineage confounding rather than independently validated ecotype structure. [src: prophage_ecology, plant_microbiome_ecotypes]
- **Hypothesis — definitional difference:** “Environmental structure” may refer either to broad genome-wide ecotypes or to narrower compartment- or module-level differentiation; the analyses may support the latter without supporting the former.

## Resolving Work

- Reanalyze identical genome sets with both diversity-maximizing downsampling to a maximum of 250 genomes and all-genomes inclusion, then test whether the median partial correlations remain 0.003 and 0.081 under matched distance and embedding procedures.
- Partition gene-content analyses into core genome, accessory genome, prophage modules, and selected plant markers, using matched genome-size and family-level controls to test where environmental signal is concentrated.
- Repeat the plant-compartment PERMANOVA and db-RDA after balancing genome-rich taxa, testing whether pseudo-F = 23.2, p = 0.001, R² = 0.071, and location-only R² = 0.060 persist.
- Perform cross-validation across species and independent sampling sets to determine whether prophage-module and plant-marker signals generalize beyond the analyzed lineages.
