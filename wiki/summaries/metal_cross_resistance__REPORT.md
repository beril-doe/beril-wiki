---
type: Summary
description: Gene-resolution analysis reveals conserved bacterial metal cross-resistance
  architecture.
doc_type: short
full_text: ../sources/metal_cross_resistance__REPORT.md
title: Gene-Resolution Metal Cross-Resistance Across Diverse Bacteria
sources:
- id: metal_cross_resistance
  resource: ../sources/metal_cross_resistance__REPORT.md
  title: metal cross resistance
---
# Gene-Resolution Metal Cross-Resistance Across Diverse Bacteria

## Overview

This study analyzes gene-level fitness responses to metals across diverse bacteria, testing whether cross-resistance is directionally conserved, whether shared and metal-specific genes differ in pangenome conservation, and whether cross-resistance predicts metal-associated isolation environments. The dataset comprises 452 metal experiments across 37 organisms and 14 metals, with 119,561 genes having metal fitness data from 28 organisms with at least 3 metals. [^metal_cross_resistance]

## Key Findings

### Universal, positive cross-resistance

Across 317 organism-metal pair observations involving 28 organisms and 85 unique metal pairs, 98.1% of gene-level fitness correlations were positive (311/317), and 99.1% were statistically significant (p < 0.05). All 15 metal pairs tested in at least 5 organisms showed greater than 90% sign consistency, and no metal pair showed systematically negative cross-resistance in any organism. [^metal_cross_resistance]

The strongest consensus associations were Fe-Zn (mean r = 0.61, n = 6 organisms), Co-Ni (r = 0.56, n = 28), Co-Zn (r = 0.52, n = 18), Ni-Zn (r = 0.51, n = 18), Cu-Zn (r = 0.48, n = 16), Cu-Fe (r = 0.45, n = 7), Al-Zn (r = 0.44, n = 13), Co-Fe (r = 0.45, n = 7), Co-Cu (r = 0.43, n = 24), and Cu-Ni (r = 0.43, n = 24). Al was the most independent metal, with a mean r = 0.34; Al-Ni and Al-Co were the weakest listed pairs at r = 0.34 and r = 0.30, respectively. [^metal_cross_resistance]

The study interprets cross-resistance as having a universal directional layer, because metals disrupt shared cellular processes including protein stability, DNA integrity, membrane function, and cofactor insertion, and a chemistry-specific magnitude layer, because divalent cations that compete for binding sites show stronger associations while metals with distinctive toxicity mechanisms show weaker associations. The chemistry-specific layer was moderately conserved across organisms: leave-one-out consensus prediction had r = 0.41, while the Mantel mean was r = 0.23. [^metal_cross_resistance]

### Conservation across organisms

The cross-resistance direction was consistent across phylogenetically diverse organisms spanning Proteobacteria, Bacteroidetes, Firmicutes, and Actinobacteria. Co-Ni had median r approximately 0.58 across 28 organisms, while Al-Co and Al-Ni had median r approximately 0.30. Individual-organism matrices repeatedly showed Ni-Co/Co-Zn among the strongest blocks, whereas Mo was the most independent metal in the 13-metal DvH dataset. Pairwise Spearman correlations of metal-pair rankings across the 10 common metal pairs and 12 organisms with at least 5 metals showed mostly positive agreement. [^metal_cross_resistance]

Mantel tests across 351 organism pairs produced a mean r = 0.23, with 62% positive values. The metal-label permutation test was non-significant (p = 0.42), because all metal pairs were positive and label shuffling did not change the mean; the report interprets this as indicating that the dominant signal is universal positivity rather than specific metal-pair identities. Leave-one-out consensus prediction had mean r = 0.41, although only 2/28 organisms reached individual significance. [^metal_cross_resistance]

### Three-tier gene architecture

Among 8,162 metal-important genes across 28 organisms, 1,484 (18.2%) were classified as general stress genes, 2,306 (28.3%) as metal-shared genes, and 4,372 (53.6%) as metal-specific genes. Their mean pangenome core fractions were 92.0%, 91.0%, and 89.8%, respectively, while the percentages fully core at at least 95% were 57.2%, 50.4%, and 45.7%. The fully core gradient therefore spans 11.5 percentage points. [^metal_cross_resistance]

The report states that this gradient supports an evolutionary model progressing from ancestral general stress defense, to shared metal defense, to more accessory and faster-evolving specialized metal-specific resistance. General stress genes were enriched for energy/respiration and cell-envelope functions, whereas metal-specific genes were enriched for transporters/efflux and iron/metal-related functions. [^metal_cross_resistance]

### Conserved cross-resistance gene families

The analysis identified 318 ortholog groups that were metal-shared, meaning important for at least 2 metals, in at least 2 organisms. The most broadly conserved families spanned up to 14 organisms and included cell-envelope, energy-metabolism, DNA-repair, and ion-homeostasis functions. [^metal_cross_resistance]

### BacDive validation

Multi-metal tolerance scores did not correlate with BacDive isolation from metal environments at the Fitness Browser species scale (Spearman rho approximately -0.02, p > 0.8). After excluding 2 organisms without tier-classification data and collapsing multiple Fitness Browser strains from the same species, the effective sample size was 20 independent species, which the report considers too small for a meaningful correlation test. Genus-plus-species substring matching was imprecise for organisms identified only to genus level, such as Acidovorax sp., so those fuzzy matches require caution. [^metal_cross_resistance]

The report compares this null result with the prior Metal Fitness Atlas validation, where pangenome-scale analysis of 42K strains produced Cohen's d = +1.0, and concludes that a properly powered test would apply KEGG/PFAM mapping to cross-resistance gene signatures across 27K species. [^metal_cross_resistance]

## Caveats

Metal concentrations differed among experiments, so dose-response effects could influence cross-resistance estimates. Organisms also ranged from 3 to 112 metal experiments, affecting the reliability of per-organism matrices. [^metal_cross_resistance]

The 28 organisms are not phylogenetically independent; formal phylogenetic comparative methods such as PGLS (phylogenetic generalized least squares) or independent contrasts would strengthen the conservation claim. [^metal_cross_resistance]

The BacDive validation is underpowered: the limitations section reports n = 26 at Fitness Browser organism scale, while the validation results report 20 independent species after matching and collapsing. The report emphasizes that this scale lacks the statistical power achieved by the Metal Fitness Atlas at pangenome scale with 42K strains. [^metal_cross_resistance]

No negative controls were tested. Because all tested metal pairs were positive, the study cannot distinguish universal cross-resistance from a general-stress response to all metals without non-metal stress controls; the report states that the counter_ion_effects project partially addresses this issue. [^metal_cross_resistance]

The study identifies future analytical needs including pangenome-scale validation across 27K species, phylogenetic independent contrasts, normalization by metal concentration relative to MIC, ICA (independent component analysis) of metal-condition modules, and AlphaFold-based structural analysis of metal-shared proteins. [^metal_cross_resistance]

## Slots Into

- [metal-cross-resistance](../concepts/metal-cross-resistance.md) — central synthesis of universal directional cross-resistance, chemistry-dependent magnitudes, and the three-tier gene architecture.
- [cofitness-network-architecture](../concepts/cofitness-network-architecture.md) — gene-level fitness correlations reveal conserved cross-resistance structure across metal conditions.
- [pangenome-integration](../concepts/pangenome-integration.md) — shared, specific, and general-stress gene tiers are distinguished by pangenome core enrichment, and 318 conserved ortholog groups are identified.
- [environmental-resistome](../concepts/environmental-resistome.md) — the study tests whether cross-resistance gene signatures predict metal-associated isolation environments and documents the underpowered BacDive result.
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — cross-metal fitness correlations quantify condition-linked gene importance across 452 experiments.

[^metal_cross_resistance]: [metal cross resistance](../sources/metal_cross_resistance__REPORT.md)
