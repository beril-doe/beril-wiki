<!-- tension-hash: e8ac0fe110ef7248 -->
# Prophage and conjugative-machinery evidence for gene mobilization: genome-wide association versus local and mechanistic support

Mobile genetic elements (MGEs; prophages, plasmids and integrative elements that can move DNA between cells) are often invoked to explain how resistance and other adaptive genes spread. In this corpus, prophage density is strongly associated with resistance-gene breadth, while local proximity is modest and heterogeneous [src: prophage_amr_comobilization]. Conjugative-machinery co-occurrence and transfer counts are reported alongside no CAZy genes on plasmids [src: t4ss_cazy_environmental_hgt]. This matters for [[concepts/environmental-resistome]]: if mobile elements are cited as a driver of resistome structure, the claim's evidence grade depends on which kind of evidence is admitted.

## Evidence Sides

**Side A: Aggregate association signals link mobile elements to gene repertoires**

Species with higher prophage density were strongly associated with greater antimicrobial-resistance (AMR) breadth. The Spearman rank correlation (rho, a measure of association between ranked values) was rho=0.572, and the partial rho was 0.464 after controlling for genome count. [src: prophage_amr_comobilization]

For type IV secretion system (T4SS, conjugative transfer machinery) loci and carbohydrate-active enzyme (CAZy) genes, the T4SS–CAZy project reports 92 elevated co-occurrences. It also reports 77 horizontal gene transfer (HGT) events for glycosyltransferase family 2 (GT2) genes and 32 normalized high-confidence cross-phylum events. T4SS-positive genomes had 10× higher MGE density. [src: t4ss_cazy_environmental_hgt]

**Side B: Local and mechanistic evidence does not demonstrate transfer**

The local proximity of AMR genes to prophages was modest and heterogeneous, with a median species-level odds ratio (OR; the odds of the outcome in one group relative to another) of 0.85. [src: prophage_amr_comobilization]

The T4SS–CAZy project found no CAZy genes on plasmids by ICEfinder, a tool that detects integrative and conjugative elements. It found only 12 integrative mobilizable elements (IMEs) among the top 100 accumulators. Its evidence therefore supports dissemination as a hypothesis rather than demonstrated transfer. [src: t4ss_cazy_environmental_hgt]

## Possible Reconciliations

- **Hypothesis 1: confounding by lineage or lifestyle.** Density and co-occurrence associations may reflect shared lineage or lifestyle traits that independently raise both MGE load and gene repertoire size. Under this reading, MGEs and the genes in question co-vary without the elements physically carrying those genes.
- **Hypothesis 2: transfer erases local signal.** Transfer may occur through chromosomal or integrative routes that do not leave genes adjacent to intact elements or on plasmids. Mobilization would then be real but invisible to proximity and plasmid-location tests.
- **Hypothesis 3: species-specific mechanisms.** The relationship may differ by species: a minority of lineages may mobilize genes through elements, while most do not.
- **Hypothesis 4: gene class matters.** AMR genes and CAZy genes may differ in how mobile they are, so the two projects may not be testing the same phenomenon.

## Resolving Work

- Prophage density, AMR breadth and a species phylogeny, analysed with phylogenetically controlled regression: does the density–breadth association survive control for shared ancestry?
- Species with high versus low per-species proximity ORs, compared by element type and gene family: which lineages drive the heterogeneity, and do they share a mobilization mechanism?
- The 77 GT2 HGT events [src: t4ss_cazy_environmental_hgt], with flanking regions inspected for integrase, recombinase or IME signatures: are inferred transfers physically associated with integrative elements?
- AMR genes in high-prophage-density species, tested for phylogenetic incongruence with species trees: are AMR genes in MGE-rich genomes horizontally acquired more often than in MGE-poor genomes?
- The same proximity and plasmid-location tests applied to both AMR and CAZy gene sets: does the gap between aggregate and local evidence depend on gene class?
