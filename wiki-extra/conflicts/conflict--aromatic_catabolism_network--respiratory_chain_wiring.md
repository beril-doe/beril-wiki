<!-- tension-hash: 10ef6928e49ddfba -->
# Complex I Dispensability Versus ADP1 Growth Dependence

The tension concerns whether Complex I is functionally dispensable under the tested conditions because NDH-2 can compensate, or whether ADP1-specific modeling instead indicates a substantial Complex I contribution to growth. The disagreement matters because it changes how respiratory-chain redundancy, NADH handling, and transferred fitness effects should be interpreted across carbon sources and species. The conflict is documented on [[concepts/respiratory-capacity-and-nadh-load]].

## Evidence Sides

**Earlier transferred-fitness interpretation**

The earlier transferred-fitness interpretation reports Complex I as dispensable on glucose and lactate and treats this as consistent with NDH-2 compensation. [src: aromatic_catabolism_network]

**New ADP1-specific analysis**

The new ADP1-specific analysis reports a Complex I growth ratio of 1.44 on glucose, predicts zero NDH-2 flux under standard FBA conditions, and finds no significant cross-species compensation pattern (p = 0.52). [src: respiratory_chain_wiring]

## Possible Reconciliations

- **Hypothesis — fitness-metric difference:** “Dispensable” may describe an earlier transferred-fitness metric, whereas a growth ratio of 1.44 may reflect a different quantitative definition of growth impact. The two results could therefore measure related but non-identical phenotypes.
- **Hypothesis — model-assumption difference:** The prediction of zero NDH-2 flux under standard FBA conditions may depend on how reactions, objectives, nutrient constraints, or alternative respiratory routes are represented. The earlier interpretation may have used assumptions that permit or imply NDH-2 compensation.
- **Hypothesis — species-level respiratory architecture:** The earlier result and the ADP1-specific result may concern respiratory systems whose wiring differs across species. Compensation observed or inferred in one species need not produce the same pattern in ADP1.
- **Hypothesis — condition-specific compensation:** Compensation may vary between glucose and lactate, or between modeled and experimentally imposed respiratory states. A single standard-FBA prediction may not capture condition-dependent NADH oxidation.

## Resolving Work

- Perform matched Complex I deletion assays in ADP1 on glucose and lactate, using the same growth-fitness metric for both conditions; test whether Complex I loss is dispensable or produces the reported growth effect.
- Measure NADH/NAD⁺ ratios directly in wild type and Complex I-deficient ADP1 across glucose and lactate; determine whether NDH-2-associated compensation corresponds to altered redox balance.
- Re-run both analytical frameworks with harmonized reaction inventories, objective functions, medium constraints, and species-specific respiratory architectures; test whether the Complex I growth ratio of 1.44 and zero NDH-2 flux persist.
- Quantify NDH-2 flux experimentally, using isotope-resolved or fluxomic measurements under the same conditions as the deletion assays; test whether the modeled zero flux reflects biology or model constraints.
- Compare compensation patterns across the relevant species with a common deletion and redox-measurement protocol; test whether the reported p = 0.52 reflects genuine absence of cross-species compensation or insufficiently matched data.
