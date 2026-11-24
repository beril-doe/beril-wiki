---
type: "Research direction"
description: "Is Desulfovibrio vulgaris truly unable to make serine, and if so, is the loss an economy that depends on serine being supplied?"
hypothesis: "D. vulgaris Hildenborough cannot grow without serine in defined medium, and its fitness data show serine uptake genes that matter only when serine is scarce. An alternative is a divergent enzyme route that GapMind misses."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Growth tests on serine-free medium are not in the catalog, and the pathway calls come from only 7 organisms."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.experiment", "kbase.ke_pangenome.gapmind_pathways"]
findings: ["essential_metabolome--04b688de", "essential_metabolome--b2b186cc", "essential_metabolome--be48dd15"]
conflicts: []
papers: ["15077118", "29769716", "24910088", "32576650"]
builds_on: ["findings/essential_metabolome--04b688de", "findings/essential_metabolome--b2b186cc", "findings/essential_metabolome--be48dd15"]
projects: ["essential_metabolome"]
topics: ["metabolic-traits-auxotrophy-and-community-dependence"]
---
# Does serine auxotrophy in Desulfovibrio vulgaris reflect genomic economy rather than an unrecognised pathway?

Is Desulfovibrio vulgaris truly unable to make serine, and if so, is the loss an economy that depends on serine being supplied?

## Hypothesis

D. vulgaris Hildenborough cannot grow without serine in defined medium, and its fitness data show serine uptake genes that matter only when serine is scarce. An alternative is a divergent enzyme route that GapMind misses.

## Why it matters

It would separate real auxotrophy from annotation gaps in a model sulfate reducer. It would also add a worked example of gene loss in a free-living bacterium.

## How to test it

Grow D. vulgaris on serine-free and serine-supplied defined media with and without cross-feeding partners. Check lower-confidence GapMind calls and fitness profiles for serine-related genes in the Fitness Browser. If it grows without serine, run isotope labelling to trace the route.

## What would support or refute it

Support: no growth without serine, rescue by serine or a partner, and no alternative pathway in the fitness data. Refute: growth without serine, or fitness defects in a candidate non-canonical route.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Growth tests on serine-free medium are not in the catalog, and the pathway calls come from only 7 organisms.

## Builds on

- Finding: [[findings/essential_metabolome--04b688de|Desulfovibrio vulgaris alone lacks a complete serine biosynthesis pathway]] (Insufficient literature evidence)
- Finding: [[findings/essential_metabolome--b2b186cc|Genomic economy may explain apparent serine auxotrophy in Desulfovibrio vulgaris]] (Candidate novel)
- Finding: [[findings/essential_metabolome--be48dd15|Amino acid prototrophy may be the ancestral state in free-living bacteria]] (Candidate novel)

## Closest published work

- [PMID 15077118](https://pubmed.ncbi.nlm.nih.gov/15077118/) The genome sequence of the anaerobic, sulfate-reducing bacterium Desulfovibrio vulgaris Hildenborough.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 24910088](https://pubmed.ncbi.nlm.nih.gov/24910088/) Less is more: selective advantages can explain the prevalent loss of biosynthetic genes in bacteria.
- [PMID 32576650](https://pubmed.ncbi.nlm.nih.gov/32576650/) GapMind: Automated Annotation of Amino Acid Biosynthesis.

15077118 gives the genome and 29769716 the mutant fitness data. 24910088 proposes an economy explanation for gene loss in general, but none tests serine in this organism.
