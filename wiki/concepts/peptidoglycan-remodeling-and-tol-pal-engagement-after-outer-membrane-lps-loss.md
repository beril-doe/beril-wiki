---
type: "Concept"
description: "How peptidoglycan turnover and Tol-Pal components change when lipid A is lost and how the Pal interpretation was revised; stops at Caulobacter data."
sources: ["summaries/caulobacter_fur_lipida_loss__REPORT.md"]
---
# Peptidoglycan remodeling and Tol-Pal engagement after outer-membrane LPS loss

This page covers how peptidoglycan (PG) turnover and Tol-Pal components change when lipid A is lost in Caulobacter crescentus (the Δlpxc state), and how the report revised its reading of Pal. All evidence comes from one organism and one report ([[summaries/caulobacter_fur_lipida_loss__REPORT]]). The expression changes are measured. The mechanism for Pal is an inference from a published paper, not a direct measurement. [src: caulobacter_fur_lipida_loss]

## Peptidoglycan remodeling is mostly shutdown

SdpA at +4.8 log2 in the outer-membrane (OM) proteome led the report to add PG remodeling as a fourth hypothesis (H4), which the first plan did not contain. [src: caulobacter_fur_lipida_loss] The pre-registered gene set had 53 loci and was locked before differential-expression analysis. [src: caulobacter_fur_lipida_loss] It gave 28 genes meeting the H4 threshold (≥3 required): 25 transcript-significant genes in 4599-vs-4584 (false discovery rate, FDR, <0.05) plus 6 OM-proteome |log2|>1 hits, deduplicated to 28 unique loci. [src: caulobacter_fur_lipida_loss] H4 passed strongly. [src: caulobacter_fur_lipida_loss]

Most of these changes are downregulation. Twenty of the 28 hits are down, including FtsI, PbpZ, MurD, multiple endopeptidases and amidases. [src: caulobacter_fur_lipida_loss] The report says its earlier framing of "coordinated bidirectional reorganization" overstated the bidirectionality. Direction is predominantly down (20 DOWN) with specific inductions (5 UP transcript and 3 UP protein). [src: caulobacter_fur_lipida_loss]

### Down

- FtsI, a cell-division penicillin-binding protein. [src: caulobacter_fur_lipida_loss]
- PbpZ at -1.08 transcript, PbpC at -1.15 protein, and D,D-transpeptidase at -1.27 protein. [src: caulobacter_fur_lipida_loss]
- murD and mviN/murJ, the biosynthesis and flippase machinery. [src: caulobacter_fur_lipida_loss]
- Multiple LdpD/E/F M23-family endopeptidases. [src: caulobacter_fur_lipida_loss]
- amiC amidase and ripA hydrolase. [src: caulobacter_fur_lipida_loss]
- Membrane-bound transglycosylase A at -2.47 log2 protein. [src: caulobacter_fur_lipida_loss]

### Specific inductions

SdpA, PleA, PbpX and Pal stand out against this shutdown. [src: caulobacter_fur_lipida_loss] SdpA (CCNA_01252) is a soluble lytic murein transglycosylase, up +4.8 log2 protein. [src: caulobacter_fur_lipida_loss] PleA, PbpX and CCNA_01754 were also among the induced PG activities. [src: caulobacter_fur_lipida_loss] The report reads this as shutdown of normal division and elongation PG turnover, with a specific subset of lytic transglycosylases and Pal-Tol anchoring factors engaged. [src: caulobacter_fur_lipida_loss]

### Gene-set false positives

Two members of the set are likely regex false positives. CCNA_00565 is a γ-glutamyltranspeptidase, a glutathione enzyme matched on "transpeptidase". [src: caulobacter_fur_lipida_loss] CCNA_01833 is a glucosylceramidase, a ceramide enzyme matched because "ceramidase" contains "amidase". [src: caulobacter_fur_lipida_loss] They remain in the union of significant hits. They do not change the H4 verdict, which is well above the threshold, but downstream interpretation should not rest on them. [src: caulobacter_fur_lipida_loss]

## Pal up, and the revised interpretation

Pal (CCNA_00784) is a PG-associated OM lipoprotein of the Tol-Pal envelope-integrity complex. It is also a top late-cohort ChvI gene from NB03. [src: caulobacter_fur_lipida_loss] It rose +2.08 at the transcript level and +2.84 at the protein level. [src: caulobacter_fur_lipida_loss] The report listed this as a post-hoc finding. [src: caulobacter_fur_lipida_loss]

An earlier draft proposed that, with no LPS, the cell upregulates Pal to compensate through direct protein anchoring for lost LPS-mediated Mg²⁺-bridged OM-LPS-Pal stacking. [src: caulobacter_fur_lipida_loss] The report retracted this because it had no cited support. [src: caulobacter_fur_lipida_loss] It was also inconsistent with current Tol-Pal biology. [src: caulobacter_fur_lipida_loss]

The revision follows Tan & Chng 2025 (Nat Commun 16:2293, PMID 40055349, PMID = PubMed identifier). That paper established retrograde phospholipid transport for OM lipid homeostasis as the primary Tol-Pal function, not LPS-Pal structural anchoring. [src: caulobacter_fur_lipida_loss] An adversarial review had flagged the missing citation. [src: caulobacter_fur_lipida_loss] In Δlpxc, loss of outer-leaflet LPS disrupts OM lipid asymmetry. Tol-Pal upregulation, Pal included, is then consistent with increased retrograde phospholipid transport. [src: caulobacter_fur_lipida_loss]

Direct Pal-PG contacts may also contribute. [src: caulobacter_fur_lipida_loss] Yeh et al. 2010 (PMID 20693330) showed that Caulobacter Tol-Pal is essential for OM constriction at cell division, unlike E. coli Tol-Pal. [src: caulobacter_fur_lipida_loss]

### Predicted test

The revised interpretation predicts increased Tol-Pal retrograde phospholipid-transport activity in Δlpxc. [src: caulobacter_fur_lipida_loss] The report proposes pulse-chase lipidomics after exogenous fluorescent phospholipid loading to test this directly. [src: caulobacter_fur_lipida_loss] Tol-Pal essentiality complicates depletion experiments, but they are testable in conditional-depletion strains. [src: caulobacter_fur_lipida_loss]

## Open Directions

- Run the pulse-chase lipidomics with fluorescent phospholipid in rescued cells versus controls. This closes the gap between Pal-up expression data and the transport inference.
- Test Tol-Pal in conditional-depletion strains. This would separate the phospholipid-transport role from the Pal-PG contact role.
- Rerun the H4 test with CCNA_00565 and CCNA_01833 removed. This would confirm that the 28-locus result and its direction summary do not depend on them.
