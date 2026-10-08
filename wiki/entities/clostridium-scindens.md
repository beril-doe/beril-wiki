---
type: "Organism"
description: "Human gut bacterium whose apparent Crohn's-disease enrichment in IBD metagenome re-analyses moved from a flagged protective-species paradox to a confound-free CD-up call after feature-leakage repair."
sources: ["summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md", "summaries/pitfalls.md"]
---
*Clostridium scindens* is the named gut species at the centre of the apparent Crohn's-disease (CD) enrichment paradox in the IBD metagenome re-analyses [src: ibd_phage_targeting]. The central digest describes it as a protective species: a secondary bile-acid producer via 7α-dehydroxylation, a TGR5 activator, present at ~79 % prevalence in healthy individuals, and an inhibitor of *C. difficile* [src: discoveries]. It is also one of the named organisms in the ecotype feature-leakage analysis [src: pitfalls].

## Aliases

- Aliases: *C. scindens*, *Clostridium scindens* [src: discoveries]

## Bile-acid metabolism

The report cites the `bai` operon of *Clostridium scindens*-like bacteria as the mechanism of bile-acid 7α-dehydroxylation, and treats it as the literature anchor for the NB09c bile-acid network finding [src: ibd_phage_targeting]. See [[entities/bile-acid-7alpha-dehydroxylation]].

## The CD-enrichment call and its re-analysis

The v2 preliminary IBD report (2026-03-28) called *C. scindens* CD-enriched at log₂FC = +2.67 from pooled Mann-Whitney differential abundance (DA — testing whether a taxon's abundance differs between groups), a direct conflict with its documented protective role and ~79 % healthy prevalence; three explanations were considered possible at that stage — compositional artifact, strain heterogeneity, and ecotype mixing in the pooled analysis [src: discoveries, ibd_phage_targeting]. See [[entities/mann-whitney-u-test]].

The preliminary interpretation spelled the three candidate mechanisms out as reasons the call was false: (1) compositional / relative-abundance artifact — Ruminococcaceae loss in severe patients inflates the relative abundance of surviving *C. scindens* strains; (2) strain heterogeneity — not all *C. scindens* strains carry the `bai` operon, so species-level presence ≠ functional presence; (3) ecotype mixing — pooled analysis averages across patient subgroups with different microbiomes [src: discoveries].

At that point compositional-aware DA (ANCOM-BC / MaAsLin2 / [[entities/linda]]) run *within* patient ecotypes was only the **proposed** fix, not a reported validation [src: discoveries]. The preliminary false-call framing is in tension with the later within-substudy result below, which found the species genuinely CD↑; the tension is not resolved by averaging the two, and what the digest later retracts is the H2c claim that stratification resolved the paradox, not this analysis proposal [src: discoveries]. Relevant concepts: [[concepts/compositional-robustness-of-differential-abundance-calls]], [[concepts/gut-microbiome-ecotypes-as-patient-strata]].

Compositional correction alone did **not** remove the signal — a null result for explanation (1): *C. scindens* remained CD-enriched under both methods (raw log₂FC +5.66; CLR Δ +1.25, where CLR is the centred log-ratio transform used to blunt compositional bias), leaving strain heterogeneity and ecotype mixing live at that stage [src: ibd_phage_targeting].

The report's own implication is that pooled Mann-Whitney on relative abundance is systematically under-sensitive for protective-species depletion, an artifact of compositional bias plus pooled-cohort heterogeneity, and that *C. scindens* is not resolvable at that level; resolution required a design that eliminates study confounding, namely the within-IBD-substudy CD-vs-nonIBD meta-analysis [src: ibd_phage_targeting].

## Retraction of the "paradox resolved" claim

Before the repair work, NB04 reported a 33-species within-ecotype Tier-A list (18 E1, 15 E3) with the H2c *C. scindens* paradox marked "RESOLVED by stratification"; two rigor-repair notebooks (NB04b + NB04c) then applied three evidence filters to every candidate [src: discoveries].

H2c is **retracted**. Under the confound-free within-IBD-substudy CD-vs-nonIBD contrast, *C. scindens* is genuinely CD↑ with pooled CLR-Δ = +1.18, FDR = 1e-8 (FDR — false discovery rate, the multiple-testing-adjusted error rate) and 4/4 sign concordance across sub-studies; the NB04 within-ecotype "n.s." call was a feature-leakage artifact of clustering samples on taxon abundances and then testing the same taxa within cluster, and under leave-one-species-out (LOO) refit *C. scindens* is CD↑ in both E1 and E3 once it is not part of the clustering input — this **contradicts** the earlier paradox-resolution claim rather than qualifying it [src: discoveries, ibd_phage_targeting]. See [[concepts/selection-on-outcome-leakage]] and [[concepts/ecotype-clustering-validity]].

The pitfalls digest records the reversal with intervals: *C. scindens* went from NB04 "n.s. within both ecotypes" (the basis for the "paradox RESOLVED" claim) to CD↑ in both E1 (CI +0.68, +0.87) and E3 (CI +1.13, +1.71) under LOO, making the within-ecotype n.s. call a self-selection effect [src: pitfalls].

The same confound-free analysis reversed several other NB04 within-ecotype calls — *F. prausnitzii*, *R. hominis* and *L. eligens* had been called CD↑ within both E1 and E3 and are CD↓ under the confound-free design — so the *C. scindens* reversal is part of a systematic artifact of feature leakage plus the substudy × diagnosis confound, not an isolated species-level correction; critically, both compositional-bias-aware DA methods tried on the within-ecotype subsets (CLR-MW and LinDA) share that bias, so agreement among within-ecotype methods alone does not resolve the direction [src: ibd_phage_targeting].

## Status as an intervention target

Despite being CD↑ under the confound-free design, *C. scindens* was excluded at the A4 screening step on the curated protective list, alongside *Anaerostipes hadrus* (−0.32 confound-free effect) and *Roseburia faecis* (−2.74 effect) [src: ibd_phage_targeting]. This bears on [[concepts/ecological-cost-of-microbiome-target-depletion]].
