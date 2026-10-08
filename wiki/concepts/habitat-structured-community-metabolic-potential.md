---
type: "Concept"
description: "Community-level predicted metabolic pathway completeness separates soil from freshwater communities, with carbon-utilization pathways on the main ordination axis and amino-acid biosynthesis on a secondary axis."
sources: ["summaries/nmdc_community_metabolic_ecology__REPORT.md"]
---
This page covers whether habitat type structures the *metabolic potential* of whole microbial communities, measured as predicted pathway completeness, beyond simply changing which taxa are present. The current evidence comes from a single project, [[summaries/nmdc_community_metabolic_ecology__REPORT]], which drew community samples from [[entities/nmdc]]. The ordination and per-pathway contrasts are direct statistical results on predicted completeness. The proposed mechanism remains a hypothesis. [src: nmdc_community_metabolic_ecology]

## Ordination Evidence

The project ran [[entities/principal-component-analysis]] (PCA, a projection of samples onto orthogonal axes of maximal variance) on a 220-sample × 80-pathway completeness matrix. PC1 captured 49.4% of variance and PC2 captured 16.6%, with 83% total in PC1–5. A [[entities/kruskal-wallis-test]] (a rank-based test across more than two groups) compared three ecosystem types and was highly significant on both PC1 (H = 52.98, p < 0.0001) and PC2 (H = 123.74, p < 0.0001). Soil and Freshwater communities occupied nearly non-overlapping regions of PC space. [src: nmdc_community_metabolic_ecology]

The pairwise Soil vs. Freshwater separation was extreme by a [[entities/mann-whitney-u-test]] (a rank-based two-group test): U = 3,674, p < 0.0001. Median PC1 was +3.86 for Soil and −6.28 for Freshwater. [src: nmdc_community_metabolic_ecology]

## Which Pathway Classes Load Each Axis

PC1 loads almost entirely on carbon-utilization pathways, with near-uniform positive loadings. The listed pathways are glucuronate, fumarate, succinate, cellobiose and galactose. The project reads this as Soil communities having broadly higher carbon-substrate completeness than Freshwater communities. Amino-acid pathways load more strongly on PC2 and separate samples within the Soil cluster. [src: nmdc_community_metabolic_ecology]

Per-pathway tests **refine** this axis picture: amino-acid pathways load mainly on PC2, but most of them still differ individually across habitats. Per-pathway Kruskal-Wallis tests were corrected with [[entities/benjamini-hochberg-fdr]] (BH-FDR, control of the false discovery rate, the expected share of false positives among significant calls). After correction, 17 of 18 amino-acid pathways had significantly different community completeness across ecosystem types (q < 0.05). The most extreme differences were in biosynthesis of [[entities/glycine]] (H = 92.98, q = 1.2×10⁻¹⁹), [[entities/asparagine]] (H = 66.19, q = 3.8×10⁻¹⁴) and cysteine (H = 62.66, q = 1.5×10⁻¹³). Only [[entities/tyrosine]] was not significantly differentiated (q = 0.71), which is a null result within an otherwise near-universal contrast. [src: nmdc_community_metabolic_ecology]

## Interpretation and Evidence Grading

The report says the ecosystem separation is *consistent with* the metabolic niche hypothesis. It does not claim to demonstrate it. That framing suggests the hypothesis that habitat physicochemistry (aquatic vs. terrestrial) selects fundamentally different community metabolic configurations, not just different taxa. Because carbon-utilization pathways dominate PC1, the report further proposes carbon-substrate availability as the primary axis differentiating ecosystem metabolic type, with amino-acid biosynthesis in a secondary, PC2-level role. Both statements are interpretations of loadings, not tests of mechanism. [src: nmdc_community_metabolic_ecology]

Several limits apply to the evidence summarized here. It comes from one project. It uses predicted pathway completeness rather than measured activity. It uses habitat labels rather than measured physicochemical variables. So the separation itself is well supported statistically, but its causal attribution to carbon availability or physicochemistry is untested in this corpus. The page [[concepts/occurrence-versus-catabolic-activity]] discusses the general gap between gene-content potential and realized function. [src: nmdc_community_metabolic_ecology]

## Open Directions

- **Separate habitat from composition.** Regress per-sample completeness scores on measured physicochemical covariates, such as carbon and nutrient measurements where available, while conditioning on taxonomic composition. This would test whether habitat selects metabolic configurations beyond taxon turnover, which the current habitat-label contrast cannot do. [src: nmdc_community_metabolic_ecology]
- **Test the carbon-axis claim directly.** Correlate PC1 scores with measured organic-carbon or substrate data from the same samples. This would turn the proposed primary carbon axis from a loading-based interpretation into a tested association. [src: nmdc_community_metabolic_ecology]
- **Explain the tyrosine exception.** Check whether the non-differentiated tyrosine pathway reflects true habitat-invariance or a completeness-scoring artifact, for example by comparing pathway-step definitions against the 17 differentiated amino-acid pathways. [src: nmdc_community_metabolic_ecology]
- **Probe the within-soil PC2 structure.** Stratify Soil samples by available metadata to ask what drives the amino-acid separation inside the Soil cluster. [src: nmdc_community_metabolic_ecology]
