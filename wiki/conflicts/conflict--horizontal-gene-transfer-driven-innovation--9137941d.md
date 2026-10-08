<!-- tension-hash: 9137941d71787a29 -->
# Plant-Growth-Promoting Traits: Vertically Inherited Core Genes or Transposase-Linked Mobile Cargo?

Two projects disagree on how plant-growth-promoting (PGP) traits, genes that help bacteria benefit plant hosts, spread among bacteria. One reads high core-genome membership as support for vertical inheritance and rejected its own horizontal gene transfer (HGT) hypothesis; HGT is the movement of genes between lineages. The other finds PGP markers among the genes most strongly co-occurring with transposases, the enzymes of mobile genetic elements. The answer matters for [[concepts/horizontal-gene-transfer-driven-innovation]]. It decides whether PGP traits count as mobile ecological innovations or as stable lineage features, and the two projects measure different quantities. [src: pgp_pangenome_ecology, plant_microbiome_ecotypes]

## Evidence Sides

**Side A: PGP genes are more core than baseline, with vertical inheritance cited for acdS**

The PGP project found all 13 PGP genes more core than the 46.8% baseline. Here "core" means classified as core by the gene's species pangenome, the full gene set across a species. [src: pgp_pangenome_ecology] On this basis it rejected its HGT hypothesis and cited predominantly vertical (parent-to-offspring) inheritance of acdS. [src: pgp_pangenome_ecology] The measure used is the within-species core fraction. [src: pgp_pangenome_ecology, plant_microbiome_ecotypes]

**Side B: PGP markers carry the strongest transposase co-occurrence signal**

The plant-microbiome deep dive found that PGP markers had the strongest transposase co-occurrence. [src: plant_microbiome_ecotypes] Examples were ACC deaminase, with an odds ratio (OR, the odds of co-occurrence relative to the odds without the marker) of OR=6.43, and nitrogen fixation, with OR=3.76. [src: plant_microbiome_ecotypes] Nitrogen fixation was also 72.3% core in that project. [src: plant_microbiome_ecotypes] The measure used is species-level co-occurrence with transposase singletons, meaning transposase gene clusters classified as singletons within their own species pangenome. [src: pgp_pangenome_ecology, plant_microbiome_ecotypes]

**Shared limit**

Neither side establishes what share of PGP carriage arrived by transfer. [src: pgp_pangenome_ecology, plant_microbiome_ecotypes]

## Possible Reconciliations

- **Hypothesis 1, frequent events under purifying selection:** The plant report itself suggests that individual HGT events are common while the markers as a class are under purifying selection, which removes harmful changes and keeps genes conserved. [src: pgp_pangenome_ecology, plant_microbiome_ecotypes] If so, a gene could be transferred often and still end up core once it is fixed in a species.
- **Hypothesis 2, different scales:** The two projects measure different things: within-species core fraction versus species-level co-occurrence with transposase singletons. [src: pgp_pangenome_ecology, plant_microbiome_ecotypes] A high core fraction within a species may fit with transfer between species. Under this reading, the two results answer different questions and do not contradict each other.
- **Hypothesis 3, a proxy artefact:** Transposase co-occurrence may track genome size or the overall load of mobile elements rather than transfer of the PGP gene itself. This is untested in the evidence here.

## Resolving Work

- **acdS and nitrogen-fixation gene trees reconciled against species trees:** Use the pangenome gene clusters behind both projects and phylogenetic reconciliation, which counts transfer events by comparing gene and species trees. The question is what fraction of PGP carriage is explained by transfer rather than vertical descent, the quantity neither side establishes.
- **Contig co-location of PGP markers with transposases, stratified by core vs. accessory status:** Use the deep dive's data on contigs (assembled stretches of contiguous sequence), splitting marker copies into core and accessory (non-core) classes. The question is whether transposase-adjacent copies are the accessory minority or also occur in core copies.
- **Odds ratios controlled for genome size and total mobile-element count:** Refit the co-occurrence models with these covariates. The question is whether the PGP signals at OR=6.43 and OR=3.76 survive. [src: plant_microbiome_ecotypes]
- **Within-species versus between-species comparison on one shared gene set:** Apply both projects' metrics to the identical 13 PGP genes. [src: pgp_pangenome_ecology] The question is whether the disagreement disappears once the denominators are aligned.
