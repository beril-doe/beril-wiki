<!-- tension-hash: 10ef6928e49ddfba -->
# Is Complex I Dispensable or Growth-Relevant in ADP1?

The disagreement concerns whether Complex I can be treated as dispensable during growth on glucose and lactate because NDH-2 compensates for its loss, or whether Complex I makes a measurable contribution under ADP1-specific conditions. The distinction matters because the two interpretations imply different respiratory architectures and different expectations for how NADH reoxidation supports growth. As summarized on [[concepts/respiratory-capacity-and-nadh-load]], the conflict may arise from fitness metrics, model assumptions, or species-level differences rather than from a direct contradiction.

## Evidence Sides

**Earlier transferred-fitness interpretation — Complex I is dispensable and NDH-2 compensates.**  
The earlier transferred-fitness interpretation reports Complex I as dispensable on glucose and lactate and treats this as consistent with NDH-2 compensation. [src: aromatic_catabolism_network]

**New ADP1-specific analysis — Complex I contributes to growth, without predicted NDH-2 compensation.**  
The new ADP1-specific analysis reports a Complex I growth ratio of 1.44 on glucose, predicts zero NDH-2 flux under standard FBA conditions, and finds no significant cross-species compensation pattern (p = 0.52). [src: respiratory_chain_wiring]

These results do not establish that the earlier interpretation is false. [src: respiratory_chain_wiring]

## Possible Reconciliations

- **Hypothesis — fitness-metric difference:** “Dispensable” may describe a thresholded or transferred-fitness result, whereas a growth ratio of 1.44 may quantify a more specific ADP1 growth effect. The analyses could therefore measure different consequences of Complex I loss.
- **Hypothesis — model-assumption difference:** The prediction of zero NDH-2 flux under standard FBA conditions may depend on the permitted reactions, objective function, medium, or flux constraints. Alternative assumptions could allow NDH-2 compensation without making it necessary in the standard model.
- **Hypothesis — species-level respiratory architecture:** The earlier result and the ADP1-specific result may apply to organisms with different respiratory wiring. A compensation pattern observed across transferred systems need not hold in ADP1.
- **Hypothesis — carbon-source or experimental-context difference:** Results described for glucose and lactate may not be directly comparable if the assays or simulations impose different carbon-source conditions, respiratory demands, or growth environments.

## Resolving Work

- Perform matched ADP1 Complex I deletion assays on glucose and lactate, using the same strain background, media, growth conditions, and fitness metric; test whether Complex I loss is experimentally dispensable or produces the reported growth effect.
- Measure NADH/NAD⁺ directly across the same carbon sources in wild type and Complex I-deficient ADP1; determine whether loss of Complex I produces a redox imbalance and whether NDH-2 activity changes.
- Re-run the relevant FBA models with harmonized reaction inventories, objective functions, exchange constraints, and carbon-source definitions; ask whether the prediction of zero NDH-2 flux and the growth ratio of 1.44 persist under matched assumptions.
- Compare respiratory-chain architectures across the species underlying the transferred-fitness interpretation and ADP1; test whether the presence or use of alternative NADH dehydrogenases predicts the observed compensation pattern.
