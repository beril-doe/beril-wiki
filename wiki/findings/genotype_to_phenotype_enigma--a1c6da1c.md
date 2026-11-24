---
type: "Finding"
description: "The report states that transition from genome-scale to gene-specific bacterial growth prediction requires 46K training pairs: with n=7 strains the model learns genome-size associations with amino-acid growth, whereas with n=46K pairs it learns condition-specific catabolic genes."
finding_id: "genotype_to_phenotype_enigma--a1c6da1c"
result: "inference"
source: "genotype_to_phenotype_enigma"
quantities: [{"value": "46K", "what": "training pairs needed for gene-specific prediction", "unit": "pairs", "denominator": "", "scope": ""}, {"value": "n=7", "what": "strains in the model learning genome-size associations", "unit": "strains", "denominator": "", "scope": ""}]
caveat: "The report characterizes the initial model as learning \"big genomes grow on amino acids\" \u2014 biologically real but not the condition-specific prediction needed for practical use."
first_added: "2026-11-24"
source_hash: "e69de667de1b74a70a09c07dc5b5bfb99aa3f042b003017eb1e60ec118fbab42"
---
# Gene-specific growth prediction emerges only with a much larger training corpus

The report states that transition from genome-scale to gene-specific bacterial growth prediction requires 46K training pairs: with n=7 strains the model learns genome-size associations with amino-acid growth, whereas with n=46K pairs it learns condition-specific catabolic genes. [src: genotype_to_phenotype_enigma]

## Key figures

- **46K pairs**: training pairs needed for gene-specific prediction [src: genotype_to_phenotype_enigma]
- **n=7 strains**: strains in the model learning genome-size associations [src: genotype_to_phenotype_enigma]

## Evidence

> **The transition from genome-scale to gene-specific prediction requires 46K training pairs**. With n=7 strains the model learns "big genomes grow on amino acids"; with n=46K pairs it learns condition-specific catabolic genes. [src: genotype_to_phenotype_enigma]

From the report [[summaries/genotype_to_phenotype_enigma__REPORT]].

## Caveat

The report characterizes the initial model as learning "big genomes grow on amino acids" — biologically real but not the condition-specific prediction needed for practical use. [src: genotype_to_phenotype_enigma]

> The model effectively learns "big genomes grow on amino acids" — biologically real but not the condition-specific prediction needed for practical use. [src: genotype_to_phenotype_enigma]

## Other caveats in this report

- The bacterial growth model's SHAP features are weakly concordant with Fitness Browser (1.19× enrichment), because gene presence across genera and gene essentiality within one strain address different biological questions. [src: genotype_to_phenotype_enigma]
- Transfer learning from clinical phenotype databases may be biased for ENIGMA subsurface field isolates. [src: genotype_to_phenotype_enigma]
- Matching ENIGMA strains to the KBase Data Lakehouse pangenome through ncbi_strain_identifiers caused 12 of 32 genus-level mismatches. [src: genotype_to_phenotype_enigma]
- The ENIGMA short strain name MT20, representing Rhodanobacter glycinis, matched unrelated Streptococcus pneumoniae, with name collisions injecting 1,751 spurious clinical genomes into environmental profiles. [src: genotype_to_phenotype_enigma]
- The report documents the strain-name collision pitfall in docs/pitfalls.md and says it affects any project linking ENIGMA strains to the pangenome by name. [src: genotype_to_phenotype_enigma]
