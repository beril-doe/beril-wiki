<!-- tension-hash: e62728ec46873dcf -->
# NDH-2 Compensation vs Cross-Species Generalization

The disagreement concerns whether NDH-2 compensation explains reduced Complex I dependence on particular substrates, and whether that substrate- and architecture-based mechanism generalizes across species. [[concepts/aromatic-catabolism-network]] proposes a mechanistic explanation, while [[concepts/respiratory-chain-wiring]] reports no supporting cross-species pattern. [[concepts/cross-species-fitness-transferability]] frames the stakes: conserved pathway presence and orthology may not reliably predict recipient-specific fitness dependence under particular conditions.

## Evidence Sides

**NDH-2 compensation as a substrate- and architecture-based mechanism**

The aromatic-catabolism analysis proposes that NDH-2 compensation can explain lower Complex I dependence on some substrates. This remains a substrate- and architecture-based hypothesis rather than a demonstrated universal rule. [src: aromatic_catabolism_network]

**Cross-species comparison weakens the generalization**

The cross-species respiratory-chain comparison found no supporting compensation pattern: among organisms retained after filtering, validated NDH-2 organisms had a larger mean Complex I aromatic deficit (-0.297 versus -0.156), with p = 0.52. [src: respiratory_chain_wiring] The comparison included only 4 organisms lacking NDH-2 and may therefore be underpowered; the two results should not be reconciled as a universal rule. [src: respiratory_chain_wiring] The metabolic capability analysis adds a related limitation: pathway-level conservation did not distinguish latent capabilities from active dependencies, with mean conservation of 0.869 for 248 latent capabilities versus 0.829 for 755 active dependencies and Mann–Whitney U p = 0.94 for active > latent. [src: metabolic_capability_dependency] Thus, conserved pathway presence alone does not establish conserved fitness dependence, supporting the caution that ortholog transfer cannot substitute for recipient-specific network and condition measurements. [src: metabolic_capability_dependency]

## Possible Reconciliations

- **Hypothesis — substrate-specific scope:** NDH-2 compensation may operate only for particular aromatic substrates or respiratory architectures, so a pooled cross-species comparison could obscure a conditional effect.
- **Hypothesis — statistical power:** The cross-species result may be inconclusive because the comparison included only 4 organisms lacking NDH-2; p = 0.52 may reflect limited power rather than evidence against compensation.
- **Hypothesis — capability versus dependence:** NDH-2 presence and pathway conservation may indicate latent capability without indicating that the pathway is active or fitness-critical in the tested condition.
- **Hypothesis — measurement alignment:** “Complex I aromatic deficit” may not measure the same substrate-level compensation mechanism proposed by the aromatic-catabolism analysis.

## Resolving Work

- Assemble a larger, phylogenetically balanced panel of organisms with and without validated NDH-2, then test whether the Complex I aromatic deficit differs by NDH-2 status and by substrate.
- Measure growth or fitness after targeted NDH-2 and Complex I perturbations across the relevant aromatic substrates, asking whether NDH-2 loss specifically increases Complex I dependence.
- Separate latent pathway presence from active flux using transcript, protein, metabolite, and flux measurements under matched conditions, asking whether conserved capabilities become conserved dependencies.
- Stratify the cross-species analysis by respiratory architecture and substrate rather than pooling organisms, testing whether compensation appears only in the proposed mechanistic subset.
