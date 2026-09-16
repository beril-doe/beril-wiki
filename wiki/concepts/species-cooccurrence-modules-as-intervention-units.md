---
type: "Concept"
description: "Whether species co-occurrence modules detected in gut metagenomes can serve as units for microbiome intervention, given that they concentrate phage-target candidates but shift membership between community states."
sources: ["summaries/ibd_phage_targeting__REPORT.md"]
---
A species-level co-occurrence module is the natural candidate unit for a multi-target microbiome intervention: if the species one wants to remove sit together in one correlated block, one cocktail addresses them as an ecological group rather than one by one. The IBD phage-targeting project tested this by building four per-subnet correlation networks via CLR transform (centered log-ratio, a transform applied to compositional abundance vectors before correlation) plus rank-based Pearson correlation (equivalent to Spearman rho), with per-edge BH-FDR (Benjamini-Hochberg false discovery rate control), thresholded at |rho| > 0.3 AND FDR < 0.05, then ran Louvain community detection (`networkx.community.louvain_communities`, edge-weighted by |rho|); Networkx 3.5's built-in Louvain was sufficient and FastSpar / SpiecEasi installation was held back as unnecessary for the question given clear module structure at CLR-Spearman [src: ibd_phage_targeting].

## Module structure across ecotype subnets

The four subnets differ in sample count, and the resulting networks differ in both density and module count [src: ibd_phage_targeting]:
| Subnet | n samples | n nodes | n edges | n modules |
|---|---:|---:|---:|---:|
| E1_all | 2,601 | 318 | 28,730 | 6 |
| E1_CD | 581 | 255 | 15,354 | 4 |
| E3_all | 1,364 | 296 | 30,453 | 3 |
| E3_CD | 605 | 252 | 19,909 | 7 |

The headline test of "modules as intervention units" failed on its own stated metric but passed on inspection: the raw mean-actionable-per-module is 1.38 on E1_all + E3_all, below the >= 2 bar stated in the plan, yet the signal is not uniformly distributed across modules, because in every subnet a single module contains 4-5 of the 6 actionable Tier-A candidates [src: ibd_phage_targeting].

That concentration is what gives the module its role as a candidate unit, and its composition and size vary by subnet [src: ibd_phage_targeting]:
| Subnet | Pathobiont module | Size | Actionable members |
|---|---:|---:|---|
| E1_all | module 1 | 84 | *E. lenta, E. bolteae, F. plautii, H. hathewayi, M. gnavus* |
| E1_CD | module 0 | 75 | (same set) |
| E3_all | module 1 | 76 | *E. lenta, E. bolteae, E. coli, H. hathewayi, M. gnavus* |
| E3_CD | module 1 | 57 | *E. lenta, E. coli, H. hathewayi, M. gnavus* |

This **refines** rather than rescues the mean-based criterion: the remaining modules per subnet are commensal / *Prevotella* / diverse-healthy communities that naturally contain 0 Tier-A hits by construction, so the mean-per-module statistic is diluted by these biologically-irrelevant-to-the-question modules [src: ibd_phage_targeting]. The practical lesson is that a module-level enrichment claim should be evaluated on the module where the targets are expected, not as an average over modules that cannot contain them.

## Membership is not stable across community states

The unit is not transferable between community states unchanged. *F. plautii* is in the main pathobiont module in E1 but in the generalist module in E3, which the report reads as meaning that for E1 patients *F. plautii* plus main-pathobiont co-targeting is ecologically coherent, while for E3 patients *F. plautii* is less linked and may need a separate phage; that cocktail implication is a prospective design inference, not a tested result [src: ibd_phage_targeting]. See [[concepts/gut-microbiome-ecotypes-as-patient-strata]] for the subnet definitions this depends on.

*E. coli* is in the pathobiont module in E3 only, not E1, which the report interprets as consistent with adherent-invasive *E. coli* (AIEC) being more characteristic of severe-Bacteroides-expanded E3 than transitional E1 — an interpretation layered on a single cross-sectional co-occurrence analysis rather than an independently measured strain-level finding [src: ibd_phage_targeting].

## Module anchors and the collateral-damage question

The non-target members of a pathobiont module are worth enumerating because of a risk hypothesis, not a demonstrated effect: co-occurrence and hub membership do not show that a phage cocktail aimed at module pathobionts would perturb their module neighbours, and nothing in this project tested that. Top-degree non-Tier-A hubs in the pathobiont modules differ between subnets: E1_all module 1 is anchored by *Firmicutes bacterium CAG 110*, *Collinsella massiliensis* and *Phascolarctobacterium sp CAG 266*, while E3_all module 1 is anchored by *Butyricicoccus pullicaecorum*, *Anaerostipes caccae* and *Lactococcus lactis* [src: ibd_phage_targeting].

The Crohn's-disease-restricted subnets show the same pattern at smaller scale: E1_CD module 0 (75 nodes) has anchor commensals *Clostridiales bacterium 1_7_47FAA*, *Anaerostipes caccae* (the only genuine butyrate-producer among the module-anchor commensals) and *Bacteroides nordii*, together with the 5 actionable Tier-A pathobionts of that subnet (*H. hathewayi*, *F. plautii*, *E. bolteae*, *E. lenta*, *M. gnavus*); E3_CD module 1 (57 nodes) has anchor commensals *Actinomyces sp.* oral-taxon-181 and *Actinomyces sp.* HMSC035G02 (both oral cavity ectopic colonizers) plus *Lactonifactor longoviformis* (lactate utilizer), with 4 module pathobionts (*E. lenta*, *H. hathewayi*, *E. coli*, *M. gnavus*) [src: ibd_phage_targeting]. The presence of a butyrate producer inside the E1_CD target module is the kind of adjacency that feeds [[concepts/ecological-cost-of-microbiome-target-depletion]].

## Evidence strength

All of the above rests on one project's cross-sectional CLR-Spearman co-occurrence networks over metagenomic abundance profiles; correlation modules are not measured interaction modules, and no perturbation, isolate co-culture or longitudinal series tested whether removing one module member moves the others [src: ibd_phage_targeting]. The reusable claim is therefore stated as a hypothesis: co-occurrence modules concentrate candidate targets strongly enough to be useful design scaffolds, but because membership switches with community state (*F. plautii*, *E. coli*), a module defined in one patient stratum should not be assumed to be the same intervention unit in another [src: ibd_phage_targeting]. Translational use of these units is further constrained by the standards discussed in [[concepts/phage-therapy-evidence-translation]].

## Tensions

The criterion stated in the project's plan (mean >= 2 actionable candidates per module) and the project's post-hoc inspection (one module per subnet holding 4-5 of the 6 actionable Tier-A candidates) point in opposite directions on whether modules qualify as intervention units; the report keeps both rather than choosing, attributing the gap to modules that cannot contain targets by construction [src: ibd_phage_targeting]. The available evidence does not record what threshold, if any, was set for the expected module considered alone, so which reading should govern cannot be settled from this corpus.

## Open Directions

- Rebuild the four subnet networks under alternative edge estimators — FastSpar and SpiecEasi, which the project deliberately did not install, the latter targeting conditional independence rather than marginal correlation — on the same CLR matrices, and report whether the single-pathobiont-module concentration of 4-5 of the 6 Tier-A candidates is stable across estimators; this measures how far the module definition depends on the CLR-Spearman edge definition, without assuming any one estimator removes indirect association [src: ibd_phage_targeting].
- Define the module-enrichment criterion over target-containing modules only, with a permutation null that reassigns Tier-A labels across nodes, so the reported 1.38 mean and the per-subnet concentration can be judged against the same prespecified test rather than one before and one after inspection [src: ibd_phage_targeting].
- Test module stability directly by bootstrapping samples within each subnet and recording how often *F. plautii* and *E. coli* land in the pathobiont module versus the generalist module, which would say whether the E1/E3 membership switch is a community-state effect or a sampling artifact of the differing subnet sizes (n samples = 2,601 for E1_all, 1,364 for E3_all) [src: ibd_phage_targeting].
- Score each pathobiont module for collateral risk by annotating its anchor commensals (e.g. the butyrate producer *Anaerostipes caccae* in E1_CD module 0) for functions that would be lost if those taxa declined, giving a per-subnet risk list to pair with the per-subnet target list [src: ibd_phage_targeting].
- Repeat the module construction in a longitudinal cohort so that module co-membership can be checked against within-patient co-movement over time. This is a stability analysis only: temporal co-movement would strengthen the module-as-unit hypothesis but could not by itself establish that acting on the module produces the intended community change, which needs perturbation data [src: ibd_phage_targeting].
