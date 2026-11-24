---
type: "Concept"
description: "Whether knocking out resistance genes becomes more harmful when matching or any antibiotic is present, and how mechanism breadth (efflux versus enzymatic) modulates it; stops at baseline cost."
sources: ["summaries/amr_fitness_cost__REPORT.md", "summaries/amr_pangenome_atlas__REPORT.md", "summaries/discoveries.md"]
---
# Antibiotic-dependent fitness flip of resistance genes

Under any antibiotic, 57% of antimicrobial resistance (AMR) genes become more important when knocked out, and the effect depends on mechanism. [src: amr_fitness_cost] The evidence comes from one project, amr_fitness_cost, which is summarised in [[summaries/amr_fitness_cost__REPORT]]. The any-antibiotic result is significant. The stricter class-matched result is not significant. [src: amr_fitness_cost] The page stops at the effect of antibiotics; baseline cost is covered in [[concepts/fitness-cost-of-antimicrobial-resistance-genes]].

## Literature Context

The candidate papers do not test genome-wide knockout fitness, so none directly replicates the hub's central result. They do bear on the idea that the fitness effect of a resistance gene depends on whether antibiotic is present. They are mostly experiments on single strains or plasmids, or on small sets of strains, and they are not pooled knockout screens.

Several studies find that the cost of carrying resistance shrinks or disappears under antibiotic exposure. In engineered E. coli carrying different trimethoprim resistance genes (dfr), strains with the introduced genes grew slower than sensitive ones at 0 and 10 µg/L. A significant reduction in cost was found already at 10 µg/L [PMID 32890888](https://pubmed.ncbi.nlm.nih.gov/32890888/). In E. coli carrying prophages with or without resistance genes, the resistance genes were more beneficial upon antibiotic exposure, and the benefits of prophages and of resistance genes peaked in different environments [PMID 33347602](https://pubmed.ncbi.nlm.nih.gov/33347602/). For the mcr-1 IncI2 plasmid pBD110, strong colistin selection (4 mg/L) increased plasmid abundance. Moderate pressure (2 mg/L) led to fitness costs and reduced plasmid copy number, and the plasmid was stably maintained for 120 passages without colistin [PMID 41257606](https://pubmed.ncbi.nlm.nih.gov/41257606/). These are laboratory experiments on a few constructs, and the direction of the effect depends on concentration.

Other reports describe amplification of resistance genes. In a single patient's pre- and post-treatment E. coli strains, IS26-mediated blaCTX-M-65 amplification did not impose fitness costs and was associated with faster growth under high antibiotic concentrations [PMID 37802302](https://pubmed.ncbi.nlm.nih.gov/37802302/). In a hypervirulent Klebsiella pneumoniae isolate, a two-copy blaKPC-14 arrangement gave high-level cross-resistance without appreciable fitness cost [PMID 42435862](https://pubmed.ncbi.nlm.nih.gov/42435862/). Both are single-isolate observations. A review of last-resort resistance genes likewise notes that persistence relies on compensatory evolution and context-dependent fitness costs [PMID 41621305](https://pubmed.ncbi.nlm.nih.gov/41621305/).

The corpus finds that 57% of AMR genes show a flip under any antibiotic (Wilcoxon p = 0.0001, N = 797). The stricter class-matched test, with 157 gene-antibiotic pairs, is not significant (p = 0.14). The papers above support the general direction. Resistance genes are less costly, or more useful, when antibiotic is present, so the any-antibiotic result is **consistent with** the literature. They tested matching antibiotics in targeted designs, whereas the corpus's matched test did not reach significance. That gap is not resolved by these papers, and the class-matched result should stay null.

The mechanism-breadth finding is not addressed by any candidate. The corpus reports that efflux genes flip more strongly than enzymatic inactivation genes (+0.094 vs −0.001, MWU p = 0.007). No candidate compares efflux with enzymatic genes, so this finding is **novel** relative to this evidence. It has not been confirmed or contradicted here. The corpus's mean flips are small (+0.045 for any-antibiotic). The papers describe cost changes in different units, such as growth rate and competition, so the numbers cannot be compared directly.

## Any-antibiotic flip

Under any antibiotic, 57% of AMR genes show a fitness flip: they have lower fitness when knocked out than under non-antibiotic conditions (Wilcoxon signed-rank p = 0.0001, N = 797). [src: amr_fitness_cost] The report calls this analysis much better powered and highly significant. [src: amr_fitness_cost] The mean flip is +0.045 (noabx − abx fitness). The report reads this as a shift from slight burden to slight importance. [src: amr_fitness_cost] The report suggests that the 43% of genes that do not flip likely reflect narrow-spectrum resistance tested against non-matching antibiotics, not non-functional genes. [src: amr_fitness_cost]

## Class-matched validation

The class-matched analysis does not confirm the flip at conventional significance. It used 157 gene-antibiotic pairs across 4 resistance classes. The mean flip was +0.113, and the Wilcoxon signed-rank test gave p = 0.14. [src: amr_fitness_cost] The report attributes this to small numbers per class after matching and to heterogeneity across organisms. Some organisms show strong flips and others near zero. [src: amr_fitness_cost]

| Metric | Class-matched | Any-antibiotic |
|---|---|---|
| Gene-antibiotic pairs | 157 | 797 [src: amr_fitness_cost] |
| Fraction more important under antibiotic | 54.8% | 57.0% [src: amr_fitness_cost] |
| Mean fitness flip | +0.113 | +0.045 [src: amr_fitness_cost] |
| Wilcoxon p | 0.14 [src: amr_fitness_cost] | 0.0001 [src: amr_fitness_cost] |

Within the class-matched set, chloramphenicol resistance genes show the expected flip in 6/6 (100%) cases. [src: amr_fitness_cost] Beta-lactam genes (105 pairs across 10 organisms) show a 50% flip rate. The report considers this consistent with many tests using non-carbenicillin beta-lactams. [src: amr_fitness_cost]

Two limits apply. Only 4 classes have matched antibiotic experiments: beta-lactam, aminoglycoside, chloramphenicol and tetracycline. [src: amr_fitness_cost] Macrolide, glycopeptide and polymyxin classes could not be validated. [src: amr_fitness_cost] The report classified 6,804 experiments, of which 443 were antibiotic experiments. [src: amr_fitness_cost]

## Mechanism breadth

The flip depends on mechanism, even though the report says baseline cost does not. [src: amr_fitness_cost] Efflux genes, which are broad-spectrum, flip more strongly than enzymatic inactivation genes, which are narrow-spectrum: +0.094 vs −0.001, MWU (Mann-Whitney U) p = 0.007. [src: amr_fitness_cost, discoveries] The report also states that broad-spectrum mechanisms show stronger antibiotic-dependent importance in general (MWU p = 0.007). [src: amr_fitness_cost]

The report's explanation is that [[entities/efflux-pumps]] protect against many antibiotics. They should matter under any antibiotic experiment. Narrow-spectrum enzymes such as beta-lactamases matter only when the matching antibiotic is present. [src: amr_fitness_cost] Efflux pumps therefore become significantly more important under any antibiotic (flip +0.094). [src: amr_fitness_cost] [[entities/enzymatic-inactivation-of-antibiotics]] genes flip only under their matching antibiotic. [src: amr_fitness_cost]

## Related proposal

The amr_pangenome_atlas report ([[summaries/amr_pangenome_atlas__REPORT]]) proposes using the full "FB-pangenome link table" to test fitness costs under antibiotic stress conditions, not just standard lab media. [src: amr_pangenome_atlas]

## Open Directions

- Run the expansion proposed above: test AMR fitness costs under antibiotic stress across the full link table. This would close the gap left by the small matched set.
- Add matched experiments for macrolide, glycopeptide and polymyxin classes, which currently lack them. Then test whether narrow-spectrum genes flip only under their matching antibiotic.
- Fit a per-organism model of the flip to quantify the heterogeneity behind the nonsignificant class-matched result.
- Separate carbenicillin from other beta-lactams in the beta-lactam pairs. This would test the explanation for their 50% flip rate.
