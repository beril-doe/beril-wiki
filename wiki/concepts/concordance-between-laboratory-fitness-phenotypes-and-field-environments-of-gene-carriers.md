---
type: "Concept"
description: "Whether the condition under which a gene matters in the lab predicts the environments of genomes that carry it; covers within-species carrier tests, pre-registered lab–field concordance and its statistical caveats."
sources: ["summaries/discoveries.md", "summaries/functional_dark_matter__REPORT.md"]
---
# Concordance between laboratory fitness phenotypes and field environments of gene carriers

This page asks whether the condition under which a gene matters in the lab predicts the environments of the genomes that carry it. The functional dark matter project tested this for its "dark genes", using carrier genomes in the pangenome. [src: functional_dark_matter] About 62% of testable clusters agree in direction, and independent NMDC checks agree with the predictions. [src: functional_dark_matter] The evidence is moderate. The binomial test against chance is only marginal (p = 0.072), though Fisher's combined probability across the 47 tests is p = 0.031. Null controls were not run, and the metagenomic validation is inflated. [src: functional_dark_matter] See also [[summaries/functional_dark_matter__REPORT]] and [[summaries/discoveries]].

## Literature Context

The candidate papers are Tn-seq (transposon sequencing) fitness studies. Each maps gene fitness to a condition in one organism. None of them tests whether carrier genomes of a gene come from the environment where the gene matters in the lab, so they only give indirect context.

Several papers show that fitness effects depend on condition. In Staphylococcus aureus, Tn-seq under calprotectin metal limitation found that loss of clpP reduced fitness, and ClpP contributed to pathogenesis in vivo in a calprotectin-dependent manner [PMID 38920392](https://pubmed.ncbi.nlm.nih.gov/38920392/). A separate MRSA Tn-seq study found substantial differences in the genes needed in intracellular and blood environments. It also found that each mouse organ imposed unique growth constraints, and it identified 27 core genes shared across the host environments tested [PMID 40721419](https://pubmed.ncbi.nlm.nih.gov/40721419/). In Caulobacter crescentus, ppk1 was required for recovery from phosphate starvation but not for entry into starvation [PMID 42234530](https://pubmed.ncbi.nlm.nih.gov/42234530/). Proteotoxic stress screens likewise reported genetic- and environment-context-specific vulnerabilities [PMID 41575849](https://pubmed.ncbi.nlm.nih.gov/41575849/). These results agree with the premise of the hub page that lab fitness is condition-specific, and they support its emphasis on stress conditions.

Two papers bear on the plant and soil settings of the hub's examples. In a Burkholderia contaminans isolate from the International Space Station, Tn-seq found that the type II secretion system was critical for establishment in the tomato root zone. The paper reported stress-adaptation mechanisms, rather than antifungal or siderophore gene clusters, as the basis of persistence when the plant was challenged with Fusarium [PMID 41528136](https://pubmed.ncbi.nlm.nih.gov/41528136/). This is loosely consistent with the corpus finding that P. syringae genes with in planta or stress phenotypes are enriched in plant-associated genomes. It is a single-isolate lab result and does not test carrier genomes. A Pseudomonas veronii soil study is a partial caution. It found that most genes important in soil were not soil-specific, because they also affected growth in liquid minimal medium. It also found that flagella and motility mutants gained fitness in soil [PMID 36786610](https://pubmed.ncbi.nlm.nih.gov/36786610/). That finding suggests lab phenotypes do not always map cleanly to an environment. It is also relevant to the corpus's use of motility as a condition class.

The corpus's findings therefore extend this literature and are not in tension with it. The candidate papers stop at lab or host fitness in one organism. The corpus asks whether those phenotypes predict where carrier genomes occur in the pangenome. It reports 29 of 47 testable clusters (61.7%) concordant, but its binomial test is only marginal (p = 0.072). Fisher's combined probability is p = 0.031, and null controls were not run. None of the candidate papers can confirm or refute this carrier-environment link, so it remains novel and moderately supported. The P. veronii result suggests that generalist genes may weaken concordance. That is worth checking in the corpus's accessory-gene null.

## Setting up the question

The report asks whether genomes carrying stress-responsive dark genes come from stressful environments, as a test of the ecological relevance of lab phenotypes. [src: functional_dark_matter] Stress conditions (metals, oxidative, osmotic) dominate among dark genes with strong fitness effects, followed by carbon and nitrogen source utilization. [src: functional_dark_matter] Among pangenome-linked dark genes, 12,686 are accessory (described as environment-specific). [src: functional_dark_matter] The census identifies 511 accessory dark genes with strong fitness effects as the key intersection for biogeographic analysis. [src: functional_dark_matter]

The plan specified 7 condition–environment mappings. [src: functional_dark_matter] The implementation used 6: stress (metal, osmotic and oxidative consolidated), carbon source, nitrogen source, pH, motility and anaerobic. [src: functional_dark_matter] Stress was consolidated because the Fitness Browser (FB) expGroup field only has a broad "stress" category. [src: functional_dark_matter] Motility and anaerobic were added because they were prominent among dark genes with strong fitness effects. [src: functional_dark_matter]

## Within-species carrier tests

Carrier versus non-carrier tests that control for phylogeny found significant environmental enrichment in 10/137 clusters (false discovery rate, FDR, < 0.05). [src: functional_dark_matter] They found AlphaEarth embedding divergence in 1/67 clusters. [src: functional_dark_matter] A second description gives 151 accessory dark gene clusters testable across 31 species, with 10 enriched in environment category and 1 showing embedding divergence. [src: functional_dark_matter] The report counts this as support for its biogeographic hypothesis (H1d). [src: functional_dark_matter] The strongest within-species signals are in Pseudomonas and P. syringae. [src: functional_dark_matter]

Examples fit the lab phenotype. P. putida dark genes with stress or nitrogen phenotypes are enriched in clinical or human-associated isolates, which the report reads as a possible role in host-associated niche adaptation. [src: functional_dark_matter] P. syringae dark genes with in planta or stress phenotypes are enriched in plant-associated genomes. [src: functional_dark_matter] See pseudomonas putida and [[entities/pseudomonas-syringae-b728a]].

| Organism | Gene | Phenotype | abs(fit) | Carrier environment | OR | FDR | Tag |
|---|---|---|---|---|---|---|---|
| P. putida | PP_0025 | stress | 4.8 | human_clinical | 27.5 | 7e-6 | [src: functional_dark_matter] |
| P. putida | PP_3434 | nitrogen | 3.1 | human_clinical | 28.6 | 7e-6 | [src: functional_dark_matter] |
| P. putida | PP_0642 | nitrogen | 2.8 | human_clinical | 11.6 | 0.001 | [src: functional_dark_matter] |
| P. putida | PP_3105 | stress | 3.7 | human_assoc | inf | 0.004 | [src: functional_dark_matter] |
| P. syringae B728a | Psyr_0167 | in planta | 4.6 | plant_assoc | 11.9 | 0.005 | [src: functional_dark_matter] |
| P. syringae B728a | Psyr_2830 | stress | 3.4 | plant_assoc | 10.9 | 0.031 | [src: functional_dark_matter] |
| P. putida N2C3 | AO356_11255 | nitrogen | 3.4 | freshwater | inf | 0.031 | [src: functional_dark_matter] |

Not every hit matches an expected direction. B. thetaiotaomicron 354052 (stress, abs(fit) 2.4, human_assoc) has OR 0.17 at FDR 0.005. [src: functional_dark_matter] Locus 350920 (stress, abs(fit) 2.2, human_assoc) has OR 0.37 at FDR 0.031. [src: functional_dark_matter] K. oxytoca BWI76_RS15640 (carbon, abs(fit) 2.1, human_assoc) has OR 0.14 at FDR 0.031. [src: functional_dark_matter] See [[entities/bacteroides-thetaiotaomicron]]. The top-ranked candidate, P. putida N2C3 AO356_11255, has carriers only in freshwater/soil, matching its nitrogen phenotype. [src: functional_dark_matter]

## Pre-registered lab–field concordance

Of 47 testable dark gene clusters, 29 (61.7%) were concordant with pre-registered condition–environment predictions. Carrier genomes were enriched in the environments the lab phenotype predicted. [src: functional_dark_matter, discoveries] Concordance was strongest for pH genes (100%, n=4) and nitrogen source genes (78%, n=9). [src: functional_dark_matter] Six clusters reached FDR < 0.2. [src: functional_dark_matter] Two K. oxytoca carbon clusters, BWI76_RS15525 (abs(fit) 2.3) and BWI76_RS15535 (abs(fit) 2.2), had 14.3% of carriers versus 2.5% of non-carriers in the expected soil, freshwater and plant environments (OR 6.6, FDR 0.069). [src: functional_dark_matter]

Four P. putida N2C3 genes show carrier enrichment in the expected environments, each with FDR above 0.05. [src: functional_dark_matter]

- AO356_11255 (nitrogen, abs(fit) 3.4): 80.0% of carriers versus 8.3% of non-carriers in soil, freshwater and wastewater (OR 44.0, FDR 0.093). [src: functional_dark_matter]
- AO356_12450 (carbon, abs(fit) 2.1): 62.5% versus 0% in soil, freshwater and plant (OR inf, FDR 0.093). [src: functional_dark_matter]
- AO356_25185 (anaerobic, abs(fit) 2.7): 55.6% versus 0% in soil, freshwater and animal (OR inf, FDR 0.178). [src: functional_dark_matter]
- AO356_24150 (nitrogen, abs(fit) 3.0): 55.6% versus 0% in soil, freshwater and wastewater (OR inf, FDR 0.178). [src: functional_dark_matter]

The report calls AO356_11255, the project's top candidate, the clearest lab–field signal, matching its strong nitrogen utilization fitness. [src: functional_dark_matter]

NMDC metagenomic validation confirmed all 4 testable pre-registered abiotic predictions (nitrogen~nitrogen, pH~pH, anaerobic~dissolved oxygen). [src: functional_dark_matter, discoveries] In the discoveries digest it also confirmed all 7 trait predictions. [src: discoveries] Nitrogen carriers correlated with nitrogen-rich environments and pH carriers with pH-extreme environments, and 76/105 abiotic correlations reached significance. [src: functional_dark_matter] The report frames these as community-level corroboration across 6,365 metagenomic samples. [src: functional_dark_matter] See [[concepts/metagenome-based-cross-validation-of-genomic-trait-predictions]].

The report concludes that genes important under stress in the lab tend to come from organisms in stressful environments. It validates fitness data as a proxy for ecological function. [src: functional_dark_matter, discoveries] It also claims, to its knowledge, that systematic application of this approach across organisms and condition classes is novel. [src: functional_dark_matter]

## Statistical caveats

The headline is weaker than the conclusion suggests. The one-sided binomial test (29/47 vs. p = 0.5) gives p = 0.072, described as marginal, and the Wilson score 95% confidence interval [0.474, 0.742] includes 0.50. [src: functional_dark_matter] Fisher's combined probability across all 47 individual Fisher's exact test p-values is p = 0.031, which the report presents as stronger aggregate evidence that concordance is non-random. [src: functional_dark_matter] The digest reports the same 29/47 and p=0.031 without the binomial result. [src: discoveries]

- The report states that compositional coupling inflates the NMDC signal. It still argues that directional concordance across independent datasets supports the inference. [src: functional_dark_matter] See [[concepts/compositional-coupling-in-metagenomic-validation-of-carrier-abundance]].
- Equivalent null controls were not run for the biogeographic and lab-field analyses. [src: functional_dark_matter] A full annotated-accessory-gene null through the same pipeline would strengthen rejection of the null but needs Spark carrier-genome queries. [src: functional_dark_matter]
- AlphaEarth embeddings cover only 28% of genomes (83K/293K), and NCBI isolation-source metadata is inconsistent, which limits power. [src: functional_dark_matter] See [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]] and [[entities/alphaearth-environmental-embeddings]].
- The P. putida N2C3 hits above have FDR of 0.093 to 0.178, so none passes the FDR < 0.05 threshold used for the within-species tests. [src: functional_dark_matter]

## Tensions

- Prediction versus result on conservation: stress dark genes were predicted to be more accessory than carbon/nitrogen genes. The test rejected this (Fisher's exact, n=7,491; p=0.013), with stress genes 23.0% accessory versus 25.5% (OR=1.15). [src: functional_dark_matter] The report concludes the link between condition specificity and pangenome conservation is more complex than a stress=accessory, metabolism=core model. [src: functional_dark_matter] See [[concepts/gene-fitness-importance-as-a-predictor-of-pangenome-conservation]].
- Strong claim versus marginal test: the report says the concordance validates fitness as an ecological proxy. [src: functional_dark_matter] Its own binomial test is marginal at p = 0.072, while Fisher's combined probability is p = 0.031. [src: functional_dark_matter]

## Open Directions

- Run the annotated accessory-gene null through the same carrier pipeline, to test whether 61.7% exceeds what ordinary accessory genes give.
- Repeat the NMDC check with a control for compositional coupling, to see how much of the 76/105 significant correlations survives.
- Expand condition classes beyond broad stress, for example by splitting metal, osmotic and oxidative stress, to test whether concordance differs by stress type.
- Add environment metadata for genomes without AlphaEarth coverage, to raise power beyond the 28% of genomes covered.
- Examine the reversed-direction hits (odds ratios below 1 in B. thetaiotaomicron and K. oxytoca) as possible non-concordant cases.
- Test the 511 accessory, strong-fitness dark genes beyond the 47 testable clusters, to see whether the P. putida N2C3 candidates reach FDR < 0.05 with more carrier genomes.
