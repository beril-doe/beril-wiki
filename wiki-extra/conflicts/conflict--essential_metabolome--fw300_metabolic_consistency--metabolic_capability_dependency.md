<!-- tension-hash: e14ae831d270e00d -->
# Matched Fitness Concordance vs. Broader Metabolic Capability

The disagreement concerns whether metabolic-pathway capability should be treated as concordant with measured fitness. A selected matched subset reports complete agreement between Fitness Browser and GapMind comparisons, while broader analyses identify complete pathways that are latent or intermediate under measured fitness criteria. Related tensions arise from rich-media assays, incomplete organism-action data, and inconsistent strain-level evidence. The distinction matters because apparent disagreement may reflect different scopes and definitions rather than incompatible biological results. See [[concepts/cross-condition-metabolic-comparability]].

## Evidence Sides

**Matched comparisons support metabolic–fitness concordance**

The FW300-N2E3 matched subset shows **100% concordance** for **21 Fitness Browser** and **13 GapMind comparisons**. This result applies to a selected matched subset of organisms, pathways, and conditions. [src: fw300_metabolic_consistency]

The Web of Microbes evidence also provides a production-to-Fitness Browser bridge for **19 metabolites**, connecting metabolite production evidence to fitness comparisons. [src: webofmicrobes_explorer]

**Broader capability analyses identify latent or condition-dependent metabolism**

The broader metabolic-capability analysis finds complete pathways that are latent or intermediate under measured fitness criteria. The newer analysis reports **57 (35.4%) Active Dependencies** and **66 (41.0%) Latent Capabilities**. [src: metabolic_capability_dependency] [src: pathway_capability_dependency]

The essential-metabolome pilot found **17 of 18 amino-acid pathways complete in all 7 mapped organisms**, but used rich-media RB-TnSeq and computational GapMind calls that cannot determine whether pathways are required under defined conditions. [src: essential_metabolome]

The Web of Microbes **2018 snapshot** has no organism consumption action, whereas other comparisons include utilization or single-substrate growth evidence. [src: webofmicrobes_explorer]

Strain-level evidence is also unresolved: the absorbed FW300 report gives trehalose as **1 of 6 BacDive strains positive**, while the main comparison reports **1+/5-**. Both values are retained because the source materials do not reconcile them. [src: fw300_metabolic_consistency] [src: fw300_metabolic_consistency]

## Possible Reconciliations

- **Hypothesis — matched-scope effect:** The 100% result may describe only the selected matched subset, whereas the broader classifications span organisms and conditions with less direct alignment.
- **Hypothesis — requirement versus capability:** A complete pathway may indicate latent capability without demonstrating that the pathway is required under the measured medium or fitness assay.
- **Hypothesis — assay and evidence granularity:** Rich-media RB-TnSeq, GapMind calls, production data, utilization data, and single-substrate growth tests may measure different parts of the capability-to-fitness relationship.
- **Hypothesis — strain and identifier differences:** The trehalose discrepancy may result from different strain sets, mappings, or compound curation.

## Resolving Work

- Repeat matched Fitness Browser–GapMind comparisons across more organisms, pathways, and explicitly aligned media to test whether 100% concordance persists beyond the selected subset.
- Measure direct metabolite consumption and single-substrate growth for the **19 metabolites** in the Web of Microbes bridge to determine whether production capability predicts organism-level utilization.
- Pair pathway-completeness calls with defined-condition essentiality assays to ask whether the **57 (35.4%) Active Dependencies** and **66 (41.0%) Latent Capabilities** separate reliably by condition.
- Re-map BacDive strains and trehalose identifiers using strain-level, identifier-based compound curation to determine whether **1 of 6** and **1+/5-** represent the same underlying observations.
