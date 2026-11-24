---
type: "Finding"
description: "Across the Fitness Browser organisms, 4,799 families (27.9%) are variably essential, being essential in some organisms and non-essential in others."
finding_id: "essential_genome--eee309a6"
result: "observation"
source: "essential_genome"
quantities: [{"value": "4,799", "what": "variably essential families", "unit": "", "denominator": "", "scope": ""}, {"value": "27.9%", "what": "share of ortholog families", "unit": "", "denominator": "", "scope": ""}]
caveat: "Transitive connections in the BBH graph can merge unrelated genes into the same ortholog group, particularly for multi-domain proteins."
first_added: "2026-11-24"
source_hash: "6bf9c96cf9fac3bfd553efb4fed76a92d75e70a0549d7be588a83c632ea0c049"
---
# Most essential families are variably essential rather than universal

Across the Fitness Browser organisms, 4,799 families (27.9%) are variably essential, being essential in some organisms and non-essential in others. [src: essential_genome]

## Key figures

- **4,799**: variably essential families [src: essential_genome]
- **27.9%**: share of ortholog families [src: essential_genome]

## Evidence

> 4,799 families (27.9%) are variably essential -- essential in some organisms, non-essential in others. [src: essential_genome]

From the report [[summaries/essential_genome__REPORT]].

## Caveat

Transitive connections in the BBH graph can merge unrelated genes into the same ortholog group, particularly for multi-domain proteins. [src: essential_genome]

> **Connected components can over-merge**: Transitive connections in the BBH graph can merge unrelated genes into the same ortholog group, particularly for multi-domain proteins. [src: essential_genome]

## Other caveats in this report

- Among hypothetical essential genes, 4,385 are orphans and are not predictable by the report's module-transfer method. [src: essential_genome]
- The report attributes its smaller experimentally defined universally essential set to restricting it to genes whose transposon disruption is lethal across all 48 tested organisms, a more stringent criterion than computational conservation. [src: essential_genome]
- The report's essential gene definition is an upper bound because absent transposon insertions can reflect small gene size, AT-rich sequence, or scaffold edge effects rather than true essentiality. [src: essential_genome]
- Bidirectional best BLAST hit orthology can miss paralogs, gene fusions, and distant homologs, so some reported orphan essentials may have undetected diverged orthologs. [src: essential_genome]
- The report's RB-TnSeq essentiality is defined under library construction conditions, typically rich media, and misses genes essential only under stress. [src: essential_genome]
