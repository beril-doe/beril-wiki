---
type: "Concept"
description: "Whether bacterial species carrying more prophage-related genes also carry more anti-phage defense systems, after controlling for genome size and phylum; stops at phylogenetically uncorrected tests."
sources: ["summaries/phage_defense_arsenal__REPORT.md"]
---
# Defense-system burden scaling with prophage load (anti-phage arms race)

Across 7,323 bacterial species, those carrying more prophage clusters also carry more anti-phage defense systems. The association survives control for genome size and phylum, and it is positive in all 9 major phyla. [src: phage_defense_arsenal] The evidence comes from one report ([[summaries/phage_defense_arsenal__REPORT]]). It is correlational and has no phylogenetic correction beyond categorical phylum, so it is consistent with an arms race but does not formally test one. [src: phage_defense_arsenal]

## Literature Context

The candidate papers describe the bacteria–phage arms race mainly through mechanisms and models. They do not report cross-species comparative scaling. A review of bacterial anti-phage strategies lists defenses such as blocking adsorption, superinfection exclusion, restriction-modification (R-M), CRISPR-Cas and abortive infection (Abi). It pairs them with phage counter-strategies such as anti-CRISPR (Acr) proteins and modification of phage genes to evade R-M recognition, and it says this reciprocal pressure drives coevolution [PMID 36901793](https://pubmed.ncbi.nlm.nih.gov/36901793/). This is a qualitative background to the hub's premise that phage pressure should favor larger defense repertoires. It is an abstract-level review, not a test of that premise.

Two other candidates widen what counts as defense. A study of Mycobacterium smegmatis infected with phage SWU1 found that loss of non-homologous end joining (NHEJ) increased plaque counts and reduced bacterial survival. The proposed mechanism is that error-prone NHEJ repair at phage cos sites blocks replication [PMID 41603729](https://pubmed.ncbi.nlm.nih.gov/41603729/). This is a single-species experimental result. It suggests that some antiphage function comes from core DNA repair machinery, which a catalog of dedicated defense systems would not necessarily capture. A stochastic model of CRISPR-Cas carried on conjugative plasmids found robust protection against virulent phage except in limited parameter sets. In those sets, high segregation loss generates defenceless cells where phage can evolve and escape [PMID 38262608](https://pubmed.ncbi.nlm.nih.gov/38262608/). This is a modeling result, not an empirical survey. It shows that mobile elements can take part in the arms race.

The corpus finding is that, across 7,323 species, defense-system count rises with prophage clusters. The marginal Spearman ρ is 0.609 and the partial ρ is 0.301 after controlling genome size and phylum. The association is positive in all 9 major phyla. This is consistent with the arms-race framing in the review [PMID 36901793](https://pubmed.ncbi.nlm.nih.gov/36901793/). It extends that framing to a large comparative scale, which the candidate papers do not address. The hub itself cautions that the data are correlational, that phylum is the only phylogenetic control, and that the result does not formally test an arms race.

The mechanistic papers also bear on the scope of the corpus count. The Mycobacterium result [PMID 41603729](https://pubmed.ncbi.nlm.nih.gov/41603729/) shows an antiphage contribution from a repair pathway, and the hub reports the weakest effect in Actinomycetota (partial ρ = 0.18). The abstract does not link the two, so any connection stays a hypothesis. The plasmid model [PMID 38262608](https://pubmed.ncbi.nlm.nih.gov/38262608/) shows that defenses can sit on mobile elements. The candidates do not say how the corpus assigned defense systems, so they cannot show that its counts are incomplete. None of the candidates contradicts the corpus. The phylogenetically explicit test it proposes remains novel relative to this evidence.

## Marginal and adjusted association

The raw association is strong. Marginal Spearman ρ between per-species defense-system count and n_prophage_clusters is 0.609 (p ≈ 0, n = 7,323). [src: phage_defense_arsenal] After residualizing on log₁₀(median genome size) and phylum, partial ρ is 0.301 (p = 1.6 × 10⁻¹⁵³). [src: phage_defense_arsenal] The report therefore calls it a moderate effect that survives the two strongest known confounders. [src: phage_defense_arsenal] It uses n_prophage_clusters, an unbounded continuous count, as the primary predictor because the module classifier over-counts. [src: phage_defense_arsenal] See [[concepts/annotation-based-prophage-detection-prevalence-and-domesticated-remnants]] for how prophages are detected.

A negative-binomial generalized linear model (GLM) of defense count on prophage clusters, log₁₀ genome size and phylum gives independent contributions from both predictors. The prophage-cluster coefficient is β = 2.0 × 10⁻⁴ (p < 0.001). [src: phage_defense_arsenal] The genome-size coefficient is β = 0.755 (p < 0.001), so each 10-fold genome-size increase goes with e^0.755 ≈ 2.1× more defense systems. [src: phage_defense_arsenal]

The report compares the residual partial ρ = 0.30 to the phylogenetic-signal strength typical of labile microbial traits. [src: phage_defense_arsenal] It reads the universal positive pattern as extending Stern & Sorek and Koskella & Brockhurst arms-race predictions from theory and small comparative studies to the 293K-genome scale. [src: phage_defense_arsenal]

## Consistency across phyla

All 9 major phyla show positive, significant partial correlations, Bonferroni-safe at 9 tests. [src: phage_defense_arsenal] The report states that this holds after controlling log₁₀ genome size within each phylum, with values from 0.18 in Actinomycetota to 0.53 in Campylobacterota. [src: phage_defense_arsenal] The effect is not lineage-restricted. Even Actinomycetota, where CRISPR-Cas is very rare in Mycobacterium and Streptomyces gene-content data, shows partial ρ = 0.18 (p < 10⁻⁷). [src: phage_defense_arsenal]

| Phylum | n species | partial ρ | p |
|---|---|---|---|
| Campylobacterota | 102 | 0.530 | 9.8×10⁻⁹ [src: phage_defense_arsenal] |
| Bacillota | 735 | 0.481 | 8.4×10⁻⁴⁴ [src: phage_defense_arsenal] |
| Bacillota_A | 1,134 | 0.419 | 2.0×10⁻⁴⁹ [src: phage_defense_arsenal] |
| Verrucomicrobiota | 129 | 0.369 | 1.6×10⁻⁵ [src: phage_defense_arsenal] |
| Patescibacteria | 191 | 0.343 | 1.2×10⁻⁶ [src: phage_defense_arsenal] |
| Pseudomonadota | 2,172 | 0.342 | 9.6×10⁻⁶¹ [src: phage_defense_arsenal] |
| Cyanobacteriota | 124 | 0.309 | 4.9×10⁻⁴ [src: phage_defense_arsenal] |
| Bacteroidota | 925 | 0.261 | 6.3×10⁻¹⁶ [src: phage_defense_arsenal] |
| Actinomycetota | 803 | 0.185 | 1.3×10⁻⁷ [src: phage_defense_arsenal] |

Effect strength itself varies by lineage. The Actinomycetota effect is about 3× weaker than the Campylobacterota effect, and the report suggests exploring which covariates predict this heterogeneity. [src: phage_defense_arsenal] For DISARM, the arms-race and syndrome results rely on species-level presence/absence rather than per-cluster core/auxiliary calls, so the report says they survive its detection caveat. [src: phage_defense_arsenal] For the core/auxiliary distinction, see [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]].

## Limits of the evidence

- **Sampling filter.** Requiring at least 5 genomes per species reduces the set to 7,323 species, 26 % of 27,690 pangenome species. This biases the set toward well-sampled, culturable, high-priority organisms. [src: phage_defense_arsenal] Extrapolation to the full 293K-genome tree, which includes many environmental metagenome assembled genomes (MAGs), is plausible but untested. [src: phage_defense_arsenal]
- **No phylogenetic correction.** Partial correlation and the negative-binomial GLM control for phylum categorically, not for finer phylogenetic structure. [src: phage_defense_arsenal] The report calls this a coarse-grained analog. It leaves open whether the arms race is independent of shared ancestry or partly a within-genus pattern amplified to appear cross-phylum. [src: phage_defense_arsenal] The results are consistent with, but not a formal test of, a phylogenetically independent arms race. [src: phage_defense_arsenal]
- **Proposed stronger test.** The report proposes a phylogenetic mixed-effects model with the GTDB tree as the covariance structure as a stronger arms-race test. [src: phage_defense_arsenal] It suggests refitting the negative-binomial GLM this way, for example with phyr::pglmm. [src: phage_defense_arsenal]
- **Fixed dispersion.** NB04 fits the negative-binomial GLM with NegativeBinomial(alpha=1.0), holding dispersion at 1.0 instead of estimating it. [src: phage_defense_arsenal] The report expects a small effect on the two focal coefficients, both significant at p<0.001 with wide margins, but says standard errors may be slightly under- or over-stated. [src: phage_defense_arsenal] It states that the qualitative direction and per-phylum consistency, the load-bearing pieces of the arms-race claim, are not affected. [src: phage_defense_arsenal]

## Open Directions

- Refit the negative-binomial GLM with the GTDB tree as a phylogenetic covariance structure, for example with phyr::pglmm. This would test whether the arms race holds independent of shared ancestry, which the current categorical phylum control cannot do.
- Re-estimate negative-binomial dispersion from the data instead of fixing alpha=1.0, and check whether the standard errors change.
- Repeat the analysis with species that have fewer than 5 genomes, including environmental MAGs, to test whether the pattern extends beyond well-sampled, culturable species.
- Model effect-size heterogeneity across phyla, for example Actinomycetota against Campylobacterota, using candidate covariates.
- Run within-genus analyses to check whether part of the signal is a within-genus pattern that only appears cross-phylum.
