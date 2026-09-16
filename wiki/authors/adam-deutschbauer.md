# Adam Deutschbauer

ORCID: [0000-0003-2728-7622](https://orcid.org/0000-0003-2728-7622)

## Contributions

[[summaries/metal_fitness_atlas__REPORT]] built a cross-species atlas of bacterial fitness under metal stress from the Fitness Browser. The Fitness Browser held 559 metal-related experiments across 31 organisms and 16 metals, which is 8.2% of 6,804 total experiments. Only 24 of the 31 organisms had fitness matrices, and these yielded 383,349 gene × metal fitness records spanning 14 metals. Of these records, 12,838 (3.3%) were broad metal-important genes and 5,667 (1.5%) were strict metal-important genes. The report defines "important" inconsistently: the findings section uses fit < -1, |t| > 4, and the limitations section uses fit < -1 OR n_sick ≥ 1. DvH was the most-profiled organism, with 149 experiments across 13 metals, and 1,366 of its genes (49.8% of its genome) were metal-important. [src: metal_fitness_atlas]

The project tested genome conservation across 22 organisms and 14 metals. Metal-important genes were 87.4% core versus 76.9% core for baseline genes (odds ratio, OR=2.08, p=4.3e-162), which reverses the initial hypothesis that these genes would be enriched in the accessory genome. The result held after excluding four duplicate *P. fluorescens* FW300 strains (OR=2.065, p=5.9e-141). In 21 of 22 organisms, metal-important genes were more core than baseline, and 14 of those differences were significant at p<0.05. *P. fluorescens* FW300-N2E3 was the exception, with a delta of -0.003 (p=0.70). [src: metal_fitness_atlas]

> **Editorial note.** Text was removed here after scientific review (caveat). The removed material and the objection are recorded in the run's salvage ledger.

Essential-metal genes for Fe, Mo, W, Se and Mn showed a mean core-fraction delta of +0.148, compared with +0.081 for toxic metals (one-sided Mann-Whitney U=39, p=0.015). Manganese had the largest delta (+0.198; all 30 important genes were core). Twelve of 14 metals were individually significant at p<0.05. The two exceptions were cadmium, tested in 1 organism (delta=-0.010, p=0.92), and uranium, tested in 2 organisms (delta=+0.035, p=0.34). The report identifies limited organism coverage as a likely explanation for these null results. [src: metal_fitness_atlas]

Among 2,891 ortholog groups with metal phenotypes, 1,182 were conserved in at least two organisms and 601 in at least three. The project flagged 149 novel metal-biology candidates that lack full functional annotation: 89 truly unknown, 43 with DUF/UPF domains (domain-of-unknown-function or uncharacterized-protein-family domains), and 17 with partial functional hints. These candidates are function predictions based solely on cross-species fitness data. [src: metal_fitness_atlas]

Module analysis used z-scores, which are module activity profiles standardized across all experiments per organism, and found 600 metal-responsive module records with |z| > 2.0 among 19,453 module × metal-experiment records (3.1%). The 183 responsive modules with conservation data had a mean core fraction of 0.826. An initial analysis that used raw activity scores found zero responsive modules because of a scale mismatch, and switching to z-normalized profiles resolved this. [src: metal_fitness_atlas]

The project derived a signature of 1,286 KO terms (KEGG Orthology functional groups) and used it to score 27,702 pangenome species. After genome-size normalization, *Leptospirillum* ranked at the 91st percentile. Bioleaching genera were not significantly enriched over background (Mann-Whitney p=0.17). A simple gene-presence repertoire score failed to predict metal fitness. [src: metal_fitness_atlas]

From these results, the report proposed a two-tier model:
- **Tier 1:** core general-stress functions, which make up most metal fitness genes.
- **Tier 2:** accessory specialized resistance functions.

The report presents this model as a refinement of the accessory-resistance idea rather than a rejection of it. [src: metal_fitness_atlas]

The report lists several caveats. Metal coverage was uneven, so rare-metal patterns largely reflect DvH and psRCH2. The report gives both 26 and 27 organisms for nickel and does not reconcile the two counts. Metal concentrations were not dose-normalized; for example, nickel concentrations ranged from 0.01-2.0 mM. Putatively essential genes, approximately 14.3% of protein-coding genes and approximately 82% core, are absent from the fitness data, so the report treats the core enrichment as a conservative estimate. Phylogenetic non-independence among *P. fluorescens* strains remains a limitation, although excluding four duplicate FW300 strains left the core-enrichment result robust. [src: metal_fitness_atlas]

## Projects (1)

- [[summaries/metal_fitness_atlas__REPORT|metal_fitness_atlas]]
