---
type: "Research direction"
description: "Is the enrichment of flagellar motility terms in antimicrobial resistance cofitness networks caused by flagellar genes being dispensable in lab conditions?"
hypothesis: "Flagellar genes join AMR support networks because both are neutral under most lab conditions. A fitness-variance-matched set of other dispensable gene classes will show the same enrichment, and it will vanish when only antibiotic experiments are used."
approach: "lakehouse analysis"
readiness: "data in the lakehouse"
readiness_basis: "Cofitness, experiment and gene tables are in the catalog for Fitness Browser organisms."
databases: ["kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.cofit", "kescience.fitnessbrowser.experiment", "kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.genedomain"]
findings: ["amr_cofitness_networks--5e805dd1", "amr_cofitness_networks--7d0cfcd7", "amr_cofitness_networks--ca058750"]
conflicts: []
papers: ["31501286", "28542589", "29769716", "23499305"]
builds_on: ["findings/amr_cofitness_networks--5e805dd1", "findings/amr_cofitness_networks--7d0cfcd7", "findings/amr_cofitness_networks--ca058750"]
projects: ["amr_cofitness_networks"]
topics: ["gene-fitness-landscapes-and-cofitness-modules"]
---
# Do AMR support networks reflect flagellar dispensability rather than shared regulation?

Is the enrichment of flagellar motility terms in antimicrobial resistance cofitness networks caused by flagellar genes being dispensable in lab conditions?

## Hypothesis

Flagellar genes join AMR support networks because both are neutral under most lab conditions. A fitness-variance-matched set of other dispensable gene classes will show the same enrichment, and it will vanish when only antibiotic experiments are used.

## Why it matters

It would separate true functional coupling of resistance and motility, as seen for MarA/SoxS repression of flagella in Salmonella, from a data artefact. It would show how far cofitness networks can be read as regulatory networks.

## How to test it

For organisms where flagellar terms were enriched, rebuild AMR cofitness partner sets with partners matched on mean fitness and variance. Compute flagellar enrichment separately in antibiotic experiments and in other experiments, and compare with enrichment for other dispensable classes such as histidine and tryptophan biosynthesis.

## What would support or refute it

Support: enrichment disappears after matching and is absent in antibiotic-only subsets. Refute: flagellar enrichment persists above the matched null, pointing to a real link between resistance and motility.

## Data

Approach: lakehouse analysis. Readiness: data in the lakehouse. Cofitness, experiment and gene tables are in the catalog for Fitness Browser organisms.

## Builds on

- Finding: [[findings/amr_cofitness_networks--5e805dd1|Flagellar motility GO terms enriched in AMR support networks across organisms]] (Candidate novel)
- Finding: [[findings/amr_cofitness_networks--7d0cfcd7|Organism identity shapes AMR support networks more than resistance mechanism]] (Candidate novel)
- Finding: [[findings/amr_cofitness_networks--ca058750|Support-network size does not track AMR gene fitness cost]] (Candidate novel)

## Closest published work

- [PMID 31501286](https://pubmed.ncbi.nlm.nih.gov/31501286/) Multidrug Resistance Regulators MarA, SoxS, Rob, and RamA Repress Flagellar Gene Expression and Motility in Salmonella enterica Serovar Typhimurium.
- [PMID 28542589](https://pubmed.ncbi.nlm.nih.gov/28542589/) Validating regulatory predictions from diverse bacteria with mutant fitness data.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 23499305](https://pubmed.ncbi.nlm.nih.gov/23499305/) Intrinsic antibiotic resistance: mechanisms, origins, challenges and solutions.

31501286 links resistance regulators to flagellar repression in Salmonella, and 28542589 validates regulatory predictions with fitness data; neither tests whether network-level enrichment is a dispensability artefact.
