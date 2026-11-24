<!-- tension-hash: 5cc5b57dfa936cd3 -->
# Horizontal Gene Transfer versus Vertical Core Inheritance: A Tension in Reading Core/Accessory Status of Trait Genes

Projects disagree on whether the core versus accessory (pangenome) status of trait genes points to horizontal gene transfer (HGT, acquisition of DNA from other lineages) or to vertical inheritance (descent from a common ancestor). The cog_analysis report asserts HGT is the primary innovation mechanism, while the plant growth-promoting (PGP) analysis rejects HGT for 13 PGP genes. The plant microbiome report reads the same core status two ways. This matters because the HGT reading is mostly an interpretation of core/accessory status, not a direct transfer test, so the same pattern can support opposite conclusions. See [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]].

## Evidence Sides

**Side A: HGT is read as the innovation mechanism, including for some plant-interaction markers**
- The cog_analysis report asserts HGT, not vertical inheritance, is the primary innovation mechanism in bacterial pangenomes. [src: discoveries]
- PGP genes are mostly core, yet plant-interaction marker singletons co-occur with transposase/integrase singletons, which the report reads as recent HGT on mobile elements. [src: discoveries]
- The plant microbiome report suggests acquisition by HGT followed by core stabilization. [src: plant_microbiome_ecotypes]
- pqqD is largely accessory-leaning (55.5% core, 27.5% singleton). [src: pgp_pangenome_ecology]

**Side B: vertical inheritance with the core**
- The PGP analysis rejects HGT for 13 PGP genes and finds them vertically inherited with the core. [src: pgp_pangenome_ecology]
- The pqqB–pqqC operon is predominantly core. [src: pgp_pangenome_ecology]
- The plant microbiome report reads its core-enriched orthologous groups (OGs) as stable core inheritance. [src: plant_microbiome_ecotypes]
- It finds beneficial genes largely core, contrasting with Loper et al.'s largely accessory Pseudomonas biocontrol traits. It attributes this to taxonomic scope, which it does not test. [src: plant_microbiome_ecotypes]

Both readings rest on core/accessory status. [src: plant_microbiome_ecotypes]

## Possible Reconciliations

- **Hypothesis: gene-level versus operon-level behavior.** Standalone genes such as pqqD may spread horizontally while the intact pqqB–pqqC operon is inherited vertically, so each report describes a different unit. [src: pgp_pangenome_ecology]
- **Hypothesis: transfer then stabilization.** Genes may be acquired by HGT and later fixed in the core, making core status compatible with both readings. [src: plant_microbiome_ecotypes]
- **Hypothesis: taxonomic scope.** The difference from Loper et al.'s accessory Pseudomonas traits may reflect clade breadth, which the plant microbiome report does not test. [src: plant_microbiome_ecotypes]
- **Hypothesis: different gene classes.** Mobile-element-linked singletons may reflect recent HGT, while core PGP genes reflect ancestral inheritance. [src: discoveries]

## Resolving Work

- Data: gene trees and species trees for the 13 PGP genes. Method: phylogenetic incongruence tests. Question: do core PGP genes track the species phylogeny, as vertical inheritance predicts?
- Data: genomic neighborhoods of plant-interaction marker singletons. Method: test for flanking transposase/integrase and mobile-element signatures. Question: is the co-occurrence with transposase/integrase singletons evidence of transfer or coincidence?
- Data: pqqD orphan copies versus pqqB–pqqC operon copies. Method: compare codon usage and phylogenetic placement. Question: does pqqD spread horizontally while the operon does not?
- Data: plant microbiome genes and Pseudomonas biocontrol genes under matched taxonomic sampling. Method: rerun core/accessory classification within the same clades. Question: does taxonomic scope explain the contrast with Loper et al.?
- Data: core-enriched OGs from the plant microbiome report. Method: ancestral-state reconstruction. Question: were they acquired then stabilized, or always present?
