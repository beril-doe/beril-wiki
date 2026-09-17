<!-- tension-hash: c50aa829e1d71f9c -->
# Cross-Organism Growth-Prediction Accuracy vs. ADP1 Gene-Level Concordance: Two Endpoints, Two Verdicts on Draft Models

Two projects in this corpus report opposite-feeling verdicts on whether flux balance analysis (FBA) — a constraint-based method that predicts feasible metabolic flux distributions from a genome-scale model — tracks experimental phenotype data. A cross-organism benchmark reports 42.5% baseline FBA accuracy driven by 330 false positives [src: annotation_gap_discovery], while an *Acinetobacter baylyi* ADP1 analysis reports that FBA often agrees with TnSeq (transposon-sequencing mutant fitness, used here to call gene essentiality), with 73.8% concordance [src: acinetobacter_adp1_explorer]. The disagreement matters because it decides whether a draft model is usable evidence on its own or only a hypothesis generator needing condition-specific validation — the core question of [[concepts/metabolic-model-gapfilling]]. Crucially, the two results are not measured against the same denominator or the same endpoint, so neither number licenses a general claim about the other's domain.

## Evidence Sides

**Cross-organism accuracy is poor and asymmetric.** Baseline FBA across many organism–carbon-source combinations yielded 42.5% overall accuracy, with 330 false positives, indicating overly permissive draft models that predict growth where none occurs [src: annotation_gap_discovery]. The endpoint here is growth/no-growth prediction per condition, and the failure mode is directional: predicting too much capability, not too little.

**Within ADP1, model and experiment largely agree.** ADP1-centered evidence finds that FBA often agrees with TnSeq, at 73.8% concordance [src: acinetobacter_adp1_explorer]. The endpoint here is gene-level essentiality agreement in a single, well-characterized organism, not condition-level growth prediction. The tension text is explicit that this 73.8% concordance does not erase the broader accuracy result [src: acinetobacter_adp1_explorer].

## Possible Reconciliations

- *Hypothesis (endpoint mismatch):* the two figures may measure different things — condition-level growth prediction versus gene-level essentiality concordance — so both could hold simultaneously without either being wrong.
- *Hypothesis (organism selection):* ADP1 may be better annotated and better curated than the average organism in the cross-organism panel, so its agreement rate may not generalize.
- *Hypothesis (media mapping):* differing carbon-source-to-exchange-reaction mappings may inflate false positives in the cross-organism setting while leaving ADP1's richer curation unaffected.

- *Hypothesis (protocol artifact):* the organisms, media mappings, and endpoints differ between the two analyses, so the gap may reflect protocol rather than model quality; harmonized simulations are required to tell these apart.

## Resolving Work

- Re-run both analyses under one harmonized simulation protocol — identical media definitions, identical exchange-reaction mappings, identical growth thresholds — and ask whether ADP1's concordance survives the cross-organism protocol.
- Compute the cross-organism benchmark's gene-level essentiality concordance, not only condition-level growth accuracy, to test whether the endpoint-mismatch hypothesis explains the gap.
- Include ADP1 as one organism inside the cross-organism panel and report its per-organism accuracy alongside the others, testing the organism-selection hypothesis directly.
- Perturb the carbon-source-to-compound mapping and report how much of the false-positive burden is mapping error versus genuine model permissiveness.
- Report both precision-style and recall-style breakdowns for each side separately, so asymmetric failure modes are visible rather than collapsed into one accuracy figure.
