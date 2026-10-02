<!-- tension-hash: e6421a5b76b98540 -->
# Do capability-only and production-only datasets count as comparable metabolic evidence?

Two projects extend the corpus's cross-assay comparisons in [[concepts/cross-condition-metabolic-comparability]] with datasets that are broad on one axis and silent on another, and the disagreement is about scope rather than about any conflicting measurement. One reports 17 of 18 amino-acid pathways complete in all 7 mapped organisms but cannot say whether those pathways are required under defined conditions [src: essential_metabolome]; the other bridges 19 metabolites from production data to mutant-fitness data but records no organism consumption action at all [src: webofmicrobes_explorer]. Whether such evidence can sit alongside utilization or single-substrate growth results in the same comparison determines what the corpus is entitled to conclude about metabolic agreement across assays.

## Evidence Sides

**Complete pathways, condition-blind assays.** The essential-metabolome pilot adds an assay-scope and coverage tension rather than contradicting the other results: it found 17 of 18 amino-acid pathways complete in all 7 mapped organisms, but used rich-media RB-TnSeq — random barcode transposon sequencing, a pooled assay of mutant fitness — and computational GapMind calls (pathway-completeness predictions from genome annotation) that cannot determine whether pathways are required under defined conditions [src: essential_metabolome].

**A production-only bridge with a null consumption record.** The Web of Microbes evidence adds a related scope tension: it provides a production-to-Fitness Browser bridge for 19 metabolites — the Fitness Browser being the mutant-fitness data collection the bridge connects to — but its 2018 snapshot has no organism consumption action, whereas other comparisons include utilization or single-substrate growth evidence [src: webofmicrobes_explorer]. This is a null, not a small number: the action is absent from the snapshot, so the bridge reaches only the production side of metabolism.

## Possible Reconciliations

- *Complementary-projection hypothesis*: the two datasets may be non-overlapping projections of the same metabolism — capability breadth from one, metabolite-level linkage from the other — in which case neither substitutes for condition-resolved utilization evidence and both should be labelled by assay scope rather than pooled.
- *Latent-capability hypothesis*: uniform completeness across all 7 mapped organisms may reflect latent genomic capability rather than condition-specific dependency [src: essential_metabolome], which would explain why it neither agrees nor disagrees with utilization assays.
- *Snapshot-artifact hypothesis*: the absent consumption action may be a property of the 2018 export rather than of exometabolomics — the measurement of metabolites an organism releases into or removes from its surroundings — as an assay [src: webofmicrobes_explorer], in which case a later export could convert this scope gap into a testable comparison.

## Resolving Work

- Re-run the pathway calls under defined-medium RB-TnSeq for the same 7 mapped organisms and ask which of the 17 of 18 complete pathways become fitness-required when the corresponding metabolite is withheld [src: essential_metabolome].
- Obtain a Web of Microbes export that carries a consumption action, then re-test the 19-metabolite bridge and ask whether consumed metabolites, unlike produced ones, predict mutant-fitness phenotypes [src: webofmicrobes_explorer].
- Build a pathway-to-metabolite lookup table joining GapMind pathway names to exometabolite identifiers, and ask how many of the 19 bridged metabolites map onto a completeness call at all.
- Score every cross-assay comparison in the corpus by assay scope (condition-resolved versus capability-only; production-only versus utilization) and ask whether apparent agreement tracks scope match rather than biology.
