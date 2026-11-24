---
type: "Concept"
description: "How growth defects of deletion mutants vary across carbon sources and overlap between conditions; stops at model predictions."
sources: ["summaries/acinetobacter_adp1_explorer__REPORT.md", "summaries/adp1_deletion_phenotypes__REPORT.md", "summaries/adp1_triple_essentiality__REPORT.md"]
---
# Condition-specific gene importance across carbon sources

In Acinetobacter baylyi ADP1, growth defects of deletion mutants depend strongly on the carbon source, and conditions overlap only moderately in which genes matter. [src: adp1_deletion_phenotypes, adp1_triple_essentiality] The evidence comes from one organism and one set of 8 carbon sources, analysed in three reports. The numbers differ between reports, so each is stated with its own source. See [[entities/acinetobacter-baylyi-adp1]] and [[concepts/condition-specific-fitness-correlation-across-carbon-sources]].

## Literature Context

The candidate literature for this page is thin. Only one retrieved paper bears directly on how gene importance changes across growth conditions. It is a pooled CRISPR interference (CRISPRi, gene repression) screen of the cyanobacterium Synechocystis sp. PCC 6803. The library had 21,705 individual mutants and was screened in 11 bioreactor-controlled conditions that spanned multiple light regimes and carbon sources [PMID 37494719](https://pubmed.ncbi.nlm.nih.gov/37494719/). The authors report that repressing some genes helped growth in one condition and generally hurt it in others. Examples include light-harvesting antenna components at high light and PSII subunits during photoheterotrophy [PMID 37494719](https://pubmed.ncbi.nlm.nih.gov/37494719/). They also report that the data set assigns condition-specific importance to many previously unannotated genes. Phosphoribulokinase, glyceraldehyde-3-phosphate dehydrogenase and the small protein CP12 were critical for mixotrophy and photoheterotrophy [PMID 37494719](https://pubmed.ncbi.nlm.nih.gov/37494719/). These points come from the abstract only, and the paper is a different organism, a different perturbation type (repression rather than deletion) and a different condition set (light plus carbon) from the ADP1 work.

The second candidate, a yeast nucleosome-positioning model that draws on cells grown on diverse carbon sources, concerns promoter chromatin and transcription. It does not address mutant growth defects, so it gives no evidence for this page's claims.

The corpus's central finding is that ADP1 deletion-mutant growth defects depend strongly on carbon source and that conditions overlap only moderately. The reports give a mean pairwise defect correlation of 0.38, and 70% of 478 genes had defects on some but not all conditions. This is qualitatively **consistent** with the Synechocystis result that gene importance is condition-dependent rather than fixed [PMID 37494719](https://pubmed.ncbi.nlm.nih.gov/37494719/). The two studies agree on the direction of the effect, and the corpus rests on one organism and 8 carbon sources. The Synechocystis abstract gives no correlation or overlap figure, so the numbers cannot be compared.

Several corpus findings have no counterpart in the retrieved literature. These are the demanding, moderate and robust tiers of carbon sources, the urea outlier with its largely independent gene set, and the 10 genes defective on all 8 conditions. They are **novel** relative to these candidates, and the urea interpretation remains a hypothesis. The Synechocystis finding that suboptimal gene regulation may trade growth speed for robustness [PMID 37494719](https://pubmed.ncbi.nlm.nih.gov/37494719/) suggests a testable extension. One could ask whether ADP1 genes with defects in only some conditions show comparable tradeoffs. The deletion data cannot test this, because a deletion only removes a gene and does not tune its expression. The retrieved literature does not contradict any corpus claim.

## Conditions differ in how demanding they are

The 8 carbon sources fall into demanding, moderate and robust tiers by the fraction of genes with growth defects, and the tiers hold across multiple thresholds. [src: adp1_deletion_phenotypes] Mean growth ratios span a 3.3-fold range, from 0.41 for urea to 1.36 for quinate. [src: adp1_deletion_phenotypes]

- Demanding (urea, acetate, butanediol): mean growth ratio 0.41–0.65, with defects at ratio < 0.8 in 95–100% of genes. [src: adp1_deletion_phenotypes]
- Moderate (asparagine, lactate): mean growth ratio 0.80–0.82, with defects at ratio < 0.8 in 37–45% of genes. [src: adp1_deletion_phenotypes]
- Robust (glucarate, glucose, quinate): mean growth ratio 1.25–1.36, with defects at ratio < 0.8 in 0.5–2.4% of genes. [src: adp1_deletion_phenotypes]

Urea is the most demanding: 97.9% of genes show severe defects at ratio < 0.5. Quinate is the most robust, with only 1.6% defective. [src: adp1_deletion_phenotypes]

## Overlap between conditions is moderate

Gene sets needed on different carbon sources overlap only partly. The mean pairwise defect correlation was 0.38 (range −0.03 to 1.0), which indicates moderate but incomplete overlap. [src: adp1_triple_essentiality] A separate analysis reports a mean pairwise fitness correlation of r = 0.44 across the 8 sources, with notable outliers. [src: acinetobacter_adp1_explorer] A third reports a highest pairwise Pearson correlation of r = 0.58 (acetate–butanediol) and a median of r = 0.25 across all 28 pairs. [src: adp1_deletion_phenotypes] These figures come from different reports and are not directly comparable.

The strongest pairs are butanediol–acetate (r = 0.58) and butanediol–lactate (r = 0.53). The report reads these as consistent with shared central carbon metabolism. [src: acinetobacter_adp1_explorer]

Urea is the outlier. Its fitness is nearly uncorrelated with quinate (r = 0.11) and weakly correlated with all other conditions (r = 0.12–0.28). [src: acinetobacter_adp1_explorer] One report suggests that urea catabolism involves a largely independent gene set. [src: acinetobacter_adp1_explorer] This is an interpretation of the correlations, not a direct test of the gene sets.

## Condition-specific versus universal defects

Of 478 genes, 333 (70%) showed defects on some but not all conditions. [src: adp1_triple_essentiality] Ten genes (2%) had defects on all 8 conditions. [src: adp1_triple_essentiality] 135 genes (28%) had no defect on any condition. [src: adp1_triple_essentiality] The report states that the original study also found 70% of genes with condition-specific defects. [src: adp1_triple_essentiality]

The report treats growth importance as condition-dependent and continuous. [src: adp1_triple_essentiality] It measures this as growth defect magnitude per condition, from growth rate on specific substrates. [src: adp1_triple_essentiality] It attributes the variation to metabolic pathway usage differing by substrate. [src: adp1_triple_essentiality] This attribution is the report's interpretation. See [[concepts/continuous-versus-discrete-structure-of-condition-dependent-gene-essentiality]].

## Tensions

- Neither flux balance analysis (FBA) class nor transposon sequencing (TnSeq) essentiality captures this condition-specific variation. [src: adp1_triple_essentiality]
- The mean inter-condition correlation is 0.38 in one report [src: adp1_triple_essentiality] and 0.44 in another. [src: acinetobacter_adp1_explorer] The reports do not reconcile the two values, so both are listed.

## Open Directions

- Test whether the genes defective only on urea form a distinct pathway set. Use gene-level enrichment on the urea-specific defects against the other 7 conditions.
- Recompute all pairwise correlations with one shared definition (defect call versus growth ratio). This would explain the gap between 0.38, 0.44 and the median of 0.25.
- Examine the 10 genes defective in all 8 conditions. Ask whether they are general growth genes and whether they overlap TnSeq essentials.
- Check whether the demanding-tier conditions (urea, acetate, butanediol) share genes beyond the acetate–butanediol–lactate group.
