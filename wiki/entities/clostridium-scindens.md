---
type: "Organism"
description: "Bile-acid 7α-dehydroxylating gut bacterium whose Crohn's disease enrichment was falsely called in pooled analysis."
sources: ["summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md", "summaries/pitfalls.md"]
aliases: ["C. scindens"]
---
# Clostridium scindens

Clostridium scindens (C. scindens) is a bile-acid 7α-dehydroxylating gut bacterium whose Crohn's disease (CD) enrichment was falsely called in pooled analysis. [src: discoveries] A later within-substudy analysis in ibd_phage_targeting still finds it CD-increased, but for a different reason than the first call. [src: discoveries] Both rest on one project, as reported in [[summaries/ibd_phage_targeting__REPORT]] and [[summaries/discoveries]].

## Key facts

- The report describes C. scindens as a well-documented protective species. It makes secondary bile acids by 7α-dehydroxylation, activates TGR5, occurs at ~79 % prevalence in healthy individuals and inhibits C. difficile. [src: discoveries]
- Not all strains carry the bai operon, so species-level presence does not establish functional presence. [src: discoveries]

## The preliminary pooled call

The preliminary pooled Mann-Whitney differential-abundance analysis called C. scindens CD-enriched at log₂FC +2.67. This contradicted its established protective role. [src: ibd_phage_targeting, discoveries]

The report proposes three likely mechanisms for the false call:
- Ruminococcaceae loss in severe patients may inflate the relative abundance of surviving C. scindens strains. [src: discoveries]
- Strain heterogeneity may play a part. [src: discoveries]
- Pooling across patient subgroups with different microbiomes (ecotype mixing) may play a part. [src: discoveries]

The proposed fix is compositional-aware differential abundance (ANCOM-BC, MaAsLin2 or LinDA) run within patient ecotypes. [src: discoveries]

In NB00, compositional correction alone did not remove the signal. C. scindens stayed CD-enriched at raw log₂FC +5.66 and CLR (centered log-ratio) Δ +1.25. The report says explanations (2) and (3) remain live. [src: ibd_phage_targeting]

## Confound-free reanalysis

Within-substudy CD-versus-nonIBD analysis found C. scindens genuinely CD-increased. Pooled CLR-Δ was +1.18, FDR (false discovery rate) 1e-8, with 4/4 sign concordance across sub-studies. [src: discoveries, ibd_phage_targeting] This directly contradicted the H2c "paradox resolution" hypothesis. [src: discoveries]

The report reads this as expected behaviour for a species more prevalent in the IBD-cohort source studies than in the healthy-cohort source studies in cMD. [src: ibd_phage_targeting] That is the report's interpretation. See [[concepts/substudy-nesting-and-feature-leakage-in-pooled-cohort-microbiome-comparisons]].

## Leakage artifact in the ecotype analysis

NB04 had called C. scindens nonsignificant within both ecotypes. That call was the basis for the "paradox resolved" claim. [src: pitfalls] Leave-one-species-out refitting in NB04b excluded the test species from the ecotype definition. C. scindens then came out CD-increased in both E1 and E3. [src: discoveries] The confidence intervals were E1 (CI +0.68, +0.87) [src: pitfalls] and E3 (CI +1.13, +1.71). [src: pitfalls] The report attributes the earlier nonsignificant call to a self-selection (leakage) effect. [src: pitfalls]

## Related pages

- [[concepts/bile-acid-7-dehydroxylation-deficit-and-the-ecological-cost-of-targeting-bile-acid-transforming-species]]
- [[concepts/gut-microbiome-ecotype-stability-and-cross-study-reproducibility]]
- [[summaries/pitfalls]]
