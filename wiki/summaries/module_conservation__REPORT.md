---
type: "Summary"
description: "Shows fitness modules are enriched in conserved core genes."
doc_type: "short"
full_text: "sources/module_conservation__REPORT.md"
---
# Fitness Modules × Pangenome Conservation

## Overview

This analysis uses independent component analysis (ICA), a decomposition method for identifying co-regulated fitness modules, together with pangenome conservation mappings to test whether module genes and cross-organism module families preferentially occupy the bacterial core genome. It analyzes 1,116 ICA modules across 32 organisms, module families, gene-to-cluster conservation mappings, and essentiality classifications. [src: module_conservation]

## Key Findings

### Module Genes Are More Core Than Average

Module genes are 86.0% core, compared with 81.5% for all genes, a difference of +4.5 percentage points. The enrichment is statistically strong (OR=1.46, p=1.6e-87), indicating that co-regulated functional units preferentially reside in the conserved core genome, although the absolute effect is modest because the baseline core rate is already high. [src: module_conservation]

### Most Modules Are Core

Of 974 modules with >=3 mapped genes, 577 (59%) are core modules (>90% core genes), 349 (36%) are mixed modules (50-90% core), and 48 (5%) are accessory modules (<50% core). The median module is 93.4% core, showing that most co-regulated fitness-response units are embedded in the conserved genome. [src: module_conservation]

### Family Breadth Does Not Predict Conservation

Module families spanning more organisms do not have higher core fractions: the Spearman correlation was rho=-0.01 with p=0.914. Families are nearly all core regardless of the number of organisms they span, suggesting that conservation is a property of individual genes rather than the cross-organism scope of their regulatory module; the high core-genome baseline of ~82% leaves little room for a breadth-dependent gradient. [src: module_conservation]

### Accessory Module Families Exist

Thirty-eight families have <50% core genes. These co-regulated accessory gene modules may represent horizontally transferred functional units or niche-specific operons; this interpretation is a hypothesis because the analysis identifies conservation patterns rather than directly demonstrating horizontal transfer or niche-specific regulation. [src: module_conservation]

### Essential Genes Are Absent from Modules

Zero essential genes appear in any module. Because ICA requires measurable fitness variation from transposon-insertion data, essential genes with no usable insertion-based fitness data are invisible to the modules, so the modules represent the non-essential portion of the genome. [src: module_conservation]

## Interpretation and Context

The 86.0% module-gene core fraction versus the 81.5% all-gene baseline supports enrichment of co-regulated functional units in the conserved genome, but the +4.5 percentage-point difference is modest under the ceiling imposed by the already high baseline. The null association between family breadth and conservation (rho=-0.01, p=0.914) redirects interpretation toward gene-level conservation rather than module-family scope. [src: module_conservation]

The analysis builds on the Fitness Browser data and ICA decomposition approach of Price et al. (2018), the evaluation of module-detection methods by Saelens et al. (2018), and core/accessory pangenome definitions reviewed by Vernikos et al. (2015). The finding that 59% of fitness modules are >90% core extends the notion of core conservation from individual genes to functionally coherent regulatory units. [src: module_conservation]

## Caveats

The baseline core rate is already ~81.5%, limiting the maximum observable enrichment; consequently, the +4.5 percentage-point difference to 86% is statistically significant but represents a modest absolute effect. [src: module_conservation]

The pangenome-linked analysis covers a 29/32 organism subset because Cola, Kang, and SB2B lack pangenome links; their species had too few genomes in GTDB for pangenome construction. [src: module_conservation]

Upstream ICA module membership uses |Pearson r| >= 0.3 with a maximum of 50 genes per module, so this threshold can influence which genes are classified as module members and therefore the conservation composition. [src: module_conservation]

The >90% core and <50% core cutoffs used to classify core, mixed, and accessory modules are convenient classification thresholds rather than biologically motivated boundaries. [src: module_conservation]

Essential genes are excluded from all modules because ICA requires fitness data and essential genes lack transposon insertions; therefore, the reported module conservation profiles cannot characterize essential-gene modules. [src: module_conservation]

## Data and Provenance

The analysis used ICA fitness modules from `fitness_modules/data/modules/`, cross-organism module families from `fitness_modules/data/module_families/`, the KBase pangenome gene-to-cluster conservation table `conservation_vs_fitness/data/fb_pangenome_link.tsv`, and essentiality classifications from `conservation_vs_fitness/data/essential_genes.tsv`. It generated `data/module_conservation.tsv` and `data/family_conservation.tsv`; notebooks `01_module_conservation.ipynb` and `02_family_conservation.ipynb` provide the per-module and family-breadth analyses. [src: module_conservation]

## Slots Into

- [[concepts/pangenome-integration]] — The finding that 86.0% of module genes are core versus 81.5% of all genes extends pangenome conservation analysis from individual genes to co-regulated functional units. [src: module_conservation]
- [[concepts/cofitness-network-architecture]] — The distribution of 974 mapped modules, including 577 (59%) core modules and 38 accessory module families, characterizes the genomic conservation architecture of fitness modules. [src: module_conservation]
- [[concepts/gene-essentiality]] — The absence of 0 essential genes from ICA modules clarifies how essentiality and transposon-based fitness measurements constrain module discovery. [src: module_conservation]
