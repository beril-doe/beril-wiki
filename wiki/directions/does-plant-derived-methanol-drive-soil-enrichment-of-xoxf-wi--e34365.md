---
type: "Research direction"
description: "Within Acidobacteriota, xoxF is enriched in soil/sediment genomes (odds ratio 2.16, adjusted p = 2.2 \u00d7 10\u207b\u2075). Is this selection for lanthanide-dependent methanol oxidation fed by plant-derived methanol, or a lineage-composition effect?"
hypothesis: "If soil selects for xoxF, xoxF-carrying soil Acidobacteriota will more often carry genes for plant-polysaccharide methyl-ester release (e.g. pectin methylesterase) than xoxF-negative soil relatives, and xoxF will be gained independently in several soil clades. XoxF-bearing soil isolates should also grow on methanol only when a lanthanide is supplied. This is a hypothesis, since the finding itself does not test a mechanism."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Genome annotations and habitat labels exist, but the decisive growth and expression tests need new isolates and microcosm measurements."
collections: ["kbase-ke-pangenome", "nmdc-ncbi-biosamples", "kbase-genomes"]
findings: ["lanthanide_methylotrophy_atlas--73b82896", "lanthanide_methylotrophy_atlas--6465f1d3"]
conflicts: []
papers: ["38369453", "29997591", "32341564", "42678158"]
builds_on: ["findings/lanthanide_methylotrophy_atlas--73b82896", "findings/lanthanide_methylotrophy_atlas--6465f1d3"]
projects: ["lanthanide_methylotrophy_atlas"]
topics: ["lanthanide-dependent-methylotrophy"]
---
# Does plant-derived methanol drive soil enrichment of xoxF within Acidobacteriota?

Within Acidobacteriota, xoxF is enriched in soil/sediment genomes (odds ratio 2.16, adjusted p = 2.2 × 10⁻⁵). Is this selection for lanthanide-dependent methanol oxidation fed by plant-derived methanol, or a lineage-composition effect?

## Hypothesis

If soil selects for xoxF, xoxF-carrying soil Acidobacteriota will more often carry genes for plant-polysaccharide methyl-ester release (e.g. pectin methylesterase) than xoxF-negative soil relatives, and xoxF will be gained independently in several soil clades. XoxF-bearing soil isolates should also grow on methanol only when a lanthanide is supplied. This is a hypothesis, since the finding itself does not test a mechanism.

## Why it matters

It would turn a statistical enrichment into an ecological explanation, linking soil xoxF to a specific methanol source, and show whether the soil signal is partly a function of habitat. The H2 environmental analyses were only stratified within phyla, not fitted with a phylogeny-aware mixed model.

## How to test it

Step 1 (lakehouse): among soil/sediment Acidobacteriota genomes in the Pangenome Collection, test whether xoxF carriage co-occurs with pectin-methylesterase and related plant-polymer genes, with family as a random effect. Check on a family-level tree whether xoxF-positive soil genomes arise from independent gains or one clade. Use NMDC BioSamples labels to confirm habitat assignments. Step 2 (experiment): grow xoxF-positive soil Acidobacteriota isolates on methanol with and without added lanthanide, and measure xoxF expression in soil microcosms amended with pectin.

## What would support or refute it

Support: co-occurrence with methanol-releasing genes, multiple independent gains, and lanthanide-dependent methanol growth. Refutation: xoxF enrichment explained by one or few clades, no association with methanol-source genes, and growth independent of lanthanide.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Genome annotations and habitat labels exist, but the decisive growth and expression tests need new isolates and microcosm measurements.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/nmdc-ncbi-biosamples|NMDC BioSamples]]
- Collection: [[data/kbase-genomes|KBase Genomes]]

## Builds on

- Finding: [[findings/lanthanide_methylotrophy_atlas--73b82896|Soil enrichment of xoxF persists within Acidobacteriota]] (Candidate novel)
- Finding: [[findings/lanthanide_methylotrophy_atlas--6465f1d3|Lanthanide-dependent xoxF vastly outnumbers calcium-dependent mxaF across a large genome collection]] (Extends retrieved work)

## Closest published work

- [PMID 38369453](https://pubmed.ncbi.nlm.nih.gov/38369453/) Weathered granites and soils harbour microbes with lanthanide-dependent methylotrophic enzymes.
- [PMID 29997591](https://pubmed.ncbi.nlm.nih.gov/29997591/) Lanthanide-Dependent Methanol Dehydrogenases of XoxF4 and XoxF5 Clades Are Differentially Distributed Among Methylotrophic Bacteria and They Reveal Different Biochemical Properties.
- [PMID 32341564](https://pubmed.ncbi.nlm.nih.gov/32341564/) A complete domain-to-species taxonomy for Bacteria and Archaea.
- [PMID 42678158](https://pubmed.ncbi.nlm.nih.gov/42678158/) xoxF-linked methanol oxidation signals recur across wetland metagenomes.

PMID 38369453 found xoxF3/xoxF5 clusters in Acidobacteria and other phyla in weathered granite and soil but did not test habitat enrichment within a phylum or a methanol-source mechanism; PMID 29997591 describes clade distributions among methylotrophs, not habitat.
