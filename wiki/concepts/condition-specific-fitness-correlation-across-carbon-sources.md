---
type: "Concept"
description: "How mutant growth fitness correlates across carbon-source conditions and what that shows about shared versus independent gene sets; stops at single-organism data."
sources: ["summaries/acinetobacter_adp1_explorer__REPORT.md", "summaries/adp1_deletion_phenotypes__REPORT.md", "summaries/adp1_triple_essentiality__REPORT.md", "summaries/fw300_metabolic_consistency__REPORT.md"]
---
# Condition-specific fitness correlation across carbon sources

Condition-specific fitness correlation across carbon sources. ADP1 fitness across carbon sources is moderately correlated overall, with urea standing out as largely independent. [src: acinetobacter_adp1_explorer] The evidence is from one organism, Acinetobacter baylyi ADP1, plus a side comparison from one Fitness Browser strain, FW300-N2E3. These are single-organism results.

## Literature Context

The candidate literature is thin and only partly relevant to carbon-source fitness correlation. The most relevant paper is a genome-wide fitness study in Shewanella oneidensis MR-1. It used pools of tagged transposon mutants to probe the mutant fitness of 3,355 genes in 121 diverse conditions, including different growth substrates, alternative electron acceptors, stresses and motility [PMID 22125499](https://pubmed.ncbi.nlm.nih.gov/22125499/). It found that 2,350 genes had a fitness pattern significantly different from random. Of these, 1,230 genes (37% of the total assayed) had enough signal to show strong biological correlations [PMID 22125499](https://pubmed.ncbi.nlm.nih.gov/22125499/). The authors used fitness patterns to propose specific molecular functions for 40 genes or operons that lacked specific annotations or had incomplete ones [PMID 22125499](https://pubmed.ncbi.nlm.nih.gov/22125499/). They also reported that gene expression and mutant fitness are poorly correlated [PMID 22125499](https://pubmed.ncbi.nlm.nih.gov/22125499/). Only the abstract was available, so details such as per-condition-pair correlations are not known here.

The second candidate studied Dickeya solani transcriptional units induced by plant tissues. It screened 10,000 Tn5 reporter mutants and found 210 with plant tissue-dependent expression. It then characterized 13 of them, including carbon and nitrogen source utilization phenotypes [PMID 32983224](https://pubmed.ncbi.nlm.nih.gov/32983224/). That work measures reporter induction and selected phenotypes, not pairwise fitness correlation across carbon sources. It therefore gives little direct evidence for or against the corpus's claims.

The corpus reports a moderate mean pairwise correlation of r = 0.44 across 8 ADP1 carbon sources, with urea largely independent (r = 0.11 with quinate and r = 0.12-0.28 with the other conditions). It also reports a separate mean defect correlation of 0.38 from a different analysis. The Shewanella study is consistent with the general idea that fitness profiles across many conditions carry biologically meaningful correlation structure [PMID 22125499](https://pubmed.ncbi.nlm.nih.gov/22125499/). It does not test carbon-source pairs, urea independence or the housekeeping-versus-substrate-specific split, so it neither confirms nor contradicts those results. The FW300-N2E3 observation, in which amino acid biosynthesis genes were significant in all 21 conditions, has no counterpart in the candidates. The Shewanella abstract does not report such a split.

The corpus's specific findings are therefore not covered by these papers. The ADP1 urea independence, the 8-carbon-source correlation values and the entry-point hypothesis remain novel relative to this evidence. They are single-organism results, and the entry-point explanation is an untested hypothesis. The Shewanella dataset suggests a route for testing them: apply the same pairwise analysis to a multi-condition fitness compendium, as the page's open directions propose.

## ADP1 pairwise correlations

ADP1 fitness across 8 carbon sources is moderately correlated, with a few outliers. [src: acinetobacter_adp1_explorer, adp1_deletion_phenotypes, adp1_triple_essentiality]

- The mean pairwise r across the 8 carbon sources is 0.44. [src: acinetobacter_adp1_explorer]
- One analysis reports the highest pairwise Pearson correlation as acetate–butanediol, r = 0.58. It reports a median of r = 0.25 across all 28 pairs. [src: adp1_deletion_phenotypes]
- Butanediol–acetate (r = 0.58) and butanediol–lactate (r = 0.53) are the strongest correlations. The report calls them consistent with shared central carbon metabolism. [src: acinetobacter_adp1_explorer]
- The ADP1 database supplies this fitness data. ADP1 is absent from the Fitness Browser, so the database is the only source of condition-specific fitness data for this organism in the KBase Data Lakehouse. Coverage of mutant growth fitness on the 8 carbon sources is 39%. [src: acinetobacter_adp1_explorer] See adp1 sqlite database berdl tables db.

A separate analysis of defect calls gives a mean pairwise defect correlation of 0.38 (range -0.03 to 1.0). The authors read this as moderate but incomplete overlap in the genes required on different carbon sources. [src: adp1_triple_essentiality] The 0.44 and 0.38 values come from different analyses, so I do not compare them directly.

## Urea as a largely independent condition

Urea fitness is nearly uncorrelated with quinate (r = 0.11) and weakly correlated with all other conditions (r = 0.12-0.28). The report suggests urea catabolism involves a largely independent set of genes. [src: acinetobacter_adp1_explorer] This is an inference from correlation. The report proposes identifying the urea-specific genes and examining their pangenome conservation. [src: acinetobacter_adp1_explorer]

## Independence versus overlap in defect calls

Among 478 ADP1 genes, 333 (70%) showed condition-specific growth defects. Ten (2%) had defects on all 8 conditions, and 135 (28%) had no defect on any condition. [src: adp1_triple_essentiality]

The "any defect" background rate is 72% of 478 genes. If conditions were independent, 90% would be expected. The original study attributes the lower observed value to inter-condition correlation. [src: adp1_triple_essentiality] The Q25 threshold flags about 25% of genes per condition, so aggregating across 8 conditions gives a high background rate by design (1 − 0.75⁸ = 90% under independence). [src: adp1_triple_essentiality]

## Why conditions might be independent

The ADP1 report contrasts its largely independent carbon-source requirements with correlated fitness profiles in many *E. coli* chemical-genomics conditions (Nichols et al. 2011). [src: adp1_deletion_phenotypes] It proposes that the difference reflects the diversity of metabolic entry points, because each carbon source enters central metabolism at a different point. [src: adp1_deletion_phenotypes] This is a hypothesis, not a tested result.

## Shared genes in FW300-N2E3

In FW300-N2E3 Fitness Browser data, 231 genes were significant in 3+ metabolite conditions. [src: fw300_metabolic_consistency] The top 18 genes, significant in all 21 conditions, are amino acid biosynthesis enzymes. They include homoserine O-acetyltransferase (methionine), ATP (adenosine triphosphate) phosphoribosyltransferase (histidine), dihydroxy-acid dehydratase (branched-chain amino acids), isopropylmalate dehydrogenase (leucine), shikimate dehydrogenase (aromatic amino acids) and imidazoleglycerol-phosphate dehydratase (histidine). [src: fw300_metabolic_consistency]

The report interprets these as essential for growth on any minimal medium, so they reflect housekeeping fitness and not substrate-specific metabolism. [src: fw300_metabolic_consistency] It identifies about 370 genes significant in only 1-2 conditions as truly substrate-specific. Examples are carnitine-specific transporters, lactate dehydrogenases and trehalose-specific phosphotransferases. [src: fw300_metabolic_consistency] See [[concepts/housekeeping-versus-substrate-specific-fitness-genes]] and condition specific gene importance across carbon sources.

## Open Directions

- Identify the ADP1 urea-specific genes and test their pangenome conservation. This would show whether the independence of urea is a conserved trait.
- Recompute the ADP1 correlations after removing the housekeeping and biosynthesis genes that are important in every condition. This would show how much of the moderate mean r (0.44) comes from shared core genes.
- Test the metabolic entry-point hypothesis by relating correlation between carbon-source pairs to the distance between their entry points in central metabolism.
- Run the same pairwise analysis on Fitness Browser organisms with many carbon sources. This would test whether ADP1's pattern holds outside one organism.
