---
type: "Concept"
description: "Whether genes important under ecologically relevant (field-like) conditions are more conserved in the pangenome than genes important under laboratory conditions; stops at single-organism evidence from DvH."
sources: ["summaries/field_vs_lab_fitness__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md"]
---
# Field-relevant versus laboratory fitness as a predictor of gene conservation

In Desulfovibrio vulgaris Hildenborough (DvH), genes important under field-like conditions are more often core than baseline. [src: field_vs_lab_fitness] Lab-nutrient genes are also enriched, and the direct field-versus-lab comparison is not significant. [src: field_vs_lab_fitness] The evidence comes from one organism and small gene sets, so it is suggestive, not general. See [[summaries/field_vs_lab_fitness__REPORT]] and [[entities/desulfovibrio-vulgaris-hildenborough]].

## Literature Context

The candidate papers do not test whether field-relevant fitness predicts pangenome conservation better than laboratory fitness. They do bear on how gene importance, condition and conservation relate, and they come mostly from single organisms or small strain sets, usually under laboratory growth.

Several studies link essentiality to conservation. In Synechococcus elongatus PCC 7942, 718 of 2,723 genes were essential under laboratory conditions. That essential set overlapped tightly with well-conserved genes [PMID 26508635](https://pubmed.ncbi.nlm.nih.gov/26508635/). In six Pectobacteriaceae strains grown in rich medium, Tn-seq (transposon sequencing) found a core essentialome of 225 genes conserved across all six strains. It also found 181 strain-specific essential genes. Differences from the Escherichia coli essentialome were often attributed to growth conditions, such as temperature, and to genetic redundancy [PMID 42726091](https://pubmed.ncbi.nlm.nih.gov/42726091/). In Salmonella Typhimurium D23580, 68 genes were required for intra-macrophage replication but had no in vitro fitness effect. None of them was unique to this strain, which the authors read as high conservation of gene function between ST313 and ST19 [PMID 31560731](https://pubmed.ncbi.nlm.nih.gov/31560731/). This is a host-relevant condition, and the genes were conserved, but the paper did not compare them with laboratory-important genes.

Other papers show that importance depends on context and is graded. In Mycobacterium tuberculosis, CRISPR interference showed that vulnerability is a continuous trait. Some essential genes are invulnerable, and vulnerability is incompletely conserved between a reference strain and a hypervirulent isolate [PMID 34297925](https://pubmed.ncbi.nlm.nih.gov/34297925/). In Streptococcus sanguinis SK36, 23 of 32 deletion mutants of previously essential genes survived with extremely slow growth. These genes are widely conserved, and suppressor mutations restored fitness, so even conserved essential functions can be bypassed [PMID 41170999](https://pubmed.ncbi.nlm.nih.gov/41170999/). In Corynebacterium glutamicum, an essentiality classification used expression, phylogenetic conservation and knockout data. Deleting 26 clusters of genes judged irrelevant for growth on defined medium did not impair growth [PMID 25139579](https://pubmed.ncbi.nlm.nih.gov/25139579/). In Piscirickettsia salmonis, conserved natural-transformation genes contributed to fitness in a gene- and genogroup-specific manner, and dprA showed no detectable phenotype [PMID 41636501](https://pubmed.ncbi.nlm.nih.gov/41636501/).

The corpus's Desulfovibrio vulgaris Hildenborough result is consistent with this literature in one respect. Genes important under field-stress and field-core conditions were enriched in the core genome, as were lab-nutrient genes, and the field-specific versus lab-specific comparison was not significant (n=50-52 per group). Together with the hub's conclusion that fitness magnitude predicts conservation better than condition, this fits the general link between essentiality and conservation [PMID 26508635](https://pubmed.ncbi.nlm.nih.gov/26508635/). It also fits the observation that condition and redundancy shape which genes appear important [PMID 42726091](https://pubmed.ncbi.nlm.nih.gov/42726091/). The graded-importance papers [PMID 34297925](https://pubmed.ncbi.nlm.nih.gov/34297925/) are compatible with the magnitude interpretation. They did not test it. The corpus appears to extend this work by stratifying RB-TnSeq (random barcode transposon sequencing) effects by ecological relevance. None of the candidates does this, so that framing is novel here, and it rests on one organism. None of the candidates contradicts the DvH findings, and none supports a general field-versus-lab claim. The hub's cross-organism replication directions remain untested by this evidence.

## Condition classes and core enrichment

The report classified 757 DvH experiments into 6 condition categories. [src: field_vs_lab_fitness] The broad split is 337 field experiments (44.5%) and 420 lab experiments (55.5%). [src: field_vs_lab_fitness] Among 2,725 non-essential genes with both fitness data and pangenome links, 76.3% are core overall. [src: field_vs_lab_fitness]

Field-stress, field-core and lab-nutrient important genes are significantly enriched in the core genome after Benjamini-Hochberg false discovery rate (BH-FDR) correction. [src: field_vs_lab_fitness] Heavy-metals and lab-antibiotic genes trend below baseline but are not significant. [src: field_vs_lab_fitness]

| Class | Genes | % core | OR | FDR q |
|---|---|---|---|---|
| Field-stress | 298 | 83.6% | 1.58 | 0.026 [src: field_vs_lab_fitness] |
| Field-core | 376 | 82.4% | 1.46 | 0.026 [src: field_vs_lab_fitness] |
| Lab-other | 292 | 81.5% | 1.37 | 0.073 [src: field_vs_lab_fitness] |
| Lab-nutrient | 452 | 81.4% | 1.36 | 0.037 [src: field_vs_lab_fitness] |
| Lab-antibiotic | 109 | 73.4% | 0.86 | 0.49 [src: field_vs_lab_fitness] |
| Heavy-metals | 198 | 71.2% | 0.77 | 0.14 [src: field_vs_lab_fitness] |

OR is the odds ratio versus baseline. Condition classes differ in conservation, but they do not cleanly separate field from lab conditions. [src: field_vs_lab_fitness]

A later report, [[summaries/metal_fitness_atlas__REPORT]], attributes the low heavy-metal conservation (71.2% core) to the DvH analysis isolating genes important only for metals. Its own atlas captures all genes with any metal fitness defect. [src: metal_fitness_atlas] See also [[concepts/core-genome-enrichment-of-metal-stress-fitness-genes]]. The pathway report adopted the condition-type stratification, citing field-important genes at 83.6% core versus a 76.3% baseline. [src: pathway_capability_dependency]

## Condition-specific genes

The specificity analysis gives these core fractions: Lab-specific (sick in lab only), 50 genes, 96.0%. [src: field_vs_lab_fitness] Field-specific (sick in field only), 52 genes, 88.5%. [src: field_vs_lab_fitness] Field-biased, 89 genes, 83.1%. [src: field_vs_lab_fitness] Universal (sick in both), 352 genes, 79.8%. [src: field_vs_lab_fitness] Neutral (no strong effects), 2,083 genes, 74.5%. [src: field_vs_lab_fitness]

The field-specific versus lab-specific comparison is not significant (Fisher exact OR=0.32, p=0.27, n=50-52 per group). [src: field_vs_lab_fitness] Universal genes are significantly more core than neutral genes (OR=1.35, p=0.033). [src: field_vs_lab_fitness] The report suggests that the high core fractions of both specific sets, well above the 74.5% baseline, mean that any fitness importance predicts conservation regardless of ecological context. [src: field_vs_lab_fitness] It concludes that the magnitude of the fitness effect predicts conservation better than the condition producing it. [src: field_vs_lab_fitness] It proposes that the core genome reflects general functional importance rather than niche-specific selection. [src: field_vs_lab_fitness] This is an interpretation, not a direct test. The report calls itself the first analysis to stratify RB-TnSeq (random barcode transposon sequencing) fitness effects by ecological relevance. [src: field_vs_lab_fitness] See [[concepts/gene-fitness-importance-as-a-predictor-of-pangenome-conservation]].

A separate view from the pathway report is that lab fitness is an incomplete proxy for natural selection, because every latent pathway matters under some conditions. [src: pathway_capability_dependency]

## Caveats

- The field-specific and lab-specific sets are small (n=50-52), which limits power for the key comparison. [src: field_vs_lab_fitness]
- Field and lab fitness effects are correlated (r ~ 0.7 from the scatter plot), so most genes sick in one context are sick in the other. [src: field_vs_lab_fitness]
- Condition classification relies on manual mapping of condition_1 labels. Edge cases such as zinc sulfate as metal versus sulfate source needed subjective judgment. [src: field_vs_lab_fitness]

## Open Directions

- Repeat the stratified analysis in other organisms with field-like conditions to test whether the DvH result generalises. This closes the single-organism gap.
- Enlarge the specific gene sets, for example with a looser sickness threshold, and rerun the field-versus-lab test. This addresses the low power at n=50-52.
- Regress core status on fitness magnitude and condition class together, to separate magnitude from context given the r ~ 0.7 correlation.
- Re-run the classification with an independent second labeller to measure the effect of subjective edge-case calls.
