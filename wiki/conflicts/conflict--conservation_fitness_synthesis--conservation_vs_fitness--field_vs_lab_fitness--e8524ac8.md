<!-- tension-hash: d64c9fd5c1dbb782 -->
# Laboratory Fitness versus Natural Selection: Conserved Genes That Look Dispensable, Burdensome, or Unmeasured in the Lab

The concept page [[concepts/laboratory-fitness-versus-natural-selection]] carries six distinct tensions that all turn on the same question: when a gene's laboratory fitness signal and its pangenome conservation disagree, which measurement is wrong? "Core" here means a gene retained across essentially all genomes in a pangenome (the set of genes across a species or clade); "accessory" and "singleton" genes are retained in fewer genomes or only one. The disagreements are (1) core genes being burdensome in the lab while also being the most conserved, (2) condition-specific fitness being read as niche-specific, (3) singleton genes looking neutral, (4) field-stress versus heavy-metal importance inside one organism, (5) two different essential-core percentages from two cohorts, and (6) whether the fitness–conservation gradient survives adjustment for gene length. This page covers all six. It records them separately because they demand different resolving data: some are biological, some are definitional, and at least two are artifacts-of-measurement candidates that would dissolve under better covariate control rather than under new biology.

## Evidence Sides

### D1 — Core genes are burdens, yet core genes are the most conserved

**Side A — the laboratory burden signal.** 24.4% of core genes were burdensome when deleted in the laboratory, meaning the deletion mutant grew better than wild type under tested conditions. [src: conservation_fitness_synthesis] Read alone, this is a cost signal: the cell pays to maintain these genes and gains by losing them.

**Side B — the conservation signal.** Core genes were nonetheless more conserved than always-neutral genes, which were 66% core. [src: conservation_fitness_synthesis] Pangenome retention across many genomes is the opposite of what a purely costly gene should show. The project's own reading is an environmental mismatch: laboratory conditions measure a restricted component of fitness, whereas pangenome conservation integrates selection across broader contexts. [src: conservation_fitness_synthesis]

### D2 — Condition-specific fitness is not niche-specific fitness

**Side A — the specificity-implies-accessory expectation.** The naive expectation, which this result overturns, is that genes with strong condition-restricted phenotypes should be the flexible, niche-adapted part of the genome.

**Side B — the measurement.** Core genes were 1.78x more likely to show strong condition-specific phenotypes. [src: conservation_fitness_synthesis] The report is explicit that condition-specific fitness was not equivalent to niche-specific fitness, and that resolving this requires environmental experiments or validated environmental proxies, not further interpretation of laboratory measurements alone. [src: conservation_fitness_synthesis]

### D3 — Singleton neutrality: real dispensability or missing measurement

**Side A — core genes are the functionally extreme ones.** Core genes were more likely to show beneficial deletion effects and strong fitness effects overall, while singleton genes appeared largely neutral. [src: fitness_effects_conservation] This **supports** an assay-coverage-and-network-context reading: core genes sit in well-covered, well-connected pathways and therefore produce detectable effects in both directions.

**Side B — neutrality is unproven either way.** The same report states that this does not establish whether singleton neutrality reflects true dispensability or missing measurements. [src: fitness_effects_conservation] The two readings — singletons are genuinely inert, versus singletons are simply not being measured — are observationally identical in the current data.

### D4 — Two ecologically relevant categories, opposite conservation

**Side A — field-stress genes are more core.** In *Desulfovibrio vulgaris* Hildenborough (DvH), field-stress genes were more core than heavy-metal-important genes, although both categories were treated as ecologically relevant. [src: field_vs_lab_fitness] If ecological relevance drove conservation, the two should behave alike.

**Side B — the proposed biology is untested.** The report hypothesizes that specific metal-resistance mechanisms may be accessory while uranium- and mercury-related responses may involve fundamental stress pathways; this is not a direct mobile-element or natural-selection measurement. [src: field_vs_lab_fitness] The mechanism is therefore a label placed on the pattern, not evidence independent of it.

### D5 — 82% versus 86.1% essential-core

**Side A — the broad synthesis.** The 82% essential-core estimate comes from the broad synthesis. [src: conservation_fitness_synthesis]

**Side B — the 33-organism linkage.** The 86.1% estimate comes from the 33-organism linkage. [src: conservation_vs_fitness]

These are an unresolved scope tension because their cohorts and definitions differ. [src: conservation_fitness_synthesis] [src: conservation_vs_fitness] Neither figure may be averaged with the other or substituted for it.

### D6 — Does the gradient survive gene-length adjustment?

**Side A — length dominates in DvH.** Adding gene length raised CV-AUC to 0.645, whereas fitness alone reached 0.517–0.548. [src: field_vs_lab_fitness] CV-AUC is cross-validated area under the ROC curve, a 0.5-to-1.0 measure of how well a model separates core from non-core genes on held-out data; 0.5 is chance.

**Side B — the broad gradient, unadjusted.** Broader analyses report a real but weak gradient without length adjustment. [src: fitness_effects_conservation, conservation_fitness_synthesis]

These results are not contradictory estimates of one model; the unresolved issue is how much of the broad gradient survives explicit adjustment for length, insertion callability (whether a gene can receive and retain scorable transposon insertions at all), phylogeny, and pangenome coverage.

## Possible Reconciliations

Each of the following is a **hypothesis**, not a finding, and none is preferred here.

**D1 — trade-off maintenance (hypothesis).** Both sides are right if the burdensome 24.4% are genes whose cost is real in the tested regime and whose benefit is real outside it, so that lab burden and pangenome retention measure opposite ends of the same trade-off rather than contradicting each other. [src: conservation_fitness_synthesis] This is the environmental mismatch interpretation the report already endorses; it remains an interpretation because the compensating benefit has not been measured. [src: conservation_fitness_synthesis]

**D2 — detectability, not ecology (hypothesis).** Core genes may be 1.78x more likely to show strong condition-specific phenotypes because they are more likely to be assayed under a condition that engages them, not because specificity itself is a core-genome property. [src: conservation_fitness_synthesis] Under this hypothesis the conflict is definitional: "condition-specific" indexes the experimental panel, "niche-specific" indexes the organism's habitat, and the two were never the same quantity.

**D3 — coverage asymmetry (hypothesis).** If singleton genes systematically receive fewer usable transposon insertions or fewer informative conditions, apparent singleton neutrality and true singleton dispensability would produce the same near-neutral readout, and Side A's network-context account would be correct for core genes while saying nothing about singletons. [src: fitness_effects_conservation]

**D4 — mechanism-class heterogeneity (hypothesis).** The DvH split reconciles if "ecologically relevant" is not one category: narrowly specific metal-resistance determinants could be accessory while broad uranium- and mercury-linked stress responses are core, exactly as the report hypothesizes. [src: field_vs_lab_fitness] Because this is not a direct mobile-element or natural-selection measurement, the alternative — that the split reflects condition-panel composition rather than gene class — is equally live. [src: field_vs_lab_fitness]

**D5 — non-overlapping estimands (hypothesis).** 82% and 86.1% may both be correct for their own cohorts and essentiality definitions, in which case the disagreement is one of scope rather than of fact. [src: conservation_fitness_synthesis] [src: conservation_vs_fitness] The competing hypothesis is that one definition is systematically more permissive, which would make the gap an artifact of thresholding rather than of organism sampling.

**D6 — confounded, not contradicted (hypothesis).** If gene length correlates with both core status and fitness detectability, the weak broad gradient and the length-dominant DvH model are compatible: length could be a shared cause that inflates the unadjusted gradient, or a proxy for the same functional centrality that fitness importance tracks. [src: field_vs_lab_fitness] [src: fitness_effects_conservation, conservation_fitness_synthesis] Which of those two it is determines whether the gradient shrinks or survives under adjustment.

## Resolving Work

**D1 — burden versus conservation**
- Re-assay the burdensome core genes under non-laboratory-like regimes (starvation, community coculture, surface attachment) and ask whether the positive deletion effect reverses sign; a sign reversal converts the mismatch interpretation from reading to result. [src: conservation_fitness_synthesis]
- Partition the 24.4% by functional category and test whether burden is concentrated in categories with a plausible off-panel benefit, which would localize the mismatch rather than assert it globally. [src: conservation_fitness_synthesis]
- Compare burden frequency in core versus always-neutral genes under matched condition counts, so that the 66%-core neutral class is not compared against a differently sampled core class. [src: conservation_fitness_synthesis]

**D2 — condition-specific versus niche-specific**
- Run the environmental experiments the report names as necessary, or validate an environmental proxy against measured field conditions before using it, since laboratory reinterpretation cannot settle this. [src: conservation_fitness_synthesis]
- Recompute the 1.78x enrichment after stratifying by the number of conditions in which each gene was testable, separating specificity from panel coverage. [src: conservation_fitness_synthesis]
- Define "niche-specific" operationally against habitat occupancy data and test whether that definition also enriches for core genes; if it does not, the two terms are confirmed to be distinct quantities. [src: conservation_fitness_synthesis]

**D3 — singleton neutrality**
- Quantify per-gene insertion density and scorable-condition count for singleton versus core genes, then ask whether singleton mean fitness stays near neutral within the well-covered subset only. [src: fitness_effects_conservation]
- Targeted deletion of a sample of singleton genes with direct growth assays, removing the pooled-assay coverage dependency entirely. [src: fitness_effects_conservation]
- Test whether the strong-effect excess in core genes persists after matching core and singleton genes on network connectivity, which would isolate network context from conservation status. [src: fitness_effects_conservation]

**D4 — field-stress versus heavy-metals in DvH**
- Map the heavy-metal-important and field-stress gene sets onto mobile-element annotations and genomic-island calls to test the accessory-mechanism hypothesis directly, since the report's claim is not a mobile-element measurement. [src: field_vs_lab_fitness]
- Check whether the difference persists when the two condition classes are matched on number of experiments and effect-size distribution, ruling out panel composition. [src: field_vs_lab_fitness]
- Extend the same field-versus-lab condition classification to additional organisms; a DvH-only pattern is a single-organism result and must be treated as such. [src: field_vs_lab_fitness]

**D5 — 82% versus 86.1%**
- Recompute both estimates on the intersection of the two cohorts under a single essentiality definition, reporting the value for each definition separately rather than a merged figure. [src: conservation_fitness_synthesis] [src: conservation_vs_fitness]
- Perform a definition-swap analysis: apply the 33-organism essentiality criterion to the broad-synthesis cohort and vice versa, attributing the gap to cohort or to definition. [src: conservation_fitness_synthesis] [src: conservation_vs_fitness]
- Report per-organism core percentages for the shared organisms so the aggregate difference can be traced to specific taxa rather than to a global shift. [src: conservation_fitness_synthesis] [src: conservation_vs_fitness]

**D6 — length adjustment and the gradient**
- Refit the broad fitness–conservation gradient with gene length as a covariate and report the change in effect size; this is the single analysis that most directly settles the tension. [src: fitness_effects_conservation, conservation_fitness_synthesis] [src: field_vs_lab_fitness]
- Add insertion callability as a covariate alongside length, since a gene too short or too poorly insertible to score contributes to both axes. [src: field_vs_lab_fitness]
- Apply a phylogeny-aware model across organisms so that the gradient is not carried by a few closely related genomes counted as independent observations. [src: fitness_effects_conservation, conservation_fitness_synthesis]
- Stratify by pangenome coverage depth and test whether the gradient weakens in shallowly sampled pangenomes, where core calls are least reliable. [src: fitness_effects_conservation, conservation_fitness_synthesis]
- Repeat the DvH CV-AUC comparison (fitness alone 0.517–0.548 versus 0.645 with length) in at least two further organisms to establish whether length dominance is general or DvH-specific. [src: field_vs_lab_fitness]
