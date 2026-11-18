---
type: "Research direction"
description: "Do xoxF-carrying genomes with no pyrroloquinoline quinone (PQQ) synthesis genes in either annotation source live alongside PQQ producers, consistent with cofactor sharing?"
hypothesis: "Metagenome-assembled xoxF carriers without PQQ synthesis come from samples that contain PQQ-synthesizing community members more often than matched carriers with PQQ synthesis do, and this is not explained by low assembly completeness."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Catalogs of metagenome-assembled genomes with completeness and sample ids plus annotation tables are listed, but the catalog did not show whether gene-level calls exist for the metagenome-assembled genomes."
databases: ["kbase.ke_pangenome", "kbase.nmdc_mags"]
tables: ["kbase.nmdc_mags.mag_catalog", "kbase.ke_pangenome.bakta_annotations", "kbase.ke_pangenome.eggnog_mapper_annotations", "kbase.ke_pangenome.genome"]
findings: ["lanthanide_methylotrophy_atlas--4129a02d", "lanthanide_methylotrophy_atlas--6465f1d3"]
conflicts: []
papers: ["29997591", "24816778", "41023737"]
builds_on: ["findings/lanthanide_methylotrophy_atlas--4129a02d", "findings/lanthanide_methylotrophy_atlas--6465f1d3"]
projects: ["lanthanide_methylotrophy_atlas"]
topics: ["lanthanide-dependent-methylotrophy"]
---
# Do xoxF carriers without their own PQQ synthesis depend on neighbours for the cofactor?

Do xoxF-carrying genomes with no pyrroloquinoline quinone (PQQ) synthesis genes in either annotation source live alongside PQQ producers, consistent with cofactor sharing?

## Hypothesis

Metagenome-assembled xoxF carriers without PQQ synthesis come from samples that contain PQQ-synthesizing community members more often than matched carriers with PQQ synthesis do, and this is not explained by low assembly completeness.

## Why it matters

It would reveal a cofactor dependency in methylotroph communities. Otherwise these genomes reflect assembly gaps or lost genes, which would change how the xoxF census is read.

## How to test it

Take xoxF carriers with no PQQ evidence from either annotation source and find those that are metagenome-assembled genomes with sample context. Compare the share of PQQ-carrying genomes in the same sample against matched xoxF carriers that do have PQQ synthesis, controlling for completeness and contamination. Then test whether spent medium from a PQQ-producing methylotroph restores lanthanide-dependent growth of an isolate lacking PQQ synthesis.

## What would support or refute it

Support: PQQ-lacking carriers sit in PQQ-producer-rich samples beyond completeness-matched controls, and spent medium restores growth. Refute: the pattern disappears after completeness control, or the isolate grows without help.

## Data

Approach: analysis then experiment. Readiness: needs compute. Catalogs of metagenome-assembled genomes with completeness and sample ids plus annotation tables are listed, but the catalog did not show whether gene-level calls exist for the metagenome-assembled genomes.

## Builds on

- Finding: [[findings/lanthanide_methylotrophy_atlas--4129a02d|xoxF dominance holds under several phylogeny-aware corrections, strongest in the mixed model]] (Insufficient literature evidence)
- Finding: [[findings/lanthanide_methylotrophy_atlas--6465f1d3|Lanthanide-dependent xoxF vastly outnumbers calcium-dependent mxaF across a large genome collection]] (Extends retrieved work)

## Closest published work

- [PMID 29997591](https://pubmed.ncbi.nlm.nih.gov/29997591/) Lanthanide-Dependent Methanol Dehydrogenases of XoxF4 and XoxF5 Clades Are Differentially Distributed Among Methylotrophic Bacteria and They Reveal Different Biochemical Properties.
- [PMID 24816778](https://pubmed.ncbi.nlm.nih.gov/24816778/) PQQ-dependent methanol dehydrogenases: rare-earth elements make a difference.
- [PMID 41023737](https://pubmed.ncbi.nlm.nih.gov/41023737/) Diversity and distribution of the lanthanome in aerobic methane-oxidising bacteria.

PMID 29997591 and PMID 24816778 describe lanthanide-dependent enzymes and their distribution among methylotrophs. None asks whether carriers without cofactor synthesis rely on community supply.
