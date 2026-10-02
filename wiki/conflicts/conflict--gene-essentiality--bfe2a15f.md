<!-- tension-hash: bfe2a15fe26a86e3 -->
# Whether Genomic Completeness and Observed Production Can Establish Essentiality

The corpus disagrees about how far an organism's *encoded* or *observed* metabolism licenses claims about what it *requires*. On one side sits an observation of near-uniform pathway completeness across a small mapped organism set; on the other, findings that metabolite-production records underdetermine uptake, pathway completeness and gene essentiality, and that measured essentiality is mostly organism-specific rather than universal. The disagreement matters because it decides whether pathway and metabolite-production catalogues can be read as dependency evidence in [[concepts/gene-essentiality]], or only as capability inventories that require perturbation data before any essentiality claim is made.

## Evidence Sides

**Completeness is near-uniform across the mapped organisms.** In the mapped organism set, 17 of 18 amino-acid pathways were complete in all 7 mapped organisms [src: essential_metabolome]. This near-invariant pathway presence within the sample is the capability observation that the rest of the tension is measured against.

**Observation of production cannot establish uptake or essentiality.** In the Web of Microbes snapshot — a record of metabolite observations relative to a starting medium — the snapshot has no organism consumption actions, so consumption (and therefore uptake) is simply not recorded [src: webofmicrobes_explorer]. Chemical identity is also ambiguous: 107 formula-only matches (matches made on molecular formula alone, without structure) expanded to 900 candidate molecules [src: webofmicrobes_explorer]. On this side, production matches cannot establish uptake, pathway completeness, or gene essentiality.

**Measured essentiality is predominantly conditional, not universal.** Of 17,222 ortholog families (groups of genes descended from a common ancestral gene across organisms), only 859 were universally essential, while 4,799 were variably essential and 11,564 were never essential [src: discoveries]. Within the completeness result itself there is a counter-instance: DvH (*Desulfovibrio vulgaris* Hildenborough) lacked predicted serine biosynthesis [src: essential_metabolome]. Genomic completeness is a statement of capability, not of measured dependency [src: metabolic_capability_dependency].

## Possible Reconciliations

- **Hypothesis: the two sides measure different quantities.** Completeness scores presence of an encoded route; essentiality scores loss-of-function growth defect under one tested condition. If so, 17 of 18 complete pathways [src: essential_metabolome] and 859 universally essential families [src: discoveries] are compatible without either being wrong.
- **Hypothesis: the level of aggregation drives the discrepancy.** A pathway may be required while most of its constituent ortholog families are individually dispensable through redundancy, which would place the 11,564 never-essential families [src: discoveries] under complete pathways.
- **Hypothesis: environmental supply substitutes for biosynthesis.** If required metabolites are obtained from the medium, biosynthetic genes score non-essential and absent pathways (DvH serine) go unpunished [src: essential_metabolome] — but the snapshot's lack of consumption actions means uptake cannot currently be checked [src: webofmicrobes_explorer].

## Resolving Work

- Pair the 7 mapped organisms' pathway-completeness calls with per-gene fitness data from the same organisms and ask whether complete pathways carry measurably essential genes, pathway by pathway.
- Test DvH for serine auxotrophy in defined medium with and without serine, asking whether the predicted gap is a real growth requirement.
- Stratify the 4,799 variably essential families by condition metadata to ask whether variability tracks medium composition rather than genomic context.
- Resolve the 107 formula-only matches to structures using authentic chemical standards, asking how many of the 900 candidates survive.
- Extend the metabolite snapshot with depletion (consumption) measurements to test whether observed production co-occurs with uptake of the same compounds.
