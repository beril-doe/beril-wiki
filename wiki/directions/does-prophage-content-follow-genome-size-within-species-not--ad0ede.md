---
type: "Research direction"
description: "Across species, genome size predicts prophage-module composition far better than environment or phylogeny, and no individual terminase lineage tracks an environment. Does prophage load also scale with genome size among strains of one species?"
hypothesis: "Within a species, strains with larger genomes carry more prophage-associated modules, so prophage content mainly follows genome size, and environmental associations reduce to genome-size differences."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Genome size and annotation tables are in the catalog, though prophage detection rests on annotation proxies, not dedicated detectors, and the linking of annotations to genomes was not shown."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.genome", "kbase.ke_pangenome.gtdb_metadata", "kbase.ke_pangenome.eggnog_mapper_annotations"]
findings: ["prophage_ecology--9f2125cc", "prophage_ecology--3c13d0b7", "prophage_ecology--d880eadf"]
conflicts: []
papers: ["25092302", "28692019", "39549700"]
builds_on: ["findings/prophage_ecology--9f2125cc", "findings/prophage_ecology--3c13d0b7", "findings/prophage_ecology--d880eadf"]
projects: ["prophage_ecology"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Does prophage content follow genome size within species, not environment?

Across species, genome size predicts prophage-module composition far better than environment or phylogeny, and no individual terminase lineage tracks an environment. Does prophage load also scale with genome size among strains of one species?

## Hypothesis

Within a species, strains with larger genomes carry more prophage-associated modules, so prophage content mainly follows genome size, and environmental associations reduce to genome-size differences.

## Why it matters

If it holds, apparent environment-prophage links need genome size as a core covariate, and prophage burden may reflect a genome's capacity to tolerate extra DNA, not selection by habitat.

## How to test it

For species with many genomes, regress per-genome counts of prophage-associated annotations (from the functional annotation table, as in the original survey) on genome size from genome metadata, with species as a random effect. Then add isolation environment and ask whether it explains variation beyond genome size. Repeat on a gene-poor lineage subset.

## What would support or refute it

Support: a positive within-species size slope that absorbs most environmental effects. Refute: no within-species slope, so the between-species pattern is phylogenetic, or environment effects persisting after size is accounted for.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Genome size and annotation tables are in the catalog, though prophage detection rests on annotation proxies, not dedicated detectors, and the linking of annotations to genomes was not shown.

## Builds on

- Finding: [[findings/prophage_ecology--9f2125cc|Genome size dwarfs environment and phylogeny as predictor of prophage module composition]] (Insufficient literature evidence)
- Finding: [[findings/prophage_ecology--3c13d0b7|No individual TerL lineage shows environment-specific enrichment beyond host phylogeny]] (Insufficient literature evidence)
- Finding: [[findings/prophage_ecology--d880eadf|Prophage-associated gene clusters occur in every surveyed species, with modules varying]] (Insufficient literature evidence)

## Closest published work

- [PMID 25092302](https://pubmed.ncbi.nlm.nih.gov/25092302/) Pervasive domestication of defective prophages by bacteria.
- [PMID 28692019](https://pubmed.ncbi.nlm.nih.gov/28692019/) Bacteriophage evolution differs by host, lifestyle and genome.
- [PMID 39549700](https://pubmed.ncbi.nlm.nih.gov/39549700/) Genome dynamics across the evolutionary transition to endosymbiosis.

PMID 28692019 relates phage evolution to host and genome; PMID 25092302 shows domestication of defective prophages. Neither tests within-species scaling of prophage content with genome size.
