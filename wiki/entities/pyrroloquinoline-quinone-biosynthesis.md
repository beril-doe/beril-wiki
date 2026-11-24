---
type: "Gene_Or_Pathway"
description: "PQQ cofactor biosynthesis genes (pqqA–E, including pqqC and pqqD) needed for PQQ-dependent dehydrogenases, and their use as phosphate-solubilization and phylogenetic markers."
sources: ["summaries/adp1_deletion_phenotypes__REPORT.md", "summaries/aromatic_catabolism_network__REPORT.md", "summaries/discoveries.md", "summaries/lanthanide_methylotrophy_atlas__REPORT.md", "summaries/pgp_pangenome_ecology__REPORT.md"]
aliases: ["PQQ", "pqqA-E", "pqqC", "pqqD", "pyrroloquinoline quinone biosynthesis protein C"]
---
# Pyrroloquinoline quinone biosynthesis

Pyrroloquinoline quinone (PQQ) biosynthesis genes (pqqA–E, including pqqC and pqqD) are the subject of this page. In the report, pqqC stands for phosphate solubilization through PQQ cofactor biosynthesis. [src: pgp_pangenome_ecology]

The evidence comes from three projects: growth phenotypes in [[entities/acinetobacter-baylyi-adp1]], PQQ annotation in xoxF-bearing genomes, and a pangenome survey of plant-growth-promoting (PGP) genes. [src: adp1_deletion_phenotypes, lanthanide_methylotrophy_atlas, pgp_pangenome_ecology]

## Key facts

- In ADP1, quinate dehydrogenase quiA is a PQQ-dependent quinoprotein, which explains the dependence on pqqC and pqqD. [src: aromatic_catabolism_network]
- PQQ-dependent quinate dehydrogenases are documented across aromatic-degrading bacteria. [src: aromatic_catabolism_network]
- pqqC was also used as a phylogenetic marker by Meyer et al. (2011). The pangenome report takes this to imply enough vertical inheritance for phylogenetic signal. [src: pgp_pangenome_ecology]

## Role in ADP1 catabolism

PQQ genes affect growth on both quinate and glucose in ADP1, so the dependency is not only aromatic. [src: adp1_deletion_phenotypes, aromatic_catabolism_network]

- The top quinate-specific genes include pcaC, pcaG, pcaH, pcaB, quiA, quiB, pqqC and pqqD. These cover protocatechuate/quinate degradation and PQQ biosynthesis. [src: adp1_deletion_phenotypes] See [[entities/quinate]] and [[entities/ketoadipate-pathway]].
- The top glucose-specific genes include eda, gntT, gluconokinase and PQQ-dependent glucose dehydrogenase. [src: adp1_deletion_phenotypes]
- The report reads this as PQQ-dependent dehydrogenases catalyzing the first step of both pathways. [src: adp1_deletion_phenotypes]
- The aromatic-network report lists 2 PQQ biosynthesis genes in the quinate-specific network. They supply the cofactor for quinoprotein quinate dehydrogenase. [src: aromatic_catabolism_network, discoveries]
- The aromatic-network report says it quantifies PQQ and iron dependencies at whole-genome level for the first time. [src: aromatic_catabolism_network]
- Stuani et al. (2014) reported 4/5 PQQ biosynthesis genes upregulated on quinate versus succinate in ADP1. The report says its quinate-specific growth phenotypes extend this transcriptomic observation to function. [src: aromatic_catabolism_network]
- The aromatic-network report notes that PQQ biosynthesis genes also appear glucose-specific in the adp1_deletion_phenotypes project. [src: aromatic_catabolism_network]

See [[concepts/support-gene-networks-around-catabolic-pathways]].

## PQQ in xoxF-bearing genomes

PQQ is described as an obligate cofactor of XoxF. [src: lanthanide_methylotrophy_atlas] The pilot found 2,320 xoxF-bearing genomes with no eggNOG PQQ-biosynthesis annotation. [src: lanthanide_methylotrophy_atlas]

| Category | Genomes | % of xoxF set |
|---|---|---|
| Complete eggNOG pqqA-E | 33 [src: lanthanide_methylotrophy_atlas] | 0.9 % [src: lanthanide_methylotrophy_atlas] |
| Partial eggNOG pqq (1–4 of A-E) | 1,472 [src: lanthanide_methylotrophy_atlas] | 39.9 % [src: lanthanide_methylotrophy_atlas] |
| Bakta-only strong (≥3 PQQ products) | 899 [src: lanthanide_methylotrophy_atlas] | 24.4 % [src: lanthanide_methylotrophy_atlas] |
| Bakta-only partial (1–2 PQQ products) | 389 [src: lanthanide_methylotrophy_atlas] | 10.5 % [src: lanthanide_methylotrophy_atlas] |
| No PQQ detected by either source | 897 [src: lanthanide_methylotrophy_atlas] | 24.3 % [src: lanthanide_methylotrophy_atlas] |

Of 2,185 genomes with no eggNOG pqq, 1,288 (59 %) have at least one bakta PQQ product. The report calls these annotation gaps. [src: lanthanide_methylotrophy_atlas] The 897 genomes lacking evidence from either source are candidates for assembly incompleteness, pseudogenization or reliance on community-acquired PQQ. Telling these apart needs sequence-level inspection, which the report left out of scope. [src: lanthanide_methylotrophy_atlas] The report also says bakta over-calls pqqA-E in the hit-bearing genome matrix, so it uses eggNOG as primary. [src: lanthanide_methylotrophy_atlas] See [[concepts/pqq-cofactor-biosynthesis-support-in-xoxf-bearing-genomes]] and [[concepts/annotation-source-disagreement-and-coverage]].

## Pangenome distribution and PGP associations

pqqD is the most widespread PGP gene, present in 11,040 species and 55.5% core. [src: pgp_pangenome_ecology] It is the most promiscuous pqq gene and is a single-gene orphan in many species lacking other pqq genes. [src: pgp_pangenome_ecology] Excluding pqqD, pqqC is the most prevalent focal trait, in 3,028 species (26.8% of species with any PGP gene). [src: pgp_pangenome_ecology]

| Gene | Core | Auxiliary | Singleton |
|---|---|---|---|
| pqqC | 81.5% [src: pgp_pangenome_ecology] | 7.8% [src: pgp_pangenome_ecology] | 10.7% [src: pgp_pangenome_ecology] |
| pqqB | 78.1% [src: pgp_pangenome_ecology] | 8.9% [src: pgp_pangenome_ecology] | 13.0% [src: pgp_pangenome_ecology] |
| pqqD | 55.5% [src: pgp_pangenome_ecology] | 17.0% [src: pgp_pangenome_ecology] | 27.5% [src: pgp_pangenome_ecology] |

pqqD is an outlier, with 55.5% core against 63–81% for other PGP genes. Its singleton fraction of 27.5% is the highest, which suggests occasional horizontal spread as a standalone gene. [src: pgp_pangenome_ecology] The functional pqqB–pqqC operon as a unit is predominantly core. [src: pgp_pangenome_ecology] See [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]].

Co-occurrence and environment:

- pqqC × acdS was the strongest positive focal PGP association (OR = 7.24, n = 286 co-occurring species, q = 1.2e-83). [src: pgp_pangenome_ecology, discoveries] See [[entities/acc-deaminase-acds]].
- The report identifies pqqC + acdS as a multi-trait genotype with n = 153. [src: pgp_pangenome_ecology]
- pqqC also co-occurred with hcnC (OR = 1.91) and ipdC (OR = 1.55). The report calls this a coherent "rhizosphere effectiveness" module. [src: pgp_pangenome_ecology] See [[entities/hcnc]].
- nifH was negatively associated with pqqC (OR = 0.57, q = 2.9e-19). [src: pgp_pangenome_ecology] See bacterial nitrogen fixation nif genes.
- pqqC prevalence was 43.8% in soil/rhizosphere species versus 21.2% elsewhere (OR 2.90, q 2.8e-53). [src: pgp_pangenome_ecology, discoveries] See [[concepts/environmental-enrichment-of-plant-growth-promoting-genes-in-soil-and-rhizosphere]] and [[concepts/co-occurrence-of-plant-growth-promoting-genes-and-trait-guilds]].
