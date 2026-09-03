<!-- tension-hash: b7accc771db7edad -->
# Shared-stress fitness: common signal or analysis-specific response?

The disagreement concerns whether shared-stress fitness patterns reflect a stable, broadly directional biological response or depend strongly on the stressor pair, record set, organism coverage, and correction procedure. The conflict is documented on [[concepts/shared-stress-versus-stressor-specific-fitness]] and has two related dimensions: different estimates of per-metal conservation after shared-stress treatment, and different interpretations of positive cross-metal correlations. Resolving it matters because a universal mechanism should remain evident under matched analyses, whereas analysis-specific signals would limit how broadly the results can be generalized.

## Evidence Sides

**Counter-ion analysis: manganese and iron are +0.182, while zinc is +0.115**  
After shared-stress treatment, the counter-ion analysis reports manganese at +0.182, zinc at +0.115, and iron at +0.182. [src: counter_ion_effects]

**Primary atlas: manganese is +0.198, zinc is +0.151, and iron is +0.116**  
The primary atlas reports manganese at +0.198, zinc at +0.151, and iron at +0.116. [src: metal_fitness_atlas]

**Metal cross-resistance study: all tested metal-pair correlations were positive**  
The metal cross-resistance study reports that all tested metal-pair correlations were positive and interprets this as a universal directional layer. [src: metal_cross_resistance]

**Counter-ion analysis: metal–NaCl correlations vary substantially across metals**  
The counter-ion analysis shows that metal–NaCl correlations vary substantially across metals, including iron r=0.086 and zinc r=0.715. [src: counter_ion_effects] It states that this is not a direct contradiction because the analyses compare different condition pairs, but refines the interpretation: positivity across metals does not establish a uniform response to NaCl or identify which shared stressor generates the signal. [src: metal_cross_resistance, counter_ion_effects]

## Possible Reconciliations

- **Hypothesis — record-set difference:** The per-metal estimate discrepancies may arise because the analyses use different record sets rather than because the underlying biology differs. The input explicitly states that the analyses differ in record sets, organism coverage, and correction procedure. [src: counter_ion_effects, metal_fitness_atlas]
- **Hypothesis — organism-coverage difference:** Different organism coverage could change the relative conservation estimates while preserving a shared-stress pattern within each analysis.
- **Hypothesis — correction-procedure difference:** The correction procedure may shift manganese, zinc, and iron estimates in different directions without implying biological disagreement.
- **Hypothesis — condition-pair difference:** Positive metal-pair correlations may represent a directional layer specific to metal-pair comparisons, while metal–NaCl correlations capture a different response structure.
- **Hypothesis — partially shared biology:** Both analyses may detect positive relationships, but the magnitude and uniformity of the response may depend on which stressor is paired with which metal.

## Resolving Work

- Re-run both conservation analyses on the same records, organisms, and metal conditions using each correction procedure; test whether the per-metal estimates converge.
- Perform a leave-one-organism and leave-one-record-set analysis; test whether manganese, zinc, and iron discrepancies are driven by coverage.
- Analyze metal-pair and metal–NaCl correlations in one matched dataset; test whether positivity persists across stressor-pair definitions.
- Use a common statistical model with interaction terms for metal and stressor pair; test whether a universal directional effect or metal-specific responses better explain the data.
