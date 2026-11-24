---
type: "Finding"
description: "Continuous bacterial growth parameters (\u00b5max, lag, yield) are not predictable from KO content or bulk genomic features under cross-genus holdout."
finding_id: "genotype_to_phenotype_enigma--710d2e8e"
result: "null result"
source: "genotype_to_phenotype_enigma"
quantities: []
caveat: "GC%, codon usage bias (CUB), and molecular fingerprints (Morgan FP) were planned but not computed, and these would be needed for continuous growth rate prediction."
first_added: "2026-11-24"
source_hash: "e69de667de1b74a70a09c07dc5b5bfb99aa3f042b003017eb1e60ec118fbab42"
---
# Continuous growth parameters are not predictable from gene content

Continuous bacterial growth parameters (µmax, lag, yield) are not predictable from KO content or bulk genomic features under cross-genus holdout. [src: genotype_to_phenotype_enigma]

## Evidence

> **Continuous growth parameters (µmax, lag, yield) are NOT predictable** from KO content or bulk genomic features under cross-genus holdout. [src: genotype_to_phenotype_enigma]

From the report [[summaries/genotype_to_phenotype_enigma__REPORT]].

## Caveat

GC%, codon usage bias (CUB), and molecular fingerprints (Morgan FP) were planned but not computed, and these would be needed for continuous growth rate prediction. [src: genotype_to_phenotype_enigma]

> **What was NOT used**: GC%, codon usage bias (CUB), and molecular fingerprints (Morgan FP) were planned but not computed — GC% is only available for 32/727 genomes, CUB requires nucleotide sequences not accessible from JupyterHub, and Morgan FP requires RDKit. These would be needed for continuous growth rate prediction. [src: genotype_to_phenotype_enigma]

## Other caveats in this report

- The bacterial growth model's SHAP features are weakly concordant with Fitness Browser (1.19× enrichment), because gene presence across genera and gene essentiality within one strain address different biological questions. [src: genotype_to_phenotype_enigma]
- Transfer learning from clinical phenotype databases may be biased for ENIGMA subsurface field isolates. [src: genotype_to_phenotype_enigma]
- Matching ENIGMA strains to the KBase Data Lakehouse pangenome through ncbi_strain_identifiers caused 12 of 32 genus-level mismatches. [src: genotype_to_phenotype_enigma]
- The ENIGMA short strain name MT20, representing Rhodanobacter glycinis, matched unrelated Streptococcus pneumoniae, with name collisions injecting 1,751 spurious clinical genomes into environmental profiles. [src: genotype_to_phenotype_enigma]
- The report documents the strain-name collision pitfall in docs/pitfalls.md and says it affects any project linking ENIGMA strains to the pangenome by name. [src: genotype_to_phenotype_enigma]
