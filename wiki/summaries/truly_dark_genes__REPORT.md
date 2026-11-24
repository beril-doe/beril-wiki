---
type: "Summary"
description: "Summary of the project Truly Dark Genes — What Remains Unknown After Modern Annotation?."
doc_type: "short"
full_text: "sources/truly_dark_genes__REPORT.md"
---
# Truly Dark Genes — What Remains Unknown After Modern Annotation?

Summary of the project Truly Dark Genes — What Remains Unknown After Modern Annotation?. The report splits 57,011 dark genes into annotation lag and a hard core of 6,427 truly dark genes. [src: truly_dark_genes] It argues that this core is genuinely novel biology, not annotation lag. [src: truly_dark_genes] Its coverage is incomplete, because 17,479 unlinked dark genes could not be assessed with bakta. [src: truly_dark_genes]

## Key Findings

### Decomposition of dark genes

The 57,011 Fitness Browser (FB) dark genes fall into three categories. [src: truly_dark_genes] Annotation-lag genes number 33,105. Bakta v1.12.0 annotates them, which the report reads as a database vintage problem. [src: truly_dark_genes] Truly dark genes number 6,427. Both FB and bakta call them hypothetical. [src: truly_dark_genes] Unlinked genes number 17,479. They have no pangenome link and an unknown bakta status. [src: truly_dark_genes]

Of the 39,532 dark genes with pangenome links, bakta reclassifies 33,105 (83.7%). That leaves 6,427 truly dark genes. [src: truly_dark_genes] The 17,479 unlinked genes could not be assessed. [src: truly_dark_genes] The report says the 57,011 → 6,427 reduction separates annotation lag from genuine novelty and gives a tractable target set for experiments. [src: truly_dark_genes] It states that the 16.3% truly-dark rate (6,427/39,532) aligns with bacterial ORFan prevalence estimates (10-30%; Siew & Fischer 2003). It concludes that a hard core of genuinely novel proteins persists. [src: truly_dark_genes] See [[concepts/reannotation-lag-versus-genuinely-unannotatable-dark-genes]].

Truly dark genes are concentrated in a few organisms. Methanococcus strains S2 and JJ account for 55% of them. The report attributes this to archaea being underrepresented in annotation databases. [src: truly_dark_genes] It attributes the dominance of Methanococcus strains to a well-known bias: archaeal proteins are systematically underrepresented in reference databases compared to bacteria. [src: truly_dark_genes] It adds that even the annotation-lag category underestimates true novelty in archaea, citing Makarova et al. (2019). [src: truly_dark_genes] Across organisms, 4–96% of dark genes resist bakta annotation, with archaea at the high end. [src: truly_dark_genes]

### Structural differences from annotation-lag genes

Truly dark genes differ from annotation-lag genes on length, core genome fraction, essential fraction, GC content, ortholog presence and ortholog breadth. [src: truly_dark_genes] The report states that all effects exceed its pre-registered thresholds (Cohen's d ≥ 0.2 or OR ≥ 1.5). [src: truly_dark_genes] That blanket statement does not match the listed values. The odds ratios of 0.284, 0.236 and 1.420 do not meet OR ≥ 1.5 as written, so the statement should be read with caution. [src: truly_dark_genes] The values below are truly dark versus annotation-lag.

| Measure | Truly dark | Annotation-lag | Effect |
|---|---|---|---|
| Median length (aa) | 121 | 194 | d = −0.432 [src: truly_dark_genes] |
| Core genome fraction | 43.1% | 72.7% | OR = 0.284 [src: truly_dark_genes] |
| Essential fraction | 18.0% | 13.4% | OR = 1.420 [src: truly_dark_genes] |
| Mean GC content | 0.542 | 0.584 | d = −0.395 [src: truly_dark_genes] |
| Has orthologs | 29.3% | 63.7% | OR = 0.236 [src: truly_dark_genes] |
| Ortholog breadth (median organisms) | 1 | 4 | d = −1.072 [src: truly_dark_genes] |

The report considers this pattern consistent with biological novelty rather than database lag. [src: truly_dark_genes] It reads shorter sequences, accessory genome enrichment, higher GC deviation, mobile-element proximity and narrow taxonomic breadth together as convergent evidence of recently acquired, rapidly evolving genes. [src: truly_dark_genes] Truly dark genes are 4.2× less likely to have cross-organism orthologs. [src: truly_dark_genes] Only 3 of 65 dark-gene ortholog groups with cross-organism concordance data contain truly dark genes, so these genes are nearly invisible to cross-organism analysis. [src: truly_dark_genes] See [[concepts/sequence-composition-and-conservation-of-unannotatable-genes]] and [[concepts/cross-organism-fitness-concordance-of-dark-gene-orthologs]].

### Annotation landscape

The landscape covers 5,870 unique truly dark gene clusters. [src: truly_dark_genes] Many have identifiers but few functional hits.

- Despite the "hypothetical" label, 79.4% of truly dark genes have UniRef50 links. 84.7% have database cross-references such as RefSeq and UniParc. [src: truly_dark_genes]
- Cross-references total 26,917 entries for 4,971 clusters. They are dominated by SO, UniRef and UniParc identifiers, with only 6 KEGG and 1 EC (Enzyme Commission) number. [src: truly_dark_genes]
- Only 4.0% have Pfam domain hits and only 4.6% have KEGG KOs (KEGG orthologs). The report reads this as resistance to standard functional annotation. [src: truly_dark_genes]
- Pfam gives 362 hits for 235 clusters. TPR repeats dominate the non-DUF hits. [src: truly_dark_genes] 56 clusters have DUF-only domains. [src: truly_dark_genes]
- eggNOG gives 2,551 annotations for 2,551 clusters (43.5%). [src: truly_dark_genes] Only 17.0% have COG (clusters of orthologous groups) categories. [src: truly_dark_genes]
- Of the COG assignments, 55.4% are category S, function unknown. [src: truly_dark_genes] The rest span L, M, K, T, C and J with no dominant functional theme. [src: truly_dark_genes]
- Ortholog data cover 3,449 pairs for 1,885 truly dark genes (29.3%) across 48 FB organisms. [src: truly_dark_genes]

See [[entities/pfam-domain-annotations]] and [[entities/eggnog-orthologous-groups]].

### Clue tiers

A 12-dimensional clue matrix finds only 246 truly dark genes (3.8%) with zero annotation clues. [src: truly_dark_genes] The other 96.2% have combinations of sequence identifiers, eggNOG hits, orthologs, module membership or fitness phenotypes. [src: truly_dark_genes] The report provides a 41-column clue profile for each truly dark gene, which supports hypothesis generation even without a product annotation. [src: truly_dark_genes]

- Tier 1, no clues: 246 genes (3.8%), with no sequence IDs, hits or phenotype. [src: truly_dark_genes]
- Tier 2, minimal: 3,867 genes (60.2%), with sequence identifiers only (UniRef50 or RefSeq). [src: truly_dark_genes]
- Tier 3, partial function: 711 genes (11.1%), with Pfam, COG or eggNOG functional descriptions. [src: truly_dark_genes]
- Tier 4, phenotype only: 1,603 genes (24.9%), with fitness, essentiality or module signals but no functional annotation. [src: truly_dark_genes]

The report prioritizes Tiers 3 and 4, 2,314 genes in total. Their partial clues can narrow experimental hypotheses. [src: truly_dark_genes]

### Horizontal gene transfer and genomic context

GC deviation from the host genome mean is higher for truly dark genes (mean |ΔGC| = 0.047 vs 0.038, d = 0.247, p = 1.3e-43). [src: truly_dark_genes] Strong deviation (|z| > 2) affects 9.2% of truly dark genes versus 4.0% of annotation-lag genes. The report calls this consistent with recent horizontal gene transfer (HGT) outpacing annotation databases. [src: truly_dark_genes] Also, 12.0% of truly dark genes lie within 2 genes of a mobile genetic element. The report says this further supports HGT as a source of annotation resistance. [src: truly_dark_genes] The report says these signatures agree with Daubin et al. (2003) and others, who showed that horizontally transferred genes are enriched among hypothetical proteins. [src: truly_dark_genes] See [[concepts/horizontal-gene-transfer-and-mobile-elements-as-a-source-of-novel-and-dark-genes]].

The report also looks at 4,394 truly dark genes in independent component analysis (ICA) organisms. [src: truly_dark_genes]

- 41% of neighboring genes are also hypothetical, forming "dark islands". [src: truly_dark_genes]
- 12.0% are within 2 genes of a mobile element. [src: truly_dark_genes]
- 25.9% show operon-like cofitness (|r| ≥ 0.3) with adjacent genes. [src: truly_dark_genes]
- 594 belong to ICA fitness modules. Guilt-by-association there suggests functions including phage integrases, metal transporters, chemotaxis systems and iron regulation. [src: truly_dark_genes]

The ICA module guilt-by-association approach extends Oliver's (2000) principle from expression to fitness data. [src: truly_dark_genes] The report calls its fitness-based prioritization complementary to the global metagenomic approach of Pavlopoulos et al. (2023). [src: truly_dark_genes] See [[concepts/guilt-by-association-inference-of-dark-gene-function-from-modules-operons-synteny-and-co-fitness]].

### Condition profiles

The report's stress-enrichment hypothesis (H2) was not supported. Truly dark genes with strong fitness phenotypes (|f| ≥ 2) are depleted in stress conditions relative to annotation-lag genes (28.7% vs 43.2%, OR = 0.53, p < 0.001). [src: truly_dark_genes] They are instead enriched in nutrient, mixed community and iron conditions. The report suggests novel metabolic or community-interaction functions rather than stress responses. [src: truly_dark_genes] The report calls the rejection of H2 informative. [src: truly_dark_genes] It suggests that enrichment in community/nutrient conditions may indicate inter-species interaction functions, novel metabolic capabilities or community-specific behaviors poorly represented in single-organism annotation databases. [src: truly_dark_genes] It links this to mobile-element proximity, since horizontally transferred genes often encode community-relevant functions such as antibiotic resistance, bacteriocins and specialized metabolites. [src: truly_dark_genes]

A separate breakdown gives these condition profiles for strong-fitness truly dark genes versus annotation-lag genes:

- Mixed community is enriched (7.5% vs 0%). [src: truly_dark_genes]
- Iron is enriched (0.7% vs 0%). [src: truly_dark_genes]
- Nutrient time-series and rich media are enriched. [src: truly_dark_genes]
- Stress is depleted (43.3% vs 54.7%). [src: truly_dark_genes]
- Carbon source is depleted (13.7% vs 21.7%). [src: truly_dark_genes]
- Motility is depleted (1.2% vs 3.2%). [src: truly_dark_genes]

The two stress figures differ (28.7% vs 43.2% in one, 43.3% vs 54.7% in the other). The claims do not say why. [src: truly_dark_genes] See [[concepts/condition-specific-fitness-of-dark-genes]].

### Candidate prioritization

A multi-criteria score ranks all 6,427 truly dark genes. It uses fitness importance, annotation clues, ortholog breadth, genomic context and tractability, with a maximum score of 12. [src: truly_dark_genes] It identifies 100 top candidates (scores 8–10) across 19 organisms. [src: truly_dark_genes] The report says this list enables resource-efficient experimental campaigns. [src: truly_dark_genes] Methanococcus_S2 contributes 29, DvH 13, Methanococcus_JJ 13 and MR-1 8. [src: truly_dark_genes] Of the top candidates, 34 are essential, 53 are in operons and 30 are in ICA fitness modules. [src: truly_dark_genes]

Example candidates:

- PV4/5210953 (score 10) has a motility phenotype (|f| = 5.5), an operon with TatC (Sec-independent translocase), and ICA module M016 membership. [src: truly_dark_genes]
- ANA3/7026383 (score 9) has a nitrogen source phenotype (|f| = 8.6), an operon with an ABC (ATP-binding cassette) transporter, and ICA module M018 membership. [src: truly_dark_genes]
- DvH/206658 (score 9) has a stress phenotype (|f| = 5.4). eggNOG suggests trehalose synthase despite the hypothetical annotation, which could indicate a mis-annotation or novel variant. [src: truly_dark_genes]
- Methanococcus_S2/MMP_RS06570 (score 9) has 8 annotation clues, including DUF190, COG-T signal transduction and an operon with fluoride efflux transporter CrcB. [src: truly_dark_genes]

## Caveats and Open Work

- The 17,479 unlinked dark genes could not be assessed. [src: truly_dark_genes] At the 16.3% truly-dark rate, the report estimates ~2,841 additional truly dark genes among them, including 2,208 with strong fitness phenotypes. [src: truly_dark_genes] The ranked list covers ~69% of the estimated total truly dark gene population. [src: truly_dark_genes] The report calls this a 31% coverage gap. [src: truly_dark_genes] This is an extrapolation, not a measurement. [src: truly_dark_genes] The report proposes extending pangenome linkage to these genes, then running bakta to find more candidates. [src: truly_dark_genes]
- Some bakta "hypothetical protein" calls may be false negatives, meaning genes with known functions that did not match the PSC database version tested (v6.0). [src: truly_dark_genes]
- BBH (bidirectional best hit) orthologs cover only 32 of 48 FB organisms. Truly dark genes from the other 16 lack concordance and ortholog-breadth data. [src: truly_dark_genes]
- Methanococcus strains S2 and JJ hold 55% of truly dark genes, a concentration the report attributes to archaeal underrepresentation in annotation databases. [src: truly_dark_genes]
- The HGT interpretation rests on GC deviation and proximity to mobile elements. The report describes the GC result as consistent with HGT and the mobile-element result as supporting it. [src: truly_dark_genes] GC deviation is an imperfect HGT proxy. It can also reflect gene-specific composition biases, such as membrane proteins, or amelioration over time. [src: truly_dark_genes]
- Short genes are harder to annotate and harder to measure fitness for. The length difference (d = −0.432) may therefore partly explain other differences. [src: truly_dark_genes]
- Some strong fitness phenotypes may reflect polar effects on downstream genes rather than the truly dark gene's own function. [src: truly_dark_genes]

### Dark island hypotheses

The report defines dark islands as contiguous hypothetical regions. [src: truly_dark_genes] It hypothesizes that they likely represent recently acquired genomic islands consistent with HGT signatures. [src: truly_dark_genes] It also hypothesizes phage-derived regions, supported by integrase/phage protein proximity. [src: truly_dark_genes] A third hypothesis is species-specific gene neighborhoods that arose after the last common ancestor shared with well-studied organisms. [src: truly_dark_genes] It suggests some islands may be prophage remnants. [src: truly_dark_genes] It suggests others may be recently acquired metabolic cassettes. [src: truly_dark_genes]

### Proposed next steps

The report proposes AlphaFold2/ESMFold structure prediction with Foldseek as the next frontier for these candidates. [src: truly_dark_genes] It would run these on the top-100 candidates and search for remote structural homologs. [src: truly_dark_genes] The report calls this the most promising path to annotating sequences with no detectable sequence homology. [src: truly_dark_genes] It proposes growth assays in predicted conditions, such as motility assays for PV4/5210953 [src: truly_dark_genes] and nitrogen limitation for ANA3/7026383. [src: truly_dark_genes] It suggests Mobile-CRISPRi could enable rapid functional testing across organisms. [src: truly_dark_genes] It also proposes a focused Methanococcus analysis using high cofitness signals (r > 0.97) to map operonic structure and predict functions for archaeal-specific hypothetical proteins. [src: truly_dark_genes] The report states that archaea contribute 55% of truly dark genes. [src: truly_dark_genes]

## Slots Into

- [[concepts/reannotation-lag-versus-genuinely-unannotatable-dark-genes]]: bakta reclassifies 83.7% of linked dark genes and leaves 6,427 truly dark. [src: truly_dark_genes]
- [[concepts/sequence-composition-and-conservation-of-unannotatable-genes]]: truly dark genes are shorter, lower in GC and less conserved. [src: truly_dark_genes]
- [[concepts/horizontal-gene-transfer-and-mobile-elements-as-a-source-of-novel-and-dark-genes]]: 9.2% show strong GC deviation, and 12.0% lie near mobile elements. [src: truly_dark_genes]
- [[concepts/condition-specific-fitness-of-dark-genes]]: truly dark genes are depleted in stress conditions, contrary to H2. [src: truly_dark_genes]
- [[concepts/guilt-by-association-inference-of-dark-gene-function-from-modules-operons-synteny-and-co-fitness]]: 594 truly dark genes are in ICA modules, and 25.9% show operon-like cofitness. [src: truly_dark_genes]
- [[concepts/cross-organism-fitness-concordance-of-dark-gene-orthologs]]: only 3 of 65 ortholog groups with concordance data contain truly dark genes. [src: truly_dark_genes]
