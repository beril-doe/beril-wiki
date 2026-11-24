---
type: "Concept"
description: "Which genes specifically confer metal tolerance versus general stress response (including urease-associated nickel handling as a nickel-specific or general predictor), and how genome-based predictions compare with phenotype-based validation; stops at AMR in general."
sources: ["summaries/bacdive_phenotype_metal_tolerance__REPORT.md", "summaries/discoveries.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/metal_specificity__REPORT.md"]
---
# Metal tolerance determinants and shared-stress confounding

This page covers metal tolerance determinants and shared-stress confounding. Much metal fitness reflects shared stress biology: 39.8% of metal-important genes were also NaCl (sodium chloride)-important across 19 organisms and 14 metals. [src: discoveries] Phenotypes such as urease status are phylogenetically confounded, and genome-encoded resistance gene count predicts tolerance better (full model R²=0.63). [src: discoveries] Several results come from a single dataset, as noted below.

## Literature Context

The candidate papers are mostly single-organism mechanistic or transcriptomic studies. They bear on the page's central question, which is how far metal tolerance rests on general stress biology and how far on metal-specific determinants. None tests urease and nickel, and none tests genome-based versus phenotype-based prediction.

Several papers show that metal exposure triggers broad stress responses. In Xanthomonas campestris pv. campestris, RNA-seq after 15 minutes of 0.8 mM CuSO4 showed changes in general stress, oxidoreductase, chaperone, heat-shock, membrane lipid, multidrug efflux and DNA repair genes. Only cohL and a chromosomal czcCBA operon were upregulated among the metal-specific genes at that time point [PMID 38461228](https://pubmed.ncbi.nlm.nih.gov/38461228/). Several efflux pumps responded to other toxic metals as well as copper, so they were not copper-specific [PMID 38461228](https://pubmed.ncbi.nlm.nih.gov/38461228/). In Escherichia coli, anaerobic copper treatment caused protein aggregation, and strains lacking the chaperone DnaK or trigger factor were highly sensitive to copper [PMID 35289645](https://pubmed.ncbi.nlm.nih.gov/35289645/). In Klebsiella pneumoniae, CusR links copper efflux to oxidative stress resistance, and cusR loss caused hypersensitivity to hydrogen peroxide [PMID 43006896](https://pubmed.ncbi.nlm.nih.gov/43006896/). In Aromatoleum sp. CIB, arsenite induced the canonical ars genes, and oxygen availability intensified the global oxidative-stress response [PMID 41936227](https://pubmed.ncbi.nlm.nih.gov/41936227/). Genome annotation of Rhizobium sp. LBMP-C04 likewise linked metal resistance genes mainly to DNA repair and metal import and export [PMID 39690265](https://pubmed.ncbi.nlm.nih.gov/39690265/). That study is a single-strain annotation with in vitro assays.

These findings are consistent with the corpus's main claim. The Metal Fitness Atlas found that survival under metal stress depends mainly on cell envelope integrity, DNA repair, protein quality control and central metabolism, and the page reports 39.8% NaCl overlap among metal-important genes. The chaperone, DNA repair and oxidative-stress responses above fit that picture. They are single-organism results, so they support the shared-stress interpretation but do not quantify it.

The literature also supports the corpus's view that specific determinants exist alongside the general response. CusR directly activates the cusCFBA efflux operon [PMID 43006896](https://pubmed.ncbi.nlm.nih.gov/43006896/). In Pseudomonas aeruginosa, CzcS/CzcR activated by zinc excess regulates the copper tolerance gene ptrA [PMID 38376236](https://pubmed.ncbi.nlm.nih.gov/38376236/). That is cross-metal coupling, which matches the page's caution that spanning many metals does not make a gene metal-specific. This is consistent with the two-tier model, where a small accessory tier gives targeted tolerance through efflux. It is also in mild tension with the specificity report's framing, because efflux systems here are partly cross-responsive. The Atlas claim that efflux pumps are not the main survival factor is a statement about fitness effects, so it is not directly contradicted.

The corpus's urease and nickel findings, the lineage confounding, the R²=0.63 genome-based model, and the YebC and keyword-enrichment results have no counterpart in these candidates. They remain novel relative to this evidence. The remaining candidates, on extracellular vesicles, Cr(VI) reduction, kiwifruit metallothioneins and Arthrobacter drought, are not relevant to these claims.

## Urease and nickel: specific or general predictor?

Urease-positive bacteria need nickel import and handling machinery, so the nickel-import hypothesis predicted better nickel tolerance. [src: bacdive_phenotype_metal_tolerance] The data went the other way: BacDive urease-positive species had lower metal tolerance (d = -0.18, p < 1e-5). [src: bacdive_phenotype_metal_tolerance] The univariate result was d = -0.175, n = 3,035, p = 3.7e-06, FDR (false discovery rate) q = 9.1e-06. [src: bacdive_phenotype_metal_tolerance] The report labels hypothesis H1e (urease → nickel tolerance) reversed and driven by Actinomycetes. [src: bacdive_phenotype_metal_tolerance] See [[entities/urease]] and [[entities/bacdive]].

The effect comes from lineage composition. In Actinomycetes the effect was d = -0.59, p < 1e-16, and urease-positive species form a distinct low-metal-score subgroup. [src: bacdive_phenotype_metal_tolerance] Within Gammaproteobacteria (d = +0.08, ns) the effect disappears. [src: bacdive_phenotype_metal_tolerance] It also disappears within Bacilli (d = +0.06, ns). [src: bacdive_phenotype_metal_tolerance] Within other classes the report finds zero urease effect. [src: bacdive_phenotype_metal_tolerance] The report concludes that urease positivity correlates with Actinomycetes and other lineages that have fewer metal resistance genes, so this is not a true paradox. [src: bacdive_phenotype_metal_tolerance] The same point appears in the cross-project digest. [src: discoveries] See [[concepts/phylogenetic-confounding-of-phenotype-metal-tolerance-associations]].

The report argues that urease-associated nickel handling is narrowly nickel-specific and does not confer general metal tolerance. [src: bacdive_phenotype_metal_tolerance] It reasons that urease activity is tightly coupled to nickel efflux, so nickel homeostasis in urease producers is a balancing act rather than a broad tolerance mechanism. [src: bacdive_phenotype_metal_tolerance] These are interpretations. The report therefore proposes per-metal phenotype analysis (catalase for copper, urease for nickel) rather than composite metal scores. [src: bacdive_phenotype_metal_tolerance] It also proposes per-metal fitness profiling of urease+ versus urease- bacteria from one class, ideally Gammaproteobacteria, where the pangenome-scale urease effect is near zero. [src: bacdive_phenotype_metal_tolerance] A direct test would be RB-TnSeq (random barcode transposon sequencing) of matched urease+/- strains under nickel versus other metals. [src: bacdive_phenotype_metal_tolerance]

In the direct Fitness Browser–BacDive validation, all urease-typed organisms were urease-negative yet routinely tested against nickel. The report calls this consistent with urease status not predicting metal tolerance at pangenome scale. [src: bacdive_phenotype_metal_tolerance]

## Shared stress confounds metal fitness

Many metal-important genes are general stress genes. The 39.8% NaCl overlap is attributed to shared cell-envelope, ion-homeostasis and DNA-repair biology rather than chloride contamination. [src: discoveries] Zinc sulfate, with 0 mM Cl⁻, showed 44.6% NaCl overlap and the highest DvH profile correlation (r=0.715), exceeding most chloride-delivered metals. [src: discoveries] See [[concepts/counter-ion-confounding-in-metal-fitness-assays]] and [[concepts/shared-metal-and-osmotic-stress-fitness-determinants]].

In DvH, whole-genome correlation with NaCl ran Zn (r=0.72) > Mn (0.55) > Cu (0.53) > Co (0.50) > Hg (0.48) > Ni (0.45) > Al (0.42) > Mo (0.40) > U (0.35) > Se (0.34) > Cr (0.32) > W (0.30) > Fe (0.09). [src: discoveries] The report interprets this as follows. Metals that broadly displace cofactors share more genes with ionic stress. Mo/W (molybdopterin) and Fe (iron-sulfur clusters) target specific pathways and are distinct from general stress. [src: discoveries]

The Metal Fitness Atlas defines metal-important genes broadly (fit < -1 OR n_sick ≥ 1). That captures ~3.3% of genes, most of them general stress genes rather than metal-specific ones. [src: metal_fitness_atlas] The report attributes metal-fitness core enrichment to core processes vulnerable to metal disruption (cell envelope, DNA repair, central metabolism), not specialized resistance mechanisms. [src: metal_fitness_atlas] It also says survival under metal stress depends mainly on cell envelope integrity, DNA repair, protein quality control and central metabolism, not on efflux pumps or metal-binding proteins. [src: metal_fitness_atlas] To separate the core stress response from genuine metal-resistance evolution, it proposes repeating the conservation analysis with genes important for metals but not other stresses. [src: metal_fitness_atlas]

After removing the ~40% of metal-important genes that overlap NaCl stress, core-genome enrichment persisted for 12 of 14 metals. [src: discoveries] The metals the report calls essential (Mo, W, Se, Hg) showed stronger enrichment after correction, for example Mo delta +0.132 → +0.145. [src: discoveries] The report concludes the original atlas result (OR = 2.08, odds ratio) is not an artifact of shared NaCl stress. [src: discoveries] See [[concepts/core-genome-enrichment-of-metal-stress-fitness-genes]].

### Two-tier model

The Atlas report frames this as two tiers. Tier 1 (core) is general stress response, the majority of metal fitness genes, conserved because they serve essential functions beyond metal tolerance. [src: metal_fitness_atlas] Tier 2 (accessory) is a smaller fraction giving targeted tolerance through efflux, sequestration or enzymatic detoxification. These genes are enriched in the accessory genome, visible only when controlling for general stress response. [src: metal_fitness_atlas] See [[entities/metal-fitness-atlas]].

### Keyword evidence for metal-specific genes

Metal-specific genes carry metal-resistance annotations more often than general sick genes do: 12.2% vs 7.8%, Fisher exact OR=1.64, p=2.4e-8. [src: metal_specificity]

The report's text says general sick genes show slightly higher general-stress keyword enrichment, giving the values as 11.5% vs 13.7%. [src: metal_specificity] The report's own table gives the opposite direction. Among 3,344 annotated metal-specific genes, 12.2% have metal-resistance keywords and 13.7% have general-stress keywords. [src: metal_specificity] Among 2,573 annotated general sick genes, 7.8% have metal-resistance keywords and 11.5% have general-stress keywords. [src: metal_specificity] By the table, metal-specific genes have the higher general-stress rate, which conflicts with the text's wording. This page does not resolve the conflict. Among 495 annotated metal+stress genes, 8.9% have metal-resistance keywords and 6.5% have general-stress keywords. [src: metal_specificity]

The report interprets the 1.64x enrichment as confirming genuine metal tolerance determinants rather than general stress genes that also affect metal survival. [src: metal_specificity] The absolute rates are low, so most metal-specific genes lack such keywords. [src: metal_specificity]

### Experiment-count caveat

*Synechococcus elongatus* had 12 NaCl dose-response experiments (0.5–250 mM), against 1–6 in other organisms. [src: discoveries] That made the n_sick >= 1 threshold much easier to satisfy and gave an 88.6% shared-stress rate. [src: discoveries] Excluding it lowered overall overlap from 39.8% to 36.7%. [src: discoveries] The report recommends that NaCl analyses account for experiment count when setting importance thresholds. [src: discoveries] See [[entities/synechococcus-elongatus]].

## Genes that look metal-specific

Among the top novel Atlas candidates, three stand out as metal-specific rather than pleiotropic.
- UCP030820/OG01015: 67% metal-specific, oxidoreductase, 7 metals. [src: discoveries]
- YebC/OG01383: 58%, transcriptional regulator/translation factor, 6 metals, 11 organisms. [src: discoveries]
- DUF1043-YhcB/OG03264: 50%, cell division protein, 5 metals. [src: discoveries]

YfdZ (15%) and the Mla/Yrb system (0-25%) are pleiotropic. [src: discoveries] DUF39 is a general fitness factor (0% metal-specific, sick rate 0.64) despite spanning 8 metals. [src: discoveries] Spanning many metals therefore does not mean metal-specific. See [[concepts/metal-specific-versus-pleiotropic-stress-gene-classification]] and [[concepts/conserved-metal-phenotype-gene-families-and-novel-metal-tolerance-candidates]].

For YebC, the report cites Ignatov et al. 2025 as showing it is a translation factor for proline-rich proteins. [src: discoveries] Many metal homeostasis proteins, including P-type ATPases CopA/ZntA and CDF transporters, have proline-rich cytoplasmic loops. [src: discoveries] The report hypothesizes that YebC resolves a translation bottleneck from upregulated proline-rich metal transporters under metal stress, and is dispensable otherwise. [src: discoveries] See [[entities/yebc]].

The specificity analysis had a bug. A locusId type mismatch silently excluded DvH, so the initial analysis showed 0% specificity for Mo, W, Se and Mn, which seemed due to DvH's 608 non-metal experiments. [src: discoveries] After the fix, specificity was Manganese 61%, [src: discoveries] Molybdenum 61%, [src: discoveries] Tungsten 57% [src: discoveries] and Selenium 46%. [src: discoveries] The report says the experiment-count bias is real but less severe than first thought. [src: discoveries]

## Genome-based prediction versus phenotype-based validation

Genome-encoded resistance predicts tolerance better than classical phenotypes. BacDive phenotypes (Gram stain, oxygen tolerance, enzyme activities) capture a real signal (R²=0.16 alone, 7/10 significant after FDR). [src: discoveries] The signal is entirely phylogenetically confounded: adding phenotype features to a taxonomy-based model gave zero improvement (delta R²=-0.009). [src: discoveries] The report identifies genome metal-resistance gene count as the true predictor (full model R²=0.63). [src: discoveries] It concludes this validates genome-based prediction over phenotype-based screening. [src: discoveries] See [[concepts/genome-encoded-metal-resistance-repertoire-versus-phenotype-as-predictor-of-metal-tolerance]].

The effect is dose-dependent: heavy metal (+1.00) > waste/sludge (+0.57) > all contamination (+0.43) > industrial (+0.20). [src: discoveries] It holds within Pseudomonadota and Actinomycetota after phylogenetic stratification. [src: discoveries] The report reads this as validating the Atlas's genome-based method. [src: discoveries]

One result runs against expectation. Host-associated bacteria (n=12,086) scored slightly higher than environmental bacteria (d=+0.14, p<0.0001), although host niches should have lower metal exposure. [src: discoveries] The report proposes genome size confounding: large-genome Pseudomonadota pathogens with more KEGG-annotated gene clusters inflate the normalized score. [src: discoveries]

The linkage behind these comparisons is partial. Species-name matching (exact plus GTDB suffix removal) links 42,227 BacDive strains (43.4% of 97K) to 6,426 GTDB pangenome species. [src: discoveries] This allows cross-referencing without Spark queries. [src: discoveries] The report attributes the 56.6% unmatched strains to GTDB's different species boundaries from LPSN/DSMZ taxonomy. [src: discoveries] See [[concepts/linking-isolate-and-strain-records-to-reference-genome-databases]].

## Tensions

- Urease should confer nickel tolerance because it needs nickel import machinery. [src: bacdive_phenotype_metal_tolerance] The pooled data show lower tolerance in urease-positive species. [src: bacdive_phenotype_metal_tolerance] The report resolves this as lineage confounding, with the effect absent within Gammaproteobacteria, Bacilli and other classes. [src: bacdive_phenotype_metal_tolerance]
- Metal-important genes are mostly general stress genes. [src: metal_fitness_atlas] Yet core enrichment survives NaCl correction for 12 of 14 metals. [src: discoveries]
- The Atlas report says most metal fitness genes are general stress genes. [src: metal_fitness_atlas] The specificity report says metal-specific genes are genuine metal tolerance determinants, enriched for resistance keywords. [src: metal_specificity]
- The specificity report's text says general sick genes have higher general-stress keyword enrichment (11.5% vs 13.7%). [src: metal_specificity] Its table gives 13.7% for metal-specific genes and 11.5% for general sick genes, the opposite direction. [src: metal_specificity]

## Open Directions

- Run per-metal phenotype analysis, such as catalase against copper and urease against nickel, instead of composite scores. This tests whether any phenotype predicts a specific metal. [src: bacdive_phenotype_metal_tolerance]
- Run per-metal fitness profiling of urease+ and urease- bacteria from the same class, ideally Gammaproteobacteria. This tests whether urease+ organisms are nickel-specific rather than generally metal-tolerant. [src: bacdive_phenotype_metal_tolerance]
- Use RB-TnSeq on matched urease+/- strains under nickel versus other metals. This would directly test nickel-specific tolerance. [src: bacdive_phenotype_metal_tolerance]
- Repeat the conservation analysis using only genes important for metals but not for other stresses. This separates the core stress response from metal-resistance gene evolution. [src: metal_fitness_atlas]
- Test the YebC translation-bottleneck hypothesis, for example by measuring expression of proline-rich metal transporters under metal stress in yebC mutants. [src: discoveries]
- Recompute the general-stress keyword rates for metal-specific and general sick genes from the underlying gene lists. This would settle the text-versus-table conflict. [src: metal_specificity]
- Check whether keyword-free metal-specific genes (most of the 3,344) fall into the accessory tier, by testing their accessory-genome enrichment. [src: metal_fitness_atlas, metal_specificity]
