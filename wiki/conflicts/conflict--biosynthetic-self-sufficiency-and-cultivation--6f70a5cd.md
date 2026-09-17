<!-- tension-hash: 6f70a5cd97013747 -->
# Genome expansion versus pathway completeness as evidence of biosynthetic self-sufficiency

Two projects in this corpus disagree about what evidence bears on biosynthetic self-sufficiency in cultured subsurface genomes — the capacity to make one's own building blocks rather than scavenging them from neighbours or the environment. One reads expanded genome content as supporting a self-sufficiency model; the other measures amino-acid biosynthesis pathways directly, finds no elevated completeness, and finds lower completeness in the deep cohort after quality filtering. The disagreement matters because it decides what counts as evidence for self-sufficiency at all: the two lines measure different aspects of genomic and metabolic capacity, so a gene-content result and a pathway-completeness result cannot stand in for one another. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface] This tension originates in [[concepts/biosynthetic-self-sufficiency-and-cultivation]].

## Evidence Sides

**Genome expansion supports self-sufficiency.** The Bacillota_B analysis of deep-clay lineages supports a self-sufficiency model for cultivable subsurface genomes through larger genome size and greater OG content — OG meaning orthologous group, a cluster of genes inferred to share common ancestry and function. [src: bacillota_b_subsurface_accessory] On this reading, deep-clay genomes carry more functional capacity than their comparators, and that added capacity is interpreted as room for autonomous biosynthesis.

**Pathway completeness does not support it.** The clay-confined cultured-genome project applies GapMind — a tool that reconstructs amino-acid biosynthesis pathways from genome annotations and scores their completeness — and finds no elevated amino-acid pathway completeness in the relevant cohort. [src: clay_confined_subsurface] After quality filtering of the genomes, the direction reverses rather than merely flattening: the deep cohort shows *lower* completeness. [src: clay_confined_subsurface] This is a null result on the primary comparison plus a negative result after filtering, not a weaker version of the first side's positive finding.

## Possible Reconciliations

*Hypothesis 1 — different measurands.* The two sides may not be in contact at all: one counts total genomic and orthologous-group content, the other scores a specific metabolic module, and these measure different aspects of genomic and metabolic capacity. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface] Under this hypothesis both results stand and neither licenses the other's conclusion.

*Hypothesis 2 — expansion is non-biosynthetic.* Genome expansion in deep-clay lineages may be concentrated in functions unrelated to amino-acid biosynthesis, leaving biosynthetic pathways flat or degraded while total OG content rises. [src: bacillota_b_subsurface_accessory]

*Hypothesis 3 — quality filtering is the pivot.* The reversal to lower completeness appears only after quality filtering, so genome incompleteness may be generating or masking the apparent signal in one or both cohorts. [src: clay_confined_subsurface]

These findings should not be reconciled by treating genome expansion as proof of biosynthetic self-sufficiency. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface]

## Resolving Work

- Run GapMind on the same genome set used for the OG-enrichment comparison, so pathway completeness and OG content are scored on one denominator: does expansion co-occur with completeness genome-by-genome?
- Partition the enriched OGs by functional category and ask what fraction falls in biosynthetic versus non-biosynthetic functions — does the expansion touch biosynthesis at all?
- Repeat the GapMind comparison at several quality-filtering thresholds and report the completeness difference at each: at which threshold does the deep-cohort direction flip, and is the flip threshold-driven?
- Test amino-acid auxotrophy experimentally in isolates from both cohorts using defined media drop-out growth assays, to check whether either genomic signal predicts phenotype.
- Compare genome size against per-pathway GapMind scores across cohorts to determine whether size explains any biosynthetic variance once cohort is controlled.
