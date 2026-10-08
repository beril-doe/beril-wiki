---
type: "Concept"
description: "Why a species-level disease association must be decomposed into carriage prevalence, within-carrier pathway-level function, and strain content, worked through CD-associated gut species whose signals sit at different levels."
sources: ["summaries/ibd_phage_targeting__REPORT.md"]
---
# Decomposing Species-Level Disease Association into Carriage, Within-Carrier Function, and Strain Content

A species can look "disease-associated" for at least three non-equivalent reasons: more people carry it, carriers carry a functionally different version of it, or carriers carry a different strain of it. These levels are measured by different statistics and imply different interventions, and the gut-microbiome analyses in [[summaries/ibd_phage_targeting__REPORT]] separate them explicitly: within-carrier pathway testing finds substantial Crohn's disease (CD) versus non-IBD shifts in [[entities/hungatella-hathewayi]] (33 passing pathways) and [[entities/escherichia-coli]] (20 passing), while four other "Tier-A core" species show almost none [src: ibd_phage_targeting]. Throughout, FDR is the false discovery rate — the expected fraction of false positives among calls declared significant (see [[entities/benjamini-hochberg-fdr]]).

## Level 1 — carriage prevalence

The four other Tier-A core species named in the report — [[entities/mediterraneibacter-gnavus]], [[entities/eggerthella-lenta]], [[entities/flavonifractor-plautii]] and [[entities/enterocloster-bolteae]] — show small within-carrier shifts, at most 4 passing pathways each, and the report attributes their CD signal to carriage prevalence rather than within-carrier metabolic shift; its stated implication is that pathway-level mechanism is not the right resolution for these species, and the alternatives it names that need no raw reads are biosynthetic gene cluster (BGC) level analysis, which the report records as already executed, and Kumbhari strain-frequency analysis, which applies only to the species represented in its `fact_strain_competition` table [src: ibd_phage_targeting]. This is a null result at the pathway level, not an absence of association, and it is the clearest case for keeping the three levels separate (compare [[concepts/null-results-under-limited-statistical-resolution]], [[concepts/pathobiont-biosynthetic-gene-cluster-repertoires]]).

For *E. lenta* specifically, the CD-down pattern the report interprets is a CB-ORF-level pattern — a per-ORF read-mapping measure, not pathway abundance — and the report reads that CD-down direction as consistent with *E. lenta* per-pathway abundance being mostly carriage-prevalence-driven rather than within-carrier abundance-shifted, and as aligning with the canonical *Eggerthella* CD-association mechanism being drug metabolism (cardiac glycoside inactivation, Koppel et al. 2018) rather than BGC-encoded inflammatory mediators [src: ibd_phage_targeting]. This is an interpretation that crosses measurement levels, not an independent measurement of the drug-metabolism route.

## Level 2 — within-carrier functional shift

*H. hathewayi* is the corpus's clearest observed case of this level: 33 passing within-carrier CD-versus-non-IBD pathways, described as a coherent biosynthesis-versus-degradation shift inside carriers rather than a change in who carries the species [src: ibd_phage_targeting].

Top *H. hathewayi* pathway effects with their FDRs [src: ibd_phage_targeting]:

| Direction [src: ibd_phage_targeting] | Top pathway | Effect | FDR |
|---|---|---:|---:|
| CD-up | Pentose phosphate pathway | +1.18 | 1.6e-5 |
| CD-up | Glycolysis IV (plant cytosol) | +0.94 | 1.0e-3 |
| CD-up | Chorismate biosynthesis I | +0.86 | 1.6e-6 |
| CD-up | Purine nucleobases degradation | +0.89 | 2.6e-4 |
| CD-down | Pyrimidine deoxyribonucleosides salvage | −1.51 | 2.4e-7 |
| CD-down | 1,3-Propanediol biosynthesis | −1.27 | 4.3e-6 |

Two further CD-down pathways are reported alongside these: lactose / galactose degradation at −1.18 (FDR 7.0e-5) and O-antigen biosynthesis (GDP-mannose) at −1.07 (FDR 3.4e-4) [src: ibd_phage_targeting].

*E. coli* is the instructive case because its level-2 signal runs against the cohort-level direction: with 20 passing pathways, within-carrier per-pathway abundance is CD-**down**, the opposite of the cohort-level CD-up direction, which the report states as *E. coli* **relative abundance** being CD-up — an abundance measure, not a measurement of how many subjects carry the species [src: ibd_phage_targeting].

Within-carrier CD-down *E. coli* pathways with effects and FDRs [src: ibd_phage_targeting]:

| Direction [src: ibd_phage_targeting] | Pathway | Effect | FDR |
|---|---|---:|---:|
| CD-down | CMP-legionaminate biosynthesis | −0.95 | 3.0e-5 |
| CD-down | L-1,2-propanediol degradation | −0.81 | 2.9e-4 |
| CD-down | Allantoin degradation to glyoxylate | −0.81 | 1.8e-6 |
| CD-down | Phospholipid remodeling (PE) | −0.84 | 7.3e-6 |
| CD-down | Octane oxidation | −0.72 | 2.4e-5 |
| CD-down | L-histidine degradation I | −0.62 | 2.8e-3 |

The report characterises this set — allantoin degradation, propanediol degradation, octane oxidation, histidine degradation, phospholipid remodeling — as alternative-electron-acceptor and niche-specialization pathways, all CD-down within carriers despite the cohort-level CD-up direction [src: ibd_phage_targeting].

Two non-mutually-exclusive readings are offered for that depletion, and both remain hypotheses here: that CD-associated *E. coli* are an AIEC- (adherent-invasive *E. coli*) specialized subset that has invested in iron and adherent-invasion machinery at the cost of generalist metabolic capabilities, and that CD's *E. coli* face metabolic competition from co-abundant [[entities/klebsiella]] or other Enterobacteriaceae, so the per-cell read-mapping share is lower across pathways [src: ibd_phage_targeting]. The first **refines** the expansion argument in iron acquisition and pathobiont expansion by proposing a cost side to iron-acquisition investment; the second is a compositional explanation that would need no strain change at all, and neither is distinguished by the data reported here.

## Level 3 — strain content

The strain level can be empty even when the species level is not. For *F. plautii* in the Kumbhari data, zero genes reach FDR<0.10 for strain adaptation out of 3,245 genes tested, despite confirmed CD association at the species level and at the active-mechanism level via [[entities/bile-acid-7alpha-dehydroxylation]] (7α-dehydroxylation) [src: ibd_phage_targeting].

The report treats this null as biologically meaningful, reading *F. plautii*'s CD association as mediated by **how much** *F. plautii* is present rather than **which** strain is dominant [src: ibd_phage_targeting]. That reading is an inference drawn from an absence of signal, and it inherits whatever power limit the gene set and cohort impose.

The accompanying explanation is explicitly presumptive: the 7α-dehydroxylation activity is said to be presumably encoded by core *bai*-operon genes present in essentially all strains, which would leave no strain-content variation to detect [src: ibd_phage_targeting]. Presence of *bai* genes across the detected strains is not demonstrated in the report.

## Tensions

The two *E. coli* results point opposite ways and the report declines to average them. On one side, cohort-level *E. coli* relative abundance is CD-up, so total pathway flux scales up; on the other, within carriers the per-cell pathway repertoire is CD-down [src: ibd_phage_targeting]. The report states these are **not contradictory** and interprets the within-carrier result as *E. coli* in CD samples showing less metabolic versatility per cell [src: ibd_phage_targeting]. The reconciliation is a reinterpretation of what each statistic measures — population-level abundance versus per-cell repertoire — and both directions must be carried forward together; reporting either alone misstates the species' CD association.

## Open Directions

- For the Tier-A species whose CD signal is carriage-prevalence-dominated, extend the strain-frequency arm that the report scopes to the species present in `fact_strain_competition`, and read it against the BGC-level analysis the report already executed, to establish whether their association has any within-genome correlate at all [src: ibd_phage_targeting].
- Separate the two readings of *E. coli*'s within-carrier CD-down direction by pairing within-carrier pathway abundance with both strain-level AIEC marker calls and co-abundant Enterobacteriaceae load in the same samples; at present specialization and competition for read-mapping share are not distinguished [src: ibd_phage_targeting].
- Convert the *F. plautii* strain null into a positive statement by checking whether *bai*-operon genes are near-fixed across the strains actually detected, which is the specific premise the report assumes rather than measures [src: ibd_phage_targeting].
- Report, for each species, a power estimate for the strain-content test alongside the null, so that "abundance-mediated, not strain-mediated" can be distinguished from "underpowered at this gene count and cohort size" [src: ibd_phage_targeting].
- Ask whether the biosynthesis-versus-degradation shift seen within *H. hathewayi* carriers reproduces in an independent cohort, which would separate reproducible within-carrier reprogramming from cohort-specific structure and would feed patient-stratification arguments in [[concepts/gut-microbiome-ecotypes-as-patient-strata]] [src: ibd_phage_targeting].
