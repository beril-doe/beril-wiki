<!-- tension-hash: cded18a33b671af0 -->
# Do co-inherited resistance islands and cofitness network size measure the same thing?

Two projects in this corpus characterise the "architecture" of antimicrobial-resistance (AMR) gene sets with different instruments and arrive at claims that are hard to hold together without care. One measures co-inheritance across genomes — whether resistance genes travel together — and finds it strong. The other measures functional coupling in fitness space — whether a gene's cofitness neighbourhood size tracks its fitness cost — and finds nothing. The disagreement is not about a shared number; it is about whether these are two readings of one underlying network, or two different networks that happen to share a vocabulary. It matters because treating them as interchangeable would let a genomic linkage result be cited as evidence of functional synergy, which neither project claims. See [[concepts/antimicrobial-resistance-fitness-cost]].

## Evidence Sides

**Genomic co-inheritance is strong and multi-mechanism.** Resistance islands show a mean phi of **0.827** — phi being a correlation coefficient for binary presence/absence data, where values near 1 mean genes are almost always found together or absent together — and **88%** of islands contain genes from multiple resistance mechanisms, together indicating strong co-inheritance. [src: amr_strain_variation] Critically, the same project explicitly cautions that linkage on mobile genetic elements (transposons, integrons, genomic islands that move as units) does not prove co-selection or functional synergy. [src: amr_strain_variation]

**Functional coupling shows no size–cost relationship.** Against this, the cofitness analysis — cofitness being the correlation between two genes' fitness profiles across many experimental conditions — yields a null relationship between cofitness network size and fitness cost. [src: amr_cofitness_networks] The null stays null: it is an absence of detected association, not a demonstrated absence of coupling.

Thus genomic co-inheritance can coexist with a null cofitness-size–cost relationship, and the two analyses should not be treated as interchangeable measures of network architecture. [src: amr_strain_variation] [src: amr_cofitness_networks]

## Possible Reconciliations

- *Hypothesis: different timescales.* Co-inheritance records historical selection and physical linkage accumulated over evolutionary time, whereas cofitness records contemporaneous phenotypic coupling in laboratory conditions; the two need not correlate. [src: amr_strain_variation] [src: amr_cofitness_networks]
- *Hypothesis: hitchhiking without synergy.* Genes may be co-mobilised as intact units without interacting functionally, which would produce tight co-occurrence alongside no cost structure in fitness space — a reading the atlas's own caution leaves open. [src: amr_strain_variation]
- *Hypothesis: condition mismatch.* If the conditions assayed for cofitness rarely include the antibiotic pressures that maintain islands, functional coupling could exist but go undetected, leaving the null intact as a statement about the assayed conditions only. [src: amr_cofitness_networks]

## Resolving Work

- Restrict cofitness computation to antibiotic-exposure conditions versus standard growth and ask whether a size–cost relationship appears only under selection, testing the condition-mismatch hypothesis. [src: amr_cofitness_networks]
- Run a permutation test — re-computing the statistic over randomly redrawn comparison sets to build a null distribution — using non-AMR genes matched on mean fitness level, and ask whether AMR cofitness neighbourhoods are distinguishable from a shared-dispensability baseline, the pattern expected when two genes look coupled only because both are dispensable under the assayed conditions. [src: amr_cofitness_networks]
- Intersect island membership with cofitness neighbourhoods gene-by-gene, asking whether genes inside high-phi islands are cofit with their island partners at all. [src: amr_strain_variation] [src: amr_cofitness_networks]
- Stratify islands by mechanism composition and ask whether multi-mechanism islands differ from single-mechanism ones in measured fitness cost. [src: amr_strain_variation]
- Extend the cofitness test to other dispensable gene classes to establish whether any null result is AMR-specific or general. [src: amr_cofitness_networks]
