---
type: "Concept"
description: "How cofitness modules from transposon fitness data are built, annotated and used to predict function, how essential genes are shared across bacteria, and how per-condition phenotypes behave in one model organism; stops at conservation analyses."
sources: ["summaries/discoveries.md"]
---
# Fitness modules, essential genes and condition-specific gene function

This page covers fitness modules, essential genes and condition-specific gene function, with Acinetobacter baylyi ADP1 ([[entities/acinetobacter-baylyi-adp1]]) as the model organism. All evidence comes from the central discoveries digest ([[summaries/discoveries]]). Robust ICA (independent component analysis) finds 17-52 stable modules per organism across 32 bacteria. [src: discoveries] Modules capture process-level co-regulation, not specific molecular function, and they contain no essential genes. [src: discoveries] A separate cross-organism analysis of 48 bacteria finds a small universal essential core. [src: discoveries] The condition-specific results come from one organism, ADP1, and the cross-species NDH-2 test is a null result. [src: discoveries]

## Literature Context

Only one of the two candidate papers bears on this page. [PMID 41979344](https://pubmed.ncbi.nlm.nih.gov/41979344/) is a transposon mutagenesis study in Escherichia coli BW25113. It sequenced mutant populations at multiple time points in three growth media. It reports a core set of 412 genes with high fitness impact across all conditions, plus distinct medium-specific gene sets. A sliding-window analysis of read counts over time found further genes whose inactivation has an appreciable but lower fitness impact. The authors combined these sets into medium-specific gene modules. They conclude that essentiality is context dependent and not binary, and that it should be described as a condition-specific framework and not a universal list. The evidence is an abstract only, from one strain and three media.

The other candidate, [PMID 17350973](https://pubmed.ncbi.nlm.nih.gov/17350973/), learns microRNA-mRNA modules from human cancer expression data. It concerns a different kind of data and organism, and it says nothing about bacterial fitness, essentiality or cofitness. I do not use it as evidence for this page. The word "module" is the only link.

The corpus's findings are consistent with [PMID 41979344](https://pubmed.ncbi.nlm.nih.gov/41979344/) in two ways. First, the corpus reports a small universal essential core: 15 families essential in every one of 48 bacteria. It also reports that 4,799 families (27.9%) are variably essential. Together these fit the view that essentiality depends on context. The E. coli study's 412 core genes come from one strain and are not directly comparable. Second, the corpus finds that ADP1 gene requirements vary continuously across 8 carbon sources. This matches the claim that fitness contributions are graded and condition-dependent. The ADP1 result is a single-organism finding, so it supports the E. coli observation and does not independently confirm it.

The corpus extends that paper in several ways. It builds modules by robust ICA across 32 organisms, not by assembling medium-specific gene lists. It finds that the modules contain 0 essential genes. It also transfers module context from non-essential orthologs to hypothetical essential genes, giving 1,382 predictions that have no direct validation. The candidate literature has nothing to compare against these claims, including module families, annotation enrichment, the quinate support network and the null cross-species NDH-2 test. They remain novel relative to the retrieved papers. The E. coli study defines modules differently, as sets of essential and fitness-contributing genes per medium. Its modules therefore include the essential genes that the corpus's ICA modules exclude by construction, and the two uses of the term should not be conflated.

## Building fitness modules

Robust ICA gives stable, operon-like modules once membership is thresholded sensibly. It uses 30-50 FastICA runs plus DBSCAN clustering. [src: discoveries] See [[entities/independent-component-analysis-fitness-modules]] and [[concepts/construction-and-validity-of-cofitness-gene-groups]].

- 94.2% of modules show significantly elevated within-module cofitness (Mann-Whitney U, p < 0.05; mean |r| = 0.34 vs background 0.12). [src: discoveries]
- Genomic adjacency enrichment averages 22.7× across organisms, which the report takes as confirmation that modules capture operon-like co-regulated gene groups. [src: discoveries]

The first membership rule failed. D'Agostino K² normality-based thresholding gave 100-280 genes per module, which the report calls biologically meaningless. [src: discoveries] The report attributes the problem to deciding which genes belong to a module, not to the ICA components. [src: discoveries] Switching to |Pearson r| ≥ 0.3 with the module profile and a maximum of 50 genes reduced modules to 5-50 genes. [src: discoveries] Cofitness enrichment rose from 59% to 94.2%. [src: discoveries] Within-module |r| rose from 0.047 to 0.34 (mean across 32 organisms). [src: discoveries]

Data size matters less than expected. Caulo, with 198 experiments, had the weakest pilot signal (2.9x correlation enrichment vs 31x for DvH). [src: discoveries] Even so, Ponti produced stable modules with 104 experiments. [src: discoveries] The report recommends capping ICA components at 40% of experiments, because higher ratios cause FastICA convergence failures and extreme slowness. [src: discoveries]

## Cross-organism module families

Aligning modules with BBH (bidirectional best hit) ortholog fingerprints revealed 156 module families spanning 2+ organisms. [src: discoveries] The largest spans 21 of 32 organisms across Proteobacteria, Bacteroidetes, Firmicutes and Archaea, which the report reads as evidence of deeply conserved fitness regulons. [src: discoveries] 28 families span 5+ organisms. [src: discoveries] See [[concepts/conservation-of-cofitness-modules-across-genomes-and-organisms]].

Ortholog scope changed the result sharply. The comparison used BBH pairs from 5 organisms (10K pairs, 1,861 OGs, ortholog groups) versus all 32 organisms (1.15M pairs, 13,402 OGs). [src: discoveries] The 5-organism run found just 27 families, none spanning more than 4 organisms. [src: discoveries] Using all organisms changed module families from 27 to 156 (6x), families spanning 5+ organisms from 0 to 28, and family-backed predictions from 31 (4%) to 493 (56%). [src: discoveries] The report's lesson is to extract orthologs for all organisms, because the ortholog graph is not additive and new organisms create transitive connections. [src: discoveries] See [[entities/bidirectional-best-blast-hit-orthology]].

## Annotating modules and predicting function

Module annotation depended on the choice of annotation database and threshold. The initial pipeline (KEGG + SEED + TIGRFam, min_annotated=3) annotated only 8.2% of modules (92/1,116). [src: discoveries] The report attributes this to KEGG KO (KEGG ortholog) groups averaging ~1.2 genes per term, so modules of 5-50 members almost never have 3+ genes sharing a KO. [src: discoveries] Adding PFam domains (814 terms with 2+ genes vs TIGRFam's 88) and lowering the overlap threshold to 2 raised annotation to 79.7% (890/1,116). [src: discoveries] PFam is the dominant source, because its domain-level labels match module granularity. [src: discoveries] See [[entities/pfam-domain-annotations]] and [[concepts/annotation-coverage-and-resolution-in-genome-wide-cofitness-analysis]].

The improvements increased predictions from 878 to 6,691 (7.6×), now covering all 32 organisms. [src: discoveries] Annotated families rose from 32 to 145 out of 156 (93%). [src: discoveries] Three organisms (Caulo, Methanococcus_S2, Korea) went from 0 enrichments to 24-29 enriched modules. [src: discoveries]

The min_annotated parameter is the minimum number of overlapping genes to test, and it must be calibrated to annotation granularity. [src: discoveries] For gene-specific KOs (~1 gene/term), min_annotated=3 eliminates nearly all tests. [src: discoveries] For domain-level PFam annotations, min_annotated=2 works well with FDR (false discovery rate) correction. [src: discoveries] The report says Fisher's exact test handles small counts correctly, and validity comes from FDR correction across all tests, not from large overlaps. [src: discoveries]

### What modules predict

A held-out KO prediction benchmark across 32 organisms found ortholog transfer dominant for gene-level prediction (95.8% precision, 91.2% coverage). [src: discoveries] Module-ICA had <1% precision at the KO level. [src: discoveries] The report calls this expected: modules capture process-level co-regulation (94.2% cofitness enrichment, 22.7× adjacency enrichment), not specific molecular function. [src: discoveries] An ABC (ATP-binding cassette) transporter module groups binding, permease and ATPase subunits that each have a different KO. The report therefore frames module predictions as "involved in [biological process]", not "has function [specific KO]". [src: discoveries] See [[concepts/function-prediction-for-uncharacterized-genes-by-guilt-by-association-and-ortholog-transfer]].

## Essential genes across bacteria

Modules cannot see essential genes. 0 essential genes appear in any of the 1,116 fitness modules across 32 organisms. [src: discoveries] ICA decomposes fitness variation, so genes without transposon insertions have no fitness data, and modules capture only the non-essential part of the genome's functional architecture. [src: discoveries] See [[concepts/essential-genes-as-a-blind-spot-of-transposon-fitness-screens]].

The essential_genome analysis covers 48 diverse bacteria, 221,005 genes and 17,222 ortholog families. [src: discoveries] Fifteen families are essential in every organism: ribosomal proteins (rpsC, rplW, rplK, rplB, rplA, rplF, rps11, rpsJ, rpsI, rpsM), groEL, pyrG, fusA, valS and SelGGPS. [src: discoveries] The report calls these the irreducible essential core of bacterial life. [src: discoveries] See [[entities/ribosomal-protein-families]].

Under a looser definition, 859 families (5.0%) are essential in every organism where the family has members. [src: discoveries] 4,799 families (27.9%) are variably essential, and 11,564 (67.1%) are never essential. [src: discoveries] The report reads variable essentiality as showing that genomic context profoundly shapes viability requirements. [src: discoveries] See [[concepts/universal-versus-variable-gene-essentiality-across-bacteria]] and [[concepts/essential-genes-and-core-genome-conservation]].

### Orphan essentials and conservation

7,084 essential genes have no orthologs in any other FB (Fitness Browser) organism. [src: discoveries] Of these, 58.7% are annotated as hypothetical proteins, against 8.2% for universally essential genes. [src: discoveries] The report calls the orphans prime candidates for novel biology. [src: discoveries] Universally essential genes are 91.7% core vs 80.7% for non-essential genes. [src: discoveries] 71% of universally essential families are 100% core across all genomes in their species. [src: discoveries] Orphan essentials are only 49.5% core, which the report describes as strain-specific essential functions not conserved across species. [src: discoveries]

### Transferring module function to essential genes

Non-essential orthologs that sit in ICA modules gave 1,382 function predictions for hypothetical essential genes across 48 organisms. [src: discoveries] All of these predictions are backed by cross-organism module family conservation. [src: discoveries] The report concludes that module context from non-essential orthologs can illuminate essential genes that fitness-based methods cannot see. [src: discoveries]

## Condition-specific phenotypes in ADP1

Condition-specific genes in ADP1 map to the expected biochemistry. The deletion-phenotype report identifies 625 such genes. [src: discoveries] 31% of dispensable genes have condition-specificity scores ≥ 1.0. [src: discoveries] The top genes per carbon source are the enzymes biochemically predicted to be required:
- urease subunits for urea [src: discoveries]
- protocatechuate 3,4-dioxygenase for quinate [src: discoveries]
- Entner-Doudoroff enzymes for glucose [src: discoveries]
- the glyoxylate shunt for acetate [src: discoveries]
- a lactate-responsive regulator for lactate [src: discoveries]

See [[concepts/condition-specific-gene-phenotypes-and-functional-annotation-yield]].

### Continuous rather than modular structure

Clustering 2,034 genes by 8-condition growth profiles gives an optimal K=3 with silhouette=0.24, which the report reads as no discrete functional modules overall. [src: discoveries] The landscape is a gradient with one exception: 24 genes form a tight quinate-specific aromatic-degradation module. [src: discoveries] Essentiality varies continuously across conditions, which the report says supports the Guzman et al. (2018) "adaptive flexibility" framework. [src: discoveries] See [[concepts/continuous-versus-discrete-structure-of-condition-dependent-gene-essentiality]].

### Quinate support genes

Quinate needs 51 genes with quinate-specific growth defects, although the β-ketoadipate pathway has 8 core genes. The report calls this a 7:1 support-to-pathway ratio. [src: discoveries] The support genes fall into three subsystems: Complex I (21 genes, NADH reoxidation), iron acquisition (7 genes, Fe²⁺ for ring-cleavage dioxygenase) and PQQ (pyrroloquinoline quinone) biosynthesis (2 genes, cofactor for quinate dehydrogenase). [src: discoveries] The report reads the aromatic support network as a high-NADH-flux bottleneck network, not an aromatic-chemistry-specific one. [src: discoveries] See [[concepts/support-gene-networks-around-catabolic-pathways]].

### Respiratory-chain requirements

Each of ADP1's 8 carbon sources needs a distinct set of respiratory-chain components. [src: discoveries] The report calls this qualitatively different wiring per substrate class, not a quantitative gradient. [src: discoveries] See [[concepts/condition-dependent-respiratory-chain-configuration]].
- Quinate requires only Complex I, and all other components are dispensable. [src: discoveries]
- Acetate is the most demanding source. It requires Complex I, cytochrome bo3, ACIAD3522 and more. [src: discoveries]
- Glucose requires no specific component, because of full redundancy. [src: discoveries]

The complexes differ as follows:
- Complex I has 13 subunits and is proton-pumping. It is quinate-essential and glucose-dispensable. [src: discoveries]
- NDH-2 has 1 subunit and is non-pumping. It has no growth data and is only predicted to back up glucose. [src: discoveries]
- ACIAD3522 is an NADH-FMN oxidoreductase. It is acetate-lethal (0.013) and quinate-fine (1.39). [src: discoveries]

The report describes this as division of labor, with each enzyme handling a different metabolic regime. [src: discoveries]

### NADH flux explanation

Quinate yields fewer NADH (reduced nicotinamide adenine dinucleotide) per carbon (0.57) than glucose (1.50), yet Complex I is more essential on quinate. [src: discoveries] The report resolves this by proposing that β-ketoadipate pathway products (succinyl-CoA and acetyl-CoA) enter the tricarboxylic acid (TCA) cycle simultaneously. That creates an NADH burst beyond NDH-2's reoxidation capacity. [src: discoveries] Glucose spreads NADH across Entner-Doudoroff and TCA steps, where NDH-2 suffices. [src: discoveries] See [[concepts/nadh-flux-rate-versus-nadh-yield-as-determinant-of-complex-i-dependence]].

Proteomics under standard conditions shows similar expression of the three NADH dehydrogenases. They sit within 1.4 units of each other around the genome median (26.4). [src: discoveries]
- Complex I mean: 27.6 (66th percentile). [src: discoveries]
- NDH-2: 27.0 (59th percentile). [src: discoveries]
- ACIAD3522: 26.2 (48th percentile). [src: discoveries]

The report concludes that ADP1 does not switch configurations by regulating dehydrogenase expression. All three run at once, and the limiting one depends on the NADH flux from the carbon source. [src: discoveries] It calls this a passive, flux-based system, not an active regulatory switch. [src: discoveries]

### NDH-2 compensation across species

The aromatic_catabolism_network report hypothesized that ADP1's quinate specificity reflects NDH-2 compensation on lower-NADH-flux substrates. [src: discoveries] A cross-species test did not support this. The initial result, with 10/14 organisms identified as having NDH-2, was driven by misannotated Complex I subunits passing the text filter in 5 organisms. [src: discoveries] After restricting candidates to organisms with ≤2 hits per genome, organisms with validated NDH-2 had larger Complex I aromatic deficits (mean -0.297) than those without (-0.156, p=0.52). That does not support compensation. [src: discoveries] Separately, ortholog-transferred fitness data show Complex I defects are largest on acetate (-1.55 vs background) and succinate (-1.39), not aromatics. [src: discoveries] See [[concepts/ndh-2-compensation-for-complex-i-loss-across-species]] and [[concepts/substrate-dependent-complex-i-requirement-and-ndh-2-compensation]].

### Unannotated genes with strong phenotypes

ACIAD3522 has a growth ratio of 0.013 on acetate, essentially lethal, with no defect on quinate (1.39) or glucose (1.39). [src: discoveries] This is the largest condition-specific effect of any single gene in the 2,034-gene growth matrix. [src: discoveries] Its biological role is unknown. The report suggests the extreme acetate specificity points to an NADH-linked reaction uniquely required for acetate catabolism. [src: discoveries] See [[entities/aciad3522]].

ACIAD3137 (UPF0234/YitK) and ACIAD2176 (DUF2280) correlate at r > 0.98 with Complex I genes across 8 growth conditions. [src: discoveries] Both lack FBA (flux balance analysis) reaction mappings and have no assigned metabolic function. [src: discoveries] The report suggests the near-perfect cofitness with the nuo operon points to physical or regulatory association with Complex I. [src: discoveries] See [[entities/aciad3137-and-aciad2176]].

## Limits of metabolic models

Flux balance analysis misses much of this biology. Of the 51 quinate-specific genes, 30 (59%) have no FBA reaction mappings. These include PQQ biosynthesis, iron acquisition, transcriptional regulators and respiratory-chain components. [src: discoveries] For Complex I, FBA predicts 1.76× higher flux on aromatics but 0% essentiality. [src: discoveries] The report says FBA's linear programming cannot represent the threshold effect of losing one subunit of a multi-subunit complex. [src: discoveries] FBA predicts zero flux through ACIAD3522 on all conditions. [src: discoveries] See [[concepts/systematic-blind-spots-of-flux-balance-models-for-condition-specific-requirements]].

## Coverage bias in the deletion collection

Of 2,593 TnSeq-dispensable genes, 272 (10.5%) lack deletion-collection growth data. [src: discoveries] Those genes differ systematically from represented ones:
- They are shorter (813 vs 981 bp). [src: discoveries]
- They are less annotated (91% vs 100% RAST). [src: discoveries]
- They are less conserved in the pangenome (76.5% core vs 93.3%, p=1.4e-20). [src: discoveries]
- Hypothetical proteins are massively enriched (q=2.4e-25). [src: discoveries]

The report concludes that the deletion collection is biased toward well-characterized, conserved genes. [src: discoveries] See [[concepts/coverage-gaps-in-deletion-collections-and-their-link-to-pangenome-conservation]].

## Open Directions

- Measure NDH-2 mutant growth on glucose and acetate in ADP1. This would replace the prediction with data (the gap in the NDH-2 claim).
- Test whether ACIAD3137 and ACIAD2176 physically interact with Complex I, for example by co-purification, to follow up on their cofitness.
- Rerun the cross-species NDH-2 test with sequence-validated NDH-2 calls, such as profile-based ones, to check the null result against the earlier misannotation problem.
- Profile ACIAD3522 on more acetate-related and NADH-linked conditions to narrow its unknown reaction.
- Add respiratory-chain and cofactor reactions to the FBA model, then test whether threshold effects can be captured.
- Test whether the 1,382 module-transfer predictions for hypothetical essential genes hold up, for example by conditional knockdowns, to check a result that has no direct validation here.
- Rebuild module families with ortholog graphs from additional organisms, to see whether the 156 families keep growing as the graph densifies.
