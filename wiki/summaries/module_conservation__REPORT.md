---
type: "Summary"
description: "Summary of the project Fitness Modules x Pangenome Conservation."
doc_type: "short"
full_text: "sources/module_conservation__REPORT.md"
---
# Fitness Modules x Pangenome Conservation

This page summarises the project Fitness Modules x Pangenome Conservation. It asks whether co-regulated fitness modules, found by independent component analysis (ICA), sit in the conserved core genome. Module genes are modestly enriched in core genes, and most modules are mostly core. The enrichment is statistically strong but small in absolute terms. [src: module_conservation]

## Key Findings

### Module genes skew core

Genes in ICA modules are described as co-regulated functional units that skew toward the conserved core genome. [src: module_conservation] Module genes are 86.0% core versus 81.5% of all genes, a difference of +4.5 percentage points. [src: module_conservation] The enrichment is reported as OR (odds ratio)=1.46, p=1.6e-87. [src: module_conservation] The median module is 93.4% core. [src: module_conservation] The report reads this as extending the idea of "core" from individual genes to functionally coherent regulatory units. [src: module_conservation]

### Module classes

Of 974 modules with >=3 mapped genes [src: module_conservation]:

| Class | Core-gene share | Modules |
|---|---|---|
| Core | >90% | 577 (59%) [src: module_conservation] |
| Mixed | 50-90% | 349 (36%) [src: module_conservation] |
| Accessory | <50% | 48 (5%) [src: module_conservation] |

### Family breadth does not predict conservation

Module families spanning more organisms do not have higher core fractions (Spearman rho=-0.01, p=0.914). [src: module_conservation] Families are nearly all core regardless of how many organisms they span. [src: module_conservation] The report attributes the missing gradient to a high core baseline of ~82%. [src: module_conservation] It also suggests that conservation is a property of individual genes, not of the cross-organism scope of their regulatory module. [src: module_conservation]

### Accessory families

The analysis finds 38 families with <50% core genes. The report describes them as co-regulated accessory gene modules conserved across organisms. [src: module_conservation] It hypothesizes that they may be horizontally transferred functional units or niche-specific operons. [src: module_conservation]

### No essential genes in modules

No essential genes appear in any module. [src: module_conservation] ICA captures only non-essential genes with transposon insertions and measurable fitness variation. Essential genes are invisible to it because they have no fitness data. [src: module_conservation]

## Data and Methods

The source modules are 1,116 co-regulated ICA modules across 32 organisms. [src: module_conservation] The analysis also used cross-organism module families, a pangenome link table for gene-to-cluster conservation, and an essential-genes classification. [src: module_conservation] Upstream module membership uses |Pearson r| >= 0.3 with at most 50 genes per module. [src: module_conservation] The report credits Price et al. (2018) with the Fitness Browser data and the ICA approach. [src: module_conservation] It cites Saelens et al. (2018) as showing that ICA outperforms other decomposition methods for microbial expression data. [src: module_conservation] It cites Vernikos et al. (2015) for core and accessory genome definitions. [src: module_conservation] See also [[entities/independent-component-analysis-fitness-modules]] and [[entities/fitness-browser]].

## Caveats and Open Work

- The baseline core rate of ~81.5% limits the maximum observable enrichment. The +4.5pp difference is significant but modest in absolute terms. [src: module_conservation]
- Only 29 of 32 module organisms are covered. Cola, Kang and SB2B lack pangenome links because their species had too few genomes in GTDB for pangenome construction. [src: module_conservation]
- The upstream membership threshold affects which genes are in a module and could influence conservation composition. [src: module_conservation]
- The 90% and 50% class cutoffs are arbitrary conveniences, not biologically motivated. [src: module_conservation]
- Essential genes are absent from modules by construction. [src: module_conservation]

## Slots Into

- [[concepts/conservation-of-cofitness-modules-in-the-core-genome]]: modules are 86.0% core versus 81.5% baseline, and the median module is 93.4% core. [src: module_conservation]
- [[concepts/conservation-of-cofitness-modules-across-genomes-and-organisms]]: family breadth does not track core fraction (rho=-0.01). [src: module_conservation]
- [[concepts/limits-of-transposon-based-essentiality-calls]]: essential genes are absent from ICA modules. [src: module_conservation]
