---
type: "Research direction"
description: "Over half of the unannotated gene families are pan-bacterial. When such a family has a measured phenotype in one distant lineage, does its ortholog in another lineage show the same kind of condition-specific phenotype (stress, carbon, nitrogen, and so on)?"
hypothesis: "Condition-class conservation of unannotated gene families extends across phyla. Orthologs of the same family in Proteobacteria and in Bacteroides or Methanococcus have specific phenotypes in the same condition class more often than expected from how common each class is."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The ortholog, specific-phenotype, condition-group and gene tables are listed, but the matching and shuffling analysis has to be built."
databases: ["kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.ortholog", "kescience.fitnessbrowser.specificphenotype", "kescience.fitnessbrowser.specog", "kescience.fitnessbrowser.experiment", "kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.organism"]
findings: ["functional_dark_matter--b069dc6a", "functional_dark_matter--1e0e1f03"]
conflicts: []
papers: ["29769716", "22125499"]
builds_on: ["findings/functional_dark_matter--b069dc6a", "findings/functional_dark_matter--1e0e1f03"]
projects: ["functional_dark_matter"]
topics: ["gene-essentiality-and-perturbation-assay-validity"]
---
# Do conserved unannotated genes keep their phenotype type across deeply divergent bacteria?

Over half of the unannotated gene families are pan-bacterial. When such a family has a measured phenotype in one distant lineage, does its ortholog in another lineage show the same kind of condition-specific phenotype (stress, carbon, nitrogen, and so on)?

## Hypothesis

Condition-class conservation of unannotated gene families extends across phyla. Orthologs of the same family in Proteobacteria and in Bacteroides or Methanococcus have specific phenotypes in the same condition class more often than expected from how common each class is.

## Why it matters

If true, a phenotype measured in a convenient Proteobacterium can guide function discovery for conserved dark genes in organisms with no mutant library. If false, phenotype transfer works only among close relatives and the pan-bacterial dark families need testing in each host.

## How to test it

Take unannotated Fitness Browser genes with a strong condition-specific phenotype. Group them into ortholog sets spanning Proteobacteria and at least one non-Proteobacterial organism (Bacteroides thetaiotaomicron, the two Methanococcus strains). Record each gene's dominant condition class from the specific-phenotype and condition-group tables. Compare class agreement between cross-phylum ortholog pairs with agreement after shuffling class labels among genes within each organism. A within-Proteobacteria comparison gives the upper bound.

## What would support or refute it

Support: cross-phylum pairs agree on condition class clearly more often than shuffled pairs, though less than within Proteobacteria. Refute: agreement across phyla is no better than shuffled labels, which would mean phenotype class is not a conserved property of dark families at this depth.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The ortholog, specific-phenotype, condition-group and gene tables are listed, but the matching and shuffling analysis has to be built.

## Builds on

- Finding: [[findings/functional_dark_matter--b069dc6a|Over half of dark-gene ortholog groups are pan-bacterial]] (Insufficient literature evidence)
- Finding: [[findings/functional_dark_matter--1e0e1f03|Many unannotated Fitness Browser genes have measurable phenotypes]] (Insufficient literature evidence)

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 22125499](https://pubmed.ncbi.nlm.nih.gov/22125499/) Evidence-based annotation of gene function in Shewanella oneidensis MR-1 using genome-wide fitness profiling across 121 conditions.

PMIDs 29769716 and 22125499 assign condition-specific phenotypes to poorly annotated genes within single organisms, but neither asks whether the phenotype class is conserved between distant lineages.
