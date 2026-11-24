---
type: "Concept"
description: "How genes missing from a deletion collection differ from those present in length, annotation and pangenome conservation, and how this biases essentiality and dispensability calls; stops at one species' collection."
sources: ["summaries/adp1_deletion_phenotypes__REPORT.md", "summaries/discoveries.md"]
---
# Coverage gaps in deletion collections and their link to pangenome conservation

In *Acinetobacter baylyi* ADP1, the TnSeq-dispensable genes absent from the deletion collection are shorter, less annotated and less conserved in the pangenome than those present. [src: adp1_deletion_phenotypes, discoveries] This is direct measurement within one species' collection ([[entities/acinetobacter-baylyi-adp1]]). The link to pangenome conservation is an association. The report's explanation for it, evolutionary retention pressure, is a suggestion and not a tested mechanism. [src: adp1_deletion_phenotypes]

## Literature Context

The single candidate paper is a comparative transposon-sequencing study of 13 sequenced high-density transposon mutant libraries from five genera of the Enterobacteriaceae [PMID 39207104](https://pubmed.ncbi.nlm.nih.gov/39207104/). The study is only available here as an abstract. It treats the Keio *E. coli* single-gene deletion library as a gold standard that is often relied on for essential gene sets. It then asks how essentiality varies between related strains and species. The authors assess essentiality prediction approaches and the effect of transposon density. They also identify biases in transposon insertion sequencing data, and they build a new classifier for gene essentiality [PMID 39207104](https://pubmed.ncbi.nlm.nih.gov/39207104/).

Their main findings are these. They define a core essential genome of 201 universally essential genes. They report that approximately a third of the genes essential in any particular strain are non-essential in another related strain. They find no evidence for genus-specific essential genes, and they describe a large cohort of variably essential genes whose essentiality is gained or lost rapidly during evolution. They conclude that essentiality depends on genomic context rather than being immutable [PMID 39207104](https://pubmed.ncbi.nlm.nih.gov/39207104/). The abstract does not examine genes missing from deletion collections, so it says nothing directly about coverage gaps.

The hub's central finding is a direct measurement in one species. In *Acinetobacter baylyi* ADP1, the 272 TnSeq-dispensable genes lacking deletion-collection data are shorter, less annotated and less core than the 2,321 present dispensable genes. The core fraction is 76.5% against 93.3%, with p = 1.4×10⁻²⁰. This is largely novel relative to the candidate paper, because the paper does not address which genes a deletion library fails to capture. The two are compatible in a limited sense. The paper's point that essentiality calls carry method-specific biases, and that deletion libraries are often taken as a benchmark, fits the hub's view that a collection biased toward well-characterized, conserved genes is an imperfect reference [PMID 39207104](https://pubmed.ncbi.nlm.nih.gov/39207104/).

The paper also bears on the hub's interpretation, though more loosely. Rapid turnover of essentiality across related strains is consistent with the hub's suggestion, which is not a tested mechanism, that dispensability and pangenome status are linked through evolutionary retention pressure. It supports the caution that essentiality is strain-dependent. The abstract does not link essentiality to pangenome conservation or to collection coverage. It also covers Enterobacteriaceae, not *Acinetobacter*. The ADP1 association therefore remains a single-species result. It extends, but is not confirmed by, the broader literature, and it is not in tension with it.

## Who is missing

Of 2,593 TnSeq-dispensable genes, 272 (10.5%) lack deletion-collection growth data. The other 2,321 present dispensable genes have data. [src: adp1_deletion_phenotypes, discoveries] The report describes the missing genes as systematically different from the present ones. [src: adp1_deletion_phenotypes, discoveries]

| Property | Present dispensable | Missing dispensable |
|---|---|---|
| Mean length | 981 bp [src: adp1_deletion_phenotypes] | 813 bp [src: adp1_deletion_phenotypes] |
| RAST annotated | 100% [src: adp1_deletion_phenotypes] | 91% [src: adp1_deletion_phenotypes] |
| KO (KEGG ortholog) annotated | 59% [src: adp1_deletion_phenotypes] | 49% [src: adp1_deletion_phenotypes] |
| Pangenome core | 93.3% [src: adp1_deletion_phenotypes] | 76.5% [src: adp1_deletion_phenotypes] |

The core difference has p = 1.4×10⁻²⁰. [src: adp1_deletion_phenotypes, discoveries] The discoveries digest states the same length, annotation and conservation differences. [src: discoveries]

Missing genes are also enriched for hypothetical proteins. There are 25 completely unannotated genes (q = 2.4×10⁻²⁵) and 48 annotated as "hypothetical protein" (q = 3.0×10⁻⁴). [src: adp1_deletion_phenotypes, discoveries]

## Link to pangenome conservation

The report connects condition-dependent essentiality to pangenome dynamics. It proposes that the least conserved genes are also the ones most likely to be missed when a deletion collection is built. [src: adp1_deletion_phenotypes] By cross-referencing KBase Data Lakehouse pangenome data, it finds the 272 missing genes significantly less conserved across *Acinetobacter* species. It suggests that dispensability and pangenome status are linked through evolutionary retention pressure. [src: adp1_deletion_phenotypes] The core/accessory status used in the analysis comes from the species-level *A. baylyi* pangenome, which may have limited resolution. [src: adp1_deletion_phenotypes] The report cites Rosconi et al. (2022) as showing that pangenome variation makes essentiality strain-dependent and evolvable. [src: adp1_deletion_phenotypes] The collection as a whole is described as biased toward well-characterized, conserved genes. [src: discoveries]

## Uncertain-class genes

The 313 uncertain-class genes are more extreme. They have 361 bp mean length, 42% annotated and 31% core. The report reads this as consistent with gene fragments or pseudogenes rather than true essential genes. [src: adp1_deletion_phenotypes] See also [[concepts/fitness-modules-essential-genes-and-condition-specific-gene-function]].

## Caveats

- The complete ADP1 matrix (2,034 genes) excludes essential genes (499) and genes with incomplete data (316). This biases it toward dispensable genes with successful deletion mutants. [src: adp1_deletion_phenotypes]
- Core/accessory status comes from the species-level *A. baylyi* pangenome, which may have limited resolution compared with a population-level analysis. [src: adp1_deletion_phenotypes]

## Open Directions

- Repeat the missing-versus-present comparison in another species with a deletion collection and a Lakehouse pangenome. This would test whether the bias is general or specific to ADP1.
- Redo the core-membership comparison using population-level or multi-genome data for ADP1. This would address the species-level resolution limit.
- Fit a model with length, annotation and conservation as joint predictors of missingness. This would separate the contributions of each.
- Check whether the uncertain-class genes map to fragments or pseudogenes in the genome. This would test the report's interpretation.
