---
type: "Dataset"
description: "Strain-level gene-content and strain-competition reference (LSS-PRISM) covering 59 gut commensal species, used to test IBD-biased adaptation genes."
sources: ["summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md"]
aliases: ["Kumbhari", "LSS-PRISM"]
---
# Kumbhari strain-adaptation gene inference dataset

This page covers the Kumbhari strain-adaptation gene inference dataset (Kumbhari, LSS-PRISM), a strain-level gene-content and strain-competition reference for 59 gut commensal species, used to test IBD-biased adaptation genes. The project's own analysis found a modest functional enrichment. [src: ibd_phage_targeting] The central discoveries digest instead reports zero strain-adaptation gene signal. [src: discoveries] The strain-adaptation result rests on one cohort. [src: ibd_phage_targeting]

## Key facts

- The analysis (NB10a) used the precomputed table ref_kumbhari_s7_gene_strain_inference, with 219,121 gene × species rows across 59 species. It cross-referenced this with fact_strain_competition, which has 15,520 strain × sample rows and 100 UHGG genome IDs (identifiers) in 94 LSS-PRISM participants. [src: ibd_phage_targeting]
- Only Flavonifractor plautii from the actionable Tier-A core is in the 59-species panel. [src: ibd_phage_targeting]
- The other 5 actionable Tier-A core species are absent: Hungatella hathewayi, Mediterraneibacter gnavus, Eggerthella lenta, Enterocloster bolteae and Escherichia coli. Kumbhari focused on commensal strain heterogeneity, not pathobiont mechanism. [src: ibd_phage_targeting]

## Results in ibd_phage_targeting

The analysis found 23,579 strain-adaptation genes at FDR (false discovery rate) <0.10. Of these, 12,159 were IBD-biased and 11,420 were health-biased, across 59 species. [src: ibd_phage_targeting]

Among the IBD-biased genes, adaptation genes (7 subcategories) made up 2.13 % versus 1.59 % of background. The Fisher odds ratio (OR) was 1.38 and p was 2.4e-6. [src: ibd_phage_targeting] Housekeeping genes (6 subcategories) were depleted: 2.81 % versus 4.36 % of background, with OR 0.62 and p 6.4e-20. [src: ibd_phage_targeting]

## Interpretation in the discoveries digest

The discoveries digest records zero strain-adaptation gene signal in Kumbhari. [src: discoveries] It reads this as species-abundance mediation. It predicts that phage targeting will deplete activity predictably, with no within-species strain-content escape route. [src: discoveries] This framing sits in tension with the functional enrichment above. The cited claims do not reconcile the two, so each stands as stated. See [[summaries/discoveries]] and [[summaries/ibd_phage_targeting__REPORT]].

## Caveats

- The strain-adaptation result comes from one cohort (Kumbhari/LSS-PRISM). Its cross-cohort sensitivity test was acknowledged-weak. [src: ibd_phage_targeting]
- In NB10a, 95 % of FDR-passing genes are unclassified by the gene-symbol regex. The curated 13-category classifier captures only annotated roles. The functional enrichment therefore applies to the category-classified subset, not the full gene set. [src: ibd_phage_targeting]
- Because only F. plautii overlaps the Tier-A core, the dataset says little about most targets in [[concepts/pathobiont-target-prioritization-for-ibd-phage-therapy]]. [src: ibd_phage_targeting]
