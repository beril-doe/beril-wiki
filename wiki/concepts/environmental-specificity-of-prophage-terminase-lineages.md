---
type: "Concept"
description: "Whether prophage lineages defined by terminase large-subunit (TerL) clustering show environment-specific enrichment beyond what host phylogeny predicts; covers lineage clustering, specialist/generalist classes and sensitivity to identity threshold."
sources: ["summaries/prophage_ecology__REPORT.md"]
---
# Environmental specificity of prophage terminase lineages

Prophage lineages defined by terminase large subunit (TerL) clustering show no individual environment-specific enrichment beyond what host phylogeny predicts. The evidence comes from one report, [[summaries/prophage_ecology__REPORT]], and rests on a permutation test that preserved host family composition. [src: prophage_ecology] The report does find specialist and generalist lineage classes, so niche breadth varies even though no single lineage's enrichment passes the null. [src: prophage_ecology]

## Literature Context

The candidate papers give context on how temperate phages and prophages are distributed across hosts, but none tests terminase lineages against environment, so none bears directly on the enrichment test. A comparative genomic study of 337 fully sequenced tailed phages infecting Enterobacteriaceae grouped them into 56 clusters (32 lytic and 24 temperate). It found that 78% of the subclusters correlate with host genus [PMID 25240328](https://pubmed.ncbi.nlm.nih.gov/25240328/). That is a single bacterial family, and it did not test environment. It does show that phage relatedness tracks host taxonomy.

In the human gut, an analysis of 43,942 bacterial genomes (439 species of 12 phyla) found 105,613 prophage regions in ~92% of the genomes. About 4% of prophages could integrate across genera, and ~17% showed broad predicted host ranges (2-35 genera) [PMID 39679618](https://pubmed.ncbi.nlm.nih.gov/39679618/). A cultivation study of gut phages isolated 32 temperate phages. These had higher prevalence in the human gut than lytic gut phages, and most carried diversity-generating retroelements and may have a broad host range [PMID 41362956](https://pubmed.ncbi.nlm.nih.gov/41362956/). Both are drawn from one habitat. They indicate that host range varies a lot between prophages, and the cultivation study is an abstract-level result from an isolate collection.

The corpus's finding is that no individual TerL lineage showed environment-specific enrichment beyond host phylogeny. This is consistent with the host-genus structure of phage clusters in [PMID 25240328](https://pubmed.ncbi.nlm.nih.gov/25240328/). The report's explanation is that lineage ecology mirrors host ecology, and the host-range findings in [PMID 39679618](https://pubmed.ncbi.nlm.nih.gov/39679618/) are compatible with it. These papers do not test the null directly, because they analyze neither environmental enrichment nor TerL lineages. So the corpus result is not confirmed by them. It stays a null result from one report, obtained with permutations that preserved host family composition.

The corpus's specialist and generalist classes, 325 and 499 lineages among 824 lineages with at least 5 species, extend this picture. The candidates give no comparable lineage-level niche-breadth measure, so that classification is novel relative to them. The broad host ranges of gut temperate phages ([PMID 41362956](https://pubmed.ncbi.nlm.nih.gov/41362956/)) and the cross-genus prophages ([PMID 39679618](https://pubmed.ncbi.nlm.nih.gov/39679618/)) parallel the generalist class. They do not show that generalists span environments. The tension with Paez-Espino et al. (2016) on habitat specificity, noted on the hub page, is not addressed by any candidate paper. The candidates also cannot settle whether the null depends on the identity threshold.

## Lineage clustering

[[entities/mmseqs2|MMseqs2]] clustering of 38,085 TerL protein sequences from 11,789 species at 70% amino acid identity yielded 10,991 lineages. [src: prophage_ecology] The report describes the size distribution as highly skewed, with median 1 and maximum 1,094. [src: prophage_ecology] Of these lineages, 6,921 (63%) are singletons, described as species-specific prophage types. [src: prophage_ecology] The largest lineage, L_SFJM01000051.1_13, has 1,094 members across 869 species, and the report calls it a cosmopolitan prophage type. [src: prophage_ecology] The 869 species figure describes that largest lineage. The 11,789 species figure describes all sequences clustered. [src: prophage_ecology]

The threshold sensitivity analysis gave lineage counts from 4,001 at 50% amino acid identity (AAI) to 16,283 at 80% AAI. [src: prophage_ecology]

## Enrichment test (H1b)

H1b was the hypothesis that TerL lineages show environment-specific enrichment. It was not supported at the individual lineage level, because no lineage passed false discovery rate (FDR) correction. [src: prophage_ecology] None of 500 tests was significant, which the report reads as lineage-level adaptation not exceeding what host phylogeny predicts. [src: prophage_ecology] The permutations preserved host family composition, and the lineage distribution is well explained by host phylogeny alone. [src: prophage_ecology]

## Specialists and generalists

Shannon entropy analysis covered 824 lineages with at least 5 species. [src: prophage_ecology] It identified 325 specialist lineages, defined by Shannon < 1.0 or a dominant environment above 80%. They concentrate in animal_associated, freshwater and marine environments. [src: prophage_ecology] It also identified 499 generalist lineages spread across 3+ environments. [src: prophage_ecology] The report concludes that niche breadth varies substantially between lineages, even though no single lineage's enrichment exceeds the constrained null model. [src: prophage_ecology]

## Interpretation

The report reads lineage ecology as largely mirroring host ecology, not independent environmental adaptation. It links this to the two modes of temperate phage evolution, high and low gene flux, described by Mavrich & Hatfull (2017). [src: prophage_ecology] That earlier work found temperate phage evolution shaped mainly by host range, not environmental selection. [src: prophage_ecology]

Module-level and lineage-level ecology are decoupled. Modules show environment effects beyond phylogeny and lineages do not, which suggests modular exchange rather than whole-phage adaptation. [src: prophage_ecology] See [[concepts/environmental-structuring-of-prophage-gene-modules-beyond-host-phylogeny]].

## Tensions

- The null lineage-level result [src: prophage_ecology] contrasts with Paez-Espino et al. (2016), who found strong habitat-type specificity for most viral groups. [src: prophage_ecology] The report notes that its own analysis used constrained permutations preserving host family composition. [src: prophage_ecology]

## Open Directions

- Repeat the constrained-permutation test at several AAI thresholds between 50% and 80%. This would show whether the null result depends on lineage granularity.
- Rerun the test without host-family constraints, so the result can be compared directly with Paez-Espino-style habitat specificity.
- Test whether the 325 specialist lineages are enriched for their environments within host families. This would separate host ecology from environmental effects.
- Run the same enrichment test on modules and lineages with matched host controls, to check the proposed modular-exchange explanation.
