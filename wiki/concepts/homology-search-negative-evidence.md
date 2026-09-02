---
type: "Concept"
description: "Negative homology hits are evidence only after sensitivity is benchmarked."
sources: ["summaries/caulobacter_fur_lipida_loss__REPORT.md"]
---
# Negative homology-search results require sensitivity validation

A negative homology-search result does not by itself demonstrate that a gene or pathway is absent, because search sensitivity can be reduced by naming conventions, annotation quality, database coverage, or method-specific limitations. [src: caulobacter_fur_lipida_loss] Negative evidence becomes more credible when the search is benchmarked against known positives and independently checked with complementary annotations or sequence-based methods. [src: caulobacter_fur_lipida_loss]

The [[summaries/caulobacter_fur_lipida_loss__REPORT]] provides a direct sensitivity failure case: the initial PaperBLAST search returned 0 hits for Caulobacter LpxA versus 11 NCBI hits, 0 for LpxC versus 15, 0 for LpxD versus 15, 1 for LpxB versus 18, and 0 for LpxK versus 18. [src: caulobacter_fur_lipida_loss] Across these tested Caulobacter lipid A genes, the report characterizes the result as an approximately 80% false-negative rate for PaperBLAST. [src: caulobacter_fur_lipida_loss] These results show that a zero-hit PaperBLAST result can reflect search or representation failure rather than biological absence. [src: caulobacter_fur_lipida_loss]

## Benchmark negative results against known positives

The Caulobacter lipid A genes supplied an internal positive-control set because independent NCBI annotation identified genes that PaperBLAST failed to retrieve. [src: caulobacter_fur_lipida_loss] This supports a workflow in which negative searches are first tested for recall on genes known to be present in the focal genome before negative results are interpreted across comparator genomes. [src: caulobacter_fur_lipida_loss] [[entities/kescience-paperblast]] is therefore most informative when its hit behavior is evaluated against an independently annotated reference rather than treated as a complete absence catalog. [src: caulobacter_fur_lipida_loss]

## Independent annotation can strengthen absence claims

Despite the PaperBLAST false negatives, NCBI annotation independently supported the cross-species absence claims for the tested comparison. [src: caulobacter_fur_lipida_loss] NCBI annotation identified *spt* and *cerR* as Caulobacter-unique across *C. crescentus*, *A. baumannii*, *N. meningitidis*, and *M. catarrhalis*, with pattern 1000. [src: caulobacter_fur_lipida_loss] The same analysis identified ChvG and ChvI as pattern 1000, supporting restriction of the ChvG-ChvI circuit to Caulobacter among the tested species. [src: caulobacter_fur_lipida_loss] Thus, the report preserves these absence claims because they were supported by NCBI annotation and literature rather than by the negative PaperBLAST results alone. [src: caulobacter_fur_lipida_loss]

## Database and naming coverage are part of the evidence

The comparison was vulnerable to naming-convention false negatives, and *M. catarrhalis* was under-annotated in PaperBLAST with 162 genes total. [src: caulobacter_fur_lipida_loss] These limitations make database representation and annotation completeness explicit components of the evidential basis for a negative homology result. [src: caulobacter_fur_lipida_loss] This issue connects to [[concepts/annotation-dependent-resistome-inference]], where inferred biological absence or prevalence can depend on how genes are represented and annotated in the underlying resource. [src: caulobacter_fur_lipida_loss]

## Species-specific alternatives require separate testing

The comparison identified species-specific alternative routes to lipid A loss: *A. baumannii* had PBP1A and Ld-transpeptidases, *N. meningitidis* had 9 capsule-biosynthesis PaperBLAST hits, and *A. baumannii* and *N. meningitidis* had late acyltransferase *lpxX/lpxL* hits numbering 8 and 3, respectively. [src: caulobacter_fur_lipida_loss] The report states that Caulobacter lacks these alternatives and instead uses its sphingolipid substitution route, but it treats the Caulobacter absence conclusions as stronger because they were supported by independent NCBI annotation and literature. [src: caulobacter_fur_lipida_loss] A negative search for one route therefore cannot establish absence of the phenotype or pathway function when unrelated replacement mechanisms remain possible. [src: caulobacter_fur_lipida_loss]

## Tensions

PaperBLAST produced strong negative evidence for several Caulobacter lipid A genes, while NCBI annotation produced positive evidence for the same genes, creating a method-level conflict rather than a biological contradiction. [src: caulobacter_fur_lipida_loss] The discrepancy is resolved provisionally by treating PaperBLAST negatives as sensitivity-limited and retaining cross-species absence claims only where independent annotation and literature support them. [src: caulobacter_fur_lipida_loss]

## Open Directions

- Search named RefSeq proteomes with Pfam HMMs and sequence-based homology methods to determine whether unannotated paralogs explain the PaperBLAST negatives for LpxA, LpxC, LpxD, LpxB, and LpxK. [src: caulobacter_fur_lipida_loss]
- Build a sensitivity benchmark from the 11 NCBI LpxA hits, 15 NCBI LpxC hits, 15 NCBI LpxD hits, 18 NCBI LpxB hits, and 18 NCBI LpxK hits, then compare recall across PaperBLAST, NCBI annotation, and Pfam HMM searches. [src: caulobacter_fur_lipida_loss]
- Reanalyze *M. catarrhalis* with a complete, quality-controlled proteome because the PaperBLAST representation contained 162 genes total, and test whether the reported absence claims persist after improved coverage. [src: caulobacter_fur_lipida_loss]
- Compare the Caulobacter sphingolipid substitution route with PBP1A, Ld-transpeptidase, capsule-biosynthesis, and *lpxX/lpxL* alternatives using profile-HMM and synteny searches to ask whether replacement pathways are genuinely absent or merely poorly annotated. [src: caulobacter_fur_lipida_loss]
