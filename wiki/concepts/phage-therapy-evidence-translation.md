---
type: Concept
description: Framework for converting phage host-range evidence into individualized
  therapy
sources:
- id: ibd_phage_targeting
  resource: ../summaries/ibd_phage_targeting__REPORT.md
  title: ibd phage targeting
title: Translating Phage Host-Range Evidence into Patient-Specific Therapy
---
# Translating Phage Host-Range Evidence into Patient-Specific Therapy

[ibd_phage_targeting__REPORT](../summaries/ibd_phage_targeting__REPORT.md) develops a translation framework in which phage host-range evidence is combined with patient-specific target presence, ecological state, strain coverage, and non-phage alternatives rather than treated as a sufficient proxy for clinical efficacy. [^ibd_phage_targeting]

## Translation principle

Patient-specific phage therapy requires at least four linked decisions: whether a target is present in the patient, whether a lytic phage can infect the relevant strain, whether the target is mechanistically and ecologically worth removing, and whether the proposed intervention has evidence beyond in-vitro susceptibility. [^ibd_phage_targeting]

The report therefore distinguishes target prioritization from therapeutic tractability: six species reached the actionable Tier-A threshold, but their phage evidence ranged from clinical-trial-stage evidence for Escherichia coli to lytic-literature evidence for Eggerthella lenta and Enterocloster bolteae, temperate-only evidence for Mediterraneibacter gnavus, and coverage gaps for Hungatella hathewayi and Flavonifractor plautii. [^ibd_phage_targeting]

This distinction supports a hybrid-cocktail model in which direct phage targeting is used where lytic host-range evidence exists, monitored or engineered approaches are considered where evidence is limited, and non-phage interventions are retained for targets without a usable phage. [^ibd_phage_targeting]

## Host-range evidence and cocktail coverage

The PhageFoundry evidence layer contained 96 phages, 188 Escherichia coli strains, and 17,672 experimentally tested susceptibility pairs, of which 3,929 were susceptible, corresponding to a 22 % susceptibility rate. [^ibd_phage_targeting]

A greedy minimum-set-cover analysis selected five phages—DIJ07_P2, LF73_P1, AL505_Ev3, 55989_P2, and LF110_P2—that covered 94.7 % of the 188 tested strains. [^ibd_phage_targeting]

An extended eight-phage design reached 98.4 % coverage of the tested Escherichia coli strains. [^ibd_phage_targeting]

Among 94 phages with host-phylogroup information, 65 (69 %) were isolated against B2/D hosts, the phylogroups emphasized as AIEC-relevant in the report. [^ibd_phage_targeting]

Twenty-six strains (14 %) were phage-resistant at ≤5 % susceptibility, showing that even a high-coverage cocktail leaves a measurable resistant fraction in the tested strain panel. [^ibd_phage_targeting]

These coverage values describe the PhageFoundry strain panel rather than the UC Davis patient isolates, because the dataset did not provide patient-isolate matching, explicit AIEC-versus-commensal labels, burst-size measurements, titer data, or in-vivo delivery validation. [^ibd_phage_targeting]

Accordingly, the minimum-set-cover result supports prioritizing a candidate cocktail for laboratory testing, but it does not establish patient-level coverage or in-vivo efficacy. [^ibd_phage_targeting]

## Patient-level targetability

Among 23 UC Davis Crohn's disease patients, Mediterraneibacter gnavus was present in 21 (91 %), Hungatella hathewayi in 19 (83 %), Enterocloster bolteae in 19 (83 %), Flavonifractor plautii in 18 (78 %), Eggerthella lenta in 16 (70 %), and Escherichia coli in 8 (35 %). [^ibd_phage_targeting]

The patient-level target profile therefore cannot be inferred from population-level target prioritization alone, because target prevalence and phage tractability differed across the six actionable species. [^ibd_phage_targeting]

The report assigned direct phage targeting to Escherichia coli, monitored lytic-phage targeting to Eggerthella lenta and Enterocloster bolteae, limited or engineered targeting to Mediterraneibacter gnavus, and non-phage alternatives or external database searches to Hungatella hathewayi and Flavonifractor plautii. [^ibd_phage_targeting]

All 9 E1 patients carried the full five-species E1 pathobiont module, but Hungatella hathewayi and Flavonifractor plautii were phage gaps and Mediterraneibacter gnavus was temperate-only. [^ibd_phage_targeting]

The E1 pattern makes a pure phage cocktail structurally infeasible for those patients and supports a three-strategy hybrid consisting of direct phage targeting where lytic options exist, alternatives such as GAG-degrading enzyme inhibitors or bile-acid co-therapy, and limited or engineered approaches for Mediterraneibacter gnavus. [^ibd_phage_targeting]

Flavonifractor plautii was deprioritized despite its Tier-A score because it combined the highest bile-acid coupling cost with a phage gap. [^ibd_phage_targeting]

## Ecological state and treatment updating

The four-ecotype framework assigned the 23 UC Davis patients to 7 E0, 9 E1, 6 E3, and 1 mixed-ecotype patient, with no UC Davis patient assigned to E2. [^ibd_phage_targeting]

The report recommends retaining a universal Tier-1 trio of Mediterraneibacter gnavus, Hungatella hathewayi, and Eggerthella lenta, dropping Flavonifractor plautii after an E1-to-E3 transition, and considering Escherichia coli targeting in E3 when an AIEC strain diagnostic is positive. [^ibd_phage_targeting]

This state-dependent strategy connects [condition-specific-fitness](condition-specific-fitness.md) to therapy selection by treating ecological state as a variable that can alter target priority, intervention composition, and the expected cost of removing a species. [^ibd_phage_targeting]

Patient 6967 shifted from E1 to E3 across two visits, while Mediterraneibacter gnavus increased from 0.53 to 7.45 reads, a 14.0× expansion. [^ibd_phage_targeting]

In the same patient, Eggerthella lenta increased 3.1×, Flavonifractor plautii 1.9×, Enterocloster bolteae 2.1×, and Hungatella hathewayi 1.3×, whereas Escherichia coli remained absent. [^ibd_phage_targeting]

The visit-level cocktail Jaccard similarity was 0.60, with Hungatella hathewayi, Mediterraneibacter gnavus, and Eggerthella lenta shared between visits and Enterocloster bolteae plus Flavonifractor plautii present only at visit 1. [^ibd_phage_targeting]

These observations support reassessing the target and cocktail profile over time rather than assuming that one baseline cocktail remains appropriate after ecological state changes. [^ibd_phage_targeting]

The proposed workflow recommends ecotype reassessment every 3–6 months and a five-fold change in Mediterraneibacter gnavus abundance as a trigger for full ecotype retesting, but the report explicitly labels the qPCR proxy, trigger, and dosing rule as hypotheses requiring prospective validation. [^ibd_phage_targeting]

## Evidence limits and safety of translation

HMP2 endogenous phageome analysis covered 630 samples and identified Gokushovirus WZ-2015a as CD-down in E1 with cliff δ = −0.358, FDR = 5e-7, n_CD = 231, and n_HC = 125. [^ibd_phage_targeting]

Escherichia coli correlated with Podoviridae at ρ = +0.183 and Myoviridae at ρ = +0.125, while the maximum absolute endogenous-phage correlation was ≤ 0.18. [^ibd_phage_targeting]

These associations are compatible with ecological coupling but do not demonstrate that endogenous phages control target abundance or that adding exogenous phages will reproduce the observed relationship. [^ibd_phage_targeting]

The report also notes that HMP2 viromics had an 80 % family-classification Unknown fraction, leaving substantial uncertainty in phage identity and host assignment. [^ibd_phage_targeting]

The unresolved gaps motivate [phage-therapy-evidence-translation](phage-therapy-evidence-translation.md) as a distinct translational problem rather than collapsing host-range measurement, ecological association, and clinical efficacy into one evidence category. [^ibd_phage_targeting]

The framework should also be interpreted alongside [pangenome-integration](pangenome-integration.md), because susceptibility was measured across strains and the proposed AIEC-relevant selection depends on strain-level diagnostics that were not available in the current patient data. [^ibd_phage_targeting]

It also intersects [environmental-resistome](environmental-resistome.md), because patient-specific treatment requires distinguishing a target's abundance association from evidence that phage-mediated removal will alter disease-relevant ecology. [^ibd_phage_targeting]

Finally, the integration of PhageFoundry, HMP2 viromics, and UC Davis profiles illustrates the cross-dataset provenance and comparability issues captured by [cross-tenant-data-bridging](cross-tenant-data-bridging.md). [^ibd_phage_targeting]

## Open Directions

- Match the five-phage and eight-phage designs against raw UC Davis isolates using adsorption, killing-curve, resistance-frequency, burst-size, and titer assays to determine patient-isolate coverage rather than extrapolating from the 188-strain PhageFoundry panel. [^ibd_phage_targeting]
- Query INPHARED and IMG/VR for Hungatella hathewayi, Flavonifractor plautii, and Mediterraneibacter gnavus, then validate candidate host assignments and lytic activity experimentally to resolve the three gut-anaerobe coverage gaps. [^ibd_phage_targeting]
- Add AIEC strain diagnostics and pks, Yersiniabactin, Enterobactin, and other strain-level markers to patient-matched susceptibility models to test whether phylogroup and virulence-gene status improve Escherichia coli cocktail selection. [^ibd_phage_targeting]
- Prospectively follow patients every 3–6 months with metagenomics, qPCR, ecotype reassignment, bile-acid measurements, and phage-resistance assays to test whether the proposed reassessment interval and five-fold Mediterraneibacter gnavus trigger predict clinically relevant state transitions. [^ibd_phage_targeting]
- Perform controlled longitudinal phage or hybrid-intervention studies with target abundance, metabolomics, resistance, and clinical outcomes to distinguish phage-mediated causality from the modest endogenous-phage associations observed in HMP2. [^ibd_phage_targeting]
- Compare direct phage targeting, GAG-degrading enzyme inhibitors, bile-acid co-therapy, and engineered-phage approaches in patient-derived communities to determine whether hybrid treatment can address phage gaps without worsening bile-acid coupling costs. [^ibd_phage_targeting]

[^ibd_phage_targeting]: [ibd phage targeting](../summaries/ibd_phage_targeting__REPORT.md)
