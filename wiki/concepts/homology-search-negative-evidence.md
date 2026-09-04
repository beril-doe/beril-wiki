---
type: "Concept"
description: "Why gene-absence claims require sensitivity benchmarks and independent, orthogonal evidence."
sources: ["summaries/caulobacter_fur_lipida_loss__REPORT.md"]
---
# Negative homology-search results require sensitivity validation

A negative homology-search result does not by itself demonstrate that a gene or pathway is absent: naming conventions, annotation quality, database coverage, and method-specific limitations can reduce sensitivity. [src: caulobacter_fur_lipida_loss] Claims of absence should therefore be treated as method-dependent until independent evidence supports them. [src: caulobacter_fur_lipida_loss] Negative evidence becomes more credible when searches are benchmarked against known positives and checked with complementary annotations, sequence-based methods, pathway reconstruction, or biological evidence. [src: caulobacter_fur_lipida_loss]

The [[summaries/caulobacter_fur_lipida_loss__REPORT]] provides a direct sensitivity failure case. PaperBLAST returned 0 hits for Caulobacter LpxA versus 11 NCBI hits, 0 for LpxC versus 15, 0 for LpxD versus 15, 1 for LpxB versus 18, and 0 for LpxK versus 18. [src: caulobacter_fur_lipida_loss] The report characterized these results as an approximately 80% false-negative rate for the tested Caulobacter lipid A genes. [src: caulobacter_fur_lipida_loss] Thus, a zero-hit PaperBLAST result can reflect search or representation failure rather than biological absence, and a single-database result should be reported as “not detected by that method” rather than as definitive absence. [src: caulobacter_fur_lipida_loss]

## Benchmark negative results against known positives

The Caulobacter lipid A genes supplied an internal positive-control set because independent NCBI annotation identified genes that PaperBLAST failed to retrieve. [src: caulobacter_fur_lipida_loss] This supports testing recall on genes known to be present in the focal genome before interpreting negative results across comparator genomes. [src: caulobacter_fur_lipida_loss] [[entities/kescience-paperblast]] is therefore most informative when its hit behavior is evaluated against an independently annotated reference rather than treated as a complete absence catalog. [src: caulobacter_fur_lipida_loss]

## Evidence triangulation in the Caulobacter comparison

Despite the PaperBLAST false negatives, NCBI annotation independently supported the cross-species absence claims for the tested comparison. [src: caulobacter_fur_lipida_loss] NCBI annotation found *spt* and *cerR* to be Caulobacter-unique across *C. crescentus*, *A. baumannii*, *N. meningitidis*, and *M. catarrhalis*, with pattern 1000. [src: caulobacter_fur_lipida_loss] ChvG and ChvI also showed pattern 1000, supporting restriction of the ChvG–ChvI regulatory circuit to Caulobacter among the tested species. [src: caulobacter_fur_lipida_loss] The conclusion that comparator species lacked the Caulobacter sphingolipid-substitute pathway and ChvG–ChvI circuit therefore rested on NCBI annotation and literature rather than on the original PaperBLAST screen alone. [src: caulobacter_fur_lipida_loss]

These independent positive detections **refine** absence analysis by showing that pathway-level conclusions require searches for both the queried pathway and plausible replacement routes. [src: caulobacter_fur_lipida_loss] The comparison identified species-specific alternatives to lipid A loss: *A. baumannii* had PBP1A and Ld-transpeptidases, *N. meningitidis* had 9 capsule-biosynthesis PaperBLAST hits, and late acyltransferase *lpxX/lpxL* hits numbered 8 in *A. baumannii* and 3 in *N. meningitidis*. [src: caulobacter_fur_lipida_loss] The report states that Caulobacter lacks these alternatives and instead uses its sphingolipid-substitution route, but treats the Caulobacter absence conclusions as stronger because they were supported by independent NCBI annotation and literature. [src: caulobacter_fur_lipida_loss] A negative search for one route therefore cannot establish absence of the phenotype or pathway function when unrelated replacement mechanisms remain possible. [src: caulobacter_fur_lipida_loss]

## Database, annotation, and method coverage

The comparison was vulnerable to naming-convention false negatives, and *M. catarrhalis* was under-annotated in PaperBLAST with 162 genes total. [src: caulobacter_fur_lipida_loss] This under-annotation further weakened negative results from that comparison and makes database representation and annotation completeness explicit components of the evidential basis for a negative homology result. [src: caulobacter_fur_lipida_loss] This issue connects to [[concepts/environmental-resistome]], where inferred biological absence or prevalence can depend on how genes are represented and annotated in the underlying resource. [src: caulobacter_fur_lipida_loss]

The report identifies the need for a deeper Pfam HMM search against named RefSeq proteomes to detect unannotated paralogs. [src: caulobacter_fur_lipida_loss] This limitation **supports** [[concepts/structural-annotation-gap]] and [[concepts/evidence-triangulation-for-functional-annotation]]: absence claims become stronger when independent annotation systems, sequence-based homology searches, and biological evidence converge. [src: caulobacter_fur_lipida_loss] Pathway absence and gene absence remain distinct claims: the cross-species patterns concerned annotated genes and regulatory components, whereas the functional conclusion concerned availability of alternative routes for lipid A loss. [src: caulobacter_fur_lipida_loss]

A stronger absence claim should combine database annotation with sensitive sequence-profile searches, independent homology searches, inspection of pathway alternatives, and, where feasible, direct functional or biochemical tests. [src: caulobacter_fur_lipida_loss]

## Tensions

PaperBLAST produced strong negative evidence for several Caulobacter lipid A genes, while NCBI annotation produced positive evidence for the same genes, creating a method-level conflict rather than a biological contradiction. [src: caulobacter_fur_lipida_loss] The discrepancy is provisionally handled by treating PaperBLAST negatives as sensitivity-limited and retaining cross-species absence claims only where independent annotation and literature support them. [src: caulobacter_fur_lipida_loss]

## Open Directions

- Search named RefSeq proteomes with Pfam HMMs and other profile-based or sequence-based homology methods to determine whether unannotated paralogs explain or undermine the reported absence of LpxA, LpxC, LpxD, LpxB, LpxK, *spt*, *cerR*, ChvG, and ChvI in comparator species. [src: caulobacter_fur_lipida_loss]
- Build a sensitivity benchmark from the 11 NCBI LpxA hits, 15 NCBI LpxC hits, 15 NCBI LpxD hits, 18 NCBI LpxB hits, and 18 NCBI LpxK hits, then compare recall across PaperBLAST, NCBI annotation, and Pfam HMM searches. [src: caulobacter_fur_lipida_loss]
- Reanalyze the four comparator proteomes, especially *M. catarrhalis*, with consistent gene calling, complete quality-controlled proteomes, and annotation pipelines to test whether the reported absence claims persist after replacing its 162-gene PaperBLAST representation. [src: caulobacter_fur_lipida_loss]
- Compare the Caulobacter sphingolipid-substitution route with PBP1A, Ld-transpeptidase, capsule-biosynthesis, and *lpxX/lpxL* alternatives using profile-HMM, synteny, and genome-resolved pathway searches to ask whether replacement pathways are genuinely absent or merely poorly annotated. [src: caulobacter_fur_lipida_loss]
- Combine genome-resolved pathway reconstruction with targeted lipidomics to test whether annotated absence of comparator lipid A-loss alternatives corresponds to absence of predicted biochemical products. [src: caulobacter_fur_lipida_loss]
- Perform cross-species genetic engineering or complementation to test whether the Caulobacter sphingolipid-substitution route is functionally distinct from the alternative routes identified in *A. baumannii* and *N. meningitidis*. [src: caulobacter_fur_lipida_loss]
