<!-- tension-hash: d3e253179b304f6f -->
# Metal Resistance and T4SS Gene-Transfer Machinery: Associated or Distinct?

Two reports disagree, or appear to, about how metal resistance relates to mobile gene-transfer machinery in environmental genomes. One report finds metal resistance higher in genomes with GT2 (a glycosyltransferase family from the CAZy carbohydrate-active enzyme database) near T4SS (type IV secretion system, conjugative transfer machinery) loci. [src: t4ss_cazy_environmental_hgt] The other reports 2.8% metal resistance prevalence against 21.8% T4SS prevalence and concludes the two are distinct features. [src: metal_resistance_global_biogeography] This matters because it decides whether metal resistance can be treated as a marker of horizontal gene transfer (HGT) hotspots. The two reports use different datasets and comparisons, so the claims are not reconciled. See [[concepts/metal-resistance-co-occurrence-with-mobile-gene-transfer-hubs]] and [[concepts/geographic-and-biome-distribution-of-environmental-metal-resistance]].

## Evidence Sides

**Side A: metal resistance is higher in GT2 genomes**

- Within the GT2 neighbourhood analysis, metal resistance is higher in GT2 genomes. [src: t4ss_cazy_environmental_hgt]
- The evidence comes from this single observational report, and it stops at association. [src: t4ss_cazy_environmental_hgt]

**Side B: metal resistance and T4SS are distinct features**

- The metal_resistance_global_biogeography report reports 2.8% global metal resistance prevalence in the 22,356 MAGs (metagenome-assembled genomes) with coordinates. [src: metal_resistance_global_biogeography]
- It reports 21.8% T4SS prevalence, a figure given alongside the 2.8%. The two percentages are not stated to share a denominator. [src: metal_resistance_global_biogeography]
- It concludes that AMRFinderPlus (a tool that annotates resistance genes) metal resistance genes and T4SS machinery are distinct features not uniformly co-distributed. [src: metal_resistance_global_biogeography]

## Possible Reconciliations

- **Hypothesis:** The comparisons differ in scope. One looks at GT2-proximal neighbourhoods within genomes, the other at overall prevalence across MAGs with coordinates. Both could hold if metal resistance is enriched only in a subset of T4SS-linked genomes.
- **Hypothesis:** The datasets differ. The 22,356 coordinate-bearing MAGs may not represent the genomes used in the GT2 analysis, so the associations may not transfer.
- **Hypothesis:** The association may be confounded by biome or taxonomy rather than reflecting a functional link.

## Resolving Work

- Data: the GT2 analysis genomes and the 22,356 coordinate MAGs. Method: compute metal resistance prevalence on both with one AMRFinderPlus definition. Question: does the difference persist on shared genomes?
- Data: genomes with and without T4SS in one MAG set. Method: Fisher's exact test (a test of association in a 2x2 table) with FDR (false discovery rate) correction. Question: is metal resistance associated with T4SS presence overall, not only near GT2?
- Data: GT2-proximal and other genomes. Method: logistic regression controlling for biome and phylum. Question: does the GT2 difference survive confounder control?
- Data: metal resistance gene coordinates and T4SS loci. Method: distance-based neighbourhood analysis. Question: do metal resistance genes sit physically near T4SS loci, or only co-occur in the same genome?
