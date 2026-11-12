---
type: "Research direction"
description: "About four in ten metal-important genes are also important under salt stress, and chloride delivery does not explain it (zinc sulfate overlapped as much as chloride metals). Is the shared set a general osmotic or envelope response, or specific to sodium?"
hypothesis: "The shared genes are important under non-ionic osmotic stress (such as sorbitol or sucrose) about as often as under sodium chloride, and less often under potassium or choline chloride at matched strength."
approach: "lakehouse analysis"
readiness: "unknown"
readiness_basis: "The condition fields are listed, but the catalog did not show whether enough potassium chloride, choline chloride and non-ionic osmolyte experiments exist across organisms."
databases: ["kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.experiment", "kescience.fitnessbrowser.specificphenotype", "kescience.fitnessbrowser.specog", "kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.seedannotation"]
findings: ["counter_ion_effects--482d2003", "counter_ion_effects--619981e8", "counter_ion_effects--5a2d3c21", "counter_ion_effects--5c39821b"]
conflicts: ["conflict--gene-essentiality--1ce33d4d"]
papers: ["32986214", "19227837", "12829273", "27474723"]
builds_on: ["findings/counter_ion_effects--482d2003", "findings/counter_ion_effects--619981e8", "findings/counter_ion_effects--5a2d3c21", "findings/counter_ion_effects--5c39821b", "conflicts/conflict--gene-essentiality--1ce33d4d"]
projects: ["counter_ion_effects", "metal_specificity"]
topics: ["gene-essentiality-and-perturbation-assay-validity"]
---
# Is the shared metal and salt gene set an osmotic response rather than a sodium one?

About four in ten metal-important genes are also important under salt stress, and chloride delivery does not explain it (zinc sulfate overlapped as much as chloride metals). Is the shared set a general osmotic or envelope response, or specific to sodium?

## Hypothesis

The shared genes are important under non-ionic osmotic stress (such as sorbitol or sucrose) about as often as under sodium chloride, and less often under potassium or choline chloride at matched strength.

## Why it matters

This would show what the shared metal-salt gene set is and how to correct for it in metal studies. Support points to envelope and osmotic biology. Refutation points to sodium-specific handling or to metal-specific mechanisms.

## How to test it

In Fitness Browser organisms with several salt and osmolyte experiments, select the metal-important genes that are also important under sodium chloride. Using the experiment table's condition fields, find experiments with potassium chloride, choline chloride, sorbitol or sucrose. Measure what fraction of the shared set is important in each, relative to the fraction of other genes. Check that the answer is not dominated by one organism, such as Synechococcus elongatus.

## What would support or refute it

Support: shared genes are as often important under non-ionic osmolytes as under sodium chloride. Refute: they are important under sodium chloride but not under matched osmolytes, or the experiments needed do not exist in enough organisms.

## Data

Approach: lakehouse analysis. Readiness: unknown. The condition fields are listed, but the catalog did not show whether enough potassium chloride, choline chloride and non-ionic osmolyte experiments exist across organisms.

## Builds on

- Finding: [[findings/counter_ion_effects--482d2003|NaCl overlap does not track chloride delivered by the metal salt]] (Insufficient literature evidence)
- Finding: [[findings/counter_ion_effects--619981e8|Dose-dependent chloride effect on NaCl overlap rejected]] (Insufficient literature evidence)
- Finding: [[findings/counter_ion_effects--5a2d3c21|Large share of metal-important genes also matter under NaCl stress]] (Insufficient literature evidence)
- Finding: [[findings/counter_ion_effects--5c39821b|DvH metal–NaCl fitness correlations vary widely; report attributes this to toxicity mechanism]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--gene-essentiality--1ce33d4d|How Large Is the Overlap Between Metal-Fitness and Osmotic-Stress Genes?]]

## Closest published work

- [PMID 32986214](https://pubmed.ncbi.nlm.nih.gov/32986214/) Inhibitory Effect of Copper and Zinc Ions on the Growth of Streptococcus pyogenes and Escherichia coli Biofilms.
- [PMID 19227837](https://pubmed.ncbi.nlm.nih.gov/19227837/) Biosorption of nickel by yeasts in an osmotically unsuitable environment.
- [PMID 12829273](https://pubmed.ncbi.nlm.nih.gov/12829273/) Efflux-mediated heavy metal resistance in prokaryotes.
- [PMID 27474723](https://pubmed.ncbi.nlm.nih.gov/27474723/) Novel Metal Cation Resistance Systems from Mutant Fitness Analysis of Denitrifying Pseudomonas stutzeri.

PMIDs 32986214 and 19227837 study copper, zinc and nickel effects in other systems and do not dissect a genome-wide gene set shared between metal and osmotic stress.
