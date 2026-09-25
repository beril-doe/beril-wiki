<!-- tension-hash: 9f5d14d39bddd3db -->
# Do guilt-by-association counts constitute functional evidence for dark genes, or a baseline artifact that must be kept separate from validated prediction?

Within the evidence-weighted prioritization framework of [[concepts/experimental-prioritization-of-functional-dark-matter]], projects disagree about what module membership and genomic-neighborhood context are worth as evidence. One line of reporting treats large counts of dark genes (protein-coding genes with no functional annotation) carrying module or operon context as substantive functional inference; the same and a neighboring report argue that the headline neighbor rate is what the genome-wide annotation baseline predicts anyway, and that module-based and ortholog-based predictions have measured precision so different that pooling them is unsafe. The stake is practical: whether these signals may be folded into one confidence score used to rank experimental candidates.

## Evidence Sides

**Breadth of module and neighborhood context is functional evidence.** 6,142 dark genes belonged to ICA fitness modules — independent component analysis, a signal-decomposition method that groups genes co-varying across fitness experiments — and 30,190 dark genes shared a predicted operon (co-transcribed, adjacent gene unit) with an annotated gene, while 97.2% had at least one annotated neighbor within a five-gene window. [src: functional_dark_matter]

**The same signals are guilt-by-association, and the neighbor rate is baseline-expected.** Module and neighborhood predictions are guilt-by-association inferences — function assumed from an annotated associate — rather than direct experimental validation. [src: functional_dark_matter] The report further cautions that the 97.2% neighbor rate is expected given a 75% genome-wide annotation rate. [src: functional_dark_matter]

**Gene-level and process-level predictors are not interchangeable.** Ortholog transfer (assigning function from an evolutionary counterpart) achieved 95.8% precision and 91.2% coverage for gene-level KO prediction — KO being KEGG Orthology, a specific molecular-function identifier — while Module-ICA had <1% KO-level precision while capturing process-level co-regulation. [src: discoveries] These should remain distinct evidence products rather than being combined into one confidence score without calibration. [src: discoveries]

## Possible Reconciliations

- *Hypothesis:* the two sides measure different quantities — coverage versus enrichment over baseline — so both statements can hold if neighborhood evidence is scored as a departure from the 75% annotation baseline rather than as a raw rate. [src: functional_dark_matter]
- *Hypothesis:* the precision gap reflects mismatched prediction targets, not predictor quality, so module evidence would be informative at a process-level target and uninformative at the KO-level target against which it was scored. [src: discoveries]
- *Hypothesis:* the signals are combinable only after per-signal calibration, in which case a single confidence score is premature but not impossible. [src: discoveries]

## Resolving Work

- Recompute the neighbor statistic on annotated (non-dark) genes under the identical five-gene window to ask whether the 97.2% rate exceeds the matched-baseline expectation. [src: functional_dark_matter]
- Score the 6,142 module-member dark genes against process-level rather than KO-level labels, and ask whether Module-ICA precision rises when the prediction target matches the signal. [src: discoveries]
- Cross-tabulate the 30,190 operon-partnered genes against ortholog-transfer calls to ask how often the two evidence products agree, disagree, or cover disjoint genes.
- Hold out experimentally characterized dark genes and fit per-signal calibration curves, asking whether a pooled confidence score outperforms the best single signal.
- Test module and neighborhood evidence independently against direct assay outcomes, asking which signal survives as a predictor once the other is conditioned on.
