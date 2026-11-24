---
type: "Concept"
description: "Whether the size, breadth and condition dependence of a gene's laboratory fitness effect predicts core versus accessory status, and what that implies for selection in nature; stops at individual gene mechanisms."
sources: ["summaries/conservation_fitness_synthesis__REPORT.md", "summaries/core_gene_tradeoffs__REPORT.md", "summaries/discoveries.md", "summaries/field_vs_lab_fitness__REPORT.md", "summaries/fitness_effects_conservation__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md"]
---
# Gene fitness importance as a predictor of pangenome conservation

Laboratory fitness predicts whether a gene is core or accessory, but only modestly. Genes with larger, broader or more condition-specific fitness effects are somewhat more often core. [src: discoveries, conservation_fitness_synthesis] The link between essentiality and conservation is quantitative, not binary. [src: discoveries] In well-characterized bacteria most essential and non-essential genes alike are core. [src: discoveries] The evidence comes from several Fitness Browser (FB) analyses and the synthesis built on them. It supports a view of the core genome as functionally active. [src: conservation_fitness_synthesis] Metal-stress genes in 22 organisms and a pathway-level analysis in 7 FB organisms point the same way. [src: metal_fitness_atlas, pathway_capability_dependency] A single-organism field-versus-lab analysis in Desulfovibrio vulgaris Hildenborough (DvH) agrees: fitness magnitude predicts conservation better than ecological context does, but fitness alone classifies core status poorly. [src: field_vs_lab_fitness] The report authors state that the 16 percentage point gradient is statistically robust yet only weakly predictive. [src: fitness_effects_conservation] Inferences about natural selection are interpretations, not direct measurements. [src: conservation_fitness_synthesis]

## Size and breadth of fitness effect

Core fraction rises steadily with fitness importance. Across 194,216 protein-coding genes in 43 bacteria, core fraction fell by 16 percentage points from essential genes (82% core) to always-neutral genes (66% core). [src: discoveries, conservation_fitness_synthesis] The fitness_effects_conservation report states the same gradient spans ~194,000 genes across 43 diverse bacteria. [src: fitness_effects_conservation] Binning by the strongest negative fitness effect gave the same pattern: genes with min_fit < -3 were 78% core, against 66% for min_fit near 0. [src: discoveries] The finer figures were 82.2% core for essential genes, 77.7% for min_fit < -3 and 66.4% for min_fit -1 to 0. [src: fitness_effects_conservation] Binning by breadth also agreed: genes important in 20+ conditions were 79% core, against 66% for genes important in 0 conditions. [src: discoveries]

By breadth, the core fractions were:

| Breadth class | % core |
|---|---|
| Essential | 82% [src: fitness_effects_conservation] |
| 20+ experiments | 79% [src: fitness_effects_conservation] |
| 6-20 experiments | 73% [src: fitness_effects_conservation] |
| 1-5 experiments | 71% [src: fitness_effects_conservation] |
| 0 experiments | 66% [src: fitness_effects_conservation] |

Genes important in more conditions were more likely core (Spearman rho=0.086, p=8.1e-230). [src: fitness_effects_conservation] By sickness class, often-sick genes (>10% of experiments; 15,989 genes) were 78% core. [src: fitness_effects_conservation] Sometimes-sick genes (25,201) were 72% core. [src: fitness_effects_conservation] Mixed sick-and-beneficial genes (20,739) were 70% core. [src: fitness_effects_conservation] Sometimes-beneficial genes (9,705) were 70% core. [src: fitness_effects_conservation] Always-neutral genes (94,889) were 66% core. [src: fitness_effects_conservation]

The report concludes that the essentiality–conservation link is quantitative rather than binary. [src: discoveries] In the same analysis, essential genes with no viable mutants numbered 27,693 and were 82% core. [src: fitness_effects_conservation] The pathway report adopted breadth as 30% of its composite importance score, citing the finding that breadth predicts conservation better than magnitude. [src: pathway_capability_dependency]

Essentiality in particular gives a real but modest enrichment. Across 33 diverse bacteria, putative essential genes (no RB-TnSeq transposon insertions; RB-TnSeq is random barcode transposon sequencing) were 86.1% core versus 81.2% for non-essential genes. The median OR (odds ratio) was 1.56, and 18 of 33 organisms were significant after BH-FDR (Benjamini-Hochberg false discovery rate). [src: discoveries] The enrichment is modest because most genes in well-characterized bacteria are core regardless of essentiality. [src: discoveries] It is strongest in organisms with larger clades, which give more reliable core classification. [src: discoveries] The synthesis report also calls the overall importance–conservation effect modest. [src: conservation_fitness_synthesis]

Essential genes differ in what they do, depending on conservation. Essential genes in core clusters are 41.9% enzymes and 13.0% hypothetical, and form a well-characterized backbone of ribosomes, DNA replication, cell wall and cofactor biosynthesis. [src: discoveries] Essential-auxiliary genes, essential but absent from some strains, are 13.4% enzymes and 38.2% hypothetical. [src: discoveries] Essential-unmapped genes, which are strain-specific with no pangenome match, are 44.7% hypothetical and are flagged as functional-discovery targets. [src: discoveries] Against non-essential genes, essential-core genes are enriched in SEED Protein Metabolism (+13.7 pp), Cofactors/Vitamins (+6.2 pp) and Cell Wall (+3.9 pp). [src: discoveries] They are depleted in Carbohydrates (-7.9 pp), Amino Acids (-5.6 pp) and Membrane Transport (-4.0 pp), which are conditionally important rather than universally essential. [src: discoveries] The report cites Rosconi et al. (2022), who found that pan-genome composition influences essentiality in S. pneumoniae. [src: discoveries]

## Condition dependence and trade-offs

Genes with condition-dependent effects are more often core, not more often accessory. Genes with strong condition-specific phenotypes were 77.3% core versus 70.3% for genes without them (OR=1.78, p=1.8e-97). [src: discoveries, conservation_fitness_synthesis] The report says this contradicts the intuition that condition-specific fitness means niche-specific, accessory genes. It attributes the pattern to core genes sitting in well-characterized, essential pathways, where effects are easier to detect. [src: discoveries, conservation_fitness_synthesis, core_gene_tradeoffs]

The dark-gene analysis gives a related null result. The hypothesis that stress-condition dark genes are more accessory than carbon/nitrogen dark genes was rejected (Fisher's exact, n=7,491; p=0.013). [src: functional_dark_matter] Stress genes were 23.0% accessory versus 25.5% for carbon/nitrogen genes (OR=1.15), the opposite of the prediction. [src: functional_dark_matter] The report says condition specificity and conservation are more complex than a simple stress=accessory, metabolism=core model. [src: functional_dark_matter]

Trade-off genes follow the same direction. In core_gene_tradeoffs, 25,271 genes (17.8%) were important (fit < -1) in some conditions and burdensome (fit > 1) in others. [src: discoveries] These genes were 1.29x more likely to be core (OR=1.29, p=1.2e-44). [src: discoveries, core_gene_tradeoffs, conservation_fitness_synthesis] The report attributes this to core genes taking part in more pathways with condition-dependent costs and benefits. [src: discoveries]

Latent metabolic capabilities show the same dependence on condition. All Latent Capabilities became fitness-important under condition-specific analysis (nitrogen limitation, stress or carbon source shifts). [src: discoveries] The pathway report states that all 66 Latent Capability pathway-organism pairs become fitness-important under at least one condition type. [src: pathway_capability_dependency] It says this stratification, motivated by core_gene_tradeoffs, revealed that all Latent Capabilities become important under stress or limitation. [src: pathway_capability_dependency] Nitrogen limitation, stress and carbon limitation most often trigger reclassification. [src: pathway_capability_dependency] The discoveries digest reads this as validating the core_gene_tradeoffs finding that laboratory fitness underestimates natural selection on metabolic genes. [src: discoveries] The pathway report proposes that pathways dispensable under carbon-rich conditions may be essential under nitrogen limitation. [src: pathway_capability_dependency] It cautions that, with enough condition types and a median threshold per subset, some pathways will inevitably cross the threshold, so "all become important" partly reflects that. [src: pathway_capability_dependency]

## Burden and the streamlining hypothesis

Accessory genes are not more burdensome than core genes, which counts against the streamlining hypothesis. Core genes were more likely to show a positive fitness effect when deleted: 24.4% versus 19.9% for auxiliary genes (OR=0.77 for auxiliary vs core, p=5.5e-48). [src: discoveries, conservation_fitness_synthesis] The report attributes this to core genes' participation in more pathways and trade-offs. [src: discoveries]

The core-burden pattern is not uniform. Core genes are more burdensome in RNA Metabolism (+12.9pp), Motility/Chemotaxis (+7.8pp) and Protein Metabolism (+6.2pp). [src: discoveries] Cell Wall reverses it, with non-core cell wall genes more burdensome (-14.1pp). [src: discoveries] The report says the paradox reflects the trade-off architecture of specific functional systems, not a uniform core-genome property. [src: discoveries]

## Metal-stress genes

Across 22 organisms and 14 metals in the Pan-Bacterial Metal Fitness Atlas, genes with significant metal-stress fitness defects were 87.4% core versus 76.9% baseline (OR=2.08, p=4.3e-162). [src: metal_fitness_atlas] Metal-important genes were more core than baseline in 21 of 22 organisms, 14 significant at p<0.05. [src: metal_fitness_atlas] The pathway report reuses this OR-based validation framework and cites it as consistent with small core enrichment for Active Dependencies. [src: pathway_capability_dependency]

Most metal-important genes are specific to metal stress, and they are still mostly core. Across 24 organisms, 4,177 (55%) of 7,609 metal-important gene records were sick under metal stress but had a <5% sick rate across 5,945 non-metal experiments. [src: discoveries] Another 38% were general sick (important across many conditions) and 7% were metal+stress (shared with other stresses). [src: discoveries] The report concludes that the Metal Fitness Atlas gene set is not dominated by general stress response; most are genuine metal tolerance determinants. [src: discoveries]

Metal-specific genes were 84.8% core (pooled) versus 90.2% for general sick genes (Cochran-Mantel-Haenszel p=0.011). [src: discoveries] Both categories were enriched above the 79.8% core baseline. [src: discoveries] The report says this partially supports the Metal Atlas two-tier model: general stress response (Tier 1) is more core than specialized metal resistance (Tier 2), but both are predominantly core. [src: discoveries] It concludes that the accessory genome contributes only modestly to metal resistance machinery. [src: discoveries]

## Field versus lab fitness in one organism

In DvH, fitness importance under almost any condition class goes with core status, and field conditions do not separate cleanly from lab ones. Important genes were defined as those with fitness < -2. [src: field_vs_lab_fitness] Field-stress (298 genes) were 83.6% core, OR 1.58, FDR q=0.026. [src: field_vs_lab_fitness] Field-core (376 genes) were 82.4% core, OR 1.46, q=0.026. [src: field_vs_lab_fitness] Lab-other (292 genes) were 81.5% core, OR 1.37, q=0.073. [src: field_vs_lab_fitness] Lab-nutrient (452 genes) were 81.4% core, OR 1.36, q=0.037. [src: field_vs_lab_fitness] Lab-antibiotic (109 genes) were 73.4% core, OR 0.86, q=0.49. [src: field_vs_lab_fitness] After BH-FDR correction, field-stress, field-core and lab-nutrient genes were significantly enriched in the core genome. [src: field_vs_lab_fitness] The report says fitness effects vary by condition class, though conservation patterns do not cleanly separate field from lab conditions. [src: field_vs_lab_fitness] The pathway report cites a field_vs_lab_fitness result of field-important genes 83.6% core versus a 76.3% baseline. [src: pathway_capability_dependency]

Specificity classes tell the same story. Lab-specific genes (sick in lab only; 50 genes) were 96.0% core. [src: field_vs_lab_fitness] Field-specific genes (52) were 88.5% core. [src: field_vs_lab_fitness] Field-biased genes (89) were 83.1% core. [src: field_vs_lab_fitness] Universal genes (sick in both; 352) were 79.8% core. [src: field_vs_lab_fitness] Neutral genes (2,083) were 74.5% core. [src: field_vs_lab_fitness] The report reads the high values for both specific classes as meaning that any fitness importance predicts conservation, regardless of ecological context. [src: field_vs_lab_fitness] The field-specific versus lab-specific comparison is not significant (Fisher exact OR=0.32, p=0.27, n=50-52 per group). [src: field_vs_lab_fitness] Universal genes were significantly more core than neutral genes (OR=1.35, p=0.033). [src: field_vs_lab_fitness]

### Prediction and threshold sensitivity

Fitness barely predicts core status in DvH. Using logistic regression with 10-fold cross-validated AUC (area under curve), [src: field_vs_lab_fitness] field fitness alone gave 0.517 (Std 0.052), [src: field_vs_lab_fitness] lab fitness alone 0.531 (Std 0.052), [src: field_vs_lab_fitness] and field plus lab 0.548 (Std 0.053). [src: field_vs_lab_fitness] Adding gene length raised it to 0.645 (Std 0.068). [src: field_vs_lab_fitness] Gene length is a much stronger predictor than fitness from either field or lab conditions, and neither fitness dimension alone is informative. [src: field_vs_lab_fitness] The report says cross-validation confirms the in-sample estimates are not inflated. [src: field_vs_lab_fitness]

The pattern is robust across fitness thresholds from -1 to -3, with -2 as the primary cutoff. [src: field_vs_lab_fitness] Core percentages at thresholds -3.0, -2.0, -1.5 and -1.0 were, class by class:

- Field-stress: 89.4%, 83.6%, 84.0%, 82.1%. [src: field_vs_lab_fitness]
- Field-core: 84.4%, 82.4%, 81.9%, 79.0%. [src: field_vs_lab_fitness]
- Lab-nutrient: 83.5%, 81.4%, 81.0%, 79.5%. [src: field_vs_lab_fitness]
- Lab-other: 85.2%, 81.5%, 80.1%, 77.5%. [src: field_vs_lab_fitness]
- Lab-antibiotic: 82.2%, 73.4%, 77.3%, 76.2%. [src: field_vs_lab_fitness]
- Heavy-metals: 70.6%, 71.2%, 76.7%, 76.7%. [src: field_vs_lab_fitness]

Field-stress genes were consistently the most conserved and heavy-metals genes the least. [src: field_vs_lab_fitness] The report attributes the lab-antibiotic dip at -2 to a small sample (n=109 at -2 vs n=45 at -3). [src: field_vs_lab_fitness]

The report concludes that fitness magnitude matters more than which condition produces it. [src: field_vs_lab_fitness] It suggests, as an unanticipated result, that the core genome reflects general functional importance rather than niche-specific selection. [src: field_vs_lab_fitness]

### Limits of the DvH analysis

- Gene length is confounded with fitness measurement quality (short genes get fewer insertions) and with core status (core genes tend to be longer). [src: field_vs_lab_fitness]
- The field-specific and lab-specific sets are small (n=50-52), which limits power. [src: field_vs_lab_fitness]
- Field and lab effects are correlated (r ~ 0.7 from the scatter plot), so most genes sick in one context are sick in the other. [src: field_vs_lab_fitness]
- A single organism limits generalizability, particularly to organisms with larger accessory genomes. [src: field_vs_lab_fitness]
- The pangenome has few genomes, giving a coarse classification and a high baseline core fraction (76.3%) that compresses effect sizes. [src: field_vs_lab_fitness]

The DvH report proposes two refinements. It would replace binary core/auxiliary status with the fraction of genomes carrying the gene cluster, to increase statistical power. [src: field_vs_lab_fitness] It would also replace binary important/not-important status with continuous fitness scores, such as mean or minimum fitness per condition class, as logistic-regression predictors. [src: field_vs_lab_fitness]

## Modules and pathways

Co-regulated fitness modules are also enriched in the core. ICA (independent component analysis) fitness modules were 86.0% core versus 81.5% baseline across 29 organisms (Fisher OR=1.46, p=1.6e-87). Per-organism paired Wilcoxon p=1.0e-03, and 22 of 29 organisms showed enrichment. [src: discoveries] 59% of modules were >90% core genes. [src: discoveries] The report concludes that the core genome is functionally coherent at module level. [src: discoveries]

Module families spanning more organisms did not have higher core fractions (Spearman rho=-0.01, p=0.914). [src: discoveries] The report reads this as a ceiling effect from the ~82% baseline core rate, not as evidence against the conservation–function relationship. [src: discoveries] The pathway report cites the same module_conservation null result. [src: pathway_capability_dependency] It presents pathway variability, not breadth, as the informative metric at pathway level. [src: pathway_capability_dependency] It also treats the cofitness_coinheritance result that 73% of accessory modules show co-inheritance with co-fitness as validating pathway-level fitness aggregation. [src: pathway_capability_dependency]

At pathway level, Active Dependencies had mean core gene completeness of 0.986 versus 0.975 for Latent Capabilities. [src: pathway_capability_dependency] The report attributes the small gap to the 7 FB organisms being well-studied models with near-complete, well-annotated core genomes. [src: pathway_capability_dependency] It describes its Tier 2 analysis as extending core enrichment from genes to whole pathways, showing that pathway completeness can depend on accessory genes. [src: pathway_capability_dependency] It places Active Dependencies at the high end of the 16pp gradient, as the metabolic instance of conserved genes being fitness-important. [src: pathway_capability_dependency]

## Implications for selection in nature

The fitness_effects_conservation report interprets the gradient as empirical support for selection as a major driver of core gene maintenance. [src: fitness_effects_conservation] It reads core genes as the most functionally active, with the largest fitness effects in both directions because they are embedded in critical pathways. [src: fitness_effects_conservation] Accessory genes it reads as functionally quieter under laboratory conditions. [src: fitness_effects_conservation] It cites Luo et al. (2015), who showed stronger purifying selection on core than accessory genes, as consistent. [src: fitness_effects_conservation] The pathway report proposes that core genes encode universally needed functions (central metabolism, metal tolerance, translation) and accessory genes conditionally needed ones, including specific biosynthetic pathways. [src: pathway_capability_dependency] It also asserts that how often a species meets each condition type sets the selective pressure to keep a pathway. [src: pathway_capability_dependency]

The report treats lab fitness as capturing the cost of maintaining genes and pangenome conservation as capturing evolutionary pressure to keep them. [src: conservation_fitness_synthesis] On that reading, 28,017 genes are costly in the lab and conserved in the pangenome. The report calls them its strongest evidence for purifying selection in natural environments. [src: conservation_fitness_synthesis, discoveries, pathway_capability_dependency] Another 5,526 genes are costly and dispensable, which makes them candidates for ongoing gene loss. [src: conservation_fitness_synthesis, discoveries] A further 21,886 genes are neutral and dispensable, described as niche-specific. [src: discoveries] These are interpretations, not direct measurements of selection.

Several caveats limit them:
- Laboratory conditions are an impoverished proxy for nature. [src: conservation_fitness_synthesis]
- Condition-type stratification only partially addresses this, because laboratory RB-TnSeq cannot capture the full range of natural selective pressures. [src: pathway_capability_dependency]
- A gene with positive fitness when deleted in rich media may be essential in soil, biofilm, host tissue or other natural conditions. [src: conservation_fitness_synthesis]
- The identity of the 5,526 genes is open. They may be mobile elements or recently acquired genes on the way out. [src: conservation_fitness_synthesis]
- Whether organisms from more variable environments have more core trade-off genes is unresolved. The report proposes connecting laboratory fitness to AlphaEarth environmental data. [src: conservation_fitness_synthesis]

The pathway report proposes that, under the Black Queen Hypothesis, pathway gene loss may be constrained by the breadth of environmental conditions a species meets, not only by mean fitness under one condition. [src: pathway_capability_dependency]

A separate pathway analysis shows that fitness-neutral does not mean absent. Across 7 FB organisms × 23 GapMind pathways, 35.4% were Active Dependencies (complete and fitness-important) and 41.0% were Latent Capabilities (complete but fitness-neutral in rich media). A further 14.9% were Incomplete but Important and 8.7% were Missing. [src: discoveries] See [[concepts/latent-metabolic-capability-versus-fitness-dependency]].

## Open Directions

- Test the 5,526 costly and dispensable genes for mobile-element annotation and recent acquisition, to settle whether they are genes being lost. See mobile element origin of costly non conserved genes.
- Link laboratory fitness to AlphaEarth environmental data, to ask whether organisms from more variable environments carry more core trade-off genes.
- Repeat the module-breadth test in a set with a lower baseline core rate, to see whether the ceiling effect hides a gradient.
- Compare lab-defined costly-conserved genes with field-relevant fitness, to test the purifying-selection interpretation. See [[concepts/field-relevant-versus-laboratory-fitness-as-a-predictor-of-gene-conservation]].
- Rerun the DvH analysis with the fraction of genomes carrying each gene cluster and with continuous fitness scores, to see whether the weak prediction (CV-AUC near 0.5) reflects coarse binary inputs.
- Rerun the pathway condition-type stratification against a null that permutes condition labels, to separate real triggers from inevitable threshold crossing.
