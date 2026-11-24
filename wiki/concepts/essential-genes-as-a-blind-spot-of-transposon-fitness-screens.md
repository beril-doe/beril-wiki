---
type: "Concept"
description: "Genes without viable transposon mutants have no fitness profiles, so fitness-based prioritization misses them; covers how essential dark genes are ranked from non-fitness evidence and tested by CRISPRi knockdown."
sources: ["summaries/counter_ion_effects__REPORT.md", "summaries/discoveries.md", "summaries/essential_genome__REPORT.md", "summaries/field_vs_lab_fitness__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/metal_specificity__REPORT.md", "summaries/pitfalls.md", "summaries/truly_dark_genes__REPORT.md"]
---
# Essential genes as a blind spot of transposon fitness screens

Genes with no viable transposon mutants have no fitness profiles, so fitness-based analyses and prioritization cannot see them. [src: functional_dark_matter] One report ([[summaries/functional_dark_matter__REPORT]]) ranks essential dark genes from non-fitness evidence and proposes CRISPR interference (CRISPRi) knockdown tests. [src: functional_dark_matter] The ranking is computational; the CRISPRi tests are proposals, not results. [src: functional_dark_matter, essential_genome]

## How large the blind spot is

Putative essential genes are about 14.3% of protein-coding genes. They lack transposon insertions and are absent from both NaCl and metal fitness data. They are 82% core, and excluding them affects the original and corrected conservation analyses equally. [src: counter_ion_effects] The metal-specificity report says the same: about 14% of genes (~82% core) are absent from fitness data. This biases all categories toward core enrichment, so the true baseline core fraction is likely below 81% and the reported deltas are conservative. [src: metal_specificity] In Desulfovibrio vulgaris Hildenborough, 678 essential genes (80.1% core) are excluded for lack of transposon mutants. [src: field_vs_lab_fitness] Including them would raise the overall baseline slightly. It would not change condition-class comparisons, which use only non-essential genes. [src: field_vs_lab_fitness] See [[concepts/essential-genes-and-core-genome-conservation]] and [[concepts/limits-of-transposon-based-essentiality-calls]].

Fitness modules share the blind spot. Independent component analysis (ICA) decomposes fitness variation, so genes without fitness data are invisible to it. Modules therefore capture only the non-essential part of functional architecture. [src: discoveries] In one analysis, 0 essential genes appear in the 1,116 fitness modules across 32 organisms. [src: discoveries]

The Fitness Browser has no explicit essentiality column, insertion count or has-fitness-data flag across its 45 tables. [src: pitfalls] Essential genes are therefore inferred as protein-coding genes (gene-table type='1') absent from genefitness. This is an upper bound on true essentiality. [src: pitfalls] Querying only genefitness misses about 14.3% of protein-coding genes. [src: pitfalls] Fitness-versus-conservation analyses must include these genes or acknowledge that the most extreme fitness category is missing. [src: pitfalls]

## Essential dark genes

Among functionally dark genes in the Fitness Browser, 9,557 are essential. [src: functional_dark_matter] They are 55% of the 17,344 scored dark genes. [src: functional_dark_matter] They are invisible to standard random barcode transposon sequencing (RB-TnSeq) because they have zero rows in genefitness. [src: functional_dark_matter] The report says they are 55% of the experimentally actionable dark matter. [src: functional_dark_matter] They are also the majority of phenotype-bearing dark genes, yet fitness-based scoring systematically misses them. [src: functional_dark_matter]

Their absence from the fitness-centric NB05 top 100 follows from the scoring design. Missing rows put fitness importance at the essentiality bonus floor, and the tractability dimension penalizes non-knockable genes. [src: functional_dark_matter] A separate analysis of hypothetical essential genes found 8,297 across 48 organisms, 20.2% of all essentials. [src: essential_genome] Of these, 4,385 are orphans that the module-transfer method cannot predict. [src: essential_genome] That report says it adds cross-organism essentiality to Fitness Browser data to enable function prediction for essential genes beyond fitness profiling. [src: essential_genome] Among top truly dark gene candidates, 34 are essential. [src: truly_dark_genes] Truly dark genes have a higher essential fraction than annotation-lag genes: 18.0% versus 13.4% (OR = 1.420, p < 1e-10). [src: truly_dark_genes]

## Ranking without fitness

The report scores essential dark genes on evidence that does not need fitness data. This avoids penalizing them for data they structurally cannot have. [src: functional_dark_matter] NB07 produced 50 ranked candidates amenable to CRISPRi. [src: functional_dark_matter] All 9,557 genes were ranked on five dimensions, weighted as gene neighbor context (0.25), cross-organism conservation (0.20), phylogenetic breadth (0.20), domain annotations (0.15) and CRISPRi tractability (0.20). [src: functional_dark_matter]

The top 50 score 0.740–0.875 and span 15 organisms. [src: functional_dark_matter] They exceed the fitness-active top 100 (0.624–0.715), which the report attributes to stronger conservation and neighborhood signals. [src: functional_dark_matter] All have high-confidence hypotheses from operon context. [src: functional_dark_matter] The report explains the high scores by converging evidence. The candidates have detectable domains, widely conserved ortholog groups and conserved neighborhoods with annotated partners. They also sit in organisms amenable to CRISPRi. [src: functional_dark_matter]

Top ten candidates:

| Rank | Organism | Locus | Score | Domains and context |
|---|---|---|---|---|
| 1 | E. coli Keio | 14796 | 0.875 | YbeY, TIGR00043; ion transport + NTP hydrolase [src: functional_dark_matter] |
| 2 | Shewanella MR-1 | 200382 | 0.874 | RimP_N, DUF150_C; tRNA-Met + NusA [src: functional_dark_matter] |
| 3 | K. oxytoca | BWI76_RS08540 | 0.865 | OmpA, TIGR02802; TolB + CpoB [src: functional_dark_matter] |
| 4 | P. putida N2C3 | AO356_29395 | 0.838 | Peptidase_M20; ABC transporter + peptidase [src: functional_dark_matter] |
| 5 | Shewanella MR-1 | 201473 | 0.835 | EarP, TIGR03837; EF-P + flavodoxin [src: functional_dark_matter] |
| 6 | E. coli Keio | 14768 | 0.833 | DUF493; lipoate biosynthesis + PBP5 [src: functional_dark_matter] |
| 7 | Shewanella MR-1 | 200359 | 0.833 | YbeY, TIGR00043; CorC + PhoH [src: functional_dark_matter] |
| 8 | P. putida | PP_1910 | 0.828 | YceD; 50S ribosomal L32 + PlsX [src: functional_dark_matter] |
| 9 | P. putida | PP_5002 | 0.828 | GBBH-like_N; HslVU protease + PhaC1 [src: functional_dark_matter] |
| 10 | E. coli Keio | 11474 | 0.825 | DUF4109; tRNA-Met + translation [src: functional_dark_matter] |

The report's own summary table also describes the top three. Gene 14796 is conserved in 5+ phyla, in a synteny-confirmed operon, with predicted ion transport. [src: functional_dark_matter] Gene 200382 is a predicted ribosome assembly factor in a conserved neighborhood. [src: functional_dark_matter] BWI76_RS08540 is predicted to act in cell division and is conserved across Enterobacteriaceae. [src: functional_dark_matter]

Rankings depend on the weights. For essential genes, dropping tractability keeps only 18/50 (36%) of the top candidates. [src: functional_dark_matter] Dropping neighbor context keeps 24/50 (48%). [src: functional_dark_matter] Across weight choices, 6 stay always in the top 50 and 19 always in the top 100. [src: functional_dark_matter]

## CRISPRi as the proposed test

CRISPRi gives an experimental path that transposon mutagenesis cannot. Gene neighborhood analysis recovers context for nearly all essential dark genes: 97.2% have annotated neighbors. [src: functional_dark_matter] The covering set has 8,900 essential genes that cannot be studied by transposon knockout. [src: functional_dark_matter] The action plans flag or recommend them for CRISPRi. [src: functional_dark_matter] The report proposes CRISPRi knockdown for top candidates that lack viable knockouts. [src: functional_dark_matter] Each top candidate has a design with target organism, sgRNA target, growth condition, expected phenotype and validation strategy. [src: functional_dark_matter] For the top candidate, Keio:14796, the report predicts ion transport from its operon. It proposes knockdown in E. coli Keio on varied carbon and nitrogen sources, monitoring OD600 for growth defects. [src: functional_dark_matter] The essential-genome report separately proposes testing its 1,382 module-transfer predictions by CRISPRi under conditions predicted from module context. [src: essential_genome] The truly-dark-genes report suggests Mobile-CRISPRi could enable rapid functional testing across organisms. [src: truly_dark_genes] See [[entities/crispr-interference-knockdown]].

## Open Directions

- Run CRISPRi knockdowns for the top 10 candidates (for example Keio:14796 in [[entities/escherichia-coli]]). This tests whether operon-context hypotheses predict phenotypes, which none of the evidence here has done.
- Repeat the weight-sensitivity analysis with orthogonal evidence. Rankings change substantially when neighbor context or tractability is dropped, and held-out knockdown results would show which dimensions carry real signal.
- Add the excluded essential genes to the conservation baselines as a separate category. This would quantify the core-enrichment bias directly, instead of only stating its direction.
- Find a way to give the 4,385 orphan hypothetical essentials a prediction route beyond module transfer, for example domain or neighborhood evidence.
