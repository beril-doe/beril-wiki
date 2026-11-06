---
type: "Research direction"
description: "Bakta-validated lanmodulin occurred in 62 genomes, all in Beijerinckiaceae, Acetobacteraceae or Hyphomicrobiaceae, but xoxF co-occurred in only 49/62 (79.0%), short of the preregistered 80% threshold (one-sided p = 0.65; H3b not formally supported). Is lanmodulin in xoxF-negative genomes a functional lanthanide-handling system or a non-functional remnant?"
hypothesis: "Lanmodulin in xoxF-negative genomes is functional and serves lanthanide uptake or storage independent of methanol oxidation, so deleting it will reduce lanthanide accumulation or lanthanide tolerance even without XoxF. The alternative is that it is a non-functional remnant, in which case deletion has no phenotype. The result is bounded by bakta annotation, which the report used exclusively for lanmodulin because eggNOG calls were judged false positives."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Annotations and genomes are present, but the decisive deletion and lanthanide-accumulation assays need new strains and measurements."
collections: ["kbase-ke-pangenome", "kbase-genomes", "kbase-uniprot"]
findings: ["lanthanide_methylotrophy_atlas--6543a6a6", "lanthanide_methylotrophy_atlas--d54adcf1"]
conflicts: []
papers: ["30351021", "35814700", "37259003", "34737731", "41023737"]
builds_on: ["findings/lanthanide_methylotrophy_atlas--6543a6a6", "findings/lanthanide_methylotrophy_atlas--d54adcf1"]
projects: ["lanthanide_methylotrophy_atlas"]
topics: ["lanthanide-dependent-methylotrophy"]
---
# What does lanmodulin do in methylotrophs that lack xoxF?

Bakta-validated lanmodulin occurred in 62 genomes, all in Beijerinckiaceae, Acetobacteraceae or Hyphomicrobiaceae, but xoxF co-occurred in only 49/62 (79.0%), short of the preregistered 80% threshold (one-sided p = 0.65; H3b not formally supported). Is lanmodulin in xoxF-negative genomes a functional lanthanide-handling system or a non-functional remnant?

## Hypothesis

Lanmodulin in xoxF-negative genomes is functional and serves lanthanide uptake or storage independent of methanol oxidation, so deleting it will reduce lanthanide accumulation or lanthanide tolerance even without XoxF. The alternative is that it is a non-functional remnant, in which case deletion has no phenotype. The result is bounded by bakta annotation, which the report used exclusively for lanmodulin because eggNOG calls were judged false positives.

## Why it matters

It would show whether lanmodulin is an accessory of XoxF-dependent methylotrophy or a standalone lanthanide-handling system, which bears on its biological role beyond the methanol dehydrogenase.

## How to test it

Step 1 (lakehouse): list the lanmodulin genomes without an xoxF call and re-check them against both annotation sources (xoxF calls were 418 shared, 3,272 eggNOG-only, 1,402 bakta-only), so that annotation discordance is excluded. Inspect lanmodulin gene neighbourhoods for TonB-dependent receptors and metal transporters. Step 2 (experiment): in a xoxF-negative lanmodulin-bearing strain, compare wild type with a lanmodulin deletion for (a) cell-associated lanthanide by ICP-MS (inductively coupled plasma mass spectrometry), (b) growth tolerance at high lanthanide concentration, and (c) lanthanide retention in periplasmic versus cytoplasmic fractions.

## What would support or refute it

Support: deletion changes lanthanide accumulation or tolerance in a xoxF-negative strain; uptake versus storage separated by fractionation. Refutation: no phenotype in any assay, or the xoxF-negative genomes are accounted for by annotation discordance.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Annotations and genomes are present, but the decisive deletion and lanthanide-accumulation assays need new strains and measurements.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-genomes|KBase Genomes]]
- Collection: [[data/kbase-uniprot|UniProt Annotations]]

## Builds on

- Finding: [[findings/lanthanide_methylotrophy_atlas--6543a6a6|Lanmodulin–xoxF co-occurrence falls just short of preregistered threshold]] (Insufficient literature evidence)
- Finding: [[findings/lanthanide_methylotrophy_atlas--d54adcf1|Bakta-validated lanmodulin is confined to alpha-Proteobacterial methylotroph families]] (Insufficient literature evidence)

## Closest published work

- [PMID 30351021](https://pubmed.ncbi.nlm.nih.gov/30351021/) Lanmodulin: A Highly Selective Lanthanide-Binding Protein from a Lanthanide-Utilizing Bacterium.
- [PMID 35814700](https://pubmed.ncbi.nlm.nih.gov/35814700/) A Periplasmic Lanthanide Mediator, Lanmodulin, in Methylobacterium aquaticum Strain 22A.
- [PMID 37259003](https://pubmed.ncbi.nlm.nih.gov/37259003/) Enhanced rare-earth separation with a metal-sensitive lanmodulin dimer.
- [PMID 34737731](https://pubmed.ncbi.nlm.nih.gov/34737731/) Comprehensive Comparative Genomics and Phenotyping of Methylobacterium Species.
- [PMID 41023737](https://pubmed.ncbi.nlm.nih.gov/41023737/) Diversity and distribution of the lanthanome in aerobic methane-oxidising bacteria.

PMIDs 30351021 and 35814700 characterize lanmodulin in Methylobacterium and PMID 34737731 compares Methylobacterium genomes, but none tests lanmodulin function in genomes that lack xoxF.
