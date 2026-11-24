---
type: "Concept"
description: "Whether genes essential for growth in transposon-mutant libraries are preferentially core versus accessory across a species' pangenome, including essential-core, essential-auxiliary, universal, variable and orphan essentials; stops at laboratory-condition fitness beyond essentiality."
sources: ["summaries/acinetobacter_adp1_explorer__REPORT.md", "summaries/conservation_fitness_synthesis__REPORT.md", "summaries/conservation_vs_fitness__REPORT.md", "summaries/discoveries.md", "summaries/essential_genome__REPORT.md", "summaries/field_vs_lab_fitness__REPORT.md", "summaries/fitness_effects_conservation__REPORT.md", "summaries/pitfalls.md"]
---
# Essential genes and core genome conservation

Genes essential for growth in transposon-mutant libraries are somewhat more often core than other genes, but the enrichment is modest. [src: acinetobacter_adp1_explorer, conservation_vs_fitness, discoveries] The evidence comes mostly from Fitness Browser organisms plus one ADP1 study. Essentiality calls rest on missing transposon insertions, so they are putative. The core percentage also depends on the denominator used, so figures from different analyses are not directly comparable. [src: pitfalls] See [[concepts/limits-of-transposon-based-essentiality-calls]].

## Overall enrichment: real but modest

Reports agree that essential genes are more often core, and that the effect is small because most genes in well-characterized bacteria are core anyway. [src: conservation_vs_fitness, discoveries]

- In ADP1, essential genes are more likely to be in the core pangenome. [src: acinetobacter_adp1_explorer]
- The synthesis reports a gradient from essential genes (82% core) to always-neutral genes (66% core). [src: conservation_fitness_synthesis]
- The same gradient holds when binning Fitness Browser genes by strongest fitness effect: essential 82.2% core, min_fit < -3 77.7%, and min_fit -1 to 0 66.4%. [src: fitness_effects_conservation]
- A separate Fitness Browser table lists essential genes with no viable mutants as 27,693 genes, 82% core. [src: fitness_effects_conservation]
- In fitness_effects_conservation, essential genes absent from genefitness are reported as 82% core and called the most functionally important genes. [src: pitfalls]
- Across 33 bacteria, 27,693 putative essential genes make up 18.6% of 148,826 protein-coding genes, with a per-organism range of 12.9-28.9%. [src: conservation_vs_fitness]
- In conservation_vs_fitness, essential genes are 86.1% core versus 81.2% for non-essential genes. [src: conservation_vs_fitness, discoveries] The median odds ratio (OR) is 1.56. [src: conservation_vs_fitness]
- The enrichment was significant in 18 of 33 organisms by Fisher's exact test with Benjamini-Hochberg false discovery rate (BH-FDR) q < 0.05. [src: conservation_vs_fitness]
- The strongest signals were *Methanococcus maripaludis* S2 (OR=5.21), *Ralstonia syzygii* PSI07 (OR=3.41) and *Marinobacter adhaerens* (OR=3.08). [src: conservation_vs_fitness]
- Clade-size and lifestyle stratification show the enrichment is robust across diverse genomic contexts. [src: conservation_vs_fitness] The signal is strongest in organisms with larger clades, which give more reliable core classification. [src: discoveries]

### The denominator matters

The 82% and 86% figures differ partly by denominator. In conservation_fitness_synthesis, essential genes were 82% core using all genes including unmapped ones, versus 86% using mapped genes only. [src: pitfalls] This mismatch caused a critical review issue, because figures showed 86%/78% while the prose said 82%/66%. [src: pitfalls] Figures from other reports, such as the 86.1% in conservation_vs_fitness, are separate analyses and each stands on its own. [src: conservation_fitness_synthesis, conservation_vs_fitness]

## Categories of essential genes

The conservation_vs_fitness report splits genes by pangenome status, and the categories differ sharply in annotation. [src: conservation_vs_fitness]

| Category | Genes | % enzymes | % hypothetical | Tags |
|---|---|---|---|---|
| Essential-core | 22,751 | 41.9% | 13.0% | [src: conservation_vs_fitness] |
| Essential-auxiliary | 3,683 | 13.4% | 38.2% | [src: conservation_vs_fitness] |
| Essential-unmapped | 1,259 | 18.2% | 44.7% | [src: conservation_vs_fitness] |
| Non-essential | 124,744 | 21.5% | 24.5% | [src: conservation_vs_fitness] |

- **Essential-core.** These genes are the most enzyme-rich and best annotated, with 87% having known function. [src: conservation_vs_fitness] They form a well-characterized backbone of ribosomes, DNA replication, cell wall and cofactor biosynthesis. [src: discoveries] Versus non-essential genes they are enriched in Protein Metabolism (+13.7 percentage points), Cofactors/Vitamins (+6.2%), Cell Wall (+3.9%) and Fatty Acid biosynthesis (+3.1%). [src: conservation_vs_fitness] They are depleted in Carbohydrates (-7.9%), Amino Acids (-5.6%) and Membrane Transport (-4.0%), which the report describes as conditionally important rather than universally essential. [src: conservation_vs_fitness]
- **Essential-auxiliary.** These genes are essential for viability but not present in all strains. [src: conservation_vs_fitness, discoveries] The top subsystems are ribosomes, DNA replication, type 4 secretion and plasmid replication, which the report reads as strain-specific variants of core machinery plus mobile genetic elements. [src: conservation_vs_fitness]
- **Essential-unmapped.** These are strain-specific essentials with no pangenome cluster match, and the least characterized category. [src: conservation_vs_fitness] Known functions include divergent ribosomal proteins L34, L36, S11 and S12, translation factors, transposases and DNA-binding proteins, interpreted as likely recently acquired or highly divergent variants of core functions. [src: conservation_vs_fitness] They are named as targets for functional discovery. [src: discoveries]

The report parallels these categories with Rosconi et al. (2022), who studied 36 *S. pneumoniae* strains and found that the pan-genome makes essentiality strain-dependent. [src: conservation_vs_fitness] That study named "universal essential," "core strain-specific essential" and "accessory essential" genes, and the report says it extends the concept across 33 diverse species. [src: conservation_vs_fitness]

## Universal, variable and orphan essentials

In the essential_genome analysis, core fraction falls sharply only for orphan essentials. [src: essential_genome]

| Class | % core | Genes | Tags |
|---|---|---|---|
| Universally essential | 91.7% | 6,963 | [src: essential_genome] |
| Variably essential | 88.9% | 90,844 | [src: essential_genome] |
| Never essential | 81.7% | 47,140 | [src: essential_genome] |
| Orphan essential | 49.5% | 4,683 | [src: essential_genome] |

- Universally essential genes are 91.7% core versus 80.7% for non-essential genes. [src: discoveries, essential_genome]
- 71% of universally essential families are 100% core across all genomes in their species. [src: discoveries, essential_genome]
- Essentiality penetrance and core fraction correlate only weakly (rho=0.123, p=1.6e-17). Core fraction is 97.1% for families with >80% penetrance versus 92.8% for those with <20%. [src: essential_genome]
- 7,084 essential genes have no orthologs in any other Fitness Browser organism. [src: discoveries, essential_genome] Of these, 58.7% are annotated as hypothetical proteins, while universally essential genes are only 8.2% hypothetical. [src: discoveries]
- Orphan essentials are only 49.5% core and are described as strain-specific essential functions not conserved across species. [src: discoveries] The report suggests they may include recently acquired genes, rapidly evolving proteins or lineage-specific innovations, and that many are not conserved even within their own species. [src: essential_genome]
- The report identifies orphan essentials as prime candidates for novel biology. [src: discoveries]
- The 7,084 no-ortholog count and the 4,683 orphan essentials in the hierarchy table are different numbers, and the claims do not say how they relate. [src: essential_genome]
- The essential_genome report proposes rerunning its analysis as Fitness Browser taxonomic coverage expands, to test whether the 15 pan-essential families remain universal. [src: essential_genome]

## Caveats from excluded genes

In *Desulfovibrio vulgaris* Hildenborough, 678 essential genes (80.1% core) lack fitness data because no transposon mutants were recovered, so they are excluded from the fitness analysis. [src: field_vs_lab_fitness] Among 2,725 non-essential genes with fitness data and pangenome links, 76.3% are core. [src: field_vs_lab_fitness] Including the essentials would slightly raise the overall baseline but would not change condition-class comparisons, which use only non-essential genes. [src: field_vs_lab_fitness]

## Open Directions

- Rerun the essential_genome analysis on expanded Fitness Browser coverage to test the 15 pan-essential families.
- Reconcile the 7,084 no-ortholog genes with the 4,683 orphan essentials by tracing which genes fall in each set. This would clarify the orphan definition.
- Recompute essential-gene core percentages for every report with both denominators (all genes versus mapped genes only), to separate real differences from denominator effects.
- Check whether the 49.5% core rate of orphan essentials reflects true accessory status or poor core classification in small clades, by comparing against clade size.
- Test whether essential-unmapped genes are divergent core-function variants or acquired genes, by comparing their sequences with core homologs.
- Repeat the enrichment test in the 15 organisms where it was not significant, to separate low power from a true absence of effect.
