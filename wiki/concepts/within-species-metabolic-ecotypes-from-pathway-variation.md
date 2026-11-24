---
type: "Concept"
description: "Whether genomes of one species cluster by pathway completeness into metabolic ecotypes, how their number relates to pangenome openness, and whether they track environment."
sources: ["summaries/discoveries.md", "summaries/metabolic_capability_dependency__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md", "summaries/pseudomonas_carbon_ecology__REPORT.md"]
---
# Within-species metabolic ecotypes from pathway variation

Genomes of one species can be clustered by pathway completeness into "metabolic ecotypes". A survey of 225 species finds a median of 4 per species, and more ecotypes go with more open pangenomes. [src: discoveries] A targeted analysis of 10 species finds clear clusters in all of them, but links to isolation environment in only some. [src: metabolic_capability_dependency] The evidence is observational and correlational, and phylogeny and sampling depth are unresolved confounders. [src: metabolic_capability_dependency, pathway_capability_dependency] See [[entities/metabolic-ecotype-clustering]] for the method and [[concepts/pangenome-openness-and-its-correlates]] for openness.

## Literature Context

The one candidate paper is a study of twelve strains of the marine bacterium *Alteromonas macleodii*. It combines pangenomic, exometabolomic and physiological evidence to link genotype to ecological niche [PMID 31964928](https://pubmed.ncbi.nlm.nih.gov/31964928/). It reports strain-specific differences in carbon metabolism, microbial interactions, cellular communication and iron acquisition. Examples include amino acid secretion and phenol degradation in strain MIT1002, which may promote association with *Prochlorococcus*. They also include algal polysaccharide utilization in strain 83-1 and three novel Pacific isolates. Toluene and xylene degradation, mediated by a plasmid, was unique to strain EZ55. Benzoate degradation in strain EC673 related to a chromosomal gene cluster shared with a plasmid of *A. mediterranea* EC615. The authors conclude that mobile genetic elements drive some of these adaptations [PMID 31964928](https://pubmed.ncbi.nlm.nih.gov/31964928/). Phenotypic variability corresponded to different competitiveness in co-culture and to geographic distribution. The authors call this "ecological microdiversity" and take it to indicate links between intraspecific diversity, microbial interactions and biogeography [PMID 31964928](https://pubmed.ncbi.nlm.nih.gov/31964928/). The evidence comes from only twelve strains, and the abstract is the only text available here.

The corpus finding that sits closest to this paper concerns *Alteromonas macleodii*. The targeted analysis of 56 genomes gave 2 pathway clusters with a silhouette of 0.738. Those clusters did not correlate with isolation environment. The twelve-strain study is consistent with the corpus's broader claim that a single species can contain meaningful metabolic and ecological variation. It also extends the corpus, because it shows strain-level niche differences in this very species. Its strain-level differences were in phenol, toluene, xylene and benzoate degradation, siderophore production and polysaccharide use, and they were linked to geography and co-culture competitiveness. The paper therefore gives a plausible reason for the corpus's marine null result. Niche-relevant variation may sit in accessory gene content, including plasmids, which pathway-completeness clustering of 80 pathways may not capture. This fits the hypothesis the hub already raises, that GapMind pathway annotations miss gene-content differences. It remains a hypothesis, because the paper did not test pathway-completeness clustering or NCBI isolation-source categories.

The paper does not address the corpus's survey-level claims. These are the median of 4 ecotypes per species across 225 species, the partial rho of 0.322 between ecotype count and pangenome openness, and the phylogenetic and sampling-depth confounders. It cannot test them with twelve strains. The paper does not contradict any corpus claim. Its evidence is a small, mechanistic strain comparison, whereas the corpus evidence is observational and correlational. Its findings also support the hub's proposed follow-up of comparing gene-content clustering with pathway clustering in marine species.

## How many ecotypes per species

Across 225 species with at least 50 genomes and at least 3 variable pathways, clustering by pathway profile gave a median of 4 ecotypes per species and a maximum of 8. [src: discoveries, pathway_capability_dependency] The method clusters binary complete/incomplete profiles across 80 pathways with hierarchical clustering and Jaccard distance. [src: pathway_capability_dependency] It sets the ecotype count by cutting each dendrogram at 50% of maximum distance. [src: pathway_capability_dependency] The report gives the range as 2-8 ecotypes per species. [src: pathway_capability_dependency] [[entities/alistipes-onderdonkii]] and [[entities/barnesiella-intestinihominis]] each had 8 ecotypes. Both are gut commensals with substantial intraspecific metabolic diversity. [src: discoveries, pathway_capability_dependency] A separate report proposes looking for such ecotypes, meaning subpopulations adapted to different niches, within *Pseudomonas*. [src: pseudomonas_carbon_ecology]

The count depends on the cut. A fixed 50% threshold is a simplification, and other thresholds would give other counts. [src: pathway_capability_dependency] The median of 4 should be read as an order-of-magnitude estimate. [src: pathway_capability_dependency]

## Ecotypes and pangenome openness

Ecotype count correlates with pangenome openness. The raw Spearman rho is 0.262 (p=6.8e-05). [src: pathway_capability_dependency] After controlling for genome count, the partial rho is 0.322 (p=8.0e-07). [src: discoveries, pathway_capability_dependency] The report reads this as species with genuinely more metabolic diversity, not just more sampled genomes, tending to have more open pangenomes. It says this supports hypothesis H2, that the variation is biological and not merely a sampling artifact. [src: pathway_capability_dependency]

This is limited by sampling. Species with more genomes are more likely to show pathway variation and more ecotypes. Partial correlations mitigate this bias but do not fully remove it. [src: pathway_capability_dependency] See [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]].

## Cluster sharpness in ten target species

All 10 target species (at least 50 genomes and at least 15 variable pathways) showed meaningful clustering, with every silhouette score above 0.2. [src: metabolic_capability_dependency] Silhouette scores ranged from 0.35 (PALSA-747 sp.) to 0.89 (*Salmonella enterica*), so some species separate almost perfectly and others have softer boundaries. [src: metabolic_capability_dependency] The report takes this as evidence that within-species pathway heterogeneity is a general feature, not an exception. [src: metabolic_capability_dependency]

| Species | Genomes | Clusters | Silhouette |
|---|---|---|---|
| Salmonella enterica | 11,396 | 6 | 0.894 [src: metabolic_capability_dependency] |
| Stutzerimonas stutzeri | 149 | 2 | 0.780 [src: metabolic_capability_dependency] |
| Alteromonas macleodii | 56 | 2 | 0.738 [src: metabolic_capability_dependency] |
| Acetatifactor intestinalis | 59 | 6 | 0.657 [src: metabolic_capability_dependency] |
| Ruminococcus E sp. | 53 | 2 | 0.609 [src: metabolic_capability_dependency] |
| Phenylobacterium sp. | 51 | 2 | 0.544 [src: metabolic_capability_dependency] |
| Limivicinus sp. | 50 | 2 | 0.528 [src: metabolic_capability_dependency] |
| Pelagibacter sp. | 79 | 2 | 0.430 [src: metabolic_capability_dependency] |
| Prochlorococcus A sp. | 74 | 2 | 0.429 [src: metabolic_capability_dependency] |
| PALSA-747 sp. | 51 | 2 | 0.349 [src: metabolic_capability_dependency] |

The pathways that varied most across species were all amino acid biosynthesis pathways. Valine/leucine had heterogeneity 0.60, tryptophan 0.51 and lysine/threonine 0.49. [src: metabolic_capability_dependency] The report reads these as pathways that some populations kept and others lost. It calls this consistent with the ecological partitioning of amino acid dependencies seen by Ramoneda et al. (2023) across 26,277 bacterial genomes. [src: metabolic_capability_dependency]

## Do ecotypes track environment?

Only in some species. Metabolic clusters correlated with isolation environment in *Salmonella enterica* (χ²=1570.2, df=25, p<0.0001) and in *Phenylobacterium* sp. (χ²=12.2, df=1, p=0.0005). [src: metabolic_capability_dependency] They did not in the marine *Stutzerimonas* and *Alteromonas*. [src: metabolic_capability_dependency] The non-significant result extended to *Pelagibacter* and *Prochlorococcus*. [src: metabolic_capability_dependency]

*Salmonella enterica* had the strongest structure (silhouette=0.89, k=6). Its clusters correlated strongly with clinical, food and environmental isolation sources. [src: metabolic_capability_dependency] The report compares this to the established epidemiological serovars of Salmonella, and to Van Rossum et al. (2020) on strain-level metabolic differentiation in human microbiome species. [src: metabolic_capability_dependency] See [[entities/salmonella-enterica]].

The report offers three possible reasons for the marine null results. They are hypotheses, not tested findings:
- NCBI isolation-source fields may be too coarse for marine isolates. [src: metabolic_capability_dependency]
- Clusters may track depth or nutrient zone rather than discrete source categories. [src: metabolic_capability_dependency]
- Differences in marine oligotrophs may come from gene content that GapMind pathway annotations do not capture at the relevant resolution. [src: metabolic_capability_dependency]

The report cites Nowinski et al. (2023), who found marine ecological divergence shaped by gene content and expression, a signal pathway clustering may partly miss. [src: metabolic_capability_dependency] It also cites Tschoeke et al. (2020) on the *Prochlorococcus* collective. Both are described as showing marine metabolic ecotypes defined by gene-content differences. [src: metabolic_capability_dependency] The report proposes supplementing NCBI isolation source with BacDive or GTDB environmental labels to improve the association test. [src: metabolic_capability_dependency] See [[concepts/reliability-and-coverage-limits-of-gapmind-pathway-predictions]] and [[concepts/harmonizing-free-text-isolation-source-and-environment-metadata]].

The planned H2 analysis, correlating ecotypes with AlphaEarth environmental niche breadth, was not executed. [src: pathway_capability_dependency] AlphaEarth embeddings cover only 28% of genomes (83K/293K), which would significantly limit the sample size. [src: pathway_capability_dependency]

## Tensions

- **Biology versus phylogeny.** The report reads ecotype-environment correlations in *Salmonella* and *Phenylobacterium* as suggesting ecological selection. [src: metabolic_capability_dependency] It also notes that phylogenetic confounding is possible without explicit correction. [src: metabolic_capability_dependency] A separate project found phylogeny dominates gene content in 60.5% of species, so ecotypes may partly reflect intra-species phylogenetic structure. [src: pathway_capability_dependency] See [[concepts/phylogenetic-structure-versus-ecological-adaptation-in-gene-content-patterns]] and [[concepts/environmental-versus-phylogenetic-drivers-of-gene-content]].
- **Openness link versus sampling bias.** The persistence of the partial correlation is read as biological. [src: pathway_capability_dependency] The same report says the genome-count bias is not fully eliminated. [src: pathway_capability_dependency]

## Open Directions

- Test ecotype-environment association with phylogenetic correction, for example within-clade tests in *Salmonella* and *Phenylobacterium*. This would address the phylogenetic confounding caveat.
- Replace NCBI isolation source with BacDive or GTDB environmental labels, and retest the marine species. This would show whether the null results come from metadata resolution.
- Run the planned AlphaEarth niche-breadth analysis (H2) on the 28% of genomes with embeddings. Check first that the sample is large enough.
- Repeat the ecotype count at several dendrogram cut thresholds and check whether the openness correlation holds. This would address the fixed 50% threshold.
- Compare gene-content clustering with pathway clustering in marine species. This would test whether GapMind misses the signal.
- Carry out the proposed within-species *Pseudomonas* pathway analysis to look for niche-adapted subpopulations.
