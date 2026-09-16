<!-- tension-hash: e14ae831d270e00d -->
# Does matched-assay concordance mean metabolic evidence agrees? Perfect cross-database agreement in a selected subset versus widespread latent capability

Every claim below comes from [[concepts/cross-condition-metabolic-comparability]] and the projects cited there. The corpus contains one headline result in which computational pathway predictions and experimental fitness data agree perfectly for a single organism, and a second set of results in which genomically complete pathways routinely fail to register as required under the conditions actually measured. Read carelessly, the first says metabolic databases are interchangeable and the second says they are not. The disagreement matters because it determines whether a "complete pathway" call, a production record, or a growth phenotype can be moved between projects as if it were the same kind of fact. This page covers four distinct disagreements in the input: (1) matched-subset concordance versus latent capability; (2) the assay-scope and coverage limits of the essential-metabolome pilot; (3) production-only versus utilization-bearing database scope; and (4) an unreconciled trehalose count.

## Evidence Sides

**Side A — matched comparisons agree completely (scope: one organism, selected metabolites).** In the FW300-N2E3 matched subset, concordance was 100% for 21 Fitness Browser comparisons and 13 GapMind comparisons. [src: fw300_metabolic_consistency] Fitness Browser here is the mutant-fitness database built from RB-TnSeq (random barcode transposon sequencing, a pooled mutant assay that scores each gene's contribution to growth in a given condition); GapMind is a computational predictor that scores whether a genome encodes a complete biosynthesis or catabolism pathway. Within this subset the two lines of evidence never disagreed.

**Side B — complete pathways are often latent or intermediate.** The broader metabolic-capability analysis finds complete pathways that are latent or intermediate under measured fitness criteria. [src: metabolic_capability_dependency] The newer analysis puts numbers on the split: 57 (35.4%) Active Dependencies and 66 (41.0%) Latent Capabilities. [src: pathway_capability_dependency] Both statements are scoped to what registered as required under the fitness criteria measured, not to an absolute absence of requirement. [src: metabolic_capability_dependency] [src: pathway_capability_dependency]

**Side C — the essential-metabolome pilot: high completeness, no requirement test.** The pilot found 17 of 18 amino-acid pathways complete in all 7 mapped organisms, but used rich-media RB-TnSeq and computational GapMind calls that cannot determine whether pathways are required under defined conditions. [src: essential_metabolome] The concept page frames this as an assay-scope and coverage tension rather than a contradiction of Sides A and B. [src: essential_metabolome]

**Side D — production evidence without consumption evidence.** The Web of Microbes evidence provides a production-to-Fitness Browser bridge for 19 metabolites, but its 2018 snapshot has no organism consumption action, whereas other comparisons include utilization or single-substrate growth evidence. [src: webofmicrobes_explorer]

**Side E — two trehalose counts, unreconciled.** The absorbed FW300 report gives trehalose as 1 of 6 BacDive strains positive, while the main comparison reports 1+/5-; both values are retained because the source materials do not reconcile them. [src: fw300_metabolic_consistency] [src: fw300_metabolic_consistency]

## Possible Reconciliations

These are hypotheses, not findings.

- **Scope, not contradiction (A vs B).** The concept page already reads the A/B gap this way: this is a scope difference rather than a numerical contradiction: one is a selected matched subset, while the other classifies complete pathway–organism pairs across organisms and conditions. [src: fw300_metabolic_consistency] [src: metabolic_capability_dependency] Hypothesis: the 21 Fitness Browser and 13 GapMind comparisons were selected precisely because a matching condition existed, which enriches for pathways that are active dependencies rather than latent capabilities.
- **Denominator selection.** Hypothesis: the matched subset's 100% figure is conditioned on metabolites that appear in more than one database at all; the 35.4%/41.0% split is computed over all classified organism–pathway pairs, so the two denominators are not comparable populations. [src: fw300_metabolic_consistency] [src: pathway_capability_dependency]
- **Assay can't fail (A/C).** Hypothesis: rich-media RB-TnSeq relieves biosynthetic demand, so a complete pathway has no opportunity to show a fitness requirement; agreement between GapMind completeness and such an assay would then be close to guaranteed and would carry little discriminating power. On this hypothesis the pilot's apparent agreement with Side A would be an artifact of what the assay could not measure rather than independent support for it — a reading the input does not assert, since it frames the pilot as adding an assay-scope and coverage tension rather than contradicting the other results. [src: essential_metabolome]
- **Measured capability differs (D).** Hypothesis: production and utilization are different biological actions, so a production-only snapshot cannot agree or disagree with a utilization record — the comparison is undefined rather than concordant or discordant. [src: webofmicrobes_explorer]
- **Formatting versus counting (E).** Hypothesis: the two trehalose renderings differ in whether the denominator counts strains tested or strains scored negative; because the source materials do not reconcile them, this remains a hypothesis and neither value should be preferred. [src: fw300_metabolic_consistency]

## Resolving Work

**A vs B — matched concordance versus latent capability**
- Recompute the matched-subset concordance rate after restricting the 57/66 Active Dependency and Latent Capability classification to the same organism and pathway set used for the 21 Fitness Browser and 13 GapMind comparisons; question: does 100% survive on the shared denominator? [src: fw300_metabolic_consistency] [src: pathway_capability_dependency]
- Repeat matched comparisons across more organisms, pathways, and explicitly aligned media, as the concept page's resolving work specifies, and report concordance stratified by whether a matching condition existed a priori. [src: fw300_metabolic_consistency] [src: metabolic_capability_dependency]
- Classify each of the 21 Fitness Browser and 13 GapMind matched comparisons into the Active Dependency / Latent Capability scheme and ask whether matched-subset membership predicts Active Dependency status. [src: fw300_metabolic_consistency] [src: pathway_capability_dependency]

**C — essential-metabolome assay scope and coverage**
- Re-run the 7-organism, 18-pathway panel under defined minimal media rather than rich media, and ask how many of the 17 complete amino-acid pathways become fitness-required. [src: essential_metabolome]
- Report, for each of the 7 mapped organisms, which pathway calls rest on computational GapMind evidence only versus experimental fitness evidence, so completeness conservation is not read as requirement conservation. [src: essential_metabolome]
- Address the coverage limit directly: extend the panel beyond the 7 mapped organisms and ask whether "17 of 18 pathways complete in all organisms" holds outside the set that happened to map, or is a property of those 7. [src: essential_metabolome]
- Place the 18 amino-acid pathways into the Active Dependency / Latent Capability classification so the pilot's completeness calls can be compared on the same scheme as the 57/66 split rather than on completeness alone. [src: essential_metabolome] [src: pathway_capability_dependency]

**D — production-only database scope**
- Extend the 19-metabolite production-to-Fitness Browser bridge with direct consumption measurements, so each metabolite carries both a production and a utilization action. [src: webofmicrobes_explorer] [src: fw300_metabolic_consistency]
- Refresh the 2018 snapshot and check whether organism consumption actions are recorded in later releases before treating absent consumption as negative consumption. [src: webofmicrobes_explorer]
- Add strain-level mapping and identifier-based compound curation so production and utilization records refer to the same strain and the same chemical entity. [src: fw300_metabolic_consistency]

**E — the trehalose count**
- Retrieve the underlying per-strain BacDive records behind both the "1 of 6 strains positive" and the "1+/5-" renderings and report the strain list, so the counts are reconciled by data rather than by preference. [src: fw300_metabolic_consistency]
- Apply strain-level mapping and identifier-based compound curation to the trehalose record specifically, checking that both renderings refer to the same strains and the same compound identifier before either is treated as the corrected count. [src: fw300_metabolic_consistency]
- Until then, carry both values explicitly wherever the trehalose result is cited, since the source materials do not reconcile them. [src: fw300_metabolic_consistency]
