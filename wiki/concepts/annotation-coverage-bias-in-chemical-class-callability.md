---
type: "Concept"
description: "Covers whether the chemical class or physicochemical properties of a compound predict whether its catabolism can be called from genomes, and how annotation coverage confounds this; it stops at class-level tests with small numbers of callables."
sources: ["summaries/enigma_carbon_census_1__REPORT.md"]
---
# Annotation-coverage bias in chemical-class callability

This page covers annotation-coverage bias in chemical-class callability. In the ENIGMA Carbon Census, callable compounds look smaller and simpler than dark ones. [src: enigma_carbon_census_1] The report reads this partly as an annotation-coverage ceiling. [src: enigma_carbon_census_1] The class-gradient test is null, and the evidence is directional only. [src: enigma_carbon_census_1] See also [[summaries/enigma_carbon_census_1__REPORT]].

## Literature Context

The candidate papers do not test whether chemical class or physicochemical properties predict genome-based callability of catabolism. They do bear on the annotation-coverage side of the question. One review notes that microbial metabolism is considered well understood, yet researchers still find non-canonical pathways, unforeseen reactions and unexpected metabolites that contradict the expected canon [PMID 39126421](https://pubmed.ncbi.nlm.nih.gov/39126421/). That is a general caution that annotation-based inference is incomplete. It is not a measurement of class-specific gaps.

A pathway-level comparison for trehalose metabolism in Variovorax sp. PAMC28711 is more direct. The KEGG pathway database lacked one enzyme (maltooligosyl-trehalose synthase, EC 5.4.99.15), and MetaCyc was also incomplete. RAST annotation of the whole genome found the enzymes that KEGG and MetaCyc lacked [PMID 34991451](https://pubmed.ncbi.nlm.nih.gov/34991451/). This is a single organism and a single pathway, so it shows only that the resource used shapes what can be called. A methods review of COBRA (constraint-based reconstruction and analysis) models lists identifying missing enzymatic functions in annotated genomes as a routine use of curation [PMID 34719001](https://pubmed.ncbi.nlm.nih.gov/34719001/). A fusion/fission screen in Archaea found that around 25% of the identified families lack functional annotation in both composite and split states [PMID 38700364](https://pubmed.ncbi.nlm.nih.gov/38700364/). Tools such as MetaPathPredict, which predicts KEGG module presence in incomplete genomes, address coverage gaps in the genomes themselves. They do not address gaps in compound-level annotation [PMID 38696239](https://pubmed.ncbi.nlm.nih.gov/38696239/).

Against this background, the corpus's central reading is consistent with the literature. The ENIGMA Carbon Census found that callable compounds were smaller and simpler, with median Complexity 133 versus 207 for dark compounds (p=0.034). The report treats this partly as an annotation-coverage ceiling, because KEGG, ModelSEED and genome_depot are deep for aromatics and phthalates and absent for most alkaloids and terpenoids. The candidate papers support only the general premise that database coverage is uneven and that the resource chosen changes the result. None of them shows a chemical-class gradient in coverage.

The corpus's own class-level result is null. The χ² test on the 8 enigma_isolate_call callables gave χ²=5.07, p=0.53 (df=6), so uniform coverage across classes was not rejected. With about 9 callables in 83 compounds, the design is underpowered, and the descriptor contrasts use uncorrected p values. The literature here neither confirms nor contradicts these class-level numbers. The link between simplicity and annotation depth is therefore a novel, untested hypothesis in this corpus. It is not an established finding. The open directions, which regress descriptors on per-compound reaction counts and compare within aromatics, would test it. No candidate paper has done that.

## Physicochemical contrast

The report contrasted PubChem physicochemical descriptors of callable and dark compounds across all 83 census compounds. [src: enigma_carbon_census_1] Callable compounds were smaller and structurally simpler. Median Complexity was 133 versus 207 for dark compounds (p=0.034). [src: enigma_carbon_census_1] MolecularWeight was 152 versus 179 (p=0.066). [src: enigma_carbon_census_1] HeavyAtomCount was 11 versus 13 (p=0.057). [src: enigma_carbon_census_1] Polarity was directionally higher in callables, with TPSA 57 versus 41 [src: enigma_carbon_census_1] and H-bond donors 2 versus 1. [src: enigma_carbon_census_1]

With only n=9 callable compounds, this comparison is directional, not inferential. It uses [[entities/mann-whitney-u-test|Mann–Whitney]] tests reported as directions with uncorrected p values. [src: enigma_carbon_census_1] The contrasts are descriptive, not calibrated significance. [src: enigma_carbon_census_1]

## Annotation coverage as confounder

The report reads the simplicity signal as at least as much an annotation-coverage ceiling as a biological-bioavailability effect. KEGG, [[entities/modelseed-biochemistry|ModelSEED]] and genome_depot annotate simple, common, pollutant-adjacent aromatics. [src: enigma_carbon_census_1] Catabolic knowledge in the queried resources is deep for the aromatic/phthalate subset and absent for most alkaloids and terpenoids. [src: enigma_carbon_census_1] The aromatic/phthalate concentration of callables is unaffected by the xanthine caveat. It directionally matches curated biodegradation knowledge and KEGG coverage. [src: enigma_carbon_census_1]

## Class-level test

The pre-registered null of uniform coverage across classes was not rejected. A χ² test on the 8 enigma_isolate_call callables by class gave χ²=5.07, p=0.53 (df=6). [src: enigma_carbon_census_1] Coverage by class was:

| Class | Callable / total |
|---|---|
| Shikimates | 5/25 [src: enigma_carbon_census_1] |
| Alkaloids | 2/26 [src: enigma_carbon_census_1] |
| Terpenoids | 1/17 [src: enigma_carbon_census_1] |
| Fatty acids | 0/10 [src: enigma_carbon_census_1] |
| Polyketides | 0/2 [src: enigma_carbon_census_1] |
| AA/Peptides | 0/2 [src: enigma_carbon_census_1] |
| mixed | 0/1 [src: enigma_carbon_census_1] |

Adding the single measured-fitness lauric acid (Fatty acids 1/10) does not change the verdict. [src: enigma_carbon_census_1] See [[concepts/measured-fitness-as-independent-evidence-of-carbon-utilization]] for fitness as independent evidence.

## Tensions

- Callables are smaller and simpler (Complexity p=0.034) [src: enigma_carbon_census_1], yet the report reads this partly as an annotation artefact rather than biology. [src: enigma_carbon_census_1]
- Callables cluster in shikimates (5/25) [src: enigma_carbon_census_1], yet the formal class test does not reject uniform coverage. [src: enigma_carbon_census_1]

## Caveats

With about 9 callables across 83 compounds, the design is underpowered to detect a class gradient. The directional pattern is confounded with annotation coverage, not a clean biological degradability gradient. [src: enigma_carbon_census_1] H1 is not formally supported. The per-class Tier-0 list remains a useful descriptive enrichment-design deliverable. [src: enigma_carbon_census_1]

## Open Directions

- Repeat the class and descriptor tests after adding callables from measured fitness or other independent evidence, to raise power beyond n=9.
- Test descriptors against annotation depth (for example, the number of KEGG or ModelSEED reactions per compound) to separate coverage from biology.
- Run the comparison within the aromatic class, where annotation is deep, to see whether simplicity still predicts callability.
- Test whether callability in alkaloids and terpenoids rises after targeted curation of their catabolic pathways.
