---
type: "Method"
description: "The Kruskal-Wallis test, a rank-based test for differences among three or more groups, as applied across BERIL projects to resistome, fitness-cost, eukaryotic-admixture, growth-rate and metabolic-pathway comparisons."
sources: ["summaries/adp1_triple_essentiality__REPORT.md", "summaries/amr_environmental_resistome__REPORT.md", "summaries/amr_fitness_cost__REPORT.md", "summaries/amr_pangenome_atlas__REPORT.md", "summaries/euk_in_prok_correlates__REPORT.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md"]
---
The Kruskal-Wallis test (often reported as "KW" or "Kruskal H") is a rank-based method for testing whether three or more groups differ. In this corpus it is used to compare antimicrobial-resistance (AMR) gene content across environments, AMR fitness costs across mechanisms, eukaryotic DNA fraction across sample types, sites and vegetation, growth rates across metabolic-model classes, and pathway completeness across ecosystems. [src: amr_environmental_resistome, amr_fitness_cost, amr_pangenome_atlas, euk_in_prok_correlates, adp1_triple_essentiality, nmdc_community_metabolic_ecology]

## Uses in the corpus

### Environmental resistome

Species from clinical sources have a median of 5 AMR gene clusters, compared with 2 for soil, aquatic and host-associated species. Human gut species resemble clinical species, with a median of 5. The Kruskal-Wallis result is H = 781.9, p = 9.4×10⁻¹⁶⁷, η² = 0.056. Of 15 pairwise environment comparisons, 13 remain significant after FDR (false discovery rate) correction. The largest effect is clinical versus aquatic (rank-biserial r = −0.49). These results are reported in [[summaries/amr_environmental_resistome__REPORT]] and feed [[concepts/environmental-resistome]]. [src: amr_environmental_resistome]

Resistome composition also differs across environments. In clinical species, 68% of AMR is accessory (acquired); in soil species the figure is 43%. The Kruskal-Wallis result is H = 506.0, p = 4×10⁻¹⁰⁷, η² = 0.036. [src: amr_environmental_resistome]

| Mechanism tested by environment | KW H | p | η² | Source |
|---|---|---|---|---|
| Metal | 1498.4 | ~0 | 0.107 | [src: amr_environmental_resistome] |
| Target modification | 1394.9 | 1.7×10⁻²⁹⁹ | 0.100 | [src: amr_environmental_resistome] |
| Efflux | 768.0 | 9.8×10⁻¹⁶⁴ | 0.055 | [src: amr_environmental_resistome] |
| Enzymatic inactivation | 266.0 | 2.0×10⁻⁵⁵ | 0.019 | [src: amr_environmental_resistome] |

The table above lists the project's per-mechanism H3 tests. Each test compares one mechanism's fraction across environments, but these fractions cover only the classified clusters. 18.7% of AMR clusters (15,550) could not be assigned a mechanism from gene name or product annotation, and the project excluded them from the mechanism fractions. [src: amr_environmental_resistome]

The project's `data/mechanism_by_environment.csv` output holds these per-mechanism results in 4 rows. [src: amr_environmental_resistome]

### Pangenome-scale AMR atlas

An independent pangenome analysis reports a similar pattern; it **supports** the clinical-enrichment result above. Human/Clinical species carry 10.6 AMR clusters per species (n=2,248). The comparison groups are Soil/Terrestrial at 4.6 (n=2,469), Aquatic at 3.9 (n=1,827) and Animal at 3.0 (n=959). The Kruskal-Wallis result is H=440, p=7.0e-93. Clinical AMR is also less core (30.8%) than soil AMR (58.1%) or plant AMR (63.1%). Caveat: of the 14,723 AMR-carrying species, only 7,838 (53.2%) received an environment classification other than "Other/Unknown", and the test is restricted to these species across 6 categories ([[summaries/amr_pangenome_atlas__REPORT]]). [src: amr_pangenome_atlas]

### Eukaryotic DNA admixture in prokaryotic metagenomes

In a univariate test across studies, the eukaryotic fraction differs strongly across sample matrix (Kruskal–Wallis H=77.8, p=1.3×10⁻¹⁷). All pairwise matrix contrasts are significant after BH-FDR, the Benjamini-Hochberg false-discovery-rate correction ([[entities/benjamini-hochberg-fdr]]). This result should not be read as an environment effect. The project calls the study/batch confounding its central methodological result: each biome is ~80–100% nested within a single study. When whole studies are held out, the environment model does not generalize (out-of-study detection AUC = 0.56 ≈ chance). The matrix association is therefore largely batch-driven. This feeds [[concepts/eukaryotic-dna-admixture-in-prokaryotic-metagenomes]] and [[concepts/study-batch-confounding-of-environmental-associations]]. [src: euk_in_prok_correlates]

The vegetation and geography tests below differ in kind. They are run within a single [[entities/neon]] soil metagenome study (1,186 runs, constant protocol/batch), so batch is held constant. Within this study, the eukaryotic fraction differs across 11 local-vegetation levels (`env_local_scale`; Kruskal H=119.1, p=7.6×10⁻²¹). It is highest in sedge/forb herbaceous soil (median 23%), followed by emergent wetland (14%), dwarf scrub (13%) and evergreen forest (2%). It is ≈0 in deciduous forest, cropland and pasture. [src: euk_in_prok_correlates]

Within the same NEON soil study, the eukaryotic fraction also differs by geography across 47 sites (Kruskal H=310.4, p=2.4×10⁻⁴⁶). It is highest at Arctic tundra sites: Utqiaġvik 30%, Caribou-Poker Creeks 22% and Toolik 17%. Temperate forests range from 2–8%. [src: euk_in_prok_correlates]

### Community metabolic ecology

In the NMDC community metabolic ecology project, H1 used [[entities/spearman-correlation]] with BH-FDR. H2 combined [[entities/principal-component-analysis]] with Kruskal-Wallis tests of ecosystem separation. The figure `figures/pathway_completeness_boxplot.png` shows amino-acid pathway completeness by ecosystem type, with Kruskal-Wallis significance marked. [src: nmdc_community_metabolic_ecology]

## Null results

In the ADP1 triple-essentiality project, the test covered only the 478 triple-covered genes (genes with TnSeq, FBA and growth data). All of these genes are TnSeq-dispensable on minimal media. Within this restricted set, mean growth rates did not differ significantly across FBA (flux balance analysis; [[entities/flux-balance-analysis]]) classes (Kruskal-Wallis H = 1.67, p = 0.43). The null result does not extend to TnSeq-essential genes. [src: adp1_triple_essentiality]

In the AMR fitness-cost project, the test detected no significant difference in AMR-gene fitness cost by resistance mechanism, contrary to that project's H2. Four testable mechanisms were compared: efflux (N=254), enzymatic inactivation (N=304), metal resistance (N=144) and unknown (N=74). The result was H = 0.65, p = 0.89. A non-significant test does not show that costs are equal across mechanisms. The figure `h2_mechanism_stratification.png` plots fitness by mechanism with this test. The result bears on [[concepts/antimicrobial-resistance-fitness-cost]]. [src: amr_fitness_cost]

## Caveats

Several environment comparisons combine extremely small p-values with modest effect sizes. Examples are η² = 0.056 for AMR cluster counts and η² = 0.036 for accessory fraction. With thousands of species, significance alone overstates the share of variance explained by environment. [src: amr_environmental_resistome]

In the pangenome atlas, the test is restricted to environment-classified species, so its Kruskal-Wallis result covers only about half of AMR-carrying species. It is not a full census. [src: amr_pangenome_atlas]

In these projects, pairwise follow-ups are reported with FDR correction: 13 of 15 comparisons significant in one project, and all matrix contrasts significant in the other. Pairwise effect sizes such as rank-biserial r are reported alongside them; see [[entities/mann-whitney-u-test]] for the two-group analogue. [src: amr_environmental_resistome, euk_in_prok_correlates]
