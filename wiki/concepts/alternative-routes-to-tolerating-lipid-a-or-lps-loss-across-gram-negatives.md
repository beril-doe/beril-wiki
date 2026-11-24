---
type: "Concept"
description: "Which species-specific substitution routes (sphingolipid, peptidoglycan remodeling, capsule, acylation truncation) permit survival without LPS, and what that predicts for resistance; stops at presence/absence evidence and predictions."
sources: ["summaries/caulobacter_fur_lipida_loss__REPORT.md"]
---
# Alternative routes to tolerating lipid A or LPS loss across Gram-negatives

This page covers which species-specific substitution routes permit survival without lipid A or lipopolysaccharide (LPS), and what they predict for resistance. The comparison covers Caulobacter crescentus, Acinetobacter baumannii, Neisseria meningitidis and Moraxella catarrhalis. [src: caulobacter_fur_lipida_loss] The evidence is genome presence/absence from [[entities/paperblast]] text matching and NCBI annotation, plus published literature. It is not functional testing in the comparator species, and the resistance predictions are model-based. See [[entities/caulobacter-crescentus]] and the [[summaries/caulobacter_fur_lipida_loss__REPORT|report summary]].

## Caulobacter: sphingolipid substitution

The sphingolipid pathway is Caulobacter-unique in this panel. PaperBLAST presence/absence found spt (serine palmitoyltransferase), bcerS (bacterial ceramide synthase) and sphingosine kinase absent from the other three species. [src: caulobacter_fur_lipida_loss] The report treats the pathway as confirmed by NCBI annotation, reporting spt: PB(7,0,0,0) + NCBI(7,0,0,0) and cerR: PB(1,1,0,0) + NCBI(6,0,0,0). [src: caulobacter_fur_lipida_loss] NCBI annotation gave spt counts of 7,0,0,0 and cerR counts of 6,0,0,0 across the four species. [src: caulobacter_fur_lipida_loss] The report notes the bcerS query failed in C. crescentus, but other markers confirm the result. [src: caulobacter_fur_lipida_loss] NCBI annotation scored both spt and cerR as Caulobacter-only. [src: caulobacter_fur_lipida_loss] Independent literature (Olea-Ozuna 2020/2024; PMIDs 33063925, 39093898) agrees. [src: caulobacter_fur_lipida_loss] The report concludes that A. baumannii, N. meningitidis and M. catarrhalis do not encode the pathway. [src: caulobacter_fur_lipida_loss] It also notes that none of the three is an alphaproteobacterium or Bacteroidetes. [src: caulobacter_fur_lipida_loss]

The envelope-stress circuit ChvG-ChvI shows the same pattern. NCBI counts were ChvG 5,0,0,0 and ChvI 6,0,0,0, and both proteins were scored Caulobacter-only. [src: caulobacter_fur_lipida_loss] Its absence in the three comparators is supported by NCBI annotation, PaperBLAST text matching and literature. [src: caulobacter_fur_lipida_loss] This is consistent with the published alphaproteobacterial restriction (Greenwich et al. 2023, PMID 37040790). [src: caulobacter_fur_lipida_loss] The report argues the other three species cannot use the Caulobacter Δfur plus anionic-sphingolipid rescue, because they lack the substitute lipid machinery. [src: caulobacter_fur_lipida_loss] It asserts that Caulobacter has none of the alternative routes below, so sphingolipid substitution is its only viable path. [src: caulobacter_fur_lipida_loss]

## Routes in the other species

The report says the published alternative routes align with what the genomes encode for A. baumannii and N. meningitidis. [src: caulobacter_fur_lipida_loss] This is presence/absence evidence only. For M. catarrhalis the table below gives only the published route.

| Species | Route | Genomic support |
|---|---|---|
| A. baumannii | Peptidoglycan remodeling: Δlpxc via PBP1A loss plus LdtJ/LdtK (Kang 2021, PMID 33402533) [src: caulobacter_fur_lipida_loss] | PBP1A and Ld-transpeptidases present [src: caulobacter_fur_lipida_loss] |
| N. meningitidis | Capsule substitution for ΔlpxA (Steeghs 2001, PMID 11742971) [src: caulobacter_fur_lipida_loss] | Large capsule locus, 9 PaperBLAST hits versus 2-3 in the others [src: caulobacter_fur_lipida_loss] |
| M. catarrhalis | Late-acyltransferase truncation (Gao 2008, PMID 18795947) [src: caulobacter_fur_lipida_loss] | No genomic support is given in the claims here |
| A. baumannii and N. meningitidis | Acylation truncation via lpxX/lpxL | 8 and 3 hits respectively [src: caulobacter_fur_lipida_loss]; absent (0) in C. crescentus [src: caulobacter_fur_lipida_loss] |

The report calls the Caulobacter Δlpxc response (SdpA/PleA and Pal-Tol peptidoglycan remodeling) mechanistically distinct from the A. baumannii route but biologically analogous. Both organisms reorganize peptidoglycan when LPS or LOS is removed, using different enzyme families. [src: caulobacter_fur_lipida_loss]

## Predictions for resistance

The report's structural-unavailability model predicts that adding the Caulobacter sphingolipid pathway to A. baumannii should be neutral or modestly protective under colistin selection. [src: caulobacter_fur_lipida_loss] The A. baumannii PBP1A/Ldt route works independently of sphingolipids. [src: caulobacter_fur_lipida_loss] A sphingolipid-engineered A. baumannii should therefore have two alternative routes to colistin resistance, and the report predicts more colistin-resistant escapers. [src: caulobacter_fur_lipida_loss] These are predictions, not measurements.

## Proposed sequence-based check

The report proposes a sequence-based comparative search against named RefSeq proteomes, including GCF_000196795.1 for A. baumannii ATCC 17978. [src: caulobacter_fur_lipida_loss]

## Open Directions

- Run Pfam HMM searches against the named RefSeq proteomes, such as GCF_000196795.1 for A. baumannii ATCC 17978. This would replace annotation-based presence/absence with sequence-based calls. See [[concepts/annotation-based-false-negatives-in-comparative-presence-absence-searches]].
- Express the Caulobacter sphingolipid pathway in A. baumannii and measure colistin-resistant escaper rates. This tests the two-route prediction.
- Count lpxX/lpxL homologs in M. catarrhalis. Genomic support for acylation truncation there is not yet shown.
- Test whether the capsule locus count predicts LPS-loss tolerance across more Neisseria strains.
