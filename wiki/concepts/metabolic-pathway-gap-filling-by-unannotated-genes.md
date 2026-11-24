---
type: "Concept"
description: "Whether dark genes co-occurring with nearly complete pathways could encode missing enzymatic steps, using GapMind pathway calls and curated domain matching; limited to organism-level co-occurrence."
sources: ["summaries/functional_dark_matter__REPORT.md"]
---
# Metabolic pathway gap-filling by unannotated genes

This page asks whether dark genes that co-occur with nearly complete metabolic pathways could encode the missing enzymatic steps. The evidence comes from one report, [[summaries/functional_dark_matter__REPORT]], which used [[entities/gapmind]] pathway calls and curated domain matching. It supports only a suggestive reading: the link is organism-level co-occurrence plus annotation compatibility, not a demonstrated gene-to-step assignment. [src: functional_dark_matter]

## Literature Context

The one candidate paper addresses a closely related problem: missing reactions, or gaps, in genome-scale metabolic networks. It reports that draft networks are incomplete even for well studied organisms such as Escherichia coli, and that the gap-filling choices made to complete them influence model predictions [PMID 26041773](https://pubmed.ncbi.nlm.nih.gov/26041773/). The authors supplemented four draft networks with all Model SEED reactions for which minimal sequence similarity was found in the genomes. They found that the number of reactions that could take part in a gap-filling solution was vast: 3,270 in the case of E. coli, where 72% of the metabolites in the draft network could connect a gap-filling solution [PMID 26041773](https://pubmed.ncbi.nlm.nih.gov/26041773/).

Two further results bear on this page. First, none of the four networks could be completed without including orphaned enzymes. The authors take this to suggest that some biochemistry integral to biomass precursor formation is uncharacterized. This result comes from the four tested draft networks only [PMID 26041773](https://pubmed.ncbi.nlm.nih.gov/26041773/). Second, many gap-filling reactions were well determined, and the resulting networks predicted gene essentiality better than networks from canonical gap filling. Essentiality predictions that were sensitive to poorly determined gap-filling reactions were of poor quality [PMID 26041773](https://pubmed.ncbi.nlm.nih.gov/26041773/).

The corpus finding is consistent with this literature in its general premise. The functional_dark_matter report found 1,256 organism-pathway pairs with nearly complete GapMind pathways where dark genes with strong fitness effects co-occur, and it suggests that some dark genes could encode the missing steps. The cited paper likewise treats gaps as places where uncharacterized biochemistry may be hiding. The two approaches differ, though. The paper tests sequence-supported gap filling in four draft metabolic models and evaluates it through gene essentiality predictions. The corpus works at the level of organism-pathway co-occurrence and annotation compatibility.

The corpus extends this literature by using dark genes with fitness phenotypes, together with EC, PFam and keyword matching, to narrow candidates to 3,186 unique dark genes. Most of these are low-confidence keyword matches. The paper's caution about poorly determined gap-filling reactions applies here. The candidate sets are large, and the corpus has not assigned any gene to a specific missing step. The paper's work therefore does not confirm the hub's hypothesis. It supports treating the hypothesis as suggestive until EC matching, structure prediction or experimental validation is done. The paper's essentiality-based evaluation is also a possible model for testing the corpus candidates. That use is a suggestion, not something either source has done.

## Co-occurrence of gaps and dark genes

GapMind gap-filling asks whether dark genes encode missing enzymatic steps in nearly complete pathways. [src: functional_dark_matter] Across 44 Fitness Browser-linked species, GapMind identified 1,256 organism-pathway pairs with nearly complete pathways (score steps_missing_low) where dark genes with strong fitness effects co-occur. [src: functional_dark_matter]

These pairs are organism-level co-occurrences. No direct gene-to-gap enzymatic matching was performed at this stage. [src: functional_dark_matter] The report says the co-occurrence suggests dark genes could encode missing steps, and confirming that needs EC (Enzyme Commission) number matching, structure prediction, or experimental validation. [src: functional_dark_matter]

### Which pathways are gapped

Carbon source utilization pathways are the most frequently gapped. [src: functional_dark_matter] Organism counts and example organisms from the report:

| Pathway | Organisms with gaps | Examples |
|---|---|---|
| Fucose utilization | 32 | Marinobacter, P. stutzeri RCH2, D. vulgaris [src: functional_dark_matter] |
| Rhamnose utilization | 31 | Marinobacter, P. putida, Phaeo [src: functional_dark_matter] |
| Sorbitol utilization | 30 | D. desulfuricans, D. vulgaris, Miyama [src: functional_dark_matter] |
| Myoinositol utilization | 28 | P. putida, P. syringae, WCS417 [src: functional_dark_matter] |
| Gluconate utilization | 26 | Marinobacter, D. desulfuricans [src: functional_dark_matter] |
| Asparagine biosynthesis (amino acid) | 24 | across diverse phyla [src: functional_dark_matter] |

### Organisms with the most gaps

Marinobacter has 49 gapped pathways, D. desulfuricans ME-23 has 45, and P. stutzeri has 45. [src: functional_dark_matter] The report notes that these organisms also have the largest dark gene complements and the most specific fitness phenotypes. It suggests their missing steps may be encoded by dark genes. [src: functional_dark_matter] This is the report's interpretation, not a tested result.

## Domain matching narrows the candidates

To go beyond organism-level co-occurrence, the report used curated pathway-enzyme mappings. These mappings combine EC prefixes, PFam families and functional keywords. They identify dark genes whose annotations are compatible with gapped pathways. [src: functional_dark_matter]

Of the 1,256 organism-pathway pairs, domain matching found 42,239 gene-pathway candidates across 3,186 unique dark genes. [src: functional_dark_matter] The 3,186 genes are drawn from 57,011 dark genes. [src: functional_dark_matter] Hits by confidence level:

- 5,398 high-confidence hits (EC prefix match). [src: functional_dark_matter]
- 4,687 medium-confidence hits (PFam family match). [src: functional_dark_matter]
- 32,154 low-confidence hits (keyword match). [src: functional_dark_matter]

The report says these candidates narrow the search from all dark genes in a gapped organism, or from organism-level co-occurrence, to genes with enzymatically plausible annotations. [src: functional_dark_matter] It rates the pathway-integration hypothesis (H1e) as suggestive, with partial domain-level support. [src: functional_dark_matter] The report describes the domain matching as only a partial answer to the co-occurrence limit. [src: functional_dark_matter]

## Limits

- Full confirmation of specific gene-to-step assignments requires AlphaFold structure prediction or experimental enzymology. [src: functional_dark_matter]
- GapMind covers amino acid biosynthesis and carbon utilization, not all metabolic functions. [src: functional_dark_matter] Dark genes with signaling, regulatory or structural roles are not captured. [src: functional_dark_matter]
- Most candidates are low-confidence keyword matches. [src: functional_dark_matter]

See [[concepts/reliability-and-coverage-limits-of-gapmind-pathway-predictions]] for wider limits on GapMind predictions.

## Open Directions

- Match the 5,398 high-confidence EC-prefix candidates to the specific missing step in each gapped pathway. This would turn organism-level co-occurrence into gene-to-step hypotheses.
- Run AlphaFold structure prediction on the top candidates in Marinobacter, D. desulfuricans ME-23 and P. stutzeri, which have the most gapped pathways. This tests the proposed link to missing steps.
- Test growth on gapped carbon sources, such as fucose, rhamnose and sorbitol, in strains with candidate dark genes. Pair this with the existing fitness data to check enzymatic function directly.
- Compare the dark-gene candidate rate in gapped pathways with a background set of non-gapped pathways. This would test whether the enrichment is specific.
- Extend the pathway mappings to regulatory and structural functions. This would address the coverage gap.
