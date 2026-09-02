---
type: "Concept"
description: "Pathway completeness, prototrophy, auxotrophy, and nutrient dependence"
sources: ["summaries/essential_metabolome__REPORT.md"]
---
# Biosynthetic Prototrophy, Auxotrophy, and Nutrient Dependence

[[summaries/essential_metabolome__REPORT]] examines biosynthetic prototrophy and possible auxotrophy using [[entities/gapmind]], a computational method for evaluating pathway completeness, across seven organisms selected from essential-gene data. [src: essential_metabolome]

## Definitions and Scope

Biosynthetic prototrophy here refers to the predicted capacity to synthesize a required metabolite, whereas auxotrophy refers to a predicted pathway gap that could create dependence on an externally supplied nutrient. [src: essential_metabolome]

The analysis is a seven-organism pilot rather than a pan-bacterial assessment because only 7 organisms were mapped successfully, although the underlying essential-gene collection contains 45 organisms. [src: essential_metabolome]

The pathway calls used GapMind categories of complete or likely_complete, so they represent computational evidence rather than direct growth or biochemical measurements. [src: essential_metabolome]

## Evidence for Broad Amino-Acid Prototrophy

17 of 18 amino-acid biosynthesis pathways were present in all 7 analyzed organisms, representing 100% within this sample. [src: essential_metabolome]

The pathways complete in all 7 organisms were arg, asn, chorismate, cys, gln, gly, his, ile, leu, lys, met, phe, pro, thr, trp, tyr, and val. [src: essential_metabolome]

Six of the 7 organisms had all 18 amino-acid pathways complete, while [[entities/desulfovibrio-vulgaris-hildenborough]] had 17/18 complete pathways, or 94.4%. [src: essential_metabolome]

The other six organisms—*Caulobacter vibrioides*, *Shewanella oneidensis*, *Pseudomonas aeruginosa*, *Pseudomonas putida*, *Sinorhizobium meliloti*, and *Azospirillum brasilense*—each had 18/18 pathways and 100%. [src: essential_metabolome]

This pattern supports the hypothesis that amino-acid prototrophy is common among the sampled free-living bacteria, but it does not establish universal completeness across bacteria because the sample contained only 7 organisms and one pathway was incomplete in one organism. [src: essential_metabolome]

These findings refine [[concepts/biosynthetic-self-sufficiency-and-cultivation]] by showing that predicted pathway completeness can indicate biosynthetic potential without demonstrating that the pathway is required or sufficient for growth under a defined cultivation condition. [src: essential_metabolome]

## Apparent Serine Auxotrophy in *Desulfovibrio vulgaris*

Serine biosynthesis was the sole amino-acid pathway not present in all 7 organisms, with a complete prediction in 6 of 7 organisms, or 85.7%. [src: essential_metabolome]

The missing serine pathway was assigned to *D. vulgaris* by the GapMind analysis. [src: essential_metabolome]

This result suggests the hypothesis that *D. vulgaris* may depend on externally supplied serine, but the evidence is not sufficient to establish serine auxotrophy because the result is computational and may reflect pathway-detection limitations. [src: essential_metabolome]

A divergent enzyme, a non-canonical pathway, or a gene missing from the genome annotation could produce an apparent GapMind gap even when serine biosynthesis is biologically possible. [src: essential_metabolome]

The report interprets the possible auxotrophy in the context of *D. vulgaris* as an anaerobic sulfate-reducing bacterium associated with organic-rich environments, including sediments, intestinal tracts, and biofilms, where amino acids may be available from protein degradation. [src: essential_metabolome]

The hypothesis that losing an energetically costly biosynthetic capacity could be advantageous when serine is freely available is an ecological interpretation rather than a demonstrated mechanism. [src: essential_metabolome]

This case connects to [[concepts/metabolic-model-gapfilling]] because the serine result illustrates how a pathway-completeness call can identify a testable metabolic gap while remaining vulnerable to incomplete annotation and non-canonical chemistry. [src: essential_metabolome]

## Carbon-Source Capacity

Fumarate and succinate were reported as conserved TCA-cycle intermediates, acetate, propionate, and L-lactate were reported as conserved fermentation products, all amino acids were reported as carbon sources, deoxyribose and deoxyribonate were reported as conserved nucleotide derivatives, and putrescine was reported as a conserved polyamine carbon source. [src: essential_metabolome]

Each of these reported carbon-source capacities was present in all 7 organisms, or 87.5%. [src: essential_metabolome]

Ethanol and deoxyinosine were nearly universal, occurring in 6 of 7 organisms, or 75%. [src: essential_metabolome]

The shared carbon-catabolic capacity is consistent with the ecological breadth of the sampled organisms, but that interpretation is limited by the small and phylogenetically restricted sample. [src: essential_metabolome]

## Pathway Potential Is Not Essentiality

The report does not establish that a complete biosynthetic pathway is essential for viability. [src: essential_metabolome]

The essential-gene measurements used RB-TnSeq, or random-barcode transposon sequencing, in rich media, where nutrient supplementation can make biosynthetic genes appear non-essential. [src: essential_metabolome]

Consequently, the dataset cannot distinguish genes essential for biosynthesis from genes essential for viability under the tested rich-media conditions. [src: essential_metabolome]

This caveat supports [[concepts/condition-specific-fitness]] because the apparent importance of a biosynthetic pathway depends on which nutrients are supplied and which environmental condition is assayed. [src: essential_metabolome]

It also qualifies the interpretation of [[concepts/gene-essentiality]]: pathway completeness and essential-gene measurements address related but non-identical questions about metabolic capacity and condition-specific viability. [src: essential_metabolome]

## Coverage and Inference Limits

The [[entities/escherichia-coli]] K-12 genome was absent from the GapMind results in the KBase pangenome collection, with 0 GapMind predictions for the Keio genome GCF_000005845.2. [src: essential_metabolome]

The mapped genomes had 694 predictions for *D. vulgaris* GCF_000195755.1, 694 for *S. oneidensis* GCF_000146165.2, 1,041 for *P. putida* GCF_000007565.2, 745 for *P. aeruginosa* GCF_000006765.1, 694 for *C. vibrioides* GCF_000022005.1, 1,735 for *S. meliloti* GCF_000006965.1, and 1,786 for *A. brasilense* GCF_000011365.1. [src: essential_metabolome]

The report attributes the missing *E. coli* coverage to its exclusion from [[entities/gtdb]] pangenome construction because it had too many genomes for species-level analysis. [src: essential_metabolome]

This coverage issue reduced the intended analysis from 45 Fitness Browser organisms to a 7-organism pilot and leaves coverage for the remaining 38 organisms unknown. [src: essential_metabolome]

The source data included 305M GapMind predictions across 293K genomes in [[entities/kbase-ke-pangenome]], 859 universally essential gene families across 45 organisms, 80 pathway-completeness records, 18 amino-acid pathway records, 62 carbon-pathway records, 7,389 raw GapMind predictions for the selected organisms, and 8 manual organism-to-genome mappings. [src: essential_metabolome]

These missing-data and sampling constraints connect to [[concepts/callability-limited-comparative-inference]] because an absent prediction can reflect collection or mapping coverage rather than biological absence. [src: essential_metabolome]

## Open Directions

- Inspect lower-confidence GapMind predictions and records with a steps_missing status for *D. vulgaris* to determine whether the serine gap reflects a near-complete pathway rather than a true absence. [src: essential_metabolome]
- Test *D. vulgaris* growth on serine-free minimal medium and matched serine-supplemented medium to distinguish physiological auxotrophy from a computational detection gap. [src: essential_metabolome]
- Expand organism-to-genome mapping across the remaining 38 organisms and rerun GapMind to test whether the 17-of-18 amino-acid completeness pattern persists across broader phylogenetic coverage. [src: essential_metabolome]
- Combine GapMind with [[entities/eggnog]] EC-to-[[entities/kegg]] pathway analysis to test whether independent annotation pipelines recover the same serine and carbon-source capacities. [src: essential_metabolome]
- Link essential-gene calls directly to pathway membership and assay organisms in defined media to test whether predicted pathway completeness corresponds to condition-specific biosynthetic essentiality. [src: essential_metabolome]
- Stratify pathway gaps by phylogeny and ecology after expanding the sample to test whether nutrient dependence is associated with lineage or environment. [src: essential_metabolome]
