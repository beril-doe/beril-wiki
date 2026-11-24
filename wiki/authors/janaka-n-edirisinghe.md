# Janaka N. Edirisinghe

ORCID: [0000-0003-2493-234X](https://orcid.org/0000-0003-2493-234X)

## Contributions

The project [[summaries/annotation_gap_discovery__REPORT]] combined gapfilling, fitness, pangenome, GapMind and BLAST evidence to assign genes to metabolic annotation gaps. Candidate genes were assigned to 96 (47.8%) of 201 gapfilled enzymatic reaction-organism pairs across 14 Fitness Browser organisms and 18 carbon sources. [src: annotation_gap_discovery] The report says this exceeds the pre-specified H1 threshold of 30%. [src: annotation_gap_discovery] The evidence is computational, and knockout validation could not test the assignments. [src: annotation_gap_discovery] The confidence tiers were 44 high (21.9%), 19 medium (9.5%) and 33 low (16.4%). A further 105 pairs (52.2%) were unresolved. [src: annotation_gap_discovery] See [[concepts/multi-evidence-triangulation-of-metabolic-annotation-gaps]].

Leave-one-out and single-stream runs showed that BLAST homology contributed most. BLAST alone resolved 70 pairs (34.8%). Removing BLAST left 73 pairs (36.3%) resolved, and the full pipeline added 13 percentage points over BLAST alone. [src: annotation_gap_discovery] Removing any one stream still left resolution above 36%. [src: annotation_gap_discovery] Resolution ranged from 20% in *Bacteroides thetaiotaomicron* (3 of 15 gaps) to 71.4% in *Klebsiella michiganensis* (5 of 7 gaps). [src: annotation_gap_discovery] The report's explanation for the low *B. thetaiotaomicron* rate, phylogenetic distance and divergent metabolism, is an interpretation and was not tested. [src: annotation_gap_discovery]

Rxn02185 and rxn03436 were each resolved with high confidence in 9 of 14 organisms. [src: annotation_gap_discovery] Of the 201 gapfilled reactions, 50 (24.9%) had no ModelSEED EC number. Only 8 of these 50 (16%) were resolved, against 88 of 151 (58.3%) reactions with known EC numbers. [src: annotation_gap_discovery] GapMind pathway predictions partially corroborated gapfilling across 104 pathway pairings. Exact concordance was limited because the available data give step counts, not step identities. [src: annotation_gap_discovery]

The baseline flux balance analysis (FBA) over 574 organism-carbon source combinations gave 42.5% overall accuracy. Recall was 86.5% (244 of 282 growth-positive conditions), and precision was 42.5% with 330 false positives. [src: annotation_gap_discovery] Conditional gapfilling on 38 false-negative cases added 219 reactions (201 enzymatic, 14 transport, 12 exchange). [src: annotation_gap_discovery] See [[concepts/concordance-of-genome-scale-metabolic-model-predictions-with-experimental-data]].

## Projects (1)

- [[summaries/annotation_gap_discovery__REPORT|annotation_gap_discovery]]
