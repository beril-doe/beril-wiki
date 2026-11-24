---
type: "Concept"
description: "Caveats on assay design, cohort selection, biofilm relevance and omitted nutrients that bound inference from laboratory inhibition data."
sources: ["summaries/cf_formulation_design__REPORT.md", "summaries/pitfalls.md"]
---
# Generalizability limits of planktonic single-strain inhibition assays

Planktonic, single-strain inhibition assays for a cystic fibrosis (CF) formulation are limited by the reference strain, the growth mode, the nutrients tested and the cohort. [src: cf_formulation_design] The evidence comes from one project, [[summaries/cf_formulation_design__REPORT|cf_formulation_design]], and its own stated caveats, plus one cross-project pitfall entry. [src: pitfalls]

## Literature Context

Two candidate papers address the gap this page identifies, which is that planktonic susceptibility or inhibition data may not predict behaviour in the cystic fibrosis (CF) lung. A review of susceptibility testing in biofilm-growing bacteria links the lack of correlation between conventional susceptibility results and therapeutic success in chronic infections to the use of planktonic rather than biofilm-growing bacteria. It uses chronic *Pseudomonas aeruginosa* infection in CF as its leading example [PMID 24766583](https://pubmed.ncbi.nlm.nih.gov/24766583/). The review also reports that several studies found very significant quantitative and qualitative differences in antibiotic effects on planktonic versus biofilm bacteria. It notes that standardization of procedures, parameters and breakpoints is still needed before such tests reach routine clinical use. This is an abstract-level review, not a direct test of the formulation approach in the hub.

An experimental study built an artificial sputum medium (ASM) microtitre assay containing amino acids, mucin and free DNA. It tested tobramycin against 15 *P. aeruginosa* isolates [PMID 22711026](https://pubmed.ncbi.nlm.nih.gov/22711026/). Compared with standard broth growth, there was some evidence of increased MIC values in ASM. The largest differences appeared under microaerophilic conditions, with resistance up to >128 fold higher than in aerobic assays. The authors also criticize existing methods for relying on single or a few isolates grown aerobically and planktonically. This study used an antibiotic, not competing commensals, and it was in vitro.

A third paper is related but does not address the planktonic-versus-clinical testing gap. It combined flow-cell biofilms grown in an artificial CF sputum medium with a 2D mathematical model to examine inhaled silver carbene complex (SCC) treatment of *P. aeruginosa* biofilms [PMID 23518337](https://pubmed.ncbi.nlm.nih.gov/23518337/). In the simulations, environmental inactivation of SCC was critical for aqueous SCC but not for SCC-polymer treatment. Polymer particle degradation rate was an important parameter that could be chosen optimally given environmental conditions and bacterial susceptibility. It is an in vitro and in silico study. It shows that a CF-like biofilm model can be built, but it says nothing about single-strain inhibition assays.

The corpus's caveats are consistent with this literature. The hub says planktonic PA14 inhibition may not translate to biofilm disruption in the structured CF lung. Its proposed CFBE biofilm challenge, with PA14 CFU and biomass measured over 48 hours, matches the field's move toward biofilm and sputum-like models [PMID 24766583](https://pubmed.ncbi.nlm.nih.gov/24766583/). The hub's concern about omitted nutrients such as mucins is also in line with ASM work, which includes mucin and DNA [PMID 22711026](https://pubmed.ncbi.nlm.nih.gov/22711026/). The candidates do not cover the hub's other limits: PA14 as a minority ExoU+ strain, GC-confounded codon usage bias, and cohort enrichment in the 142-isolate core. Those points are specific to this corpus and remain untested against the literature here. The candidates concern antibiotics, not commensal-based formulations, so the corpus's extension of the planktonic-assay concern to inhibition by competing organisms is an extrapolation, not an established finding.

## Reference strain

All inhibition assays used PA14, an ExoU+ and Pel-only strain that represents <5% of CF *Pseudomonas aeruginosa* isolates. [src: cf_formulation_design] T3SS (type III secretion system) typing of 6,760 PA genomes found CF isolates are 94% ExoS+, while PA14 is ExoU+. [src: cf_formulation_design] The pitfalls digest states the consequence: the assays test the formulation against a minority variant. [src: pitfalls] See [[concepts/pseudomonas-aeruginosa-strain-diversity-and-representativeness-of-reference-strains]] and [[entities/pseudomonas-aeruginosa-pa14]].

## Planktonic versus biofilm growth

The assays measure only planktonic competition, but PA14 in CF lungs grows mainly in biofilms. There, metabolic dynamics, diffusion gradients and spatial structure differ substantially. [src: cf_formulation_design] Planktonic inhibition may therefore not translate to biofilm disruption in the structured CF lung. [src: cf_formulation_design] The report proposes growing PA14 biofilms on CF bronchial epithelial cell cultures (CFBE), challenging them with formulation organisms, and measuring PA14 CFU and biofilm biomass over 48 hours. [src: cf_formulation_design]

## Nutrients and measurements

The 22 tested carbon sources cover major amino acids and glucose/lactate. They omit mucins, lipids, iron, polyamines, and the sugar alcohols that genomic analysis predicts to be important. [src: cf_formulation_design] The CF lung holds nutrients beyond amino acids, and iron limitation or acidic pH may reveal further competitive advantages or vulnerabilities. [src: cf_formulation_design] The report proposes testing the 5 core species on N-acetylglucosamine, putrescine/spermidine, iron-limited conditions and pH 6.5 (CF sputum pH). [src: cf_formulation_design] See also [[entities/cystic-fibrosis-sputum]].

Endpoint optical density (OD) shows whether an organism can grow on a substrate, not how fast. [src: cf_formulation_design] Genomic proxies do not fill this gap. Codon usage bias (CUB) comparisons across species are confounded by GC content, which ranges from 31% for *G. sanguinis* to 73% for *M. luteus*. Extreme GC composition inflates CUB scores regardless of growth optimization. [src: cf_formulation_design] CUB therefore cannot reliably distinguish growth rate potential, and laboratory growth data remain the definitive measure of competitive dynamics on amino acid substrates. [src: cf_formulation_design] The report also notes that the *P. aeruginosa* genome (6.58 Mb, 6,177 CDS) is 2.5–3× larger than the commensal genomes (2.1–2.7 Mb, 2,200–3,000 CDS). [src: cf_formulation_design]

## Cohort selection

The PROTECT isolate collection reflects the typical CF airway microbiome plus deliberate oversampling of pathogens. [src: cf_formulation_design] The 142-isolate core cohort is the overlap of inhibition and carbon utilization data. That overlap limits multivariate model power, and growth kinetics exist for only 32 isolates. [src: cf_formulation_design] The cohort covers 62 of 211 species (29%). [src: cf_formulation_design] It is enriched for species with multiple assay types, so it may over-represent organisms prioritized for deeper characterization. [src: cf_formulation_design]

The enrichment is visible by genus. The core cohort versus the full collection is Rothia 22% vs 6% [src: cf_formulation_design], Streptococcus 15% vs 8% [src: cf_formulation_design], Neisseria 8% vs 3% [src: cf_formulation_design], and Gemella 7% vs 3%. [src: cf_formulation_design] The report attributes this to deliberate selection of inhibition-tested species. [src: cf_formulation_design] It expects the metabolic overlap–inhibition relationship to generalize, but the absolute R² may differ for under-represented taxa. [src: cf_formulation_design] Related reasoning appears in [[concepts/community-level-niche-coverage-and-resource-depletion-for-competitive-exclusion]].

## Open Directions

- Repeat the inhibition assays with ExoS+ CF *P. aeruginosa* isolates alongside PA14. This would show how far the minority-variant result transfers.
- Run the proposed CFBE biofilm challenge with 48-hour CFU and biomass readouts. It would test whether planktonic inhibition predicts biofilm disruption.
- Extend the substrate panel to N-acetylglucosamine, polyamines, iron limitation and pH 6.5. It would close the nutrient gap.
- Collect growth kinetics beyond the 32 isolates, rather than endpoint OD, to replace the GC-confounded CUB proxy.
- Refit the overlap–inhibition model on a cohort balanced for genus. It would show how R² changes for under-represented taxa.
