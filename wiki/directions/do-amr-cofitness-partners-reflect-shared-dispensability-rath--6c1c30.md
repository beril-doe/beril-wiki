---
type: "Research direction"
description: "Is the flagellar and biosynthesis enrichment among antimicrobial-resistance gene cofitness partners explained by shared dispensability in the lab?"
hypothesis: "Random non-AMR genes matched on mean fitness show equal flagellar enrichment in their cofitness neighbourhoods, so the signal is a general feature of dispensable genes."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Cofitness and fitness tables are in the catalog; the matched permutation has not been run."
databases: ["kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.cofit", "kescience.fitnessbrowser.genefitness", "kescience.fitnessbrowser.experiment", "kescience.fitnessbrowser.gene"]
findings: ["amr_cofitness_networks--5e805dd1", "amr_cofitness_networks--7d0cfcd7", "amr_cofitness_networks--ca058750"]
conflicts: []
papers: ["31501286", "28542589", "29769716", "23499305"]
builds_on: ["findings/amr_cofitness_networks--5e805dd1", "findings/amr_cofitness_networks--7d0cfcd7", "findings/amr_cofitness_networks--ca058750"]
projects: ["amr_cofitness_networks"]
topics: ["laboratory-fitness-versus-natural-selection-and-gene-conservation"]
---
# Do AMR cofitness partners reflect shared dispensability rather than regulatory coupling?

Is the flagellar and biosynthesis enrichment among antimicrobial-resistance gene cofitness partners explained by shared dispensability in the lab?

## Hypothesis

Random non-AMR genes matched on mean fitness show equal flagellar enrichment in their cofitness neighbourhoods, so the signal is a general feature of dispensable genes.

## Why it matters

It would show whether cofitness networks of resistance genes encode biology or lab artefacts, affecting how cofitness is used for resistance gene function.

## How to test it

For organisms with the flagellar enrichment, draw random non-AMR genes matched on mean fitness and conservation class, compute cofitness neighbourhood GO enrichment, and compare with AMR genes. Compute cofitness separately for antibiotic versus standard conditions, and check whether flagellar knockouts have positive mean fitness.

## What would support or refute it

Support: matched controls reproduce the enrichment, and it does not rise under antibiotics. Refute: AMR genes stay uniquely enriched, and more so under antibiotic stress.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Cofitness and fitness tables are in the catalog; the matched permutation has not been run.

## Builds on

- Finding: [[findings/amr_cofitness_networks--5e805dd1|Flagellar motility GO terms enriched in AMR support networks across organisms]] (Candidate novel)
- Finding: [[findings/amr_cofitness_networks--7d0cfcd7|Organism identity shapes AMR support networks more than resistance mechanism]] (Candidate novel)
- Finding: [[findings/amr_cofitness_networks--ca058750|Support-network size does not track AMR gene fitness cost]] (Candidate novel)

## Closest published work

- [PMID 31501286](https://pubmed.ncbi.nlm.nih.gov/31501286/) Multidrug Resistance Regulators MarA, SoxS, Rob, and RamA Repress Flagellar Gene Expression and Motility in Salmonella enterica Serovar Typhimurium.
- [PMID 28542589](https://pubmed.ncbi.nlm.nih.gov/28542589/) Validating regulatory predictions from diverse bacteria with mutant fitness data.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 23499305](https://pubmed.ncbi.nlm.nih.gov/23499305/) Intrinsic antibiotic resistance: mechanisms, origins, challenges and solutions.

31501286 links resistance regulators to flagellar repression in Salmonella, but no paper tests this across organisms against fitness-matched controls.
