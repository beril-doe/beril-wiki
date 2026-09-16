<!-- tension-hash: ee9b5b4acb582310 -->
# Metal cross-resistance: a strong within-fitness signal that no external dataset has yet confirmed, explained, or measured the same way

Gene-level fitness data show metal cross-resistance to be near-universal and directionally conserved, and several projects have tried to check whether that signal shows up outside fitness assays, whether it is metal-specific at all, and how much of it is carried by conserved core genes. Those attempts disagree in three distinct ways, and this page records all three. The first is a **cross-scale validation disagreement**: a species-scale test against isolation-source data returned a null where a pangenome-scale test returned a large effect, and three further studies (groundwater prevalence, soil community ordination, mobile-element gene neighborhoods) added associations that are neither clearly confirmatory nor comparable to one another. The second is a **causal-attribution disagreement**: universal positive cross-resistance is consistent both with genuinely metal-specific mechanisms and with a general-stress response, and the specificity and soil analyses constrain but do not close that gap. The third is a **definitional disagreement**: three projects report core-genome fractions for "metal genes" that differ because they define the gene class differently. This matters because the cross-resistance claim on [[concepts/metal-cross-resistance]] is currently supported almost entirely by one data modality; how these three disagreements resolve determines whether it is a general ecological law, a fitness-assay artifact of shared cellular vulnerability, or something in between.

## Evidence Sides

### Disagreement 1 — does multi-metal fitness breadth predict environmental outcomes?

**Side A: the pangenome-scale validation succeeded.** The prior [[entities/metal-fitness-atlas]] validation reported Cohen's d = +1.0 — Cohen's d being the difference between two group means expressed in standard-deviation units, so +1.0 is a large effect — from pangenome-scale analysis of 42K strains. [src: metal_cross_resistance]

**Side B: the species-scale validation was null.** The species-scale BacDive validation was null, with Spearman rho (a rank-based correlation coefficient) approximately -0.02 and p > 0.8. [src: metal_cross_resistance] The results therefore leave unresolved whether the discrepancy reflects insufficient power and imprecise matching in the species-scale test or a genuine difference between multi-metal fitness signatures and environmental isolation. [src: metal_cross_resistance]

**Side C: groundwater prevalence gives a weak positive, but its targeted test is null.** The MicrobeAtlas groundwater prevalence association (ρ = +0.112, p = 0.0019) supports a weak environmental occurrence relationship, but its null groundwater-specific fold-enrichment test (ρ = +0.042, p = 0.242) does not resolve the BacDive tension. [src: microbeatlas_metal_ecology] The datasets differ in environmental definition, taxonomic aggregation, and outcome, so they should not be combined into a single validation estimate. [src: microbeatlas_metal_ecology]

**Side D: the soil ordination is strong but answers a different question.** The soil analysis adds a related tension: its conditional db-RDA model — distance-based redundancy analysis, an ordination that regresses community dissimilarity on predictors — reports R² = 0.799 and p = 0.005 after conditioning on batch and project effects, whereas the BacDive and groundwater tests address environmental occurrence and isolation rather than residual community functional variance. [src: soil_metal_functional_genomics] These results cannot be treated as convergent effect estimates; the soil signal may partly reflect project structure and has not yet been spatially or effect-size validated. [src: soil_metal_functional_genomics]

**Side E: the mobility-linked association is real but non-comparable.** The T4SS result adds a related observational association rather than resolving this tension: GT2-neighborhood MAGs (metagenome-assembled genomes — genomes reconstructed from environmental sequencing) showed 0.045 versus 0.004 metal-resistance types and an 11× difference in metal-resistance genes, but these data concern syntenic gene neighborhoods and not fitness, isolation, or prevalence outcomes. [src: t4ss_cazy_environmental_hgt] Thus, the new result supports environmental coupling between mobility and resistance breadth while remaining non-comparable to the BacDive, groundwater, and soil effect estimates. [src: t4ss_cazy_environmental_hgt]

### Disagreement 2 — is cross-resistance metal-specific or a general-stress response?

**Side A: the positivity is universal, and its cause is untested.** The report identifies a tension between strong universal positivity and uncertainty about its cause: all tested metal pairs were positive, but no non-metal stress controls were included. [src: metal_cross_resistance] The [[sources/counter_ion_effects__REPORT]] project is identified as partially addressing this issue, but the present study cannot independently separate metal-specific cross-resistance from a general-stress response. [src: metal_cross_resistance]

**Side B: a substantial metal-specific component exists, but general-stress genes remain a large minority.** The specificity analysis supports the existence of a substantial metal-specific component, but also found 38.0% general-sick records and 7.2% metal+stress records, so it does not eliminate the causal ambiguity. [src: metal_specificity]

**Side C: the soil discovery rate may be statistically inflated.** The soil study reinforces this causal tension: its 2,355 discoveries among 3,915 implied tests represent a 60% discovery rate, but positive correlation among co-contaminating metals may make Benjamini–Hochberg FDR correction — the standard procedure for controlling the false discovery rate, the expected share of false positives among significant results — anti-conservative and the true FDR higher than reported. [src: soil_metal_functional_genomics] Effect sizes were not systematically reported, and planned audits will flag associations with rho < 0.05; therefore statistical significance does not yet demonstrate substantial biological effect. [src: soil_metal_functional_genomics]

### Disagreement 3 — how core-enriched are "metal genes"?

**Side A: three-tier analysis.** A further definitional tension is that the three-tier analysis found metal-specific genes to be 89.8% core — "core" meaning present across essentially all genomes of a species' pangenome, as opposed to accessory. [src: metal_cross_resistance, metal_fitness_atlas]

**Side B: the atlas.** The atlas found broad metal-important genes to be 87.4% core versus 76.9% baseline and explicitly attributes much of its signal to general cellular vulnerability. [src: metal_cross_resistance, metal_fitness_atlas] These values should not be reconciled as a single estimate: they use different gene classes, organism sets, and analytical definitions. [src: metal_cross_resistance, metal_fitness_atlas]

**Side C: the specificity analysis.** The specificity analysis adds a third estimate — 84.8% pooled core for metal-specific genes and 90.2% for general sick genes — but likewise uses different inclusion and classification rules, so it refines rather than resolves this tension. [src: metal_specificity]

## Possible Reconciliations

These are hypotheses, not findings; none is established by the evidence above.

- **Scale mismatch (Disagreement 1).** The pangenome-scale and species-scale tests may both be correct if the fitness–environment coupling exists at strain/pangenome resolution and is averaged away when strains are collapsed to species. The input explicitly leaves open "insufficient power and imprecise matching in the species-scale test" as the alternative to "a genuine difference between multi-metal fitness signatures and environmental isolation" [src: metal_cross_resistance].
- **Outcome mismatch (Disagreement 1).** Isolation source, global prevalence, groundwater-specific fold-enrichment, residual community variance, and gene-neighborhood co-occurrence are five different dependent variables. The hypothesis that they measure one underlying quantity is exactly what the sources decline to assume, noting differing "environmental definition, taxonomic aggregation, and outcome" [src: microbeatlas_metal_ecology] and non-comparability of the soil and T4SS outcomes [src: soil_metal_functional_genomics, t4ss_cazy_environmental_hgt].
- **Mixed causal architecture (Disagreement 2).** Both sides could be right if the gene pool is heterogeneous: a metal-specific majority plus a 38.0% general-sick and 7.2% metal+stress remainder [src: metal_specificity] would produce universal positive pair correlations dominated by the shared component while leaving genuine metal-specific mechanisms intact.
- **Significance-without-effect (Disagreement 2).** A high discovery rate under possibly anti-conservative FDR control, with effect sizes unreported [src: soil_metal_functional_genomics], is compatible with a true but small metal-specific effect; the disagreement would then be about magnitude, not existence.
- **Definitional, not empirical (Disagreement 3).** 89.8%, 87.4% and 84.8%/90.2% may all be accurate for their own gene classes, since the sources state the estimates use different gene classes, organism sets, inclusion rules and analytical definitions [src: metal_cross_resistance, metal_fitness_atlas, metal_specificity]. Under this hypothesis the conflict dissolves once the classes are stated side by side — but it cannot be dissolved by averaging them.

## Resolving Work

**Disagreement 1 — cross-scale validation**

- Re-run the BacDive isolation test at the same taxonomic resolution as the 42K-strain pangenome analysis, with a pre-registered power calculation, to determine whether rho ≈ -0.02, p > 0.8 reflects a true null or a resolution/power artifact [src: metal_cross_resistance].
- Harmonize the strain-to-record matching step and report the match rate and its uncertainty, since "imprecise matching" is named as a candidate explanation for the null [src: metal_cross_resistance].
- Fit one model per outcome (isolation source, global prevalence, groundwater fold-enrichment, residual community variance) on a shared taxon set, reporting standardized effect sizes so the +1.0 Cohen's d, ρ = +0.112, and ρ = +0.042 values become comparable rather than pooled [src: metal_cross_resistance, microbeatlas_metal_ecology].
- Validate the soil db-RDA R² = 0.799 with spatial cross-validation and hold-out projects, to separate metal-driven community structure from the batch and project effects it conditions on [src: soil_metal_functional_genomics].
- Test whether the GT2-neighborhood contrast (0.045 vs 0.004 metal-resistance types; 11× metal-resistance genes) predicts any fitness or isolation outcome in the same genomes, which would convert a non-comparable association into a bridging test [src: t4ss_cazy_environmental_hgt].

**Disagreement 2 — metal-specific versus general stress**

- Add non-metal stress controls to the cross-resistance design and recompute pairwise correlations, since their absence is the stated reason the causal question cannot be settled from the present data [src: metal_cross_resistance].
- Recompute the cross-resistance matrix after excluding the 38.0% general-sick and 7.2% metal+stress records, testing whether universal positivity survives on the metal-specific subset alone [src: metal_specificity].
- Integrate the [[sources/counter_ion_effects__REPORT]] design as a formal control arm rather than a partial address, and report how much of the pairwise positivity it accounts for [src: metal_cross_resistance].
- Replace Benjamini–Hochberg with a dependence-robust procedure (or a permutation-based empirical null preserving metal co-contamination structure) and re-report the 2,355/3,915 discovery count under the corrected FDR [src: soil_metal_functional_genomics].
- Execute the planned audits that flag associations with rho < 0.05 and publish the effect-size distribution, so the 60% discovery rate can be partitioned into substantial and negligible effects [src: soil_metal_functional_genomics].

**Disagreement 3 — core-fraction definitions**

- Publish a single definition table stating, for each of the three estimates, the gene class, organism set, pangenome source and core threshold used, so 89.8%, 87.4% and 84.8%/90.2% are read as distinct quantities [src: metal_cross_resistance, metal_fitness_atlas, metal_specificity].
- Recompute all three core fractions on one common organism set and one common core-gene threshold; any residual gap after harmonization is the genuine empirical disagreement.
- Test the atlas's own attribution — that much of its signal reflects general cellular vulnerability [src: metal_cross_resistance, metal_fitness_atlas] — by comparing its broad metal-important class against the specificity project's general-sick class (90.2% pooled core) on shared genomes [src: metal_specificity].
- Report baseline core fractions alongside every metal-gene estimate, since only the atlas contrast currently carries an explicit baseline (87.4% versus 76.9%) [src: metal_cross_resistance, metal_fitness_atlas].
