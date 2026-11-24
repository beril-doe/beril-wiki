---
type: "Concept"
description: "How genes whose growth importance concentrates on one condition recover known pathways and add annotation value; stops at the per-condition specificity analysis of a single deletion collection."
sources: ["summaries/adp1_deletion_phenotypes__REPORT.md", "summaries/aromatic_catabolism_network__REPORT.md", "summaries/discoveries.md", "summaries/fw300_metabolic_consistency__REPORT.md"]
---
# Condition-specific gene phenotypes and functional annotation yield

In the *Acinetobacter baylyi* ADP1 single-gene deletion collection, genes whose growth importance concentrates on one carbon source recover the expected pathways for that substrate. [src: adp1_deletion_phenotypes] They also add annotation value that a single-condition screen would miss. [src: adp1_deletion_phenotypes] The evidence comes from one organism and one deletion collection, with one supporting observation from a different organism, so it is direct but narrow. [src: adp1_deletion_phenotypes, fw300_metabolic_consistency] See [[entities/acinetobacter-baylyi-adp1]] and [[summaries/adp1_deletion_phenotypes__REPORT]].

## Literature Context

Two candidate papers describe the resource and the biology that the hub page builds on. The first built a collection of single-gene deletion mutants for all dispensable genes of *Acinetobacter baylyi* ADP1. It obtained 2594 deletion mutants. 499 (16%) could not be obtained and are therefore candidate essential genes for life on minimal medium [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/). The authors report that this essentiality data set is 88% consistent with the *Escherichia coli* data set inferred from the Keio collection. They also report that 80% of the orthologous genes described as essential in *Pseudomonas aeruginosa* are essential in ADP1 [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/). The same work phenotyped the mutant collection systematically on a variety of carbon sources, including quinate, 2-3 butanediol and glucose, and presented the collection as a resource for forward and reverse genetics [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/). The abstract does not give a count of condition-specific genes.

The second paper combined RNA-seq transcriptomics, LC/MS metabolomics and systematic phenotyping of the same deletion collection. It compared growth on succinate with growth on quinate. The shift to quinate caused a specific transcriptional response needed to catabolize the new substrate, and also a major reorganization of the transcription pattern. More than 12% of genes were affected, most of them of unknown function. About 50% of the LC/MS-detected metabolites changed in concentration. Many unidentified compounds were present only in quinate-grown cells. The authors concluded that ADP1 metabolism involves unsuspected enzymatic reactions that await discovery [PMID 25374488](https://pubmed.ncbi.nlm.nih.gov/25374488/). These are abstract-level findings from one organism.

The corpus finding that 625 genes (31%) have a condition specificity score ≥ 1.0 is consistent with this literature. It uses the same deletion collection and the same idea, that carbon-source-specific phenotypes expose metabolism [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/). The recovery of the expected quinate pathway genes (pca genes, qui genes and PQQ biosynthesis) agrees with the quinate-specific response seen in the multiomics study [PMID 25374488](https://pubmed.ncbi.nlm.nih.gov/25374488/). The corpus's quinate-specific set also includes Complex I subunits. Neither candidate abstract mentions this, so it extends the literature as a hypothesis about electron transport demands, not as an established result. The same is true of the corpus's co-fitness assignments of uncharacterized genes (for example the two DUF proteins as candidate Complex I accessory factors). The multiomics paper does support the view that many unannotated genes are involved in quinate metabolism [PMID 25374488](https://pubmed.ncbi.nlm.nih.gov/25374488/), which fits the hub's annotation-yield argument. Neither paper contradicts the corpus. The corpus's 31% figure, its two denominators, and the cross-species FW300-N2E3 comparison are not addressed by these candidates. Those claims stand on the corpus's own evidence. See [[entities/acinetobacter-baylyi-adp1]].

## How many genes are condition-specific

In ADP1, 625 genes (31%) have a condition specificity score ≥ 1.0, meaning their growth importance is concentrated on one carbon source. [src: adp1_deletion_phenotypes] The report gives 31% of the complete matrix and reads this as nearly one-third of the dispensable genome having condition-specific importance. [src: adp1_deletion_phenotypes] The central digest states the figure with a different denominator, 31% of dispensable genes. [src: discoveries] The sources do not show that the two denominators are equivalent, so each is stated as written. The digest also lists 625 condition-specific genes mapping to expected pathways. [src: discoveries]

## Recovery of expected pathways

The report states that the top condition-specific genes for each carbon source correspond precisely to the expected metabolic pathways. [src: adp1_deletion_phenotypes] The digest gives the same picture for urea, quinate, glucose, acetate and lactate. [src: discoveries] The table below lists the top genes per substrate.

| Carbon source | Top specific genes | Pathway |
|---|---|---|
| Quinate | pcaC, pcaG, pcaH, pcaB, quiA, quiB, pqqC, pqqD | Protocatechuate/quinate degradation and pyrroloquinoline quinone (PQQ) biosynthesis [src: adp1_deletion_phenotypes] |
| Urea | ureA, ureB, ureC, ureD, ureE, ureF, ureG | Urease complex, all 7 subunits and accessory proteins [src: adp1_deletion_phenotypes] |
| Asparagine | aspartate ammonia-lyase, L-asparaginase | Asparagine catabolism [src: adp1_deletion_phenotypes] |
| Acetate | fadB, malate synthase G, citB | Fatty acid β-oxidation and glyoxylate shunt [src: adp1_deletion_phenotypes] |
| Glucarate | gudD, D-glucarate transporter, 2,5-dioxovalerate dehydrogenase | Glucarate degradation [src: adp1_deletion_phenotypes] |
| Glucose | eda, gntT, gluconokinase, glucose dehydrogenase (PQQ) | Entner-Doudoroff pathway and PQQ-glucose dehydrogenase [src: adp1_deletion_phenotypes] |
| Butanediol | 2,3-butanediol dehydrogenase, E2 acetyltransferase | Butanediol catabolism and acetoin pathway [src: adp1_deletion_phenotypes] |
| Lactate | lldR, cyoC/cyoD | Lactate regulation and cytochrome oxidase [src: adp1_deletion_phenotypes] |

The quinate calls fit prior work. The report says they align with Fischer et al. (2008), who showed coordinated, carbon-source-dependent regulation of ADP1 aromatic degradation operons. [src: adp1_deletion_phenotypes]

## Beyond the core pathway

Specificity also reaches past the canonical enzymes. The quinate-specific set has 51 genes at spec > 0.5, z < -1. It includes Complex I NADH-ubiquinone oxidoreductase subunits, which the report takes to suggest that aromatic catabolism places unique demands on the electron transport chain. [src: adp1_deletion_phenotypes]

A related report used co-fitness, which correlates growth profiles, to place unclassified genes. Of 23 ADP1 genes first labelled Other or Unknown, 16 were assigned to support subsystems with medium or high confidence. [src: aromatic_catabolism_network] The method recovered pcaC, which keyword matching had miscategorized. [src: aromatic_catabolism_network] It also assigned 16 previously uncharacterized genes to subsystems, including two DUF proteins (ACIAD3137, ACIAD2176) as candidate Complex I accessory factors with r > 0.98. [src: aromatic_catabolism_network] See [[concepts/support-gene-networks-around-catabolic-pathways]] and [[entities/cofitness-analysis]].

## Annotation yield

The report says Wetmore et al. (2015) showed that RB-TnSeq (random barcode transposon sequencing) across diverse conditions identifies condition-specific gene functions. [src: adp1_deletion_phenotypes] It reaches the same conclusion with single-gene deletions instead of TnSeq (transposon sequencing): condition-specific phenotyping dramatically increases functional annotation yield. [src: adp1_deletion_phenotypes] The 625 genes include many with known functions that a single carbon source would not detect. [src: adp1_deletion_phenotypes]

A different organism gives a parallel observation. About 370 FW300-N2E3 genes were significant in only 1-2 conditions. The report calls these the truly substrate-specific genes, for example carnitine-specific transporters, lactate dehydrogenases and trehalose-specific phosphotransferases. [src: fw300_metabolic_consistency] Compare [[concepts/housekeeping-versus-substrate-specific-fitness-genes]].

## Caveats and proposed extensions

ADP1 growth ratios are single-timepoint measurements with unknown technical noise. The specificity analysis assumes that variation across conditions is biological, not measurement error. [src: adp1_deletion_phenotypes] The report proposes comparing ADP1 specificity profiles with Fitness Browser RB-TnSeq data for organisms grown on overlapping carbon sources such as glucose and lactate, to test whether the same pathways are condition-specific across species. [src: adp1_deletion_phenotypes] It also proposes inferring regulatory relationships from the condition-specific gene sets, since co-specific genes may share transcriptional regulators. [src: adp1_deletion_phenotypes]

## Open Directions

- Compare ADP1 specificity profiles with Fitness Browser RB-TnSeq data for organisms grown on glucose and lactate, to test cross-species pathway specificity.
- Use co-specific gene sets to infer shared regulators, and test the predictions against known regulons such as the quinate operons.
- Measure replicate variation in the growth ratios, to test the assumption that cross-condition variation is biological.
- Recompute the 31% figure against both denominators (complete matrix and dispensable genes), to show whether they agree.
- Compare the Complex I subunits in the quinate-specific set with other carbon sources. See [[concepts/substrate-dependent-complex-i-requirement-and-ndh-2-compensation]].
