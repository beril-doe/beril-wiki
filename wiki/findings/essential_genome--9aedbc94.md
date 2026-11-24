---
type: "Finding"
description: "Of 17,222 ortholog families across 48 bacteria, 859 (5.0%) are universally essential."
finding_id: "essential_genome--9aedbc94"
result: "observation"
source: "essential_genome"
quantities: [{"value": "859", "what": "universally essential ortholog families", "unit": "", "denominator": "", "scope": ""}, {"value": "17,222", "what": "ortholog families examined", "unit": "", "denominator": "", "scope": "48 bacteria"}, {"value": "5.0%", "what": "share of families universally essential", "unit": "", "denominator": "", "scope": ""}]
caveat: "RB-TnSeq essentiality is defined under specific library construction conditions (typically rich media), so genes essential only under stress would be missed."
first_added: "2026-11-24"
source_hash: "6bf9c96cf9fac3bfd553efb4fed76a92d75e70a0549d7be588a83c632ea0c049"
---
# A small fraction of ortholog families is universally essential across bacteria

Of 17,222 ortholog families across 48 bacteria, 859 (5.0%) are universally essential. [src: essential_genome]

## Key figures

- **859**: universally essential ortholog families [src: essential_genome]
- **17,222**: ortholog families examined (scope 48 bacteria) [src: essential_genome]
- **5.0%**: share of families universally essential [src: essential_genome]

## Evidence

> Of 17,222 ortholog families across 48 bacteria, 859 (5.0%) are universally essential. [src: essential_genome]

From the report [[summaries/essential_genome__REPORT]].

## Caveat

RB-TnSeq essentiality is defined under specific library construction conditions (typically rich media), so genes essential only under stress would be missed. [src: essential_genome]

> **Essentiality is condition-dependent**: RB-TnSeq essentiality is defined under specific library construction conditions (typically rich media). Genes essential only under stress would be missed. [src: essential_genome]

## Other caveats in this report

- Among hypothetical essential genes, 4,385 are orphans and are not predictable by the report's module-transfer method. [src: essential_genome]
- The report attributes its smaller experimentally defined universally essential set to restricting it to genes whose transposon disruption is lethal across all 48 tested organisms, a more stringent criterion than computational conservation. [src: essential_genome]
- The report's essential gene definition is an upper bound because absent transposon insertions can reflect small gene size, AT-rich sequence, or scaffold edge effects rather than true essentiality. [src: essential_genome]
- Bidirectional best BLAST hit orthology can miss paralogs, gene fusions, and distant homologs, so some reported orphan essentials may have undetected diverged orthologs. [src: essential_genome]
- Connected components of the report's bidirectional best BLAST hit graph can over-merge unrelated genes into an ortholog group through transitive connections, particularly for multi-domain proteins. [src: essential_genome]
