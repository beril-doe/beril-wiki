<!-- tension-hash: 6cbe6ebd14c61211 -->
# Ecological Guilds: Shared Selection or Complementary Provisioning?

The disagreement concerns what co-occurrence means in microbial ecological guilds. The [[concepts/gene-cooccurrence-ecological-guilds]] evidence supports an environmental-selection interpretation for particular genes, while a complementary analysis reports that co-occurring genus pairs are less complementary than random pairs. A related tension compares whole-pangenome openness, which shows no significant relationship with environment or phylogeny effects, with strong environmental enrichment for selected genes. The distinction matters because guilds may reflect shared habitat filtering, metabolic cooperation, or patterns that appear only at particular biological scales.

## Evidence Sides

**Guilds as shared environmental selection.** The PGP analysis supports a pqqC–acdS ecological-guild interpretation through strong pairwise association and environmental enrichment. It also found strong environment-associated enrichment for particular genes, including acdS and pqqC. [src: pgp_pangenome_ecology]

**Co-occurrence as limited complementarity.** The plant-microbiome complementarity analysis found co-occurring genus pairs slightly less complementary than random pairs (Cohen’s d ≈ −0.4, permutation p < 0.001). [src: plant_microbiome_ecotypes]

**Whole-pangenome openness as weakly related to broad effects.** The pangenome-openness analysis found no significant relationship between openness and either environment or phylogeny effects (Spearman rho = -0.05, p-value = 0.54; Spearman rho = 0.03, p-value = 0.73). [src: pangenome_openness]

**Selected genes as environmentally associated despite aggregate null results.** The PGP analysis found strong environment-associated enrichment for particular genes, including acdS and pqqC. [src: pgp_pangenome_ecology]

## Possible Reconciliations

- **Hypothesis — different meanings of guild:** A guild may denote shared environmental selection in the PGP analysis, whereas complementarity refers specifically to complementary metabolic provisioning. Under this definition, strong gene association need not imply stronger-than-random genus-level complementarity.
- **Hypothesis — scale and representation:** A whole-pangenome openness metric may not predict broad eco-phylogenetic structure even when selected gene subsets retain environmental associations.
- **Hypothesis — taxonomic versus pathway resolution:** Gene-level pairwise associations and genus-pair complementarity may summarize different units of biological organization, so their effect sizes need not agree.
- **Hypothesis — activity versus potential:** Presence or co-occurrence of pqqC and acdS may indicate ecological filtering without demonstrating that the genes are jointly active or metabolically exchanged.

## Resolving Work

- Measure pqqC and acdS abundance, transcription, and protein or enzyme activity across matched environments; test whether co-occurrence predicts simultaneous function rather than presence alone.
- Recalculate complementarity at the gene and pathway levels, not only the genus-pair level; test whether pqqC–acdS pairs differ from random pairs in pathway overlap and metabolic exchange potential.
- Partition pangenome openness into whole-genome and selected-gene subsets; test whether subset-level openness associates with environment or phylogeny when the aggregate metric does not.
- Use matched samples and permutation tests controlling for phylogeny, habitat, abundance, and sampling depth; test whether environmental enrichment remains after these factors are accounted for.
