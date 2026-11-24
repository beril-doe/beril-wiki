<!-- tension-hash: 0aad5f5587d29647 -->
# Soil Depletion Versus Plant-Association Enrichment of Nitrogen-Fixation and ipdC Genes

Two projects report plant-growth-promoting (PGP) gene enrichment in ways that look opposed. One finds nifH depleted in soil, while another finds nitrogen fixation enriched in plant-associated genomes. Separately, the ipdC result changes with the phylogenetic adjustment. The comparison matters because the concept page [[concepts/environmental-enrichment-of-plant-growth-promoting-genes-in-soil-and-rhizosphere]] covers presence-based, species-level enrichment, and the direction of a result seems to depend on the environment contrast and on taxonomic control. An odds ratio (OR) is the odds of a gene being present in one group divided by the odds in another; OR below 1 means depletion and OR above 1 means enrichment.

## Evidence Sides

**Side A: depletion in soil, and a conclusion that depends on adjustment**
- nifH is depleted in soil (OR 0.60). [src: pgp_pangenome_ecology]
- ipdC is non-significant in the raw test. [src: pgp_pangenome_ecology]
- ipdC is depleted under phylum control, meaning the comparison is adjusted for phylum, a high-level taxonomic rank. [src: pgp_pangenome_ecology]
- The conclusion for ipdC therefore depends on the phylogenetic adjustment. [src: pgp_pangenome_ecology]

**Side B: enrichment in plant-associated genomes**
- Nitrogen fixation is enriched in plant-associated genomes (OR 2.71). [src: plant_microbiome_ecotypes]

The two nitrogen results use different comparisons. Side A tests the single gene nifH against soil, and Side B tests a nitrogen-fixation category against plant association. The figures are not directly interchangeable, and neither is preferred here.

## Possible Reconciliations

- **Hypothesis 1: different contrasts.** Soil versus other environments and plant-associated versus other genomes may be separate questions, so both results could hold at once.
- **Hypothesis 2: different units.** A gene-level marker (nifH) and a broader nitrogen-fixation category may not capture the same set of genomes.
- **Hypothesis 3: taxonomic confounding.** The ipdC reversal suggests that taxonomic structure can mask or create enrichment. The nitrogen results may also shift under a common adjustment.

None of these is established by the cited evidence.

## Resolving Work

- Re-run the nifH and nitrogen-fixation tests on one shared genome set, using logistic regression with the same phylum control. This asks whether the opposite directions persist when the data and adjustment are identical.
- Cross-tabulate soil and plant-associated labels for the same species and test both contrasts against one reference group. This asks whether soil and plant association pull nifH in different directions.
- Compare ipdC raw and phylum-controlled tests, adding progressively finer taxonomic ranks. This asks at which rank the reversal from non-significant to depleted appears.
- Map which genes define the nitrogen-fixation category and test nifH alone and the category alone. This asks whether the category and the single gene differ in direction.
- Check environment label quality by manually auditing a sample of soil and plant-associated assignments. This asks whether label error could produce either direction.
