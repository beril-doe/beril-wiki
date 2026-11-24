---
type: "Research direction"
description: "Desulfovibrio vulgaris is the only one of seven organisms lacking a complete serine pathway by GapMind. Is serine synthesis truly lost, or does it use divergent enzymes?"
hypothesis: "D. vulgaris has lost serine synthesis and relies on environmental serine, so it will not grow without serine and no divergent homolog of the canonical enzymes will be found."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Homology search uses catalog tables, but the growth test needs new cultures."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser", "kescience.paperblast"]
tables: ["kbase.ke_pangenome.gapmind_pathways", "kbase.ke_pangenome.eggnog_mapper_annotations", "kescience.paperblast.curatedgene", "kescience.fitnessbrowser.gene"]
findings: ["essential_metabolome--b2b186cc", "essential_metabolome--04b688de", "essential_metabolome--be48dd15"]
conflicts: []
papers: ["15077118", "29769716", "32576650", "24910088"]
builds_on: ["findings/essential_metabolome--b2b186cc", "findings/essential_metabolome--04b688de", "findings/essential_metabolome--be48dd15"]
projects: ["essential_metabolome"]
topics: ["metabolic-models-and-pathway-level-evidence"]
---
# Is apparent serine auxotrophy in Desulfovibrio vulgaris genomic economy or a missed pathway?

Desulfovibrio vulgaris is the only one of seven organisms lacking a complete serine pathway by GapMind. Is serine synthesis truly lost, or does it use divergent enzymes?

## Hypothesis

D. vulgaris has lost serine synthesis and relies on environmental serine, so it will not grow without serine and no divergent homolog of the canonical enzymes will be found.

## Why it matters

It would separate real gene loss from annotation gaps in pathway-based prototrophy calls. It would also bear on whether prototrophy is the usual state in free-living bacteria.

## How to test it

Search D. vulgaris proteins for divergent homologs of serine biosynthesis enzymes using eggNOG annotations and curated PaperBLAST genes. Check the pangenome for the same gap across Desulfovibrio genomes. Test growth in defined medium with and without serine.

## What would support or refute it

Support: no candidate enzyme is found, the gap is shared across the species, and growth needs serine. Refute: a divergent enzyme is found or growth occurs without serine, which would mean annotation failure.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Homology search uses catalog tables, but the growth test needs new cultures.

## Builds on

- Finding: [[findings/essential_metabolome--b2b186cc|Genomic economy may explain apparent serine auxotrophy in Desulfovibrio vulgaris]] (Candidate novel)
- Finding: [[findings/essential_metabolome--04b688de|Desulfovibrio vulgaris alone lacks a complete serine biosynthesis pathway]] (Insufficient literature evidence)
- Finding: [[findings/essential_metabolome--be48dd15|Amino acid prototrophy may be the ancestral state in free-living bacteria]] (Candidate novel)

## Closest published work

- [PMID 15077118](https://pubmed.ncbi.nlm.nih.gov/15077118/) The genome sequence of the anaerobic, sulfate-reducing bacterium Desulfovibrio vulgaris Hildenborough.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 32576650](https://pubmed.ncbi.nlm.nih.gov/32576650/) GapMind: Automated Annotation of Amino Acid Biosynthesis.
- [PMID 24910088](https://pubmed.ncbi.nlm.nih.gov/24910088/) Less is more: selective advantages can explain the prevalent loss of biosynthetic genes in bacteria.

The D. vulgaris genome (15077118) and mutant phenotype study (29769716) do not address serine loss; GapMind (32576650) supplies the pathway calls tested here.
