---
type: "Concept"
description: "Measurement and classification limits (essential-gene censoring, keyword-based AMR identification, polar effects, relative fitness) on inferring resistance gene costs from RB-TnSeq data."
sources: ["summaries/amr_fitness_cost__REPORT.md", "summaries/amr_pangenome_atlas__REPORT.md", "summaries/discoveries.md"]
---
# Essentiality and annotation caveats in transposon-based resistance gene fitness analysis

This page covers the measurement and classification limits on inferring resistance gene costs from random barcode transposon sequencing (RB-TnSeq) data. In the amr_fitness_cost report, the keyword-identification concern was checked and mostly mitigated. [src: amr_fitness_cost] Essential-gene censoring was argued to be small. [src: amr_fitness_cost] Polar effects and the environmental bias of the organisms remain unresolved. [src: amr_fitness_cost, amr_pangenome_atlas] See [[concepts/fitness-cost-of-antimicrobial-resistance-genes]] for the main result and [[concepts/limits-of-transposon-based-essentiality-calls]] for the general essentiality issue.

## Literature Context

The candidate papers say little about the measurement limits this page discusses: essential-gene censoring, keyword-based annotation, polar effects and relative fitness. They do bear on the biological question the page addresses, which is whether resistance genes carry a fitness cost. They give a mixed picture, and most of them study acquired resistance in pathogens.

Several papers report that acquired resistance elements carry a cost that is small or context-dependent. Tet(X3) and Tet(X4) tigecycline-resistance genes on conjugative plasmids conferred "a mild fitness cost (relative fitness of >0.704)" [PMID 31133751](https://pubmed.ncbi.nlm.nih.gov/31133751/). IncN plasmids carrying blaIMP-4 in nine carbapenem-resistant E. coli isolates showed minimal fitness cost [PMID 41347505](https://pubmed.ncbi.nlm.nih.gov/41347505/). Carriage of an inactivated or inducible Tn1549 had no cost in enterococci when vancomycin induction was absent. Induced or constitutively resistant strains were impaired, so tight regulation of expression removed the cost [PMID 20833818](https://pubmed.ncbi.nlm.nih.gov/20833818/). The cost of phage-defense integron cassettes varied with genetic context and cassette order [PMID 40338999](https://pubmed.ncbi.nlm.nih.gov/40338999/). In contrast, uptake of the Tn7100 integrative conjugative element reduced fitness in Haemophilus influenzae in head-to-head competition [PMID 35935209](https://pubmed.ncbi.nlm.nih.gov/35935209/). Insertion sequences can lower a plasmid's cost by disrupting a gene that is harmful to the host, in experimental evolution of pB1000 in E. coli [PMID 37097157](https://pubmed.ncbi.nlm.nih.gov/37097157/). Reviews state that mobile element acquisition produces a cost that compensatory mutations can ease [PMID 31492517](https://pubmed.ncbi.nlm.nih.gov/31492517/). They also note that the idea that resistance is usually costly may not be as solid as thought, since resistance can enhance in vivo fitness [PMID 27248008](https://pubmed.ncbi.nlm.nih.gov/27248008/).

Two papers relate more directly to the methods. A genome-wide transposon-sequencing analysis of a rifampicin-resistant rpoB H526Y mutant found that some genes compound the cost of resistance and others mitigate it [PMID 34697460](https://pubmed.ncbi.nlm.nih.gov/34697460/). That is a different design from the corpus's knockouts of resistance genes, but it shows how Tn-seq can resolve cost. A CRISPRi-seq study in H. influenzae refined earlier Tn-seq essentiality calls and found growth-medium-dependent fitness costs [PMID 41171899](https://pubmed.ncbi.nlm.nih.gov/41171899/). This is consistent with the hub's caution that transposon essentiality calls are imperfect. It does not test the 4.6% figure for putatively essential AMR genes.

The corpus's main result is a small positive effect of +0.086, the difference between AMR knockout fitness (−0.024) and non-AMR knockout fitness (~−0.11). It is consistent in direction with the literature on low or regulated costs, and it extends that work to environmental organisms. The literature here is almost all on acquired elements in clinical or host-associated bacteria, so it does not settle the hub's caveat that the 37/48 organisms with AMR genes are mostly environmental strains. The Tn7100 result shows that costs can be real for acquired elements in a pathogen, which fits the hub's warning that recently acquired mobile resistance may differ. Nothing in the candidates addresses keyword-based identification or polar effects, so those caveats remain unresolved and are neither supported nor contradicted by this literature.

## Essential-gene censoring

Genes that cannot be knocked out are absent from fitness matrices, so their costs cannot be seen. About 4.6% of antimicrobial resistance (AMR) genes are putatively essential because they are absent from the fitness matrices. If these are the most costly AMR genes, the +0.086 estimate would be a lower bound. [src: amr_fitness_cost]

The 4.6% is substantially lower than the ~14% background essential rate from a prior analysis (fitness_effects_conservation) that used a different organism set. [src: amr_fitness_cost] The report reads this as consistent with resistance genes being more dispensable. It also reads it as arguing against strong right-censoring bias. [src: amr_fitness_cost] The two rates come from different organism sets, so this is an interpretation and not a matched test. [src: amr_fitness_cost]

## Keyword-based AMR identification

Most AMR genes come from keyword matching, so some may not be AMR genes. The report uses [[entities/bakta-amr]] for Tier 1 identification and keyword annotation for Tier 2 expansion. [src: amr_fitness_cost] About 86% of AMR genes are Tier 2 keyword matches from bakta annotations. These may include non-AMR genes such as general efflux transporters. [src: amr_fitness_cost]

A sensitivity check mitigates this concern. Tier 1 (N=110) and Tier 2 (N=691) genes have indistinguishable fitness distributions (KS p = 0.17). [src: amr_fitness_cost] The cross-project digest likewise reports the cost as tier-independent (p=0.26). [src: discoveries] These two p-values are as the sources state them. [src: amr_fitness_cost, discoveries]

The Tier 2 product classifier also omits fosfomycin and tellurite resistance annotations. This leaves ~25 genes in the "unknown" mechanism category. Adding the annotations would reclassify them as enzymatic_inactivation and metal_resistance respectively. [src: amr_fitness_cost] See [[concepts/functional-annotation-of-amr-genes-and-mechanism-classification]].

## Polar effects

Transposon insertions can cause polar effects on downstream genes. This can confound fitness measurements for AMR genes in operons. [src: amr_fitness_cost]

## Relative fitness

RB-TnSeq measures fitness relative to the pool average. [src: amr_fitness_cost] The +0.086 effect is the difference between AMR knockout fitness (−0.024) and non-AMR knockout fitness (~−0.11). It is not an absolute selection coefficient. [src: amr_fitness_cost]

## Organism coverage

Only 37/48 Fitness Browser organisms had AMR genes, and these are predominantly environmental strains. The analysis therefore does not capture the cost of recently acquired mobile resistance in pathogens. [src: amr_pangenome_atlas] The amr_pangenome_atlas report adds that intrinsic resistance predominates in these environmental isolates. The cost of recently acquired mobile elements in clinical pathogens may differ substantially. [src: amr_pangenome_atlas]

## Open Directions

- Re-run the fitness comparison with fosfomycin and tellurite genes reclassified, to see whether the "unknown" mechanism group changes. This addresses the ~25 misclassified genes.
- Compute the essential-gene rate for AMR and non-AMR genes within the same organism set, to replace the cross-analysis comparison of 4.6% with ~14%.
- Test AMR genes inside operons against single-gene transcription units, to estimate how much polar effects contribute.
- Add fitness data from clinical pathogens carrying acquired mobile resistance, to close the environmental-strain gap.
