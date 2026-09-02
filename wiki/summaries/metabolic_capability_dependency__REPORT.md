---
type: "Summary"
description: "Quantifies latent metabolic pathways, pangenome links, and within-species ecotypes."
doc_type: "short"
full_text: "sources/metabolic_capability_dependency__REPORT.md"
---
# Metabolic Capability vs Metabolic Dependency

## Overview

This study compares genomic metabolic capability with experimentally measured metabolic dependency across 1,695 pathway-organism pairs from 48 organisms, using GapMind pathway completeness predictions, Fitness Browser gene-fitness data, and SEED subsystem annotations as a pathway-membership proxy. It tests whether complete but fitness-neutral pathways are common, whether latent capabilities relate to pathway conservation and pangenome openness, and whether within-species metabolic profiles form environment-linked ecotypes. [src: metabolic_capability_dependency]

## Key Findings

### Latent capabilities

A pathway was classified as an active dependency when mean absolute fitness t-score exceeded 2.0 or more than 20% of its genes were essential; as a latent capability when mean absolute t-score was below 1.0 and fewer than 5% of genes were essential; and as intermediate between these thresholds. Of 1,695 complete pathway-organism pairs, 267 (15.8%) were latent, 547 (32.3%) intermediate, and 881 (51.9%) active. The pathway category strongly predicted dependency class (χ²=163.6, df=4, p=2.5×10⁻³⁴). [src: metabolic_capability_dependency]

Carbon source utilization pathways were most likely to be latent: 217 of 892 (24.3%) were latent, 320 (35.9%) intermediate, and 355 (39.8%) active. Amino acid biosynthesis pathways were predominantly active: 48 of 735 (6.5%) were latent, 220 (29.9%) intermediate, and 467 (63.5%) active. Other pathways were rarely latent: 2 of 68 (2.9%) were latent, 7 (10.3%) intermediate, and 59 (86.8%) active. Thus, carbon source utilization pathways were 3.7× more likely to be latent than amino acid biosynthesis pathways, using the reported 24.3% and 6.5% fractions. [src: metabolic_capability_dependency]

The latent fraction varied across organisms from 0–31.6%, with a mean of 15.0%; *Pseudomonas syringae* strains and *Klebsiella michiganensis* had the highest reported proportions. Sensitivity analysis across 16 combinations of active thresholds from 1.5–2.5 and latent thresholds from 0.75–1.25 produced latent fractions from 4.7% to 21.1%, with SD = 5.9 percentage points; the qualitative conclusion that a non-trivial fraction of complete pathways are fitness-neutral, especially carbon pathways, held across the tested range. [src: metabolic_capability_dependency]

### Conservation and pangenome openness

Pathway-level conservation did not distinguish latent capabilities from active dependencies. Among 755 active dependencies, mean conservation was 0.829 and the median was 1.000; among 508 intermediate pathways, mean conservation was 0.907 and the median was 1.000; and among 248 latent capabilities, mean conservation was 0.869 and the median was 1.000. Latent capabilities therefore had slightly higher mean conservation than active dependencies, with Mann–Whitney U p = 0.94 for active > latent and rank-biserial r = 0.052; this pathway-level test did not support H2a. [src: metabolic_capability_dependency]

At the clade level, the study supported H2b: after aggregating 41 organisms to 22 unique species clades so that multiple Fitness Browser strains from one clade shared a single pangenome-openness value, latent capability rate correlated positively with pangenome openness (Spearman ρ = 0.69, p = 0.0004, n = 22 clades). Clades with more fitness-neutral complete pathways therefore tended to have more dynamic, less-conserved pangenomes, consistent with a Black Queen framework signal operating at the level of genome dynamics and community context rather than simple per-pathway conservation. [src: metabolic_capability_dependency]

The pangenome dataset contained 7,334 species. Among well-sampled pathogens with more than 2,500 genomes, *Klebsiella pneumoniae* was reported as most open (99.05% open; 0.95% core genes), while *Mycobacterium tuberculosis* was reported as most closed (97.4% open; 2.6% core genes). [src: metabolic_capability_dependency]

### Metabolic ecotypes

All 10 target species, each with at least 50 genomes and at least 15 variable pathways, showed metabolic clustering with silhouette scores greater than 0.2. Scores ranged from 0.35 for *PALSA-747* sp. to 0.89 for *Salmonella enterica*. The reported species-level results were: *Salmonella enterica*, 11,396 genomes, k=6, silhouette 0.894; *Stutzerimonas stutzeri*, 149 genomes, k=2, 0.780; *Alteromonas macleodii*, 56 genomes, k=2, 0.738; *Acetatifactor intestinalis*, 59 genomes, k=6, 0.657; *Ruminococcus* E sp., 53 genomes, k=2, 0.609; *Phenylobacterium* sp., 51 genomes, k=2, 0.544; *Limivicinus* sp., 50 genomes, k=2, 0.528; *Pelagibacter* sp., 79 genomes, k=2, 0.430; *Prochlorococcus* A sp., 74 genomes, k=2, 0.429; and *PALSA-747* sp., 51 genomes, k=2, 0.349. [src: metabolic_capability_dependency]

Metabolic clusters were significantly associated with isolation environment in *Salmonella enterica* (χ²=1570.2, df=25, p<0.0001) and *Phenylobacterium* sp. (χ²=12.2, df=1, p=0.0005), but not in the marine organisms *Stutzerimonas*, *Alteromonas*, *Pelagibacter*, and *Prochlorococcus*. The strongest pathway heterogeneity occurred in valine/leucine biosynthesis (0.60), tryptophan biosynthesis (0.51), and lysine/threonine biosynthesis (0.49). [src: metabolic_capability_dependency]

The study interprets the strong *Salmonella enterica* structure as consistent with strain-level differentiation across clinical, food, and environmental isolation sources, while the non-significant marine associations may reflect insufficient isolation-source metadata, depth- or nutrient-zone structure, or pathway annotations that lack resolution for relevant gene-content differences. These ecological interpretations are observational and do not establish causality. [src: metabolic_capability_dependency]

## Data and exclusions

The analysis covered 48 organisms from the Fitness Browser, including diverse proteobacteria, firmicutes, and other phyla. It used `kbase_ke_pangenome.gapmind_pathways`, `pangenome`, and `gtdb_metadata` for pathway completeness, pangenome openness, and taxonomy, and `kescience_fitnessbrowser.genefitness`, `gene`, and `seedannotation` for gene-level fitness scores, essentiality inference, and SEED-proxy pathway mapping. Generated datasets included 23,424,480 per-genome pathway records, 27,690 species pathway summaries, 3,065 pathway-fitness aggregates, 1,695 classifications, 1,511 conservation records, 7,334 pangenome-openness records, 800 pathway-heterogeneity records, 12,018 metabolic ecotype assignments, 10 ecotype-cluster summaries, and 370 pathway-cluster signatures. [src: metabolic_capability_dependency]

Two GapMind pathways, deoxyribonate and myoinositol, had no matching SEED subsystem role descriptions and were excluded from all analyses. Full-name phenylalanine and tyrosine lacked SEED coverage, but their three-letter equivalents, `phe` and `tyr`, were included through abbreviation-based matching. Alanine was excluded from classification for every organism because fewer than 3 SEED-annotated genes met the minimum coverage threshold. [src: metabolic_capability_dependency]

## Caveats and limitations

The study states that SEED-proxy mapping can introduce false positives because related subsystem annotations may not represent direct GapMind pathway membership; direct GapMind per-step gene assignments would improve precision. The large intermediate zone (32.3%) makes the latent fraction moderately sensitive to threshold tightening, as shown by the 4.7%–21.1% sensitivity range. [src: metabolic_capability_dependency]

Fitness experiments are biased toward laboratory conditions, so pathways that are important in environments not represented by the tested media may appear latent. Pathway-level conservation cannot detect partial erosion or progressive loss of individual genes within otherwise complete pathways, and only 48 organisms were fitness-tested among 293,000 genomes with pathway predictions, limiting generalization across taxa. [src: metabolic_capability_dependency]

The conservation comparison may be affected by species-level averaging: many genomes in a species clade were not fitness-tested, potentially inflating apparent conservation of pathways classified from a limited set of organisms. The reported Black Queen signal may also be difficult to detect because gene loss can require longer evolutionary timescales than current sampling captures. [src: metabolic_capability_dependency]

The ecotype analysis is observational. Environment-cluster associations, including those in *Salmonella* and *Phenylobacterium*, may be confounded by phylogenetic structure because explicit phylogenetic correction was not performed. Marine non-associations may reflect coarse NCBI isolation-source metadata or pathway-level annotations that miss ecologically relevant gene-content and expression differences. [src: metabolic_capability_dependency]

An attempted organism-to-clade linkage using NCBI taxonomy IDs from `kbase_ke_pangenome.gtdb_metadata` returned zero matches because the relevant column contained boolean strings rather than numeric taxids. Downstream analyses therefore used organism-level fitness aggregates without an explicit clade-level linkage, which may reduce the precision of the H2a conservation comparison. [src: metabolic_capability_dependency]

## Slots Into

- [[concepts/condition-specific-fitness]] — The 15.8% latent fraction, carbon-versus-amino-acid contrast, threshold sensitivity, and laboratory-condition limitation show that genomic pathway completeness does not by itself establish fitness dependence. [src: metabolic_capability_dependency]
- [[concepts/gene-essentiality]] — The active, intermediate, and latent classes are defined using pathway-level mean absolute fitness t-scores and percentages of essential genes. [src: metabolic_capability_dependency]
- [[concepts/metabolic-model-gapfilling]] — GapMind completeness predictions, SEED-proxy mapping, excluded pathways, and the proposed direct GapMind gene mapping expose how annotation choices affect metabolic capability analysis. [src: metabolic_capability_dependency]
- [[concepts/pangenome-integration]] — The positive association between latent capability rate and pangenome openness (ρ = 0.69, p = 0.0004, n = 22 clades) connects fitness-neutral pathways to pangenome dynamics. [src: metabolic_capability_dependency]
- [[concepts/ecotype-environment-gene-content]] — All 10 target species formed metabolic clusters, with significant environment-cluster associations in *Salmonella enterica* and *Phenylobacterium* sp. [src: metabolic_capability_dependency]
- [[concepts/gene-function-acquisition-depth]] — The findings distinguish encoded metabolic capability from measured dependency and identify pathway-category-specific functional realization. [src: metabolic_capability_dependency]
