---
type: "Concept"
description: "Covers whether genomes carrying one catabolic capacity tend to carry others, whether capacities form portable modules, and the effect-size methods used to test this; it stops at genome-level presence data."
sources: ["summaries/enigma_carbon_census_1__REPORT.md"]
---
# Co-occurrence and modularity of catabolic capacities across genomes

In the ENIGMA Carbon Census, most genomes with a catabolic capacity carry only one of the 8 aromatic/alkaloid capacities, and the report finds no broad cross-module modularity. [src: enigma_carbon_census_1] Co-occurrence does appear within the aromatic block and for a few enriched pairs, but the report reads these as aromatic-derived. [src: enigma_carbon_census_1] Versatility is described as a clade trait, not a portable module set. [src: enigma_carbon_census_1] All of this rests on one project, so it is a single-dataset result. See also [[summaries/enigma_carbon_census_1__REPORT]].

## Literature Context

The candidate papers are mostly genome-level descriptions of aromatic catabolism in single taxa. They say little about whether capacities co-occur across many genomes. Several show that aromatic degradation is concentrated in particular lineages and is often carried on mobile or clustered genetic elements. In the genus Rhodococcus, a pan-genome of 109 high-quality genomes found that every member had at least one gene in the benzoate degradation pathway, while biphenyl degradation was mainly restricted to strains closely related to the authors' isolates [PMID 38376357](https://pubmed.ncbi.nlm.nih.gov/38376357/). In 164 Pseudomonas putida strains, protocatechuate and phenylacetate degradation were widely conserved. Capacities for ferulate, phenol and cresols varied markedly between strains [PMID 41919942](https://pubmed.ncbi.nlm.nih.gov/41919942/). Comparative work on marine Roseobacters likewise lists aromatic compound degradation among genes shared across the clade [PMID 17526795](https://pubmed.ncbi.nlm.nih.gov/17526795/).

Some papers describe several catabolic modules in one genome. Pseudomonas putida CSV86 carries genes for naphthalene, salicylate, benzoate, benzylalcohol, p-hydroxybenzoate, phenylacetate and p-hydroxyphenylacetate degradation on its chromosome. The naphthalene genes sit in a proposed genomic island, which is consistent with transferability [PMID 24475028](https://pubmed.ncbi.nlm.nih.gov/24475028/). That is a single draft genome. In Mycobacterium vanbaalenii PYR-1, high-molecular-weight PAH degradation is proposed to feed the beta-ketoadipate pathway through protocatechuate [PMID 18421421](https://pubmed.ncbi.nlm.nih.gov/18421421/). In the 31 reconstructed subseafloor Chloroflexi genomes, most genomes simultaneously contained degradation pathways for complex carbohydrates, detrital protein, aromatic compounds and hydrogen. The authors link this to acetogenesis [PMID 32372496](https://pubmed.ncbi.nlm.nih.gov/32372496/). These are uncultured, reconstructed genomes, and the paper does not test pairwise co-occurrence statistically. Horizontal transfer is also suggested for the anaerobic hydroxyhydroquinone pathway. Mobile elements flank some of its clusters, and the pathway was detected in only a few Proteobacteria genomes [PMID 30884168](https://pubmed.ncbi.nlm.nih.gov/30884168/).

The corpus result fits the clade-structure picture. In the ENIGMA Carbon Census, among genomes carrying at least one of the 8 aromatic/alkaloid capacities, 675 carry exactly one and only 18 carry three or more. Only 25/3109 genomes carry both an aromatic and a non-aromatic capacity. The report reads versatility as a clade trait, concentrated in Burkholderiales. This agrees with the taxon-restricted distributions seen in Rhodococcus and P. putida, where capacities vary with phylogeny and strain [PMID 38376357](https://pubmed.ncbi.nlm.nih.gov/38376357/), [PMID 41919942](https://pubmed.ncbi.nlm.nih.gov/41919942/). The report's within-aromatic co-occurrence, explained by a shared lower pathway, matches the funnel into protocatechuate and the beta-ketoadipate route described for PYR-1 [PMID 18421421](https://pubmed.ncbi.nlm.nih.gov/18421421/).

The corpus is in partial tension with the multi-pathway genomes. Chloroflexi genomes combining aromatic, carbohydrate and protein degradation [PMID 32372496](https://pubmed.ncbi.nlm.nih.gov/32372496/) and the mobile-element evidence [PMID 24475028](https://pubmed.ncbi.nlm.nih.gov/24475028/) suggest portable modules. The corpus finds no broad cross-module modularity, but its test is limited to 15 cross-block pairs. It extends the literature by supplying effect sizes (Haldane odds ratio and Jaccard index) across thousands of genomes. None of the candidates reports such measures. The phenylethylamine×aromatic enrichment (OR 2.84 and 3.37) has no direct counterpart in these papers. It is a single-dataset result, and gene proximity was not examined.

## Specialists and generalists

Catabolic capacity is mostly a specialist trait. Among genomes carrying at least one of the 8 aromatic/alkaloid capacities, 675 are specialists with exactly 1 capacity. Only 18 are generalists with ≥3 capacities, and the maximum is 4. [src: enigma_carbon_census_1] Versatility is right-skewed, with mean ~1.19, median 1 and max 4 capacities per genome. [src: enigma_carbon_census_1] The report also finds this capacity phylogenetically concentrated in Burkholderiales. [src: enigma_carbon_census_1] See [[entities/burkholderiales]] and [[concepts/taxonomic-distribution-of-aromatic-compound-catabolism]].

## Co-occurrence between modules

Cross-module co-occurrence is near zero in share terms. Jaccard is ≈ 0, and only 25/3109 genomes carry both an aromatic and a non-aromatic capacity. [src: enigma_carbon_census_1] That is 0.8% of genomes. [src: enigma_carbon_census_1] The report's verdict is no broad cross-module modularity. [src: enigma_carbon_census_1]

Within the aromatic block, co-occurrence is expected. The six callable aromatics share one lower pathway and co-occur within the aromatic block. [src: enigma_carbon_census_1] See [[entities/ketoadipate-pathway]].

## Effect-size methods

The analysis first used the φ coefficient. φ compresses toward zero when a capacity is rare, and most capacities occur in tens to hundreds of 3109 genomes. This can hide a real multiplicative enrichment. [src: enigma_carbon_census_1] The review step (NB05b) therefore recomputed two effect sizes per pair from the saved 2×2 counts. These were a Haldane-corrected odds ratio (OR) with 95% confidence interval (CI), and the Jaccard index. No Spark re-run was needed. [src: enigma_carbon_census_1] The outputs cover 28 pairs: one file holds φ, p and q [src: enigma_carbon_census_1], and another holds the Haldane OR with CI and the Jaccard index. [src: enigma_carbon_census_1]

Results by pair class:

| Pair class | Median OR | Pairs with CI > 1 | Median Jaccard |
|---|---|---|---|
| Within-aromatic | 1.12 [src: enigma_carbon_census_1] | 3/10 [src: enigma_carbon_census_1] | 0.026 [src: enigma_carbon_census_1] |
| Cross-block (distinct lower pathways) | 2.28 [src: enigma_carbon_census_1] | 4/15 [src: enigma_carbon_census_1] | ≈ 0 [src: enigma_carbon_census_1] |

The within-other OR is driven by the Haldane correction on near-zero counts. [src: enigma_carbon_census_1] Cross-block pairs are the genuine modularity test. [src: enigma_carbon_census_1]

## The one positive signal

The Haldane OR detects a modest phenylethylamine×aromatic enrichment, with OR ≈ 2.8–3.4. [src: enigma_carbon_census_1] Two pairs show it:
- 4-hydroxybenzaldehyde with phenylethylamine: OR 2.84 (95% CI 1.49–5.40, q=0.035, n11=11). [src: enigma_carbon_census_1]
- Phthalic acid with phenylethylamine: OR 3.37 (95% CI 1.46–7.75, q=0.071, n11=6). [src: enigma_carbon_census_1]

The report reads this as aromatic-derived. Phenylethylamine is deaminated to phenylacetate and then enters the paa/phenylacetyl-CoA route, so versatile aromatic degraders tend to carry both. [src: enigma_carbon_census_1] This route is mechanistically separate from the β-ketoadipate funnel. [src: enigma_carbon_census_1] Even for these pairs, Jaccard stays ≈ 0.04, so only ~4% of genomes with either capacity carry both. [src: enigma_carbon_census_1] The report concludes that versatility is a clade trait, not a portable module set. [src: enigma_carbon_census_1] The positive signal is co-occurrence within the broad aromatic-catabolism phenotype, not co-assembly of mechanistically distinct modules. [src: enigma_carbon_census_1]

## Open Directions

- Test whether the phenylethylamine×aromatic enrichment survives a phylogenetically controlled test, for example within Burkholderiales only. This would separate clade structure from true module linkage.
- Repeat the Haldane OR and Jaccard analysis on a larger capacity set with more non-aromatic pathways. The cross-block test has only 15 pairs and few genomes with both module types (25/3109).
- Go beyond genome-level presence. Check gene proximity or operon context for the paa and funnel genes, to ask whether co-occurring capacities are physically linked and so portable.
