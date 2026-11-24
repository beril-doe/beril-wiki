---
type: "Summary"
description: "Summary of the project GapMind Pathway Analysis Across Essential Gene Organisms."
doc_type: "short"
full_text: "sources/essential_metabolome__REPORT.md"
---
# GapMind Pathway Analysis Across Essential Gene Organisms

This summary covers the project "GapMind Pathway Analysis Across Essential Gene Organisms". It asked whether a core set of metabolic pathways is universally complete across bacteria with essential-gene data. The answer is "near-universal, not strictly universal". [src: essential_metabolome] The evidence is a pilot of 7 organisms, not the intended 45 Fitness Browser (FB) organisms. [src: essential_metabolome] The report states that it cannot be generalized to a pan-bacterial scale. [src: essential_metabolome]

## Key Findings

### Amino acid biosynthesis is almost fully conserved

17 of 18 amino acid biosynthesis pathways are present in all 7 organisms (100% within this sample). [src: essential_metabolome]

The complete pathways are arg, asn, chorismate, cys, gln, gly, his, ile, leu, lys, met, phe, pro, thr, trp, tyr, and val. [src: essential_metabolome]

The report reads this conservation as a minimal metabolic repertoire for independent growth. [src: essential_metabolome]

It also reads complete biosynthesis of all 18 amino acids in 6 of 7 organisms (85.7%) as suggesting that amino acid prototrophy is ancestral for free-living bacteria. [src: essential_metabolome]

The report describes auxotrophs lacking such pathways as depending on external nutrients or on symbiotic or commensal relationships. [src: essential_metabolome]

See [[concepts/conservation-of-amino-acid-biosynthesis-pathways-across-bacteria]].

Per-organism completeness (GapMind, amino acid pathways):

| Organism | Pathways complete |
|---|---|
| Caulobacter vibrioides (Caulo) | 18/18 (100%) [src: essential_metabolome] |
| Shewanella oneidensis (MR1) | 18/18 (100%) [src: essential_metabolome] |
| Pseudomonas aeruginosa (PS) | 18/18 (100%) [src: essential_metabolome] |
| Pseudomonas putida (Putida) | 18/18 (100%) [src: essential_metabolome] |
| Sinorhizobium meliloti (Smeli) | 18/18 (100%) [src: essential_metabolome] |
| Azospirillum brasilense (azobra) | 18/18 (100%) [src: essential_metabolome] |
| Desulfovibrio vulgaris (DvH) | 17/18 (94.4%) [src: essential_metabolome] |

### Serine is the exception in Desulfovibrio vulgaris

Serine biosynthesis is present in only 6 of 7 organisms (85.7%). [src: essential_metabolome]

Desulfovibrio vulgaris is the only organism lacking a complete serine pathway under GapMind's complete or likely_complete categories. [src: essential_metabolome]

It is an anaerobic sulfate-reducing bacterium. [src: essential_metabolome]

It uses sulfate as terminal electron acceptor in anaerobic respiration. [src: essential_metabolome]

It utilizes the organic acids lactate, formate, and pyruvate. [src: essential_metabolome]

It lives in anaerobic, organic-rich environments, including sediments and intestinal tracts. [src: essential_metabolome]

The report lists its niches as anaerobic sediments, biofilms, and intestinal tracts. [src: essential_metabolome]

The report offers hypotheses, not measurements, for the gap:
- Environmental protein degradation would supply abundant serine. [src: essential_metabolome]
- It may be a genuine metabolic auxotrophy that depends on external serine. [src: essential_metabolome]
- Losing biosynthetic capacity could help when nutrients are abundant. [src: essential_metabolome]
- It may be genomic economy: losing genes that are energetically costly when their product is freely available. [src: essential_metabolome]

The report proposes testing growth on serine-free minimal media to confirm auxotrophy. [src: essential_metabolome]

See [[entities/desulfovibrio-vulgaris-hildenborough]].

Artifact explanations are also possible. Each could make a real pathway look absent:
- It may use a non-canonical serine pathway not in GapMind's reference database. [src: essential_metabolome]
- The pathway may use divergent enzymes below GapMind's homology threshold. [src: essential_metabolome]
- The genes may be present but unannotated in the genome assembly. [src: essential_metabolome]

### Carbon source utilization is widely conserved

The report lists several groups among the most widely conserved carbon sources.

Fumarate and succinate (tricarboxylic acid, TCA, cycle intermediates) are present in all 7 organisms, 87.5%. [src: essential_metabolome]

Acetate, propionate, and L-lactate are also among the most widely conserved. [src: essential_metabolome]

Deoxyribose and deoxyribonate are also among them. [src: essential_metabolome]

Putrescine is also among them. [src: essential_metabolome]

Separately, the report states that all amino acids can be catabolized as carbon sources. It gives no prevalence for this. [src: essential_metabolome]

Ethanol and deoxyinosine are nearly universal, occurring in 6 of 7 organisms, 75%. [src: essential_metabolome]

The report reads this as a shared central catabolic capacity for common organic compounds across diverse ecological niches. [src: essential_metabolome]

### Hypothesis outcome

The report's revised original H1 states that a core set of metabolic pathways is universally complete across bacteria. [src: essential_metabolome]

It judges H1 partially supported with significant caveats. [src: essential_metabolome]

The report also states that no pathways are truly universal (100%) even in this small sample. [src: essential_metabolome] This sits awkwardly beside the finding that 17 of 18 amino acid pathways are present in all 7 organisms. [src: essential_metabolome] The claims do not say how the report reconciles the two. One reading is that C49 refers to a wider set of pathways than the amino acid set, but the claims do not confirm this.

The report concludes that completeness is near-universal rather than strictly universal. [src: essential_metabolome]

It attributes the remaining diversity, even among organisms with experimental essential gene data, to likely ecological adaptation and nutrient availability. [src: essential_metabolome]

### GapMind coverage of the organisms

Escherichia coli genomes are completely absent from GapMind in the KBase pangenome collection. [src: essential_metabolome]

E. coli K-12 (Keio), GCF_000005845.2, has 0 predictions. [src: essential_metabolome]

The report attributes the exclusion to E. coli having too many genomes for species-level GTDB pangenome construction. [src: essential_metabolome]

The other organisms are present, with these prediction counts:

| Organism | Genome | GapMind predictions |
|---|---|---|
| D. vulgaris (DvH) | GCF_000195755.1 | 694 [src: essential_metabolome] |
| S. oneidensis (MR1) | GCF_000146165.2 | 694 [src: essential_metabolome] |
| P. putida (Putida) | GCF_000007565.2 | 1,041 [src: essential_metabolome] |
| P. aeruginosa (PS) | GCF_000006765.1 | 745 [src: essential_metabolome] |
| C. vibrioides (Caulo) | GCF_000022005.1 | 694 [src: essential_metabolome] |
| S. meliloti (Smeli) | GCF_000006965.1 | 1,735 [src: essential_metabolome] |
| A. brasilense (azobra) | GCF_000011365.1 | 1,786 [src: essential_metabolome] |

## Data and Methods

The analysis used GapMind pathway predictions for 7 organisms from the FB set, counting the complete and likely_complete categories. [src: essential_metabolome]

The source of the pathway predictions is the kbase_ke_pangenome collection's gapmind_pathways and genome tables, which cover 305M predictions and 293K genomes. [src: essential_metabolome] Universally essential gene families come from the projects/essential_genome collection's essential_families.tsv, which holds 859 families across 45 organisms. [src: essential_metabolome]

The report's data files are:
- data/pathway_completeness.tsv has 80 rows covering all pathway completeness across 7 organisms. [src: essential_metabolome]
- data/aa_pathway_completeness.tsv has 18 rows for amino acid biosynthesis pathways. [src: essential_metabolome]
- data/carbon_pathway_completeness.tsv has 62 rows for carbon source utilization pathways. [src: essential_metabolome]
- data/gapmind_fb_predictions.tsv has 7,389 rows of raw GapMind predictions for 7 organisms. [src: essential_metabolome]
- data/fb_genome_mapping_manual.tsv has 8 rows mapping FB organisms to genome identifiers. [src: essential_metabolome]

The report identifies 02_gapmind_pathway_analysis.ipynb as the notebook supporting the analysis, covering pathway analysis, organism mapping, and visualization. [src: essential_metabolome]

The report records v1 (2026-02-17) as its initial findings from a 7-organism GapMind analysis. [src: essential_metabolome]

## Caveats and Open Work

- Coverage limits the work to a pilot of 7 organisms, not the intended 45 FB organisms with essential gene data. [src: essential_metabolome]
- Coverage is unknown for the remaining 38 FB organisms. [src: essential_metabolome]
- The sample has limited phylogenetic diversity, mostly Proteobacteria plus 1 Deltaproteobacterium. [src: essential_metabolome]
- The results cannot be generalized to a pan-bacterial scale. [src: essential_metabolome]
- GapMind predictions are computational, not experimental. [src: essential_metabolome]
- Using complete and likely_complete categories may miss partial pathways. [src: essential_metabolome]
- GapMind may miss organisms with divergent metabolic genes. [src: essential_metabolome]
- Non-canonical or poorly characterized pathways are not detected. [src: essential_metabolome]
- The RB-TnSeq (random barcode transposon sequencing) experiments behind the essential gene data used rich media. [src: essential_metabolome]
- Nutrient supplementation may make biosynthetic genes appear non-essential. [src: essential_metabolome]
- The report cannot distinguish genes essential for biosynthesis from those essential for viability. [src: essential_metabolome]

Next analyses the report proposes:
- A literature review of whether D. vulgaris serine auxotrophy has been documented experimentally. [src: essential_metabolome]
- Checking lower-confidence GapMind predictions for a D. vulgaris serine pathway with "steps_missing" status. [src: essential_metabolome]
- Expanding the FB organism mapping to increase the sample size. [src: essential_metabolome]
- An eggNOG pathway analysis using Enzyme Commission (EC) annotations mapped to KEGG pathways for all 45 FB organisms, including E. coli. [src: essential_metabolome]
- A hybrid approach combining pathway-level GapMind analysis with gene-level eggNOG analysis for comprehensive coverage. [src: essential_metabolome]
- Mapping essential genes directly to metabolic pathways rather than relying on GapMind. [src: essential_metabolome]

The report also leaves open three questions:
- Are pathways predicted complete actually essential for viability? [src: essential_metabolome]
- Which pathways are essential only under specific growth conditions? [src: essential_metabolome]
- Do pathway gaps cluster by phylogeny or ecology? [src: essential_metabolome]

## Slots Into

- [[concepts/conservation-of-amino-acid-biosynthesis-pathways-across-bacteria]]: 17 of 18 pathways were complete in all 7 organisms, and serine was the exception. [src: essential_metabolome]
- [[concepts/reliability-and-coverage-limits-of-gapmind-pathway-predictions]]: E. coli is absent from GapMind, and non-canonical pathways go undetected. [src: essential_metabolome]
- [[concepts/metabolic-capability-versus-fitness-dependency]]: Rich-media RB-TnSeq may make biosynthetic genes look non-essential. [src: essential_metabolome]
