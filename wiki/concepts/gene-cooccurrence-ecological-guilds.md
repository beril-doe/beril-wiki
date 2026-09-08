---
type: Concept
description: Gene co-occurrence can reveal ecological guilds without proving physical
  linkage
sources:
- id: pgp_pangenome_ecology
  resource: ../summaries/pgp_pangenome_ecology__REPORT.md
  title: pgp pangenome ecology
- id: ecotype_analysis
  resource: ../summaries/ecotype_analysis__REPORT.md
  title: ecotype analysis
- id: cofitness_coinheritance
  resource: ../summaries/cofitness_coinheritance__REPORT.md
  title: cofitness coinheritance
- id: plant_microbiome_ecotypes
  resource: ../summaries/plant_microbiome_ecotypes__REPORT.md
  title: plant microbiome ecotypes
- id: pangenome_openness
  resource: ../summaries/pangenome_openness__REPORT.md
  title: pangenome openness
title: Gene co-occurrence can reveal ecological guilds without proving physical linkage
---
# Gene co-occurrence can reveal ecological guilds without proving physical linkage

Gene co-occurrence is useful for identifying ecological guilds: recurring combinations of genes can indicate shared environmental selection or complementary ecological roles. However, co-occurrence across genomes does not establish that genes are physically linked in the same operon, genomic island, or locus. [^pgp_pangenome_ecology]

## Evidence from plant-growth-promoting genes

The [pgp_pangenome_ecology__REPORT](../summaries/pgp_pangenome_ecology__REPORT.md) analyzed 13 plant-growth-promoting gene markers across 27,702 species, including 32,736 PGP gene clusters. [^pgp_pangenome_ecology] Eight of 10 focal-gene pairs were significantly associated after Benjamini–Hochberg false-discovery-rate (BH-FDR) correction, with five positive and three negative associations. [^pgp_pangenome_ecology]

The strongest positive association was between [pqqc](../entities/pqqc.md) and [acds](../entities/acds.md), with odds ratio (OR) = 7.24, n = 286 co-occurring species, and q = 1.2e-83. [^pgp_pangenome_ecology] [pqqc](../entities/pqqc.md) also co-occurred significantly with [hcnc](../entities/hcnc.md) (OR = 1.91) and [ipdc](../entities/ipdc.md) (OR = 1.55), forming a putative non-diazotrophic rhizosphere-effectiveness module. [^pgp_pangenome_ecology]

This pattern supports the use of co-occurrence to identify an ecological guild, because the genes recur together more often than expected under the tested association model. [^pgp_pangenome_ecology] It does not prove that [pqqc](../entities/pqqc.md), [acds](../entities/acds.md), [hcnc](../entities/hcnc.md), and [ipdc](../entities/ipdc.md) occupy the same genomic neighborhood or are transferred as one unit. [^pgp_pangenome_ecology]

The negative associations involving [nifh](../entities/nifh.md) further refine the guild interpretation. nifH was negatively associated with hcnC (OR = 0.23, q = 5.8e-29) and pqqC (OR = 0.57, q = 2.9e-19), while its association with ipdC was not significant (OR = 1.13, q = 0.54). [^pgp_pangenome_ecology] These results support ecological separation between diazotrophs and pqqC/acdS-bearing rhizobacteria in this dataset, rather than proving mutually exclusive genomic architectures. [^pgp_pangenome_ecology]

Only 157 species (1.4%) carried at least three focal traits, indicating that broad multi-trait combinations were uncommon in the analyzed species set. [^pgp_pangenome_ecology] The most common reported multi-trait genotype was pqqC + acdS (n = 153), while nifH + pqqC was reported at n = 225 despite the negative genome-wide association between those genes. [^pgp_pangenome_ecology] This illustrates why pairwise association statistics and genotype counts should be interpreted together rather than treated as interchangeable evidence of a single guild. [^pgp_pangenome_ecology]

## Environmental support and qualification

The co-occurrence pattern was accompanied by environmental differentiation. Among 1,039 soil/rhizosphere species and 10,233 species from other environments, acdS prevalence was 15.8% versus 2.6% (OR = 7.02, q = 5.1e-62), pqqC prevalence was 43.8% versus 21.2% (OR = 2.90, q = 2.8e-53), and hcnC prevalence was 11.3% versus 6.4% (OR = 1.85, q = 6.1e-08). [^pgp_pangenome_ecology] nifH was depleted in soil-classified species, with prevalence of 12.9% versus 19.7% (OR = 0.60, q = 5.5e-08). [^pgp_pangenome_ecology]

The acdS enrichment remained strong after phylum-level fixed effects in logistic regression (OR = 6.98, p = 4.8e-61) and in a strict rhizosphere-only sensitivity analysis using genomes whose isolation source contained “rhizosphere” or “root nodule” (OR = 10.6, q = 7.6e-38). [^pgp_pangenome_ecology] The agreement between gene co-occurrence and environment-stratified prevalence supports an ecological-guild interpretation more strongly than co-occurrence alone. [^pgp_pangenome_ecology]

The [ecotype_analysis__REPORT](../summaries/ecotype_analysis__REPORT.md) **refines** this interpretation by showing that environmental similarity was generally weak for whole-genome gene-content similarity: across 172 species, phylogeny generally dominated, with a median partial correlation of 0.0025 for environment versus 0.0143 for phylogeny, and no significant environmental effect in 156 species (90.7%). [^ecotype_analysis] This does not contradict the gene-specific environmental enrichments above; instead, it supports the hypothesis that ecological selection may be concentrated in particular gene subsets rather than expressed as a strong whole-genome signal. [^ecotype_analysis]

The [pangenome_openness__REPORT](../summaries/pangenome_openness__REPORT.md) **supports** this qualification: among species with both pangenome statistics and ecotype-analysis results, pangenome openness was not significantly related to either environment effect (Spearman rho = -0.05, p-value = 0.54) or phylogeny effect (Spearman rho = 0.03, p-value = 0.73). [^pangenome_openness] Thus, an open or closed pangenome did not predict which broad driver dominated gene-content variation, reinforcing that gene-specific ecological signals should not be inferred from a single whole-pangenome summary metric. [^pangenome_openness] The report further treats the possibility that core/accessory labels miss functionally adaptive genes, or that horizontal gene transfer is opportunistic rather than environmentally patterned, as hypotheses rather than demonstrations. [^pangenome_openness]

The [plant_microbiome_ecotypes__REPORT](../summaries/plant_microbiome_ecotypes__REPORT.md) **refines** the complementary-function interpretation: corrected analysis of plant-associated co-occurring genus pairs found them slightly less complementary than random pairs, with Cohen’s d ≈ −0.4 and permutation p < 0.001; prevalence-weighted aggregation gave d = −0.39. [^plant_microbiome_ecotypes] Thus, gene co-occurrence can still mark shared selection or ecological guild structure, but co-occurrence should not be treated as evidence that partners provide complementary metabolic functions. [^plant_microbiome_ecotypes]

BacDive metabolite-utilization data agreed with GapMind predictions at 83.1% consistency, supporting the reliability of the pathway completeness scores, although the GapMind core-level completeness score was 0% across compartments and may be too stringent for broad taxonomic comparisons. [^plant_microbiome_ecotypes] The refined C-score test was structurally underpowered: among 69 NMDC co-occurring genera, there were 0 PGP-dominant, 3 pathogen-dominant, and 66 dual-or-mixed genera. [^plant_microbiome_ecotypes] This **supports** retaining prevalence- and power-aware null models when translating co-occurrence into functional complementarity claims. [^plant_microbiome_ecotypes]

Evidence from [cofitness_coinheritance__REPORT](../summaries/cofitness_coinheritance__REPORT.md) further **refines** this gene-specific interpretation: across 9 organisms, pairwise laboratory co-fitness produced only a weak positive co-occurrence signal, with mean delta phi (cofit minus prevalence-matched random pairs) of +0.011 across organisms and aggregate delta = +0.003, despite aggregate Mann-Whitney p=1.66e-29; the across-organism Wilcoxon signed-rank test was not significant (W=9, p=0.13). [^cofitness_coinheritance] Thus, co-occurrence can support a guild hypothesis, but pairwise functional similarity is not a uniformly strong predictor of genomic co-occurrence across taxa. [^cofitness_coinheritance]

This pattern connects to [ecotype-environment-gene-content](ecotype-environment-gene-content.md), because the gene combinations and their negative or positive associations corresponded to different environmental distributions. [^pgp_pangenome_ecology] It also complements [module-level-coinheritance](module-level-coinheritance.md), while leaving open whether the observed module is physically coinherited or instead assembled repeatedly by ecological selection. [^pgp_pangenome_ecology]

## Co-occurrence is not physical linkage

The report explicitly notes that co-occurrence does not establish physical linkage. [^pgp_pangenome_ecology] The pqqC–acdS association could reflect a shared habitat, complementary functions, correlated lineage structure, repeated independent acquisition, or physical linkage, and the reported analysis does not distinguish among these mechanisms. [^pgp_pangenome_ecology]

The cofitness analysis **supports** this caution: only 0.7% of its cofit pairs were genomically adjacent within 5 genes, and excluding adjacent pairs did not change the result pattern. [^cofitness_coinheritance] Its stronger signal arose instead at the coordinated multi-gene level: across 195 independent component analysis (ICA) modules in 6 organisms, within-module co-occurrence exceeded a prevalence-matched null by delta phi = +0.053; 51/195 modules were significant at p<0.05 and 21/195 remained significant at q<0.05 after BH-FDR correction. [^cofitness_coinheritance] This supports interpreting recurring gene sets as possible selective or ecological units without equating statistical co-inheritance with a physically linked cassette. [^cofitness_coinheritance]

The core/accessory results also caution against assuming that a co-occurring pair is a horizontally transferred cassette. [^pgp_pangenome_ecology] All 13 PGP genes had higher core fractions than the 46.8% genome-wide baseline, and pqqC was 81.5% core, 7.8% auxiliary, and 10.7% singleton, whereas acdS was 70.4% core, 13.4% auxiliary, and 16.2% singleton. [^pgp_pangenome_ecology] Thus, the pqqC–acdS guild signal is compatible with predominantly conserved gene distributions rather than requiring a single mobile element. [^pgp_pangenome_ecology] The null relationship between openness and broad environment or phylogeny effects **supports** treating these core/accessory summaries as insufficient on their own to identify the adaptive or mobile basis of a guild. [^pangenome_openness]

The [plant_microbiome_ecotypes__REPORT](../summaries/plant_microbiome_ecotypes__REPORT.md) **refines** this conclusion by showing that HGT indicators are scale-dependent: species carrying singleton plant-interaction marker clusters were 16 times more likely to carry transposase or integrase singletons (Fisher OR = 15.95, p = 8.8e-20), yet marker singletons had an overall enrichment ratio of 0.78 relative to the genomic average. [^plant_microbiome_ecotypes] At genus scale, plant-associated genera had a median 3.7 mobile elements per genome versus 2.8 in non-plant genera (Mann–Whitney p = 1.49×10⁻⁵). [^plant_microbiome_ecotypes] These mixed scales support testing mobility directly rather than inferring a transferred cassette from co-occurrence.

The ICA results **refine** this conclusion by showing stronger co-inheritance for accessory modules: accessory modules had mean delta phi +0.108, compared with +0.059 for core modules and +0.031 for mixed modules, although the accessory-versus-core difference trended toward significance (Mann-Whitney p=0.051). [^cofitness_coinheritance] This makes accessory gene sets plausible candidates for ecological guilds or coordinated selective units, but does not establish that their members share physical loci. [^cofitness_coinheritance]

The analysis also identified pqqD as an exception, with 55.5% core and 27.5% singleton status, suggesting that pqqD can sometimes spread as a standalone gene. [^pgp_pangenome_ecology] This distinction between statistical co-occurrence, shared ecological function, and physical coinheritance is central to interpreting [gene-cooccurrence-ecological-guilds](gene-cooccurrence-ecological-guilds.md). [^pgp_pangenome_ecology]

## Interpretation limits

The environmental classification was conservative and noisy: 1,637 species (5.9% of species with an environment label) were classified as soil/rhizosphere dominant, while 291,279 genomes had isolation-source metadata and 93.5% were classifiable. [^pgp_pangenome_ecology] NCBI sampling is biased toward clinical and host-associated genomes, so the observed acdS and pqqC enrichment may underestimate true rhizosphere enrichment. [^pgp_pangenome_ecology]

The ecotype analysis further **refines** this limitation: AlphaEarth embeddings covered only 28.4% of genomes, and geographic coordinates were often missing or imprecise; for host-associated organisms they may describe collection sites rather than biologically relevant microenvironments. [^ecotype_analysis] Its partial-correlation framework also assumed linear relationships between distance matrices, so weak whole-genome environmental effects may reflect both biology and limited environmental representation. [^ecotype_analysis]

The pangenome-openness analysis adds that its sample was limited to species with both pangenome statistics and ecotype-analysis results, and that openness is only a single summary metric; the upstream ecotype analysis also had limited power for some species with few genomes. [^pangenome_openness] These caveats **support** interpreting its null correlations as limits on prediction by this metric, not as proof that pangenome structure is independent of ecological dynamics. [^pangenome_openness]

The cofitness study adds a related prevalence limitation: its strongest co-fitness pairs were often core genes with near-universal prevalence, producing a prevalence ceiling with little co-occurrence variance; co-fitness strength was weakly anti-correlated with co-occurrence (Spearman rho=-0.109, p<1e-300 across 1.04M pairs). [^cofitness_coinheritance] This **supports** treating accessory enrichment and prevalence-matched nulls as important qualifications when translating pairwise co-occurrence into ecological claims. [^cofitness_coinheritance]

The plant-microbiome analysis **supports** an additional caution about marker-defined guilds: 878 of 1,115 plant-associated species (78.7%) were classified as dual-nature under refined marker rules, but categorical cohorts did not usefully discriminate a curated validation panel; all 14 known beneficial or pathogenic species were dual-nature and all four neutral controls were misclassified. [^plant_microbiome_ecotypes] This supports interpreting marker co-occurrence as a coarse ecological screen, not as proof of a unified phenotype or co-expressed guild.

PGP detection relied on Bakta annotations matching exact gene names such as nifH, acdS, and pqqC, so product-only annotations and variant gene names could have been missed. [^pgp_pangenome_ecology] Gene clusters were not functionally validated for truncations, frameshifts, or pseudogenization, meaning that an annotated co-occurring cluster was not necessarily functional. [^pgp_pangenome_ecology]

Phylogenetic structure and uneven sampling can also contribute to apparent co-occurrence, so the guild interpretation should be tested with lineage-aware models and genome-context analyses. [^pgp_pangenome_ecology] The cofitness analysis likewise found higher mean phi among near genomes than medium-distance genomes (0.102 versus 0.067), while most species lacked genomes in the far stratum (>0.05 branch distance), limiting separation of functional coupling from shared ancestry. [^cofitness_coinheritance] These limitations connect the concept to [phylogenetic-confounding-of-pangenome-associations](phylogenetic-confounding-of-pangenome-associations.md), [environmental-resistome](environmental-resistome.md), and [evidence-triangulation-for-functional-annotation](evidence-triangulation-for-functional-annotation.md).

## Tensions

The PGP analysis supports a pqqC–acdS ecological-guild interpretation through strong pairwise association and environmental enrichment, while the plant-microbiome complementarity analysis found co-occurring genus pairs slightly less complementary than random pairs (Cohen’s d ≈ −0.4, permutation p < 0.001). [^pgp_pangenome_ecology] [^plant_microbiome_ecotypes] These findings are not mutually exclusive: the tension is whether a guild denotes shared environmental selection or complementary metabolic provisioning, and it should not be resolved without pathway- and activity-level tests.

The pangenome-openness analysis found no significant relationship between openness and either environment or phylogeny effects (Spearman rho = -0.05, p-value = 0.54; Spearman rho = 0.03, p-value = 0.73), whereas the PGP analysis found strong environment-associated enrichment for particular genes, including acdS and pqqC. [^pangenome_openness] [^pgp_pangenome_ecology] This is a scale and representation tension rather than a direct contradiction: a whole-pangenome openness metric may fail to predict broad eco-phylogenetic structure while selected gene subsets retain environmental associations.

## Open Directions

- Use complete or well-assembled genomes from the pqqC–acdS-positive set, together with operon and genomic-island analysis, to test whether the two genes are physically linked or occur at separate loci. [^pgp_pangenome_ecology]
- Apply phylogeny-aware co-occurrence models to the PGP gene matrix and ask whether the pqqC–acdS association persists after accounting for shared ancestry. [^pgp_pangenome_ecology]
- Compare gene neighborhoods, synteny, mobile-element context, and gene-tree reconciliation for pqqC, acdS, hcnC, and ipdC to distinguish vertical conservation from repeated horizontal acquisition. [^pgp_pangenome_ecology]
- Reanalyze nifH associations after stratifying by environment, lineage, and diazotrophic ecological context to determine whether the negative nifH–pqqC and nifH–hcnC associations reflect ecological separation or sampling structure. [^pgp_pangenome_ecology]
- Functionally validate representative co-occurring clusters with transcript or phenotype data to test whether annotated pqqC, acdS, hcnC, and ipdC genes are active components of the proposed guild. [^pgp_pangenome_ecology]
- Reanalyze gene-specific guild associations with alternative environmental distances and direct metadata, then compare them with whole-genome and ecotype-cluster contrasts to test whether environmental signal is concentrated in selected loci. [^ecotype_analysis]
- Stratify pangenome openness analyses by gene function, including L (mobile) and V (defense) categories, and test auxiliary fraction, Heap’s law alpha, and pangenome fluidity to determine whether specific functional subsets recover environment-associated guild signals. [^pangenome_openness]
- Test openness-by-lifestyle interactions, such as open pathogen versus open environmental species comparisons, rather than treating openness as a universal predictor. [^pangenome_openness]
- Restrict co-fitness comparisons to auxiliary-only pairs below 95% prevalence and test whether the pairwise guild signal strengthens after removing the prevalence ceiling. [^cofitness_coinheritance]
- Build module co-transfer networks and compare their accessory-module membership with environmental gene guilds, testing whether multi-gene co-inheritance predicts ecological distribution better than pairwise co-occurrence. [^cofitness_coinheritance]
- Test the plant-associated co-occurrence and complementarity tension with reaction-level pathway comparisons, transcript measurements, and direct mobile-element or gene-neighborhood data. [^plant_microbiome_ecotypes]

[^pgp_pangenome_ecology]: [pgp pangenome ecology](../summaries/pgp_pangenome_ecology__REPORT.md)
[^ecotype_analysis]: [ecotype analysis](../summaries/ecotype_analysis__REPORT.md)
[^pangenome_openness]: [pangenome openness](../summaries/pangenome_openness__REPORT.md)
[^plant_microbiome_ecotypes]: [plant microbiome ecotypes](../summaries/plant_microbiome_ecotypes__REPORT.md)
[^cofitness_coinheritance]: [cofitness coinheritance](../summaries/cofitness_coinheritance__REPORT.md)
