---
type: "Summary"
description: "Pilot GapMind analysis of amino-acid biosynthesis and carbon-source pathway completeness across 7 Fitness Browser organisms with essential-gene data, including an apparent Desulfovibrio vulgaris serine gap and E. coli coverage loss."
doc_type: "short"
full_text: "sources/essential_metabolome__REPORT.md"
---
# Essential Metabolome: GapMind Pathway Analysis Across Essential-Gene Organisms

## Overview

This report uses [[entities/gapmind]], a computational pathway-completeness method, to compare amino-acid biosynthesis and carbon-source utilization across 7 organisms selected from essential-gene data. Only 7 organisms were mapped successfully, although the underlying essential-gene collection contains 45 organisms. The analysis is therefore a pilot, not a pan-bacterial assessment. [src: essential_metabolome]

The report includes a pathway completeness visualization (`figures/pathway_completeness.png`). It shows amino-acid pathway completeness together with the top carbon sources. [src: essential_metabolome]

## Key Findings

### Amino-Acid Biosynthesis Is Highly Conserved

17 of 18 amino-acid biosynthesis pathways were present in all 7 organisms analyzed, which the report gives as 100% within this sample. The complete pathways were arg, asn, chorismate, cys, gln, gly, his, ile, leu, lys, met, phe, pro, thr, trp, tyr, and val. [src: essential_metabolome]

Serine biosynthesis was the sole exception, present in 6 of 7 organisms (85.7%). According to GapMind predictions, the organism missing it was [[entities/desulfovibrio-vulgaris-hildenborough]]. This is a computational prediction, not a demonstrated auxotrophy. [src: essential_metabolome]

The organism-level results were:
- *Caulobacter vibrioides* (Caulo): 18/18 pathways, 100%.
- *Shewanella oneidensis* (MR1): 18/18, 100%.
- *Pseudomonas aeruginosa* (PS): 18/18, 100%.
- *Pseudomonas putida* (Putida): 18/18, 100%.
- *Sinorhizobium meliloti* (Smeli): 18/18, 100%.
- *Azospirillum brasilense* (azobra): 18/18, 100%.
- *Desulfovibrio vulgaris* (DvH): 17/18, 94.4%. [src: essential_metabolome]

### Apparent *D. vulgaris* Serine Auxotrophy

*Desulfovibrio vulgaris* was the only one of the 7 organisms without a complete serine-biosynthesis pathway. The report's criterion was a GapMind score_category of complete or likely_complete. The result suggests the hypothesis that DvH depends on externally supplied serine. It is not established, because the evidence is computational and may reflect limits of pathway detection. [src: essential_metabolome]

The report gives three points of context for DvH. It respires anaerobically using sulfate as the terminal electron acceptor. It uses organic acids (lactate, formate, pyruvate). Its niche is anaerobic sediments, biofilms, and intestinal tracts. [src: essential_metabolome]

The report argues that DvH lives in anaerobic, organic-rich environments where serine would be abundant from protein degradation. On this basis it suggests the gap could be a genuine metabolic auxotrophy, with the organism depending on external serine. This rationale is speculative: neither external serine availability nor dependency was tested. [src: essential_metabolome]

The report also proposes that metabolic streamlining could be advantageous when nutrients are abundant. It frames this as "genomic economy": losing energetically costly genes when the product is freely available. These are proposed explanations for the predicted serine loss, not direct findings or a demonstrated mechanism. [src: essential_metabolome]

The report also offers alternative explanations for the predicted gap:
- DvH may use a non-canonical serine biosynthesis pathway that is not in GapMind's reference database.
- The pathway may use divergent enzymes that fall below GapMind's homology threshold.
- The genes may be present but unannotated in the genome assembly. [src: essential_metabolome]

Growth testing on serine-free minimal medium would be needed to confirm auxotrophy. [src: essential_metabolome]

### Conserved Carbon-Source Utilization

The report lists these carbon sources as "present in all 7 organisms": the TCA-cycle intermediates fumarate and succinate; the fermentation products acetate, propionate, and L-lactate; all amino acids as carbon sources; the nucleotide derivatives deoxyribose and deoxyribonate; and the polyamine putrescine. It labels this group 87.5%. That percentage does not match the stated 7-organism count, and the report does not explain the denominator. The figure is reproduced as reported. [src: essential_metabolome]

Ethanol and deoxyinosine were reported as nearly universal, occurring in 6 of 7 organisms, but labeled 75%. This is the same unexplained denominator discrepancy, and the figures are reproduced as reported. [src: essential_metabolome]

The report reads these predictions as a shared central catabolic capacity consistent with the diverse ecological niches of these bacteria. This is an interpretation of computational predictions, not a direct metabolic measurement. The small, phylogenetically restricted sample further limits it. [src: essential_metabolome]

### GapMind Coverage Limitation

[[entities/escherichia-coli]] genomes were completely absent from GapMind in the KBase pangenome collection. The Keio *E. coli* K-12 genome GCF_000005845.2 had 0 GapMind predictions. [src: essential_metabolome]

The mapped genomes had the following prediction counts:
- DvH (GCF_000195755.1): 694.
- MR1 (GCF_000146165.2): 694.
- *P. putida* (GCF_000007565.2): 1,041.
- PS (GCF_000006765.1): 745.
- Caulo (GCF_000022005.1): 694.
- Smeli (GCF_000006965.1): 1,735.
- azobra (GCF_000011365.1): 1,786. [src: essential_metabolome]

The report attributes the missing *E. coli* coverage to its exclusion from [[entities/gtdb]] pangenome construction: it had too many genomes for species-level analysis. This cut the intended analysis of 45 Fitness Browser organisms with essential-gene data down to a 7-organism pilot. Coverage for the remaining 38 organisms is unknown, and organisms with divergent metabolic genes may be missed. [src: essential_metabolome]

## Hypothesis Test

The original hypothesis (H1, revised version) was "A core set of metabolic pathways is universally complete across bacteria." The report judges it "Partially supported with significant caveats." [src: essential_metabolome]

The report lists three points against H1. First, no pathways are truly universal (100%), even in this small sample. Second, there are organism-specific gaps (the DvH serine gap). Third, the analysis covers only 7 organisms and is not pan-bacterial. The first point conflicts with the report's own finding that 17 of 18 pathways were present in all 7 organisms. The report does not reconcile the two statements, so both are recorded here as written. [src: essential_metabolome]

The report concludes that the data show near-universal rather than strictly universal pathway completeness. It attributes the remaining metabolic diversity to likely ecological adaptation and nutrient availability, which is an inference rather than a tested explanation. [src: essential_metabolome]

## Interpretation and Caveats

The report suggests the hypothesis that amino-acid prototrophy is the ancestral state for free-living bacteria. The basis is that 6 of 7 organisms (85.7%) had complete biosynthesis pathways for all 18 amino acids. With so few organisms, this is a hypothesis, not an established pan-bacterial finding. [src: essential_metabolome]

The report also proposes that the high conservation (17/18 pathways at 100% within the sample) indicates a minimal metabolic repertoire required for independent growth. This extrapolates from a small sample and is not a demonstrated requirement. [src: essential_metabolome]

The report does not establish that complete pathways are essential for viability. The essential-gene experiments used RB-TnSeq (random-barcode transposon sequencing, which measures gene fitness from pooled mutant libraries) in rich media. Nutrient supplementation in rich media can make biosynthetic genes appear non-essential, so the data cannot distinguish "essential for biosynthesis" from "essential for viability." [src: essential_metabolome]

The study analyzed only 7 organisms, not the 45 originally planned. Its phylogenetic diversity is limited, mostly Proteobacteria plus one Deltaproteobacterium. The results therefore cannot be generalized to a pan-bacterial scale. [src: essential_metabolome]

GapMind predictions are computational, not experimental. The analysis used only the complete and likely_complete categories, so partial pathways may be missed, and non-canonical or poorly characterized pathways are not detected. [src: essential_metabolome]

The source data were:
- 305M GapMind predictions across 293K genomes in [[entities/kbase-ke-pangenome]].
- 859 universally essential gene families across 45 organisms, from the essential_genome project. [src: essential_metabolome]

The generated tables were:
- 80 pathway-completeness records.
- 18 amino-acid pathway records.
- 62 carbon-pathway records.
- 7,389 raw GapMind predictions for the selected organisms.
- 8 manual organism-to-genome mappings. [src: essential_metabolome]

## Follow-up Directions

The report lists three open checks:
- A literature review on whether *D. vulgaris* serine auxotrophy is documented experimentally.
- A check of whether DvH has a lower-confidence serine prediction with steps_missing status.
- Mapping more Fitness Browser organisms to increase the sample size. [src: essential_metabolome]

The report also proposes three alternative analyses:
- Pathway analysis from [[entities/eggnog]] EC annotations to [[entities/kegg]] pathways for all 45 Fitness Browser organisms, including *E. coli*.
- A hybrid that combines GapMind's pathway-level calls with eggNOG's gene-level annotation.
- Mapping essential genes directly to metabolic pathways instead of relying on GapMind. [src: essential_metabolome]

Three questions remain unresolved:
- Are "complete" pathways actually essential for viability?
- Which pathways are essential only under specific growth conditions?
- Do pathway gaps cluster by phylogeny or ecology? [src: essential_metabolome]

## Slots Into

- [[concepts/biosynthetic-prototrophy-and-auxotrophy]] — Near-universal amino-acid pathway completeness, the predicted DvH serine gap, and the ancestral-prototrophy and genomic-streamlining hypotheses. [src: essential_metabolome]
- [[concepts/computational-pathway-prediction-validation]] — GapMind calls are computational, carbon-source percentages carry unexplained denominators, and serine-free growth tests are needed for validation. [src: essential_metabolome]
- [[concepts/metabolic-model-gapfilling]] — GapMind pathway-completeness results, including the apparent DvH serine gap. [src: essential_metabolome]
- [[concepts/homology-search-negative-evidence]] — An apparent pathway absence may reflect divergent enzymes below the homology threshold, non-canonical pathways, or unannotated genes. [src: essential_metabolome]
- [[concepts/community-metabolic-interdependence]] — The proposed dependence of DvH on external serine from protein degradation in organic-rich habitats. [src: essential_metabolome]
- [[concepts/data-landscape-ownership-and-coverage-bias]] — *E. coli* K-12 has 0 GapMind predictions in the collection. [src: essential_metabolome]
- [[concepts/genomic-under-representation]] — Coverage gaps cut 45 intended organisms to a 7-organism pilot, with coverage unknown for the remaining 38. [src: essential_metabolome]
- [[concepts/pangenome-core-boundary-and-clade-size-bias]] — *E. coli* was excluded from GTDB pangenome construction because it had too many genomes. [src: essential_metabolome]
- [[concepts/gene-essentiality]] — The link between the 859 universally essential gene families, pathway completeness, and rich-media RB-TnSeq essentiality. [src: essential_metabolome]
- [[concepts/condition-specific-fitness]] — Rich-media supplementation can obscure biosynthetic essentiality, and conditional pathway essentiality remains open. [src: essential_metabolome]
