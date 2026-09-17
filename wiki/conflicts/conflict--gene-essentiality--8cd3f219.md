<!-- tension-hash: 8cd3f2196491d149 -->
# Complex I on Quinate: Measured Essentiality Against Stoichiometric Prediction and a Cross-Species Null

Three lines of evidence about the same respiratory branch point point in different directions. Direct growth measurement makes Complex I, a respiratory-chain NADH dehydrogenase, required on quinate at a theoretical yield of 0.57 NADH per carbon while dispensable on glucose at 1.50 NADH per carbon — the opposite ordering from what reduced-cofactor supply alone would predict [src: respiratory_chain_wiring]. A constraint-based metabolic model assigned no flux at all to NDH-2, the alternative route for NADH reoxidation [src: respiratory_chain_wiring]. And a comparison across species found no significant pattern of NDH-2 compensating for Complex I (p=0.52) [src: discoveries]. Which of these is the load-bearing description of essentiality here matters for [[concepts/gene-essentiality]], where measured perturbation, metabolic modelling and cross-species comparison all feed one synthesis while carrying different evidential weight.

## Evidence Sides

**Measured essentiality contradicts per-carbon NADH supply.** Complex I was required for growth on quinate, where the theoretical yield is 0.57 NADH per carbon, and dispensable on glucose, where the theoretical yield is 1.50 NADH per carbon [src: respiratory_chain_wiring]. This is a direct perturbation-and-growth result, the strongest evidence class in this corpus, and it inverts the expectation that higher reduced-cofactor flux imposes greater dependence on the pumping dehydrogenase.

**Flux balance analysis predicts NDH-2 carries nothing.** Flux balance analysis (FBA) — steady-state optimization of a stoichiometric network under an objective — predicted zero NDH-2 flux because it optimizes ATP yield [src: respiratory_chain_wiring]. The prediction is a consequence of that objective function, not an independent measurement, so it cannot by itself adjudicate whether NDH-2 is used in vivo.

**The cross-species comparison returns a null.** Testing whether NDH-2 presence predicts Complex I dispensability across organisms found no significant compensatory pattern, p=0.52 [src: respiratory_chain_wiring, discoveries]. This is a null result and must stay one: it neither establishes that compensation is absent nor rescues the single-organism mechanism as a general rule.

## Possible Reconciliations

- *Hypothesis:* the relevant variable is the temporal or pathway distribution of NADH production rather than its per-carbon total, so a stoichiometric summary and an FBA optimum can both be correct about yield while mispredicting dependence [src: respiratory_chain_wiring].
- *Hypothesis:* the measured wiring is species-specific, and a cross-species test is therefore underpowered to detect it rather than evidence against it [src: respiratory_chain_wiring].
- *Hypothesis:* FBA's zero-flux prediction reflects the ATP-yield objective alone; under a different objective NDH-2 would carry flux, making model and measurement compatible without either changing [src: respiratory_chain_wiring].

## Resolving Work

- Measure NDH-2 and Complex I flux directly on quinate versus glucose and compare against the zero-NDH-2 FBA prediction: does the model fail on flux, or only on essentiality? [src: respiratory_chain_wiring]
- Re-run FBA with non-ATP-maximizing objectives (e.g. redox-balance or rate constraints) and ask which objective, if any, recovers the measured quinate requirement [src: respiratory_chain_wiring].
- Time-resolve NADH pool dynamics on both substrates to test whether distribution rather than the 0.57 versus 1.50 per-carbon totals tracks Complex I dependence [src: respiratory_chain_wiring].
- Expand the cross-species fitness panel and report power alongside the p=0.52 null, so absence of a compensatory pattern can be distinguished from inability to detect one [src: discoveries].
- Perturb Complex I on quinate in a second organism carrying validated NDH-2 to test the species-specificity hypothesis directly [src: respiratory_chain_wiring].
