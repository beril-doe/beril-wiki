---
type: "Finding"
description: "Clade size does NOT predict essentiality rate (rho=-0.13, p=0.36)."
finding_id: "essential_genome--28731145"
result: "null result"
source: "essential_genome"
quantities: [{"value": "rho=-0.13", "what": "correlation of clade size with essentiality rate", "unit": "", "denominator": "", "scope": ""}, {"value": "p=0.36", "what": "p-value", "unit": "", "denominator": "", "scope": ""}]
caveat: "The essential gene definition is an upper bound, because genes without transposon insertions may lack them due to small size, AT-rich sequence, or scaffold edge effects rather than true essentiality."
first_added: "2026-11-24"
source_hash: "6bf9c96cf9fac3bfd553efb4fed76a92d75e70a0549d7be588a83c632ea0c049"
---
# Clade size does not predict essentiality rate

Clade size does NOT predict essentiality rate (rho=-0.13, p=0.36). [src: essential_genome]

## Key figures

- **rho=-0.13**: correlation of clade size with essentiality rate [src: essential_genome]
- **p=0.36**: p-value [src: essential_genome]

## Evidence

> Clade size does NOT predict essentiality rate (rho=-0.13, p=0.36). [src: essential_genome]

From the report [[summaries/essential_genome__REPORT]].

## Caveat

The essential gene definition is an upper bound, because genes without transposon insertions may lack them due to small size, AT-rich sequence, or scaffold edge effects rather than true essentiality. [src: essential_genome]

> **Essential gene definition is an upper bound**: Genes without transposon insertions may lack insertions due to small size, AT-rich sequence, or scaffold edge effects, not true essentiality. [src: essential_genome]

## Other caveats in this report

- Among hypothetical essential genes, 4,385 are orphans and are not predictable by the report's module-transfer method. [src: essential_genome]
- The report attributes its smaller experimentally defined universally essential set to restricting it to genes whose transposon disruption is lethal across all 48 tested organisms, a more stringent criterion than computational conservation. [src: essential_genome]
- Bidirectional best BLAST hit orthology can miss paralogs, gene fusions, and distant homologs, so some reported orphan essentials may have undetected diverged orthologs. [src: essential_genome]
- Connected components of the report's bidirectional best BLAST hit graph can over-merge unrelated genes into an ortholog group through transitive connections, particularly for multi-domain proteins. [src: essential_genome]
- The report's RB-TnSeq essentiality is defined under library construction conditions, typically rich media, and misses genes essential only under stress. [src: essential_genome]
