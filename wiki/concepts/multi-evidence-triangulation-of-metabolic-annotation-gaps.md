---
type: "Concept"
description: "Whether combining gapfilling, fitness, pangenome conservation, GapMind and sequence homology can assign genes to gapfilled reactions, including dark reactions lacking EC numbers and how confidence tiers are set; stops at experimental validation."
sources: ["summaries/acinetobacter_adp1_explorer__REPORT.md", "summaries/annotation_gap_discovery__REPORT.md", "summaries/pitfalls.md"]
---
# Multi-evidence triangulation of metabolic annotation gaps

It proposes validation but has not done it. [src: annotation_gap_discovery] In [[summaries/annotation_gap_discovery__REPORT]], the five integrated evidence types were gapfilling, fitness, pangenome, GapMind and BLAST. [src: annotation_gap_discovery] Together they assigned candidate genes to 96 (47.8%) of 201 gapfilled enzymatic reaction-organism pairs across 14 Fitness Browser organisms and 18 carbon sources. [src: annotation_gap_discovery] Reactions without EC (Enzyme Commission) numbers ("dark reactions") resolved far less often. [src: annotation_gap_discovery]

## Literature Context

The candidate papers frame gap filling as a central and uncertain step in building genome-scale metabolic models (GEMs). A review of ESKAPE pathogen models describes the reconstruction workflow as running from an automated draft network through manual curation, gap filling and experimental validation. It notes that high-quality GEMs exist for only a fraction of ESKAPE species, and that many are constrained by incomplete annotation or limited experimental validation [PMID 42841777](https://pubmed.ncbi.nlm.nih.gov/42841777/). The same review points to machine learning as a way to expand functional annotation. That bears on the hub's proposal to use enzyme prediction tools for reactions without EC numbers.

Work on sequence-based network completion shows why gapfilled reactions need independent evidence. Four draft networks were supplemented with every Model SEED reaction that had minimal sequence similarity in the genome. The number of reactions that could take part in a gap-filling solution was vast: 3,270 in the case of E. coli. No network could be completed without orphaned enzymes, which suggests that part of the biochemistry behind biomass precursor formation is uncharacterized. Many gap-filling reactions were nonetheless well determined. Networks built this way predicted gene essentiality better than canonically gapfilled ones. Gene essentiality predictions that depended on poorly determined gap-filling reactions were of poor quality [PMID 26041773](https://pubmed.ncbi.nlm.nih.gov/26041773/). A reconciliation of the Zymomonas mobilis ZM4 model (iHN446: 446 genes, 859 reactions, 894 metabolites) is a single-organism example. Its gap-filling combined computational tools with manual refinement, and it was evaluated against experimental data and literature [PMID 32385302](https://pubmed.ncbi.nlm.nih.gov/32385302/).

The corpus is consistent with this literature. The annotation gap discovery report assigned candidate genes to 96 (47.8%) of 201 gapfilled reaction-organism pairs. Homology was the strongest single stream: BLAST alone resolved 70 pairs, and the full pipeline added 13 percentage points. That fits the sequence-similarity-supported completion described in [PMID 26041773](https://pubmed.ncbi.nlm.nih.gov/26041773/). The low resolution of the 50 dark reactions (8 resolved, 16%) is also consistent with that paper's finding that orphaned, uncharacterized enzymes remain after homology-based completion. The corpus does not test the finding that poorly determined gap-filling reactions degrade essentiality predictions. Its confidence tiers, with 44 high-confidence pairs (21.9%) and 105 unresolved (52.2%), could serve as a way to flag such reactions, but this is a hypothesis.

The corpus extends the literature by adding fitness, pangenome conservation and GapMind evidence to homology across 14 organisms. The candidate papers do not describe a comparable multi-evidence scheme, so the report's claim of a first systematic five-evidence integration is neither supported nor contradicted here. These are the report's own claims. As the hub notes, the assignments are proposals and have not been validated experimentally. The ESKAPE review's emphasis on limited experimental validation applies equally to them [PMID 42841777](https://pubmed.ncbi.nlm.nih.gov/42841777/).

## Resolution rate and hypothesis test

The report states that H1 is supported, because 47.8% exceeds the pre-specified 30% threshold. [src: annotation_gap_discovery] Its confidence tiers split the pairs as follows:

- High: 44 pairs (21.9%), combining BLAST homology, fitness evidence and pangenome conservation. [src: annotation_gap_discovery]
- Medium: 19 pairs (9.5%), BLAST homology with partial supporting evidence. [src: annotation_gap_discovery]
- Low: 33 pairs (16.4%), a single evidence stream only. [src: annotation_gap_discovery]
- Unresolved: 105 pairs (52.2%), with no convincing gene candidate. [src: annotation_gap_discovery]

The report notes that the high-confidence share closely matches the 15-25% range expected in its research plan. [src: annotation_gap_discovery] It presents the tiers as a way to prioritize experimental follow-up. [src: annotation_gap_discovery]

## Contribution of each evidence stream

No single stream is sufficient, according to the report's leave-one-out cross-validation. [src: annotation_gap_discovery] These are the pairs resolved by each configuration:

| Configuration | Pairs resolved | Share |
|---|---|---|
| Full pipeline | 96 [src: annotation_gap_discovery] | 47.8% |
| Without NB03 (EC match) | 86 [src: annotation_gap_discovery] | 42.8% |
| Without NB04 (Bakta) | 80 [src: annotation_gap_discovery] | 39.8% |
| Without NB06 (BLAST) | 73 [src: annotation_gap_discovery] | 36.3% |
| BLAST alone | 70 [src: annotation_gap_discovery] | 34.8% |
| NB03 alone | 51 [src: annotation_gap_discovery] | 25.4% |
| NB04 alone | 22 [src: annotation_gap_discovery] | 10.9% |

BLAST was the most impactful single stream, and the full pipeline added 13 percentage points over BLAST alone. [src: annotation_gap_discovery] Removing any one stream kept resolution above 36%, which the report reads as robustness. [src: annotation_gap_discovery]

The streams work as follows:

- EC-based matching linked gapfilled reaction EC numbers to Fitness Browser gene annotations via pangenome gene clusters. It resolved 51 of 201 pairs (25.4%) with 107 gene candidates. [src: annotation_gap_discovery]
- [[entities/bakta]] alternative annotations queried alternative EC numbers and product-name matches for dark reactions. They added 22 newly resolved pairs (10.9%) and 1,459 EC candidate entries. [src: annotation_gap_discovery]
- Pangenome fitness profiling built a 57 EC by 14 organism presence/absence matrix and computed fitness specificity z-scores. [src: annotation_gap_discovery] It found 11 strong co-occurrence cases and four carbon-source-specific fitness defects. [src: annotation_gap_discovery]
- GapMind (see [[entities/gapmind]]) partially corroborated gapfilling across 104 GapMind-gapfill pathway pairings. [src: annotation_gap_discovery] It classified pathways as incomplete for many of the same carbon sources where ModelSEED required gapfilling. [src: annotation_gap_discovery] For its limits, see [[concepts/reliability-and-coverage-limits-of-gapmind-pathway-predictions]].
- BLAST hits meeting high-confidence thresholds (>=30% identity, >=70% coverage, e-value <=1e-10) were concentrated in branched-chain amino acid biosynthesis and polyamine metabolism. [src: annotation_gap_discovery] The top reactions by hit count were rxn02185, rxn03436 and rxn15947, which encode well-characterized enzymes with broad phylogenetic distribution. [src: annotation_gap_discovery]

## Pathway co-resolution

Two sequential branched-chain amino acid steps were each resolved with high confidence in 9 of 14 organisms. These were rxn02185 (2-acetolactate pyruvate-lyase, EC 2.2.1.6) and rxn03436 (acetohydroxy acid isomeroreductase, EC 1.1.1.86). [src: annotation_gap_discovery] The report interprets this co-resolution as validating triangulation: when one pathway gene is found, the adjacent step's gene is typically recoverable. [src: annotation_gap_discovery] This is the report's interpretation, not an independent test.

## Dark reactions

Of 201 gapfilled reactions, 50 (24.9%) had no ModelSEED EC number and were designated dark reactions. [src: annotation_gap_discovery] Only 8 of these 50 (16%) were resolved, against 88 of 151 (58.3%) for reactions with known EC numbers. [src: annotation_gap_discovery] Dark reactions are known only by stoichiometry, so both homology searches and annotation cross-referencing are harder. [src: annotation_gap_discovery] A related platform limit is that the KBase Data Lakehouse has no EC-to-reaction mapping on the `reaction` table. The pitfalls digest suggests bridging via eggNOG KEGG_ko/KEGG_Reaction to KEGG R-numbers, or using GapMind pathways. [src: pitfalls] See also [[entities/modelseed-biochemistry]].

## Context and novelty claims

Price et al. (2022, PLoS Genetics) used mutant fitness data to fill bacterial catabolic pathway gaps, annotating 716 proteins. [src: annotation_gap_discovery] The report extends this by integrating fitness with gapfilling, pangenome conservation and sequence homology rather than relying mainly on fitness. [src: annotation_gap_discovery] Benedict et al. (2014, PLoS Comput Biol) developed likelihood-based gap-filling annotations using sequence homology. [src: annotation_gap_discovery] The report's scoring also weights multiple evidence types but adds fitness and pangenome evidence. [src: annotation_gap_discovery] The report claims this is the first systematic integration of five evidence types across multiple organisms at once. [src: annotation_gap_discovery] It also says the pangenome framework allows evidence transfer across the 14 focal species. [src: annotation_gap_discovery] These are the report's own claims.

A separate report, [[summaries/acinetobacter_adp1_explorer__REPORT]], catalogs 243 missing functions in ADP1. [src: acinetobacter_adp1_explorer] It describes them as genuine gaps in genomic evidence that affect prediction reliability. [src: acinetobacter_adp1_explorer] It proposes assessing gapfill confidence with pangenome conservation, since 87% of growth predictions depend on gapfilling. [src: acinetobacter_adp1_explorer] This is a proposal, not a result. For model-versus-experiment agreement, see [[concepts/concordance-of-genome-scale-metabolic-model-predictions-with-experimental-data]].

## Proposed validation

The report states that the 44 high-confidence assignments are directly testable via targeted gene knockouts, such as CRISPR interference (CRISPRi), on specific carbon sources. [src: annotation_gap_discovery] It names rxn02185 and rxn03436 across 9 organisms as priority targets. [src: annotation_gap_discovery] It also identifies the 50 EC-less reactions as targets for enzyme prediction tools such as DeepEC and CLEAN and for experimental biochemistry. [src: annotation_gap_discovery] It treats those 50 reactions and the 105 unresolved pairs as high-value targets for enzyme characterization. [src: annotation_gap_discovery] The proposals in these claims are not reported as completed.

## Open Directions

- Knock out the genes behind the 44 high-confidence assignments on the relevant carbon sources, starting with rxn02185 and rxn03436. This would show whether the confidence tiers predict true gene function.
- Run DeepEC and CLEAN on the 50 EC-less reactions, then follow up with biochemistry. This targets the dark-reaction gap, where only 16% resolved.
- Apply the pangenome-conservation confidence assessment to ADP1's gapfilled reactions, to test whether it improves prediction reliability.
- Characterize the 105 unresolved pairs experimentally, to find what evidence the current streams miss.
