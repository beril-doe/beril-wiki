<!-- tension-hash: 326d40ead470e4cb -->
# Within-Species Ecotype Differentiation Versus Genus-Level Contamination Function Signals

The [[concepts/taxonomic-resolution-dependent-functional-inference]] page argues that taxonomic resolution controls which genotype-to-function relationships can be detected. [src: enigma_contamination_functional_potential] Evidence at two resolutions does not line up. The ecotype analysis detects functional differentiation within species among gene-content ecotypes, which are subpopulations defined by shared presence or absence of accessory genes. In contrast, the ENIGMA contamination analysis is null or mode-sensitive at genus resolution, meaning its result depends on the mapping mode used to bridge community taxa to pangenome clades. [src: enigma_contamination_functional_potential] [src: ecotype_functional_differentiation] The disagreement matters because it is unresolved whether the within-species structure is ecological or phylogenetic: the ecotype analysis lacked within-species phylogenetic controls. [src: ecotype_functional_differentiation] That gap limits direct extrapolation from gene-content ecotypes to contamination-associated community functions. [src: enigma_contamination_functional_potential] [src: ecotype_functional_differentiation]

## Evidence Sides

**Side A: finer functional structure exists within species**

- The within-species ecotype evidence supports the premise that finer functional structure exists. [src: ecotype_functional_differentiation]
  - Gene-content ecotypes are subpopulations within a species, defined by shared presence or absence of accessory genes.
- The ecotype analysis detects functional differentiation within species. [src: ecotype_functional_differentiation]
- The analysis lacked within-species phylogenetic controls, so it remains open whether the detected structure is ecological or phylogenetic. [src: ecotype_functional_differentiation]

**Side B: contamination-associated community function is null or mode-sensitive at genus resolution**

- The ENIGMA contamination analysis is null or mode-sensitive at genus resolution. [src: enigma_contamination_functional_potential]
  - "Mode-sensitive" means the result depends on the mapping mode, which is the rule used to bridge community taxa to pangenome clades.
- Within the concept framing, aggregation determines both how taxa are bridged and how much abundance is retained for functional scoring. [src: enigma_contamination_functional_potential]
- Mapped coverage is the fraction of community abundance linked to the functional features. Because of it, community-level associations can reflect representation rather than biological shifts. [src: enigma_contamination_functional_potential]

## Possible Reconciliations

- **Hypothesis 1 (resolution masking):** functional differentiation that is real within species is averaged away when taxa are aggregated to genus. Under this hypothesis, the ENIGMA null reflects resolution rather than true absence.
- **Hypothesis 2 (phylogenetic confounding):** the within-species ecotype signal is partly or wholly phylogenetic rather than ecological. This remains untested because the phylogenetic controls are absent. [src: ecotype_functional_differentiation]
- **Hypothesis 3 (functional redundancy):** contamination may change community membership while aggregated function stays stable. The concept page treats this as compatible but notes that the ENIGMA data do not directly demonstrate it. [src: enigma_contamination_functional_potential]

## Resolving Work

- **Phylogenetic control for ecotypes:** Rerun the ecotype functional-differentiation tests on the existing ecotype genomes. Add within-species core-genome phylogenies and use phylogenetic generalized least squares (PGLS), a regression that accounts for shared ancestry. The question is whether functional differentiation persists after controlling for phylogeny.
- **Finer-resolution community mapping:** Re-map ENIGMA community taxa at species or ecotype level where pangenome clades permit. Then repeat the contamination association tests. The question is whether signals that are null at genus resolution emerge at finer resolution.
- **Coverage-stratified re-analysis:** Restrict the ENIGMA tests to samples with high mapped coverage and compare results across mapping modes. The question is whether mode-sensitivity tracks representation rather than biology.
- **Ecotype-to-site bridging:** Link ecotype-discriminating accessory genes to ENIGMA site metagenomes or isolate genomes. The question is whether ecotype-defining functions vary along the contamination gradient.
