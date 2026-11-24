---
type: "Concept"
description: "How TnSeq essentiality relates to functional annotation (COG, KO), core-pangenome membership and growth medium; stops at causal explanations of conservation."
sources: ["summaries/acinetobacter_adp1_explorer__REPORT.md", "summaries/conservation_vs_fitness__REPORT.md", "summaries/discoveries.md", "summaries/essential_genome__REPORT.md"]
---
# Annotation and pangenome correlates of gene essentiality

This page covers how TnSeq (transposon sequencing) essentiality relates to functional annotation, core-pangenome membership and growth medium. Essential genes are better annotated [src: acinetobacter_adp1_explorer] and somewhat more often core [src: conservation_vs_fitness], but the core enrichment is modest. [src: essential_genome] Evidence comes from ADP1 (one organism) and from Fitness Browser analyses across many organisms. The page stops at describing these correlates and does not explain why conserved genes are essential. See also [[concepts/essential-genes-and-core-genome-conservation]].

## Literature Context

The candidate papers show that essentiality is usually studied together with conservation and annotation. A comparison of 17 essential gene sets from genome-wide in vitro screens, plus three gene collections required in vivo, covering 15 Bacteria and one Archaea, found that essential genes are typically more conserved than nonessential genes. Genes required in vivo were less conserved than those essential in vitro [PMID 26084810](https://pubmed.ncbi.nlm.nih.gov/26084810/). In 432 Pseudomonas strains, a large fraction of essential genes were highly persistent. Even so, non-essential genes made up a considerable fraction of the core genome [PMID 27922098](https://pubmed.ncbi.nlm.nih.gov/27922098/). In Mycobacterium abscessus, 326 of 4,920 annotated genes were essential. Of these, 269 (83%) have mutual homologs among essential M. tuberculosis genes, and 7 (2.1%) have no homologs in M. tuberculosis or M. avium [PMID 34126767](https://pubmed.ncbi.nlm.nih.gov/34126767/). Essential genes in respiratory pathogens were likewise treated as conserved, with 128 essential and conserved genes reported [PMID 25373505](https://pubmed.ncbi.nlm.nih.gov/25373505/).

On annotation, the papers describe a persistent pool of essential genes of unknown function. The JCVI-syn3A minimal cell model found 30 essential genes with unclear function. It also found 92% in vivo essentiality or quasi-essentiality (68% essential) among genes in the reconstruction [PMID 30657448](https://pubmed.ncbi.nlm.nih.gov/30657448/). Predicting function for such genes from TnSeq profiles across conditions is the aim of the MtbTnDB, which holds about 150 standardized screens. That work reports that genes with similar profiles are enriched in similar functional categories [PMID 40527579](https://pubmed.ncbi.nlm.nih.gov/40527579/). A caution for any essentiality-versus-annotation analysis is that overlapping open reading frames can inherit a neighbour's essentiality signal. The Rv2438A audit examined one such case in M. tuberculosis [PMID 42754103](https://pubmed.ncbi.nlm.nih.gov/42754103/). Medium and condition also matter, and databases such as DEG 10 record essential elements under diverse conditions [PMID 24243843](https://pubmed.ncbi.nlm.nih.gov/24243843/).

The hub's claim that essential genes are somewhat more often core is consistent with this literature. The Fitness Browser figures are 86.1% core for essential genes versus 81.2% for non-essential genes. Its modest enrichment, and the weak penetrance-versus-core correlation (rho=0.123), fit the Pseudomonas observation that many non-essential genes are also core [PMID 27922098](https://pubmed.ncbi.nlm.nih.gov/27922098/). The finding that universally essential genes are only 8.2% hypothetical, while orphan essential genes are 58.7% hypothetical, matches the picture of a well-characterized conserved backbone. It also matches the unexplained strain-specific remainder, such as the few M. abscessus essentials lacking homologs [PMID 34126767](https://pubmed.ncbi.nlm.nih.gov/34126767/). The ADP1 contrast of 499 genes essential on minimal medium versus 346 on LB extends the in vitro versus in vivo condition dependence described in [PMID 26084810](https://pubmed.ncbi.nlm.nih.gov/26084810/). That paper compared in vitro with in vivo requirements, not two media. The COG and KO annotation percentages, and the SEED category enrichments, have no direct counterpart in these candidates and so are novel here. The papers also give no causal explanation of why conserved genes are essential, so the hub's decision to stop at correlates is appropriate.

## Annotation correlates

Essential genes carry more annotation than dispensable ones in ADP1. The ADP1 database has TnSeq essentiality coverage of 58%. [src: acinetobacter_adp1_explorer] In ADP1, 33% of essential genes have COG (clusters of orthologous groups) assignments versus 5% of dispensable genes. [src: acinetobacter_adp1_explorer] Also, 92% of essential genes have KO (KEGG ortholog) assignments versus 53% of dispensable genes. [src: acinetobacter_adp1_explorer] The report expects this, since essential genes tend to encode housekeeping functions. It proposes that the ~8% of essential genes without KO are potential novel essential functions. [src: acinetobacter_adp1_explorer]

In the conservation_vs_fitness analysis, annotation depends on the conservation category, as the table shows. [src: conservation_vs_fitness]

| Category | Genes | Enzymes | Hypothetical | Claim |
|---|---|---|---|---|
| Essential-core | 22,751 | 41.9% | 13.0% | [src: conservation_vs_fitness] |
| Essential-auxiliary | 3,683 | 13.4% | 38.2% | [src: conservation_vs_fitness] |
| Essential-unmapped | 1,259 | 18.2% | 44.7% | [src: conservation_vs_fitness] |
| Non-essential | 124,744 | 21.5% | 24.5% | [src: conservation_vs_fitness] |

Essential-core genes are the most enzyme-rich and best annotated, with 87% having known function. [src: conservation_vs_fitness] The discoveries digest describes them as a well-characterized backbone of ribosomes, DNA (deoxyribonucleic acid) replication, cell wall and cofactor biosynthesis. [src: discoveries] Essential-auxiliary genes, essential but absent from some strains, are 13.4% enzymes and 38.2% hypothetical. [src: discoveries] Essential-unmapped genes are strain-specific essentials with no pangenome cluster match, and they are the least characterized category. [src: conservation_vs_fitness] The digest flags them as targets for functional discovery. [src: discoveries]

In the essential_genome analysis, universally essential genes are only 8.2% hypothetical. [src: essential_genome] Orphan essential genes are 58.7% hypothetical, the highest uncharacterized fraction of any category. [src: essential_genome] See [[concepts/annotation-coverage-and-annotation-density-bias-in-functional-enrichment]] for the bias this annotation gradient can introduce.

## Functional categories of essential-core genes

Relative to non-essential genes, essential-core genes are enriched in Protein Metabolism (+13.7 percentage points), Cofactors/Vitamins (+6.2%), Cell Wall (+3.9%) and Fatty Acid biosynthesis (+3.1%). [src: conservation_vs_fitness] The discoveries digest repeats the first three as SEED-category enrichments (+13.7, +6.2 and +3.9 pp). [src: discoveries] They are depleted in Carbohydrates (-7.9%), Amino Acids (-5.6%) and Membrane Transport (-4.0%). [src: conservation_vs_fitness] The reports describe these as functions that tend to be conditionally important rather than universally essential. [src: conservation_vs_fitness, discoveries] The digest cites Rosconi et al. (2022), who found that pan-genome composition influences essentiality in S. pneumoniae. [src: discoveries] See [[entities/seed-subsystems]].

Essential-auxiliary genes show a different pattern. Their top subsystems are ribosomes, DNA replication, type 4 secretion and plasmid replication. The report suggests this reflects strain-specific variants of core machinery plus mobile genetic elements. [src: conservation_vs_fitness]

## Core-pangenome membership

Essential genes are more often core, but the effect is small. In the Fitness Browser conservation analysis, essential genes are 86.1% core versus 81.2% for non-essential genes. [src: conservation_vs_fitness] The median odds ratio for essential genes being core is 1.56. [src: conservation_vs_fitness] In ADP1, essential genes are also more likely to be core, consistent with conserved genes tending to be essential. [src: acinetobacter_adp1_explorer]

The essential_genome analysis reports a gradient. Universally essential genes are 91.7% core versus 80.7% for non-essential genes. [src: essential_genome] Its hierarchy table gives core fractions by category:

| Category | % core | Genes | Claim |
|---|---|---|---|
| Universally essential | 91.7% | 6,963 | [src: essential_genome] |
| Variably essential | 88.9% | 90,844 | [src: essential_genome] |
| Never essential | 81.7% | 47,140 | [src: essential_genome] |
| Orphan essential | 49.5% | 4,683 | [src: essential_genome] |

In that report, 71% of universally essential families are 100% core across all genomes in their species. [src: essential_genome] Essentiality penetrance and core fraction correlate only weakly (rho=0.123, p=1.6e-17). [src: essential_genome] Core fraction is 97.1% for families with >80% penetrance versus 92.8% for <20%. [src: essential_genome] See [[concepts/gene-fitness-importance-as-a-predictor-of-pangenome-conservation]].

## Growth medium

Essentiality depends on the medium. In ADP1, 499 genes are essential on minimal medium versus 346 on LB. The report attributes the difference to the additional biosynthetic burden of minimal medium. [src: acinetobacter_adp1_explorer] The ADP1 database supplies TnSeq-based essentiality calls on both media, a data type not available elsewhere in the KBase Data Lakehouse. [src: acinetobacter_adp1_explorer] See adp1 sqlite database berdl tables db.

## Tensions

- The 86.1% versus 81.2% core fractions and the weak penetrance correlation show modest core enrichment. [src: conservation_vs_fitness, essential_genome]
- For essential-auxiliary genes only, the report links the top subsystems to strain-specific variants of core machinery and mobile genetic elements. [src: conservation_vs_fitness] For essential-unmapped genes, the claims say only that they are strain-specific and the least characterized. [src: conservation_vs_fitness]

## Open Directions

- Compare ADP1 minimal-medium-only essentials (499 versus 346 on LB) against core membership, to test whether condition-dependent essentials are less conserved.
- Test whether the Protein Metabolism enrichment survives after controlling for annotation density, since essential genes are better annotated.
- Characterize the ~8% of ADP1 essential genes without KO, and the essential-unmapped genes, by ortholog transfer or guilt-by-association (see [[concepts/function-prediction-for-uncharacterized-genes-by-guilt-by-association-and-ortholog-transfer]]).
- Repeat the penetrance versus core-fraction test with a definition that separates mobile-element essentials from core-machinery variants.
