---
type: "Concept"
description: "How candidate Crohn's-disease-associated species are scored and gated (ecotype-specific meta-analysis, engraftment, protective-analog exclusion, biosynthetic gene clusters) into actionable targets, with the strength of evidence per target; stops at phage availability."
sources: ["summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md", "summaries/pitfalls.md"]
---
# Pathobiont target prioritization for IBD phage therapy

The ibd_phage_targeting project scored 71 rigor-controlled Crohn's disease (CD) candidates and found 6 actionable targets. [src: ibd_phage_targeting] A separate rigor repair applied three evidence filters within each ecotype: 0 of 18 E1 candidates passed, and 3 of 15 E3 candidates passed. [src: discoveries] The evidence is weak for E1 and provisional for E3, because E3 rests on one study. [src: ibd_phage_targeting] An independent within-study check agrees that most E1 Tier-A candidates are ecotype markers, not CD drivers. [src: pitfalls] This page stops at phage availability. See also [[summaries/ibd_phage_targeting__REPORT]], [[summaries/discoveries]] and [[summaries/pitfalls]].

## Literature Context

The candidate papers frame phage therapy for IBD as an early-stage approach that depends on good target selection. A review of microbiome-phage interactions in IBD describes using phages to suppress IBD-associated pathobionts as a means of precision gut microbiome editing, and says that phage therapy is still at an early developmental stage [PMID 36191844](https://pubmed.ncbi.nlm.nih.gov/36191844/). The same review says that combinations of phages aimed at disease-contributing pathobiont strain clades may treat IBD with minimal adverse impact on the surrounding bacteria. It names three needs: better strain-level bacterial target identification, solutions to phage delivery, and ways to handle off-target effects and bacterial resistance [PMID 36191844](https://pubmed.ncbi.nlm.nih.gov/36191844/). A more recent review lists precision phage therapy among the interventions for the virome and mycobiome. It also notes that incomplete reference databases and sequencing bias limit work in this area [PMID 41928387](https://pubmed.ncbi.nlm.nih.gov/41928387/). It describes bacterial dysbiosis in IBD as including depletion of short-chain fatty acid producers and enrichment of pathobionts [PMID 41928387](https://pubmed.ncbi.nlm.nih.gov/41928387/).

The most direct precedent is a study of Klebsiella pneumoniae (Kp). In four geographically distinct IBD cohorts (n = 537), it linked a clade of Kp strains to disease exacerbation and severity. Transferring clinical IBD-associated Kp strains into colitis-prone, germ-free and colonized mice enhanced intestinal inflammation. A lytic five-phage combination then suppressed Kp in colitis-prone mice and attenuated inflammation and disease severity. Phage resilience, safety and viability in the lower gut were assessed only as proof of concept, in an artificial human gut and in healthy volunteers [PMID 35931020](https://pubmed.ncbi.nlm.nih.gov/35931020/). This work targeted a strain clade, which was defined by cohort association and then tested in mouse models.

The corpus is consistent with this literature in its emphasis on strain-level and mechanistic evidence before targeting. NB05 combines engraftment, strain-adaptation and biosynthetic gene cluster evidence with cohort association, and it excludes protective analogs. The reviews call for better strain-level target identification [PMID 36191844](https://pubmed.ncbi.nlm.nih.gov/36191844/), and the corpus supplies one concrete scoring scheme that yields 6 actionable targets among 71 candidates. The within-ecotype repair then passed 0 of 18 E1 candidates and 3 of 15 E3 candidates, and E3 rests on one study. This extends the literature by showing how ecotype markers can pass as disease drivers in species-level screens. The candidate papers do not address that problem, so the finding is novel relative to them.

The candidates do not test any of the corpus's actionable species. None of them covers Hungatella hathewayi, Mediterraneibacter gnavus or the other five targets, and the Kp study's cohort and mouse evidence cannot be carried over to them. The corpus's point that the top scorers have the weakest phage availability, and that its Tier-A lists are hypotheses for experimental validation, is therefore not contradicted or supported by these papers. The Kp study shows what validation could look like: phage selection for sensitive and resistant strains, then mouse testing [PMID 35931020](https://pubmed.ncbi.nlm.nih.gov/35931020/).

## Ecotype-specific meta-analysis

NB04e defines ecotype-specific Tier-A with a within-ecotype × within-substudy meta-analysis of the 4 IBD sub-studies that carry both CD and nonIBD: HallAB_2017, LiJ_2014, IjazUZ_2017 and NielsenHB_2014. [src: ibd_phage_targeting] E1 Tier-A has 51 candidates from 2 sub-studies (HallAB_2017 + NielsenHB_2014, 82 CD / 280 nonIBD), all 100 % sign-concordant. [src: ibd_phage_targeting] E3 Tier-A has 40 candidates from the single study HallAB_2017 (22 CD / 31 nonIBD). [src: ibd_phage_targeting] E3 is therefore provisional. It needs a second cMD-IBD study with both CD and nonIBD in E3, and that is blocked until HMP2 raw data are ingested. [src: ibd_phage_targeting] NB05 was allowed to proceed for E3 with that caveat. [src: ibd_phage_targeting] Ecotype stability is discussed in [[concepts/gut-microbiome-ecotype-stability-and-cross-study-reproducibility]], and pooling pitfalls in [[concepts/substudy-nesting-and-feature-leakage-in-pooled-cohort-microbiome-comparisons]].

In E1, Mediterraneibacter gnavus ranks 1 with CLR-Δ +4.85 and FDR (false discovery rate) 2e-12. [src: ibd_phage_targeting] The report reads E1 CD-stool enrichment of the oral-cavity species Streptococcus salivarius, S. thermophilus and S. parasanguinis as consistent with the oral-gut ectopic-colonization literature. [src: ibd_phage_targeting] S. thermophilus appears in anti-inflammatory probiotics, so its species-level signal does not establish pathobiont status. NB05 uses strain-level literature and engraftment evidence to separate the cases. [src: ibd_phage_targeting]

## Rigor repair: a confound-free filter

The rigor repair applied three evidence filters to the E1 and E3 candidates separately. No E1 candidate passed all three (0 of 18). [src: discoveries] All 14 E1 candidates that passed filters (1) and (2) had negative effects under the confound-free contrast. The report calls them ecotype-markers, not CD drivers. [src: discoveries] An independent-design cross-check (within-IBD-substudy CD-vs-nonIBD) likewise found that most NB04 Tier-A E1 candidates had negative within-study effects, and calls them ecotype-markers, not CD-drivers. [src: pitfalls] In E3, 3 of 15 candidates passed all three filters. [src: discoveries] These are the trustworthy Tier-A candidates:

- M. gnavus, with within-substudy CD↑ +5.13 and LinDA E3 +1.64. [src: discoveries]
- Flavonifractor plautii, with within-substudy +1.89 and LinDA +2.91. [src: discoveries]
- Blautia wexlerae, with within-substudy +0.91 and LinDA +2.00. [src: discoveries]

Per-ecotype Tier-A therefore shrinks from 33 candidates across E1 and E3 to 3 candidates, E3 only. [src: discoveries] The pitfalls digest states the same rule for NB04c: a species must pass both within-ecotype differential abundance (possibly leakage-contaminated) and an independent CD-vs-control contrast, which shrank Tier-A from 33 to 3. [src: pitfalls] E1 needs a reformulated analytical approach before NB05, because the current within-ecotype differential abundance is not a usable target list. [src: discoveries] The repair applies to the next three Pillar 2 deliverables, including Tier-A scoring and cocktail drafts for UC Davis patients. [src: discoveries]

Without ecotype stratification, five of the six donor-2708-engraftment pathobionts pass as CD↑ in the within-IBD-substudy confound-free contrast. They need FDR < 0.10 and ≥ 66 % sign concordance. The effects are M. gnavus +5.13 [src: ibd_phage_targeting], E. lenta +2.30 [src: ibd_phage_targeting], E. coli +1.43 [src: ibd_phage_targeting], E. bolteae +1.09 [src: ibd_phage_targeting] and H. hathewayi +0.92. [src: ibd_phage_targeting] K. oxytoca was below the prevalence filter and was not tested. [src: ibd_phage_targeting]

## NB05 scoring

NB05 applies four criteria (A3–A6) to 71 unique rigor-controlled candidates: 51 E1, 40 E3 provisional and 5 cross-ecotype engraftment, after deduplication. [src: ibd_phage_targeting] The report describes the input as the deduplicated union of the E1 meta-viable Tier-A (51), the E3 provisional Tier-A (40) and the 5 engraftment-confirmed cross-ecotype pathobionts, approximately 70–90 unique species. [src: ibd_phage_targeting] The report identifies M. gnavus as the top candidate across all three input categories. [src: ibd_phage_targeting] The total Tier-A score is A3/5 + A4 + A5 + A6, with range 0–4 and an actionable threshold of 2.5. [src: ibd_phage_targeting]

- **A3 (literature and cohort CD association, 0–5)** uses five signals: the confound-free meta-analysis, HMP2 replication, the Kumbhari differential reference, UHGG-indexed IBD associations and curated phage-biology targets. [src: ibd_phage_targeting] Scores are 0 for 13 candidates, 1 for 22, 2 for 25, 3 for 5, 4 for 5 and 5 for 1. [src: ibd_phage_targeting]
- **A4 (protective-analog exclusion, 0/1)** fails a candidate with a negative within-IBD-substudy CD effect or one on the curated protective list. [src: ibd_phage_targeting] The list includes F. prausnitzii, A. muciniphila, R. intestinalis, R. hominis, L. eligens, A. rectalis, C. scindens, C. eutactus, B. adolescentis and B. longum. [src: ibd_phage_targeting] Three candidates fail: Anaerostipes hadrus (−0.32 effect) [src: ibd_phage_targeting], Clostridium scindens (protective list) [src: ibd_phage_targeting] and Roseburia faecis (−2.74 effect). [src: ibd_phage_targeting] Gordonibacter pamelaeae was flagged for this exclusion because its E1 CD enrichment is hard to read as pathobiont activity. [src: ibd_phage_targeting]
- **A5 (engraftment or strain adaptation)** gives 1.0 to the 5 donor-2708-engraftment pathobionts: M. gnavus, E. lenta, E. coli, E. bolteae and H. hathewayi. It gives 0.5 for a Kumbhari strain-competition or IBD-adapted-strain gene signal. [src: ibd_phage_targeting]
- **A6 (BGCs)** scores 1.0 for 14 candidates. BGC means biosynthetic gene cluster. These include M. gnavus (39 BGCs, 26 CD-enriched CB-ORFs), E. coli (93 BGCs), S. salivarius (98 BGCs), S. parasanguinis (51 BGCs, 11 CD-enriched) and H. hathewayi (6 BGCs, 4 CD-enriched). [src: ibd_phage_targeting]

## Actionable targets and their evidence

Six of the 71 scored candidates are actionable. [src: ibd_phage_targeting]

| Rank | Species | Score | Basis |
|---|---|---|---|
| 1 | Hungatella hathewayi | 4.0 | E1 and engraftment; all 5 A3 signals; 6 BGCs, 4 CD-enriched CB-ORFs [src: ibd_phage_targeting] |
| 2 | [[entities/mediterraneibacter-gnavus]] | 3.8 | E1, E3_prov, engraftment; 4/5 A3; 39 BGCs, 26 CD-enriched CB-ORFs (inflammatory glucorhamnan mechanism) [src: ibd_phage_targeting] |
| 3 | Escherichia coli | 3.6 | E1 and engraftment; MIBiG matches to Colibactin, Yersiniabactin and Enterobactin [src: ibd_phage_targeting] |
| 4 | [[entities/eggerthella-lenta]] | 3.3 | E1 and engraftment; 4/5 A3; Kumbhari IBD-adapted-strain gene signal [src: ibd_phage_targeting] |
| 5 | [[entities/flavonifractor-plautii]] | 3.3 | E1 and E3_prov; Kumbhari strain competition; BGC with CD-enriched CB-ORFs [src: ibd_phage_targeting] |
| 6 | Enterocloster bolteae | 2.8 | E1 and engraftment; no BGC catalog hit [src: ibd_phage_targeting] |

The missing BGC hit for E. bolteae is a potential blind spot. [src: ibd_phage_targeting] Tier-B candidates (2.2–2.4, sub-threshold) are Enterocloster asparagiformis, [[entities/streptococcus-salivarius]], E. citroniae, E. clostridioformis, Blautia coccoides, Veillonella atypica, S. parasanguinis, Actinomyces oris and V. parvula. [src: ibd_phage_targeting] They have BGC evidence, pass A4 and have A3 = 1–2 signals, but lack direct engraftment or strain-adaptation evidence. [src: ibd_phage_targeting]

## Annotation axes beyond the score

NB09c §13 and NB10a §14 establish three per-target annotation axes alongside the Tier-A score. [src: discoveries] One is whether CD specialization is iron/AIEC-mediated (AIEC = adherent-invasive Escherichia coli) or of another kind. It informs whether to target a species broadly or only its AIEC subset. [src: discoveries] See [[concepts/iron-acquisition-as-an-aiec-specific-genomic-specialization-in-crohn-s-disease]]. A second axis separates species-abundance mediation from strain-content mediation. Kumbhari showed zero strain-adaptation gene signal. [src: discoveries] The report reads this as species-abundance mediation and predicts that phage targeting would deplete activity without a within-species strain-content escape route. [src: discoveries] That is an interpretation, not a measurement. See [[entities/kumbhari-strain-adaptation-gene-inference-dataset]].

## Tensions

- The top NB05 scorers, H. hathewayi (4.0) and M. gnavus (3.8), have the weakest phage availability. [src: ibd_phage_targeting] H. hathewayi and F. plautii are both Pillar-4 GAP. [src: ibd_phage_targeting]
- The NB05 scores and the per-ecotype repair results are reported separately. The repair passed 3 of 15 E3 candidates and 0 of 18 E1 candidates. [src: discoveries] NB05 scored H. hathewayi 4.0, E. coli 3.6 and E. lenta 3.3 among its actionable targets. [src: ibd_phage_targeting] The claims do not say how the NB05 list maps onto the repair filters, so the two are not compared here. M. gnavus and F. plautii appear in both. [src: discoveries, ibd_phage_targeting]
- Weak cross-cohort replication makes Tier-A candidates, especially E3, hypotheses for experimental validation. UC Davis cocktail drafts inherit this limit. [src: ibd_phage_targeting] See [[concepts/cross-cohort-portability-and-batch-dominance-in-microbiome-and-metabolomic-stratification]].

## Open Directions

- Ingest HMP2 raw data and rerun the E3 meta-analysis with a second study, to test whether the three trustworthy Tier-A species replicate.
- Reformulate E1 differential abundance so it excludes ecotype-markers, then re-score E1 with the confound-free filters.
- Run the three repair filters on the six NB05 actionable targets, to show which of them pass.
- Add per-candidate cross-cohort support columns to NB05 scoring so replication is visible next to each score.
- Search other BGC catalogs for E. bolteae to test whether the missing BGC hit is a real blind spot.
- Check phage availability for the repaired Tier-A list (the page's stopping point), starting with M. gnavus and F. plautii.
