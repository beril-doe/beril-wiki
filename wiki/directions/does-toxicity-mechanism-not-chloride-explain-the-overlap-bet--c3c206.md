---
type: "Research direction"
description: "Why are 39.8% of metal-important gene records also important under NaCl, and does the overlap track metal toxicity mechanism rather than chloride delivery?"
hypothesis: "Overlap reflects envelope and general stress physiology tied to toxicity mechanism, so matched-concentration chloride and sulfate salts of one metal give similar fitness profiles under identical conditions. The chloride-dose prediction was already rejected: ZnSO4 with 0 mM Cl- had 44.6% overlap."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The matched-salt, osmolarity-controlled RB-TnSeq experiment has not been run; available choline chloride experiments differ in concentration."
collections: ["kescience-fitnessbrowser"]
findings: ["counter_ion_effects--5a2d3c21", "counter_ion_effects--482d2003", "counter_ion_effects--619981e8", "counter_ion_effects--5c39821b", "counter_ion_effects--5a523214"]
conflicts: []
papers: ["32986214", "27474723", "34432491", "12829273"]
builds_on: ["findings/counter_ion_effects--5a2d3c21", "findings/counter_ion_effects--482d2003", "findings/counter_ion_effects--619981e8", "findings/counter_ion_effects--5c39821b", "findings/counter_ion_effects--5a523214"]
projects: ["counter_ion_effects"]
topics: ["laboratory-fitness-versus-natural-selection-and-gene-conservation"]
---
# Does toxicity mechanism, not chloride, explain the overlap between metal and NaCl fitness genes?

Why are 39.8% of metal-important gene records also important under NaCl, and does the overlap track metal toxicity mechanism rather than chloride delivery?

## Hypothesis

Overlap reflects envelope and general stress physiology tied to toxicity mechanism, so matched-concentration chloride and sulfate salts of one metal give similar fitness profiles under identical conditions. The chloride-dose prediction was already rejected: ZnSO4 with 0 mM Cl- had 44.6% overlap.

## Why it matters

It would let metal-specific genes be separated from generic stress genes, sharpening candidate metal-resistance lists across organisms.

## How to test it

Experiment: in one tractable organism, run RB-TnSeq with matched metal chloride and metal sulfate concentrations under identical aerobic conditions, which removes the aerobic/anaerobic confound of the psRCH2 copper comparison (cross-salt r=0.439). Include an osmolarity-matched non-chloride control. Analysis first: in Fitness Browser organisms with KCl or choline chloride experiments, compare overlap with NaCl. These isolate chloride more specifically but still deliver another ion and osmotic load, so they are not chloride-only controls. Relate the DvH correlation range (zinc r=0.715 to iron r=0.086) to toxicity class. Report overlap with and without the Synechococcus elongatus outlier (39.8% versus 36.7%). The n_sick>=1 rule favors organisms with more experiments, and seven metals were tested only in DvH.

## What would support or refute it

Support: matched chloride and sulfate profiles agree, and shared genes are envelope or transport enriched. Refute: chloride and sulfate salts diverge, or overlap falls once osmotic load is controlled.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The matched-salt, osmolarity-controlled RB-TnSeq experiment has not been run; available choline chloride experiments differ in concentration.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/counter_ion_effects--5a2d3c21|Large share of metal-important genes also matter under NaCl stress]] (Insufficient literature evidence)
- Finding: [[findings/counter_ion_effects--482d2003|NaCl overlap does not track chloride delivered by the metal salt]] (Insufficient literature evidence)
- Finding: [[findings/counter_ion_effects--619981e8|Dose-dependent chloride effect on NaCl overlap rejected]] (Insufficient literature evidence)
- Finding: [[findings/counter_ion_effects--5c39821b|DvH metal–NaCl fitness correlations vary widely; report attributes this to toxicity mechanism]] (Insufficient literature evidence)
- Finding: [[findings/counter_ion_effects--5a523214|Same-metal copper salts in psRCH2 correlate weakly across counter ions]] (Insufficient literature evidence)

## Closest published work

- [PMID 32986214](https://pubmed.ncbi.nlm.nih.gov/32986214/) Inhibitory Effect of Copper and Zinc Ions on the Growth of Streptococcus pyogenes and Escherichia coli Biofilms.
- [PMID 27474723](https://pubmed.ncbi.nlm.nih.gov/27474723/) Novel Metal Cation Resistance Systems from Mutant Fitness Analysis of Denitrifying Pseudomonas stutzeri.
- [PMID 34432491](https://pubmed.ncbi.nlm.nih.gov/34432491/) Deciphering Microbial Metal Toxicity Responses via Random Bar Code Transposon Site Sequencing and Activity-Based Metabolomics.
- [PMID 12829273](https://pubmed.ncbi.nlm.nih.gov/12829273/) Efflux-mediated heavy metal resistance in prokaryotes.

PMID 27474723 and PMID 34432491 map metal fitness genes but do not decompose them against salt stress or counter-ion; PMID 32986214 tests copper and zinc ions in biofilms only.
