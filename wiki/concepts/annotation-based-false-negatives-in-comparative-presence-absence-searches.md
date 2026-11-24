---
type: "Concept"
description: "How text-matching (PaperBLAST) and curated-annotation (NCBI) searches differ in false-negative rates for presence/absence claims, and how naming conventions and unannotated paralogs limit them; stops at screening-method validity."
sources: ["summaries/caulobacter_fur_lipida_loss__REPORT.md"]
---
# Annotation-based false negatives in comparative presence/absence searches

NCBI annotation also gave false negatives for genes annotated under non-canonical names. [src: caulobacter_fur_lipida_loss] The evidence comes from one project and one focal organism, so it shows the problem clearly but does not measure its general rate.

## PaperBLAST text matching as a screen

The original comparative analysis (NB06) used PaperBLAST description-text matching. [src: caulobacter_fur_lipida_loss] The adversarial review flagged a ~50% false-negative rate for known Caulobacter essential genes in that analysis. [src: caulobacter_fur_lipida_loss] A later NCBI cross-check (NB06b) put the PaperBLAST false-negative rate at ~80% for Caulobacter lipid A genes. [src: caulobacter_fur_lipida_loss]

NB06b reran the comparative panel against NCBI's protein database through Biopython Entrez. This uses curated genome annotation rather than text matching. [src: caulobacter_fur_lipida_loss] The per-gene counts for C. crescentus follow.

| Gene | PaperBLAST hits | NCBI hits | Report's label |
|---|---|---|---|
| LpxA | 0 | 11 | false negative [src: caulobacter_fur_lipida_loss] |
| LpxC (the deleted gene) | 0 | 15 | false negative [src: caulobacter_fur_lipida_loss] |
| LpxD | 0 | 15 | false negative [src: caulobacter_fur_lipida_loss] |
| LpxB | 1 | 18 | under-count [src: caulobacter_fur_lipida_loss] |
| LpxK | 0 | 18 | false negative [src: caulobacter_fur_lipida_loss] |

PaperBLAST also under-annotates some comparators. Moraxella catarrhalis has only 162 genes total in PaperBLAST, so the report treats its presence/absence rows as advisory only. [src: caulobacter_fur_lipida_loss] The report therefore says NB06 should be read as a screen, and NB06b is the authoritative comparative measurement for the headline claim. [src: caulobacter_fur_lipida_loss]

## Why the biological claims survive

The report argues that the PaperBLAST failures do not threaten the cross-species finding. The headline concerns absence in the comparators, and NCBI confirms those absences. [src: caulobacter_fur_lipida_loss] NB06b reconfirmed sphingolipid-pathway absence in A. baumannii, N. meningitidis and M. catarrhalis. It also reconfirmed that ChvG-ChvI is restricted to alphaproteobacteria. [src: caulobacter_fur_lipida_loss] One marker query, bcerS, failed in C. crescentus, but other markers confirm the sphingolipid-pathway finding. [src: caulobacter_fur_lipida_loss]

## Limits of curated annotation

NCBI annotation has its own false negatives in C. crescentus, for genes annotated under non-canonical names. [src: caulobacter_fur_lipida_loss] MsbA gives NCBI Cc=0, yet it is present as CCNA_00307, annotated as a phospholipid/LPS (lipopolysaccharide) ABC (ATP-binding cassette) transporter. [src: caulobacter_fur_lipida_loss] LptA also gives NCBI Cc=0, yet it is present without the lptA symbol in Caulobacter NA1000. [src: caulobacter_fur_lipida_loss] The report calls these naming-convention false negatives, not true absences. It explains that Caulobacter is annotated mainly with CCNA_* locus tags, not canonical Gram-negative gene symbols. [src: caulobacter_fur_lipida_loss]

These naming problems do not touch the sphingolipid and ChvI findings. The corresponding C. crescentus genes carry canonical symbols, with NCBI counts of 7 for spt, [src: caulobacter_fur_lipida_loss] 5 for ChvG [src: caulobacter_fur_lipida_loss] and 6 for cerR/ChvI. [src: caulobacter_fur_lipida_loss]

A second limit applies to any annotation-based search. It misses unannotated paralogs, even though the NB06b retest confirmed the headline claims. [src: caulobacter_fur_lipida_loss] The report keeps the residual concern that an unannotated spt paralog in a comparator was missed. [src: caulobacter_fur_lipida_loss] For the lipid A context see [[concepts/alternative-routes-to-tolerating-lipid-a-or-lps-loss-across-gram-negatives]].

## Proposed sequence-based test

For more rigorous comparative testing, the report proposes Pfam HMM searches for PF00155 (serine palmitoyltransferase), PF03331 (LpxC) and PF01475 (Fur), using hmmsearch or pyhmmer. [src: caulobacter_fur_lipida_loss] The report says this would address the residual concern about a missed unannotated spt paralog. [src: caulobacter_fur_lipida_loss] The targets are RefSeq proteomes GCF_000196795.1 for A. baumannii ATCC 17978, [src: caulobacter_fur_lipida_loss] GCF_000008805.1 for N. meningitidis MC58 [src: caulobacter_fur_lipida_loss] and GCF_000092265.1 for M. catarrhalis BBH18. [src: caulobacter_fur_lipida_loss] The report estimates 2-4 hours via CTS. [src: caulobacter_fur_lipida_loss]

## Tensions

- PaperBLAST text matching missed the Caulobacter lipid A genes at ~80%. [src: caulobacter_fur_lipida_loss] The report still holds that the cross-species conclusions stand, because they rest on comparator absences that NCBI confirms. [src: caulobacter_fur_lipida_loss]
- NCBI returned hits for LpxA and LpxC where PaperBLAST returned 0. [src: caulobacter_fur_lipida_loss] NCBI also gave zero counts for MsbA and LptA, which are present. [src: caulobacter_fur_lipida_loss]

## Open Directions

- Run the proposed Pfam HMM searches against the three named proteomes. This would test the residual concern that an unannotated spt paralog was missed in a comparator.
- Rerun the NCBI count with locus-tag and product-description synonyms for genes like msbA and lptA. This would test how many other false zeros are naming artifacts.
- Measure PaperBLAST false-negative rates in other organisms, to test whether the ~80% figure is specific to Caulobacter.
