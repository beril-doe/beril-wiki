<!-- tension-hash: cded18a33b671af0 -->
# Does genomic co-inheritance of resistance genes measure the same network architecture as cofitness?

The [[concepts/antimicrobial-resistance-fitness-cost]] page records a measurement tension about the architecture of antimicrobial-resistance (AMR) genes. Resistance islands indicate that AMR genes are strongly co-inherited across genomes [src: amr_strain_variation]. Cofitness is the correlation of gene-knockout fitness profiles across experiments. The cofitness analysis shows a null relationship between network size and cost, and genomic co-inheritance can coexist with that null [src: amr_strain_variation] [src: amr_cofitness_networks]. The two results do not oppose each other. The open question is whether they measure the same thing. This matters because the wiki could otherwise treat one analysis as confirming or refuting the other. The tension does not resolve the third tension recorded on the concept page; it adds a separate question about what each measurement captures [src: amr_strain_variation].

## Evidence Sides

**Side A: strong genomic co-inheritance of resistance genes**

Resistance islands show a mean phi coefficient of **0.827** [src: amr_strain_variation]. The phi coefficient is a correlation measure for two binary presence/absence variables. **88%** of islands are multi-mechanism islands [src: amr_strain_variation]. Read directly, these figures indicate strong co-inheritance [src: amr_strain_variation]. However, the atlas explicitly cautions that linkage on mobile genetic elements does not prove co-selection or functional synergy [src: amr_strain_variation]. Mobile genetic elements are DNA segments, such as transposons or integrons, that move between genomes. Co-selection here means joint selection acting on linked resistance determinants. Functional synergy means that the linked genes' products interact to produce a combined effect. Under that caveat, co-inheritance is an observed genomic pattern, not established evidence that the linked genes work together.

**Side B: a null relationship between cofitness network size and cost**

The cofitness analysis gives a null result: cofitness-network size shows no relationship to cost [src: amr_strain_variation] [src: amr_cofitness_networks]. This is a null finding. It is not a negative effect, and it should not be read as evidence that networks are absent or unimportant. The concept page argues that genomic co-inheritance can coexist with this null result. It also argues that the two analyses should not be treated as interchangeable measures of network architecture [src: amr_strain_variation] [src: amr_cofitness_networks].

## Possible Reconciliations

- *Hypothesis 1: different levels of organisation.* Co-inheritance records which genes travel together across genomes. Cofitness records which genes behave alike when knocked out in laboratory fitness assays. A strong signal at one level would not require a signal at the other.
- *Hypothesis 2: hitchhiking without synergy.* Genes linked on mobile genetic elements may be co-inherited without sharing a functional role. If so, high phi values would carry no prediction about fitness-cost coupling. This is consistent with the atlas's own caution [src: amr_strain_variation].
- *Hypothesis 3: limits of the cofitness assay.* The null result may reflect what the assays can detect rather than true biological independence.

## Resolving Work

- **Island-member cofitness:** Take the genes inside detected resistance islands and compute cofitness among them in the fitness data. Ask whether co-inherited genes are also co-fit more often than random gene pairs.
- **Condition-specific cofitness:** Recompute cofitness separately for antibiotic conditions and standard growth. Ask whether island partners become co-fit only under drug exposure, which would link co-inheritance to function.
- **Mobile-element stratification:** Split islands by whether they sit on annotated mobile genetic elements and compare phi between the two groups. Ask whether tight co-occurrence persists outside mobile contexts.
- **Matched null models:** For the network-size–cost test, build fitness-matched permutation baselines that repeatedly sample random non-resistance genes matched on mean fitness. Ask whether the null result holds against baselines that control for gene dispensability, the extent to which a gene can be lost without a fitness effect under the test conditions.
