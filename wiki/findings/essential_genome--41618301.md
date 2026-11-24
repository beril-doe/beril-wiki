---
type: "Finding"
description: "In the Fitness Browser dataset, 15 gene families are essential in all 48 organisms with no exceptions."
finding_id: "essential_genome--41618301"
result: "observation"
source: "essential_genome"
quantities: [{"value": "15", "what": "gene families essential in every organism", "unit": "", "denominator": "", "scope": ""}, {"value": "48", "what": "organisms", "unit": "", "denominator": "", "scope": "Fitness Browser"}]
caveat: "The Fitness Browser organisms are biased toward culturable Proteobacteria, so essentiality patterns in uncultured lineages, Actinobacteria, or Firmicutes are underrepresented."
first_added: "2026-11-24"
source_hash: "6bf9c96cf9fac3bfd553efb4fed76a92d75e70a0549d7be588a83c632ea0c049"
---
# A handful of gene families are essential in every organism tested

In the Fitness Browser dataset, 15 gene families are essential in all 48 organisms with no exceptions. [src: essential_genome]

## Key figures

- **15**: gene families essential in every organism [src: essential_genome]
- **48**: organisms (scope Fitness Browser) [src: essential_genome]

## Evidence

> These 15 families span all 48 organisms with no exceptions. [src: essential_genome]

From the report [[summaries/essential_genome__REPORT]].

## Caveat

The Fitness Browser organisms are biased toward culturable Proteobacteria, so essentiality patterns in uncultured lineages, Actinobacteria, or Firmicutes are underrepresented. [src: essential_genome]

> **48 organisms is taxonomically limited**: The Fitness Browser organisms are biased toward culturable Proteobacteria. Essentiality patterns in uncultured lineages, Actinobacteria, or Firmicutes are underrepresented. [src: essential_genome]

## Other caveats in this report

- Among hypothetical essential genes, 4,385 are orphans and are not predictable by the report's module-transfer method. [src: essential_genome]
- The report attributes its smaller experimentally defined universally essential set to restricting it to genes whose transposon disruption is lethal across all 48 tested organisms, a more stringent criterion than computational conservation. [src: essential_genome]
- The report's essential gene definition is an upper bound because absent transposon insertions can reflect small gene size, AT-rich sequence, or scaffold edge effects rather than true essentiality. [src: essential_genome]
- Bidirectional best BLAST hit orthology can miss paralogs, gene fusions, and distant homologs, so some reported orphan essentials may have undetected diverged orthologs. [src: essential_genome]
- Connected components of the report's bidirectional best BLAST hit graph can over-merge unrelated genes into an ortholog group through transitive connections, particularly for multi-domain proteins. [src: essential_genome]
