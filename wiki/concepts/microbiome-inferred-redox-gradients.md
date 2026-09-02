---
type: "Concept"
description: "Inferring redox structure from spatial microbial community composition"
sources: ["summaries/enigma_sso_asv_ecology__REPORT.md"]
---
# Inferring subsurface redox gradients from microbial community composition

This concept examines how spatial patterns in microbial community composition can be used to infer subsurface redox structure when direct geochemical measurements are unavailable. [src: enigma_sso_asv_ecology]

The approach is an inference rather than a direct measurement: taxa or taxonomic groups are assigned to redox-associated processes, and their spatial enrichment is interpreted as a possible sequence of electron-acceptor zones. [src: enigma_sso_asv_ecology] This distinction connects the SSO analysis to [[concepts/taxonomic-resolution-dependent-functional-inference]], [[concepts/occurrence-versus-catabolic-activity]], and [[concepts/subsurface-bacillota-specialization]].

## SSO spatial evidence

The SSO study analyzed sediment and groundwater 16S amplicon sequence variant (ASV) communities across a 3×3 grid of 9 wells spanning approximately 6 m. [src: enigma_sso_asv_ecology] The sediment dataset contained 23,458 ASVs and 37 sediment core samples aggregated per well. [src: enigma_sso_asv_ecology]

Community composition showed significant distance-decay, measured with a Mantel test that correlates ecological and geographic distance matrices, with Spearman ρ = 0.323, p = 0.029, and 9,999 permutations. [src: enigma_sso_asv_ecology] NMDS (non-metric multidimensional scaling) produced stress = 0.067, whereas Procrustes correspondence between community ordination and the physical grid was marginal, with m² = 0.379 and p = 0.080. [src: enigma_sso_asv_ecology]

The strongest similarity corridor was U3–M6–L7, where U3–M6 had Bray–Curtis dissimilarity = 0.558 and residual = −0.170, M6–L7 had Bray–Curtis dissimilarity = 0.615 and residual = −0.154, and U3–L7 had Bray–Curtis dissimilarity = 0.646 and residual = −0.133. [src: enigma_sso_asv_ecology] The report interprets this northeast-to-southwest diagonal as consistent with a contamination-plume flow path, but the hydrological explanation remains a testable inference because direct SSO geochemistry was unavailable. [src: enigma_sso_asv_ecology]

## Hydrogeological zonation

PERMANOVA (permutational multivariate analysis of variance) found that hydrogeological zone explained 27.5% of community variance, with F = 4.05 and p = 0.0001, while well identity explained 19.2% and was not significant, with F = 0.80 and p = 0.979. [src: enigma_sso_asv_ecology] Samples from the same well but different depths had median Bray–Curtis dissimilarity = 0.977, whereas samples from the same depth zone in different wells had median Bray–Curtis dissimilarity = 0.835. [src: enigma_sso_asv_ecology]

These results support the interpretation that depth and saturated-zone position can dominate well identity in structuring subsurface communities. [src: enigma_sso_asv_ecology] The depth classes were VZ with 33 samples, VSZ with 25, SZ1 with 54, and SZ2 with 45. [src: enigma_sso_asv_ecology]

Ten of 12 dominant phyla had significant depth associations at p < 0.05. [src: enigma_sso_asv_ecology] Shallow-enriched groups included Chloroflexi with Spearman ρ = −0.73, Patescibacteria with ρ = −0.70, Myxococcota with ρ = −0.54, and Spirochaetota with ρ = −0.53. [src: enigma_sso_asv_ecology] Deep-enriched groups included Firmicutes with ρ = +0.76, WPS-2 with ρ = +0.52, Bacteroidota with ρ = +0.50, and Proteobacteria with ρ = +0.49. [src: enigma_sso_asv_ecology]

## Inferred redox process pattern

Multi-resolution functional inference covered 22 classes at 78% coverage and 65 annotated genera at 21% coverage. [src: enigma_sso_asv_ecology] The class-level redox index ranged from 0.047 at M6 to 0.227 at U3. [src: enigma_sso_asv_ecology]

The genus-level analysis covered 12 biogeochemical process categories and mapped inferred process hotspots across the grid. [src: enigma_sso_asv_ecology] Denitrification ranged from 1.9–7.7% and peaked at M5 at 7.7%, with [[entities/rhodanobacter]] as the key genus. [src: enigma_sso_asv_ecology] Iron oxidation peaked at U3 at 2.8%, with [[entities/sideroxydans]], while nitrification also peaked at U3 at 2.3%, with [[entities/nitrosotalea]] absent from the current whitelist and therefore referenced here by plain text. [src: enigma_sso_asv_ecology]

Iron reduction peaked at U1 at 2.3%, with [[entities/anaeromyxobacter]], while sulfur oxidation peaked at M4 at 1.9%, with [[entities/arcobacter]] and [[entities/thiobacillus]]. [src: enigma_sso_asv_ecology] Methanotrophy peaked at M4 at 1.9%, with [[entities/methanoperedens]], and fermentation peaked at L9 at 5.3%, with [[entities/spirochaeta]] and [[entities/paenisporosarcina]]. [src: enigma_sso_asv_ecology]

The proposed spatial sequence is oxidative processes near U3, denitrification near M5, and fermentation near L9 along an inferred O₂ → NO₃⁻ → Fe(III) → SO₄²⁻ → fermentation progression. [src: enigma_sso_asv_ecology] M5 is hypothesized to be a plume mixing zone where nitrate-rich contaminated groundwater meets native organic carbon, and M6 is hypothesized to be an anaerobic dead zone with the lowest inferred iron oxidation, sulfur oxidation, and nitrification. [src: enigma_sso_asv_ecology]

These environmental assignments are hypotheses based on taxonomy-to-trait inference rather than direct measurements of oxygen, nitrate, iron, sulfate, carbon, or other geochemical variables. [src: enigma_sso_asv_ecology] The inferred redox ladder therefore supports a prioritization framework for sampling and validation, not a demonstrated geochemical map. [src: enigma_sso_asv_ecology]

## Groundwater–sediment contrast

Groundwater and sediment communities collected at the same well had median Bray–Curtis dissimilarity = 0.424, with within-well values ranging from 0.364–0.450 across 5 wells. [src: enigma_sso_asv_ecology] Groundwater was enriched in [[entities/rhodanobacter]] at 3.62% versus 1.23% in sediment, [[entities/gallionella]] at 0.14% versus 0.01%, and [[entities/sideroxydans]] at 0.06% versus 0.01%. [src: enigma_sso_asv_ecology] Sediment was enriched in [[entities/anaeromyxobacter]] at 1.24% versus 0.03% in groundwater, [[entities/arcobacter]] at 0.54% versus 0.00%, and [[entities/methanoperedens]] at 0.42% versus 0.00%. [src: enigma_sso_asv_ecology]

The report interprets groundwater enrichment in denitrifiers and iron oxidizers, together with sediment enrichment in anaerobic taxa, as evidence that attached and planktonic communities are distinct. [src: enigma_sso_asv_ecology] This interpretation is limited because the sediment and groundwater samples were collected 18 months apart, so the contrast may combine habitat effects with temporal or seasonal effects. [src: enigma_sso_asv_ecology]

## Guild associations as supporting evidence

Across 9 wells, 65 annotated genera were assigned to 11 metabolic guilds. [src: enigma_sso_asv_ecology] Nitrifier × iron oxidizer correlation was ρ = +0.95, syntroph × fermenter correlation was ρ = +0.55, fermenter × predator correlation was ρ = +0.85, denitrifier × syntroph correlation was ρ = −0.67, and sulfate reducer × aerobic heterotroph correlation was ρ = −0.75. [src: enigma_sso_asv_ecology]

These associations support hypotheses about functional coupling or spatial separation across a redox gradient, but they do not directly measure metabolic interactions or reaction rates. [src: enigma_sso_asv_ecology]

## Evidence limits and tensions

Genus-level functional annotation covered only 21% of total reads, with 65 of 1,038 genera annotated, so genus-level process estimates are lower bounds. [src: enigma_sso_asv_ecology] Class-level traits had 78% coverage and showed consistent redox patterns, but the report recommends sensitivity analysis against the lower-coverage genus-level results. [src: enigma_sso_asv_ecology]

Species-level classification was approximately 0%, genus-level taxonomy covered 44% of sediment reads, and 56% of reads remained outside the genus-level inference. [src: enigma_sso_asv_ecology] Trait scores at phylum and class levels were consensus estimates based on literature-linked taxonomy rather than empirical measurements of the specific SSO populations. [src: enigma_sso_asv_ecology]

The central tension is between a coherent composition-based redox hypothesis and the absence of direct geochemical confirmation. [src: enigma_sso_asv_ecology] The report records 221 geochemistry sample tubes in CORAL, but metals, ion chromatography/total organic carbon, isotopes, ammonia, and nitrite measurements had not been loaded into the analyzed dataset. [src: enigma_sso_asv_ecology]

Groundwater ASV coverage included only 5 of 9 wells—L7, L9, M4, M6, and U2—and excluded the inferred hotspot wells M5 and U3. [src: enigma_sso_asv_ecology] The 9-day groundwater comparison showed well identity explaining 49.9% of variance, filter size explaining 10.1%, depth within the saturated zone explaining 2.5%, and date explaining 0.8%; the corresponding p-values were 0.001, 0.001, 0.430, and 0.998. [src: enigma_sso_asv_ecology] This supports persistent spatial structure over that interval, but it does not establish seasonal or long-term redox stability. [src: enigma_sso_asv_ecology]

## Open Directions

- Load the 221 SSO geochemistry samples into CORAL and test whether nitrate, pH, and metal concentrations form the predicted northeast-to-southwest gradient. [src: enigma_sso_asv_ecology]
- Extract pump-test ASVs from Brick 460-462 for L8, M5, and U2 and test whether [[entities/rhodanobacter]] is highest at M5 and lower at L8 and U2. [src: enigma_sso_asv_ecology]
- Generate metagenomes at the same spatial resolution and test whether genes for inferred denitrification, iron oxidation, sulfur oxidation, nitrification, methanotrophy, and fermentation occur in the predicted locations. [src: enigma_sso_asv_ecology]
- Analyze the 18 M6-C2 isolate genomes for anaerobic metabolisms and test the hypothesis that M6 represents an anaerobic zone. [src: enigma_sso_asv_ecology]
- Apply weighted UniFrac to ASV sequences from Bricks 457/460/477 and test whether phylogenetic community structure strengthens the inferred hydrogeological zonation. [src: enigma_sso_asv_ecology]
- Repeat 16S profiling across seasons and test whether the U3–M6–L7 corridor and the inferred redox hotspots persist through time. [src: enigma_sso_asv_ecology]

## Related Pages

- [[summaries/enigma_sso_asv_ecology__REPORT]]
- [[concepts/ecotype-environment-gene-content]]
- [[concepts/environmental-embedding-ecological-validity]]
- [[concepts/subsurface-bacillota-specialization]]
- [[concepts/occurrence-versus-catabolic-activity]]
- [[concepts/taxonomic-resolution-dependent-functional-inference]]
- [[concepts/multi-omics-integration]]
