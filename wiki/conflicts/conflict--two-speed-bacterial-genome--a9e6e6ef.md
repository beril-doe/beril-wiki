<!-- tension-hash: a9e6e6ef9670e152 -->
# Do Metabolic and Defense Functions Sit in the Conserved Core or the Variable Genome?

The two-speed genome model in [[concepts/two-speed-bacterial-genome]] treats the conserved core as the home of metabolism and housekeeping and the accessory genome as the home of mobile, defense and unknown functions. Three projects suggest that functional classes do not map cleanly onto this core/accessory split. Amino acid metabolism looks core-enriched in one analysis [src: cog_analysis] but depleted among essential-core genes in another [src: discoveries]. Antimicrobial resistance (AMR) overall is enriched in the accessory genome, yet intrinsic AMR genes are core residents [src: amr_pangenome_atlas]. This matters because concept pages that assign whole functional categories to one "speed" may overstate how cleanly the genome partitions.

## Evidence Sides

**Side 1: Amino acid metabolism is core-enriched (COG scheme, core versus singleton)**
In the cross-species analysis using Clusters of Orthologous Groups (COG, a protein-family functional classification), COG E (amino acid metabolism) was core-enriched. It was reported as -1.81% enrichment with 81% consistency [src: cog_analysis]. The contrast here is core versus singleton genes (genes found in only one genome).

**Side 2: Essential-core genes are depleted in amino acid functions (SEED scheme, essential versus non-essential)**
Under the SEED subsystem classification, essential-core genes were depleted in Amino Acids by -5.6 pp (percentage points) relative to non-essential genes [src: discoveries]. The contrast here is essential versus non-essential genes, not core versus accessory.

**Side 3: Defense splits across both compartments**
Intrinsic AMR genes were core residents, even though AMR overall was enriched in the accessory genome [src: amr_pangenome_atlas].

**Shared caveat**
The comparisons use different category schemes (COG versus SEED) and different contrasts (core versus singleton, essential versus non-essential), so they are not direct contradictions. They do show that metabolism and defense each contain both conserved and variable components [src: cog_analysis, discoveries, amr_pangenome_atlas].

## Possible Reconciliations

- **Hypothesis A (nested partitions):** Amino acid genes may be broadly conserved across species but conditionally rather than universally required. If so, they would fall in the core yet outside its essential subset, and Sides 1 and 2 would describe different layers of the same genes.
- **Hypothesis B (classification artifact):** COG E and the SEED Amino Acids category may cover different gene sets. If so, the apparent opposition reflects the category schemes rather than the biology.
- **Hypothesis C (intrinsic versus acquired defense):** Defense may contain an ancestral, vertically inherited layer that sits in the core and an acquired layer that sits in the accessory genome. Under this hypothesis, Side 3 would be the defense counterpart of the metabolism pattern.

## Resolving Work

- **Common classification for both contrasts:** Map the SEED Amino Acids genes and the COG E genes onto one shared annotation and recompute the core-versus-singleton and essential-versus-non-essential contrasts. Question: does the sign difference persist when the category definition is held fixed?
- **Three-tier gene partitioning:** Using pangenome (the full gene set across a species' genomes) conservation calls joined to essentiality data, split genes into essential-core, non-essential-core and accessory tiers, then test COG E membership across all three. Question: are amino acid genes concentrated in the non-essential core, as Hypothesis A predicts?
- **Intrinsic versus acquired AMR split:** Using the AMR cluster annotations, separate intrinsic from acquired AMR genes and compare their core and accessory distributions by COG category. Question: does the defense split follow the intrinsic/acquired boundary?
- **Per-species consistency check:** Re-examine the species that make COG E core-enrichment less than fully consistent. Question: do those species also show the essential-core depletion reported for Amino Acids?
