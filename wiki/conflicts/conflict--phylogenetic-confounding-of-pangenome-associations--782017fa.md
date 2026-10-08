<!-- tension-hash: 782017fabdc04203 -->
# Environmental Structuring of AMR: Ecological Association or Lineage and Sampling Artifact?

Across this corpus, AMR (antimicrobial resistance) gene content has been compared across environments, including a contrast between clinical and other sources. [src: amr_environmental_resistome] The disagreement is over how far that pattern reflects ecology rather than phylogenetic confounding, meaning an apparent trait–environment relationship produced because lineages differ in both traits, as described on [[concepts/phylogenetic-confounding-of-pangenome-associations]]. Tests within taxonomic groups support an ecological association, but the majority of families were not testable or not significant. [src: amr_environmental_resistome] How much of the clinical contrast reflects lineage, representation, or unrecognized environmental resistance remains unresolved. [src: amr_environmental_resistome] This matters because acting on an environmental signal assumes it is not an artifact of which taxa happen to have been sampled where.

## Evidence Sides

**Side 1: An ecological association survives within lineages**

The environmental-resistome analysis found significant environmental effects within five of six phyla and within 20 of 141 families, which supports an ecological association. [src: amr_environmental_resistome] The project frames this as qualifying, not contradicting, the earlier environmental comparison. [src: amr_environmental_resistome] At finer resolution, case-study AMR ecotypes (resistance-defined strain groups within a species) showed visible environmental structuring. [src: amr_strain_variation]

**Side 2: The association is not generally demonstrated and may reflect lineage or representation**

The majority of families were not testable or not significant because of limited environmental breadth. [src: amr_environmental_resistome] The analysis also relied on species-level environment classifications, faced sampling imbalance, and focused on annotation from AMRFinderPlus, an AMR gene annotation tool. Together these leave unresolved how much of the clinical contrast reflects lineage, representation, or unrecognized environmental resistance. [src: amr_environmental_resistome] Within species, the visible ecotype structuring was not matched by a general statistical demonstration, because metadata and within-species environmental diversity were insufficient. [src: amr_strain_variation]

## Possible Reconciliations

- *Hypothesis:* An ecological association is real but detectable only where lineages span enough environments. Untestable families would then be uninformative rather than counter-evidence, though this would not account for the nonsignificant families.
- *Hypothesis:* The clinical contrast is partly a representation effect. Clinically sampled lineages may be over-represented, so environmental and lineage effects stay entangled at the species level.
- *Hypothesis:* Environmental species carry resistance determinants that AMRFinderPlus does not recognize. If so, the measured environmental differences would be inflated.
- *Hypothesis:* Within-species ecotype structuring is general, but current metadata are too sparse to show it statistically.

## Resolving Work

- **Genome-level environment labels:** Reclassify environment per genome rather than per species, then rerun the within-family tests. This would show whether species-level classification hides or creates within-lineage effects.
- **Balanced subsampling:** Rarefy genomes so each family has equal representation across environments, then repeat the within-phylum and within-family comparisons. This would separate the representation effect from the ecological one.
- **Broader annotation:** Supplement AMRFinderPlus with homology-based annotation of environmental pangenomes. This would test whether unrecognized environmental resistance narrows the clinical contrast.
- **Within-species permutation tests:** A permutation test compares the observed association with associations obtained after repeatedly reassigning environment labels at random. Restrict analysis to species with multi-environment strain metadata and shuffle labels only among closely related strains, so the null keeps phylogenetic structure fixed. This would show whether ecotype–environment association exceeds what relatedness alone produces, and whether case-study structuring generalizes.
