<!-- tension-hash: e62728ec46873dcf -->
# NDH-2 Compensation Versus Weak Cross-Species Support

The disagreement concerns whether NDH-2 can explain reduced Complex I dependence on particular substrates. The aromatic-catabolism analysis treats NDH-2 compensation as a substrate- and architecture-based hypothesis, while the cross-species respiratory-chain comparison found no supporting compensation pattern and therefore weakens any generalization across species. The metabolic-capability result adds a related caution: pathway conservation may not predict active fitness dependence, making recipient-specific network and condition measurements important.

## Evidence Sides

**NDH-2 compensation as a substrate- and architecture-based explanation**

The analysis in aromatic_catabolism_network proposes that NDH-2 compensation can explain lower Complex I dependence on some substrates. This claim is explicitly framed as a substrate- and architecture-based hypothesis rather than a demonstrated universal relationship. [src: aromatic_catabolism_network]

**Cross-species comparison does not support a general compensation pattern**

Among organisms retained after filtering, validated NDH-2 organisms had a larger mean Complex I aromatic deficit (-0.297 versus -0.156), with p = 0.52. The comparison included only 4 organisms lacking NDH-2 and may therefore be underpowered; the two results should not be reconciled as a universal rule. [src: respiratory_chain_wiring] The comparison therefore weakens generalization of the compensation hypothesis across species. [src: respiratory_chain_wiring]

The related analysis in metabolic_capability_dependency found that pathway-level conservation did not distinguish latent capabilities from active dependencies, with mean conservation of 0.869 for 248 latent capabilities versus 0.829 for 755 active dependencies and Mann–Whitney U p = 0.94 for active > latent. [src: metabolic_capability_dependency] Thus, conserved pathway presence alone does not establish conserved fitness dependence, supporting the caution that ortholog transfer cannot substitute for recipient-specific network and condition measurements. [src: metabolic_capability_dependency]

## Possible Reconciliations

- **Hypothesis — substrate-specific scope:** NDH-2 compensation may operate for particular substrates or network architectures, while the cross-species comparison averages across organisms and conditions that do not expose the relevant mechanism.
- **Hypothesis — statistical power:** The comparison’s 4 organisms lacking NDH-2 may be insufficient to detect a real difference, so p = 0.52 may reflect uncertainty rather than evidence that compensation never occurs.
- **Hypothesis — phenotype definition:** “Lower Complex I dependence,” aromatic deficit, latent pathway capability, and active fitness dependence may measure different biological properties; pathway conservation could therefore coexist with divergent condition-specific dependencies.
- **Hypothesis — recipient-specific wiring:** NDH-2 presence may be necessary but not sufficient for compensation, with expression, flux routing, substrate availability, or other respiratory-chain architecture determining whether it affects fitness.

## Resolving Work

- Measure Complex I and NDH-2 dependence across matched organisms, substrates, and environmental conditions using perturbations and fitness assays; ask whether NDH-2 reduces Complex I dependence only in defined contexts.
- Expand the comparison beyond the 4 organisms lacking NDH-2 and estimate uncertainty around the mean aromatic deficits; ask whether the -0.297 versus -0.156 difference is reproducible with adequate power.
- Quantify NDH-2 expression, enzymatic activity, respiratory flux, and pathway routing during the relevant substrate conditions; ask whether genomic presence predicts functional compensation.
- Separate latent capability from active dependency with condition-specific knockouts or inhibition across the 248 latent capabilities and 755 active dependencies; ask whether conservation tracks measured fitness effects.
- Test recipient-specific network models against experimental fitness data; ask whether architecture and condition variables explain when ortholog transfer succeeds or fails.
