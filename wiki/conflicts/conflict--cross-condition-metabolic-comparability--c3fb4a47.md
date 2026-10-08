<!-- tension-hash: c3fb4a474d9b3571 -->
# Does genomic pathway completeness agree with measured fitness, or do complete pathways often stay latent?

The [[concepts/cross-condition-metabolic-comparability]] page records two results that point in different directions. A matched comparison for *Pseudomonas* FW300-N2E3 reports full concordance for its Fitness Browser and GapMind comparisons [src: fw300_metabolic_consistency]. Broader analyses report that many genomically complete pathways show no measured fitness dependence under the tested conditions [src: metabolic_capability_dependency] [src: pathway_capability_dependency]. This matters because it determines how far pathway-completeness predictions can be read as evidence of metabolic function. The TENSION text frames this as a scope difference rather than a numerical contradiction, and that framing is kept here without choosing a side.

## Evidence Sides

**Side 1: Matched-subset concordance**

In the FW300-N2E3 matched subset, concordance is 100% for 21 Fitness Browser comparisons and 13 GapMind comparisons [src: fw300_metabolic_consistency]. Here concordance means agreement between each database's evidence and the strain's metabolite production [src: fw300_metabolic_consistency]. GapMind is a pathway-completeness prediction tool, and the Fitness Browser holds RB-TnSeq (random barcode transposon sequencing) mutant-fitness data [src: pathway_capability_dependency]. The TENSION text describes this result as coming from a selected matched subset in one strain [src: fw300_metabolic_consistency]. It is therefore single-organism evidence.

**Side 2: Complete pathways that are latent or intermediate**

The broader metabolic-capability analysis classifies complete pathway–organism pairs across organisms and conditions. It finds that some complete pathways are latent or intermediate under the measured fitness criteria [src: metabolic_capability_dependency]. A separate analysis **refines** this distinction. It reports 57 (35.4%) Active Dependencies, meaning complete pathways with fitness-important genes, and 66 (41.0%) Latent Capabilities, meaning complete pathways without significant fitness defects under the tested standard conditions [src: pathway_capability_dependency]. On this side, genomic completeness does not by itself predict measured dependence under those conditions.

## Possible Reconciliations

- **Hypothesis: selection effect.** The matched subset may include only metabolites where every source already had evidence. That would favour concordance, while unselected pathway–organism pairs include pathways the tested conditions never exercise. This rests on the scope description in the TENSION text and has not been tested directly.
- **Hypothesis: different questions.** The FW300-N2E3 comparison asks whether evidence sources are consistent with metabolite production. The capability analyses ask whether a complete pathway is fitness-important. If so, the two results answer different questions and need not conflict.
- **Hypothesis: condition dependence.** "Latent" may reflect which conditions were measured rather than a fixed property of a pathway. On this view, the matched subset happened to fall within conditions where the relevant genes matter.

## Resolving Work

- **Expanded FW300-N2E3 matched comparison:** Extend the comparison of Fitness Browser and GapMind evidence against metabolite production to further FW300-N2E3 metabolites, then classify the corresponding complete pathways as active or latent. Question: does 100% concordance persist on an expanded set, and do concordant pathways fall in the active class?
- **Matched-subset metabolites in the capability analysis:** Check where the FW300-N2E3 matched metabolites fall in the multi-organism capability classification. Question: are they concentrated in the Active Dependency class?
- **Condition stratification:** Stratify Fitness Browser experiments by condition type and re-classify the Latent Capability pathways. Question: does latency disappear under specific stress or nutrient-limitation conditions?
- **Threshold sensitivity:** Re-run both analyses with harmonized fitness-importance thresholds. Question: is the apparent disagreement driven by differing criteria for "important"?
