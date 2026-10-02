<!-- tension-hash: 10ef6928e49ddfba -->
# Complex I dispensability on glucose: NDH-2 compensation or a species-specific wiring pattern?

Two projects in this corpus read Complex I (NDH-1, the proton-pumping NADH:quinone oxidoreductase) dependence in ADP1 on glucose in incompatible ways. The earlier transferred-fitness interpretation reports Complex I as dispensable on glucose and lactate and treats this as consistent with compensation by NDH-2 (type II NADH dehydrogenase, a single-subunit enzyme that oxidizes NADH without translocating protons). [src: aromatic_catabolism_network] The new ADP1-specific analysis reports a Complex I growth ratio of 1.44 on glucose, predicts zero NDH-2 flux, and finds no significant cross-species compensation pattern (p = 0.52). [src: respiratory_chain_wiring] The disagreement matters because it decides whether the NADH-load model on [[concepts/respiratory-capacity-and-nadh-load]] generalizes across bacteria or describes one organism's respiratory architecture.

## Evidence Sides

**Transferred-fitness interpretation: dispensability is consistent with NDH-2 compensation.** The earlier analysis reports Complex I as dispensable on glucose and lactate and treats this as consistent with NDH-2 compensation. [src: aromatic_catabolism_network] On this reading, the fitness signal is transferred across organisms, and the absence of a Complex I requirement on these carbon sources is explained by an alternative dehydrogenase absorbing the reducing-equivalent flux rather than by any organism-specific feature.

**ADP1-specific analysis: the compensation pattern is not detected.** The new ADP1-specific analysis reports a Complex I growth ratio of 1.44 on glucose, predicts zero NDH-2 flux under standard FBA (flux balance analysis, constraint-based prediction of steady-state metabolic fluxes) conditions, and finds no significant cross-species compensation pattern (p = 0.52). [src: respiratory_chain_wiring] This is a null result on the compensation test, not a demonstration that NDH-2 is absent or inactive; the p = 0.52 comparison fails to reject the null, and the zero-flux prediction is a model output under one set of assumptions.

## Possible Reconciliations

- **Metric hypothesis:** the two sides may be scoring different quantities — a transferred fitness score versus a directly measured growth ratio — so that "dispensable" and a ratio of 1.44 are not the same claim about the same denominator. These results do not establish that the earlier interpretation is false: they may reflect different fitness metrics. [src: respiratory_chain_wiring]
- **Model-assumption hypothesis:** the predicted zero NDH-2 flux may follow from standard FBA constraints rather than from biology, so the difference may reflect model assumptions. [src: respiratory_chain_wiring]
- **Architecture hypothesis:** compensation may operate in some lineages and not others, so the apparent conflict may reflect species-level respiratory architectures. [src: respiratory_chain_wiring]

## Resolving Work

- Matched ADP1 deletion assays across carbon sources, scored with a single fitness metric, to test whether Complex I dispensability on glucose survives when the metric is held constant. [src: respiratory_chain_wiring]
- Direct NADH/NAD⁺ ratio measurements across carbon sources in wild-type and Complex I–deleted ADP1, asking whether redox balance is maintained when Complex I is absent. [src: respiratory_chain_wiring]
- NDH-2 deletion and double-deletion assays in ADP1, asking whether NDH-2 carries any flux at all on glucose, against the zero-flux prediction. [src: respiratory_chain_wiring]
- Re-running the cross-species comparison with a larger organism panel, asking whether the non-significant compensation pattern (p = 0.52) reflects a true null or limited power. [src: respiratory_chain_wiring]
