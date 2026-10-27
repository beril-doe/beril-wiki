---
type: "Research direction"
description: "Does the breadth of a resistance gene's substrate spectrum, rather than its mechanism class, determine how strongly its knockout flips from neutral to deleterious under antibiotics?"
hypothesis: "Within each mechanism class, genes with broader substrate range show larger fitness flips under antibiotics, and the efflux versus enzymatic-inactivation difference (+0.094 vs -0.001) is explained by spectrum breadth."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Fitness and AMR calls exist, but substrate-spectrum annotation and condition matching need new curation and modelling."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["amr_fitness_cost--7ffc7d6b", "amr_fitness_cost--104baecc"]
conflicts: []
papers: ["26203082", "25861385", "29769716", "34827256"]
builds_on: ["findings/amr_fitness_cost--7ffc7d6b", "findings/amr_fitness_cost--104baecc"]
projects: ["amr_fitness_cost"]
topics: ["resistance-defense-systems-and-mobile-elements"]
---
# Broad efflux pumps versus narrow enzymes: spectrum breadth drives antibiotic-conditioned fitness reversal

Does the breadth of a resistance gene's substrate spectrum, rather than its mechanism class, determine how strongly its knockout flips from neutral to deleterious under antibiotics?

## Hypothesis

Within each mechanism class, genes with broader substrate range show larger fitness flips under antibiotics, and the efflux versus enzymatic-inactivation difference (+0.094 vs -0.001) is explained by spectrum breadth.

## Why it matters

It would turn a mechanism-class contrast into a mechanistic principle that predicts which resistance genes are protective in mixed or unknown antibiotic environments.

## How to test it

For AMR genes in the Fitness Browser, annotate substrate spectrum (broad RND systems such as AcrAB-TolC versus narrow pumps; enzyme substrate range) and match each gene to antibiotic experiments with and without its cognate drug. Model flip magnitude with spectrum breadth and mechanism as terms, with organism as a random effect. Validate with condition-matched RB-TnSeq or targeted knockouts in a tractable organism.

## What would support or refute it

Support: breadth explains flip magnitude and mechanism adds little. Refute: mechanism class remains predictive after breadth is included, or the 43% of non-flipping genes do not fit the narrow-spectrum mismatch explanation.

## Data

Approach: analysis then experiment. Readiness: needs compute. Fitness and AMR calls exist, but substrate-spectrum annotation and condition matching need new curation and modelling.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/amr_fitness_cost--7ffc7d6b|Efflux genes flip toward importance under antibiotics more than enzymatic inactivation genes]] (Candidate novel)
- Finding: [[findings/amr_fitness_cost--104baecc|Fitness cost does not vary by resistance mechanism]] (Candidate novel)

## Closest published work

- [PMID 26203082](https://pubmed.ncbi.nlm.nih.gov/26203082/) Fitness cost of antibiotic susceptibility during bacterial infection.
- [PMID 25861385](https://pubmed.ncbi.nlm.nih.gov/25861385/) The fitness costs of antibiotic resistance mutations.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 34827256](https://pubmed.ncbi.nlm.nih.gov/34827256/) In-Vitro Selection of Ceftazidime/Avibactam Resistance in OXA-48-Like-Expressing Klebsiella pneumoniae: In-Vitro and In-Vivo Fitness, Genetic Basis and Activities of β-Lactam Plus Novel β-Lactamase Inhibitor or β-Lactam Enhancer Combinations.

PMID 26203082 shows resistance genes confer an in vivo advantage without splitting by mechanism or spectrum. PMID 29769716 supplies the fitness-compendium approach but not this contrast.
