---
type: "Finding"
description: "Of 17,222 ortholog families across 48 bacteria, 859 (5.0%) are universally essential, 4,799 (27.9%) are variably essential and 11,564 (67.1%) are never essential; 839 of the universal families are strict single-copy and 20 contain paralogs."
finding_id: "essential_genome--5e670ea8"
result: "observation"
source: "essential_genome"
quantities: [{"value": "859 (5.0%)", "what": "universally essential families", "unit": "families", "denominator": "17,222 ortholog families", "scope": "48 bacteria"}, {"value": "4,799 (27.9%)", "what": "variably essential families", "unit": "families", "denominator": "17,222 ortholog families", "scope": "48 bacteria"}, {"value": "11,564 (67.1%)", "what": "never essential families", "unit": "families", "denominator": "17,222 ortholog families", "scope": "48 bacteria"}, {"value": "839", "what": "universally essential families that are strict single-copy (copy ratio <=1.5, no non-essential paralogs)", "unit": "families", "denominator": "859 universally essential families", "scope": ""}]
caveat: "The table defines 'universally essential' as essential in every organism where the family has members, so a family need not be present in every organism."
first_added: "2026-10-27"
source_hash: "6bf9c96cf9fac3bfd553efb4fed76a92d75e70a0549d7be588a83c632ea0c049"
---
# Only a small fraction of ortholog families are universally essential

Of 17,222 ortholog families across 48 bacteria, 859 (5.0%) are universally essential, 4,799 (27.9%) are variably essential and 11,564 (67.1%) are never essential; 839 of the universal families are strict single-copy and 20 contain paralogs. [src: essential_genome]

## Key figures

- **859 (5.0%) families**: universally essential families (denominator 17,222 ortholog families; scope 48 bacteria) [src: essential_genome]
- **4,799 (27.9%) families**: variably essential families (denominator 17,222 ortholog families; scope 48 bacteria) [src: essential_genome]
- **11,564 (67.1%) families**: never essential families (denominator 17,222 ortholog families; scope 48 bacteria) [src: essential_genome]
- **839 families**: universally essential families that are strict single-copy (copy ratio <=1.5, no non-essential paralogs) (denominator 859 universally essential families) [src: essential_genome]

## Evidence

> Of 17,222 ortholog families across 48 bacteria, 859 (5.0%) are universally essential. Of these, 839 are strict single-copy families (copy ratio <=1.5, no non-essential paralogs); 20 contain paralogs. 4,799 families (27.9%) are variably essential -- essential in some organisms, non-essential in others. 11,564 (67.1%) are never essential. [src: essential_genome]

From the report [[summaries/essential_genome__REPORT]].

## Caveat

The table defines 'universally essential' as essential in every organism where the family has members, so a family need not be present in every organism. [src: essential_genome]

> | Universally essential | 859 | 5.0% | Essential in every organism where family has members | [src: essential_genome]

## Other caveats in this report

- Of the hypothetical essential genes, 3,912 have orthologs and are predictable by this method, while 4,385 are orphan genes that the method cannot predict. [src: essential_genome]
- The report distinguishes its experimentally defined essential set from computationally conserved gene sets by requiring lethal transposon disruption across the tested organisms. [src: essential_genome]
- The report proposes paralogs, alternative pathways, and accessory-genome compensation as explanations for variable essentiality; its broad-spectrum antibiotic-target inference is an interpretation rather than a tested drug-efficacy result. [src: essential_genome]
- Recently acquired genes, rapid evolution, and lineage-specific innovation are proposed—not established—explanations for orphan essentials; the report compares them with 149 of 473 genes (31%) of unknown function in a minimal Mycoplasma genome. [src: essential_genome]
- Essential-gene calls are an upper bound because lack of insertions can reflect small size, AT-rich sequence, or scaffold-edge effects rather than lethality. [src: essential_genome]
