---
type: "Method"
description: "Microbial-community profiling method using 16S rRNA amplicons"
sources: ["summaries/enigma_sso_asv_ecology__REPORT.md", "summaries/genotype_to_phenotype_enigma__REPORT.md", "summaries/lab_field_ecology__REPORT.md", "summaries/lignin_community_enrichment__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md", "summaries/soil_frontier_genomics__REPORT.md"]
---
# 16S Amplicon Sequencing

## What this entity is

**Canonical name:** 16S amplicon sequencing. [src: enigma_sso_asv_ecology]

**Known aliases:** 16S rRNA amplicon sequencing; 16S ASV profiling; 16S sequencing. [src: enigma_sso_asv_ecology]

**Stable external identifier:** None specified in the source report. [src: enigma_sso_asv_ecology]

16S amplicon sequencing is a microbial-community profiling method that generates amplicon sequence variant (ASV) data from environmental communities. It was used for sediment and groundwater communities at the SSO subsurface site. [src: enigma_sso_asv_ecology]

A separate Oak Ridge study used 16S amplicon sequencing to profile groundwater communities across 108 [[entities/oak-ridge-field-research-center]] sites and compare genus-level abundance with laboratory metal-tolerance measurements. This **extends** the method's demonstrated use from subsurface spatial ecology to field-scale geochemical gradients, while its genus-level resolution limited direct matching to Fitness Browser organisms. [src: lab_field_ecology]

The lignin-enrichment study **supports** this broader use for detecting strong community restructuring, but **refines** the method description by showing that its resolution and inference depend on the processing workflow: 21 samples across 7 groups were analyzed with 97% OTU clustering rather than ASV inference, using Bray–Curtis distances, PCoA, and PERMANOVA. [src: lignin_community_enrichment]

The MicrobeAtlas study **extends** this environmental application to a global 16S amplicon atlas containing 464,000 samples and 13 environment categories, where genus-level detections were used to estimate ecological niche breadth. It **refines** interpretation by treating such breadth as a sequencing-effort and detection proxy rather than confirmed ecological range. [src: microbeatlas_metal_ecology]

The soil-frontier analysis **extends** the method to a global genomic-representation audit based on 16S tables from 5,441 soil samples. It used 16S-derived OTU richness together with mean genome completeness to calculate a Genomic Discovery Index (GDI) at 1° spatial bins, linking community-diversity observations to gaps in reference-genome coverage. [src: soil_frontier_genomics]

## Use in the SSO study

The sediment dataset contained 23,458 ASVs from 37 sediment core samples aggregated per well across 9 wells arranged in a 3×3 grid spanning approximately 6 m. [src: enigma_sso_asv_ecology]

Community dissimilarity calculated from the 16S profiles had a mean Bray–Curtis value of 0.747, with pairwise values ranging from 0.558 for U3–M6 to 0.872 for U3–L9. [src: enigma_sso_asv_ecology]

A Mantel test, which correlates ecological and geographic distance matrices, detected significant distance-decay of community similarity with Spearman ρ = 0.323, p = 0.029, and 9,999 permutations. [src: enigma_sso_asv_ecology]

NMDS (non-metric multidimensional scaling) of the community profiles had stress = 0.067, while Procrustes correspondence between community ordination and the physical grid was marginal, with m² = 0.379 and p = 0.080. [src: enigma_sso_asv_ecology]

PERMANOVA (permutational multivariate analysis of variance) of 37 sediment core segments found that hydrogeological zone explained 27.5% of community variance, with F = 4.05 and p = 0.0001, whereas well identity explained 19.2% and was not significant, with F = 0.80 and p = 0.979. [src: enigma_sso_asv_ecology]

The profiles showed depth-associated patterns: Chloroflexi, Patescibacteria, Myxococcota, and Spirochaetota were enriched in shallow samples, while Firmicutes, WPS-2, Bacteroidota, and Proteobacteria were enriched at depth. [src: enigma_sso_asv_ecology]

## Environmental profiling and interpretation

A separate ENIGMA analysis used global 16S environmental data to place 14 ENIGMA genera in broader context; these genera occurred in 4,086–288,686 of 464,000 global 16S samples. Caulobacter occurred in 289K samples, [[entities/rhodanobacter]] in 228K, and Pseudomonas in 206K. [src: genotype_to_phenotype_enigma]

This comparison supports the existing environment-linked community-structure interpretation but refines it with evidence for a pH-associated niche partition. Across 587 100-Well-Survey communities, two anti-correlated genus clusters produced 47 significant pairs with |rho| > 0.2 and p < 0.01: Cluster A comprised Brevundimonas, Caulobacter, Sphingomonas, Variovorax, and Sphingobium, while Cluster B comprised Rhodanobacter, Ralstonia, Dyella, Serratia, and Comamonas. In global samples, Cluster A averaged pH 6.78 and 15.7°C, whereas Cluster B averaged pH 5.43 and 22.6°C, a difference of 1.35 pH units and 6.9°C. [src: genotype_to_phenotype_enigma]

The same analysis found that globally sampled Pseudomonas was 37.8% clinical, 12.9% soil/plant, and 9.4% aquatic, whereas all ENIGMA Pseudomonas belonged to the environmental Pseudomonas_E fluorescens/protegens clade. [[entities/rhodanobacter]] was 55% aquatic, 10% contaminated, and 0% clinical in the analyzed profiles. [src: genotype_to_phenotype_enigma]

Genus-level environmental interpretation was also vulnerable to identifier errors: a strain-name collision caused 12 of 32 genus-level mismatches when ENIGMA strains were matched to the KBase Data Lakehouse pangenome through short identifiers such as MT20. One collision matched Rhodanobacter glycinis to Streptococcus pneumoniae and introduced 1,751 spurious clinical genomes into environmental profiles; checking genus consistency reduced verified linkages from 32 to 20 and eliminated all false matches. [src: genotype_to_phenotype_enigma]

In the Oak Ridge groundwater analysis, 26 unique genera represented in the [[entities/kescience-fitnessbrowser]] were considered and 14 were detected. *Sphingomonas* occurred at 93% of 108 sites, *Pseudomonas* at 91%, and *Caulobacter* at 82%; the ENIGMA model organism *Desulfovibrio* occurred at 34% of sites and reached a maximum relative abundance of 0.09%. [src: lab_field_ecology]

This **supports** the existing evidence that 16S profiles can reveal environment-linked distributions, but **refines** it by showing bidirectional associations along a uranium gradient rather than a uniform enrichment of presumed metal-tolerant taxa. After Benjamini–Hochberg false-discovery-rate correction (BH-FDR), five of 11 tested genera had significant uranium associations: *Herbaspirillum* increased (Spearman rho=+0.336, p=3.8e-4, FDR q=0.001), *Bacteroides* increased (rho=+0.264, p=0.006, q=0.013), *Caulobacter* decreased (rho=-0.411, p=1.0e-5, q=1.1e-4), *Sphingomonas* decreased (rho=-0.382, p=4.5e-5, q=2.5e-4), and *Pedobacter* decreased (rho=-0.266, p=0.005, q=0.013). [src: lab_field_ecology]

*Azospirillum* showed a marginal positive association with uranium (rho=+0.20, p=0.042, q=0.077); *Desulfovibrio* showed no correlation (rho=0.022, p=0.82), and *Pseudomonas* showed no correlation (rho=-0.059, p=0.55). *Shewanella*, *Dechlorosoma*, and *Marinobacter* were excluded because each had prevalence below 10 sites. [src: lab_field_ecology]

High-uranium and low-uranium sites had distinct community compositions, with rare-biosphere taxa and subsurface specialists more prominent at high-uranium sites. The report interprets this as broader ecological restructuring rather than a simple increase in metal-tolerant organisms because redox conditions and carbon and energy sources also vary among sites. [src: lab_field_ecology]

The aggregate laboratory metal-tolerance score had a positive but non-significant association with the high-uranium/low-uranium field abundance ratio (Spearman rho=0.503, p=0.095, n=12 genera). This **qualifies** the environment-linked interpretation: 16S abundance patterns were informative at several genera, but genus-level field profiles did not establish that laboratory tolerance alone predicts field abundance. [src: lab_field_ecology]

The lignin experiment **supports** the interpretation that environmental conditions can act as strong selective filters: after one lignin-enrichment round, [[entities/pseudomonas-aeruginosa|Pseudomonas]] reached 39.3% and [[entities/acinetobacter-baylyi-adp1|Acinetobacter]] 25.2%, together comprising >64% of 16S reads, while Shannon diversity fell from 6.46 to 3.16 and observed OTUs from 1,594 to 163. Global PERMANOVA attributed 97.9% of community variance to treatment (R²=0.979, p=0.001), although significant PERMDISP means that dispersion as well as group location contributed to this signal. [src: lignin_community_enrichment]

The same study **refines** a simple taxon-environment interpretation: adding labile carbon increased Acinetobacter from 25.2% to 41.7%, reduced Pseudomonas from 39.3% to 23.0%, and increased Aeromonas from 0.1% to 20.2%, indicating a condition-specific copiotrophic assemblage rather than merely greater abundance of lignin-associated organisms. [src: lignin_community_enrichment]

The MicrobeAtlas analysis **supports** the use of 16S profiles for broad environmental comparison but **qualifies** causal interpretation. Across 1,264 bacterial genera with at least 3 OTUs, Levins' B_std niche breadth was phylogenetically conserved (Pagel's λ = 0.787, p = 7.9×10⁻¹⁰²), and habitat range across environment categories was even more conserved (λ = 0.909, p = 1.4×10⁻¹⁵⁷). The association between broader inferred niche breadth and metal type diversity was correlational and could reflect detection effort, genome size, metabolic versatility, biofilm capacity, or gene acquisition rather than a direct effect of metal resistance. [src: microbeatlas_metal_ecology]

The soil-frontier analysis **supports** the existing concern that 16S-based environmental comparisons are shaped by uneven sampling and reference coverage, but **refines** it by separating community richness from genomic representation. Its GDI was defined as OTU Richness / (Mean Genome Completeness + 1), calculated at 1° spatial bins; forest had GDI = 902.36, cropland had GDI = 890.82, grassland had GDI = 503.42, and wetland had GDI = 525.13. [src: soil_frontier_genomics]

Forest and cropland were therefore jointly identified as the highest-GDI biomes, rather than as meaningfully ranked separately, because the forest–cropland difference was 1.3% and no bootstrap confidence intervals were available. [src: soil_frontier_genomics] Frontier areas with GDI > 1000 had mean pH = 6.74, compared with mean pH = 5.94 in mapped areas, a +0.8 pH unit gap. This suggests a systematic under-sampling of alkaline soil microbiomes in public genomic databases, but the direction could reflect fewer 16S samples from those pH ranges rather than an assembly or annotation barrier. [src: soil_frontier_genomics]

The GDI result is not yet a validated measure of genomic discovery: because GDI = Richness / (Mean_Completeness + 1), it can equal 902 even when there are zero genomes, and it conflates OTU richness with completeness. This **qualifies** the interpretation of 16S-derived richness as evidence of functional dark matter; separate richness and completeness reporting, rarefaction-corrected GDI, bootstrap intervals, and control for 16S sampling effort are required. [src: soil_frontier_genomics]

## Functional inference and limitations

The SSO study used taxonomic profiles from 16S amplicons to infer biogeochemical functions, covering 22 functional classes at 78% coverage and 65 annotated genera at 21% coverage. [src: enigma_sso_asv_ecology]

The inferred class-level redox index ranged from 0.047 at M6 to 0.227 at U3, while genus-level inference covered 12 biogeochemical process categories. [src: enigma_sso_asv_ecology]

Genus-level functional inference covered 65 of 1,038 genera, and genus-level taxonomy covered 44% of sediment reads; species-level classification was approximately 0%, leaving 56% of reads outside the genus-level inference. [src: enigma_sso_asv_ecology]

The report treats process-abundance estimates as lower bounds because genus-level functional annotation covered only 21% of total reads. [src: enigma_sso_asv_ecology]

The functional assignments are consensus estimates based on literature-linked taxonomy rather than direct genomic evidence from the SSO populations. [src: enigma_sso_asv_ecology]

Accordingly, the inferred plume, redox ladder, and process hotspots are hypotheses that require direct geochemistry and metagenomic or isolate-genome validation rather than established measurements. [src: enigma_sso_asv_ecology]

The ENIGMA-wide analysis refines the species-level limitation: species-level biogeography was available for only 20 pangenome-linked strains with verified GTDB matches. [src: genotype_to_phenotype_enigma]

The Oak Ridge study further illustrates this limitation: 16S data could not match Fitness Browser organisms at species or strain level, and a genus such as *Pseudomonas* contains thousands of species with different ecologies. [src: lab_field_ecology]

The lignin study **supports** these cautions: its functional interpretation of lignin degradation was based on taxonomic associations and literature context, not direct gene-level pathway enrichment. The workflow retained 3,392 16S OTUs before filtering and 1,793 after prevalence and abundance filtering, and used 97% vsearch OTUs, which may merge closely related organisms. [src: lignin_community_enrichment]

The MicrobeAtlas study **refines** the detection caveat: its strict 5% within-environment prevalence filter reduced OTUs from 98,919 to 10,433 and the PGLS sample from 606 to 379 genera; the association remained positive but became non-significant (β = +0.0166, SE = 0.0099, p = 0.092). Primer bias, uneven sampling, missing environments, and heterogeneous categories therefore remain important limitations of atlas-derived niche estimates. [src: microbeatlas_metal_ecology]

The soil-frontier analysis **extends** these limitations from taxonomic functional inference to global predictability. Across 5,441 soil samples, all three predictive model families had negative out-of-sample R²: Soil & Climate, R² = −0.205 ± 0.197; Geochemical, R² = −0.331 ± 0.071; and Industrial, R² = −0.221 ± 0.042. The result does not by itself establish biological unpredictability, because spatial autocorrelation, train/test distributional shift, high-leverage outliers, batch effects, and unmeasured confounders were not separated from a genuine global-scale null. [src: soil_frontier_genomics]

The soil study's shield-efficiency test likewise found low-clay cross-validation R² = −0.268 and high-clay cross-validation R² = −0.292, with a difference of 0.024 and 95% CI: −0.423, 0.161. Because the interval includes zero, high-clay soils were not more predictable than low-clay soils. Clay remained a consistent feature with importance approximately 0.14 but did not improve predictive accuracy in high-clay soils. This **contradicts** a strong global version of the clay-shield prediction while leaving local clay effects and modelling failure unresolved. [src: soil_frontier_genomics]

## Lignin-enrichment and ecological-memory application

In the lignin experiment, 16S sequencing retained 91.2% of reads after primer trimming, 99.8% after quality filtering, and 99.8% after paired-end merging, for approximately 91% total retention; genus-level assignment was 86.5%. [src: lignin_community_enrichment]

Round-2 profiles **support** the use of 16S data for detecting ecological memory: Round-1 history explained 58.9% of variance (F=14.31, R²=0.589, p=0.002), whereas current Round-2 carbon source explained 32.7% (F=4.85, R²=0.327, p=0.018). Communities with different Round-1 histories did not converge under identical Round-2 conditions, with a reported memory index of ~0.50. [src: lignin_community_enrichment]

This result **extends** the SSO evidence for persistent spatial structure by demonstrating persistence across experimentally imposed carbon histories, but it does not establish that the mechanism is gene-level functional memory. The study proposed mapping enriched genera to pathway content through [[entities/kbase-ke-pangenome|kbase_ke_pangenome]] and functional inference of beta-ketoadipate and protocatechuate pathways as follow-up analyses. [src: lignin_community_enrichment]

## Groundwater and sediment comparison

16S profiles from groundwater and sediment collected at the same well had a median Bray–Curtis dissimilarity of 0.424, with within-well values ranging from 0.364–0.450 across 5 wells. [src: enigma_sso_asv_ecology]

Groundwater was enriched in [[entities/rhodanobacter]] at 3.62% versus 1.23% in sediment, [[entities/gallionella]] at 0.14% versus 0.01%, and [[entities/sideroxydans]] at 0.06% versus 0.01%. [src: enigma_sso_asv_ecology]

Sediment was enriched in [[entities/anaeromyxobacter]] at 1.24% versus 0.03% in groundwater, [[entities/arcobacter]] at 0.54% versus 0.00%, and [[entities/methanoperedens]] at 0.42% versus 0.00%. [src: enigma_sso_asv_ecology]

These results support a distinction between groundwater and sediment communities, but the comparison is confounded by an 18-month sampling offset between sediment collected during February–March 2023 and groundwater sampled in September 2024. [src: enigma_sso_asv_ecology]

## Temporal sampling

Groundwater 16S communities from 5 wells sampled 9 days apart showed that well identity explained 49.9% of variance, filter size explained 10.1%, depth within the saturated zone explained 2.5%, and date explained 0.8%. [src: enigma_sso_asv_ecology]

The corresponding significance values were p = 0.001 for well identity, p = 0.001 for filter size, p = 0.430 for depth, and p = 0.998 for date. [src: enigma_sso_asv_ecology]

The date-1 versus date-2 distance matrices had Mantel ρ = 0.867 and p = 0.001, indicating that well-to-well similarity rankings were nearly unchanged over the 9-day interval. [src: enigma_sso_asv_ecology]

This result supports persistent spatial structure at the 9-day groundwater timescale but does not establish long-term or seasonal stability. [src: enigma_sso_asv_ecology]

The Oak Ridge analysis adds a longer-term sampling caveat: its geochemistry measurements were point-in-time observations, and temporal mismatch between geochemical snapshots and community history may help explain the laboratory–field disconnect. [src: lab_field_ecology]

The soil-frontier analysis **supports** this caution about spatial and sampling structure: its negative out-of-sample R² values require spatial blocking and distribution-shift diagnostics before being interpreted as biological unpredictability. [src: soil_frontier_genomics]

## Limitations and related pages

The lignin experiment's n=3-per-group design limited pairwise power: the minimum achievable Mann–Whitney U p-value was 0.10, no individual OTUs reached FDR significance, and significant PERMANOVA results were accompanied by PERMDISP effects (16S p=0.0004). ITS data were even less reproducible, with within-group Bray–Curtis distances reaching 0.99–1.00 for several Round-2 groups; the planned Procrustes comparison with 16S was therefore not completed. These results **refine** interpretation of amplicon-based community differences by emphasizing replication, dispersion, and marker-specific reproducibility. [src: lignin_community_enrichment]

The SSO study's inferred functional limitations motivate the multi-omics validation needs described in [[concepts/multi-omics-integration]]. [src: enigma_sso_asv_ecology]

Its Oak Ridge application **supports** linking community composition to field chemistry, but **refines** that link by motivating species- or strain-level matching, multivariate CCA or RDA controlling for pH, redox, and carbon sources, temporal sampling, and metal-specific fitness scores. [src: lab_field_ecology]

The lignin study similarly proposed larger replication, DADA2 ASV analysis, UniFrac and phylogenetic-diversity analyses, deeper ITS sequencing, intermediate time points, and KBase Data Lakehouse cross-referencing of Pseudomonas, Acinetobacter, and Comamonas through [[entities/kbase-ke-pangenome|kbase_ke_pangenome]]. [src: lignin_community_enrichment]

The MicrobeAtlas study **extends** these validation needs by recommending multi-primer, multi-region surveys, finer subdivision of aquatic environments, alternative phylogenetic models, and genus-to-genome coverage diagnostics before treating atlas-derived niche breadth as ecological range. [src: microbeatlas_metal_ecology]

The soil-frontier study **extends** the same provenance and coverage requirements to soil discovery maps. It recommends decomposing negative R² into distributional shift, outlier leverage, and true unpredictability using spatial blocking; computing rarefaction-corrected GDI after uniform 16S sequencing-depth correction; estimating bootstrap 95% CIs for biome-level GDI rankings; controlling pH discovery bias for the number of 16S samples per pH bin; and reporting forest versus cropland GDI with uncertainty. These validations require re-running from BERIL Observatory 16S tables and `kbase_ke_pangenome` completeness data because no local CSV output is available. [src: soil_frontier_genomics]

16S amplicon sequencing supports the environment-linked community-structure analysis in [[concepts/ecotype-environment-gene-content]]. [src: enigma_sso_asv_ecology]

The method and its findings are summarized in [[summaries/enigma_sso_asv_ecology__REPORT]], [[summaries/genotype_to_phenotype_enigma__REPORT]], [[summaries/lab_field_ecology__REPORT]], [[summaries/lignin_community_enrichment__REPORT]], [[summaries/microbeatlas_metal_ecology__REPORT]], and [[summaries/soil_frontier_genomics__REPORT]]. [src: enigma_sso_asv_ecology, genotype_to_phenotype_enigma, lab_field_ecology, lignin_community_enrichment, microbeatlas_metal_ecology, soil_frontier_genomics]
