---
type: "Concept"
description: "Whether genome GC content differs among isolation environments within and across species after phylogenetic control, and how it contrasts with phylogeny-dominated gene content; stops at mechanisms."
sources: ["summaries/gc_ecotype_ecology__REPORT.md"]
---
# Genome GC content as an ecological signal

This page covers genome GC content as an ecological signal: whether it differs among isolation environments within and across species after phylogenetic control, and how that contrasts with phylogeny-dominated gene content. In 108 well-sampled bacterial species, 40 (37%) show a within-species association with isolation source after ANI (average nucleotide identity) cluster control. [src: gc_ecotype_ecology] The evidence comes from one project and is observational, and the effects are small. [src: gc_ecotype_ecology] The report's central question is whether GC content still carries an ecological signal once intra-species phylogeny is controlled. [src: gc_ecotype_ecology] A case study of *Burkholderia vietnamiensis* gives a single-species answer that the report reads as yes. [src: gc_ecotype_ecology] For the full report see [[summaries/gc_ecotype_ecology__REPORT]]. Mechanisms are covered in [[concepts/mechanisms-of-ecology-linked-gc-shifts]].

## Literature Context

The candidate papers give background on GC content and habitat, mostly from comparative genomics of single taxa or genera. They do not test the within-species, phylogeny-controlled question this page asks. A broad analysis of eubacteria argues that mutator genes, especially polC and dnaE2, play dominant roles in determining GC variability [PMID 22230424](https://pubmed.ncbi.nlm.nih.gov/22230424/). That paper treats genome size, temperature, oxygen requirement and habitat as subsidiary factors, or as acting indirectly through the mutator genes. It also reports that most terrestrial, plant-associated and nitrogen-fixing bacteria are members of the dnaE1|dnaE2 group, while most aquatic bacteria are largely dnaE1|polV. It says it is unclear whether GC changes relate directly to environmental pressure [PMID 22230424](https://pubmed.ncbi.nlm.nih.gov/22230424/). Mechanisms are left to [[concepts/mechanisms-of-ecology-linked-gc-shifts]].

Habitat-linked GC differences also appear in more focused studies. Human-specific *Anaerobutyricum hallii* and *A. soehngenii* are reported to have longer genomes and lower GC content than the rest of the genus, in an analysis of 84 genomes [PMID 41109491](https://pubmed.ncbi.nlm.nih.gov/41109491/). In a metagenomic study of 44 European freshwater lakes, nutrient availability was linked to genome size, %GC and functional properties, consistent with genome streamlining under low nutrients [PMID 38881319](https://pubmed.ncbi.nlm.nih.gov/38881319/). In 1020 *Lactobacillus* genomes, the *L. delbrueckii* clade showed GC variation fivefold greater than that seen in other bacterial genera. Individual gene analyses found no consistent link between habitat adaptation and phylogenetic proximity [PMID 39900839](https://pubmed.ncbi.nlm.nih.gov/39900839/). Within one genome, the *Rhizobium leguminosarum* core is higher in G+C than the accessory component on plasmids and chromosomal islands [PMID 16640791](https://pubmed.ncbi.nlm.nih.gov/16640791/). That is a within-genome contrast, not a between-environment one. These papers are based on abstracts, and none controls for intra-species phylogeny.

The corpus's pooled comparison, which puts soil and plant categories above aquatic and host/gut categories, is consistent with this across-lineage background. It is also consistent with the mutator-gene report that terrestrial and plant-associated bacteria sit in a distinct group [PMID 22230424](https://pubmed.ncbi.nlm.nih.gov/22230424/). The corpus's pooled comparison does not control for phylogeny, so it cannot separate habitat from ancestry. The lake and *Anaerobutyricum* findings are compatible with environment-linked GC, but they operate at genus or community level [PMID 38881319](https://pubmed.ncbi.nlm.nih.gov/38881319/) [PMID 41109491](https://pubmed.ncbi.nlm.nih.gov/41109491/).

The central corpus claim extends this literature. In 108 well-sampled species, 40 (37%) show an association between GC and isolation source after ANI cluster control, with small effects (median max-minus-min 0.15%). I found no candidate paper that tests this within species with phylogenetic control, so the result is novel relative to these candidates. The *Lactobacillus* finding of no consistent habitat–phylogeny correlation in individual genes [PMID 39900839](https://pubmed.ncbi.nlm.nih.gov/39900839/) fits the corpus contrast with gene content, which is phylogeny-dominant in 60.5% of 172 species. The mutator-gene account [PMID 22230424](https://pubmed.ncbi.nlm.nih.gov/22230424/) offers a candidate mechanism for the small shifts. The corpus has not tested it, and the observational design cannot exclude hidden confounders.

## Across-species background

The report describes the across-species link between GC and lifestyle as well known. Obligate intracellular bacteria have low GC, and soil and plant-associated bacteria tend to have high GC. [src: gc_ecotype_ecology] Within communities, GC tracks soil carbon, pH and metabolic strategy. [src: gc_ecotype_ecology]

The report checked this with a pooled comparison. Free-text isolation_source was mapped to 14 broad categories with conservative regex rules that favour "other" or unknown. [src: gc_ecotype_ecology] Pooled across species, mean GC (%) and genome counts were:

| Category | Mean GC (%) | Genomes |
|---|---|---|
| plant_microbiome | 60.9 | 384 [src: gc_ecotype_ecology] |
| plant_host | 56.2 | 5,919 [src: gc_ecotype_ecology] |
| soil | 55.0 | 9,087 [src: gc_ecotype_ecology] |
| freshwater | 53.3 | 9,315 [src: gc_ecotype_ecology] |
| wastewater | 52.2 | 3,648 [src: gc_ecotype_ecology] |
| extreme | 50.2 | 724 [src: gc_ecotype_ecology] |
| marine | 48.7 | 4,974 [src: gc_ecotype_ecology] |
| human_clinical | 48.1 | 57,950 [src: gc_ecotype_ecology] |
| animal_host | 46.9 | 9,718 [src: gc_ecotype_ecology] |
| gut_environmental | 46.0 | 17,152 [src: gc_ecotype_ecology] |
| food | 41.8 | 6,679 [src: gc_ecotype_ecology] |

The report reads the soil/plant > aquatic > host/gut order as the expected pattern and as a positive control for its categories. [src: gc_ecotype_ecology] This pooled comparison does not control for phylogeny.

## Within-species signal after phylogenetic control

In 108 species, each with at least 50 quality-filtered genomes and at least 2 environmental categories with at least 10 genomes each, 40 species (37%) had GC variation associated with isolation source. This holds after controlling for intra-species ANI cluster at FDR (false discovery rate) < 0.05. [src: gc_ecotype_ecology] The report concludes that about 40% of well-sampled species carry such a signal. [src: gc_ecotype_ecology] A separate analysis with an independent AlphaEarth axis reports 53 of 131 species (40%) significant with FDR correction. [src: gc_ecotype_ecology] Of 17 species testable by both definitions, 10 (59%) were significant. [src: gc_ecotype_ecology] See [[concepts/independent-continuous-environment-embeddings-versus-categorical-isolation-source]] for the comparison of the two definitions.

### Robustness checks

The report states that the signal survives the ANI cluster fixed effect, a permutation null and an alternative continuous environmental measurement. [src: gc_ecotype_ecology] It also says the signal is spread across taxa and habitats rather than concentrated in one clade. [src: gc_ecotype_ecology]

- **Permutation null.** Isolation labels were shuffled within species 200 times. 39 of 40 species were retained at empirical p < 0.05, and 29 of 40 at p < 0.01. [src: gc_ecotype_ecology]
- **Continuous phylogenetic control.** The ANI cluster term was replaced with a PCoA (principal coordinates analysis) of pairwise branch distances. 32 of 39 testable species (82%) stayed significant. The report takes this as showing the cluster definition was not driving the result. [src: gc_ecotype_ecology]
- **Geographic sensitivity.** Latitude and longitude were added as covariates. 12 of 16 testable species (75%) stayed significant. [src: gc_ecotype_ecology] These were species with at least 30 geo-bearing genomes, and the report says the effect is not just a proxy for geographic structure. [src: gc_ecotype_ecology]

### Caveats

The result is associational and observational. Without strain-replicate transplant experiments, hidden confounders such as geographic sampling bias correlated with isolation source cannot be excluded. [src: gc_ecotype_ecology] The permutation null rules out random label associations within species, but not all confounders. [src: gc_ecotype_ecology]

## Effect sizes

Effects are small. Across significant species the max-minus-min mean GC across categories has median 0.15% (IQR 0.09 – 0.30%, max 0.88%). [src: gc_ecotype_ecology] The report gives a typical range of 0.1–0.9%. [src: gc_ecotype_ecology] The partial R² of isolation category given ANI cluster has median 12.3% (IQR 4.3 – 22.7%). [src: gc_ecotype_ecology] The report calls these shifts small beside the ≈ 30% across-species GC range, but statistically robust, reproducible and biologically meaningful. [src: gc_ecotype_ecology] It reads them as consistent with fine-grained selective or mutational pressure rather than ancestral inheritance. [src: gc_ecotype_ecology]

### Strongest cases

The report singles out ecotype-spanning species where genomes come from genuinely different niches: *Vibrio parahaemolyticus*, *Burkholderia vietnamiensis*, *Klebsiella quasipneumoniae*, *Lactiplantibacillus plantarum* and *Bacillus anthracis*. [src: gc_ecotype_ecology] It notes that the first four of these (excluding *B. anthracis*) have the largest effects and span niches differing in recombination rate and likely oxidative environment, such as soil/plant versus gut/clinical. [src: gc_ecotype_ecology] *V. parahaemolyticus* is the cleanest case. It has 999 genomes across 6 categories, 346 ANI clusters, partial R² = 22.8%, max-min GC = 0.36% and q = 1.3e-32. [src: gc_ecotype_ecology] The analyzed taxon is *V. parahaemolyticus* sensu stricto, whose epidemiology and host range span ecotypes, and the report says its within-species GC signature reflects that range. [src: gc_ecotype_ecology]

Selected rows from the strongest-effects table (n genomes; ANI clusters; mean GC %; partial R²; max-min GC %; q):

| Species | n | ANI clusters | Mean GC | Partial R² | Max-min GC | q |
|---|---|---|---|---|---|---|
| *Aeromonas veronii* | 122 | 87 | 58.7 | 64% | 0.28 | 5.4e-08 [src: gc_ecotype_ecology] |
| *Citrobacter braakii* | 84 | 22 | 52.1 | 59% | 0.43 | 2.1e-10 [src: gc_ecotype_ecology] |
| *Mediterraneibacter faecis* | 67 | 37 | 40.7 | 30% | 0.06 | 5.8e-03 [src: gc_ecotype_ecology] |
| *Sarcina perfringens* | 104 | 44 | 28.2 | 28% | 0.21 | 1.2e-03 [src: gc_ecotype_ecology] |
| *Escherichia fergusonii* | 93 | 28 | 49.8 | 27% | 0.13 | 5.6e-05 [src: gc_ecotype_ecology] |
| *Enterococcus B hirae* | 50 | 12 | 36.8 | 27% | 0.11 | 1.3e-02 [src: gc_ecotype_ecology] |
| *Listeria monocytogenes_C* | 72 | 36 | 38.0 | 26% | 0.09 | 5.8e-03 [src: gc_ecotype_ecology] |
| *Burkholderia vietnamiensis* | 101 | 12 | 67.0 | 23% | 0.36 | 6.1e-05 [src: gc_ecotype_ecology] |
| *Enterococcus B faecium* | 1633 | 2 | 37.8 | 23% | 0.35 | 3.1e-89 [src: gc_ecotype_ecology] |
| *Vibrio parahaemolyticus* | 999 | 346 | 45.3 | 23% | 0.36 | 1.3e-32 [src: gc_ecotype_ecology] |
| *Klebsiella quasipneumoniae* | 400 | 6 | 57.7 | 23% | 0.88 | 1.7e-19 [src: gc_ecotype_ecology] |
| *Streptococcus thermophilus* | 135 | 5 | 39.0 | 22% | 0.30 | 1.4e-07 [src: gc_ecotype_ecology] |
| *Dorea formicigenerans* | 63 | 35 | 40.8 | 20% | 0.13 | 4.5e-02 [src: gc_ecotype_ecology] |
| *Cronobacter sakazakii* | 181 | 38 | 56.9 | 19% | 0.18 | 2.7e-06 [src: gc_ecotype_ecology] |
| *Leuconostoc mesenteroides* | 66 | 6 | 37.8 | 17% | 0.02 | 4.7e-03 [src: gc_ecotype_ecology] |

### Case study: *Burkholderia vietnamiensis*

*B. vietnamiensis* is a high-GC (≈ 67%) plant- and soil-associated bacterium that also colonizes human cystic fibrosis airways, which the report calls a textbook ecotype-spanning species. [src: gc_ecotype_ecology] Its dataset has 101 quality-passing genomes across human_clinical, soil and plant_host, with at least 10 in each category. [src: gc_ecotype_ecology] The 12 ANI clusters give what the report describes as meaningful phylogenetic resolution. [src: gc_ecotype_ecology] Isolation category given ANI cluster has partial R² = 23.4%, q = 6.1e-05 and max-minus-min mean GC = 0.36%. [src: gc_ecotype_ecology] The independent AlphaEarth analysis gives r = -0.60, p = 3.2e-07, FDR < 0.05. [src: gc_ecotype_ecology] The report interprets the two definitions of environment, text isolation source and satellite-derived per-coordinate embeddings, as converging on a non-trivial ecological GC signal beyond intra-species phylogeny in this species. [src: gc_ecotype_ecology] This is a single-species result.

## Contrast with gene content

The companion project ecotype_analysis addressed the gene-content version of this question. [src: gc_ecotype_ecology] It found phylogeny dominant for gene-content similarity in 60.5% of 172 species. [src: gc_ecotype_ecology] The GC result tells a partly different story. For a non-trivial fraction of species, environment leaves a residual GC signature after phylogeny is removed. [src: gc_ecotype_ecology] The report reads nucleotide composition as more environment-responsive within species than gene presence/absence. [src: gc_ecotype_ecology] See [[concepts/phylogenetic-structure-versus-ecological-adaptation-in-gene-content-patterns]] and [[concepts/environmental-versus-phylogenetic-drivers-of-gene-content]]. As a hypothesis, the report suggests that gene presence/absence is a "loud" event with large fitness cost or gain. GC drift would be a "quiet" continuous trait that responds to ongoing micro-selection. [src: gc_ecotype_ecology]

## Tensions

- The gene-content project found phylogeny dominant in 60.5% of 172 species. [src: gc_ecotype_ecology] The GC project finds a residual environmental signal in 40 of 108 species. [src: gc_ecotype_ecology] The report offers a hypothesis rather than a test of why they differ. [src: gc_ecotype_ecology]
- Effects are statistically robust but small, with median max-min 0.15%. [src: gc_ecotype_ecology] The report still calls them biologically meaningful. [src: gc_ecotype_ecology]

## Open Directions

- Rerun the test with sampling geography or study of origin as a random effect in more species. Only 16 species had enough geo-bearing genomes, so this would test the confounding caveat. [src: gc_ecotype_ecology]
- Run the GC and gene-content tests on the same species with matched controls. This would show whether the contrast comes from the trait or from the species sets. [src: gc_ecotype_ecology]
- Test whether the largest effects, such as in *Klebsiella quasipneumoniae*, track recombination rate or oxidative niche. This would turn the proposed explanation in [src: gc_ecotype_ecology] into a measured one.
- Expand the jointly testable set beyond 17 species, so the 59% overlap of the two environment definitions is better estimated. [src: gc_ecotype_ecology]
- Repeat the *B. vietnamiensis* two-definition test in other ecotype-spanning species, such as *V. parahaemolyticus*, to see whether the agreement of isolation source and embeddings holds beyond one species. [src: gc_ecotype_ecology]
