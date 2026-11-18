---
type: "Research direction"
description: "After correcting for genome size, bioleaching genera as a group do not carry more metal-signature genes than other bacteria, yet one genus, Leptospirillum, scores high individually. Do these specialists differ in which metal families they carry?"
hypothesis: "Bioleaching genera are enriched for a small set of specific metal-handling gene families (for example particular efflux or arsenic and copper resistance families) even though their total metal-gene count is unremarkable."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Annotation, cluster and genome-size tables cover all 27,702 pangenomes; the matched family-level comparison has to be computed."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.eggnog_mapper_annotations", "kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.gtdb_metadata", "kbase.ke_pangenome.gtdb_species_clade", "kbase.ke_pangenome.pangenome"]
findings: ["metal_fitness_atlas--33814a75"]
conflicts: []
papers: ["30389769", "12829273", "29150517", "27712915"]
builds_on: ["findings/metal_fitness_atlas--33814a75"]
projects: ["metal_fitness_atlas"]
topics: ["gene-essentiality-and-perturbation-assay-validity"]
---
# Do bioleaching bacteria carry different metal-resistance families rather than more of them?

After correcting for genome size, bioleaching genera as a group do not carry more metal-signature genes than other bacteria, yet one genus, Leptospirillum, scores high individually. Do these specialists differ in which metal families they carry?

## Hypothesis

Bioleaching genera are enriched for a small set of specific metal-handling gene families (for example particular efflux or arsenic and copper resistance families) even though their total metal-gene count is unremarkable.

## Why it matters

If true, metal tolerance in extreme acidic habitats comes from selected families, and a summed signature score hides it. If false, specialist metal lifestyles need no special gene content and the explanation must lie in regulation or expression.

## How to test it

Using the pangenome gene clusters with their ortholog (KO) annotations across all species, compare each bioleaching genus (Acidithiobacillus, Leptospirillum and other named bioleachers) with background species matched on genome size and phylum. Test family by family for enrichment among the metal-signature KOs, and check whether any enriched family is in the core or accessory genome of the genus.

## What would support or refute it

Support: a few named families are clearly more frequent in bioleachers than in size-matched background, and are core to the genus. Refute: no individual family differs from the matched background, so the lack of a group-level signal holds at family resolution.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Annotation, cluster and genome-size tables cover all 27,702 pangenomes; the matched family-level comparison has to be computed.

## Builds on

- Finding: [[findings/metal_fitness_atlas--33814a75|Bioleaching genera not enriched for metal signature after normalization]] (Candidate novel)

## Closest published work

- [PMID 30389769](https://pubmed.ncbi.nlm.nih.gov/30389769/) Comparative Genomic Analysis Reveals the Distribution, Organization, and Evolution of Metal Resistance Genes in the Genus Acidithiobacillus.
- [PMID 12829273](https://pubmed.ncbi.nlm.nih.gov/12829273/) Efflux-mediated heavy metal resistance in prokaryotes.
- [PMID 29150517](https://pubmed.ncbi.nlm.nih.gov/29150517/) Multi-omics Reveals the Lifestyle of the Acidophilic, Mineral-Oxidizing Model Species Leptospirillum ferriphilumT.
- [PMID 27712915](https://pubmed.ncbi.nlm.nih.gov/27712915/) Comparative genomics unravels metabolic differences at the species and/or strain level and extremely acidic environmental adaptation of ten bacteria belonging to the genus Acidithiobacillus.

PMIDs 30389769 and 12829273 describe metal-resistance genes in Acidithiobacillus and widespread basic defences, and 29150517 covers Leptospirillum, but none compares specialists with a genome-size-matched background family by family.
