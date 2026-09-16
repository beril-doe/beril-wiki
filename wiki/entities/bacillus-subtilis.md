---
type: "Organism"
description: "Bacillus subtilis 168, the Gram-positive model bacterium proposed in the corpus as a priority genetic-library addition and used as a prophage validation species."
sources: ["summaries/functional_dark_matter__REPORT.md", "summaries/prophage_ecology__REPORT.md"]
---
*Bacillus subtilis* is a Firmicutes (Bacillota) bacterium. Strain 168 is described as the best-studied Gram-positive model organism and has well-established RB-TnSeq (random barcode transposon sequencing, a pooled mutant-fitness assay) protocols (Koo et al. 2017). Aliases: *B. subtilis*, *B. subtilis* 168. [src: functional_dark_matter]

## Proposed Fitness Browser library addition

[[summaries/functional_dark_matter__REPORT]] ranks *B. subtilis* 168 first among proposed RB-TnSeq library additions. The report's reason is that it would fill the largest phylogenetic gap in [[entities/kescience-fitnessbrowser]] and allow Gram-positive versus Gram-negative comparisons for universal dark gene families (DUF484, DUF971, EamA). The existing Fitness Browser Firmicutes strain, BFirm, produced only 5 top-500 genes. The report argues that a purpose-built library with broader condition screening could greatly expand this. [src: functional_dark_matter]

The report projects that adding *B. subtilis* and *S. coelicolor* would fill the two largest phylogenetic gaps (Firmicutes depth and Actinobacteria absence). Together they would allow cross-phylum testing of the ~100 "universal" dark gene families that currently can only be studied in Proteobacteria. This projection is prospective, not a demonstrated result. It suggests the hypothesis that these families could be tested across phyla once such libraries exist. [src: functional_dark_matter]

The report's own extended covering-set analysis **refines** this prioritization. That analysis added 25 non-Fitness-Browser organisms to the candidate pool. The conservation-weighted covering set then produced a 50-organism set covering 98.7% of OGs across 6 phyla. At N=5 organisms, coverage reached 57.7%, compared with 38.1% for Fitness-Browser-only candidates. *B. subtilis* and [[entities/staphylococcus-aureus]] were not selected because their OGs are subsets of coverage already provided by Pseudomonadota. The report states that both remain valuable for studying genes in their native Gram-positive genomic context. The two analyses use different criteria: phylogenetic-gap filling and OG coverage. Because of this, the covering-set result qualifies the first-place ranking rather than establishing a conflict with it. How to weigh the two criteria when choosing new libraries remains an open question. [src: functional_dark_matter]

In the extended candidate list, *B. subtilis* 168 is one of six Bacillota organisms. The others are *S. aureus* USA300, *S. pneumoniae* TIGR4, *C. difficile* R20291, *E. faecium* and *L. monocytogenes* EGD-e. The list gives [[entities/tnseq]] and [[entities/crispri]] as the available resources and cites Koo et al. 2017, Bae et al. 2004, van Opijnen et al. 2009 and Dembek et al. 2015. [src: functional_dark_matter]

## Prophage validation species

[[summaries/prophage_ecology__REPORT]] used *B. subtilis* as one of 8 well-characterized prophage-carrying validation species. The other species were *E. coli*, *S. enterica*, *S. aureus*, [[entities/pseudomonas-aeruginosa]], [[entities/mycobacterium-tuberculosis]], *V. cholerae* and *S. pyogenes*. [src: prophage_ecology]

## Related

- [[concepts/experimental-prioritization-of-functional-dark-matter]]
- [[concepts/genetic-perturbation-coverage-bias]]
