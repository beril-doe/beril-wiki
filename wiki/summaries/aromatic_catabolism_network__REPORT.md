---
type: "Summary"
description: "Summary of the project Aromatic Catabolism Support Network in ADP1."
doc_type: "short"
full_text: "sources/aromatic_catabolism_network__REPORT.md"
---
# Aromatic Catabolism Support Network in ADP1

Complex I is the largest part of that network. [src: aromatic_catabolism_network] The evidence is co-fitness analysis in ADP1 plus an ortholog-transferred cross-species check from the Fitness Browser. [src: aromatic_catabolism_network] The report itself lists limits on both. [src: aromatic_catabolism_network]

## Key Findings

### Network structure

Co-fitness analysis assigns 44/51 genes (86%) to four subsystems plus regulators. [src: aromatic_catabolism_network] The report states that aromatic catabolism requires 51 genes, over 8× the core pathway. [src: aromatic_catabolism_network] It also states that the support requirement exceeds the pathway itself by 7:1. [src: aromatic_catabolism_network] These two ratios are given separately in the report, and the report does not reconcile them. The report claims the first whole-genome quantification of the PQQ (pyrroloquinoline quinone) and iron dependencies. [src: aromatic_catabolism_network]

| Subsystem | Genes | Role |
|---|---|---|
| Aromatic pathway | 8 | quinate → protocatechuate → β-ketoadipate → TCA (tricarboxylic acid) cycle [src: aromatic_catabolism_network] |
| Complex I | 21 | NADH (reduced nicotinamide adenine dinucleotide) reoxidation of excess NADH from the TCA cycle [src: aromatic_catabolism_network] |
| Iron acquisition | 7 | Fe²⁺ for protocatechuate 3,4-dioxygenase ring cleavage [src: aromatic_catabolism_network] |
| PQQ biosynthesis | 2 | cofactor for quinoprotein quinate dehydrogenase [src: aromatic_catabolism_network] |
| Regulation | 6 | control of aromatic degradation operons [src: aromatic_catabolism_network] |
| Unassigned | 7 | low co-fitness with all subsystems [src: aromatic_catabolism_network] |

Quinate catabolism runs through protocatechuate and β-ketoadipate to succinyl-CoA and acetyl-CoA, which enter the TCA cycle. [src: aromatic_catabolism_network] The report links each subsystem to a biochemical step:
- Quinate dehydrogenase quiA is a PQQ-dependent quinoprotein, which explains pqqC and pqqD. [src: aromatic_catabolism_network]
- Protocatechuate 3,4-dioxygenase pcaGH is a non-heme Fe²⁺ enzyme. This explains 7 iron genes: siderophore biosynthesis, ExbD/TolR transport, a ferrichrome receptor and a TonB-dependent receptor. [src: aromatic_catabolism_network]
- Full TCA oxidation of the succinyl-CoA and acetyl-CoA generates NADH at multiple steps, so high flux needs Complex I. [src: aromatic_catabolism_network]

The report describes the PQQ and iron dependencies as established biochemistry. [src: aromatic_catabolism_network] It also cites Stuani et al. (2014), who found 4/5 PQQ genes upregulated on quinate versus succinate. [src: aromatic_catabolism_network] The report says its quinate-specific PQQ growth phenotypes extend that observation to function. [src: aromatic_catabolism_network] The PQQ dependency is not exclusively aromatic. PQQ biosynthesis genes also appear glucose-specific in the adp1_deletion_phenotypes project, through PQQ-dependent glucose dehydrogenase. [src: aromatic_catabolism_network]

### Co-fitness validation

Within-category co-fitness is far higher than between-category co-fitness. Complex I has mean r = 0.992 and the aromatic pathway r = 0.961. [src: aromatic_catabolism_network] The report reads the Complex I value as essentially identical profiles, consistent with single-operon co-regulation. [src: aromatic_catabolism_network] Of 23 genes first labelled Other or Unknown, 16 were assigned to subsystems with medium or high confidence. [src: aromatic_catabolism_network] The method recovered pcaC, which keyword matching had miscategorized. [src: aromatic_catabolism_network] Two DUF proteins, ACIAD3137 (UPF0234) and ACIAD2176 (DUF2280), correlate at r > 0.98 with Complex I genes. [src: aromatic_catabolism_network] They are candidate accessory factors. [src: aromatic_catabolism_network] See [[entities/aciad3137-and-aciad2176]].

The 11 co-fitness assignments to Complex I beyond the core nuo operon rest on phenotypic correlation only. Some may be indirect connections rather than physical association with Complex I. [src: aromatic_catabolism_network]

### Complex I dominance

Complex I (NADH:ubiquinone oxidoreductase) accounts for 21 of 51 quinate-specific genes (41%). [src: aromatic_catabolism_network] Its operon has 13 subunits (nuoA–N), all on one strand with <100 bp intergenic distances. [src: aromatic_catabolism_network] Disrupting any subunit eliminates the whole complex. The report uses this to explain why 10/13 subunits independently give quinate-specific defects. [src: aromatic_catabolism_network]

### Genomic organization

The subsystems sit at distinct loci. Complex I is at 714–729 kb, pca/qui at 1,709–1,724 kb and PQQ biosynthesis at 2,461 kb. Iron genes are scattered across 4 loci. [src: aromatic_catabolism_network] The report states that no cross-category operons exist, except one within the aromatic pathway. [src: aromatic_catabolism_network] It attributes the coupling to ring-cleavage biochemistry, not co-localization. [src: aromatic_catabolism_network] Genes are tightly co-regulated within the 13-gene Complex I operon and the 12-gene pca/qui operon. [src: aromatic_catabolism_network] The operon predictions match Dal et al. (2005), including the 12-gene pca/qui operon spanning pcaIJFBDCHG-quiABC plus transport genes. [src: aromatic_catabolism_network]

### Flux balance model blind spot

The FBA (flux balance analysis) model predicts 1.76× higher Complex I flux on aromatics (0.55 vs 0.31). [src: aromatic_catabolism_network] It nonetheless predicts 0% Complex I essentiality. [src: aromatic_catabolism_network] The report says the model did not predict this support requirement, and that it had not been systematically documented. [src: aromatic_catabolism_network] Also, 30/51 genes have no FBA reaction mappings. [src: aromatic_catabolism_network] The report gives these reasons:
- FBA optimizes growth rate and can redistribute flux through alternative pathways. [src: aromatic_catabolism_network]
- Loss of any Complex I subunit creates a threshold effect that linear programming does not capture. [src: aromatic_catabolism_network]
- PQQ, iron, regulation and the new accessory factors lie outside the model's scope. [src: aromatic_catabolism_network]

It frames this as a class of model incompleteness: cofactor supply chains, iron homeostasis and respiratory-chain capacity constraints. [src: aromatic_catabolism_network] The report proposes that adding PQQ biosynthesis, iron homeostasis and respiratory-chain capacity constraints to the ADP1 FBA model could improve prediction of condition-dependent essentiality. [src: aromatic_catabolism_network] See [[concepts/systematic-blind-spots-of-flux-balance-models-for-condition-specific-requirements]].

### Cross-species: high-NADH substrates, not aromatics

The report concludes that Complex I dependency tracks high-NADH substrates, not aromatics specifically. [src: aromatic_catabolism_network] The data are ortholog-transferred Fitness Browser fitness: 12,241 entries, 2,005 genes and 13 conditions. [src: aromatic_catabolism_network] Complex I orthologs fare worse on aromatic conditions (mean = -1.35 vs -0.77, Mann-Whitney p < 0.0001). [src: aromatic_catabolism_network] Per condition, the largest Complex I defects relative to background are on acetate (-1.55) [src: aromatic_catabolism_network] and succinate (-1.39). [src: aromatic_catabolism_network] Both are non-aromatic substrates with high TCA NADH flux.

The report's cross-species data show Complex I dispensable on glucose and lactate, where NDH-2 suffices. [src: aromatic_catabolism_network] It is essential on aromatics, acetate and succinate. [src: aromatic_catabolism_network] Bacteria typically have branched respiratory chains with proton-pumping Complex I (NDH-1) and non-pumping NDH-2. [src: aromatic_catabolism_network] NDH-2 can substitute at low NADH flux but cannot match Complex I at high flux. [src: aromatic_catabolism_network] The report proposes that ADP1's apparent quinate-specificity reflects NDH-2 compensating on simpler substrates. [src: aromatic_catabolism_network] This is an interpretation, not a direct measurement. See [[concepts/substrate-dependent-complex-i-requirement-and-ndh-2-compensation]].

## Data and Methods

The report draws on a user-provided SQLite database, berdl_tables.db. Its tables genome_features, gene_phenotypes and gene_reaction_data supply growth ratios, FBA predictions across 230 conditions and gene-reaction mappings. [src: aromatic_catabolism_network] Ortholog-transferred fitness from kescience_fitnessbrowser, accessed via gene_phenotypes, supplies cross-species fitness on aromatic substrates. [src: aromatic_catabolism_network] Core and accessory annotations from kbase_ke_pangenome, accessed via genome_features, give conservation context. [src: aromatic_catabolism_network]

## Caveats and Open Work

- Those 8 conditions provide only ~5 independent dimensions. [src: aromatic_catabolism_network] More conditions would sharpen subsystem boundaries. [src: aromatic_catabolism_network]
- Ortholog-transferred fitness mixes organisms with different respiratory-chain architectures. Direct Complex I measurements on aromatic substrates in a single organism would be more definitive. [src: aromatic_catabolism_network]
- The Complex I co-fitness assignments beyond the nuo operon may be indirect. [src: aromatic_catabolism_network] The report proposes protein-protein interaction studies or Complex I co-purification to tell physical accessory factors from indirect regulatory connections. [src: aromatic_catabolism_network]
- The report proposes searching the ADP1 genome for NDH-2 genes. If present, their deletion phenotypes on quinate versus glucose would directly test whether NDH-2 compensates for Complex I on non-aromatic substrates. [src: aromatic_catabolism_network]
- The report proposes adding benzoate, catechol and vanillate, plus iron limitation and respiratory inhibitors. These would refine subsystem boundaries and test the NADH-flux hypothesis directly. [src: aromatic_catabolism_network]
- The report proposes using eggnog_mapper_annotations in the KBase Data Lakehouse to test whether Acinetobacter species carrying the pca pathway more often retain Complex I (KOs K00330–K00343) than species lacking aromatic degradation. [src: aromatic_catabolism_network]

## Slots Into

- [[concepts/support-gene-networks-around-catabolic-pathways]]: 51 quinate-specific genes organize into four subsystems around the pathway. [src: aromatic_catabolism_network]
- [[concepts/substrate-dependent-complex-i-requirement-and-ndh-2-compensation]]: Complex I defects are largest on acetate and succinate as well as aromatics. [src: aromatic_catabolism_network]
- [[concepts/systematic-blind-spots-of-flux-balance-models-for-condition-specific-requirements]]: the model sees Complex I flux but predicts 0% essentiality. [src: aromatic_catabolism_network]
- [[concepts/operon-organization-versus-functional-coupling-of-pathway-support-genes]]: coupling comes from biochemistry, not co-localization. [src: aromatic_catabolism_network]
