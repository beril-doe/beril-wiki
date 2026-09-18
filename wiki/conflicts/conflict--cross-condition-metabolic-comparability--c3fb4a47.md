<!-- tension-hash: c3fb4a474d9b3571 -->
# Complete pathways in agreement: perfect concordance in a matched subset versus widespread latency in a pathway census

Three projects in this corpus bear on the same question — whether a genomically complete pathway can be treated as evidence that the organism actually uses it — and their results read in opposite directions. One finds unbroken agreement between pathway prediction, mutant fitness and measured metabolite production within a curated matched subset for a single strain, with 100% concordance for 21 Fitness Browser and 13 GapMind comparisons [src: fw300_metabolic_consistency]. A separate, broader metabolic-capability analysis that classifies complete pathway–organism pairs across organisms and conditions finds complete pathways that are latent or intermediate under measured fitness criteria [src: metabolic_capability_dependency]; a further analysis refines that distinction into 57 (35.4%) Active Dependencies and 66 (41.0%) Latent Capabilities [src: pathway_capability_dependency]. Which reading holds determines whether pathway completeness can serve as a standalone proxy for metabolic activity in downstream cross-database work — the question that [[concepts/cross-condition-metabolic-comparability]] turns on.

## Evidence Sides

**Matched subset: prediction, fitness and production agree completely.** For *Pseudomonas* FW300-N2E3, the matched subset shows 100% concordance for 21 Fitness Browser comparisons — Fitness Browser being the repository of RB-TnSeq (random barcode transposon sequencing) mutant-fitness measurements — and 13 GapMind comparisons, GapMind being the tool that scores pathway completeness from genome annotation [src: fw300_metabolic_consistency]. The denominator here is a selected matched subset for one strain, and the result is a complete-agreement count, not an estimated rate.

**Pathway census: complete does not mean depended-upon.** The broader metabolic-capability analysis finds complete pathways that are latent or intermediate under measured fitness criteria [src: metabolic_capability_dependency]. The refinement of that classification reports 57 (35.4%) Active Dependencies and 66 (41.0%) Latent Capabilities [src: pathway_capability_dependency]. The unit of analysis is the complete pathway–organism pair, counted across organisms and conditions, and the classification turns on a fitness threshold rather than on pairwise database agreement.

## Possible Reconciliations

- *Hypothesis: the disagreement is one of scope, not of number.* The tension text itself frames it this way — one analysis is a selected matched subset, the other classifies complete pathway–organism pairs across organisms and conditions — so the two results could both stand without either being wrong [src: fw300_metabolic_consistency, metabolic_capability_dependency].
- *Hypothesis: subset selection filters for the concordant cases.* If metabolites are entered into the matched subset because independent evidence already exists for them, the subset may be enriched for Active Dependencies and depleted of Latent Capabilities by construction.
- *Hypothesis: the criteria differ, not the biology.* Concordance is a pairwise agreement judgement; latency is a threshold call on fitness magnitude, so the same pathway could be concordant and latent simultaneously.

## Resolving Work

- Re-run the matched-subset comparison for FW300-N2E3 through the Active Dependency / Latent Capability classifier: do its 21 Fitness Browser and 13 GapMind comparisons fall into the Active class, or do concordant pairs also appear as Latent?
- Apply the matched-subset construction rule to every organism in the pathway census and report how many complete pathway–organism pairs it admits — measuring the selection filter directly.
- Report the Latent Capability fraction separately for pairs with and without exometabolomic evidence — exometabolomics being the measurement of extracellular metabolite emergence or increase — testing whether production evidence predicts dependency class.
- Vary the fitness threshold used to call latency and report the Active/Latent split as a function of it, so the 35.4%/41.0% split can be read as threshold-conditional rather than fixed.
- Stratify both analyses by condition type to test whether concordance in the matched subset depends on the growth conditions actually assayed.
