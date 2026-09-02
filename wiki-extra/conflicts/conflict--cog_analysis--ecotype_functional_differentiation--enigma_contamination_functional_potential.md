<!-- tension-hash: 7cda878f9e1f40d6 -->
# Coverage Sensitivity Versus Resolution-Robust Null Results

The disagreement concerns whether a contamination-associated functional signal should be treated as meaningful when it appears under a relaxed coverage-adjusted specification but disappears under stricter or coarser analyses. [[concepts/taxonomic-resolution-dependent-functional-inference]] The tension matters because the results bear on whether taxonomic bridging and coverage adjustment reveal real ecological structure or instead produce mode-sensitive associations, while independent ecotype and COG analyses suggest that functional differentiation exists at other resolutions or under other definitions.

## Evidence Sides

**Coverage-sensitive exploratory association**

The relaxed coverage-adjusted model yielded FDR q = 0.0462, whereas the strict coverage-adjusted model yielded FDR q = 0.130, and both confirmatory genus-level modes were null after predeclared testing. [src: enigma_contamination_functional_potential] This is a methodological tension between a coverage-sensitive exploratory association and a resolution- and specification-robust association, not evidence that the conflicting estimates should be averaged. [src: enigma_contamination_functional_potential] The difference could reflect retained abundance, bridge ambiguity, covariate sensitivity, taxonomic aggregation, or a combination of these factors. [src: enigma_contamination_functional_potential]

**Within-species functional differentiation**

The within-species ecotype evidence supports the premise that finer functional structure exists, but it does not resolve whether such structure is ecological or phylogenetic because the ecotype analysis lacked within-species phylogenetic controls. [src: ecotype_functional_differentiation] This tension limits direct extrapolation from gene-content ecotypes to contamination-associated community functions: the ENIGMA analysis is null or mode-sensitive at genus resolution, whereas the ecotype analysis detects functional differentiation within species. [src: enigma_contamination_functional_potential] [src: ecotype_functional_differentiation]

**Broad core-versus-novel functional partitioning**

The COG comparison found consistent core-versus-novel functional partitioning across 32 species, whereas the ENIGMA analysis did not find a robust contamination-associated shift in coarse COG proxies at genus resolution. [src: cog_analysis] [src: enigma_contamination_functional_potential] This is not a direct contradiction because the studies test different signals: broad evolutionary partitioning by gene novelty versus a site-level ecological association after taxonomic bridging. [src: cog_analysis] [src: enigma_contamination_functional_potential]

## Possible Reconciliations

- **Hypothesis — measurement sensitivity:** The relaxed model may retain abundance or coverage information that is attenuated by stricter adjustment, while the null confirmatory modes indicate that the association is not robust to specification.
- **Hypothesis — resolution dependence:** Ecotype-level differentiation may be real within species but become diluted, misassigned, or obscured after aggregation to genus-level taxonomic bridges.
- **Hypothesis — distinct biological signals:** Core-versus-novel COG partitioning may describe broad evolutionary structure rather than a contamination-associated shift, allowing both findings to hold.
- **Hypothesis — unresolved confounding:** The ecotype signal could be phylogenetic rather than ecological because within-species phylogenetic controls were absent.

## Resolving Work

- Reanalyze the ENIGMA association across retained-abundance, coverage-adjustment, covariate, and taxonomic-aggregation specifications; test whether the FDR q = 0.0462 result persists under preregistered robustness criteria.
- Repeat the ecotype analysis with within-species phylogenetic controls; test whether functional differentiation remains after separating ecological effects from lineage structure.
- Map ecotype-level functional features onto the ENIGMA samples and compare species-level, ecotype-level, and genus-level models; test whether aggregation explains the genus-resolution null.
- Partition COG features by novelty and evaluate contamination associations separately for core and novel functions; test whether a site-level signal is hidden by coarse COG proxies.
