---
type: "Concept"
description: "Whether the distribution of prophage functional modules across bacterial species tracks environment after host phylogeny and genome size are accounted for; stops at the lineage level, which is a separate concept."
sources: ["summaries/prophage_ecology__REPORT.md"]
---
# Environmental structuring of prophage gene modules beyond host phylogeny

Prophage functional modules track environment even after host phylogeny and genome size are accounted for, in one report (prophage_ecology). [src: prophage_ecology] Lineage-level patterns are a separate concept ([[concepts/environmental-specificity-of-prophage-terminase-lineages]]). For the broader confounder problem see [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]].

## Literature Context

The candidate papers give indirect context for the hub's question. None of them tests module-level prophage composition against environment while controlling for host phylogeny. A host-centric analysis of 5821 complete bacterial genomes built a life-history space defined mainly by genome size, metabolic capacity and growth rate potential. Prophage burden formed a continuous gradient across that space, and virulent phage association correlated positively with prophage burden [PMID 42372072](https://pubmed.ncbi.nlm.nih.gov/42372072/). That abstract shows host traits are relevant to prophage carriage. It does not compare host traits with environment, and it does not test whether genome size confounds environmental effects. It also reports enrichment of resource-acquisition modules, a functional-trait view that is loosely parallel to the hub's module-level framing [PMID 42372072](https://pubmed.ncbi.nlm.nih.gov/42372072/).

Two habitat-specific studies point to environment-dependent prophage ecology. In the gut symbiont Lactobacillus reuteri, nearly all human- and rodent-derived strains carried active prophages, but fewer than half of the tested porcine strains did. The authors suggest host-specific lineages differ in the role phages play [PMID 31676478](https://pubmed.ncbi.nlm.nih.gov/31676478/). The same work found prophage carriage costly in conventional mice but advantageous in gnotobiotic mice, where it killed a sensitive competitor. This is a single-species model with strain 6475 as the main system [PMID 31676478](https://pubmed.ncbi.nlm.nih.gov/31676478/). In the North Pacific Subtropical Gyre, viral marker genes suggested lysogeny was more prevalent at mesopelagic depths than in surface waters. Mesopelagic phages also differed from surface phages in gene content and putative life histories [PMID 29184020](https://pubmed.ncbi.nlm.nih.gov/29184020/). That is a time-series survey at one ocean site.

The hub's finding that prophage modules track environment after accounting for host phylogeny and genome size is consistent in direction with this literature. Habitat and host context relate to prophage presence and lifestyle in the gut [PMID 31676478](https://pubmed.ncbi.nlm.nih.gov/31676478/) and in the ocean [PMID 29184020](https://pubmed.ncbi.nlm.nih.gov/29184020/). Host genome-scale traits also matter [PMID 42372072](https://pubmed.ncbi.nlm.nih.gov/42372072/). The ranking the report gives (genome size, then environment, then phylogeny) comes from its own PERMANOVA on an n=1,773 species subsample with 99 permutations. The candidate abstracts neither support nor contradict it.

The corpus extends the literature in three ways. First, it resolves prophage content into functional modules: head morphogenesis, tail and anti-defense. Second, it reports enrichment of these modules in human-associated and clinical environments in a constrained null model across 18,031 species. The cited papers do not address anti-defense modules, and they do not test human-associated enrichment at this scale, so these results are novel relative to the candidates. Third, the report's interpretation, that human-associated bacteria face stronger phage selection and retain complete machinery, is untested. The L. reuteri work shows prophage carriage can carry both costs and competitive benefits in the gut [PMID 31676478](https://pubmed.ncbi.nlm.nih.gov/31676478/). That fits a selection-based reading but does not establish it. Finally, the Open Directions calls for a full-species-set PERMANOVA and finer taxonomic strata. These checks remain needed, because no candidate paper addresses them.

## Predictors of module composition

Genome size is the dominant predictor, followed by environment, then phylogeny. [src: prophage_ecology] The report used PERMANOVA (permutational multivariate analysis of variance, see [[entities/permanova]]) on Bray-Curtis distances of module composition, with an n=1,773 species subsample and 99 permutations. All three predictors were significant. [src: prophage_ecology] The F-statistics were 212.99 for genome size quartile (4 groups) [src: prophage_ecology], 30.04 for environment (10 groups) [src: prophage_ecology] and 6.17 for host family phylogeny (294 groups), each at p=0.01. [src: prophage_ecology]

The report therefore rejected the hypothesis that phylogeny alone explains prophage distribution. [src: prophage_ecology] Genome size is a possible artifact, so the report stratified by it. Within each genome size quartile, Kruskal-Wallis tests still found an environmental effect on module count (all p < 6.5e-78). The report reads this as showing the signal is not a genome size artifact. [src: prophage_ecology]

A second line uses [[entities/alphaearth-environmental-embeddings]]. For 2,008 species with ≥5 embedded genomes, niche breadth correlated with prophage module count after controlling for genome size (partial Spearman rho=0.468, p=8.41e-110). [src: prophage_ecology]

## Which modules carry the signal

Ubiquitous modules (A, D, F) vary little with environment. The structurally variable modules (B, C, G) carry the environmental signal. [src: prophage_ecology] Modules A, D and F were all ≥99% prevalent in the top 15 of 142 GTDB phyla. [src: prophage_ecology] The variable modules are head morphogenesis (B), tail (C) and anti-defense (G). They occur in 56.1%, 55.6% and 64.3% of species respectively. [src: prophage_ecology]

Prevalence ranges are wide:
- Head morphogenesis (B) runs from 10.2% in Thermoplasmatota to 81% in human_associated species. [src: prophage_ecology]
- Tail (C) runs from 6.5% in Thermoplasmatota to 82% in food-associated species. [src: prophage_ecology]
- Anti-defense (G) runs from 3.1% in Patescibacteria to 97.8% in Campylobacterota. [src: prophage_ecology]

Chi-squared tests found significant environment associations for B_head (chi2=1,051, p=1.72e-220) [src: prophage_ecology], C_tail (chi2=1,749, p≈0) [src: prophage_ecology] and G_anti_defense (chi2=818, p=2.58e-170). [src: prophage_ecology]

## Constrained null models

Permutation null models (500 permutations, preserving host family × genome size quartile strata, 18,031 species) found 8 significant module × environment enrichments (FDR, false discovery rate, < 0.05). [src: prophage_ecology] Enrichment is reported as log2 odds ratio (OR) with a Z-score.

| Module | Environment | log2(OR) | Z | Direction |
|---|---|---|---|---|
| Tail | human_associated | 2.21 | 10.86 | Enriched [src: prophage_ecology] |
| Head Morphogenesis | human_associated | 1.98 | 10.00 | Enriched [src: prophage_ecology] |
| Anti-Defense | human_associated | 1.70 | 8.76 | Enriched [src: prophage_ecology] |
| Anti-Defense | human_clinical | 0.14 | 5.14 | Enriched [src: prophage_ecology] |
| Tail | human_clinical | 0.77 | 3.90 | Enriched [src: prophage_ecology] |
| Head Morphogenesis | human_clinical | 0.70 | 3.59 | Enriched [src: prophage_ecology] |
| Anti-Defense | freshwater | -0.74 | -4.74 | Depleted [src: prophage_ecology] |
| Anti-Defense | animal_associated | -0.24 | -8.77 | Depleted [src: prophage_ecology] |

Anti-defense is the most environmentally responsive module. [src: prophage_ecology] Human-associated and clinical environments had higher prevalence of tail, head morphogenesis and anti-defense than freshwater, marine and animal-associated environments, after controlling for host family composition and genome size. [src: prophage_ecology] The pangenome enrichment and NMDC correlation analyses agreed: B_head_morphogenesis, C_tail and G_anti_defense were significant in both. [src: prophage_ecology] See [[concepts/prophage-anti-defense-genes-and-host-phage-arms-races]] for the anti-defense context.

## Interpretation

The Piggyback-the-Winner framework predicts higher lysogeny at high microbial densities in host-associated environments. [src: prophage_ecology] The report extends this. It finds that structural completeness and anti-defense repertoire increase, not only lysogeny. [src: prophage_ecology] It suggests, as an interpretation and not a tested result, that human-associated bacteria face more intense phage-mediated selective pressure. That pressure would drive retention of complete lytic machinery and counter-defense genes. [src: prophage_ecology] The report calls the pattern consistent with Low et al. (2024), who found prophage cargo genes enriched in human-impacted environments. [src: prophage_ecology]

Module-level and lineage-level ecology are decoupled. Modules show environment effects beyond phylogeny and lineages do not. The report suggests modular exchange rather than whole-phage adaptation. [src: prophage_ecology] The report claims this is the first systematic module-level analysis across >27,000 species and 10 environment categories. [src: prophage_ecology]

## Open Directions

- Repeat the PERMANOVA with more than 99 permutations and the full species set, since 99 permutations on a 1,773-species subsample limits p to 0.01.
- Run the constrained null with finer taxonomic strata (genus instead of family) to test whether the human-associated enrichments survive.
- Test whether the human-associated enrichment reflects sampling of well-studied clinical taxa, by controlling for genome sampling depth per species.
- Test the modular-exchange hypothesis directly by comparing module phylogenies with host phylogenies for tail, head and anti-defense modules.
