---
type: "Research direction"
description: "Among lanmodulin-carrying genomes, those lacking an xoxF call may truly lack it or may reflect incomplete annotation. If sequence-level checks confirm xoxF is absent, do these genomes use lanthanides in other enzymes, or for storage or detoxification?"
hypothesis: "Lanmodulin-positive genomes with xoxF confirmed absent carry other lanthanide-linked functions (for example other PQQ alcohol dehydrogenases) or come from lanthanide-rich habitats, so lanmodulin is retained for lanthanide handling independent of methanol oxidation."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The genomic screen is feasible now, but the function test needs growth and metal-uptake work in a lanmodulin-positive, xoxF-free strain."
collections: ["kbase-ke-pangenome", "kbase-uniprot", "kbase-uniref"]
findings: ["lanthanide_methylotrophy_atlas--6543a6a6", "lanthanide_methylotrophy_atlas--d54adcf1"]
conflicts: []
papers: ["30351021", "35814700", "41023737", "34737731"]
builds_on: ["findings/lanthanide_methylotrophy_atlas--6543a6a6", "findings/lanthanide_methylotrophy_atlas--d54adcf1"]
projects: ["lanthanide_methylotrophy_atlas"]
topics: ["lanthanide-dependent-methylotrophy"]
---
# What do lanmodulin-carrying bacteria without a confirmed xoxF use lanthanides for?

Among lanmodulin-carrying genomes, those lacking an xoxF call may truly lack it or may reflect incomplete annotation. If sequence-level checks confirm xoxF is absent, do these genomes use lanthanides in other enzymes, or for storage or detoxification?

## Hypothesis

Lanmodulin-positive genomes with xoxF confirmed absent carry other lanthanide-linked functions (for example other PQQ alcohol dehydrogenases) or come from lanthanide-rich habitats, so lanmodulin is retained for lanthanide handling independent of methanol oxidation.

## Why it matters

It would separate lanthanide handling from methanol oxidation and show a wider role for lanthanides in bacteria than the methylotroph picture suggests. If xoxF turns out to be present, lanmodulin simply tracks it.

## How to test it

Take the lanmodulin-positive genomes in Beijerinckiaceae, Acetobacteraceae and Hyphomicrobiaceae and flag those without an xoxF call from either annotation source. Confirm absence with a sequence-profile search for XoxF clades and an assembly completeness check, and keep only confirmed-absent genomes. Search that group in UniProt Annotations and UniRef Clusters for other PQQ-dependent dehydrogenases and for genes neighbouring lanmodulin, and compare isolation sources. Then, in one confirmed xoxF-free strain, grow with and without lanthanum and delete lanmodulin to see whether growth or metal uptake changes.

## What would support or refute it

Support: confirmed xoxF-free genomes consistently carry another lanthanide-linked enzyme or come from lanthanide-rich sources, and the deletion changes lanthanide-dependent growth or uptake. Refutation: xoxF is found in nearly all of them once better searches are used, or they carry no other partner, so lanmodulin simply tracks xoxF.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The genomic screen is feasible now, but the function test needs growth and metal-uptake work in a lanmodulin-positive, xoxF-free strain.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-uniprot|UniProt Annotations]]
- Collection: [[data/kbase-uniref|UniRef Clusters]]

## Builds on

- Finding: [[findings/lanthanide_methylotrophy_atlas--6543a6a6|Lanmodulin–xoxF co-occurrence falls just short of preregistered threshold]] (Insufficient literature evidence)
- Finding: [[findings/lanthanide_methylotrophy_atlas--d54adcf1|Bakta-validated lanmodulin is confined to alpha-Proteobacterial methylotroph families]] (Insufficient literature evidence)

## Closest published work

- [PMID 30351021](https://pubmed.ncbi.nlm.nih.gov/30351021/) Lanmodulin: A Highly Selective Lanthanide-Binding Protein from a Lanthanide-Utilizing Bacterium.
- [PMID 35814700](https://pubmed.ncbi.nlm.nih.gov/35814700/) A Periplasmic Lanthanide Mediator, Lanmodulin, in Methylobacterium aquaticum Strain 22A.
- [PMID 41023737](https://pubmed.ncbi.nlm.nih.gov/41023737/) Diversity and distribution of the lanthanome in aerobic methane-oxidising bacteria.
- [PMID 34737731](https://pubmed.ncbi.nlm.nih.gov/34737731/) Comprehensive Comparative Genomics and Phenotyping of Methylobacterium Species.

PMID 30351021 and 35814700 characterise lanmodulin in Methylobacterium and tie it to the lanthanide methanol dehydrogenase; PMID 41023737 surveys the lanthanome in methane oxidisers. None asks what lanmodulin does where xoxF is truly missing.
