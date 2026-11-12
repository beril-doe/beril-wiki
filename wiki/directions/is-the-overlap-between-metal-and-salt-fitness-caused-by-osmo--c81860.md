---
type: "Research direction"
description: "Many genes that matter under metal stress also matter under NaCl, even for zinc delivered as sulfate with no chloride. Is the shared stress osmotic pressure, envelope damage, or something specific to sodium or chloride?"
hypothesis: "The shared metal and NaCl genes respond to osmotic pressure or envelope damage rather than to a specific ion. Metal overlap with non-ionic osmotic conditions should then match overlap with NaCl, and should not depend on how much chloride the metal salt delivers."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Metal and NaCl experiments already exist in the Fitness Browser. Which non-ionic osmotic and envelope experiments exist per organism is not stated, so coverage may limit the first step."
collections: ["kescience-fitnessbrowser"]
findings: ["counter_ion_effects--482d2003", "counter_ion_effects--619981e8", "counter_ion_effects--5c39821b", "counter_ion_effects--5a2d3c21"]
conflicts: ["conflict--shared-stress-versus-stressor-specific-fitness--07279e23"]
papers: ["32986214", "25968644", "29769716", "12829273"]
builds_on: ["findings/counter_ion_effects--482d2003", "findings/counter_ion_effects--619981e8", "findings/counter_ion_effects--5c39821b", "findings/counter_ion_effects--5a2d3c21", "conflicts/conflict--shared-stress-versus-stressor-specific-fitness--07279e23"]
projects: ["counter_ion_effects", "metal_cross_resistance"]
topics: ["gene-fitness-landscapes-and-cofitness-modules"]
---
# Is the overlap between metal and salt fitness caused by osmotic stress or by envelope damage?

Many genes that matter under metal stress also matter under NaCl, even for zinc delivered as sulfate with no chloride. Is the shared stress osmotic pressure, envelope damage, or something specific to sodium or chloride?

## Hypothesis

The shared metal and NaCl genes respond to osmotic pressure or envelope damage rather than to a specific ion. Metal overlap with non-ionic osmotic conditions should then match overlap with NaCl, and should not depend on how much chloride the metal salt delivers.

## Why it matters

It would show what the shared-stress component of metal fitness data actually measures. Metal-specific genes could then be separated from general damage responses, and metal fitness could be read mechanistically.

## How to test it

In the Fitness Browser, take the 19 organisms with metal and NaCl experiments. Run two separate comparisons: (a) each metal's gene overlap with non-ionic osmotic conditions (sugar or polyol), and (b) overlap with envelope-targeting conditions, each set against overlap with NaCl. Within each organism, subsample to equal numbers of experiments per condition type, and repeat at several cutoffs for calling a gene important, since the overlap depends on that cutoff. Compare chloride-delivering metals (cobalt, copper, nickel) with sulfate-delivered zinc. Then, in Desulfovibrio vulgaris Hildenborough, run barcoded transposon fitness assays with matched chloride and sulfate salts, KCl and sorbitol.

## What would support or refute it

Support for an osmotic cause: overlap with sorbitol-type conditions is as high as with NaCl at every cutoff, while envelope conditions add little. Support for envelope damage: the reverse. Refute both: overlap is specific to NaCl or KCl, or vanishes with non-ionic conditions, pointing to an ion-specific mechanism. A result that changes with the cutoff or experiment count would be inconclusive.

## Data

Approach: analysis then experiment. Readiness: needs compute. Metal and NaCl experiments already exist in the Fitness Browser. Which non-ionic osmotic and envelope experiments exist per organism is not stated, so coverage may limit the first step.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/counter_ion_effects--482d2003|NaCl overlap does not track chloride delivered by the metal salt]] (Insufficient literature evidence)
- Finding: [[findings/counter_ion_effects--619981e8|Dose-dependent chloride effect on NaCl overlap rejected]] (Insufficient literature evidence)
- Finding: [[findings/counter_ion_effects--5c39821b|DvH metal–NaCl fitness correlations vary widely; report attributes this to toxicity mechanism]] (Insufficient literature evidence)
- Finding: [[findings/counter_ion_effects--5a2d3c21|Large share of metal-important genes also matter under NaCl stress]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--shared-stress-versus-stressor-specific-fitness--07279e23|Universal Positive Metal Cross-Resistance or Metal-Dependent Overlap with Salt Stress?]]

## Closest published work

- [PMID 32986214](https://pubmed.ncbi.nlm.nih.gov/32986214/) Inhibitory Effect of Copper and Zinc Ions on the Growth of Streptococcus pyogenes and Escherichia coli Biofilms.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 12829273](https://pubmed.ncbi.nlm.nih.gov/12829273/) Efflux-mediated heavy metal resistance in prokaryotes.

PMID 32986214 reports copper and zinc growth inhibition without separating ion from osmotic effects. PMID 25968644 and PMID 29769716 supply the fitness method and data. This direction asks what the shared fitness signal responds to.
