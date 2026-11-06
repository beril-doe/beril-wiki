---
type: "Finding"
description: "Resolution rates ranged from 20% (Bacteroides thetaiotaomicron) to 71% (Klebsiella michiganensis); the links to reference annotation quality, Fitness Browser coverage and phylogenetic distance are the report's interpretations, not controlled tests."
finding_id: "annotation_gap_discovery--12a061bc"
result: "observation"
source: "annotation_gap_discovery"
quantities: [{"value": "20%", "what": "lowest organism resolution rate (Bacteroides thetaiotaomicron)", "unit": "%", "denominator": "", "scope": ""}, {"value": "71%", "what": "highest organism resolution rate (Klebsiella michiganensis)", "unit": "%", "denominator": "", "scope": ""}]
caveat: "12 of 14 organisms are Proteobacteria, and the sole Bacteroidetes had the lowest resolution, so weaker performance in distant clades rests on a single organism."
first_added: "2026-10-23"
source_hash: "3c63fd0fe807325171c748094ed79318ae508fb874d02e4db139674dc478387c"
---
# Resolution rates varied widely across organisms, lowest in the Bacteroidetes

Resolution rates ranged from 20% (Bacteroides thetaiotaomicron) to 71% (Klebsiella michiganensis); the links to reference annotation quality, Fitness Browser coverage and phylogenetic distance are the report's interpretations, not controlled tests. [src: annotation_gap_discovery]

## Key figures

- **20%**: lowest organism resolution rate (Bacteroides thetaiotaomicron) [src: annotation_gap_discovery]
- **71%**: highest organism resolution rate (Klebsiella michiganensis) [src: annotation_gap_discovery]

## Evidence

> Resolution rates ranged from 20% (*Bacteroides thetaiotaomicron*) to 71% (*Klebsiella michiganensis*). Organisms with better-annotated reference genomes and stronger Fitness Browser coverage showed higher resolution rates. *B. thetaiotaomicron* — a Bacteroidetes with more divergent metabolism — had the lowest resolution, consistent with its phylogenetic distance from the proteobacterial majority. [src: annotation_gap_discovery]

From the report [[summaries/annotation_gap_discovery__REPORT]].

## Caveat

12 of 14 organisms are Proteobacteria, and the sole Bacteroidetes had the lowest resolution, so weaker performance in distant clades rests on a single organism. [src: annotation_gap_discovery]

> 7. **Phylogenetic bias**: 12 of 14 organisms are Proteobacteria, limiting generalizability. The sole Bacteroidetes (*B. thetaiotaomicron*) had the lowest resolution rate, suggesting the approach may be less effective for phylogenetically distant clades with divergent metabolism [src: annotation_gap_discovery]

## Other caveats in this report

- Thirty-three pairs (16.4%) had only single-stream, low-confidence support. [src: annotation_gap_discovery]
- The available GapMind output gives pathway step counts rather than individual step identities, limiting reaction-level concordance assessment. [src: annotation_gap_discovery]
- The Key Findings passage describes DIAMOND v2.1.16 blastp searches against 328 reviewed Swiss-Prot bacterial exemplars for 75/84 unique ECs, yielding 154 hits. Its stated search direction conflicts with the NB06 pipeline description. [src: annotation_gap_discovery]
- The NB06 pipeline passage instead says DIAMOND BLAST searched concatenated proteomes using 328 downloaded Swiss-Prot exemplars. The report leaves the search direction inconsistent with its Key Findings passage; both descriptions report 154 hits. [src: annotation_gap_discovery]
- The report labels baseline flux balance analysis across 574 combinations as 42.5% overall accuracy, gives recall as 86.5% (244 of 282) and precision as 42.5% (244 of 574), and reports 330 false positives. The repeated accuracy and precision value should not be silently treated as independently verified metrics. [src: annotation_gap_discovery]
