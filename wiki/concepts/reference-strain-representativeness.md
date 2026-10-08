---
type: "Concept"
description: "How the Pseudomonas aeruginosa PA14 reference strain diverges in effector, biofilm and regulatory genotype from the CF isolate population it is used to model, and what that implies for generalizing assay results."
sources: ["summaries/cf_formulation_design__REPORT.md"]
---
# Laboratory Reference Strains May Not Represent the Populations They Are Used to Model

When a reference strain carries a genotype that is rare in the population it stands for, the gap becomes a measurable constraint on what its assays can be taken to show. The clearest case in this corpus is the cystic fibrosis (CF) formulation project, where every inhibition assay was run against *[[entities/pseudomonas-aeruginosa]]* PA14 while type III secretion system typing of the CF isolate population showed PA14's genotype to be a minority variant, so the report concludes that PA14 is a poor model for chronic CF infection [src: cf_formulation_design]. The constraint here is not which genomes exist at all ([[concepts/cultivation-collection-bias-in-ecological-genomics]]) but the divergence between the assay organism and the typed isolate population [src: cf_formulation_design].

## Genotypic divergence between the two common reference strains

PA14 and PAO1 differ qualitatively in their type III secretion system (T3SS, the needle apparatus that injects effector proteins into host cells) effectors (ExoU vs ExoS), in biofilm polysaccharides (Pel-only vs Pel+Psl), and in regulatory state (*ladS* mutation) [src: cf_formulation_design]. These three differences suggest the hypothesis that a result obtained in one background need not transfer to the other — including for a formulation whose mechanism is competitive exclusion ([[concepts/competitive-exclusion-consortium-design]]) — but the corpus reports no test of transfer across the three axes, so the inference remains untested [src: cf_formulation_design].

## What the CF population actually looks like

CF *P. aeruginosa* is overwhelmingly ExoS+, and the PA14 ExoU+ phenotype represents only 5% of CF isolates; ExoU prevalence rises in acute and invasive contexts, at 33% in other clinical isolates and 35% in environmental isolates [src: cf_formulation_design]. The report's reading of this gradient — that ExoU acts as an acute cytotoxic effector rather than a chronic colonization factor — is an interpretation of the prevalence distribution, not a direct measurement of effector function in these isolates [src: cf_formulation_design].

The same typing gives CF *P. aeruginosa* as 94% ExoS+ (PAO1-like) and 92% Pel+Psl+, which **supports** the conclusion that PA14, being the ExoU+ reference strain used for the inhibition assays, is a poor model for chronic CF infection on both the effector and the biofilm axis [src: cf_formulation_design].

The 94% ExoS+ figure comes from 291 CF PA genomes at pangenome scale and is consistent with prior clinical studies; hypervirulent *exoS+/exoU+* co-expressing strains were detected in 1.5% of the PA genomes analyzed and were concentrated in non-CF clinical settings [src: cf_formulation_design].

## Consequence for generalizing the assay results

Because the inhibition assays were run against PA14, they tested the formulation against a minority (<5%) CF PA variant, and inhibition of ExoS+ PAO1 and clinical strains remains to be confirmed: the report states that confirming inhibition against ExoS+ strains is essential and correspondingly elevates Proposed Experiment 4.6 (PAO1 and clinical strain extension) in importance [src: cf_formulation_design]. Its accompanying argument that ExoS dominance in CF lungs is favorable — ExoS mediating slower, apoptotic killing versus ExoU's rapid cytotoxic lysis, potentially providing a wider time window for competitive exclusion — is a proposed mechanism, not a measured one [src: cf_formulation_design].

Stated as a limitation, the exposure is narrow and specific: all inhibition assays used PA14, which is ExoU+ and Pel-only, described in the limitations section as representing <5% of CF PA isolates — a figure in tension with §2.14's 5% ExoU+ among 291 CF genomes — and the inhibition measurements themselves have not been validated against ExoS+/PAO1-type strains, with Proposed Experiment 4.6 named as the direct remedy [src: cf_formulation_design]. The supporting argument that amino acid catabolism is shared across ExoU+ and ExoS+ strains is reported more precisely in §2.14 as GapMind (a tool that scores pathway completeness from genome sequence) score differences of <0.03 on a 1–5 scale with zero differences significant after false discovery rate (FDR) correction — a null result under limited resolution rather than demonstrated equivalence of inhibition ([[concepts/null-results-under-limited-statistical-resolution]]) [src: cf_formulation_design].

## Tensions

The project reports the PA14-like share of CF isolates two ways and the wiki records both as stated rather than reconciling them: T3SS typing of 6,760 PA genomes is summarized as showing CF isolates 94% ExoS+ with PA14 ExoU+, and the synthesis and limitations sections state that the PA14-like variant represents <5% of CF PA, while §2.14's table and prose report 5% ExoU+ among 291 CF genomes [src: cf_formulation_design]. A second, internal overstatement runs alongside it: the synthesis asserts that amino acid catabolism is "identical" across ExoU+ and ExoS+ variants, whereas the underlying comparison is GapMind score differences <0.03 on a 1–5 scale and zero FDR-significant differences — compatible with near-identity but neither exact identity nor validated equivalence of inhibition [src: cf_formulation_design].

## Open Directions

- Repeat the inhibition and carbon utilization assays against PAO1 and 3–5 mucoid clinical PA isolates from the PROTECT collection, whose results are not reported; this is the listed analysis that would close the gap between the ExoU+ assay background and the ExoS+ majority, converting a genotype-frequency argument into measured inhibition [src: cf_formulation_design].
- Characterize the 15 PROTECT PA strain groups for virulence factors (T3SS effectors, exotoxins), biofilm formation capacity, and antibiotic resistance profiles, and correlate these with the 1,358-gene accessory genome that distinguishes the largest from the smallest strain group; these associations remain untested, and would show whether reference-strain divergence tracks accessory gene content rather than single effector loci ([[concepts/pangenome-integration]]) [src: cf_formulation_design].

See [[summaries/cf_formulation_design__REPORT]] for the project this concept draws on, and [[concepts/genetic-perturbation-coverage-bias]] for the related problem of which organisms get assayed at all.
