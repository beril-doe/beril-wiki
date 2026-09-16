<!-- tension-hash: 459994d3d70b48a3 -->
# Technically Valid Joins Versus Demonstrated Findings: Integration and Signal That Outrun Evidential Warrant

Across [[concepts/cross-tenant-data-bridging]] and [[concepts/phage-defense-syndromes-and-arms-race]], the corpus records a recurring family of disagreements in which one project's positive result is, by another project's accounting, an artifact of how the result was measured, scoped, or defined rather than a demonstrated fact. The disputes share a shape — a join that executes, a prevalence that is near-universal, a correlation that is strong, a classifier that scores well — set against evidence that the same quantity collapses, reverses, or becomes uninterpretable when provenance, direction, annotation source, aggregation level, or cohort structure is audited. Because the sides rest on different observables rather than on contradictory measurements of one observable, none of them can be resolved by averaging. This page covers seven distinct disagreements present in the input tension text: (1) documented versus actual bridge use, (2) names and tenancy versus audited authority, (3) metabolite production versus utilization, (4) prophage prevalence versus annotation provenance and effect ranking, (5) arms-race consistency versus demonstrated coevolution, (6) pairwise versus module-level and lab versus field fitness signal, and (7) statistical strength versus translational warrant, including paper counts and sampling-dependent effect sizes. No disagreement from the input is left out.

## Evidence Sides

### Disagreement 1 — "Zero documented use" versus "zero use"

**Side A — the audit's realized-use count.** The atlas exposes a tension between 536 schema-level bridges and evidential validation: the original audit recorded five high-leverage bridges with zero realized use. [src: berdl_data_atlas]

**Side B — the count is a lower bound and already moved.** UC1 was subsequently sample-executed and UC2–UC5 remained untested, and the realized-use count is also a lower bound because README mining — scanning project documentation for evidence of use — may miss plans and notebooks. [src: berdl_data_atlas] Thus "zero documented use" and "zero use" are not equivalent claims.

### Disagreement 2 — Naming and tenancy versus audited authority

**Side A — prefixes imply common authority.** The implicit assumption under broad catalog-level integration claims is that a catalog prefix, tenant, or name proves common authority. [src: nmdc_context_audit]

**Side B — the audit contradicts that assumption.** The NMDC audit **contradicts** any assumption that a catalog prefix, tenant, or name proves common authority: 20 entries resolve to 7 resources, with `kbase.nmdc_neon` a NEON namesake collision. [src: nmdc_context_audit]

### Disagreement 3 — Production versus utilization, and formula versus compound

**Side A — the bridge is actionable.** The Web of Microbes (WoM) snapshot introduces a related tension with broad cross-collection integration claims: the 19-metabolite Fitness Browser bridge is directly actionable. [src: webofmicrobes_explorer]

**Side B — direction and identity are unresolved.** Missing consumption actions mean production cannot be treated as utilization, and 107 formula-only ModelSEED matches — matches made on molecular formula alone against the ModelSEED biochemistry reference — expand to 900 candidate molecules. [src: webofmicrobes_explorer] This **refines** rather than overturns the framework: a join may be technically valid while its biological direction and chemical identity remain uncertain. The concrete case is semantic: tryptophan increased in WoM and had 231 significant Fitness Browser genes and a complete GapMind pathway — GapMind being the pathway-completeness annotation tool — yet 0/50 *P. fluorescens* strains used it as carbon; production therefore does not imply utilization. [src: fw300_metabolic_consistency]

### Disagreement 4 — Prophage prevalence and effect ranking versus annotation provenance

**Side A — concordant, near-universal signal with an environmental effect.** The prophage study **refines** this tension: module-level pangenome and NMDC associations were concordant, and its environmental effect exceeded family-level phylogeny in the reported PERMANOVA — a permutation test of whether grouping explains multivariate composition. [src: prophage_ecology]

**Side B — provenance, dominance, and coverage caveats.** Prophage annotations came from eggNOG rather than geNomad or VIBRANT, so near-universal prevalence may include domesticated remnants, bacterial homologs, and integrases; the false-positive rate is uncharacterized. [src: prophage_ecology] In the same analysis genome size was dominant (rho=0.717, a rank correlation), only 28% of genomes had embeddings, and genus-level NMDC inference assumed conserved prophage content. [src: prophage_ecology]

### Disagreement 5 — Arms-race consistency versus demonstrated coevolution

**Side A — enrichment patterns match arms-race expectations.** The study **supports** [[concepts/phage-defense-syndromes-and-arms-race]]: human-associated environments enriched tail (log2(OR)=2.21, a log odds ratio), head morphogenesis (1.98), and anti-defense (1.70), whereas anti-defense was depleted in freshwater (-0.74) and animal-associated environments (-0.24). [src: prophage_ecology]

**Side B — mechanism is not shown.** These are consistent with arms-race theory but do not demonstrate coevolution. [src: prophage_ecology] TerL lineages did not show independent enrichment in 0/500 FDR-corrected tests — FDR being false discovery rate, the expected share of false positives among called hits — and among 824 lineages with at least 5 species, 325 were specialists and 499 generalists. [src: prophage_ecology]

### Disagreement 6 — Pairwise versus module-level, and lab versus field, fitness signal

**Side A — aggregation recovers signal.** The co-fitness bridge had weak pairwise but stronger module-level effects. [src: cofitness_coinheritance]

**Side B — the pairwise signal points the wrong way, and field data does not follow.** Co-fitness strength was anti-correlated with co-occurrence (rho=-0.109, p<1e-300 across 1.04M pairs), requiring auxiliary-only comparisons below 95% prevalence. [src: cofitness_coinheritance] The field-versus-lab study likewise found weak condition-only prediction (AUC 0.548 — area under the ROC curve, where 0.5 is chance; field-only 0.517; lab-only 0.531) and no significant module-conservation correlation with field activity (rho=0.071, p=0.62). [src: field_vs_lab_fitness]

### Disagreement 7 — Strong statistics versus translational and evidential warrant

**Side A — high-performing statistics.** Binary growth could be predicted for tryptophan (AUC 0.933), phenylalanine (0.932), and valine (0.927). [src: genotype_to_phenotype_enigma] The IBD CCA result (canonical correlation analysis, which finds maximally correlated linear combinations of two data blocks) reached r=0.964. [src: ibd_phage_targeting]

**Side B — the same analyses fail on other targets, cohorts, and designs.** Continuous phenotypes had negative R² — worse than predicting the mean. [src: genotype_to_phenotype_enigma] The IBD CCA result (r=0.964) and PhageFoundry coverage are hypothesis-generating rather than clinical validation; HMP2/FRANZOSA clustering had cross-cohort LOSO ARI=0.000 (leave-one-study-out adjusted Rand index, zero meaning no better than chance agreement), and the cocktail covered only tested strains. [src: ibd_phage_targeting] In ecotype analyses, pooled diagnosis was structurally unidentifiable because 45 sub-studies had at least 10 HC samples, 5 had at least 10 CD, and 0 had at least 10 of both; selection-on-outcome leakage reduced independent Tier-A candidates from 33 to 3. [src: pitfalls] Evidence proxies are similarly unequal: PaperBLAST's organism-level Gini coefficient is 0.967 and gene-level Gini 0.669 — Gini measuring inequality on a 0-to-1 scale; 9.2% of 50%-identity families have zero papers, 46.1% exactly one, and 4.3% at least 20, contradicting paper count as a uniform evidence proxy. [src: paperblast_explorer] And effect magnitude tracked sampling: the ecotype analysis found p=0.83 and rho=-0.085, p=0.25, while its median partial correlation was 0.081 across 183 species versus 0.003 originally, a reported 27x difference caused by different sampling. [src: ecotype_env_reanalysis]

## Possible Reconciliations

These are hypotheses, not findings; each is stated so that both sides of a disagreement could be simultaneously correct.

- **Hypothesis (measurement scope, D1):** "zero realized use" and "used but undocumented" are compatible if realized use is measured by README mining, which the atlas itself flags as a lower bound; the subsequent sample execution of UC1 would then be the first observation of a quantity the audit could not see, not a refutation of it. [src: berdl_data_atlas]
- **Hypothesis (definitional, D2):** both sides hold if "NMDC-named" and "NMDC-authored" are different predicates; 20 entries resolving to 7 resources with a NEON namesake collision is then a statement about naming space, not about the resources' scientific validity. [src: nmdc_context_audit]
- **Hypothesis (directionality and identity, D3):** an actionable 19-metabolite bridge and an uninterpretable one can coexist if the WoM snapshot records production actions only, so a join carries chemical reachability while leaving direction unmeasured; the 107 formula-only ModelSEED matches expanding to 900 candidate molecules would then be a resolution limit of formula-level matching rather than a wrong join. [src: webofmicrobes_explorer] The tryptophan case is the same hypothesis at organism scale: 231 significant Fitness Browser genes and a complete GapMind pathway may index degradation or salvage capacity that is not carbon-source growth in 0/50 *P. fluorescens* strains. [src: fw300_metabolic_consistency]
- **Hypothesis (annotation regime, D4):** near-universal prophage prevalence and an uncharacterized false-positive rate are compatible if eggNOG-based annotation captures a broader set — domesticated remnants, bacterial homologs, integrases — than dedicated prophage callers; the environmental effect exceeding family-level phylogeny could then be real for the eggNOG-defined feature set while genome size (rho=0.717) remains the dominant covariate and 28% embedding coverage limits which genomes were testable. [src: prophage_ecology]
- **Hypothesis (evidentiary level, D5):** arms-race-consistent enrichment (tail log2(OR)=2.21, head morphogenesis 1.98, anti-defense 1.70; freshwater -0.74, animal-associated -0.24) and the absence of independent TerL lineage enrichment in 0/500 FDR-corrected tests are both expected if environment selects gene-category composition without lineage-specific coevolutionary tracking, consistent with 325 specialists versus 499 generalists among 824 lineages. [src: prophage_ecology]
- **Hypothesis (aggregation and noise, D6):** weak pairwise and stronger module-level effects can both be true if pairwise co-fitness is noise-dominated while modules average that noise out; the negative pairwise relation (rho=-0.109, p<1e-300 across 1.04M pairs) would then reflect prevalence structure, which is why auxiliary-only comparisons below 95% prevalence were required. [src: cofitness_coinheritance] Near-chance field prediction (AUC 0.548; 0.517; 0.531) and a non-significant module-conservation correlation (rho=0.071, p=0.62) are compatible with real lab signal if field activity is governed by conditions absent from the lab panel. [src: field_vs_lab_fitness]
- **Hypothesis (task difficulty and design, D7):** high binary AUCs (0.933 / 0.932 / 0.927) with negative continuous R² are compatible if genotype predicts capability but not rate or magnitude. [src: genotype_to_phenotype_enigma] A within-cohort r=0.964 with cross-cohort LOSO ARI=0.000 is compatible if the canonical axis is cohort-specific. [src: ibd_phage_targeting] And a 27x difference in median partial correlation (0.081 across 183 species versus 0.003 originally) need not mean either estimate is wrong if, as reported, different sampling produced it. [src: ecotype_env_reanalysis] Paper-count inequality (organism Gini 0.967, gene Gini 0.669; 9.2% zero, 46.1% one, 4.3% at least 20 papers) would then be the mechanism that makes literature-weighted evidence non-comparable across targets. [src: paperblast_explorer]

## Resolving Work

**D1 — documented versus actual use.** 
- Execute UC2–UC5 on the live cluster with the same sample-validation protocol applied to UC1, and report which proposed join recipes require correction. [src: berdl_data_atlas]
- Re-run realized-use detection over notebooks and analysis plans rather than READMEs alone, and report the count difference against the original audit. [src: berdl_data_atlas]
- Publish, per bridge, the four evidence states (shared key, overlapping values, executable join, interpretable result) so "documented use" and "use" are separately reportable. [src: berdl_data_atlas]

**D2 — naming versus authority.** 
- Extend the 20-entry / 7-resource resolution to every tenant prefix in the catalog and count namesake collisions of the `kbase.nmdc_neon` kind. [src: nmdc_context_audit]
- Attach a provenance class to each table as a queryable field, then re-test whether any cross-tenant claim depends on a name-only inference. [src: nmdc_context_audit]

**D3 — production versus utilization.** 
- Acquire or annotate consumption actions for the WoM metabolite set and re-evaluate the 19-metabolite Fitness Browser bridge with direction as an explicit variable. [src: webofmicrobes_explorer]
- Resolve the 107 formula-only ModelSEED matches with structure- or InChIKey-level matching and report how many of the 900 candidate molecules survive. [src: webofmicrobes_explorer]
- Test tryptophan as nitrogen source and as a degradation substrate in the 50 *P. fluorescens* strains, to determine whether the 231 significant genes and the complete GapMind pathway correspond to a non-carbon phenotype. [src: fw300_metabolic_consistency]

**D4 — prophage prevalence.** 
- Re-annotate the same genomes with geNomad and VIBRANT and quantify the eggNOG false-positive rate against them. [src: prophage_ecology]
- Re-fit the PERMANOVA with genome size as a covariate, given its dominance (rho=0.717), to test whether the environmental effect still exceeds family-level phylogeny. [src: prophage_ecology]
- Restrict analyses to the 28% of genomes with embeddings as a sensitivity check, and replace genus-level NMDC inference with genome-resolved assignments where available. [src: prophage_ecology]

**D5 — arms race versus coevolution.** 
- Test paired host-defense and phage anti-defense content within the same samples to look for reciprocal change, rather than category enrichment (tail 2.21, head morphogenesis 1.98, anti-defense 1.70) alone. [src: prophage_ecology]
- Re-run the TerL lineage tests with increased power or a different lineage definition, reporting whether any of the 0/500 FDR-corrected results change. [src: prophage_ecology]
- Compare specialist and generalist lineages (325 versus 499 of 824) for differential anti-defense content, which arms-race theory predicts and category-level enrichment does not test. [src: prophage_ecology]

**D6 — pairwise, module, lab, field.** 
- Recompute the co-fitness / co-occurrence relation (rho=-0.109 across 1.04M pairs) stratified by prevalence band, including the auxiliary-only set below 95% prevalence, to isolate the prevalence contribution. [src: cofitness_coinheritance]
- Test module-level co-fitness against module-level co-occurrence directly, to check whether aggregation reverses the negative pairwise sign. [src: cofitness_coinheritance]
- Expand the lab condition panel toward measured field conditions and re-estimate condition-only prediction against the AUC 0.548 / 0.517 / 0.531 baselines. [src: field_vs_lab_fitness]
- Re-test module conservation against field activity with a larger species set, reporting whether rho=0.071, p=0.62 moves. [src: field_vs_lab_fitness]

**D7 — statistics versus warrant.** 
- Re-fit continuous phenotypes with rate-aware targets and report R² against the binary AUCs of 0.933 / 0.932 / 0.927 on the same splits. [src: genotype_to_phenotype_enigma]
- Re-run the IBD CCA under leave-one-study-out validation, so that r=0.964 and LOSO ARI=0.000 are estimated in one framework. [src: ibd_phage_targeting]
- Assay the phage cocktail against strains outside the tested set to convert coverage from tested-strain coverage to measured host range. [src: ibd_phage_targeting]
- Re-design the diagnosis analysis on sub-studies containing both arms, given that 45 sub-studies had at least 10 HC, 5 had at least 10 CD, and 0 had at least 10 of both, and re-derive Tier-A candidates without selection-on-outcome leakage (which cut 33 to 3). [src: pitfalls]
- Re-run the ecotype partial-correlation analysis under matched sampling designs to establish which of 0.081 (183 species) and 0.003 the 27x difference is attributable to. [src: ecotype_env_reanalysis]
- Replace paper count with a coverage-normalized evidence score and re-test any literature-weighted conclusion, given organism Gini 0.967 and gene Gini 0.669 and the 9.2% / 46.1% / 4.3% family distribution. [src: paperblast_explorer]
