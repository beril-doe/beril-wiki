<!-- tension-hash: 9f5d14d39bddd3db -->
# How much functional weight should module and neighborhood evidence carry for dark genes?

The [[concepts/experimental-prioritization-of-functional-dark-matter]] framework ranks "dark" genes (genes without functional annotation) partly by guilt-by-association, which infers function from co-regulated or co-located genes. Fitness modules are gene sets grouped by independent component analysis (ICA), a method that decomposes fitness profiles into independent signals. Genomic neighborhoods are genes that share a predicted operon (a co-transcribed gene cluster) or sit nearby on the chromosome. This association evidence covers many dark genes, but it is not direct experimental validation, and part of it is expected by chance. [src: functional_dark_matter] Module evidence also performs poorly at predicting specific molecular functions. [src: discoveries] The disagreement matters because merging these signals into one score could inflate confidence in candidates chosen for costly experiments.

## Evidence Sides

**Side 1: Module and neighborhood evidence provides broad functional context.** In the dark-gene census, 6,142 dark genes belonged to ICA fitness modules. 30,190 dark genes shared a predicted operon with an annotated gene, and 97.2% had at least one annotated neighbor within a five-gene window. [src: functional_dark_matter] The central digest reports that Module-ICA captures process-level co-regulation. [src: discoveries]

**Side 2: These signals are inference, partly expected by chance, and weak at the level of specific function.** Module and neighborhood predictions are guilt-by-association inferences rather than direct experimental validation. [src: functional_dark_matter] The report cautions that the 97.2% neighbor rate is expected given a 75% genome-wide annotation rate. [src: functional_dark_matter] The benchmark predicted KO (KEGG Orthology, a catalogue of molecular-function groups) at the gene level. In it, ortholog transfer, which assigns function from homologous genes in other organisms, achieved 95.8% precision and 91.2% coverage. Precision is the share of a method's predictions that are correct, and coverage is the share of genes for which the method makes a prediction. Module-ICA had <1% KO-level precision. [src: discoveries]

## Possible Reconciliations

- *Hypothesis:* The two sides measure different things. Module and neighborhood evidence may be valid for process-level statements ("involved in a process") while failing at specific molecular-function statements. That would make the sides complementary rather than contradictory. [src: discoveries]
- *Hypothesis:* Neighborhood evidence may carry information only where it departs from the background expected from the genome-wide annotation rate. If so, raw neighbor presence should be discounted, but specific operon-level linkage should not. [src: functional_dark_matter]
- *Hypothesis:* These signals may be most useful as hypothesis generators that rank leads for experiments, not as functional assignments. That would keep them as distinct evidence products and not merge them into one uncalibrated confidence score.

## Resolving Work

- Use held-out KO benchmarks scored separately at the process level (e.g., pathway or module membership) and the gene level. This would test whether Module-ICA precision rises at the coarser level while ortholog-transfer precision stays specific.
- Build a permutation null for neighborhoods that shuffles annotation labels across genomes while keeping each genome's annotation rate. This would test whether dark genes' annotated-neighbor and operon-partner rates exceed chance.
- Apply calibration curves to each evidence channel (modules, operon partners, five-gene-window neighbors, ortholog transfer) against genes with known function. This would test whether each channel's scores map to observed accuracy before any combined score is formed.
- Compare experimental outcomes for prioritized dark genes, contrasting candidates supported by module or neighborhood evidence alone with candidates that also carry direct fitness phenotypes. This would test whether association-only candidates validate at a lower rate.
