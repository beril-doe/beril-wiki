<!-- tension-hash: 24b2cb7583cf0497 -->
# Is the environmental signal in microbial genomes real, or an artifact of how it is measured?

Across the corpus, projects that ask whether a genome's environment shapes its gene content keep landing on both sides of the same line: an association is statistically detectable, and it is simultaneously too small, too confounded, or too pipeline-dependent to carry the interpretation placed on it. This page collects that family of disagreements as recorded on [[concepts/environment-embedding-geography]]. Seven blocks are covered: (1) the magnitude of the environment–gene-content partial correlation and whether the competing estimates are even comparable; (2) significant trait–environment associations that fail as predictors; (3) which covariate owns the variance when genome size or species composition is controlled; (4) metal exposure as a conditional multivariate association versus an attributable cause; (5) whether negative out-of-sample prediction is biology or model failure; (6) whether the discovered ecotype labels survive held-out validation; and (7) a set of site- and scale-transfer tensions carried in from individual studies — block 7 is not a single two-sided dispute but a bundle of separate retained tensions, presented one per bolded subsection. The stakes are shared: nearly every downstream claim in this corpus — ecotypes, mobile-element ecology, metal-resistance biogeography — is conditioned on the belief that environmental labels and satellite-derived embeddings (fixed-length numeric vectors summarizing a location's remotely sensed context) index something an organism actually experienced.

## Evidence Sides

### 1. How large is the environment–gene-content partial correlation?

**Side A — the signal is near zero.** Embeddings show clear geographic distance-decay, yet environment similarity had median partial correlation 0.0025 with gene content — a correlation between environment and gene content after removing the contribution of a third variable, here phylogeny. [src: env_embedding_explorer; ecotype_analysis] In the same analysis the phylogenetic median was 0.0143 against an environmental median of 0.0025, i.e. relatedness outweighed environment. [src: ecotype_env_reanalysis; ecotype_analysis]

**Side B — the reanalysis medians are much larger, and clinical bias does not explain them away.** The environmental-only reanalysis found median 0.051 for environmental species versus 0.084 for human-associated species, U=1536, p=0.83 (Mann–Whitney U, a rank-based two-group test), and a median of 0.081 across all 183 species. [src: ecotype_env_reanalysis; ecotype_analysis] Stated against the original figure, 0.0025 for the original environment measure versus 0.081 across all 183 species is a direct disagreement in absolute effect size. [src: ecotype_analysis; ecotype_env_reanalysis]

**Side C — the two numbers are not commensurable.** These estimates cannot be reconciled by averaging: the studies used different genome sets, species filters, and downsampling. [src: ecotype_env_reanalysis; env_embedding_explorer] The discrepancy is attributed to different genome sets, full-genome extraction, and downsampling procedures. [src: ecotype_env_reanalysis]

**Side D — the environmental variable itself is contested.** The structured `env_broad_scale` field is cleaner but covers only 42%; keyword `isolation_source` harmonization covers 71% of genomes with a label but leaves 17% Other and 12.5% Unknown. [src: env_embedding_explorer] Coordinates add a parallel tension because distance-decay may reflect environmental context, epidemiological structure, institutional clustering, or approximate coordinates. [src: env_embedding_explorer; ecotype_env_reanalysis] Under Side D, both A and B may be measuring different mixtures of ecology and sampling logistics.

### 2. Statistically significant trait–environment associations that do not predict

**Side A — the associations are real.** *Pseudomonas* carbon profiles were environmentally associated (p=0.006). [src: pseudomonas_carbon_ecology] Polyhydroxybutyrate (PHB, a bacterial carbon-storage polymer) showed a raw breadth association rho=0.106, p=1.77×10^-06 (Spearman rank correlation). [src: phb_granule_ecology] The SNIPE defense system was statistically detectable in 22/64 AlphaEarth dimensions. [src: snipe_defense_system]

**Side B — the same analyses are weak as predictors or reverse under control.** For *Pseudomonas*, balanced accuracy was 0.408 +/- 0.169 (mean per-class recall) and PCA primarily separated *Pseudomonas* s.s. from *Pseudomonas*_E — taxonomy, not environment. [src: pseudomonas_carbon_ecology] For PHB, the genome-size-controlled partial rho=-0.047, p=0.037 reverses sign relative to the raw association. [src: phb_granule_ecology] For SNIPE, the largest effect was d=0.26 (Cohen's d, a standardized mean difference), AlphaEarth covered only 28.4% of genomes, and no dimension had a biological interpretation. [src: snipe_defense_system]

### 3. Which covariate owns the variance: environment, genome size, or species composition?

**Side A — environment survives conditioning.** Prophage module effects remained significant within genome-size quartiles. [src: prophage_ecology] Plant-associated mobilome burden was higher (3.7 versus 2.8). [src: plant_microbiome_ecotypes]

**Side B — the dominant term is something else, and refinement collapses the estimate.** Genome size dominated PERMANOVA (permutational multivariate analysis of variance on a distance matrix) with F=212.99; prophage calls were annotation-based, only 28% of genomes had embeddings, and NMDC burden was genus-inferred. [src: prophage_ecology] Plant compartment PERMANOVA had refined R²=0.071, while the earlier R²=0.527 collapsed to 0.072 after removing genome-rich species — a loss attributable to sampling composition. [src: plant_microbiome_ecotypes] In the same project, marker singletons were depleted (enrichment ratio 0.78) and corrected complementarity was negative (d≈-0.4), pointing opposite to the mobilome-burden result. [src: plant_microbiome_ecotypes]

**Side C — mobility versus lineage, within prophages.** Human-associated module enrichments contrasted with 0/500 significant TerL-lineage (large terminase subunit, used here to define phage lineages) enrichments, supporting modular exchange but not independent adaptation of complete phage lineages. [src: prophage_ecology] A parallel pattern appears for SNIPE: its 86.7% accessory-plus-singleton distribution supports mobile defense-island turnover, but only 54/4,572 DUF4041 clusters carried Mug113 and DUF4041 (a domain of unknown function) can occur outside SNIPE. [src: snipe_defense_system]

### 4. Metal exposure: strong conditional association versus uncertain attribution

**Side A — a strong multivariate association.** The soil-metal study reports conditional db-RDA (distance-based redundancy analysis, an ordination regressing a community distance matrix on predictors) R²=0.799, p=0.005. [src: soil_metal_functional_genomics] A global survey found β=+0.021, p=1.5×10^-4 in MicrobeAtlas. [src: microbeatlas_metal_ecology]

**Side B — attribution is unresolved and the effect is fragile to specification.** In the soil-metal study the unconditional metal-only R² was not reported; chromium, copper, lead, and zinc co-vary, the 60% discovery rate may be inflated by correlated tests, and proximity within 10 km does not guarantee co-location. [src: soil_metal_functional_genomics] In MicrobeAtlas, strict prevalence gave p=0.092 and groundwater-specific fold enrichment was null (rho=+0.042, p=0.242). [src: microbeatlas_metal_ecology]

### 5. Negative out-of-sample R²: biological unpredictability or model failure?

**Side A — the null is informative.** The soil-frontier models all had negative out-of-sample R² (cross-validated variance explained; negative means worse than predicting the training mean) and a low- versus high-clay difference of 0.024 with 95% CI [-0.423, 0.161], supporting the conclusion that the clay shield was not demonstrated globally. [src: soil_frontier_genomics]

**Side B — the null cannot bear that reading.** This **contradicts** treating negative prediction as evidence of genuine biological unpredictability because spatial distributional shift, outlier leverage, and model failure were not separated. [src: soil_frontier_genomics] The accompanying ranking is equally fragile: Forest GDI=902.36 and cropland GDI=890.82 were jointly highest, but the 1.3% difference lacks bootstrap confidence intervals and GDI can be high when completeness is zero. [src: soil_frontier_genomics]

### 6. Do the discovered ecotypes survive validation?

**Side A — a clustering solution with a candidate list.** The pitfalls audit found K=4 LDA ecotypes (latent Dirichlet allocation, a mixture model assigning genomes fractional membership in latent classes) with a 33-species Tier-A list. [src: pitfalls]

**Side B — the list does not replicate.** Held-out-species Jaccard values (set overlap, 0 to 1) were 0.230 for E1 and 0.064 for E3, and independent within-substudy evidence reduced the list to 3 candidates. [src: pitfalls] This **contradicts** treating the unvalidated list as stable and supports held-out-feature clustering and independent validation.

### 7. Site-scale and scale-transfer tensions carried in

The ecological-agora, ENIGMA, Harvard Forest, Oak Ridge, and lanthanide results retain their respective tensions. [src: gene_function_ecological_agora; genotype_to_phenotype_enigma; harvard_forest_warming; lab_field_ecology; lanthanide_methylotrophy_atlas] Each is a separate disagreement between a reported pattern and the scale at which it is being read; they are listed individually rather than as two opposed sides.

**Alignment versus causation.** Cluster alignment is not causal. [src: gene_function_ecological_agora]

**Global versus site-specific sampling.** Global *Pseudomonas* representation differs from ENIGMA's environmental clade. [src: genotype_to_phenotype_enigma]

**Main effect versus interaction.** Treatment alone explained 7.6% (p=0.069) versus treatment × horizon 41%. [src: harvard_forest_warming]

**Laboratory versus field.** Laboratory metal tolerance was non-significant in field abundance. [src: lab_field_ecology]

**Nominal enrichment versus multiple-testing control and sample depth.** REE-impacted samples did not pass FDR (false discovery rate, the expected fraction of false positives among calls declared significant) while REE-AMD contained only 37 MAGs (metagenome-assembled genomes). [src: lanthanide_methylotrophy_atlas]

## Possible Reconciliations

These are hypotheses, not findings; none is established by the evidence above.

- **Estimator scope, not biology (blocks 1, 3).** If diversity-maximizing downsampling in one pipeline removes exactly the near-duplicate genomes that share both environment and gene content, the low and high medians could both be correct estimates of *different* estimands — within-species environmental structure after de-replication versus with it. The explicit attribution to genome sets, full-genome extraction, and downsampling is consistent with this. [src: ecotype_env_reanalysis] The plant-compartment collapse from 0.527 to 0.072 on removing genome-rich species is the same mechanism observed directly. [src: plant_microbiome_ecotypes]
- **Two different variables share one name (block 1).** A structured 42%-coverage field and a keyword harmonization leaving 17% Other and 12.5% Unknown are unlikely to behave identically; "environment similarity" may denote a cleaner, sparser variable in one study and a noisier, denser one in the other. [src: env_embedding_explorer]
- **Detectable ≠ predictive (block 2).** Association tests and classifiers answer different questions; p=0.006 alongside balanced accuracy 0.408 +/- 0.169 is internally consistent if the environmental effect is real but far smaller than within-class variance. [src: pseudomonas_carbon_ecology] Both sides could then be right, with the disagreement being about which statistic licenses an ecological claim.
- **Genome size as mediator versus confounder (blocks 2, 3).** If environment selects genome size and genome size determines prophage or PHB content, conditioning on genome size removes real environmental signal; if genome size is a purely technical covariate, conditioning is mandatory. The PHB sign reversal (rho=0.106 raw, partial rho=-0.047) is the signature of this ambiguity and does not by itself distinguish the two. [src: phb_granule_ecology]
- **Mobility without lineage adaptation (block 3).** Modular enrichment alongside 0/500 significant TerL-lineage enrichments is reconcilable if the unit of ecological selection is the gene module, not the phage genome. [src: prophage_ecology]
- **Exposure proxy versus exposure (block 4).** A conditional db-RDA R²=0.799 and a null groundwater-specific enrichment (rho=+0.042, p=0.242) can coexist if the multivariate model captures a site-level covariate bundle while the habitat-specific test targets metal exposure itself; the unreported unconditional metal-only R² is precisely the quantity that would separate them. [src: soil_metal_functional_genomics; microbeatlas_metal_ecology]
- **Model failure masquerading as a null (block 5).** Spatial distributional shift between train and test folds would produce negative R² regardless of whether the underlying biology is predictable, making Side A's null and Side B's objection compatible. [src: soil_frontier_genomics]
- **Scale mismatch (blocks 6, 7).** Clusters learned globally need not label local populations; treatment × horizon at 41% versus treatment alone at 7.6% (p=0.069) suggests environmental effects that exist only in interaction with local structure, which would also explain low held-out Jaccard for ecotype membership. [src: harvard_forest_warming; pitfalls]

## Resolving Work

**Block 1 — partial-correlation magnitude**
- Recompute both partial correlations on a single frozen genome set with identical species filters, then vary one factor at a time (downsampling on/off, full-genome versus subsetted extraction) to decompose the gap between 0.0025 and 0.081 into per-choice contributions. [src: ecotype_analysis; ecotype_env_reanalysis]
- Re-run the environmental-versus-human comparison (currently U=1536, p=0.83) on the no-downsampling and downsampled pipelines in parallel to test whether the null direction is itself pipeline-dependent. [src: ecotype_env_reanalysis]
- Restrict all estimates to genomes with a structured `env_broad_scale` label (42% coverage) and compare against the keyword-harmonized set (71% labelled, 17% Other, 12.5% Unknown) to price the metadata-quality contribution. [src: env_embedding_explorer]
- Partition coordinate-based distance-decay by submitting institution and collection year to test the epidemiological/institutional-clustering alternative against the environmental-context reading. [src: env_embedding_explorer; ecotype_env_reanalysis]

**Block 2 — significance versus prediction**
- Report classifier performance and association p-values together for every trait, with per-class confusion matrices and the applicable chance baseline, so that results like p=0.006 with balanced accuracy 0.408 +/- 0.169 are interpreted jointly rather than selectively. [src: pseudomonas_carbon_ecology]
- Test the *Pseudomonas* environmental association within *Pseudomonas* s.s. and *Pseudomonas*_E separately, since PCA separated those clades first; a within-clade association would rule out taxonomy as the driver. [src: pseudomonas_carbon_ecology]
- Fit PHB breadth against environment with genome size entered as mediator in a path model rather than as a covariate, to distinguish the rho=0.106 and partial rho=-0.047 readings. [src: phb_granule_ecology]
- Provide a biological annotation for the 22/64 informative AlphaEarth dimensions (land-cover or climate correlates) before any d=0.26 effect is interpreted ecologically, and re-test as embedding coverage rises above the current 28.4% of genomes. [src: snipe_defense_system]

**Block 3 — variance ownership**
- Re-run the prophage PERMANOVA with genome size as a continuous covariate partialled out rather than quartile-blocked, and report environment's marginal R² against the F=212.99 genome-size term. [src: prophage_ecology]
- Replace annotation-based prophage calls with assembly-level prophage boundary detection on a matched subset, and replace genus-inferred NMDC burden with sample-level calls, to test whether the environment term survives better data. [src: prophage_ecology]
- Recompute plant compartment PERMANOVA under several species-rarefaction depths to establish whether R²=0.071/0.072 is the stable estimate and 0.527 was purely a genome-rich-species artifact. [src: plant_microbiome_ecotypes]
- Reconcile the higher mobilome burden (3.7 versus 2.8) with depleted marker singletons (0.78) and negative corrected complementarity (d≈-0.4) by testing whether mobile elements in plant-associated genomes carry redundant rather than novel functions. [src: plant_microbiome_ecotypes]
- Test SNIPE mobility directly by comparing flanking-region synteny for the 54/4,572 DUF4041 clusters carrying Mug113 against DUF4041 clusters lacking it. [src: snipe_defense_system]

**Block 4 — metal attribution**
- Report the unconditional metal-only db-RDA R² alongside the conditional R²=0.799, p=0.005; the gap is the quantity currently missing from the attribution argument. [src: soil_metal_functional_genomics]
- Apply variance partitioning across chromium, copper, lead, and zinc, and re-estimate the 60% discovery rate under a dependence-aware multiple-testing correction. [src: soil_metal_functional_genomics]
- Re-run the analysis at tightened co-location thresholds below 10 km and report the effect's sensitivity to that radius. [src: soil_metal_functional_genomics]
- Reconcile β=+0.021, p=1.5×10^-4 with the strict-prevalence p=0.092 by reporting both under a common prevalence definition, and test whether the null groundwater result (rho=+0.042, p=0.242) is habitat-specific biology or a power limitation. [src: microbeatlas_metal_ecology]

**Block 5 — negative prediction**
- Separate the three candidate causes of negative out-of-sample R² with spatially blocked cross-validation, leverage/outlier diagnostics, and a learning-curve analysis, reporting which one moves the low- versus high-clay difference of 0.024 [95% CI: -0.423, 0.161]. [src: soil_frontier_genomics]
- Attach bootstrap confidence intervals to GDI before Forest (902.36) and cropland (890.82) are ranked against each other on a 1.3% difference. [src: soil_frontier_genomics]
- Recompute GDI with a completeness floor, since GDI can be high when completeness is zero, and report how the biome ranking changes. [src: soil_frontier_genomics]

**Blocks 6 and 7 — validation and scale transfer**
- Repeat the K=4 LDA solution under held-out-feature clustering and report held-out Jaccard for every ecotype alongside the current 0.230 (E1) and 0.064 (E3). [src: pitfalls]
- Treat the 3 independently supported candidates, not the 33-species Tier-A list, as the validation target, and pre-register the evidence required to promote a species back onto the list. [src: pitfalls]
- Test whether ENIGMA's environmental clade is recovered when global *Pseudomonas* sampling is restricted to comparable habitats, which would distinguish clade-specific biology from representation bias. [src: genotype_to_phenotype_enigma]
- Re-fit the warming analysis with horizon as a stratifying variable and report treatment effects within horizon, since treatment alone explained 7.6% (p=0.069) versus treatment × horizon 41%. [src: harvard_forest_warming]
- Pair laboratory metal tolerance assays with field abundance for the same strains at the same sites, since laboratory tolerance was non-significant in field abundance. [src: lab_field_ecology]
- Expand the REE-AMD MAG set beyond 37 and re-test REE-impacted samples under FDR control before any lanthanide enrichment claim is made. [src: lanthanide_methylotrophy_atlas]
- Specify the causal model behind the reported cluster alignment and test it against a permutation null, since cluster alignment is not causal. [src: gene_function_ecological_agora]
