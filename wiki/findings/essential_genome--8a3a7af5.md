---
type: "Finding"
description: "The report identifies 15 gene families (ribosomal proteins, groEL, pyrG, fusA, valS and SelGGPS) that are essential in all 48 organisms, with no exceptions."
finding_id: "essential_genome--8a3a7af5"
result: "observation"
source: "essential_genome"
quantities: [{"value": "15", "what": "gene families essential in all organisms", "unit": "families", "denominator": "", "scope": "48 organisms"}, {"value": "48", "what": "organisms spanned by these families", "unit": "organisms", "denominator": "", "scope": "no exceptions"}]
caveat: "RB-TnSeq essentiality is defined under specific library construction conditions (typically rich media), so genes essential only under stress would be missed."
first_added: "2026-10-27"
source_hash: "6bf9c96cf9fac3bfd553efb4fed76a92d75e70a0549d7be588a83c632ea0c049"
---
# Fifteen gene families are essential in every organism tested

The report identifies 15 gene families (ribosomal proteins, groEL, pyrG, fusA, valS and SelGGPS) that are essential in all 48 organisms, with no exceptions. [src: essential_genome]

## Key figures

- **15 families**: gene families essential in all organisms (scope 48 organisms) [src: essential_genome]
- **48 organisms**: organisms spanned by these families (scope no exceptions) [src: essential_genome]

## Evidence

> The absolute core of bacterial life: ribosomal proteins (rpsC, rplW, rplK, rplB, rplA, rplF, rps11, rpsJ, rpsI, rpsM), chaperonin (groEL), CTP synthase (pyrG), translation elongation factor G (fusA), valyl-tRNA synthetase (valS), and geranyltranstransferase (SelGGPS). These 15 families span all 48 organisms with no exceptions. [src: essential_genome]

From the report [[summaries/essential_genome__REPORT]].

## Caveat

RB-TnSeq essentiality is defined under specific library construction conditions (typically rich media), so genes essential only under stress would be missed. [src: essential_genome]

> - **Essentiality is condition-dependent**: RB-TnSeq essentiality is defined under specific library construction conditions (typically rich media). Genes essential only under stress would be missed. [src: essential_genome]

## Other caveats in this report

- Of the hypothetical essential genes, 3,912 have orthologs and are predictable by this method, while 4,385 are orphan genes that the method cannot predict. [src: essential_genome]
- The report distinguishes its experimentally defined essential set from computationally conserved gene sets by requiring lethal transposon disruption across the tested organisms. [src: essential_genome]
- The report proposes paralogs, alternative pathways, and accessory-genome compensation as explanations for variable essentiality; its broad-spectrum antibiotic-target inference is an interpretation rather than a tested drug-efficacy result. [src: essential_genome]
- Recently acquired genes, rapid evolution, and lineage-specific innovation are proposed—not established—explanations for orphan essentials; the report compares them with 149 of 473 genes (31%) of unknown function in a minimal Mycoplasma genome. [src: essential_genome]
- Essential-gene calls are an upper bound because lack of insertions can reflect small size, AT-rich sequence, or scaffold-edge effects rather than lethality. [src: essential_genome]
