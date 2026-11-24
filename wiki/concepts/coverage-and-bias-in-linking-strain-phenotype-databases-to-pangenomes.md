---
type: "Concept"
description: "How incomplete name-based matching, uneven phenotype coverage and small validation sets limit phenotype–genome inference."
sources: ["summaries/bacdive_metal_validation__REPORT.md", "summaries/bacdive_phenotype_metal_tolerance__REPORT.md", "summaries/pitfalls.md"]
---
# Coverage and bias in linking strain phenotype databases to pangenomes

Linking strain phenotype databases such as [[entities/bacdive]] to pangenomes loses many strains at the name-matching step. The surviving phenotype data are uneven across traits and organisms, and the direct validation sets are small. [src: bacdive_metal_validation, bacdive_phenotype_metal_tolerance] The evidence comes from two BacDive projects and the cross-project pitfalls digest. It shows the coverage limits directly, but the validation tests are underpowered. See also [[concepts/taxonomic-synonymy-and-strain-name-collisions-in-cross-database-matching]] and [[concepts/linking-isolate-and-strain-records-to-reference-genome-databases]].

## Incomplete name-based matching

Name matching links fewer than half of BacDive strains to the pangenome. In bacdive_metal_validation, species-name matching linked 42,227 BacDive strains (43.4% of 97,334) to metal tolerance scores across 6,426 unique GTDB species. [src: bacdive_metal_validation] The pitfalls digest breaks this down: direct species-name matching captures only 34.5% of strains, and stripping GTDB suffixes adds another 8.9%, for 43.4% total. [src: pitfalls]

The bacdive_phenotype_metal_tolerance project used a different bridge, with 97,334 strains in it. [src: bacdive_phenotype_metal_tolerance] It matched 37,368 strains (38.4%) to the pangenome and a metal score [src: bacdive_phenotype_metal_tolerance], covering 5,647 unique GTDB species. [src: bacdive_phenotype_metal_tolerance] The report states this as 5,647/27,702 GTDB species. [src: bacdive_phenotype_metal_tolerance] The two projects report different match rates (43.4% and 38.4%) and different species counts (6,426 and 5,647). The quotes do not say why they differ, so I do not reconcile them. [src: bacdive_metal_validation, bacdive_phenotype_metal_tolerance]

> **Erratum.** The report gives 38.4% for two different denominators. 37,368 of 97,334 matched strains is 38.4%; 5,647 of 27,702 GTDB species, the figure this sentence uses, is about one fifth, roughly half what the percentage suggests. [src: bacdive_phenotype_metal_tolerance]

Taxonomy differences explain part of the loss. GTDB renames species with suffixes such as `_A` and `_B`, adds genus-level splits, and redraws species boundaries differently from the LPSN/DSMZ taxonomy that BacDive uses. [src: pitfalls] The pitfalls digest says the unmatched 56.6% are genuinely different species concepts or genera not yet in GTDB r214. [src: pitfalls]

The reports suggest ways to recover more links. Adding GCA accession matching could recover 10–30% more species, but it was not implemented. [src: bacdive_phenotype_metal_tolerance] The current bridge relies on species-name matching alone. [src: bacdive_phenotype_metal_tolerance]

## Uneven phenotype coverage

Coverage differs widely by phenotype, and only some matched strains carry any given trait. [src: bacdive_phenotype_metal_tolerance] The table gives BacDive strains, matched strains and species with a metal score for each feature.

| Feature | BacDive strains | Matched strains | Species with metal score | Claim |
|---|---|---|---|---|
| Isolation source | 43,378 | 22,581 | 4,531 | [src: bacdive_phenotype_metal_tolerance] |
| Metabolite breadth | 29,784 | 16,454 | 3,930 | [src: bacdive_phenotype_metal_tolerance] |
| Enzyme breadth | 28,836 | 16,005 | 3,746 | [src: bacdive_phenotype_metal_tolerance] |
| Oxygen tolerance | 23,252 | 11,708 | 3,751 | [src: bacdive_phenotype_metal_tolerance] |
| Gram stain | 15,194 | 7,411 | 3,272 | [src: bacdive_phenotype_metal_tolerance] |
| Motility | 13,759 | 6,474 | 3,138 | [src: bacdive_phenotype_metal_tolerance] |
| Nitrate reduction | 20,726 | 11,357 | 3,088 | [src: bacdive_phenotype_metal_tolerance] |
| Urease | 24,438 | 14,343 | 3,035 | [src: bacdive_phenotype_metal_tolerance] |
| Catalase | 15,295 | 7,876 | 2,930 | [src: bacdive_phenotype_metal_tolerance] |
| Oxidase | 7,813 | 5,014 | 1,799 | [src: bacdive_phenotype_metal_tolerance] |
| H₂S production | 5,254 | 2,611 | 880 | [src: bacdive_phenotype_metal_tolerance] |
| Acetate utilization | 1,980 | 475 | 422 | [src: bacdive_phenotype_metal_tolerance] |

Testing is also biased by organism. Well-studied organisms such as Pseudomonas and E. coli have many phenotype tests, and poorly studied species have sparse data. [src: bacdive_phenotype_metal_tolerance]

Only measured phenotype values were used. [src: bacdive_phenotype_metal_tolerance] The report suggests that adding BacDive's ML-predicted Gram stain, motility and oxygen tolerance could raise coverage substantially, but it would introduce model-dependent bias. [src: bacdive_phenotype_metal_tolerance] A per-metal phenotype analysis would need per-metal scores for the 27K species. [src: bacdive_phenotype_metal_tolerance]

## Small validation sets

Matching shrinks the usable validation sets sharply. BacDive has 31 strains tagged cat3=#Heavy metal contamination, but only 10 match pangenome species with metal tolerance scores. [src: pitfalls] The pitfalls digest therefore advises computing post-matching sample sizes and power before interpreting results. [src: pitfalls]

Metal-utilization validation shows the problem. Only 24 BacDive metal utilization records (iron, manganese, arsenate, chromate, cobalt, zinc) matched strains with metal tolerance scores. [src: bacdive_metal_validation] With 8 positive and 16 negative results, the comparison was underpowered (Mann-Whitney p=0.14, d=-0.57). [src: bacdive_metal_validation] Positive utilizers had lower metal scores. The report calls this surprising and nonsignificant, and says it should not be over-interpreted. [src: bacdive_metal_validation] It rates the validation inconclusive. [src: bacdive_metal_validation]

The direct validation against the [[entities/fitness-browser]] is also small. Twelve Fitness Browser organisms match BacDive by taxonomy ID, representing 6 unique species: Cupriavidus basilensis, Methanococcus maripaludis, Ralstonia solanacearum, Pseudomonas simiae, Azospirillum brasilense and Pseudomonas fluorescens. [src: bacdive_phenotype_metal_tolerance] All Gram-typed organisms among them are Gram-negative, so H1a cannot be tested within this set. [src: bacdive_phenotype_metal_tolerance] The report considers this 12-organism validation underpowered. [src: bacdive_phenotype_metal_tolerance]

## Open Directions

- Implement GCA accession matching alongside name matching. Compare the species recovered with the suggested 10–30% gain, and re-run the match-rate comparison between the two bridges.
- Reconcile the 43.4% and 38.4% match rates by running both bridges on the same BacDive snapshot and GTDB release, and tracing where strains drop out.
- Compute post-matching sample sizes and power for each BacDive category, such as heavy-metal-contamination strains, before any hypothesis test.
- Add ML-predicted Gram stain, motility and oxygen tolerance as a flagged sensitivity analysis. Measure how far coverage rises and how much model-dependent bias enters.
- Check whether phenotype coverage tracks how well-studied a genus is. This would test the testing-bias concern directly.
