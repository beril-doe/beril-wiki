<!-- tension-hash: dc402e43fb85f538 -->
# Metabolic Ecotypes: Ecological Signal or Phylogenetic and Sampling Artifact?

Within a species, genomes can be grouped by how complete their metabolic pathways are, giving "metabolic ecotypes" (clusters of genomes with similar pathway content). The disagreement is over what these clusters mean. One reading treats ecotype-environment correlations as ecological selection. The other holds that phylogeny, meaning shared evolutionary ancestry, dominates gene content in 60.5% of species, so ecotypes may partly reflect intra-species phylogenetic structure. [src: pathway_capability_dependency] A second, related dispute concerns the link between ecotypes and pangenome openness (how much gene content varies across a species' genomes), which may be shaped by uneven genome counts per species. Which reading holds decides whether ecotypes can be used as evidence of adaptation. This page draws on [[concepts/within-species-metabolic-ecotypes-from-pathway-variation]].

## Evidence Sides

**Side A: the patterns are biological**

- The report reads ecotype-environment correlations in *Salmonella* and *Phenylobacterium* as suggesting ecological selection. [src: metabolic_capability_dependency]
- The persistence of the partial correlation between ecotypes and openness (a correlation that holds a third variable fixed) is read as biological. [src: pathway_capability_dependency]

**Side B: phylogeny and sampling may explain the patterns**

- The same report notes that phylogenetic confounding is possible without explicit correction. [src: metabolic_capability_dependency]
- A separate project found phylogeny dominates gene content in 60.5% of species, so ecotypes may partly reflect intra-species phylogenetic structure. [src: pathway_capability_dependency]
- The same report says the genome-count bias is not fully eliminated. [src: pathway_capability_dependency]

Related discussion: [[concepts/phylogenetic-structure-versus-ecological-adaptation-in-gene-content-patterns]] and [[concepts/environmental-versus-phylogenetic-drivers-of-gene-content]].

## Possible Reconciliations

- **Hypothesis 1: both contribute.** Ecotypes may follow lineages that are themselves adapted to different environments, so phylogeny and ecology are entangled rather than opposed. This is untested here.
- **Hypothesis 2: the openness link survives sampling.** The persistence of the partial correlation may mean genome-count bias is too small to create the link. The report says that bias is not fully eliminated, so this stays a hypothesis.
- **Hypothesis 3: the species differ.** Environment links may hold in some species, such as *Salmonella* and *Phenylobacterium*, and not in others. No species-by-species test is given in the tension.

## Resolving Work

- **Data:** ecotype assignments and isolation-environment labels for species with environment links. **Method:** a permutation test that keeps phylogenetic tree structure, or a phylogenetically corrected regression. **Question:** does the ecotype-environment association persist after correction for phylogeny?
- **Data:** genomes within one species with a within-species phylogeny. **Method:** compare ecotype clusters with phylogenetic clades, for example by cluster-clade concordance. **Question:** how much of each ecotype's membership is explained by clade?
- **Data:** pathway-openness measures across species with varying genome counts. **Method:** rarefaction, which repeatedly subsamples to equal genome counts, then recompute the partial correlation. **Question:** does the openness link remain at equal sampling depth?
- **Data:** the species where phylogeny dominates and those where it does not. **Method:** stratify the ecotype-environment analysis by that split. **Question:** do ecological signals appear only where phylogeny is weak?
