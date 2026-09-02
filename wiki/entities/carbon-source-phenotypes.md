---
type: "Dataset"
description: "Genome-by-condition corpus for predicting bacterial growth capability"
sources: ["summaries/genotype_to_phenotype_enigma__REPORT.md"]
---
# Carbon Source Phenotypes

## What this entity is

**Canonical name:** Carbon Source Phenotypes corpus. [src: genotype_to_phenotype_enigma]

**Known aliases:** Carbon Source Phenotypes; carbon-source phenotype corpus. [src: genotype_to_phenotype_enigma]

**Stable external identifier:** No stable external identifier is reported in the source document. [src: genotype_to_phenotype_enigma]

The Carbon Source Phenotypes corpus is a genome-by-condition dataset used to predict binary bacterial growth capability from genome content and to validate transfer of matched-condition phenotype information. [src: genotype_to_phenotype_enigma]

## Key facts

- The corpus contains 795 genomes and 379 conditions. [src: genotype_to_phenotype_enigma]

- It was integrated with ENIGMA growth curves, the ENIGMA Genome Depot, Fitness Browser RB-TnSeq data, Web of Microbes exometabolomics, pangenome data, and global 16S environmental data for genome-to-growth prediction. [src: genotype_to_phenotype_enigma]

- The combined modeling corpus contains 46,389 genome × condition pairs across 727 genomes and 363 conditions, with 4,293 shared [[entities/kegg]] orthologs. [src: genotype_to_phenotype_enigma]

- Matched-condition transfer from Carbon Source Phenotypes achieved an AUC of 0.800 and 76.8% accuracy at 23% coverage. Here, AUC means area under the receiver-operating-characteristic curve. [src: genotype_to_phenotype_enigma]

- Internal five-fold Carbon Source Phenotypes validation achieved an AUC of 0.858. [src: genotype_to_phenotype_enigma]

- Approximately 76% of ENIGMA conditions lacked either [[entities/gapmind]] pathway coverage or Carbon Source Phenotypes training data, and prediction on those conditions fell to approximately AUC 0.63. [src: genotype_to_phenotype_enigma]

- The corpus supported comparison between small-anchor and full-corpus models: the initial seven-strain model learned genome-scale and condition-class proxies, whereas the 46K-pair model identified more substrate-relevant transporters, catabolic enzymes, and regulators. [src: genotype_to_phenotype_enigma]

- The source report concludes that mechanistic gene-specific prediction requires hundreds of genomes per condition rather than a small number of anchor strains. [src: genotype_to_phenotype_enigma]

- The corpus is connected to [[concepts/condition-specific-fitness]] because its transfer and validation results distinguish predictable binary growth capability from continuous growth kinetics. [src: genotype_to_phenotype_enigma]

- It is also relevant to [[concepts/gene-function-acquisition-depth]] because larger training sets shifted model predictors from genome-scale proxies toward substrate-specific gene features. [src: genotype_to_phenotype_enigma]

## Limitations

- Condition matching relied on normalized names and produced 42 molecular matches; the report estimates that ChEBI-ID-based canonicalization could expand this to 60–80 matches. [src: genotype_to_phenotype_enigma]

- The source report does not provide a formal retrospective comparison between active-learning-ranked additions and random selection. [src: genotype_to_phenotype_enigma]

## Related source

- [[summaries/genotype_to_phenotype_enigma__REPORT]] — summary of the integrated ENIGMA genome-to-phenotype prediction study. [src: genotype_to_phenotype_enigma]
