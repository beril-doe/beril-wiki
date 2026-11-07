---
type: "Research direction"
description: "Are Crohn's candidate species disease-linked because of their own properties, or because of the community state (ecotype) they sit in, so that the same species is Crohn's-enriched in one state and neutral in another?"
hypothesis: "The Crohn's association of a candidate species depends on community state: species called in one state are not Crohn's-enriched when the same species are examined in the other state. Placing a candidate in an altered community in a gnotobiotic host changes its expansion."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The state-specific lists exist, but the second state has only one eligible sub-study with provisional candidates, and the gnotobiotic step needs new experiments."
collections: []
findings: ["ibd_phage_targeting--56e3bb7d", "ibd_phage_targeting--d7f80dce"]
conflicts: ["conflict--compositional-robustness-of-differential-abundance-calls--b440b98c"]
papers: ["28130329", "39244168"]
builds_on: ["findings/ibd_phage_targeting--56e3bb7d", "findings/ibd_phage_targeting--d7f80dce", "conflicts/conflict--compositional-robustness-of-differential-abundance-calls--b440b98c"]
projects: ["ibd_phage_targeting"]
topics: ["translational-microbiome-and-phage-therapeutics"]
---
# Does the same gut species become Crohn's-associated only inside a particular community state?

Are Crohn's candidate species disease-linked because of their own properties, or because of the community state (ecotype) they sit in, so that the same species is Crohn's-enriched in one state and neutral in another?

## Hypothesis

The Crohn's association of a candidate species depends on community state: species called in one state are not Crohn's-enriched when the same species are examined in the other state. Placing a candidate in an altered community in a gnotobiotic host changes its expansion.

## Why it matters

The two states pick very different target lists, and a permutation check against shuffled labels showed that this divergence is not chance. If association is state-dependent, targeting should be decided per community state and not per species. If it is species-intrinsic, the state partition adds nothing to target choice.

## How to test it

Step 1, on existing cohort data: for each species on the first-state and second-state candidate lists, estimate its Crohn's-versus-non-IBD direction within the other state, using only sub-studies with both groups, and ask whether the two lists agree in direction or are state-specific. Note that 45 of 51 first-state candidates kept the same direction in a held-out cohort, and the second-state list is provisional because only one sub-study qualifies. Step 2: colonize germ-free mice with a defined community mimicking each state plus one candidate species such as Flavonifractor plautii or Escherichia coli, and measure expansion of the candidate under an inflammatory challenge in each background.

## What would support or refute it

Support: candidates are Crohn's-enriched only in their own state, and the same species expands more in the matching defined community. Refutation: candidates show the same Crohn's direction in both states and expand equally in either synthetic background, meaning the association is species-intrinsic.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The state-specific lists exist, but the second state has only one eligible sub-study with provisional candidates, and the gnotobiotic step needs new experiments.

## Builds on

- Finding: [[findings/ibd_phage_targeting--56e3bb7d|Ecotype-specific targeting survives, but the earlier Jaccard statistic was replaced]] (Insufficient literature evidence)
- Finding: [[findings/ibd_phage_targeting--d7f80dce|E1 Crohn's candidate species replicate in held-out HMP2 cohort]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--compositional-robustness-of-differential-abundance-calls--b440b98c|Within-ecotype differential abundance: an unusable 3-taxon survivor set, or a design-controlled 51 and 40?]]

## Closest published work

- [PMID 28130329](https://pubmed.ncbi.nlm.nih.gov/28130329/) Bacteriophages Targeting Adherent Invasive Escherichia coli Strains as a Promising New Treatment for Crohn's Disease.
- [PMID 39244168](https://pubmed.ncbi.nlm.nih.gov/39244168/) Population-specific differences in the human microbiome: Factors defining the diversity.

PMID 28130329 targets a single pathobiont group in Crohn's and PMID 39244168 surveys microbiome differences between populations; neither asks whether one species' disease association depends on its community state.
