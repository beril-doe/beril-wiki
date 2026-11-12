---
type: "Research direction"
description: "The cystic fibrosis formulation work measured inhibition only on a laboratory strain that carries a different toxin type from most cystic fibrosis isolates, and no sugar or amino acid gave commensals a clear edge. Does inhibition of lung isolates depend on overlap in amino acid use instead?"
hypothesis: "For lung-adapted, toxin-type-matched isolates, metabolic overlap weighted by the isolate's own substrate preferences predicts commensal inhibition better than overlap weighted by the laboratory strain's preferences, with amino acids carrying most of the signal."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Existing competition and virulence tables supply the commensal panel and typing, but inhibition and substrate preferences for toxin-type-matched lung isolates have not been measured; their column contents were not shown."
databases: ["kbase.ke_pangenome", "protect.curated", "protect.formulation", "protect.genome_analysis"]
tables: ["protect.formulation.competition_screen", "protect.curated.silver_competition", "protect.genome_analysis.isolate_virulence_factors", "kbase.ke_pangenome.gapmind_pathways"]
findings: ["cf_formulation_design--1799127b", "cf_formulation_design--8bf20af1", "cf_formulation_design--951bde52", "cf_formulation_design--460ed03a", "cf_formulation_design--94972e2b"]
conflicts: []
papers: ["17873029", "27881418", "35174108", "25409940", "19936230"]
builds_on: ["findings/cf_formulation_design--1799127b", "findings/cf_formulation_design--8bf20af1", "findings/cf_formulation_design--951bde52", "findings/cf_formulation_design--460ed03a", "findings/cf_formulation_design--94972e2b"]
projects: ["cf_formulation_design"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Do commensals inhibit lung-adapted Pseudomonas by competing for amino acids rather than sugars?

The cystic fibrosis formulation work measured inhibition only on a laboratory strain that carries a different toxin type from most cystic fibrosis isolates, and no sugar or amino acid gave commensals a clear edge. Does inhibition of lung isolates depend on overlap in amino acid use instead?

## Hypothesis

For lung-adapted, toxin-type-matched isolates, metabolic overlap weighted by the isolate's own substrate preferences predicts commensal inhibition better than overlap weighted by the laboratory strain's preferences, with amino acids carrying most of the signal.

## Why it matters

It would show whether formulations designed around one reference strain transfer to the strains in patients. Lung isolates score lower on several sugar pathways, which the earlier work reads as possible metabolic streamlining (an interpretation, not a measured loss), so the test also shows whether design should target amino acid use.

## How to test it

Choose commensals from the existing competition screen and a panel of ExoS-positive cystic fibrosis isolates plus the laboratory strain. Measure growth inhibition of each isolate in co-culture and in conditioned medium. Measure each isolate's growth on sugars and amino acids directly, so any sugar-use difference is observed rather than inferred from pathway scores. Compute overlap weighted by each isolate's measured substrate preferences. Compare how well strain-specific and laboratory-strain weighting predict inhibition, and repeat with the three-member formulation that adds Micrococcus luteus.

## What would support or refute it

Support: strain-specific weighting predicts inhibition clearly better, and amino acids carry the predictive signal. Refutation: laboratory-strain weighting predicts as well, or inhibition of lung isolates is unrelated to overlap. That would point to non-metabolic inhibition mechanisms.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Existing competition and virulence tables supply the commensal panel and typing, but inhibition and substrate preferences for toxin-type-matched lung isolates have not been measured; their column contents were not shown.

## Builds on

- Finding: [[findings/cf_formulation_design--1799127b|Cystic fibrosis P. aeruginosa is mostly ExoS+, unlike the PA14 assay strain]] (Extends retrieved work)
- Finding: [[findings/cf_formulation_design--8bf20af1|No tested substrate gives commensals a clear advantage over PA14]] (Insufficient literature evidence)
- Finding: [[findings/cf_formulation_design--951bde52|Metabolic overlap with PA14 predicts inhibition, but only modestly]] (Insufficient literature evidence)
- Finding: [[findings/cf_formulation_design--460ed03a|Lung P. aeruginosa genomes score lower on sugar pathways than non-lung genomes]] (Extends retrieved work)
- Finding: [[findings/cf_formulation_design--94972e2b|Adding Micrococcus luteus lifts modeled niche coverage to full]] (Insufficient literature evidence)

## Closest published work

- [PMID 17873029](https://pubmed.ncbi.nlm.nih.gov/17873029/) Nutritional cues control Pseudomonas aeruginosa multicellular behavior in cystic fibrosis sputum.
- [PMID 27881418](https://pubmed.ncbi.nlm.nih.gov/27881418/) Environmental Pseudomonads Inhibit Cystic Fibrosis Patient-Derived Pseudomonas aeruginosa.
- [PMID 35174108](https://pubmed.ncbi.nlm.nih.gov/35174108/) Commensal Bacteria in the Cystic Fibrosis Airway Microbiome Reduce P. aeruginosa Induced Inflammation.
- [PMID 25409940](https://pubmed.ncbi.nlm.nih.gov/25409940/) Impact of glycerol-3-phosphate dehydrogenase on virulence factor production by Pseudomonas aeruginosa.
- [PMID 19936230](https://pubmed.ncbi.nlm.nih.gov/19936230/) Pseudomonas aeruginosa population structure revisited.

PMID 17873029 describes carbon preferences of Pseudomonas in cystic fibrosis sputum and PMID 27881418 shows environmental pseudomonads inhibiting patient-derived isolates. Neither tests whether strain-specific substrate weighting predicts inhibition of lung-adapted isolates.
