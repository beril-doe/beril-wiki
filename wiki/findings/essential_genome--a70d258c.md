---
type: "Finding"
description: "The report identifies 7,084 essential genes with no orthologs in any other Fitness Browser organism, 58.7% of them hypothetical, versus 8.2% hypothetical among universally essential genes."
finding_id: "essential_genome--a70d258c"
result: "observation"
source: "essential_genome"
quantities: [{"value": "7,084", "what": "orphan essential genes with no orthologs in other FB organisms", "unit": "genes", "denominator": "", "scope": ""}, {"value": "58.7%", "what": "fraction of orphan essentials that are hypothetical", "unit": "%", "denominator": "orphan essential genes", "scope": ""}, {"value": "8.2%", "what": "fraction of universally essential genes that are hypothetical", "unit": "%", "denominator": "universally essential genes", "scope": ""}]
caveat: "Bidirectional-best-hit orthology is conservative and misses paralogs, gene fusions and distant homologs, so some orphan essentials may have undetected orthologs with diverged sequences."
first_added: "2026-10-27"
source_hash: "6bf9c96cf9fac3bfd553efb4fed76a92d75e70a0549d7be588a83c632ea0c049"
---
# Orphan essential genes are mostly uncharacterized compared with universal ones

The report identifies 7,084 essential genes with no orthologs in any other Fitness Browser organism, 58.7% of them hypothetical, versus 8.2% hypothetical among universally essential genes. [src: essential_genome]

## Key figures

- **7,084 genes**: orphan essential genes with no orthologs in other FB organisms [src: essential_genome]
- **58.7%**: fraction of orphan essentials that are hypothetical (denominator orphan essential genes) [src: essential_genome]
- **8.2%**: fraction of universally essential genes that are hypothetical (denominator universally essential genes) [src: essential_genome]

## Evidence

> 7,084 essential genes have no orthologs in any other FB organism. These are 58.7% hypothetical -- the least characterized yet most functionally important genes in each organism. By contrast, universally essential genes are only 8.2% hypothetical. [src: essential_genome]

From the report [[summaries/essential_genome__REPORT]].

## Caveat

Bidirectional-best-hit orthology is conservative and misses paralogs, gene fusions and distant homologs, so some orphan essentials may have undetected orthologs with diverged sequences. [src: essential_genome]

> - **BBH orthology is conservative**: Bidirectional best BLAST hits miss paralogs, gene fusions, and distant homologs. Some "orphan essentials" may have undetected orthologs with diverged sequences. [src: essential_genome]

## Other caveats in this report

- Of the hypothetical essential genes, 3,912 have orthologs and are predictable by this method, while 4,385 are orphan genes that the method cannot predict. [src: essential_genome]
- The report distinguishes its experimentally defined essential set from computationally conserved gene sets by requiring lethal transposon disruption across the tested organisms. [src: essential_genome]
- The report proposes paralogs, alternative pathways, and accessory-genome compensation as explanations for variable essentiality; its broad-spectrum antibiotic-target inference is an interpretation rather than a tested drug-efficacy result. [src: essential_genome]
- Recently acquired genes, rapid evolution, and lineage-specific innovation are proposed—not established—explanations for orphan essentials; the report compares them with 149 of 473 genes (31%) of unknown function in a minimal Mycoplasma genome. [src: essential_genome]
- Essential-gene calls are an upper bound because lack of insertions can reflect small size, AT-rich sequence, or scaffold-edge effects rather than lethality. [src: essential_genome]
