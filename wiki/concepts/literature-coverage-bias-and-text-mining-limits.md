---
type: "Concept"
description: "How research attention in text-mined gene-literature collections concentrates on a few organisms and genes, and how text-mining methods, open-access restriction, curated subsets and heuristic classification limit what literature counts mean."
sources: ["summaries/paperblast_explorer__REPORT.md"]
---
# Literature coverage bias and text-mining limits

This page covers literature coverage bias and text-mining limits in gene-literature collections.

All evidence comes from one report on [[entities/paperblast]] (see [[summaries/paperblast_explorer__REPORT]]). Homo sapiens alone accounts for 46.7% of all gene-paper records. [src: paperblast_explorer] The report also flags several limits on how to read such counts. [src: paperblast_explorer]

## Literature Context

Only one of the three candidate papers bears on text-mining limits. [PMID 42754603](https://pubmed.ncbi.nlm.nih.gov/42754603/) describes PubMind, a large-language-model framework that extracts variant-function-disease associations from biomedical text. It was applied to >41 million PubMed abstracts and >5 million full-text articles and produced a database of ~1.3 million unique variants. The authors say curated resources such as ClinVar and HGMD are limited by coverage, submission bias, update frequency and sparse annotation. Only ~10% of PubMind variants overlap with ClinVar, and >80% of those overlapping variants have concordant pathogenicity labels. The benchmark reports >90% accuracy for variant recognition and 99% precision for disease extraction. Those figures describe the quality of what was extracted. The abstract gives no recall or coverage measure, so it does not show how much literature or how many findings the mined collection misses. The other two candidates, a study of online negative emotions in an urban relocation ([PMID 39550506](https://pubmed.ncbi.nlm.nih.gov/39550506/)) and a Bayesian risk-stratification model for substance use disorder ([PMID 20169014](https://pubmed.ncbi.nlm.nih.gov/20169014/)), do not address gene-literature coverage and are not used here.

The hub's findings come from a single report on [[entities/paperblast]]. The report finds heavy concentration: Homo sapiens accounts for 46.7% of gene-paper records, and 65.6% of the 841K genes with a text-mined link have exactly 1 paper. Its caution that curated subsets are partial fits the PubMind authors' view that curated resources have coverage and submission bias. The report notes that PaperBLAST includes approximately 19% of SwissProt, and PubMind's low overlap with ClinVar (~10%) likewise suggests that mined and curated collections capture different material. These are different domains, human variants versus gene-paper links, so this is consistent in spirit only and is not a direct replication.

The report's central caveat is that it has no negative controls. It cannot separate genuinely unstudied genes from genes whose literature was missed by text mining. PubMind's accuracy and precision figures do not close that gap, because they say nothing about missed records. Recall against a gold-standard set would be needed. The candidates therefore leave the hub's claims about organism and gene concentration, open-access restriction and heuristic domain classification untested. Those claims remain novel to this corpus and rest on one report. The Open Directions proposal for a negative-control gene set stays unmet by this literature.

## Concentration across organisms

Literature is concentrated in a handful of organisms. The top 5 organisms (H. sapiens, M. musculus, R. norvegicus, A. thaliana, D. melanogaster) capture 72.8%. [src: paperblast_explorer] Of 20,723 organisms with any literature, the top 1,000 capture 94.2%, and the remaining 19,723 share 5.8%. [src: paperblast_explorer] The organism-level Gini coefficient is 0.967, where 1.0 is perfect inequality. [src: paperblast_explorer]

Among 15,312 bacterial organisms, the top 100 capture 44.3% of bacterial literature. [src: paperblast_explorer] The top 3 bacteria are well-known pathogens or model organisms: [[entities/mycobacterium-tuberculosis]] H37Rv (9,079 papers), [[entities/escherichia-coli]] K-12 (8,860) and [[entities/pseudomonas-aeruginosa-pao1]] (5,928). [src: paperblast_explorer] The report states that environmental and non-pathogenic organisms are dramatically underrepresented. [src: paperblast_explorer]

The collection's 1.1M genes span 27,718 organisms across all domains of life. [src: paperblast_explorer] Bacteria dominate by organism count (6,000), but Eukarya dominate by gene count (291K), owing to over-representation of human and model-organism genes. [src: paperblast_explorer]

| Domain | Organisms | Genes | Share of genes |
|---|---|---|---|
| Bacteria | 5,997 | 397,544 | 35.0% [src: paperblast_explorer] |
| Unknown | 14,798 | 397,511 | 35.0% [src: paperblast_explorer] |
| Eukarya | 822 | 290,537 | 25.6% [src: paperblast_explorer] |
| Virus | 5,730 | 27,199 | 2.4% [src: paperblast_explorer] |
| Archaea | 371 | 22,575 | 2.0% [src: paperblast_explorer] |

## Concentration across genes

Gene-level attention is also skewed, though less than organism-level attention. The gene Gini coefficient is 0.669, which the report calls very high. [src: paperblast_explorer] Just 6% of genes (50K) account for 57.7% of all gene-paper links. [src: paperblast_explorer] Of 841K genes with any text-mined paper link, 551K (65.6%) have exactly 1 paper. [src: paperblast_explorer] The median is 1 paper per gene and the mean is 3.8. [src: paperblast_explorer] The histogram shows extreme right skew, with a tail extending to nearly 10,000 papers for p53. [src: paperblast_explorer]

The top 50 most-referenced genes are all human, led by p53 (9,988 papers), TNF (6,002) and EGFR (5,895). [src: paperblast_explorer] The report finds these are exclusively human cancer and disease genes. It regards this as consistent with Stoeger et al. (2018). [src: paperblast_explorer] The report describes that work as showing that the most-studied human genes keep attracting the most new research, a self-reinforcing "rich-get-richer" dynamic. [src: paperblast_explorer] It also describes the work as showing that gene attention can be predicted from chemical, physical and biological properties, so the bias is systematic, not random. [src: paperblast_explorer] The report likens the overall inequality to economic wealth inequality. [src: paperblast_explorer]

## Scale and structure of the collection

845K genes link to 1.1M unique papers through 3.2M many-to-many associations. [src: paperblast_explorer] Each gene averages 3.8 papers and each paper mentions 2.9 genes. [src: paperblast_explorer] The report treats the similar gene and paper counts (~1.1M each) as somewhat coincidental, driven by most genes having few papers and most papers mentioning few genes. [src: paperblast_explorer] In the gene table, 25.6% of genes (290K) have no text-mined paper link and rely solely on curated or GeneRIF annotations. [src: paperblast_explorer]

The database covers papers from 1951 to 2026. [src: paperblast_explorer] Publications peak around 2020–2021, with 30.6% of records from 2020 onwards. [src: paperblast_explorer] The 2025 data includes 125,438 records from 22,271 papers. [src: paperblast_explorer] There are 1,425 records from 2026, which the report reads as a snapshot taken in early 2026. [src: paperblast_explorer]

## Limits on what literature counts mean

- **Mention is not characterization.** A gene mentioned in a paper may be tangential to the study. The report suggests the 65.6% of genes with 1 paper likely include many incidental mentions. [src: paperblast_explorer]
- **Open-access restriction.** PaperBLAST mines full text only from PubMed Central. Paywalled papers are missed, which biases against fields and journals with lower open-access rates. [src: paperblast_explorer]
- **Partial curated coverage.** PaperBLAST includes approximately 19% of the full SwissProt database (~570K reviewed entries as of 2024), the subset matched to PMC open-access literature. [src: paperblast_explorer] The report says curated knowledge therefore exists for many proteins that PaperBLAST cannot connect to. [src: paperblast_explorer] See also [[entities/swiss-prot]].
- **Heuristic domain classification.** The report's organism-to-domain mapping left 14,798 organisms as Unknown, so many organisms are not easily classified by name heuristics alone. [src: paperblast_explorer] The report's text gives this as 35% of organisms. [src: paperblast_explorer] That figure does not match its own counts: 14,798 of 27,718 organisms [src: paperblast_explorer] is about 53.4%. The 35.0% in the table is Unknown's share of genes, not of organisms. [src: paperblast_explorer]
- **No negative controls.** The report cannot easily distinguish genuinely unstudied genes from genes whose literature text mining missed. [src: paperblast_explorer] This bears on any literature-defined "dark proteome" (see [[concepts/unstudied-protein-families-and-the-literature-defined-dark-proteome]]).

## Proposed follow-up in the report

The report proposes replacing heuristic domain classification with NCBI taxonomy lookup, to accurately quantify Bacteria/Archaea/Eukarya/Virus coverage. [src: paperblast_explorer] It also proposes a temporal trend analysis of whether literature concentration is rising or falling, meaning whether a broader or narrower set of genes is studied each year. [src: paperblast_explorer]

## Open Directions

- Apply the NCBI taxonomy lookup to the 14,798 Unknown organisms, to replace the heuristic domain shares with exact ones and settle the 35% discrepancy.
- Run the temporal trend analysis over the 1951–2026 span, to test whether concentration is growing.
- Build a negative-control set of genes known to be studied but absent from PMC-derived links. It would estimate how many "unstudied" genes are really missed literature.
- Compare PaperBLAST links with full SwissProt entries to measure how much curated knowledge open-access restriction hides.
