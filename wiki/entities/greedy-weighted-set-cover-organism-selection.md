---
type: "Method"
description: "Greedy weighted set-cover algorithm selecting a minimum set of organisms covering priority-weighted dark genes, in evidence-weighted and conservation-weighted variants."
sources: ["summaries/discoveries.md", "summaries/functional_dark_matter__REPORT.md"]
aliases: ["minimum covering set"]
---
# Greedy weighted set-cover organism selection

Greedy weighted set-cover organism selection (also called the minimum covering set) is the method that chooses a small set of organisms to cover priority-weighted dark genes. Two variants are reported: an evidence-weighted Route A and a conservation-weighted Route B. Both pick 42 organisms covering about 95% of priority, and the evidence comes from the functional_dark_matter report and the discoveries digest. [src: discoveries, functional_dark_matter]

## Key facts

- The method is a greedy weighted set-cover algorithm that optimizes priority value × tractability × phylogenetic diversity. [src: functional_dark_matter]
- The dark-gene minimum covering set selects 42 organisms from 28 genera covering 95% of total priority. [src: functional_dark_matter]
- Each dark gene is assigned to exactly one organism for experimental follow-up. [src: functional_dark_matter]
- The algorithm is described as two complementary greedy weighted set-cover algorithms, Route A (NB09) and Route B (NB11). [src: functional_dark_matter]

## Route A: evidence-weighted (NB09)

Route A optimizes Σ(composite_score) × tractability × phylo_diversity. [src: functional_dark_matter] It selects 42 organisms from 28 genera. [src: functional_dark_matter] These organisms cover 95% of the total priority value across 16,488 scored dark genes. [src: functional_dark_matter] The route is optimized for genes with testable hypotheses. [src: functional_dark_matter]

MR-1 ranks first and contributes 587 genes. [src: functional_dark_matter] 32 organisms suffice for 80% coverage. [src: functional_dark_matter]

## Route B: conservation-weighted (NB11)

Route B optimizes Σ(importance) × tractability × phylo_bonus. [src: functional_dark_matter] The phylo_bonus term penalizes genus-redundant selections. [src: functional_dark_matter] It selects 42 organisms from 28 genera. [src: functional_dark_matter] These cover 95.6% of total importance-weighted priority across 28,584 high-priority dark genes. [src: functional_dark_matter] The route is optimized for discovering functions of broadly conserved true knowledge gaps. [src: functional_dark_matter]

## Relation between the routes

The routes share 39 organisms but order them differently, which reflects different experimental strategies. [src: discoveries, functional_dark_matter] The report calls them complementary. Route A produces mechanistic insights for genes with hypotheses. Route B discovers functions for broadly conserved true knowledge gaps. [src: functional_dark_matter] The discoveries digest states that this allows targeted hypothesis testing (Route A) and novel function discovery (Route B) from largely the same organism set. [src: discoveries]

See also [[concepts/organism-selection-and-taxonomic-coverage-bias-for-experimental-characterization-of-dark-genes]], [[summaries/functional_dark_matter__REPORT]] and [[summaries/discoveries]].
