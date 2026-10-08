<!-- tension-hash: e6421a5b76b98540 -->
# Does Pathway Completeness and Metabolite Production Evidence Speak to Condition-Specific Metabolic Requirement or Use?

The [[concepts/cross-condition-metabolic-comparability]] page treats metabolic evidence as condition-dependent. Two projects add a scope and coverage tension to that framing rather than a direct contradiction. The amino-acid pathway pilot reports highly conserved pathway completeness, 17 of 18 pathways complete in all 7 mapped organisms, but its assays cannot determine whether those pathways are required under defined conditions [src: essential_metabolome]. The Web of Microbes (WoM, an exometabolomics database of metabolites organisms release) bridge links production to the Fitness Browser for 19 metabolites, but its 2018 snapshot records no organism consumption [src: webofmicrobes_explorer]. This matters because other comparisons in the corpus rest on utilization or single-substrate growth evidence [src: webofmicrobes_explorer]. Pooling capability-only or production-only evidence with use-based evidence risks treating unlike measurements as equivalent.

## Evidence Sides

**Side A: Capability and production evidence shows broad, linkable metabolic coverage**

- The essential-metabolome pilot found 17 of 18 amino-acid pathways complete in all 7 mapped organisms [src: essential_metabolome].
- The Web of Microbes evidence provides a production-to-Fitness Browser (a mutant-fitness experiment collection) bridge for 19 metabolites [src: webofmicrobes_explorer].

**Side B: These evidence types cannot establish condition-specific requirement or substrate use**

- The pilot used rich-media RB-TnSeq (random barcode transposon sequencing, a pooled mutant-fitness assay). It also used computational GapMind calls, which are pathway-completeness predictions from genome annotation. Neither can determine whether pathways are required under defined conditions [src: essential_metabolome].
- The 2018 WoM snapshot has no organism consumption action [src: webofmicrobes_explorer].
- By contrast, other comparisons include utilization or single-substrate growth evidence [src: webofmicrobes_explorer].

Neither side refutes the other. Side A's pathway completeness comes from computational GapMind calls, not direct measurement of requirement [src: essential_metabolome], and its bridge rests on production records [src: webofmicrobes_explorer]. Side B notes that these cannot determine requirement under defined conditions [src: essential_metabolome] or record organism consumption [src: webofmicrobes_explorer].

## Possible Reconciliations

- **Hypothesis 1:** Conserved pathway completeness reflects latent capability, not active dependency. Under this hypothesis, requirement would appear only under defined, nutrient-limited conditions that rich-media RB-TnSeq does not sample.
- **Hypothesis 2:** Production and consumption are separable axes. Under this hypothesis, the production bridge for 19 metabolites [src: webofmicrobes_explorer] and the utilization-based comparisons measure different capabilities and need not agree.
- **Hypothesis 3:** The 2018 snapshot has no organism consumption action [src: webofmicrobes_explorer]; the hypothesis is that this gap belongs to the snapshot rather than to exometabolomics as a method. Under this hypothesis, a dataset that records uptake could connect WoM-style evidence to the utilization-based comparisons.

## Resolving Work

- **Requirement under defined media:** Compare defined-medium RB-TnSeq fitness profiles with GapMind pathway completeness for the 7 mapped organisms, where 17 of 18 amino-acid pathways were complete in all [src: essential_metabolome]. The question is whether those complete pathways become required when the corresponding amino acid is absent.
- **Consumption data for the bridge:** Obtain an exometabolomics release that records consumption and remap it to Fitness Browser experiments. The question is whether consumed metabolites, not just produced ones, align with fitness phenotypes for the 19 bridged metabolites [src: webofmicrobes_explorer].
- **Single-substrate growth checks:** Run single-substrate growth assays on WoM-produced metabolites in the same organisms. The question is whether production predicts, contradicts, or is independent of the ability to use a metabolite.
- **Assay-scope labelling:** Tag each comparison on the concept page by evidence type: computational completeness, rich-media fitness, production, or utilization. The question is whether apparent agreement or disagreement tracks evidence type rather than biology.
