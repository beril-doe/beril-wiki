---
type: "Summary"
description: "GapMind pilot analysis finds near-universal metabolism with a DvH serine gap."
doc_type: "short"
full_text: "sources/essential_metabolome__REPORT.md"
---
# Essential Metabolome: GapMind Pathway Analysis Across Essential-Gene Organisms

## Overview

This report uses [[entities/gapmind]]—a computational pathway-completeness method—to compare amino-acid biosynthesis and carbon-source utilization across 7 organisms selected from essential-gene data. The analysis is a pilot rather than a pan-bacterial assessment because only 7 organisms were mapped successfully, although the underlying essential-gene collection contains 45 organisms. [src: essential_metabolome]

## Key Findings

### Amino-Acid Biosynthesis Is Highly Conserved

17 of 18 amino-acid biosynthesis pathways were present in all 7 organisms analyzed, representing 100% within this sample. The complete pathways were arg, asn, chorismate, cys, gln, gly, his, ile, leu, lys, met, phe, pro, thr, trp, tyr, and val. [src: essential_metabolome]

Serine biosynthesis was the sole exception, being present in 6 of 7 organisms (85.7%). [[entities/desulfovibrio-vulgaris-hildenborough]] was the missing organism according to GapMind predictions. [src: essential_metabolome]

The organism-level results were: *Caulobacter vibrioides* (Caulo), 18/18 pathways and 100%; *Shewanella oneidensis* (MR1), 18/18 and 100%; *Pseudomonas aeruginosa* (PS), 18/18 and 100%; *Pseudomonas putida* (Putida), 18/18 and 100%; *Sinorhizobium meliloti* (Smeli), 18/18 and 100%; *Azospirillum brasilense* (azobra), 18/18 and 100%; and *Desulfovibrio vulgaris* (DvH), 17/18 and 94.4%. [src: essential_metabolome]

### Apparent *D. vulgaris* Serine Auxotrophy

*Desulfovibrio vulgaris* was the only one of the 7 organisms lacking a complete serine-biosynthesis pathway under the report’s criterion of GapMind predictions categorized as complete or likely_complete. The result suggests the hypothesis that DvH may depend on externally supplied serine, but it is not established because the evidence is computational and may reflect pathway-detection limitations. [src: essential_metabolome]

The report interprets this possible auxotrophy in the context of DvH as an anaerobic sulfate-reducing bacterium associated with organic-rich environments, including sediments, intestinal tracts, and biofilms, where amino acids may be available from protein degradation. It proposes that loss of an energetically costly biosynthetic capacity could be advantageous when serine is freely available, but presents this as an ecological interpretation rather than a demonstrated mechanism. [src: essential_metabolome]

### Conserved Carbon-Source Utilization

The report identifies fumarate and succinate as conserved TCA-cycle intermediates, acetate, propionate, and L-lactate as conserved fermentation products, all amino acids as carbon sources, deoxyribose and deoxyribonate as conserved nucleotide derivatives, and putrescine as a conserved polyamine carbon source. These sources were reported as present in all 7 organisms (87.5%). [src: essential_metabolome]

Ethanol and deoxyinosine were nearly universal, occurring in 6 of 7 organisms (75%). The shared carbon-catabolic capacity is interpreted as consistent with the diverse ecological niches represented by the organisms, but the inference is limited by the small and phylogenetically restricted sample. [src: essential_metabolome]

### GapMind Coverage Limitation

The [[entities/escherichia-coli]] K-12 genome was absent from GapMind in the KBase pangenome collection: the Keio genome GCF_000005845.2 had 0 GapMind predictions. In contrast, the mapped genomes had 694 predictions for DvH (GCF_000195755.1), 694 for MR1 (GCF_000146165.2), 1,041 for *P. putida* (GCF_000007565.2), 745 for PS (GCF_000006765.1), 694 for Caulo (GCF_000022005.1), 1,735 for Smeli (GCF_000006965.1), and 1,786 for azobra (GCF_000011365.1). [src: essential_metabolome]

The report attributes the missing *E. coli* coverage to its exclusion from [[entities/gtdb]] pangenome construction because it had too many genomes for species-level analysis. This reduced the intended analysis from 45 Fitness Browser organisms to a 7-organism pilot and leaves coverage for the remaining 38 organisms unknown. [src: essential_metabolome]

## Interpretation and Caveats

The observed conservation supports the hypothesis that amino-acid prototrophy is common among free-living bacteria: 17 of 18 pathways were complete in all 7 organisms, and 6 of 7 organisms had all 18 pathways. However, the report explicitly concludes that the result demonstrates near-universal rather than strictly universal completeness because no pathway was universal at 100% across all 18 amino-acid pathways and DvH had a serine gap. [src: essential_metabolome]

The report does not establish that complete pathways are essential for viability. Essential-gene experiments used RB-TnSeq, or random-barcode transposon sequencing, in rich media, where nutrient supplementation can make biosynthetic genes appear non-essential. The data therefore cannot distinguish genes essential for biosynthesis from genes essential for viability. [src: essential_metabolome]

The study analyzed only 7 organisms, with limited phylogenetic diversity consisting mostly of Proteobacteria plus one Deltaproteobacterium, so its results cannot be generalized to bacteria as a whole. [src: essential_metabolome]

GapMind predictions are computational rather than experimental and use complete or likely_complete categories; non-canonical pathways, divergent enzymes below homology thresholds, and genes absent from genome annotations may be missed. In particular, DvH may possess a non-canonical or divergent serine pathway, or an unannotated pathway gene, so growth testing on serine-free minimal medium is required to validate auxotrophy. [src: essential_metabolome]

The source data included 305M GapMind predictions across 293K genomes in [[entities/kbase-ke-pangenome]], 859 universally essential gene families across 45 organisms, 80 pathway-completeness records, 18 amino-acid pathway records, 62 carbon-pathway records, 7,389 raw GapMind predictions for the selected organisms, and 8 manual organism-to-genome mappings. [src: essential_metabolome]

## Follow-up Directions

The report proposes checking whether DvH has lower-confidence serine predictions with a steps_missing status, reviewing the literature for experimentally documented DvH serine auxotrophy, and expanding organism mapping. It also proposes combining GapMind with [[entities/eggnog]] EC-to-[[entities/kegg]] pathway analysis, linking essential genes directly to pathways, and testing whether pathway gaps cluster by phylogeny or ecology. [src: essential_metabolome]

## Slots Into

- [[concepts/metabolic-model-gapfilling]] — GapMind pathway-completeness results, including the apparent DvH serine gap and the distinction between computational pathway calls and experimental validation. [src: essential_metabolome]
- [[concepts/gene-essentiality]] — The relationship between 859 universally essential gene families, pathway completeness, and essential-gene measurements from rich-media RB-TnSeq experiments. [src: essential_metabolome]
- [[concepts/condition-specific-fitness]] — The caveat that rich-media nutrient supplementation can obscure biosynthetic essentiality and the proposed testing of pathway essentiality under defined conditions. [src: essential_metabolome]
