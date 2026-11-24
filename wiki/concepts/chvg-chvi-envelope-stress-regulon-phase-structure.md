---
type: "Concept"
description: "Temporal partitioning of the ChvG-ChvI regulon (early, both-phase, late) in response to Fur/SspB release and lipid A loss, including the SigU attribution test; stops at transcriptional cohorts."
sources: ["summaries/caulobacter_fur_lipida_loss__REPORT.md"]
---
# ChvG-ChvI envelope-stress regulon phase structure

The Caulobacter crescentus ChvG-ChvI envelope-stress regulon splits into three disjoint transcriptional cohorts (early only, both phases, late only) as Fur and SspB are released and then lipid A is lost. The phase structure is supported by a pre-registered size threshold. The attribution of the late cohort to SigU is only partly supported, and the regulator-to-structural theme shift is not statistically significant. All evidence comes from one report on one organism ([[summaries/caulobacter_fur_lipida_loss__REPORT]]). [src: caulobacter_fur_lipida_loss]

## Literature Context

The one candidate paper, a study of the two-component system ChvGI in Caulobacter crescentus, supplies the reference ChvI regulon that the corpus uses [PMID 36480504](https://pubmed.ncbi.nlm.nih.gov/36480504/). Two-component systems (TCS) let bacteria sense and respond to environmental change. The sensor kinase ChvG autophosphorylates on signals that are still unknown, and it phosphorylates the response regulator ChvI to control transcription. The authors determined the ChvI regulon. They report that ChvI shapes cell envelope architecture by controlling outer membrane, peptidoglycan assembly/recycling and inner membrane proteins. They also found that ChvI phosphorylation is activated by vancomycin treatment. Their chv mutants were impaired by osmotic imbalance in synthetic minimal media. Mutants were also impaired by antibiotics that target peptidoglycan transpeptidation during cell elongation. They conclude that ChvGI mainly monitors osmotic imbalance and peptidoglycan damage to maintain envelope homeostasis. The abstract does not give the number of regulon genes or the sample sizes, so those details cannot be checked here [PMID 36480504](https://pubmed.ncbi.nlm.nih.gov/36480504/).

The corpus findings are consistent with this picture. The late cohort of 49 genes, induced only after lipid A loss, includes the LolA-family carrier CCNA_03820, the Pal-like CCNA_00784 and several TBDTs. These are outer-membrane and envelope-integrity functions, which fit a regulon that controls outer membrane and envelope architecture [PMID 36480504](https://pubmed.ncbi.nlm.nih.gov/36480504/). The report's reading of lipid A loss as an envelope insult that engages ChvI also fits a system that responds to envelope damage. That paper tested vancomycin and osmotic challenges, not lipid A loss or Fur/SspB release. Applying the regulon to those conditions therefore extends it to new triggers. It does not replicate the earlier work.

The corpus claims that go beyond this paper are the following. The first is the disjoint partition into 20 unique-to-early, 10 both-phase and 49 late genes. The second is ChvI (CCNA_00237) induction in both contrasts, which the report presents as autoregulation. The candidate abstract does not mention a temporal partition or autoregulation, so these claims are novel relative to it, and they rest on one report in one organism. The regulator-to-structural theme shift is not statistically significant (Fisher p=0.243). The attribution of the late cohort to SigU is only partial, and the candidate paper does not address SigU at all. These points are neither supported nor contradicted by the literature retrieved here, and they remain open to the SigU-induction experiment proposed in the hub.

## Phase structure

The published ChvI regulons of Stein 2021 and Quintero-Yanes 2022 (PMIDs 34124942 and 36480504) served as reference sets for the partition test. [src: caulobacter_fur_lipida_loss] Their union is 488 ChvI-induced genes in the tested universe. [src: caulobacter_fur_lipida_loss] The partition has 20 unique-to-early, 10 both-phase and 49 late genes, or 79 engaged genes. [src: caulobacter_fur_lipida_loss] The cohorts passed the pre-registered threshold of at least 10 genes per cohort, and the report says "strongly". [src: caulobacter_fur_lipida_loss] The report states that the full disjoint partition was not previously characterized. [src: caulobacter_fur_lipida_loss]

Earlier drafts described an "early cohort of 30 genes" that included the 10 both-phase genes. The corrected partition is disjoint, and the phase-structure verdict is unchanged. [src: caulobacter_fur_lipida_loss]

### Unique-to-early cohort

This cohort has 20 genes induced in 4584-vs-4580 but not in 4599-vs-4584. [src: caulobacter_fur_lipida_loss] Members include:
- lasso peptide cyclase CCNA_02794 at +8.6 [src: caulobacter_fur_lipida_loss]
- the ApbE iron-sulfur cluster repair protein at +3.8 [src: caulobacter_fur_lipida_loss]
- *imuB* SOS DNA polymerase at +1.5, which the report says corroborates Leaden 2018's SOS activation under Δ*fur* [src: caulobacter_fur_lipida_loss]

### Both-phase cohort

This cohort has 10 genes induced in both contrasts, which the report interprets as cooperative continuation. [src: caulobacter_fur_lipida_loss] ChvI itself (CCNA_00237) is in this set, with logFC +1.45 in 4584-vs-4580 and continued induction in 4599-vs-4584. The report calls this direct evidence of autoregulation. [src: caulobacter_fur_lipida_loss] An earlier draft wrongly labeled ChvI as early-cohort. [src: caulobacter_fur_lipida_loss] Other members are:
- SIMPL-family CCNA_02378, going from +1.9 to +3.9 [src: caulobacter_fur_lipida_loss]
- amelogenin/CpxP-related CCNA_03997, where CpxP is the *E. coli* envelope-stress chaperone partner of CpxA [src: caulobacter_fur_lipida_loss]

### Late cohort

This cohort has 49 genes induced only after lipid A is lost, in 4599-vs-4584. [src: caulobacter_fur_lipida_loss] Members include:
- LolA-family outer-membrane lipoprotein carrier CCNA_03820 at +2.89 [src: caulobacter_fur_lipida_loss]
- Pal-like CCNA_00784 at +2.08, part of the Tol-Pal envelope-integrity complex [src: caulobacter_fur_lipida_loss]
- a *zot*-like membrane perturber, the *osrP* stress protein and multiple TBDTs [src: caulobacter_fur_lipida_loss]

The report reads LolA induction under both Δ*spt* (sphingolipid loss) and Δ*lpxc* (lipid A loss) as a generic outer-membrane stress response in Caulobacter. [src: caulobacter_fur_lipida_loss]

## Theme shift

Themes move from regulator-rich early (6.7% regulator/TCS in the unique-to-early 20) to envelope-structural late. [src: caulobacter_fur_lipida_loss] TCS here means two-component system. [src: caulobacter_fur_lipida_loss] The late 49 contain 10.2% envelope/OM and 12.2% TBDT genes. [src: caulobacter_fur_lipida_loss] Lipid/membrane and PG/cell wall categories are at 0% in early. [src: caulobacter_fur_lipida_loss] This shift is suggestive only: the Fisher exact test of envelope/transport/regulator enrichment, late versus unique-to-early, gave p=0.243. [src: caulobacter_fur_lipida_loss]

## SigU attribution test

H1 proposed that SigU drives the late cohort. The criterion was at least 50% envelope/transport/regulator plus Fisher p<1e-3. [src: caulobacter_fur_lipida_loss] SigU is CCNA_02977, and it is uncharacterized in [[entities/paperblast]]. [src: caulobacter_fur_lipida_loss] A scout returned zero substantive snippets, and the published literature has no Caulobacter SigU regulon. [src: caulobacter_fur_lipida_loss] The test was therefore reframed from literature overlap to functional coherence of the late cohort. [src: caulobacter_fur_lipida_loss] The coherence check returned 24.5% enrichment, below the 50% relaxed criterion. [src: caulobacter_fur_lipida_loss] Even the relaxed criterion failed (Fisher p=0.243). [src: caulobacter_fur_lipida_loss] The verdict is that the phase-structure half of H1 is supported and SigU-as-driver is partial. [src: caulobacter_fur_lipida_loss] The late cohort remains a candidate target list for SigU validation. [src: caulobacter_fur_lipida_loss] The report says targeted SigU-induction RNA-seq would resolve the attribution, and it proposes ectopic vanillate-inducible SigU expression followed by genome-wide differential expression. [src: caulobacter_fur_lipida_loss]

## Open Directions

- Run SigU-induction RNA-seq with ectopic vanillate-inducible SigU, then genome-wide differential expression. This would resolve whether SigU drives the 49-gene late cohort, which the coherence test could not settle.
- Compare the SigU-induced genes with the late cohort. This would turn the cohort from a candidate list into a tested regulon.
- Test the regulator-to-structural theme shift with finer functional annotation or a larger cohort, since p=0.243 leaves it undiscriminated.
- Test whether the both-phase genes, including *chvI* and CCNA_03997, depend on ChvG-ChvI directly, for example by profiling a ChvI mutant across the same contrasts.
