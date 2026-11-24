---
type: "Finding"
description: "Orphan essential genes in the Fitness Browser dataset are 58.7% hypothetical, the highest uncharacterized fraction of any category."
finding_id: "essential_genome--ea3a8689"
result: "observation"
source: "essential_genome"
quantities: [{"value": "58.7%", "what": "fraction of orphan essentials that are hypothetical", "unit": "", "denominator": "", "scope": ""}]
caveat: "Bidirectional best BLAST hits miss paralogs, gene fusions, and distant homologs, so some orphan essentials may have undetected orthologs with diverged sequences."
first_added: "2026-11-24"
source_hash: "6bf9c96cf9fac3bfd553efb4fed76a92d75e70a0549d7be588a83c632ea0c049"
---
# Orphan essential genes are the most uncharacterized category

Orphan essential genes in the Fitness Browser dataset are 58.7% hypothetical, the highest uncharacterized fraction of any category. [src: essential_genome]

## Key figures

- **58.7%**: fraction of orphan essentials that are hypothetical [src: essential_genome]

## Evidence

> These orphan essentials are 58.7% hypothetical -- the highest uncharacterized fraction of any category. [src: essential_genome]

From the report [[summaries/essential_genome__REPORT]].

## Caveat

Bidirectional best BLAST hits miss paralogs, gene fusions, and distant homologs, so some orphan essentials may have undetected orthologs with diverged sequences. [src: essential_genome]

> **BBH orthology is conservative**: Bidirectional best BLAST hits miss paralogs, gene fusions, and distant homologs. Some "orphan essentials" may have undetected orthologs with diverged sequences. [src: essential_genome]

## Other caveats in this report

- Among hypothetical essential genes, 4,385 are orphans and are not predictable by the report's module-transfer method. [src: essential_genome]
- The report attributes its smaller experimentally defined universally essential set to restricting it to genes whose transposon disruption is lethal across all 48 tested organisms, a more stringent criterion than computational conservation. [src: essential_genome]
- The report's essential gene definition is an upper bound because absent transposon insertions can reflect small gene size, AT-rich sequence, or scaffold edge effects rather than true essentiality. [src: essential_genome]
- Connected components of the report's bidirectional best BLAST hit graph can over-merge unrelated genes into an ortholog group through transitive connections, particularly for multi-domain proteins. [src: essential_genome]
- The report's RB-TnSeq essentiality is defined under library construction conditions, typically rich media, and misses genes essential only under stress. [src: essential_genome]
