<!-- tension-hash: 8cd3f2196491d149 -->
# NADH-per-Carbon Stoichiometry and Flux Models Versus Measured Complex I Dependence on Quinate

Two lines of evidence give different accounts of which NADH (reduced nicotinamide adenine dinucleotide) dehydrogenase, Complex I or NDH-2, a cell needs on a given carbon source. Stoichiometric accounting says quinate yields 0.57 NADH per carbon and glucose yields 1.50 [src: respiratory_chain_wiring] [src: discoveries]. If per-carbon yield tracked reoxidation demand, a hypothesis rather than a finding, quinate would need Complex I less. Measured mutant fitness shows the reverse: Complex I is required on quinate but dispensable on glucose [src: respiratory_chain_wiring] [src: discoveries]. Flux balance analysis (FBA), a constraint-based metabolic model that optimizes a chosen objective, adds a second mismatch. It assigns zero flux to NDH-2, and a cross-species test for NDH-2 compensation found no significant pattern (p=0.52, where the p-value is the probability of a result at least this extreme if no pattern exists) [src: respiratory_chain_wiring] [src: discoveries]. The disagreement matters for [[concepts/gene-essentiality]] because stoichiometric and model-based predictors diverge here from measured fitness on respiratory genes [src: respiratory_chain_wiring] [src: discoveries].

## Evidence Sides

**Side 1: Stoichiometric and model-based expectation**
- Quinate's theoretical yield is 0.57 NADH per carbon, compared with 1.50 NADH per carbon for glucose [src: respiratory_chain_wiring] [src: discoveries].
- FBA predicted zero NDH-2 flux because it optimizes ATP (adenosine triphosphate, the cell's energy currency) yield [src: respiratory_chain_wiring] [src: discoveries].

**Side 2: Measured fitness**
- Complex I was required on quinate despite the lower NADH-per-carbon yield [src: respiratory_chain_wiring] [src: discoveries].
- Complex I was dispensable on glucose despite the higher NADH-per-carbon yield [src: respiratory_chain_wiring] [src: discoveries].
- The cross-species NDH-2 comparison found no significant compensatory pattern (p=0.52). This is a null result: it does not show that NDH-2 compensates for Complex I loss, and it does not show that NDH-2 cannot [src: respiratory_chain_wiring] [src: discoveries].

## Possible Reconciliations

- **Hypothesis A: timing of NADH production matters more than the total.** Per-carbon NADH totals may miss when and where NADH is produced. A substrate that releases NADH in a concentrated pulse could exceed NDH-2's reoxidation capacity even at a low overall yield. Direct flux or kinetic evidence for this is not supplied here.
- **Hypothesis B: the model's objective is wrong for this question.** Because the model optimizes ATP yield, its zero NDH-2 flux may reflect the chosen objective rather than enzyme usage in the cell.
- **Hypothesis C: the pattern is lineage-specific.** The absence of a cross-species compensatory pattern may mean the condition-dependent wiring holds in some organisms but not others. Alternatively, the comparison may lack the power to detect a real pattern.

## Resolving Work

- **Rerun FBA with capacity limits.** Re-solve the quinate and glucose models with enzyme-capacity constraints on NDH-2 (for example, proteome-limited FBA). Question: does a capacity-limited model reproduce Complex I dependence on quinate?
- **Measure NADH dynamics directly.** Track time-resolved NADH/NAD⁺ ratios in wild type and Complex I mutants on quinate and glucose. Question: does quinate catabolism produce a transient NADH peak that glucose catabolism does not?
- **Test NDH-2 by perturbation.** Build NDH-2 overexpression and deletion strains and measure growth on quinate. Question: does added NDH-2 capacity rescue Complex I mutants, as Hypothesis A predicts?
- **Expand the cross-species comparison.** Add organisms with curated, rather than text-matched, NDH-2 annotations and analyze them with a phylogenetically controlled comparison. Question: does any NDH-2 compensatory pattern emerge, or does the p=0.52 null hold with more taxa [src: respiratory_chain_wiring] [src: discoveries]?
- **Check other aromatic substrates.** Measure Complex I fitness on additional aromatic substrates that share quinate's catabolic route. Question: is quinate's Complex I requirement a property of the pathway or of the single substrate?
