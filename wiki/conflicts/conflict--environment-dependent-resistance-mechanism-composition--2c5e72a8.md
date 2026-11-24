<!-- tension-hash: 2c5e72a8f2a73485 -->
# Efflux and Target-Modification Shares of AMR: Conflicting Figures Within One Resistome Analysis

The amr_environmental_resistome analysis and the discoveries digest report different shares of antimicrobial resistance (AMR) attributed to efflux pumps and to target modification in human gut and clinical bacteria. The figures differ between the report's own table, its narrative and its summary line, and also between the report and the digest. The sources do not say what causes the difference, and it has not been reconciled. This matters because the concept [[concepts/environment-dependent-resistance-mechanism-composition]] reads these shares as evidence of niche-specific selection, and the size of that signal depends on which figures are used. Here η² (eta-squared) is the effect-size statistic for how much variation in a mechanism's share is explained by environment.

## Evidence Sides

**Efflux pumps in human gut and clinical species**

- The report's table gives efflux as 7.0% of human gut AMR, with η²=0.055. [src: amr_environmental_resistome]
- The discoveries digest gives 21% in human gut versus 1% in aquatic, with η²=0.127. [src: discoveries]
- The report's narrative gives clinical and gut efflux as 15-21%. [src: amr_environmental_resistome]

**Target modification in clinical and gut species**

- The report's table gives 27.5% clinical and 43.6% human gut. [src: amr_environmental_resistome]
- The report's narrative gives 19-29% for clinical and gut bacteria. [src: amr_environmental_resistome]
- The report's summary line gives 28-44%. [src: amr_environmental_resistome]

The two sides are not cleanly separated by source. For efflux, the report's table disagrees with both the digest and the report's own narrative. For target modification, the disagreement is entirely inside the report.

## Possible Reconciliations

- **Hypothesis: different denominators or groupings.** The figures may be computed over different sets of species, genes or environment categories. The sources do not say, so this is untested.
- **Hypothesis: different analysis versions.** The narrative and digest may come from an earlier or later run than the table. Nothing in the evidence confirms this.
- **Hypothesis: transcription or rounding into ranges.** The ranges (15-21%, 19-29%, 28-44%) may be loose summaries of the table. They do not match the table values for efflux, so this is doubtful for efflux in particular.

## Resolving Work

- Recompute efflux share per environment from the underlying AMR annotations, using the same species set and stating the denominator. This asks whether the human gut value is nearer 7.0% or 21%.
- Re-run the Kruskal-Wallis test (a rank-based test of differences across groups) for efflux by environment and compare η² with 0.055 and 0.127. This asks which effect size the data support.
- Trace the origin of the narrative ranges (15-21%, 19-29%, 28-44%) in the report's text against its table. This asks whether they come from a different grouping of environments.
- Compare the digest's 21% and 1% efflux figures with the report's per-environment table by tracing the digest's inputs. This asks whether the digest used a different category definition.
- Repeat the target-modification comparison for clinical and human gut species under a single fixed definition. This asks whether the 27.5% and 43.6% table values are reproduced.
