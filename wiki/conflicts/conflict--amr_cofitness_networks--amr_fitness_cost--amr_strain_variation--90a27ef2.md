<!-- tension-hash: 75c4d8f77885aac9 -->
# Antimicrobial resistance: pooled fitness signals versus their matched, mechanistic and cross-level controls

Four projects in this corpus — `amr_fitness_cost`, `fitness_effects_conservation`, `amr_cofitness_networks` and `amr_strain_variation` — contribute to a set of disagreements about how far the antimicrobial-resistance (AMR) fitness results can be pushed. A measured AMR fitness burden and an antibiotic-dependent benefit are on record and are not themselves disputed here. [src: amr_cofitness_networks] What is disputed is what surrounds that result: whether the antibiotic-dependent flip survives class matching, whether resistance *mechanism* is a causal hinge or two unrelated correlations, whether AMR genes obey the corpus-wide fitness–conservation gradient or are an exception to it, whether the co-fitness enrichment around AMR genes is mechanistic or an artifact of shared laboratory dispensability, and whether genomic co-inheritance of resistance islands and co-fitness network size measure the same architecture. The disagreements are not all of one kind — some oppose a large pooled analysis to a smaller matched one, others oppose two different observables or two different levels of organization — and treating them as interchangeable is part of what makes the pooled numbers easy to over-read downstream. This page covers all five disagreements as written on [[concepts/antimicrobial-resistance-fitness-cost]]; it imports no figures beyond those recorded in that tension text.

## Evidence Sides

### Disagreement 1 — Any-antibiotic flip versus class-matched flip

**Side A: the pooled any-antibiotic signal is strong.** The any-antibiotic analysis found a **57.0%** flip rate for **N = 797** genes with **p = 0.0001**. [src: amr_fitness_cost] A "flip" here is a gene that becomes relatively *more important* under antibiotic exposure than without it — its knockout fitness decreases. [src: amr_fitness_cost] Because these are pool-relative fitness values rather than absolute growth rates, a flip marks a shift in relative importance, not a crossing from absolute advantage to absolute cost; the concept page is explicit that the baseline AMR-knockout comparison is made against the non-AMR knockout background and must not be read as absolute advantage. [src: amr_fitness_cost]

**Side B: the class-matched validation is not significant.** The class-matched analysis — restricting to genes tested against an antibiotic of the class their mechanism is supposed to defend against — found a **54.8%** flip rate for **157** pairs with **p = 0.14**. [src: amr_fitness_cost] The class-matched analysis was less powered than the any-antibiotic analysis, so the positive pooled signal should not be treated as equally strong for every drug-resistance class. [src: amr_fitness_cost] The concept page is explicit that this does not establish opposing biological effects, because the analyses differ in sample size and matching design; it identifies a need to determine whether broad condition coverage or antibiotic-class specificity best explains the stronger result. [src: amr_fitness_cost]

### Disagreement 2 — Mechanism predicts conservation but not cost

**Side A: mechanism does not structure baseline cost.** Mechanism was not associated with baseline cost (**H = 0.65, p = 0.89**), where H is the Kruskal–Wallis statistic for a difference in distributions across more than two groups. [src: amr_fitness_cost]

**Side B: mechanism strongly structures pangenome position.** Mechanism was strongly associated with conservation status (**χ² = 69.3, p = 1.4×10⁻¹³**), a chi-square test of association between categorical mechanism and categorical core/accessory assignment. [src: amr_fitness_cost] The evidence therefore supports different roles for mechanism in fitness and pangenome distribution rather than a single mechanism-to-cost-to-retention pathway. [src: amr_fitness_cost]

### Disagreement 3 — The all-gene conservation gradient versus the AMR-specific null

**Side A: fitness importance tracks conservation corpus-wide.** The all-gene analysis found higher core representation among essential and broadly fitness-active genes, plus stronger positive and negative fitness tails among core genes. [src: fitness_effects_conservation]

**Side B: AMR genes show no such split.** Core or intrinsic and accessory or acquired AMR genes had indistinguishable baseline fitness distributions (**d = 0.002, p = 0.33**), where d is Cohen's d, a standardized difference in means. [src: fitness_effects_conservation] [src: amr_fitness_cost] As the concept page frames it, these results address different scopes and observables, but resolving whether AMR genes are an exception requires a larger, condition-matched AMR subset with comparable coverage of core, accessory, and singleton genes.

### Disagreement 4 — Mechanistic co-fitness versus shared dispensability

**Side A: AMR support neighborhoods are functionally enriched.** Flagellar motility, chemotaxis, and amino acid biosynthesis were enriched in AMR support neighborhoods — a co-fitness neighborhood being the set of genes whose fitness profiles correlate with a focal gene's across experiments. [src: amr_cofitness_networks]

**Side B: the enrichment may be a lab-condition artifact.** The cofitness analysis identifies shared dispensability under laboratory conditions as an alternative explanation and reports no network-size relationship with cost. [src: amr_cofitness_networks] This does not contradict the measured AMR fitness burden or antibiotic-dependent benefit; it limits the inference that cofitness-network structure explains that burden. [src: amr_cofitness_networks]

### Disagreement 5 — Genomic co-inheritance versus null network-size effect

**Side A: resistance islands are tightly co-inherited.** Mean phi **0.827** — phi being a correlation coefficient for two binary presence/absence variables — and **88%** multi-mechanism islands indicate strong co-inheritance. [src: amr_strain_variation]

**Side B: linkage is not co-selection, and network size does not predict cost.** The atlas explicitly cautions that linkage on mobile genetic elements (plasmids, transposons and similar transmissible DNA) does not prove co-selection or functional synergy. [src: amr_strain_variation] Thus, genomic co-inheritance can coexist with a null cofitness-size–cost relationship; the two analyses should not be treated as interchangeable measures of network architecture. [src: amr_strain_variation] [src: amr_cofitness_networks] The resistance-island result introduces this measurement tension rather than resolving Disagreement 3. [src: amr_strain_variation]

## Possible Reconciliations

These are hypotheses, not established findings.

*Power, not effect, separates the two flip rates (Disagreement 1).* The two flip rates — **57.0%** and **54.8%** — are close, while the sample sizes (**N = 797** versus **157** pairs) are not. [src: amr_fitness_cost] A plausible hypothesis is that both estimate the same modest effect and only the larger analysis can resolve it from zero, in which case the class-matched result is uninformative rather than contradictory. A competing hypothesis is that the any-antibiotic analysis is inflated by broad-spectrum mechanisms responding to off-class drugs; the concept page frames exactly this choice between broad condition coverage and antibiotic-class specificity. [src: amr_fitness_cost]

*Two channels, not one pathway (Disagreement 2).* Mechanism could determine mobility and acquisition route — and therefore pangenome position — without determining the metabolic cost of carrying the gene, which would make **H = 0.65, p = 0.89** and **χ² = 69.3, p = 1.4×10⁻¹³** jointly true of different causal channels rather than mutually inconsistent. [src: amr_fitness_cost] This is the reading the concept page already favors. [src: amr_fitness_cost]

*Scope and observable mismatch (Disagreement 3).* The all-gene gradient is built on essentiality and breadth of fitness activity across the whole gene complement, while the AMR contrast is a baseline-fitness comparison within a small, functionally homogeneous gene set. [src: fitness_effects_conservation] [src: amr_fitness_cost] A range-restriction hypothesis follows: AMR genes may occupy too narrow a slice of the fitness axis for the corpus-wide gradient to be detectable, making the **d = 0.002** null an absence of resolution rather than a genuine exception. [src: fitness_effects_conservation] [src: amr_fitness_cost]

*The laboratory selects a common phenotype (Disagreement 4).* If flagellar, chemotaxis and biosynthesis genes are dispensable under the same assay conditions that make AMR genes dispensable, co-fitness correlation would arise without any shared regulation or mechanism — the alternative the cofitness project itself names. [src: amr_cofitness_networks] Both sides are then right: the enrichment is real as measured and non-mechanistic in interpretation.

*Different levels of organization (Disagreement 5).* Physical linkage on mobile elements operates at the level of inheritance across genomes, whereas co-fitness-network size operates at the level of phenotypic response within an assayed strain. [src: amr_strain_variation] [src: amr_cofitness_networks] A tight island (phi **0.827**) could therefore be co-inherited by hitchhiking while contributing nothing detectable to the cost–network-size relationship. [src: amr_strain_variation] [src: amr_cofitness_networks]

## Resolving Work

**Disagreement 1 — pooled versus class-matched flip**
- Power analysis on the class-matched design: given the observed **54.8%** flip rate in **157** pairs, compute the pair count needed to reach conventional significance, and report whether the corpus can supply it. [src: amr_fitness_cost]
- Re-run the any-antibiotic analysis with off-class experiments excluded gene by gene, and ask whether the **57.0%** flip rate survives. [src: amr_fitness_cost]
- Stratify both flip analyses by mechanism, asking whether broad-spectrum mechanisms carry the pooled signal while narrow-spectrum ones are flat.
- Report effect sizes with confidence intervals for both analyses side by side, so that overlap versus separation — rather than the **p = 0.0001** / **p = 0.14** contrast — decides the question. [src: amr_fitness_cost]

**Disagreement 2 — mechanism, cost and conservation**
- Test mechanism against conservation with organism and phylogeny as covariates, asking whether **χ² = 69.3** reflects mechanism or lineage composition. [src: amr_fitness_cost]
- Re-test mechanism against cost within conservation class, asking whether the **H = 0.65** null hides opposing within-class effects. [src: amr_fitness_cost]
- Fit a mediation model with mechanism → cost → conservation and report whether the cost path carries any weight, which the corpus currently predicts it will not. [src: amr_fitness_cost]
- Ask whether mechanism predicts mobility markers directly, testing the alternative channel proposed above.

**Disagreement 3 — AMR exception or resolution limit**
- Assemble the larger, condition-matched AMR subset with comparable coverage of core, accessory, and singleton genes that the concept page names as the prerequisite, and repeat the baseline-fitness contrast.
- Apply the all-gene observables — essentiality and breadth of fitness activity — to the AMR subset, rather than baseline fitness alone, so the two sides measure the same thing. [src: fitness_effects_conservation]
- Draw non-AMR gene sets matched to the AMR fitness distribution and check whether the conservation gradient also vanishes in them, testing the range-restriction hypothesis.
- Report the confidence interval on **d = 0.002** to distinguish a true null from an underpowered one. [src: fitness_effects_conservation] [src: amr_fitness_cost]

**Disagreement 4 — mechanism versus shared dispensability**
- Run a fitness-matched permutation: draw control genes with the same baseline fitness distribution as AMR genes and ask whether flagellar motility, chemotaxis, and amino acid biosynthesis remain enriched in their neighborhoods. [src: amr_cofitness_networks]
- Restrict the co-fitness computation to conditions where the enriched functions are *not* dispensable and re-test the enrichment. [src: amr_cofitness_networks]
- Re-examine the reported absence of a network-size-to-cost relationship with mechanism-stratified networks, asking whether a real relationship exists in a subset. [src: amr_cofitness_networks]
- Check whether enriched neighbors share regulators or operon structure — evidence that would favor co-regulation over shared dispensability.

**Disagreement 5 — linkage versus network architecture**
- For islands with mean phi **0.827**, test whether member genes also co-vary in fitness, which would connect the two levels directly. [src: amr_strain_variation] [src: amr_cofitness_networks]
- Compare islands on mobile genetic elements against chromosomally linked ones, asking whether the co-selection interpretation holds only for the latter. [src: amr_strain_variation]
- Ask whether the **88%** multi-mechanism islands show measurable joint benefit under multi-drug conditions, the direct test of coordinated defense. [src: amr_strain_variation]
- Report island membership and co-fitness network size as separate predictors of cost in one model, making explicit that they are not interchangeable measures. [src: amr_strain_variation] [src: amr_cofitness_networks]
