---
type: "Compound"
description: "Aromatic substrate catabolized by ADP1 via quinate dehydrogenase and the β-ketoadipate pathway."
sources: ["summaries/aromatic_catabolism_network__REPORT.md", "summaries/respiratory_chain_wiring__REPORT.md"]
aliases: ["quinic acid"]
---
# Quinate

Quinate (quinic acid) is catabolized in Acinetobacter baylyi ADP1 through the β-ketoadipate pathway, and its catabolism needs a PQQ-dependent quinate dehydrogenase. [src: aromatic_catabolism_network] See [[entities/acinetobacter-baylyi-adp1]] and [[entities/ketoadipate-pathway]].

## Key facts

- The 51 quinate-specific genes in ADP1 form a coherent metabolic dependency network around the β-ketoadipate pathway. [src: aromatic_catabolism_network] Compare [[concepts/support-gene-networks-around-catabolic-pathways]].
- Quinate catabolism proceeds through protocatechuate to β-ketoadipate. It yields succinyl-CoA and acetyl-CoA, which enter the tricarboxylic acid (TCA) cycle. [src: aromatic_catabolism_network]
- Quinate dehydrogenase (quiA) is a pyrroloquinoline quinone (PQQ)-dependent quinoprotein. This explains the dependence on the 2 PQQ biosynthesis genes, pqqC and pqqD. [src: aromatic_catabolism_network] See [[entities/pyrroloquinoline-quinone-biosynthesis]].

## Respiratory requirements on quinate

Quinate growth depends strongly on Complex I, even though it yields little reduced nicotinamide adenine dinucleotide (NADH) per carbon. [src: respiratory_chain_wiring]

- Complex I (NDH-1) has 13 subunits and pumps 4 H⁺/NADH. Its growth ratios are 0.37 on quinate (essential), 1.44 on glucose (dispensable) and 0.49 on acetate (defect). [src: respiratory_chain_wiring]
- Quinate gives 0.57 NADH per carbon atom, against 1.50 for glucose and 1.50 for acetate. Complex I is nonetheless more essential on quinate. [src: respiratory_chain_wiring]
- For quinate the report lists a total of 4 NADH, 0.57 NADH per carbon, and a concentrated TCA burst. [src: respiratory_chain_wiring]
- On quinate only Complex I is required. Cytochrome bo3, cytochrome bd, SDH and all other respiratory components are dispensable. [src: respiratory_chain_wiring]

Related pages: [[concepts/nadh-flux-rate-versus-nadh-yield-as-determinant-of-complex-i-dependence]], [[concepts/substrate-dependent-complex-i-requirement-and-ndh-2-compensation]], [[concepts/condition-dependent-respiratory-chain-configuration]], [[entities/respiratory-complex-i-nadh-ubiquinone-oxidoreductase]], [[entities/cytochrome-bo3-oxidase]].
