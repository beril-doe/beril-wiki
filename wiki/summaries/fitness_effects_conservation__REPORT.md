---
type: "Summary"
description: "Summary of the project Fitness Effects vs Conservation -- Quantitative Analysis."
doc_type: "short"
full_text: "sources/fitness_effects_conservation__REPORT.md"
---
# Fitness Effects vs Conservation -- Quantitative Analysis

This report asks whether genes with larger fitness effects in the [[entities/fitness-browser]] are more likely to be core genes in the pangenome. It finds a positive, statistically robust but modest correlation across ~194,000 genes from 43 diverse bacteria, with a 16-percentage-point gradient between essential and always-neutral genes. [src: fitness_effects_conservation] The authors say fitness importance only weakly predicts conservation. [src: fitness_effects_conservation]

## Key Findings

### Fitness class and conservation

Essential genes are the most often core, and always-neutral genes the least. [src: fitness_effects_conservation] The fraction core falls steadily across the classes below. [src: fitness_effects_conservation]

| Class | Genes | % core |
|---|---|---|
| Essential (no viable mutants) | 27,693 | 82% [src: fitness_effects_conservation] |
| Often sick (>10% experiments) | 15,989 | 78% [src: fitness_effects_conservation] |
| Sometimes sick | 25,201 | 72% [src: fitness_effects_conservation] |
| Mixed (sick + beneficial) | 20,739 | 70% [src: fitness_effects_conservation] |
| Sometimes beneficial | 9,705 | 70% [src: fitness_effects_conservation] |
| Always neutral | 94,889 | 66% [src: fitness_effects_conservation] |

Binning by strongest fitness effect gives the same gradient: essential genes are 82.2% core, genes with min_fit < -3 are 77.7%, and genes with min_fit -1 to 0 are 66.4%. [src: fitness_effects_conservation]

### Breadth of importance

Genes important in more conditions are more likely to be core (Spearman rho=0.086, p=8.1e-230). [src: fitness_effects_conservation] Essential genes are 82% core. [src: fitness_effects_conservation] Genes important in 20+ experiments are 79% core, 6-20 experiments 73%, 1-5 experiments 71%, and 0 experiments 66%. [src: fitness_effects_conservation]

### Core genes show effects in both directions

Core genes are more likely than auxiliary genes to be beneficial to delete in some condition: 24.4% ever beneficial versus 19.9% for auxiliary (OR, odds ratio, =0.77 for auxiliary vs core). [src: fitness_effects_conservation] This runs against the expectation that accessory genes are costly to carry. [src: fitness_effects_conservation] The report suggests core genes may more often take part in trade-offs, helping in some conditions and costing in others. [src: fitness_effects_conservation] Core genes also have heavier tails than auxiliary genes in both the negative (important) and positive (burdensome) directions. [src: fitness_effects_conservation]

### Condition-specific effects

Genes tagged in specificphenotype for strong condition-specific effects are 77.3% core, versus 70.3% for genes without specific phenotypes (OR=1.78, p=1.8e-97). [src: fitness_effects_conservation] The report suggests core genes may have more measurable condition-specific effects because they sit in well-characterized pathways. [src: fitness_effects_conservation]

In total, 4,450 genes (2.7%) fit an "ephemeral niche gene" pattern: neutral overall but critical in one condition. [src: fitness_effects_conservation] This pattern is more common in core genes (3.0%) than in auxiliary (1.7%) or singleton (1.6%) genes. [src: fitness_effects_conservation] The report suggests core genes may simply have more detectable conditional effects because they participate in more pathways. [src: fitness_effects_conservation]

### Novel singleton genes

Novel singleton genes have near-zero mean fitness. The report suggests they are largely invisible to lab-based fitness assays, with little detectable benefit or detriment under the tested conditions. [src: fitness_effects_conservation] They are not systematically detrimental, and their mean fitness is similar to that of auxiliary genes. [src: fitness_effects_conservation] Missing fitness data for these genes may reflect poor transposon coverage rather than true neutrality. [src: fitness_effects_conservation]

### Interpretation

The report reads core genes as the most functionally active genes, with the largest fitness effects in both directions because they sit in critical pathways. [src: fitness_effects_conservation] It reads accessory genes as functionally quieter under lab conditions. [src: fitness_effects_conservation] It treats the gradient as empirical support for selection as a major driver of core gene maintenance. [src: fitness_effects_conservation] The report cites Luo et al. (2015), who showed stronger purifying selection on core than accessory genes across bacterial species. [src: fitness_effects_conservation] It also cites McInerney et al. (2017), who argued that gene frequencies reflect a balance of selection, drift, and horizontal gene transfer (HGT). [src: fitness_effects_conservation]

## Data and Methods

The report uses random barcode transposon sequencing (RB-TnSeq) mutant fitness data for ~194K genes from Price et al. (2018). [src: fitness_effects_conservation] That dataset is described as the largest resource of genome-wide bacterial mutant fitness data. [src: fitness_effects_conservation] The report adds a pangenome conservation dimension to these measurements. [src: fitness_effects_conservation] Gene-to-cluster conservation comes from a KBase pangenome link table. [src: fitness_effects_conservation] Essentiality classifications come from a separate essential-genes table. [src: fitness_effects_conservation] Condition-specific annotations come from the Fitness Browser specificphenotype table. [src: fitness_effects_conservation]

## Caveats and Open Work

- The 16-point gradient is statistically robust, but fitness importance only weakly predicts conservation. [src: fitness_effects_conservation]
- Lab conditions favour rich media and standard stresses, so many ecological niches are unrepresented. [src: fitness_effects_conservation]
- Fitness is measured for single-gene knockouts, so epistatic interactions are not captured. [src: fitness_effects_conservation]
- The 43 bacteria are mainly Proteobacteria, which limits generalizability. [src: fitness_effects_conservation]
- Singleton or novel genes may lack fitness data because of poor transposon coverage rather than true neutrality. [src: fitness_effects_conservation]

## Slots Into

- [[concepts/gene-fitness-importance-as-a-predictor-of-pangenome-conservation]]: the 16-point gradient from 82% core (essential) to 66% core (always neutral). [src: fitness_effects_conservation]
- [[concepts/essential-genes-and-core-genome-conservation]]: essential genes are 82% core. [src: fitness_effects_conservation]
- [[concepts/condition-dependent-fitness-trade-offs-of-core-versus-accessory-genes]]: core genes are more often beneficial to delete in some condition (24.4% vs 19.9%). [src: fitness_effects_conservation]
- [[concepts/costly-but-conserved-genes-laboratory-burden-versus-conservation]]: core genes show heavier tails in the burdensome direction. [src: fitness_effects_conservation]
- [[concepts/fitness-measurement-of-novel-singleton-genes-and-assay-limits]]: singleton genes have near-zero mean fitness, and the report notes the coverage caveat. [src: fitness_effects_conservation]
