<!-- tension-hash: 4df6a4843fa3777d -->
# Trait Signal vs. Lineage and Sampling: When Do Phenotype and Environment Effects Survive Their Controls?

Five projects in this corpus report associations between microbial traits or environments and some outcome — metal tolerance, gene content, functional profile, niche breadth. In most of them a control (taxonomic covariates, phylogenetic adjustment, removal of over-sampled genomes, or stricter prevalence filtering) either erases the association or sharply weakens it; in one — the ecotype-functional study — the decisive phylogenetic control was never applied at all, so its effect stands untested rather than tested and diminished. The disagreement is not "signal vs. no signal" in a single dataset; it is a recurring split between analyses that detect a trait or environment effect and analyses that attribute the same effect to lineage structure or to uneven database sampling. Because the two readings imply opposite next steps — mechanistic follow-up versus sampling repair — the corpus cannot be summarized as supporting either one. This page records five distinct disagreements drawn from [[concepts/phenotype-database-coverage-bias]], which also touches [[concepts/condition-specific-fitness]]. It uses only the figures cited on that page; it does not attempt to arbitrate.

## Evidence Sides

### Disagreement 1 — Phenotype features: broadly significant, or redundant with taxonomy?

**Side A: the phenotype associations are real and widespread.** Seven of ten phenotype features were significant after FDR correction — FDR (false discovery rate) correction being the adjustment that controls the expected share of false positives among the calls declared significant — and phenotype features alone explained 16.3% of variance. [src: bacdive_phenotype_metal_tolerance]

**Side B: the phenotypes add no independent predictive information.** Taxonomy alone explained 35.4% of variance, and adding phenotype features to taxonomy reduced the model to R² = 0.345 (R² being the fraction of outcome variance a model accounts for). [src: bacdive_phenotype_metal_tolerance] This is a tension between widespread univariate significance and limited evidence that the phenotypes add independent predictive information after taxonomic structure is accounted for. [src: bacdive_phenotype_metal_tolerance] The Gram-stain case shows the shape of the problem concretely: the univariate Gram-stain association supports the hypothesis that cell-envelope architecture may influence metal tolerance, while lineage structure prevents separating that mechanism from taxonomic composition. [src: bacdive_phenotype_metal_tolerance]

### Disagreement 2 — Catalase: positive or negative?

**Side A: catalase is positively associated with metal tolerance overall.** The overall catalase association is positive. [src: bacdive_phenotype_metal_tolerance]

**Side B: within lineages the association reverses.** The overall positive catalase association contradicts the negative within-class associations in Actinomycetes, Gammaproteobacteria, and Betaproteobacteria; the corpus therefore does not support one catalase direction across lineages. [src: bacdive_phenotype_metal_tolerance] This is a sign reversal between pooled and stratified analysis, not a difference in magnitude, so no single directional statement about catalase is currently defensible.

### Disagreement 3 — Gene content: phylogeny-dominated or environment-structured?

**Side A: phylogeny usually dominates.** The ecotype analysis found that phylogeny dominated gene-content similarity in 60.5% of species, and significant environmental effects were detected in only 16 of 172 species. [src: ecotype_analysis]

**Side B: a substantial environment-dominant minority remains, and functional subsets differentiate.** Environment dominated in 39.5% of species. [src: ecotype_analysis] This **refines** rather than contradicts the phenotype database result: lineage is often dominant at genome-wide scale, but the nonzero environmental-dominant subset and the possibility of subset-specific adaptation caution against treating weak whole-genome environmental effects as universal evidence of no ecological structuring. [src: ecotype_analysis] The ecotype-functional study further **supports** functional subset differentiation, but its lack of phylogenetic controls creates a tension: COG differences — COGs (Clusters of Orthologous Groups) being broad functional categories assigned to genes — may represent adaptive ecotypes or lineage-linked gene-content structure. [src: ecotype_functional_differentiation] This is the one side in the set whose control was not run rather than run and passed.

### Disagreement 4 — Plant compartments: genuine functional guilds or taxonomic sampling?

**Side A: compartment-associated functions are real.** The plant study found strong apparent plant-associated marker and gene-family differences before and after some controls, and the retained signals may reflect genuine plant-associated functions. [src: plant_microbiome_ecotypes]

**Side B: most of the apparent effect was over-sampled taxa.** The same study found small compartment effects after adversarial correction — an adversarial correction being a deliberate re-analysis built to strip out the most plausible confounding explanation before the effect is re-estimated — and the 86% loss of the original compartment R² after removing genome-rich species, together with the limited phylogenetic-tree coverage, prevents separating ecological adaptation from taxonomic sampling across the full cohort. [src: plant_microbiome_ecotypes]

### Disagreement 5 — Metal repertoire and niche breadth: reproducible ecology or coverage artifact?

**Side A: the association survives phylogenetic adjustment.** Metal type diversity remained associated with niche breadth after phylogenetic adjustment and coverage control. [src: microbeatlas_metal_ecology]

**Side B: it does not survive strict prevalence filtering.** The association weakened and lost significance under strict within-environment prevalence filtering (β = +0.0166, p = 0.092), where β is the estimated regression coefficient — the fitted slope of the association. [src: microbeatlas_metal_ecology] The result therefore **supports** a potentially reproducible ecological signal while **retaining** the competing explanation that detection and sampling coverage influence its strength. [src: microbeatlas_metal_ecology] This is a coverage tension rather than a resolution of the database-bias problem. [src: microbeatlas_metal_ecology]

## Possible Reconciliations

These are hypotheses, not findings; none is established by the cited evidence.

**Collinearity rather than absence (Disagreements 1, 3, 4).** A phenotype can be mechanistically causal and still add no R² once taxonomy is in the model, if the phenotype is nearly constant within the taxonomic units used as covariates. Under this hypothesis both sides of Disagreement 1 are correct: the phenotype effect exists, and the design cannot license it. The same logic would make Side A and Side B of Disagreement 4 compatible — compartment-specific functions could be real in the genome-rich species that were removed, with the 86% R² loss reflecting where the data are, not where the biology is. [src: bacdive_phenotype_metal_tolerance, plant_microbiome_ecotypes]

**Simpson-type aggregation (Disagreement 2).** A pooled positive catalase association coexisting with negative within-class associations is the classic signature of a confounded pooled estimate, in which between-lineage composition dominates the marginal sign. If so, the within-class estimates are the mechanistically interpretable ones and the pooled estimate is a composition statistic — but the input evidence does not establish which estimate should be preferred, and averaging them is not a resolution. [src: bacdive_phenotype_metal_tolerance]

**Scale mismatch: whole genome vs. functional subset (Disagreement 3).** Environmental adaptation acting on a small subset of loci would be diluted in genome-wide similarity measures, producing the 60.5%/39.5% split and the 16-of-172 significance count while still permitting real COG-level differentiation. This would make the ecotype analysis and the ecotype-functional study compatible, but it does not dispose of the competing reading that the COG differences are lineage-linked, because that study lacked phylogenetic controls. [src: ecotype_analysis, ecotype_functional_differentiation]

**Filter stringency as a power-vs-bias trade (Disagreement 5).** Strict within-environment prevalence filtering removes rarely detected taxa, which both reduces sample size and removes exactly the taxa whose apparent niche breadth is most coverage-sensitive. A true effect losing significance under a filter that also costs power (β = +0.0166, p = 0.092) is not the same event as an effect being absent — but neither reading is settled by the current analysis. [src: microbeatlas_metal_ecology]

**Outcome-definition mismatch (Disagreements 1 and 5).** The composite-score analysis cannot establish metal-specific mechanisms: per-metal scores are needed to test whether catalase predicts copper, urease predicts nickel, or H₂S predicts zinc, copper, and cadmium tolerance. [src: bacdive_phenotype_metal_tolerance] If phenotype effects are metal-specific and opposed across metals, a composite outcome would attenuate them toward the taxonomy-only result. This refines the connection to [[concepts/condition-specific-fitness]], because a phenotype may have a specific effect under one metal condition without predicting a composite score across metals. [src: bacdive_phenotype_metal_tolerance]

## Resolving Work

**For Disagreement 1 (phenotype vs. taxonomy):**
- Refit the metal-tolerance model with per-metal outcome scores rather than the composite, testing the three pre-named mechanistic predictions — catalase/copper, urease/nickel, H₂S/zinc, copper and cadmium — to ask whether metal-specific effects are being cancelled in the composite. [src: bacdive_phenotype_metal_tolerance]
- Quantify phenotype-by-taxonomy collinearity directly (within-taxon phenotype variance, variance-inflation diagnostics) to distinguish "no effect" from "no identifiable effect," reporting how many taxa retain phenotype variation at all. [src: bacdive_phenotype_metal_tolerance]
- Restrict the model to taxa with both phenotype states well represented and ask whether the 16.3% phenotype-alone variance survives inside that subset. [src: bacdive_phenotype_metal_tolerance]

**For Disagreement 2 (catalase direction):**
- Fit a hierarchical model with class-level random slopes for catalase, reporting the between-class distribution of the effect rather than a single pooled sign. [src: bacdive_phenotype_metal_tolerance]
- Extend the within-class stratification beyond Actinomycetes, Gammaproteobacteria, and Betaproteobacteria to every class with adequate counts, to test whether the negative direction is general or specific to those three. [src: bacdive_phenotype_metal_tolerance]

**For Disagreement 3 (phylogeny vs. environment in gene content):**
- Re-run the gene-content partition on functional subsets (e.g. COG-restricted distance matrices) rather than whole-genome similarity, asking whether the 39.5% environment-dominant share rises when the whole-genome dilution is removed. [src: ecotype_analysis]
- Add phylogenetic controls to the ecotype-functional COG comparison — the control that was never applied, and whose absence currently leaves adaptive ecotypes and lineage-linked gene content indistinguishable. [src: ecotype_functional_differentiation]
- Characterize the 16 species with significant environmental effects — habitat, lineage, genome availability — to test whether they are a biological class or a sampling class. [src: ecotype_analysis]

**For Disagreement 4 (plant compartments):**
- Repeat the genome-rich-species removal as a graded sensitivity curve rather than a single cut, reporting compartment R² as a function of how much of the over-sampled tail is excluded, so the 86% loss can be read as a shape rather than a point. [src: plant_microbiome_ecotypes]
- Expand phylogenetic-tree coverage for the plant cohort and re-test marker and gene-family differences with phylogenetic control across the full cohort, which the current limited coverage precludes. [src: plant_microbiome_ecotypes]

**For Disagreement 5 (metal diversity and niche breadth):**
- Report the prevalence-filter stringency as a continuum with effect size, standard error and sample size at each step, to separate power loss from bias correction around the β = +0.0166, p = 0.092 result. [src: microbeatlas_metal_ecology]
- Test the association within environment categories where detection coverage is deepest, where the coverage explanation is weakest, and compare to the pooled estimate. [src: microbeatlas_metal_ecology]
- Simulate a null in which niche breadth is generated purely from sampling depth, and ask whether it reproduces the pre-filter association strength. [src: microbeatlas_metal_ecology]
