<!-- tension-hash: 3d728916a85ef7d0 -->
# Is Complex I dispensable on glucose and lactate because NDH-2 compensates?

Projects disagree on how to read Complex I dispensability on non-aromatic carbon sources. Complex I is a respiratory NADH dehydrogenase, where NADH is reduced nicotinamide adenine dinucleotide. One reading treats its dispensability on glucose and lactate as consistent with compensation by NDH-2, an alternative NADH dehydrogenase. [src: aromatic_catabolism_network] An ADP1-specific analysis finds no significant cross-species compensation pattern. [src: respiratory_chain_wiring] The question matters for [[concepts/respiratory-capacity-and-nadh-load]]. If NDH-2 compensation explains substrate-dependent Complex I requirements, respiratory dependence could reflect dehydrogenase redundancy rather than NADH load alone.

## Evidence Sides

**Side 1: Complex I is dispensable, consistent with NDH-2 compensation**

The earlier interpretation used transferred fitness, meaning fitness scores carried over from ortholog genes in other organisms. On that basis it reports Complex I as dispensable on glucose and lactate. It treats this as consistent with NDH-2 compensating for Complex I loss. [src: aromatic_catabolism_network]

**Side 2: ADP1-specific and cross-species evidence does not support compensation**

The ADP1-specific analysis makes three findings. [src: respiratory_chain_wiring]
- It reports a Complex I growth ratio of 1.44 on glucose. [src: respiratory_chain_wiring]
- Under standard flux balance analysis (FBA) conditions, it predicts zero NDH-2 flux. FBA is a constraint-based model that predicts steady-state reaction fluxes. [src: respiratory_chain_wiring]
- It finds no significant cross-species compensation pattern (p = 0.52; the p-value is the probability of a result at least this extreme if the null hypothesis of no pattern were true). [src: respiratory_chain_wiring]

The central digest adds that an earlier cross-species result seemed to support compensation. That result was an annotation artifact: the NDH-2 candidates had been identified by text matching. [src: discoveries]

On lactate, the ADP1 wiring analysis reports a mild Complex I effect (0.77) rather than outright dispensability. [src: respiratory_chain_wiring]

These results do not establish that the earlier interpretation is false. [src: respiratory_chain_wiring]

## Possible Reconciliations

- **Hypothesis: different fitness metrics.** Ortholog-transferred fitness scores and ADP1 growth ratios may measure different quantities. If so, "dispensable" and "mild effect" could describe the same underlying phenotype at different resolutions. [src: respiratory_chain_wiring]
- **Hypothesis: model assumptions.** The zero NDH-2 flux prediction may depend on the standard FBA objective and constraints. If so, it may say little about NDH-2 activity in vivo. [src: respiratory_chain_wiring]
- **Hypothesis: species-level respiratory architectures.** Compensation by NDH-2 may operate in some species and not others. If so, a strain-specific ADP1 result and a cross-species transferred result need not conflict. [src: respiratory_chain_wiring]

## Resolving Work

- **Matched deletion assays.** Build matched ADP1 deletion assays: Complex I, NDH-2, and the double deletion, each grown on glucose and lactate. This asks whether NDH-2 loss unmasks a Complex I requirement in ADP1. [src: respiratory_chain_wiring]
- **Direct redox measurements.** Measure the NADH/NAD⁺ ratio (NAD⁺ is the oxidized form) across carbon sources in wild-type and Complex I mutants. This tests whether Complex I loss perturbs redox balance on substrates where growth looks unaffected. [src: respiratory_chain_wiring]
- **Validated cross-species annotations.** Repeat the cross-species compensation test using NDH-2 calls validated by domain or homology evidence rather than text matching. This would show whether any compensation signal survives once annotation artifacts are removed. [src: discoveries]
- **Altered FBA constraints.** Rerun FBA with NDH-2 flux allowed under alternative objectives and capacity constraints, asking whether the zero-flux prediction is robust or depends on model assumptions. [src: respiratory_chain_wiring]
- **Same-metric comparison.** Recompute transferred fitness and ADP1 growth ratios for the same genes and conditions on a common scale, asking whether the disagreement reflects the fitness metric rather than the biology. [src: respiratory_chain_wiring]
