---
type: "Concept"
description: "Biases in calling essential genes from transposon data: gene length, insertion bias, library conditions, absence-based upper bounds, orthology inference and organism sampling; stops at pangenome interpretation."
sources: ["summaries/adp1_triple_essentiality__REPORT.md", "summaries/amr_fitness_cost__REPORT.md", "summaries/conservation_vs_fitness__REPORT.md", "summaries/essential_genome__REPORT.md", "summaries/essential_metabolome__REPORT.md", "summaries/field_vs_lab_fitness__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/module_conservation__REPORT.md", "summaries/pitfalls.md"]
---
# Limits of transposon-based essentiality calls

Transposon-based essentiality calls are biased by gene length, insertion patterns, library conditions, absence-based definitions, orthology inference and organism sampling. [src: conservation_vs_fitness, essential_genome] Most of the evidence is caveats stated by the reports. One direct measurement, in Acinetobacter baylyi ADP1, shows that transposon sequencing (TnSeq) catches only 7.9% (18/229) of knockout-essential genes. [src: adp1_triple_essentiality] See also [[concepts/essential-genes-as-a-blind-spot-of-transposon-fitness-screens]] and [[concepts/transposon-insertion-fitness-versus-gene-deletion-lethality]].

## Literature Context

The one candidate paper bears directly on the main theme of this page, that absence of transposon insertions is a fragile basis for calling genes essential. It reports a completely saturated Himar1 transposon library in Mycobacterium tuberculosis. Earlier studies, it says, analyzed subsaturated libraries. That forced statistical methods to estimate whether a gap in coverage reflected biological selection or the stochasticity of insertion, so the essentiality of many genomic features, particularly small ones, could not be reliably assessed [PMID 28096490](https://pubmed.ncbi.nlm.nih.gov/28096490/).

The same paper found a previously unknown sequence bias of the Himar1 element. About 9% of potential TA dinucleotide insertion sites were less permissible for insertion. The authors report that this bias was observed in multiple prokaryotes. It affects the statistical interpretation of TnSeq data, because Himar1 had been assumed to insert with equal probability at all TA sites. They used a hidden Markov model of essentiality that accounts for the bias. With it they could evaluate features containing as few as 2 TA sites, including small ORFs, noncoding RNAs, promoters and methylation sites. They also found essential regions that matched no known feature [PMID 28096490](https://pubmed.ncbi.nlm.nih.gov/28096490/). The abstract does not report an independent validation of these calls against deletion mutants.

The corpus's caveats are consistent with this literature. The hub treats calls based on absent insertions or absent fitness data as upper bounds on essentiality. The reports note that genes without insertions may be short, AT-rich or in low-complexity regions. The essential-genome report found essential genes shorter than non-essential ones, with median lengths of 675 bp versus 885 bp. The M. tuberculosis paper supports this concern. It shows that short features are the hardest to assess without a model that handles insertion-site permissiveness, and that site-level bias exists beyond gene length. It also supports the hub's call for caution with genes that have few insertion sites.

The corpus differs in method and scope. In the Fitness Browser analysis, the putative-essential calls are protein-coding genes absent from genefitness. That is a data-availability proxy, not a saturated library with an explicit statistical model. Other corpus projects also call genes essential from missing insertions. The M. tuberculosis work therefore shows what a more rigorous call looks like, and it suggests that the corpus's absence-based calls may include permissiveness artifacts. That is a hypothesis, because the paper studied one organism and the corpus did not test TA-site bias. The paper does not address the corpus's other limits. It does not address the ADP1 result that TnSeq catches only 7.9% (18/229) of knockout-essential genes, nor orthology inference or sampling bias across the 48 Fitness Browser organisms. Those findings stand as extensions of, not replacements for, this literature.

## Absence-based calls are upper bounds

Several projects call a gene essential when it has no transposon insertions or no fitness data. Such a call is an upper bound on true essentiality. [src: conservation_vs_fitness, essential_genome, pitfalls]

- Genes without insertions may be short, in low-complexity regions, AT-rich, or at scaffold edges, rather than essential. [src: conservation_vs_fitness, essential_genome]
- In the [[entities/fitness-browser]] analysis, protein-coding genes (gene-table type='1') absent from genefitness are treated as putative essentials. [src: pitfalls]
- The Fitness Browser has no explicit essentiality column, insertion count, or has-fitness-data flag across its 45 tables. [src: pitfalls]
- The gene.type column encodes feature type (1=CDS, 5=pseudo, 7=rRNA, 2=tRNA), not essentiality. [src: pitfalls]
- Querying only genefitness misses ~14.3% of protein-coding genes. These genes are reported as 82% core. [src: pitfalls]
- Fitness-versus-conservation analyses must include these genes or acknowledge that the most extreme fitness category is missing. [src: pitfalls]

The bound can bias other estimates. In the AMR (antimicrobial resistance) fitness-cost analysis, ~4.6% of AMR genes are putatively essential because they are absent from fitness matrices. If these are the most costly AMR genes, the estimated +0.086 cost is a lower bound. [src: amr_fitness_cost]

Only 4.6% of AMR genes were absent from the matrices. A prior analysis (`fitness_effects_conservation`, different organism set) estimated a ~14% background essential rate. [src: amr_fitness_cost] The report reads the lower rate as consistent with resistance genes being more dispensable, and as arguing against strong right-censoring bias. [src: amr_fitness_cost] The two rates come from different organism sets, so the comparison is only suggestive.

In the metal fitness atlas, putatively essential genes lack insertions and are excluded: ~14.3% of protein-coding genes, ~82% core. The report says this makes the observed core enrichment of metal fitness genes a conservative estimate. [src: metal_fitness_atlas] See [[concepts/core-genome-enrichment-of-metal-stress-fitness-genes]]. Similarly, independent component analysis (ICA) fitness modules contained 0 essential genes. Essential genes are invisible to ICA because they have no fitness data. [src: module_conservation]

The denominator also matters. Essential genes were 82% core using all genes including unmapped ones, and 86% core using mapped genes only. [src: pitfalls] Mixed denominators caused a critical review issue, because figures showed 86%/78% while prose said 82%/66%. [src: pitfalls]

## Gene length and insertion bias

Short genes receive fewer insertions, so length biases calls. In the essential-genome report, essential genes were shorter than non-essential genes, with median lengths of 675 bp versus 885 bp, and 17.8% of essentials were <300 bp. [src: essential_genome] The conservation_vs_fitness report found essential genes slightly shorter on average, consistent with some insertion bias. [src: conservation_vs_fitness] Goodall et al. (2018) used TraDIS to define the E. coli K-12 essential genome and noted that gene-length biases can affect transposon-based calls. [src: conservation_vs_fitness]

In Desulfovibrio vulgaris (DvH), gene length is confounded with fitness measurement quality, because short genes get fewer insertions. It is also confounded with core status, because core genes tend to be longer. [src: field_vs_lab_fitness]

## Library conditions and what a disruption does

Random barcode transposon sequencing (RB-TnSeq) essentiality is defined under library-construction conditions, typically rich media. Genes essential only under stress are missed. [src: conservation_vs_fitness, essential_genome] Nutrient supplementation may make biosynthetic genes look non-essential. [src: essential_metabolome] One report also cannot distinguish genes essential for biosynthesis from those essential for viability. [src: essential_metabolome]

A transposon insertion is not a deletion. In A. baylyi ADP1, only 7.9% (18/229) of knockout-essential genes are caught by TnSeq at the optimal threshold. [src: adp1_triple_essentiality] The report hypothesizes that the 211 knockout-essential genes called dispensable by TnSeq tolerate partial function from disrupted alleles. [src: adp1_triple_essentiality] It lists possible mechanisms: partial or truncated protein, read-through transcription, and functional domains upstream of the insertion. [src: adp1_triple_essentiality]

Call differences also depend on the conditions measured. A gene may be essential under knockout conditions but dispensable in most TnSeq conditions. This gives low essentiality_fraction despite high lethality. [src: adp1_triple_essentiality] The original ADP1 study analyzed only TnSeq-dispensable genes (n=478), which the report calls limiting because TnSeq misses most truly essential genes. [src: adp1_triple_essentiality] TnSeq-essential genes have no viable deletion mutants, so they cannot have growth-rate measurements. [src: adp1_triple_essentiality]

## Orthology inference

Essential-genome conclusions depend on ortholog groups. Bidirectional best hit (BBH) BLAST orthology can miss paralogs, gene fusions, and distant homologs, so some reported orphan essentials may have undetected diverged orthologs. [src: essential_genome] Connected components of the BBH graph can also over-merge unrelated genes through transitive links, especially for multi-domain proteins. [src: essential_genome] See [[entities/bidirectional-best-blast-hit-orthology]].

## Organism sampling

The 48 Fitness Browser organisms are biased toward culturable Proteobacteria. Patterns in uncultured lineages, Actinobacteria, and Firmicutes are underrepresented. [src: essential_genome] The essential-genome report proposes cross-referencing the Database of Essential Genes to find families essential in organisms outside the Fitness Browser. [src: essential_genome] It also proposes testing whether essentiality of variably essential families correlates with metabolic pathway completeness, including absence of alternative pathways. [src: essential_genome]

## Open Directions

- Measure how far gene length alone predicts "essential" calls. Fit a length-adjusted model across Fitness Browser organisms, using the 675 bp versus 885 bp medians as a baseline. This would separate insertion bias from biology.
- Test the partial-function hypothesis for the 211 ADP1 genes. Check where insertions fall within each gene for knockout-essential, TnSeq-dispensable genes.
- Check the AMR cost lower-bound claim. Recompute the +0.086 estimate with the 4.6% absent genes under bounding assumptions.
- Cross-reference the Database of Essential Genes to address the taxonomic bias of the 48 organisms.
- Test whether variable essentiality tracks metabolic pathway completeness. This would separate condition-driven from artifactual calls.
- Rerun orphan-essential calls with a more sensitive orthology method to estimate how many are missed by BBH.
