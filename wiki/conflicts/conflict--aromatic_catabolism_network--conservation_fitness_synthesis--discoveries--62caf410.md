<!-- tension-hash: 3dc5da494f7d3b62 -->
# Conserved or conditional: competing accounts of what makes a gene or pathway matter

This page collects the disagreements recorded under `## Tensions` on [[concepts/condition-specific-fitness]], where the corpus repeatedly splits over the same underlying question: when a gene or pathway is *used* or *needed* in a particular condition, does that show up as higher evolutionary conservation, and is the association real or an artifact of scope, denominator, and control? Eight distinct disagreements appear in that text — (1) pathway-level versus gene-level conservation of active dependencies, (2) pathway variability versus pangenome openness as predictors, (3) three incompatible core-gene fractions for metal-important genes, (4) whether unannotated "dark" genes are stress-enriched, (5) whether environmental structure in genomes survives phylogenetic and neutral controls, (6) whether the ADP1 respiratory-chain wiring model generalizes, (7) whether essentiality is universal or context-bounded, and (8) within-study association versus cross-cohort reproducibility in IBD metabolomics. All eight are covered below; none are deferred. Several are explicitly *not* measurement contradictions but definitional or scope mismatches, and the sections below preserve that distinction rather than forcing every pair into a winner-and-loser frame.

## Evidence Sides

### 1. Do actively-required pathways look more conserved than latent ones?

**Pathway-level: no conservation advantage for active dependencies.** Latent complete pathways had mean conservation 0.869 versus 0.829 for active dependencies, and the active-greater-than-latent comparison was not significant (p = 0.94) — that is, the pathways an organism *has but does not need* in the assayed conditions were, if anything, the more conserved set. [src: metabolic_capability_dependency; conservation_fitness_synthesis; fitness_effects_conservation; essential_genome]

**Gene-level: importance tracks conservation.** Gene-level analyses associate essentiality and strong fitness effects with higher core fractions — the core fraction being the share of a gene set classified as core rather than accessory. [src: metabolic_capability_dependency; conservation_fitness_synthesis; fitness_effects_conservation; essential_genome]

**A third measurement, in the same direction as the gene-level view but compressed.** A newer 7-organism analysis found mean core gene completeness of 0.986 for Active Dependencies versus 0.975 for Latent Capabilities — the ordering the gene-level view predicts — but its model-organism coverage and near-complete genomes compress the comparison, leaving little dynamic range in which a difference could appear. [src: pathway_capability_dependency]

**A candidate tiebreaker that does not break the tie.** The NMDC negative leucine and arginine associations do not resolve this tension, because GapMind (which infers pathway potential from genome sequence) measures genomic potential, not expression or essentiality, and abiotic controls were unavailable. [src: nmdc_community_metabolic_ecology]

### 2. Does genomic variability predict pangenome openness?

**Positive: pathway variability predicts openness.** Variable pathway count was positively associated with pangenome openness after genome-count control (rho = 0.530, p = 2.83e-203), where rho is the Spearman rank correlation. [src: pathway_capability_dependency; pangenome_openness]

**Null: broader predictors show nothing.** Broader pangenome analyses reported null relationships between openness and environment or phylogeny effect sizes. [src: pathway_capability_dependency; pangenome_openness]

The source tension itself grades this as a refinement rather than a resolution: pathway variability is a narrower predictor than environment or phylogeny, and the new analysis did not compute full phylogenetic independent contrasts — the correction that removes correlation induced purely by shared ancestry. [src: pathway_capability_dependency; pangenome_openness]

### 3. What fraction of metal-important genes is core?

**High, versus a lower baseline.** The metal atlas found 87.4% core among broad metal-important genes versus 76.9% baseline. [src: metal_fitness_atlas]

**Low.** The DvH condition-specific heavy-metal result — from the field-versus-lab comparison — found 71.2% core, below even the atlas baseline. [src: field_vs_lab_fitness]

**Inverted.** The metal-specificity analysis found 84.8% pooled core for metal-specific genes and 90.2% for general sick genes, i.e. the *less* metal-specific set was the more conserved one. [src: metal_specificity]

Definitions, organism coverage, general-stress capture, and exclusion of putatively essential genes differ across the three. [src: metal_fitness_atlas; field_vs_lab_fitness; metal_specificity]

### 4. Are unannotated genes stress-enriched?

**Depleted for stress, relative to annotation-lag genes.** Stress represented 28.7% versus 43.2% of strong phenotypes for truly dark versus annotation-lag genes (OR = 0.53, p < 0.001; OR is the odds ratio). [src: truly_dark_genes]

**Yet condition-important.** The same truly-dark analysis identified genes that became important in selected nutrient, stress, iron, community, or rich-media contexts. [src: truly_dark_genes]

The source tension is explicit that this is not a contradiction in measurement: the census compares condition *distributions* among dark-gene classes, whereas the other analyses test whether individual genes or pathways matter under selected conditions. [src: truly_dark_genes]

### 5. Is environmental structure in genomes real or a control artifact?

**Raw signal is near-universal; controlled signal is small.** 94.2% of 5,671 eggNOG ortholog groups (groups of orthologous genes defined in the eggNOG database) were significant in raw plant-versus-non-plant tests, but only 50 retained enrichment after phylum-level control, and compartment separation explained only 0.060 of variance by db-RDA — distance-based redundancy analysis, an ordination that partitions distance-matrix variance among predictors. [src: plant_microbiome_ecotypes]

**A classification that fails its own negative controls.** The 78.7% refined dual-nature classification conflicted with its four-of-four neutral-control failures. [src: plant_microbiome_ecotypes]

**An independent case with the same shape.** The SNIPE result similarly found 22 of 64 AlphaEarth environmental-embedding dimensions significant but a largest Cohen's d of 0.26 (the standardized mean difference between groups) and geographic metadata for only 28.4% of genomes. [src: snipe_defense_system]

Together these support statistically detectable but modest environmental structure rather than direct habitat or causal-fitness measurement. [src: plant_microbiome_ecotypes; snipe_defense_system]

### 6. Does the ADP1 respiratory-chain model generalize?

**Mechanistic reading from stoichiometry.** Aromatic analysis and respiratory-chain studies associate quinate with greater Complex I (NADH dehydrogenase) dependence despite lower total NADH yield, but the interpretation relies on theoretical stoichiometry and inferred capacity limits. [src: aromatic_catabolism_network; discoveries; respiratory_chain_wiring]

**Constraint model disagrees.** FBA — flux balance analysis, a constraint-based steady-state model of metabolic flux — predicts zero flux through the alternative NADH dehydrogenase NDH-2 and ACIAD3522 on standard media. [src: aromatic_catabolism_network; discoveries; respiratory_chain_wiring]

**Cross-species test, underpowered.** The cross-species test found 5 of 14 organisms with validated NDH-2, whose mean Complex I aromatic deficit was −0.297 versus −0.156 without validated NDH-2; p = 0.52, with only 4 organisms lacking NDH-2. ADP1 wiring may therefore be species-specific, and the comparison is underpowered and vulnerable to annotation errors. [src: aromatic_catabolism_network; discoveries; respiratory_chain_wiring]

### 7. Is essentiality universal or bounded by genomic context?

**Essential across every organism in the panel: 15 families.** Only 15 essential families were essential in all 48 organisms. [src: essential_genome]

**Essential wherever present: 859 families.** 859 ortholog families were universally essential within every organism in which they occurred. [src: essential_genome]

The source tension grades this as a refinement of, not a contradiction to, the condition-specific interpretation: genomic context, paralogs, alternative pathways, and compensation affect essentiality. [src: essential_genome]

### 8. Strong association within a study, none across studies

**Near-perfect within-pilot association.** The IBD within-pilot taxonomy–metabolite CCA axis (canonical correlation analysis, which finds paired axes maximizing correlation between two data tables) had r = 0.964. [src: ibd_phage_targeting]

**Zero to near-zero cross-cohort reproducibility.** Pooled metabolomics had cross-cohort LOSO ARI = 0.000 and the ecotype framework had mean LOSO ARI = 0.113, where LOSO is leave-one-study-out validation and ARI is the adjusted Rand index, a chance-corrected measure of agreement between cluster assignments. [src: ibd_phage_targeting]

These measure within-pilot association versus cross-cohort reproducibility. [src: ibd_phage_targeting]

## Possible Reconciliations

Each of the following is a **hypothesis** — a way both sides could be correct — not a finding this corpus has established.

**Unit-of-selection mismatch (disagreements 1 and 7).** Hypothesis: conservation is a property of genes, while activity and latency are properties of pathways, and a pathway can be retained intact by selection acting on a subset of its genes in conditions never assayed. Under this hypothesis the pathway-level null (0.869 vs 0.829, p = 0.94) and the gene-level positive association are both true statements about different units. [src: metabolic_capability_dependency; conservation_fitness_synthesis; fitness_effects_conservation; essential_genome] A parallel hypothesis covers disagreement 7: the "15 in all 48" denominator is the union of organisms, the "859 within every organism in which they occurred" denominator is presence-conditioned, and gene loss rather than dispensability drives the gap. [src: essential_genome]

**Ceiling compression (disagreement 1).** Hypothesis: the 7-organism comparison (0.986 vs 0.975) sits so close to complete conservation that its ordering agrees with the gene-level view by construction, and the wider pathway-level comparison is the only one with room to show a null. The source itself flags model-organism coverage and near-complete genomes as the compressing factor. [src: pathway_capability_dependency]

**Predictor granularity (disagreement 2).** Hypothesis: environment and phylogeny are coarse proxies that average over the specific axis — pathway variability — that actually drives openness, so a strong narrow correlation (rho = 0.530) and null broad correlations coexist. The competing hypothesis is that the narrow correlation is phylogenetic pseudo-replication that independent contrasts would erase. [src: pathway_capability_dependency; pangenome_openness]

**Definitional divergence (disagreement 3).** Hypothesis: the three metal core fractions (87.4%/76.9%, 71.2%, 84.8%/90.2%) are not estimates of one quantity. "Metal-important", "condition-specific heavy-metal", and "metal-specific versus general sick" pick out nested or disjoint gene sets; excluding putatively essential genes removes exactly the most-core tail, which alone could invert an ordering. Dose relative to toxicity threshold may also differ, so that one assay measures general stress response and another measures metal handling. [src: metal_fitness_atlas; field_vs_lab_fitness; metal_specificity]

**Numerator versus indicator (disagreement 4).** Hypothesis: truly dark genes are stress-*depleted as a share of their own strong phenotypes* while still containing stress-important genes in absolute number; a shifted condition distribution is compatible with a long list of condition-important members. The source's own framing — distribution census versus per-gene tests — supports this reading. [src: truly_dark_genes]

**Signal real but small (disagreement 5).** Hypothesis: environmental structure exists and is genuinely detectable (22 of 64 AlphaEarth dimensions significant), but its magnitude (0.060 of variance; largest Cohen's d of 0.26) is below what habitat-assignment or fitness claims require, and phylum-level confounding accounts for the gap between the uncontrolled result (94.2% of 5,671 groups significant) and the 50 groups that survive phylum-level control. The four-of-four neutral-control failures are, on this hypothesis, the honest signal that the 78.7% classification is not yet a measurement. [src: plant_microbiome_ecotypes; snipe_defense_system]

**Scope of the model, not its correctness (disagreement 6).** Hypothesis: ADP1's quinate-associated Complex I dependence is real and species-specific, while FBA's zero-flux prediction for NDH-2 and ACIAD3522 reflects standard-media constraints rather than the aromatic conditions where the dependence appears; the 5-versus-4 organism split (−0.297 vs −0.156, p = 0.52) is simply too small to distinguish "no effect" from "effect the study cannot see". [src: aromatic_catabolism_network; discoveries; respiratory_chain_wiring]

**Batch structure as the dominant axis (disagreement 8).** Hypothesis: r = 0.964 within a pilot and LOSO ARI = 0.000 across cohorts are both correct because cohort-level technical and population variation exceeds the biological covariance that CCA fits within a pilot. The ecotype framework's mean LOSO ARI = 0.113 would then mark a small genuinely transferable component rather than a failed replication of the 0.964 result. [src: ibd_phage_targeting]

## Resolving Work

**1. Pathway versus gene conservation**
- Recompute active/latent pathway conservation with the pathway's *member genes* as the unit, so the pathway-level and gene-level analyses share one denominator and one conservation statistic; ask whether the 0.869/0.829 ordering survives. [src: metabolic_capability_dependency; conservation_fitness_synthesis; fitness_effects_conservation; essential_genome]
- Repeat the 7-organism Active-versus-Latent comparison (0.986 vs 0.975) on a genome set deliberately spanning draft-quality and non-model taxa, to test whether the ordering is an artifact of near-complete genomes. [src: pathway_capability_dependency]
- Stratify both comparisons by pathway size and by number of alternative routes, since a latent pathway with no alternative may be retained for reasons unrelated to assayed fitness. [src: metabolic_capability_dependency; pathway_capability_dependency]
- Pair GapMind pathway calls with expression or mutant-fitness data in the same samples, which is the measurement the NMDC leucine/arginine associations lacked, plus abiotic controls. [src: nmdc_community_metabolic_ecology]

**2. Pathway variability versus pangenome openness**
- Recompute the variable-pathway-count/openness association (rho = 0.530) under full phylogenetic independent contrasts, the step the source flags as missing. [src: pathway_capability_dependency; pangenome_openness]
- Regress openness jointly on pathway variability, environment, and phylogeny effect size in one model, to see whether the narrow predictor survives conditioning on the ones that were null. [src: pathway_capability_dependency; pangenome_openness]
- Re-run with genome count both controlled and stratified, since sampling depth is the standard driver of apparent openness. [src: pathway_capability_dependency; pangenome_openness]
- Test whether the association holds within individual phyla, where shared-ancestry inflation is minimized. [src: pathway_capability_dependency; pangenome_openness]

**3. Metal core fractions**
- Apply a single shared metal-specific gene definition across the atlas, DvH, and metal-specificity datasets and recompute all core fractions (87.4%/76.9%, 71.2%, 84.8%/90.2%) under it — the resolving step named in the source tension. [src: metal_fitness_atlas; field_vs_lab_fitness; metal_specificity]
- Add non-metal stress controls so that general stress response can be subtracted rather than assumed absent. [src: metal_fitness_atlas; field_vs_lab_fitness; metal_specificity]
- Normalize dose relative to MIC (minimum inhibitory concentration) per organism per metal, so "heavy-metal condition" means the same physiological severity everywhere. [src: metal_fitness_atlas; field_vs_lab_fitness; metal_specificity]
- Report each fraction with and without putatively essential genes excluded, since that exclusion plausibly explains the 90.2%-versus-84.8% inversion. [src: metal_specificity]
- Apply phylogenetic contrasts to the cross-organism pooling. [src: metal_fitness_atlas; field_vs_lab_fitness; metal_specificity]

**4. Dark-gene stress enrichment**
- Test matched truly-dark and annotation-lag genes across the same condition matrix, with controls for length, insertion density, organism, and polar effects — the design named in the source tension. [src: truly_dark_genes]
- Report both the share-of-phenotypes statistic (28.7% vs 43.2%, OR = 0.53) and per-gene hit rates, so the census and per-gene framings are visible side by side. [src: truly_dark_genes]
- Balance the condition matrix across nutrient, stress, iron, community, and rich-media categories, so the denominator of "strong phenotypes" is not set by assay availability. [src: truly_dark_genes]

**5. Environmental structure under controls**
- Re-run the plant-versus-non-plant enrichment with phylum-level control applied from the start and report only the controlled count, treating the 94.2%-of-5,671 raw figure as a diagnostic of confounding rather than a result. [src: plant_microbiome_ecotypes]
- Diagnose the four-of-four neutral-control failures before any further use of the 78.7% dual-nature classification; a classifier that fails its negative controls cannot be validated by adding data. [src: plant_microbiome_ecotypes]
- Fit the AlphaEarth dimension tests on the 28.4%-covered subset versus a metadata-imputed or coverage-matched comparison set, to estimate how much of the 22-of-64 result is isolation-source bias. [src: snipe_defense_system]
- Power-analyze what effect size — against the largest Cohen's d of 0.26 and the 0.060 of variance explained by db-RDA — would be required to support a habitat-assignment claim, and state that threshold before collecting more genomes. [src: snipe_defense_system; plant_microbiome_ecotypes]

**6. Respiratory-chain generalization**
- Measure NDH-2 and ACIAD3522 flux directly on aromatic substrates including quinate, rather than inferring it from standard-media FBA, since the model's zero-flux prediction is media-conditioned. [src: aromatic_catabolism_network; discoveries; respiratory_chain_wiring]
- Expand the cross-species panel well beyond 14 organisms, with validated NDH-2 status, to give the −0.297-versus−0.156 comparison (p = 0.52) usable power. [src: aromatic_catabolism_network; discoveries; respiratory_chain_wiring]
- Re-verify NDH-2 presence/absence calls by experiment or curated orthology, since the source flags annotation error as a live vulnerability in the 5-versus-4 split. [src: aromatic_catabolism_network; discoveries; respiratory_chain_wiring]
- Test the Complex I aromatic deficit in ADP1 under matched NADH-yield conditions across substrates, separating yield effects from wiring effects. [src: aromatic_catabolism_network; discoveries; respiratory_chain_wiring]

**7. Universality of essentiality**
- Report essential-family counts against both denominators explicitly — all 48 organisms versus presence-conditioned — whenever essentiality breadth is cited, since 15 and 859 are answers to different questions. [src: essential_genome]
- For the families essential where present but absent elsewhere, test whether the absent organisms carry paralogs or alternative pathways, which is the compensation mechanism the source names. [src: essential_genome]
- Cross-check a sample of the 859 families in organisms where they are present but were not assayed, to confirm the presence-conditioned claim is not an artifact of which organisms were screened. [src: essential_genome]

**8. Within-pilot versus cross-cohort signal**
- Re-fit the taxonomy–metabolite CCA within each cohort separately and report the distribution of axis correlations against the r = 0.964 pilot value, to see whether the within-study association itself replicates. [src: ibd_phage_targeting]
- Apply cohort-level batch correction before pooling, then recompute LOSO ARI to test whether the 0.000 value reflects biology or platform effects. [src: ibd_phage_targeting]
- Compare the ecotype framework's mean LOSO ARI = 0.113 against a permutation null to establish whether it is distinguishable from zero at all. [src: ibd_phage_targeting]
- Pre-register cross-cohort reproducibility, not within-cohort association, as the endpoint for any clinical or mechanistic claim built on these data. [src: ibd_phage_targeting]
