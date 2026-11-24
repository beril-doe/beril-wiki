---
type: "Concept"
description: "Using confident prediction errors, model uncertainty and field relevance to rank new growth experiments, and how such a ranking is to be validated; it stops at wet-lab outcomes."
sources: ["summaries/genotype_to_phenotype_enigma__REPORT.md"]
---
# Active learning for selecting growth experiments from model errors

This page covers how confident prediction errors, model uncertainty and field relevance can rank new growth experiments, and how that ranking is to be validated. The evidence comes from one project, [[summaries/genotype_to_phenotype_enigma__REPORT]]. The ranking is built and a 50-experiment list exists, but the report rates the active-learning hypothesis (H6) only partially supported, because the formal test against random selection has not been run. [src: genotype_to_phenotype_enigma]

## Where the errors come from

The error audit covered 42,771 per-pair predictions from the full-corpus genus-blocked holdout. Overall accuracy was 65.1%, with 7,844 false positives (model predicts growth, actual is no-growth) and 7,101 false negatives (model predicts no-growth, actual is growth). [src: genotype_to_phenotype_enigma]

Filtering to predictions with |p − 0.5| > 0.25 isolates 1,276 high-confidence errors. These are cases where the model commits to a wrong answer, not borderline calls. [src: genotype_to_phenotype_enigma] The errors concentrate in genus × condition-class cells. Methylobacterium on amino acids, Sphingomonas on other carbon sources, and Microbacterium on nucleosides all show elevated confident-error rates. [src: genotype_to_phenotype_enigma]

The report reads these confident errors as the most informative signal for active learning. It offers three possible causes:
- a missing feature, such as a gene family absent from the KEGG ortholog (KO) ontology or not shared across the genus holdout;
- a regulatory mismatch, where the gene is present but not expressed under the test condition;
- a genuine biological oddity. [src: genotype_to_phenotype_enigma]

The report does not establish which cause applies to any given error. [src: genotype_to_phenotype_enigma]

## The ranking

The ranking pairs high-confidence errors with uncertainty-rich regions. [src: genotype_to_phenotype_enigma] It scores each of 343 testable conditions as error rate × model uncertainty × field relevance weight. [src: genotype_to_phenotype_enigma] The field-relevance weight doubles for conditions matching Oak Ridge geochemistry. These include nitrogen sources such as nitrate, organic acids associated with necromass decomposition, low-pH-compatible substrates, and aromatic compounds. [src: genotype_to_phenotype_enigma] The report says this weighting turns generic machine-learning uncertainty into bioremediation-actionable priorities: nitrogen cycle, organic acid metabolism and low-pH compatibility. [src: genotype_to_phenotype_enigma]

The top 10 conditions are fumaric acid, melibionic acid, fumarate, itaconic acid, 2-hydroxypropanoic acid (lactic acid), hydroxy-glutaric acid γ-lactone, difumarate, L-glutamic acid, nitrate and pyruvic acid. [src: genotype_to_phenotype_enigma]

For genus choice, Prescottella (16% growth rate across tested conditions) and Microbacterium (23%) are the most informative test subjects. Their predictions are among the least reliable, and new data on them would disproportionately improve cross-genus generalization. [src: genotype_to_phenotype_enigma]

Combining the genus and condition rankings gives a concrete 50-experiment proposal for ENIGMA's next growth screens. [src: genotype_to_phenotype_enigma] The deliverable pairs conditions such as fumaric acid, melibionic acid and nitrate with Prescottella and Microbacterium. [src: genotype_to_phenotype_enigma] The audit and candidate ranking sit in notebook NB09, and the 50-condition proposal sits in NB10. [src: genotype_to_phenotype_enigma]

## Validation

So far the validation is retrospective and argumentative. The report states that the 50 proposed experiments correspond to 7,844 prediction failures in the current corpus. It says that resolving even a fraction of them would move overall accuracy from 65.1% toward the per-class ceiling of ~78% seen on amino acids and nucleosides. [src: genotype_to_phenotype_enigma] This is a projection, not a measured gain.

The formal test is still to do. It would measure accuracy improvement per labeled pair, or per experiment, when experiments are added in active-learning-ranked order versus random order, using held-out current data. [src: genotype_to_phenotype_enigma] The report says the candidate ranking framework is in place and actionable. [src: genotype_to_phenotype_enigma] Whether to run the wet-lab experiments is an ENIGMA experimental decision, not an analytical one. [src: genotype_to_phenotype_enigma]

## Open Directions

- Run the retrospective subsampling test: add held-out labeled pairs in ranked versus random order and compare accuracy gain per pair. This would turn H6 from partially supported into a measured result.
- Separate the three proposed causes of confident errors (missing feature, regulatory mismatch, biological oddity) for the Methylobacterium, Sphingomonas and Microbacterium cells. For example, check whether the relevant gene families are absent from the KO ontology. This would show which errors new growth data can fix.
- Test the sensitivity of the ranking to the doubled field-relevance weight. This would show how much the top 50 depends on that choice.
- After wet-lab results arrive, compare observed outcomes with the 7,844-failure projection toward the ~78% ceiling.
