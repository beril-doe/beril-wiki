---
title: Matched metabolic concordance versus broader pathway capability
type: Conflict
sources:
- id: fw300_metabolic_consistency
  resource: ../../wiki/summaries/fw300_metabolic_consistency__REPORT.md
  title: fw300 metabolic consistency
- id: metabolic_capability_dependency
  resource: ../../wiki/summaries/metabolic_capability_dependency__REPORT.md
  title: metabolic capability dependency
- id: pathway_capability_dependency
  resource: ../../wiki/summaries/pathway_capability_dependency__REPORT.md
  title: pathway capability dependency
- id: essential_metabolome
  resource: ../../wiki/summaries/essential_metabolome__REPORT.md
  title: essential metabolome
- id: webofmicrobes_explorer
  resource: ../../wiki/summaries/webofmicrobes_explorer__REPORT.md
  title: webofmicrobes explorer
---
<!-- tension-hash: 7648271f986a714b -->
# Matched metabolic concordance versus broader pathway capability

The disagreement concerns what metabolic concordance means when comparisons are restricted to matched organisms, pathways, and conditions versus when pathway capability is assessed across broader organism–condition spaces. The [cross-condition-metabolic-comparability](../../wiki/concepts/cross-condition-metabolic-comparability.md) evidence supports strong agreement in a selected subset, while other analyses identify complete pathways that are latent or intermediate under measured fitness criteria. Related tensions arise from assay scope, organism coverage, metabolite-consumption evidence, and an unresolved trehalose count.

## Evidence Sides

**Selected matched comparisons show complete concordance.** The FW300-N2E3 matched subset shows 100% concordance for 21 Fitness Browser and 13 GapMind comparisons. [^fw300_metabolic_consistency] This comparison is explicitly described as a selected matched subset rather than a census of pathway capability.

**Broader pathway analyses distinguish capability from measured fitness.** The broader metabolic-capability analysis finds complete pathways that are latent or intermediate under measured fitness criteria. [^metabolic_capability_dependency] The new analysis further reports 57 (35.4%) Active Dependencies and 66 (41.0%) Latent Capabilities. [^pathway_capability_dependency] These results classify complete pathway-organism pairs across organisms and conditions rather than only the matched subset.

**Assay and coverage evidence supports different levels of metabolic interpretation.** The essential-metabolome pilot found 17 of 18 amino-acid pathways complete in all 7 mapped organisms, but used rich-media RB-TnSeq and computational GapMind calls that cannot determine whether pathways are required under defined conditions. [^essential_metabolome] The Web of Microbes evidence provides a production-to-Fitness Browser bridge for 19 metabolites, but its 2018 snapshot has no organism consumption action, whereas other comparisons include utilization or single-substrate growth evidence. [^webofmicrobes_explorer]

**The trehalose result remains numerically unreconciled.** The absorbed FW300 report gives trehalose as 1 of 6 BacDive strains positive, while the main comparison reports 1+/5-. Both values are retained because the source materials do not reconcile them. [^fw300_metabolic_consistency] [^fw300_metabolic_consistency]

## Possible Reconciliations

- **Hypothesis — scope difference:** 100% concordance may hold for the selected FW300-N2E3 matched comparisons while broader analyses legitimately classify additional complete pathways as latent or intermediate across organisms and conditions.
- **Hypothesis — requirement versus capability:** Rich-media growth and GapMind completeness may indicate biochemical capacity without establishing requirement under defined media or measured fitness conditions.
- **Hypothesis — evidence-type difference:** Production, utilization, single-substrate growth, and organism-consumption actions may measure different links in the metabolic chain.
- **Hypothesis — strain or curation difference:** The trehalose discrepancy may result from different BacDive strain sets, identifier mappings, or inclusion rules.

## Resolving Work

- Repeat matched comparisons across more organisms, pathways, and explicitly aligned media; test whether concordance remains 100% outside the original subset.
- Pair pathway-completeness calls with defined-condition RB-TnSeq or growth assays; ask which complete pathways are required, dispensable, or latent in each condition.
- Add direct metabolite-consumption measurements and compare them with production and Fitness Browser evidence; determine whether the 19-metabolite bridge predicts utilization.
- Audit strain-level mappings and identifier-based compound curation for trehalose; determine whether the 1 of 6 and 1+/5- values refer to different populations or scoring rules.

[^fw300_metabolic_consistency]: [fw300 metabolic consistency](../../wiki/summaries/fw300_metabolic_consistency__REPORT.md)
[^metabolic_capability_dependency]: [metabolic capability dependency](../../wiki/summaries/metabolic_capability_dependency__REPORT.md)
[^pathway_capability_dependency]: [pathway capability dependency](../../wiki/summaries/pathway_capability_dependency__REPORT.md)
[^essential_metabolome]: [essential metabolome](../../wiki/summaries/essential_metabolome__REPORT.md)
[^webofmicrobes_explorer]: [webofmicrobes explorer](../../wiki/summaries/webofmicrobes_explorer__REPORT.md)
