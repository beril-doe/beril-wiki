---
type: "Finding"
description: "Among 11,774 root ortholog groups classified by the narrowest taxonomic rank containing all member species, 55.9% are kingdom-level; at the gene level (57,011 dark genes including 19,014 FB-only fallback assignments), 51.4% are kingdom-level."
finding_id: "functional_dark_matter--b069dc6a"
result: "observation"
source: "functional_dark_matter"
quantities: [{"value": "55.9%", "what": "root OGs classified kingdom-level", "unit": "percent", "denominator": "11,774 root OGs", "scope": ""}, {"value": "51.4%", "what": "dark genes in kingdom-level tier", "unit": "percent", "denominator": "57,011 dark genes including 19,014 FB-only fallback assignments", "scope": ""}]
caveat: "The 48 Fitness Browser organisms are biased (37/48 Pseudomonadota; Bacillota, Actinomycetota and Campylobacterota have zero representation), so kingdom-level groups (55.9% of dark gene ortholog groups) cannot be addressed in non-Proteobacterial hosts using them alone."
first_added: "2026-10-23"
source_hash: "1ea00a93830c52ac6d4c47418f8d718cf6b5aa2d81462a64855a8308888da1d0"
---
# Over half of dark-gene ortholog groups are pan-bacterial

Among 11,774 root ortholog groups classified by the narrowest taxonomic rank containing all member species, 55.9% are kingdom-level; at the gene level (57,011 dark genes including 19,014 FB-only fallback assignments), 51.4% are kingdom-level. [src: functional_dark_matter]

## Key figures

- **55.9%**: root OGs classified kingdom-level (denominator 11,774 root OGs) [src: functional_dark_matter]
- **51.4%**: dark genes in kingdom-level tier (denominator 57,011 dark genes including 19,014 FB-only fallback assignments) [src: functional_dark_matter]

## Evidence

> The 11,774 root OGs are classified into 8 taxonomic tiers based on the narrowest rank containing all member species: **kingdom 55.9%**, class 11.0%, family 10.5%, genus 6.9%, mobile 6.5%, phylum 4.8%, order 3.9%, species 0.5%. Over half of dark gene OGs are pan-bacterial — present across multiple phyla and thousands of species — demonstrating that functional dark matter is not a minor annotation gap but a fundamental limitation in our understanding of broadly conserved biology. At the gene level (57,011 dark genes including 19,014 FB-only fallback assignments): kingdom 51.4%, species 29.8%, genus 6.2%, class 4.0%, family 3.5%, mobile 1.9%, phylum 1.9%, order 1.3%. [src: functional_dark_matter]

From the report [[summaries/functional_dark_matter__REPORT]].

## Caveat

The 48 Fitness Browser organisms are biased (37/48 Pseudomonadota; Bacillota, Actinomycetota and Campylobacterota have zero representation), so kingdom-level groups (55.9% of dark gene ortholog groups) cannot be addressed in non-Proteobacterial hosts using them alone. [src: functional_dark_matter]

> Both covering sets draw only from the 48 FB organisms, which are heavily biased: 37/48 are Pseudomonadota (Proteobacteria), with Bacteroidota (4), Cyanobacteriota (1), and Halobacteriota (2) the only other phyla represented. Major bacterial phyla — Bacillota (Firmicutes), Actinomycetota (Actinobacteria), and Campylobacterota — have zero FB representation. This means kingdom-level OGs (55.9% of dark gene OGs, present across multiple phyla) cannot be experimentally addressed in their non-Proteobacterial hosts using FB organisms alone. [src: functional_dark_matter]

## Other caveats in this report

- The fraction of hypothetical genes ranges from >35% to <15% across species; the report attributes this variation to annotation depth rather than true functional content. [src: functional_dark_matter]
- The pathway-gap result is organism-level co-occurrence, not direct gene-to-gap enzymatic matching. [src: functional_dark_matter]
- Dark-gene gap filling remains a hypothesis requiring enzyme-number matching, structure prediction, or experiments. [src: functional_dark_matter]
- Marinobacter has 49 gapped pathways, and D. desulfuricans ME-23 and P. stutzeri have 45 each; their dark genes are proposed, not established, as possible missing-step enzymes. [src: functional_dark_matter]
- The report interprets carbon-source and motility concordance as possible conserved unannotated functions, and OG05812 as a possible stress-associated regulatory protease; these are functional hypotheses. [src: functional_dark_matter]
