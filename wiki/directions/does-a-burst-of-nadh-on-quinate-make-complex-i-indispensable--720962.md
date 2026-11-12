---
type: "Research direction"
description: "In Acinetobacter baylyi ADP1, Complex I matters on quinate even though quinate yields less NADH per carbon than glucose or acetate. Is the reason that ring cleavage releases NADH in a burst that the alternative NADH dehydrogenase cannot reoxidise quickly enough?"
hypothesis: "Quinate growth produces a short-lived NADH surge that exceeds the alternative dehydrogenase's capacity, so Complex I deletion fails on quinate but not on glucose. Raising alternative dehydrogenase activity should rescue the Complex I mutant on quinate."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "The existing data are growth ratios and protein abundance; the NADH-burst explanation rests on theoretical stoichiometry and needs new redox and genetic measurements."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["respiratory_chain_wiring--e16ee45a", "respiratory_chain_wiring--6d65c6de", "respiratory_chain_wiring--fcdd6421", "respiratory_chain_wiring--7d7534df"]
conflicts: []
papers: ["18319726", "25374488", "8157582", "3805038"]
builds_on: ["findings/respiratory_chain_wiring--e16ee45a", "findings/respiratory_chain_wiring--6d65c6de", "findings/respiratory_chain_wiring--fcdd6421", "findings/respiratory_chain_wiring--7d7534df"]
projects: ["respiratory_chain_wiring"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Does a burst of NADH on quinate make Complex I indispensable?

In Acinetobacter baylyi ADP1, Complex I matters on quinate even though quinate yields less NADH per carbon than glucose or acetate. Is the reason that ring cleavage releases NADH in a burst that the alternative NADH dehydrogenase cannot reoxidise quickly enough?

## Hypothesis

Quinate growth produces a short-lived NADH surge that exceeds the alternative dehydrogenase's capacity, so Complex I deletion fails on quinate but not on glucose. Raising alternative dehydrogenase activity should rescue the Complex I mutant on quinate.

## Why it matters

It would show that respiratory requirements follow the rate of reducing-equivalent release from a pathway and not its total yield. That is a different kind of rule for predicting which respiratory components a metabolic route needs.

## How to test it

Measure the NADH-to-NAD+ ratio over time in wild-type ADP1 grown on quinate, glucose and acetate, looking for a transient peak on quinate. Express a strong non-proton-pumping NADH dehydrogenase in a Complex I deletion strain and test growth on quinate. Separately, add an NDH-2 deletion to test compensation on glucose, since that gene has no growth data in the existing collection. Extend to species that carry and lack the aromatic degradation pathway by checking co-retention of Complex I in the Pangenome Collection.

## What would support or refute it

Support: a transient NADH rise on quinate and rescue of the Complex I mutant by extra dehydrogenase capacity. Refute: NADH levels on quinate match glucose and extra dehydrogenase does not rescue the mutant, pointing to another cause such as proton-motive-force demand.

## Data

Approach: experiment. Readiness: needs new measurements. The existing data are growth ratios and protein abundance; the NADH-burst explanation rests on theoretical stoichiometry and needs new redox and genetic measurements.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/respiratory_chain_wiring--e16ee45a|Quinate Complex I dependence proposed to reflect NADH burst rate, not yield]] (Candidate novel)
- Finding: [[findings/respiratory_chain_wiring--6d65c6de|Respiratory requirements in ADP1 differ qualitatively by carbon source]] (Extends retrieved work)
- Finding: [[findings/respiratory_chain_wiring--fcdd6421|Alternative dehydrogenase presence does not predict Complex I dispensability across species]] (Insufficient literature evidence)
- Finding: [[findings/respiratory_chain_wiring--7d7534df|All three NADH dehydrogenases co-expressed, suggesting flux-based wiring]] (Insufficient literature evidence)

## Closest published work

- [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/) A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1.
- [PMID 25374488](https://pubmed.ncbi.nlm.nih.gov/25374488/) Novel metabolic features in Acinetobacter baylyi ADP1 revealed by a multiomics approach.
- [PMID 8157582](https://pubmed.ncbi.nlm.nih.gov/8157582/) Mutations in NADH:ubiquinone oxidoreductase of Escherichia coli affect growth on mixed amino acids.
- [PMID 3805038](https://pubmed.ncbi.nlm.nih.gov/3805038/) Purification and characterization of phthalate oxygenase and phthalate oxygenase reductase from Pseudomonas cepacia.

PMID 18319726 phenotyped the ADP1 deletion collection and PMID 25374488 described quinate-specific expression changes. Neither tests an NADH-burst explanation for Complex I dependence.
