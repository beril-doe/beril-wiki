---
type: "Research direction"
description: "Quinate yields less NADH per carbon than glucose or acetate, yet Complex I is more essential on quinate. Does a fast burst of NADH from ring cleavage exceed the capacity of the alternative enzyme?"
hypothesis: "Slowing quinate catabolism removes the Complex I requirement, and raising alternative NADH dehydrogenase capacity relieves it. Complex I essentiality follows the rate of NADH production, not its yield."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "The central prediction needs growth and NADH measurements under controlled supply rates that are not in the catalog, and the alternative enzyme has no growth data."
databases: []
tables: []
findings: ["respiratory_chain_wiring--e16ee45a", "respiratory_chain_wiring--fcdd6421", "respiratory_chain_wiring--6d65c6de"]
conflicts: []
papers: ["18319726", "25374488", "8157582"]
builds_on: ["findings/respiratory_chain_wiring--e16ee45a", "findings/respiratory_chain_wiring--fcdd6421", "findings/respiratory_chain_wiring--6d65c6de"]
projects: ["respiratory_chain_wiring"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Does Complex I matter on quinate because ring cleavage overloads the alternative NADH dehydrogenase?

Quinate yields less NADH per carbon than glucose or acetate, yet Complex I is more essential on quinate. Does a fast burst of NADH from ring cleavage exceed the capacity of the alternative enzyme?

## Hypothesis

Slowing quinate catabolism removes the Complex I requirement, and raising alternative NADH dehydrogenase capacity relieves it. Complex I essentiality follows the rate of NADH production, not its yield.

## Why it matters

It would show that respiratory wiring is set by flux dynamics, not by pathway stoichiometry. That would explain why alternative-enzyme presence did not predict Complex I dispensability across species.

## How to test it

In Acinetobacter baylyi ADP1, grow Complex I deletion and wild-type strains on quinate at several limiting supply rates and on quinate mixed with a slowly used carbon. Measure growth and the NADH to NAD+ ratio. Repeat with the alternative NADH dehydrogenase overexpressed. Compare with the same strains on glucose and acetate.

## What would support or refute it

Support: the Complex I growth defect shrinks as quinate supply slows and recovers when the alternative enzyme is overexpressed, with a higher NADH ratio in the deletion on fast quinate. Refute: the defect stays equally severe at every supply rate and overexpression does not rescue it.

## Data

Approach: experiment. Readiness: needs new measurements. The central prediction needs growth and NADH measurements under controlled supply rates that are not in the catalog, and the alternative enzyme has no growth data.

## Builds on

- Finding: [[findings/respiratory_chain_wiring--e16ee45a|Quinate Complex I dependence proposed to reflect NADH burst rate, not yield]] (Candidate novel)
- Finding: [[findings/respiratory_chain_wiring--fcdd6421|Alternative dehydrogenase presence does not predict Complex I dispensability across species]] (Insufficient literature evidence)
- Finding: [[findings/respiratory_chain_wiring--6d65c6de|Respiratory requirements in ADP1 differ qualitatively by carbon source]] (Extends retrieved work)

## Closest published work

- [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/) A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1.
- [PMID 25374488](https://pubmed.ncbi.nlm.nih.gov/25374488/) Novel metabolic features in Acinetobacter baylyi ADP1 revealed by a multiomics approach.
- [PMID 8157582](https://pubmed.ncbi.nlm.nih.gov/8157582/) Mutations in NADH:ubiquinone oxidoreductase of Escherichia coli affect growth on mixed amino acids.

PMID 18319726 and PMID 25374488 describe ADP1 growth and expression on quinate. Neither examines Complex I need as a function of NADH production rate.
