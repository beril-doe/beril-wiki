---
type: "Research direction"
description: "About a fifth of the genes in Pseudomonas stutzeri RCH2 (21.5%) are costly in the lab yet dispensable, far above the next organism (14.0%). Are they costly only because the lab differs from this denitrifier's natural anaerobic life, or do they reflect accumulation of costly mobile DNA?"
hypothesis: "Many of its costly dispensable genes are costly only in aerobic growth. They should lose their cost under anaerobic denitrifying conditions and be less rich in mobile-element annotations than the costly genes that stay costly."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The existing oxygen comparison in RCH2 is confounded with metal salt, so the decisive matched aerobic and anaerobic competition has to be newly measured."
collections: ["kescience-fitnessbrowser"]
findings: ["costly_dispensable_genes--81b8bf3d", "costly_dispensable_genes--31cecf6a", "counter_ion_effects--5a523214"]
conflicts: []
papers: ["22448042", "32994326", "27474723", "29769716"]
builds_on: ["findings/costly_dispensable_genes--81b8bf3d", "findings/costly_dispensable_genes--31cecf6a", "findings/counter_ion_effects--5a523214"]
projects: ["costly_dispensable_genes", "counter_ion_effects"]
topics: ["laboratory-fitness-versus-natural-selection-and-gene-conservation"]
---
# Is one denitrifier's costly dispensable gene set a lab mismatch or mobile-DNA load?

About a fifth of the genes in Pseudomonas stutzeri RCH2 (21.5%) are costly in the lab yet dispensable, far above the next organism (14.0%). Are they costly only because the lab differs from this denitrifier's natural anaerobic life, or do they reflect accumulation of costly mobile DNA?

## Hypothesis

Many of its costly dispensable genes are costly only in aerobic growth. They should lose their cost under anaerobic denitrifying conditions and be less rich in mobile-element annotations than the costly genes that stay costly.

## Why it matters

It would show whether outlier organisms in cost surveys reveal real genomic parasitism or only a mismatch between assay and native lifestyle, which affects how lab-cost results are read as evidence for selection in nature.

## How to test it

Existing aerobic and anaerobic experiments in RCH2 are confounded with the metal salt used, so they can only frame the question. Use the Fitness Browser to list RCH2's costly dispensable genes and compare mobile-element keyword enrichment and singleton share against the other costly genes. The decisive step is new: run pooled mutant competition in a defined medium under aerobic and anaerobic nitrate-reducing growth with no metal added, and see which genes change cost.

## What would support or refute it

Support: a large share of the costly set loses its cost anaerobically and is not mobile-element rich. Refute: cost persists across oxygen states and stays concentrated in transposase, phage and insertion-sequence genes, which favours genomic invasion.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The existing oxygen comparison in RCH2 is confounded with metal salt, so the decisive matched aerobic and anaerobic competition has to be newly measured.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/costly_dispensable_genes--81b8bf3d|Pseudomonas stutzeri RCH2 is an extreme outlier in costly dispensable gene share]] (Insufficient literature evidence)
- Finding: [[findings/costly_dispensable_genes--31cecf6a|Costly dispensable genes are strongly enriched for mobile-element keywords]] (Insufficient literature evidence)
- Finding: [[findings/counter_ion_effects--5a523214|Same-metal copper salts in psRCH2 correlate weakly across counter ions]] (Insufficient literature evidence)

## Closest published work

- [PMID 22448042](https://pubmed.ncbi.nlm.nih.gov/22448042/) The Black Queen Hypothesis: evolution of dependencies through adaptive gene loss.
- [PMID 32994326](https://pubmed.ncbi.nlm.nih.gov/32994326/) Gene Dispensability in Escherichia coli Grown in Thirty Different Carbon Environments.
- [PMID 27474723](https://pubmed.ncbi.nlm.nih.gov/27474723/) Novel Metal Cation Resistance Systems from Mutant Fitness Analysis of Denitrifying Pseudomonas stutzeri.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.

PMID 32994326 shows gene dispensability depends on carbon environment in E. coli, and PMID 22448042 predicts loss of costly dispensable functions, but neither tests whether an outlier organism's costly set is an assay-mismatch effect.
