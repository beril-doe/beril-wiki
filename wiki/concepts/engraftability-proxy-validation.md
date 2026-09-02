---
type: "Concept"
description: "Prevalence and activity scores estimate, but do not measure, microbiome engraftment."
sources: ["summaries/cf_formulation_design__REPORT.md"]
---
# Prevalence and Transcriptional Activity Are Proxies Rather Than Measurements of Formulation Engraftment

## Core Claim

The formulation study uses an engraftability score, defined as prevalence × log(activity ratio), to prioritize candidate commensals, but this score is a proxy for post-administration engraftment rather than a direct measurement of whether an administered organism establishes in the cystic-fibrosis airway. [src: cf_formulation_design]

This distinction matters because prevalence and transcriptional activity describe organisms observed in patient samples, whereas formulation engraftment requires measuring the fate of a deliberately administered strain after dosing. [src: cf_formulation_design]

The evidence therefore supports using engraftability as a ranking signal, not as proof that a candidate will establish, persist, or remain active after formulation delivery. [src: cf_formulation_design]

## Evidence From the Formulation Study

Among 134 species detected in patient metagenomes, *Neisseria mucosa* had the highest engraftability score at 1.595, followed by *Rothia dentocariosa* at 0.422 and *Streptococcus salivarius* at 0.172. [src: cf_formulation_design]

The primary two-species formulation, *R. dentocariosa* + *N. mucosa*, had combined engraftability of 0.820, while the proposed three-species formulation, *Micrococcus luteus* + *N. mucosa* + *S. salivarius*, had engraftability of 0.140. [src: cf_formulation_design]

The report recommends the two-species formulation as the primary clinical candidate partly because both species are lung-adapted and the formulation combines 84% mean inhibition with engraftability of 0.820. [src: cf_formulation_design]

The three-species formulation achieved 100% PA14 niche coverage and 75% inhibition, but its candidacy remains contingent on demonstrating *M. luteus* engraftment in vivo. [src: cf_formulation_design]

*M. luteus* had zero detected patient engraftability and zero lung genomes despite its central role in achieving complete PA14 niche coverage. [src: cf_formulation_design]

These results show why a proxy can produce a useful prioritization while still leaving a critical biological question unresolved: a species can be metabolically valuable in the design model without having evidence that it establishes in the target airway environment. [src: cf_formulation_design]

## What the Proxy Captures—and Misses

Prevalence captures how often a species is detected across sampled patients, and the activity ratio captures its transcriptional activity relative to the comparison context, but neither quantity measures recovery of an administered strain after treatment. [src: cf_formulation_design]

The score can therefore reflect ecological compatibility or prior persistence in the sampled population, but it cannot by itself distinguish successful engraftment from transient passage, repeated exposure, unequal sampling, resident strains, or activity caused by a short-lived response. [src: cf_formulation_design]

The study inferred engraftability from patient prevalence and transcriptional activity rather than measuring it after administration. [src: cf_formulation_design]

Only 21 lung genomes across 5 species were available for lung-adaptation comparisons, limiting direct genomic evidence for airway adaptation of the candidate set. [src: cf_formulation_design]

The available evidence consequently supports a hypothesis that higher prevalence and activity may improve the probability of engraftment, rather than an established relationship between the score and post-administration establishment. [src: cf_formulation_design]

## Implications for Formulation Selection

The proxy is most defensible as one component of a multi-criteria decision that also includes inhibition, niche coverage, pathway conservation, safety filtering, and direct testing in airway-relevant conditions. [src: cf_formulation_design]

This interpretation connects the formulation study to [[concepts/condition-specific-fitness]], because a candidate's performance depends on the airway substrate environment and assay condition rather than on prevalence alone. [src: cf_formulation_design]

It also motivates [[concepts/multi-omics-integration]], since metagenomic detection and metatranscriptomic activity should be combined with longitudinal strain-resolved measurements rather than treated as equivalent to engraftment. [src: cf_formulation_design]

The gap is especially important for [[entities/micrococcus-luteus]], whose predicted contribution to niche coverage was strong but whose patient and lung-genome evidence for establishment was absent. [src: cf_formulation_design]

The planktonic design further limits translation to airway establishment because the inhibition assays used PA14 in planktonic conditions, whereas PA in cystic-fibrosis lungs primarily occupies structured biofilms. [src: cf_formulation_design]

## Tensions

The formulation ranking favors *N. mucosa* and *R. dentocariosa* because their prevalence-activity proxies are relatively high, while the complete-coverage design favors inclusion of *M. luteus* despite zero detected patient engraftability and zero lung genomes. [src: cf_formulation_design]

This is not a statistical contradiction between measurements, but a decision tension between predicted metabolic coverage and evidence of airway establishment. [src: cf_formulation_design]

The tension should not be resolved by treating the composite formulation score as an engraftment measurement, because the study's bootstrap intervals addressed composite-score uncertainty rather than post-administration colonization. [src: cf_formulation_design]

## Open Directions

- Administer barcoded or otherwise strain-resolvable versions of the candidate organisms in an airway-relevant model, then use longitudinal quantitative metagenomics to test whether the prevalence × log(activity ratio) score predicts recovery, persistence, and dose-normalized abundance. [src: cf_formulation_design]
- Measure candidate abundance and transcription before administration and at multiple post-administration time points in cystic-fibrosis airway samples to distinguish transient detection from sustained engraftment. [src: cf_formulation_design]
- Test the two-species and three-species formulations in structured biofilm or airway-mimetic systems against PAO1 and 3–5 mucoid clinical PA isolates to determine whether proxy-ranked candidates establish while retaining inhibition. [src: cf_formulation_design]
- Generate additional lung genomes and strain-resolved metagenomes for *N. mucosa*, *R. dentocariosa*, *S. salivarius*, *G. sanguinis*, and *M. luteus* to test whether genomic lung adaptation improves prediction beyond prevalence and transcriptional activity. [src: cf_formulation_design]
- Compare proxy scores with measured engraftment using mixed-effects or survival models that incorporate dose, sampling time, patient, formulation, and airway environment, thereby testing whether the score predicts establishment independently of these factors. [src: cf_formulation_design]
