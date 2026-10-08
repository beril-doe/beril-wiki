---
type: "Summary"
description: "Summary of the metal_cross_resistance project, which used gene-level fitness data across 28 bacteria to show universally positive metal cross-resistance, a three-tier gene conservation gradient, and a null BacDive isolation-environment validation at Fitness Browser scale."
doc_type: "short"
full_text: "sources/metal_cross_resistance__REPORT.md"
---
# Gene-Resolution Metal Cross-Resistance Across Diverse Bacteria

## Overview

This study analyzes gene-level fitness responses to metals across diverse bacteria, testing whether cross-resistance is directionally conserved, whether shared and metal-specific genes differ in pangenome conservation, and whether cross-resistance predicts metal-associated isolation environments. The inventory classified 452 metal experiments across 37 organisms and 14 metals (Al, Cd, Co, Cr, Cu, Fe, Hg, Mn, Mo, Ni, Se, U, W, Zn). Metal fitness data were extracted for 30 organisms, 2 of which were excluded from analysis for having fewer than 3 metals, leaving 119,561 genes with metal fitness data for the 28 analyzed organisms with at least 3 metals. [src: metal_cross_resistance]

## Key Findings

### Universal, positive cross-resistance

Across 317 organism-metal pair observations involving 28 organisms and 85 unique metal pairs, 98.1% of gene-level fitness correlations were positive (311/317), and 99.1% were statistically significant (p < 0.05). All 15 metal pairs tested in at least 5 organisms showed greater than 90% sign consistency, and no metal pair showed systematically negative cross-resistance in any organism. [src: metal_cross_resistance]

The consensus table reported mean r, number of organisms, and sign consistency for each pair: Fe-Zn 0.61 (n = 6, 100%), Co-Ni 0.56 (n = 28, 100%), Co-Zn 0.52 (n = 18, 100%), Ni-Zn 0.51 (n = 18, 100%), Cu-Zn 0.48 (n = 16, 100%), Cu-Fe 0.45 (n = 7, 100%), Al-Zn 0.44 (n = 13, 100%), Co-Cu 0.43 (n = 24, 96%), Cu-Ni 0.43 (n = 24, 96%), Co-Fe 0.45 (n = 7, 100%), Al-Fe 0.38 (n = 5, 100%), Fe-Ni 0.38 (n = 7, 100%), Al-Cu 0.34 (n = 17, 94%), Al-Ni 0.34 (n = 20, 95%), and Al-Co 0.30 (n = 20, 95%). Al was the most independent metal, with a mean r = 0.34; Al pairs were the weakest listed, with Al-Co lowest at r = 0.30. The report reads Al's independence as consistent with its unique trivalent toxicity mechanism. That mechanism is an interpretation; the fitness data do not test it directly. [src: metal_cross_resistance]

The report singles out Ni-Co (r = 0.56, n = 28 organisms) as the classic divalent cation cross-resistance pair, now validated at gene resolution across diverse phyla. Fe-Zn (r = 0.61, n = 6) was unexpectedly strong; the report proposes shared disruption of iron-sulfur cluster proteins as the likely explanation, a hypothesis rather than a demonstrated mechanism. Cu-U (r = 0.51, n = 5) was also highlighted, with the report linking it to both metals causing membrane/oxidative damage. [src: metal_cross_resistance]

The study interprets cross-resistance as having a universal directional layer, because metals disrupt shared cellular processes including protein stability, DNA integrity, membrane function, and cofactor insertion, and a chemistry-specific magnitude layer, because divalent cations that compete for binding sites show stronger associations while metals with distinctive toxicity mechanisms show weaker associations. The chemistry-specific layer was moderately conserved across organisms: leave-one-out consensus prediction had r = 0.41, while the Mantel mean was r = 0.23. [src: metal_cross_resistance]

### Conservation across organisms

The cross-resistance direction was consistent across phylogenetically diverse organisms spanning Proteobacteria, Bacteroidetes, Firmicutes, and Actinobacteria. Co-Ni had median r approximately 0.58 across 28 organisms, while Al-Co and Al-Ni had median r approximately 0.30. Individual-organism matrices repeatedly showed Ni-Co/Co-Zn among the strongest blocks, whereas Mo was the most independent metal in the 13-metal DvH dataset. Pairwise Spearman correlations of metal-pair rankings across the 10 common metal pairs and 12 organisms with at least 5 metals showed mostly positive agreement. [src: metal_cross_resistance]

Mantel tests across 351 organism pairs produced a mean r = 0.23, with 62% positive values. The metal-label permutation test was non-significant (p = 0.42), because all metal pairs were positive and label shuffling did not change the mean; the report interprets this as indicating that the dominant signal is universal positivity rather than specific metal-pair identities. Leave-one-out consensus prediction had mean r = 0.41, although only 2/28 organisms reached individual significance. [src: metal_cross_resistance]

### Three-tier gene architecture

Among 8,162 metal-important genes across 28 organisms, 1,484 (18.2%) were classified as general stress genes, 2,306 (28.3%) as metal-shared genes, and 4,372 (53.6%) as metal-specific genes. Their mean pangenome core fractions were 92.0%, 91.0%, and 89.8%, respectively, while the percentages fully core at at least 95% were 57.2%, 50.4%, and 45.7%. Pangenome conservation therefore declined from general stress genes (pleiotropic, important across many conditions) to metal-shared genes (cross-resistance drivers important for at least 2 metals) to metal-specific genes (important for exactly 1 metal), with the fully core gradient (57.2% → 50.4% → 45.7%) spanning 11.5 percentage points. [src: metal_cross_resistance]

The report states that this gradient supports an evolutionary model progressing from ancestral general stress defense, to shared metal defense, to more accessory and faster-evolving specialized metal-specific resistance. The ancestry and relative evolutionary rates in this model are the report's interpretation of the conservation gradient, not directly measured. Functional keyword analysis showed general stress genes enriched for energy/respiration and cell-envelope functions, whereas metal-specific genes were enriched for transporters/efflux and iron/metal-related functions, consistent with the expectation that specialized metal resistance is mediated by dedicated transport systems. [src: metal_cross_resistance]

### Conserved cross-resistance gene families

The analysis identified 318 ortholog groups that were metal-shared, meaning important for at least 2 metals, in at least 2 organisms. The most broadly conserved families spanned up to 14 organisms and included cell-envelope, energy-metabolism, DNA-repair, and ion-homeostasis functions. [src: metal_cross_resistance]

### BacDive validation

Multi-metal tolerance scores did not correlate with BacDive isolation from metal environments at the Fitness Browser species scale (Spearman rho approximately -0.02, p > 0.8). After excluding 2 organisms without tier-classification data (azobra and BFirm, each with fewer than 3 metals) and collapsing multiple Fitness Browser strains of the same species into single species-level entries (for example, 5 *P. fluorescens* strains sharing the same BacDive pool), the effective sample size was 20 independent species, which the report considers too small for a meaningful correlation test. Genus-plus-species substring matching was imprecise for organisms identified only to genus level, such as Acidovorax sp., so those fuzzy matches require caution. [src: metal_cross_resistance]

The report calls this null result expected and contrasts it with the prior [[summaries/bacdive_metal_validation__REPORT]] project's pangenome-scale analysis (42K strains, Cohen's d = +1.0). The report's view that metal tolerance prediction needs pangenome-scale analysis to reach statistical power is its own interpretation, not a demonstrated requirement. The report proposes that a proper test of this hypothesis would apply the KEGG/PFAM mapping approach of the Metal Fitness Atlas to the cross-resistance gene signatures across 27K species. [src: metal_cross_resistance]

The BacDive validation result is shown in the report figure `figures/multimetal_validation.png`. The figure table labels it "H3 BacDive validation (null at FB scale)". The label gives no test statistic or denominator; those come from the validation results described above. [src: metal_cross_resistance]

## Relation to Prior Observatory Work

The report ties its Co-Ni result to classical work: Nies (1999, 2003) described Co-Ni-Zn cross-resistance mediated by CzcCBA efflux systems. The gene-level data confirm the Co-Ni pair (r = 0.56, n = 28 organisms) and, per the report, extend it to show that the entire genome responds similarly to Co and Ni, not just efflux genes. [src: metal_cross_resistance]

The [[entities/metal-fitness-atlas]] (this observatory) showed metal genes are 87.4% core. This study refines that result with a finer within-metal-gene gradient of general stress (92%) > shared (91%) > specific (90%), which the report interprets as layered core enrichment reflecting the evolutionary history of metal tolerance. [src: metal_cross_resistance]

The report states that the [[summaries/counter_ion_effects__REPORT]] project found the metal–NaCl correlation hierarchy of DvH (Desulfovibrio vulgaris Hildenborough) follows toxicity mechanism rather than counter-ion identity. It interprets its own metal–metal correlations across 28 organisms as confirming and extending that mechanistic grouping. [src: metal_cross_resistance]

## Caveats

Metal concentrations differed among experiments, so dose-response effects could influence cross-resistance estimates. Organisms also ranged from 3 to 112 metal experiments, affecting the reliability of per-organism matrices. [src: metal_cross_resistance]

The 28 organisms are not phylogenetically independent; formal phylogenetic comparative methods such as PGLS (phylogenetic generalized least squares) or independent contrasts would strengthen the conservation claim. [src: metal_cross_resistance]

The BacDive validation is underpowered: the limitations section reports n = 26 at Fitness Browser organism scale, while the validation results report 20 independent species after matching and collapsing. The report emphasizes that this scale lacks the statistical power achieved by the Metal Fitness Atlas at pangenome scale with 42K strains. [src: metal_cross_resistance]

No negative controls were tested. Because all tested metal pairs were positive, the study cannot distinguish universal cross-resistance from a general-stress response to all metals without non-metal stress controls; the report states that the counter_ion_effects project partially addresses this issue. [src: metal_cross_resistance]

The report lists the following as proposed future directions, not as results it reports. (1) Pangenome-scale H3 validation: apply the cross-resistance gene signatures to predict multi-metal tolerance across 27K species using the KEGG/PFAM mapping approach from the [[entities/metal-fitness-atlas]] ([[entities/kegg]], [[entities/pfam]]), then validate against [[entities/bacdive]] polymetallic isolation environments. (2) Phylogenetic independent contrasts: formally control for phylogenetic non-independence in the cross-resistance conservation analysis using PGLS (phylogenetic generalized least squares) or phylogenetic PCA (principal component analysis). (3) Metal dose-response normalization: normalize fitness effects by metal concentration relative to MIC (minimum inhibitory concentration) to control for dose-response confounds. (4) ICA module decomposition: apply ICA (independent component analysis; [[entities/independent-component-analysis]]), taken from the [[summaries/fitness_modules__REPORT]] project, specifically to metal conditions. The goal is to identify co-regulated metal-response modules and test whether cross-resistance genes cluster into coherent regulatory units. (5) Structural biology: use AlphaFold structures to investigate whether metal-shared proteins have structural features, such as metal binding sites or membrane interfaces, that explain multi-metal sensitivity. These structural explanations are proposals, not established findings. [src: metal_cross_resistance]

## Data Sources

- `kescience_fitnessbrowser` ([[entities/kescience-fitnessbrowser]]; tables `experiment`, `genefitness`, `gene`, `organism`): metal experiment classification, gene fitness extraction, and functional annotations. [src: metal_cross_resistance]
- `kbase_ke_pangenome` ([[entities/kbase-ke-pangenome]]; accessed via ortholog groups): core/accessory genome classification. [src: metal_cross_resistance]
- `kescience_bacdive` ([[entities/bacdive]]; tables `strain`, `isolation`): isolation-environment metadata for validation. [src: metal_cross_resistance]

## Figures

- `dvh_cross_resistance_heatmap.png`: DvH 13-metal cross-resistance matrix (sanity check). [src: metal_cross_resistance]
- `cross_resistance_panel.png`: multi-organism heatmap panel (top 9 organisms). [src: metal_cross_resistance]
- `metal_pair_conservation.png`: boxplots of r across organisms for each metal pair. [src: metal_cross_resistance]
- `metal_clustering_dendrogram.png`: consensus matrix with hierarchical clustering. [src: metal_cross_resistance]
- `organism_agreement_heatmap.png`: inter-organism Spearman agreement on metal pair rankings. [src: metal_cross_resistance]
- `mantel_distribution.png`: distribution of Mantel r values across organism pairs. [src: metal_cross_resistance]
- `permutation_test.png`: null distribution vs observed consensus mean r. [src: metal_cross_resistance]
- `consensus_vs_individual.png`: LOO (leave-one-out) consensus prediction accuracy. [src: metal_cross_resistance]
- `core_enrichment_gradient.png`: H2 test of core fraction by gene tier. [src: metal_cross_resistance]
- `tier_functional_enrichment.png`: functional categories by gene tier. [src: metal_cross_resistance]

## Slots Into

- [[concepts/metal-cross-resistance]] — central synthesis of universal directional cross-resistance, chemistry-dependent magnitudes, and the three-tier gene architecture.
- [[concepts/cofitness-network-architecture]] — gene-level fitness correlations reveal conserved cross-resistance structure across metal conditions.
- [[concepts/pangenome-integration]] — shared, specific, and general-stress gene tiers are distinguished by pangenome core enrichment, and 318 conserved ortholog groups are identified.
- [[concepts/environmental-resistome]] — the study tests whether cross-resistance gene signatures predict metal-associated isolation environments and documents the underpowered BacDive result.
- [[concepts/condition-specific-fitness]] — cross-metal fitness correlations quantify condition-linked gene importance across 452 experiments. [src: metal_cross_resistance]
- [[concepts/shared-stress-versus-stressor-specific-fitness]] — general-stress, metal-shared, and metal-specific gene tiers with distinct functional enrichments, plus the mechanistic grouping echoed from counter-ion work.
- [[concepts/two-speed-bacterial-genome]] — the conservation gradient from general-stress to metal-specific genes fits a conserved-core versus faster-evolving accessory model.
- [[concepts/lab-field-fitness-concordance]] — lab-derived multi-metal tolerance scores did not predict BacDive metal-environment isolation, with sample-size limits documented.
- [[concepts/cross-species-fitness-transferability]] — the leave-one-out consensus map captures the average trend but few individual organisms reach significance.
- [[concepts/taxonomic-nomenclature-reconciliation]] — genus-only labels make BacDive substring matching imprecise.
- [[concepts/pangenome-conservation-fitness-decoupling]] — refines the Metal Fitness Atlas core estimate with a within-metal-gene conservation gradient.
- [[concepts/fitness-condition-coverage-prioritization-bias]] — unequal metal experiment counts per organism affect per-organism matrix reliability.
- [[concepts/phylogenetic-confounding-of-pangenome-associations]] — the analyzed organisms are not phylogenetically independent and no PGLS or independent contrasts were applied.
- [[concepts/fitness-module-detection-sensitivity]] — the report proposes, but has not reported, an ICA decomposition of metal conditions to test whether cross-resistance genes form coherent co-regulated modules.
