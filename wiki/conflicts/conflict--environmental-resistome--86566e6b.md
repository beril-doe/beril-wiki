<!-- tension-hash: 86566e6be31ea1c9 -->
# Species-level environment–AMR association versus sparse within-species environmental structure

The [[concepts/environmental-resistome]] page reports that the resistome (the collection of antimicrobial-resistance, or AMR, genes in a population) is associated with the environments bacterial species come from, and that this association survives controls meant to rule out a species-label artifact. [src: amr_environmental_resistome] Within families and species, however, significant environmental effects appear in only a minority of tests, and a strain-level AMR test was limited by sparse metadata. [src: amr_environmental_resistome, ecotype_analysis, amr_strain_variation] The disagreement matters because the two levels support different readings. Environment-linked resistome differences might extend within lineages. Alternatively, environment-linked lineages might differ in resistome while environment adds little within them, a pattern that phylogenetic or sampling structure could produce. Because the evidence is associational, any causal role for environment remains a hypothesis.

## Evidence Sides

**Side A: the association is robust beyond species labels**

The environment–AMR association persisted under several controls: majority-vote thresholds (assigning each species the environment most of its genomes come from), phylum-level controls and family-level controls. This supports an ecological signal beyond a simple species-label artifact. [src: amr_environmental_resistome]

**Side B: within-lineage environmental effects are mostly absent or unresolved**

Only 20 of 141 testable families (14%) showed significant within-family effects after FDR correction (false discovery rate, a multiple-testing adjustment). [src: amr_environmental_resistome, ecotype_analysis] An ecotype is a genetically distinct within-species subpopulation tied to an ecological niche. Whole-genome ecotype analysis tested whether environment explains genomic variation within species. It found environmental effects that were:

- significant and positive in 12 species (7.0%);
- significant and negative in 4 species (2.3%);
- absent in 156 species (90.7%). [src: amr_environmental_resistome, ecotype_analysis]

The strain analysis found AMR ecotypes, meaning distinct within-species resistome clusters, in 19.5% of eligible species. However, metadata were sparse and only 2 species passed strict testing criteria. That within-species result is therefore unresolved rather than null. [src: amr_strain_variation]

## Possible Reconciliations

- **Hypothesis 1 (scale dependence):** Environment structures resistomes mainly among lineages, through which lineages occupy which habitats, rather than within them. On this reading, both sides are correct at their own scale.
- **Hypothesis 2 (power limitation):** Within-family and within-species effects exist but go undetected because most families and species may not span enough environments to test. Per-genome metadata were sparse in the strain analysis. [src: amr_strain_variation]
- **Hypothesis 3 (residual confounding):** The species-level association partly reflects phylogenetic or sampling structure that phylum- and family-level controls do not fully remove.

## Resolving Work

- **Expand family-level testing.** Data: isolation-source metadata for genomes in families currently untestable. Method: within-family environment tests with FDR correction on the enlarged set. Question: does the share of families with significant effects rise as environmental coverage grows, or does it stay low?
- **Make the strain-level test powerful enough.** Data: curated or inferred per-genome isolation sources for species with AMR ecotypes. Method: environment–ecotype association testing at strict criteria. Question: are the ecotypes found in 19.5% of eligible species environment-linked when testing is adequately powered?
- **Compare phylogenetically controlled estimates across scales.** Data: species phylogenies plus environment labels. Method: phylogenetically controlled models fitted at species and within-species levels. Question: does the environmental effect shrink toward zero as phylogenetic resolution increases?
- **Contrast with the general genome background.** Data: whole-genome ecotype results alongside AMR-only ecotype results for the same species. Method: paired comparison of environmental-effect direction and significance. Question: is AMR more or less environmentally structured within species than the genome as a whole?
