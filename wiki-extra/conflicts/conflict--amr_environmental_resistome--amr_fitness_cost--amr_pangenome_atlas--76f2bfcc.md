<!-- tension-hash: 87f3f57020205fca -->
# Broad ecological AMR association vs weak within-species environmental structure

The [[concepts/environmental-resistome]] record presents a disagreement about what environmental AMR associations establish. At broad ecological scales, environment explains measurable AMR-composition variance and the association survives several controls. Yet within species, effects are uncommon, heterogeneous, and vulnerable to phylogenetic, sampling, geographic, annotation, and classification limitations. The distinction matters because a community-level association does not by itself demonstrate that environmental exposure causes selection within populations.

## Evidence Sides

**Broad ecological association is robust**

Environment effects explain 2–13% of AMR-composition variance (η² = 0.02–0.13), although phylogeny, sampling, isolation, gene mobility, and annotation coverage may explain part of these effects. [src: amr_environmental_resistome] The environment–AMR association persisted after majority-vote thresholds and phylum- and family-level controls, supporting an ecological signal beyond a simple species-label artifact. [src: amr_environmental_resistome] These results support an association that is not reducible to one obvious classification control.

**Within-species structure and causal selection remain weak or unresolved**

Only 20 of 141 testable families (14%) showed significant within-family effects after FDR correction. Whole-genome ecotype analysis found environmental effects significant and positive in 12 species (7.0%), significant and negative in 4 species (2.3%), and absent in 156 species (90.7%). [src: amr_environmental_resistome, ecotype_analysis] Strain analysis found AMR ecotypes in 19.5% of eligible species, but metadata were sparse and only 2 species passed strict testing criteria. [src: amr_strain_variation] Thus broad ecological association remains compatible with weak or unresolved within-species environmental structure. [src: amr_environmental_resistome, ecotype_analysis, amr_strain_variation]

The positive relationship between AMR and phylogenetic distance in 701/1,261 species may reflect lineage-associated acquisition or uneven sampling of lineages across environments; available analyses do not separate these explanations. Geographic coordinates were often missing or imprecise, and partial correlations assume linear relationships between distance matrices. [src: amr_strain_variation, ecotype_analysis]

## Possible Reconciliations

- **Scale hypothesis:** Environment may structure species or communities without consistently selecting AMR differences within species.
- **Confounding hypothesis:** Phylogenetic composition, isolation source, sampling intensity, and gene mobility may generate part of the broad association while masking or replacing direct exposure effects.
- **Measurement hypothesis:** Majority-vote classification, sparse metadata, imprecise coordinates, and linear distance-matrix assumptions may reduce power to detect localized adaptation.
- **Heterogeneous-selection hypothesis:** Environmental selection may be strong only in particular species, habitats, or exposure regimes, yielding positive, negative, and absent effects across taxa.

## Resolving Work

- Assemble densely sampled isolates within species across matched environments, with standardized exposure metadata, to test whether AMR frequencies differ after controlling for lineage.
- Apply hierarchical models that partition species, lineage, site, and environment effects, asking whether environment explains residual within-lineage AMR variation.
- Replace majority-vote labels with gene- and allele-level resistance profiles, asking whether within-species signals persist when genomic variation is retained.
- Improve geographic and exposure resolution, then compare nonlinear and spatial models to determine whether weak effects reflect inadequate environmental representation or absent adaptation.
