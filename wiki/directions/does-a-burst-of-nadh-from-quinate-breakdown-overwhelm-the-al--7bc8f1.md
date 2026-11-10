---
type: "Research direction"
description: "In Acinetobacter baylyi ADP1, Complex I is more essential on quinate than on glucose or acetate, although quinate yields fewer NADH per carbon (0.57 versus 1.50). Is this because quinate breakdown releases NADH in a concentrated burst that exceeds the capacity of the alternative NADH dehydrogenase (NDH-2)?"
hypothesis: "Three predictions follow. Raising NDH-2 capacity on a Complex I-deficient background restores growth on quinate. Slowing quinate flux does the same. Deleting NDH-2 makes Complex I required on glucose."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "ADP1 has no NDH-2 growth data, and the cross-species check has only 4 organisms without NDH-2."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["respiratory_chain_wiring--e16ee45a", "respiratory_chain_wiring--6d65c6de", "respiratory_chain_wiring--fcdd6421", "respiratory_chain_wiring--7d7534df"]
conflicts: []
papers: ["18319726", "25374488", "8157582", "17133620", "3805038"]
builds_on: ["findings/respiratory_chain_wiring--e16ee45a", "findings/respiratory_chain_wiring--6d65c6de", "findings/respiratory_chain_wiring--fcdd6421", "findings/respiratory_chain_wiring--7d7534df"]
projects: ["respiratory_chain_wiring"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Does a burst of NADH from quinate breakdown overwhelm the alternative dehydrogenase in Acinetobacter?

In Acinetobacter baylyi ADP1, Complex I is more essential on quinate than on glucose or acetate, although quinate yields fewer NADH per carbon (0.57 versus 1.50). Is this because quinate breakdown releases NADH in a concentrated burst that exceeds the capacity of the alternative NADH dehydrogenase (NDH-2)?

## Hypothesis

Three predictions follow. Raising NDH-2 capacity on a Complex I-deficient background restores growth on quinate. Slowing quinate flux does the same. Deleting NDH-2 makes Complex I required on glucose.

## Why it matters

The explanation attributes a carbon-source-specific respiratory requirement to the rate of NADH production and not to its yield. If it holds, respiratory wiring should be read as a flux property, which would affect how metabolic models predict substrate-dependent essentiality. The stoichiometry behind it is theoretical, not measured flux.

## How to test it

In ADP1, build an NDH-2 deletion and an NDH-2 overexpression strain on a Complex I deletion background. Measure growth and the NADH to NAD+ ratio on quinate, glucose and acetate, and on quinate at lowered uptake rates. First check in the Pangenome Collection and the Fitness Browser whether Complex I dependence on aromatic substrates tracks NDH-2 presence, using more than the 4 organisms without NDH-2 currently available.

## What would support or refute it

Support requires all three: overexpression rescues the Complex I deletion on quinate, slowed quinate uptake reduces the requirement, and NDH-2 deletion makes Complex I required on glucose, with a higher NADH ratio on quinate. Refutation: overexpression leaves the quinate requirement unchanged (against the capacity prediction), slowed uptake leaves it unchanged (against the burst prediction), or NDH-2 deletion leaves glucose growth independent of Complex I. If only some hold, the burst model is incomplete.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. ADP1 has no NDH-2 growth data, and the cross-species check has only 4 organisms without NDH-2.

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
- [PMID 17133620](https://pubmed.ncbi.nlm.nih.gov/17133620/) Substrate-inducible versions of internal alternative NADH: ubiquinone oxidoreductase from Yarrowia lipolytica.
- [PMID 3805038](https://pubmed.ncbi.nlm.nih.gov/3805038/) Purification and characterization of phthalate oxygenase and phthalate oxygenase reductase from Pseudomonas cepacia.

PMID 18319726 and PMID 25374488 describe ADP1 quinate growth phenotypes and expression changes. PMID 8157582 reports acetate-specific defects in E. coli complex I mutants. None tests whether NADH burst rate sets the Complex I requirement.
