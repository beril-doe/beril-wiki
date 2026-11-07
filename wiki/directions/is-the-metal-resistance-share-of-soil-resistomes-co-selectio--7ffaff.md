---
type: "Research direction"
description: "Metal resistance makes up 45% of AMR in aquatic species and 44% in soil species but 6% in human gut species. Are metal-resistance genes physically linked to antibiotic-resistance genes in soil genomes, as co-selection would predict, or do they sit apart?"
hypothesis: "Metal-resistance and antibiotic-resistance genes are adjacent in genomes more often than chance in soil and aquatic species with large metal shares, and less often in gut species."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Gene order is available but not yet analysed for neighbours; it needs a genome-scale neighbourhood computation."
collections: ["kbase-ke-pangenome"]
findings: ["amr_environmental_resistome--0cf37cb9", "amr_environmental_resistome--e39caf4e"]
conflicts: ["conflict--environmental-resistome--ecbc42fd"]
papers: ["16537105", "28528649", "38897736", "41601069"]
builds_on: ["findings/amr_environmental_resistome--0cf37cb9", "findings/amr_environmental_resistome--e39caf4e", "conflicts/conflict--environmental-resistome--ecbc42fd"]
projects: ["amr_environmental_resistome", "amr_pangenome_atlas"]
topics: ["resistance-defense-systems-and-mobile-elements"]
---
# Is the metal-resistance share of soil resistomes co-selection for antibiotic resistance?

Metal resistance makes up 45% of AMR in aquatic species and 44% in soil species but 6% in human gut species. Are metal-resistance genes physically linked to antibiotic-resistance genes in soil genomes, as co-selection would predict, or do they sit apart?

## Hypothesis

Metal-resistance and antibiotic-resistance genes are adjacent in genomes more often than chance in soil and aquatic species with large metal shares, and less often in gut species.

## Why it matters

If linked, metal pollution could maintain antibiotic resistance through co-selection. If unlinked, the metal share is a separate adaptation, and the resistome should not be read as an antibiotic-resistance reservoir.

## How to test it

Using the Pangenome Collection, take species with environment labels and gene-position information. Compute how often each metal-resistance cluster lies within a fixed gene distance of an antibiotic-resistance cluster. Compare against a null from shuffling positions of other accessory genes. Contrast soil/aquatic, clinical and gut species, controlling for number of AMR clusters per species. Repeat with the 18.7% of clusters lacking a mechanism label treated as a separate class, since their exclusion could bias environment comparisons.

## What would support or refute it

Support: excess adjacency only in metal-rich environments. Refute: adjacency at chance levels everywhere, or equal across environments.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Gene order is available but not yet analysed for neighbours; it needs a genome-scale neighbourhood computation.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/amr_environmental_resistome--0cf37cb9|Metal resistance dominates soil and aquatic AMR but is rare in gut]] (Extends retrieved work)
- Finding: [[findings/amr_environmental_resistome--e39caf4e|Clinical species' resistomes are mostly accessory, soil's less so]] (Extends retrieved work)
- Conflict: [[conflicts/conflict--environmental-resistome--ecbc42fd|AMRFinderPlus catalog scope: broad stress-resistance landscape versus narrow antibiotic-resistance reading, with unclassified fractions that do not match]]

## Closest published work

- [PMID 16537105](https://pubmed.ncbi.nlm.nih.gov/16537105/) Co-selection of antibiotic and metal resistance.
- [PMID 28528649](https://pubmed.ncbi.nlm.nih.gov/28528649/) Metal Resistance and Its Association With Antibiotic Resistance.
- [PMID 38897736](https://pubmed.ncbi.nlm.nih.gov/38897736/) Unravelling the mechanisms of antibiotic and heavy metal resistance co-selection in environmental bacteria.
- [PMID 41601069](https://pubmed.ncbi.nlm.nih.gov/41601069/) Co-selection for heavy metal and multidrug resistance: Cadmium primes bacterial antibiotic resistance by enhancing intrinsic oxidative stress tolerance.

PMIDs 16537105 and 28528649 review co-selection and PMID 41601069 tests one mechanism; none measure genomic linkage across habitats at pangenome scale.
