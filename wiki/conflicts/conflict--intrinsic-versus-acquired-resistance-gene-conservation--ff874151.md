<!-- tension-hash: ff874151ad465d19 -->
# Intrinsic Versus Acquired Resistance Genes: Does Conservation Track Lineage?

Antimicrobial resistance (AMR) genes are often split into intrinsic (core, present across a species) and acquired (non-core, putatively moved by horizontal transfer). The expectation is that acquired genes follow lineage less than intrinsic genes. Phylogenetic signal in strain data points the other way, and core status is not fully fixed within species. This matters because the intrinsic/acquired reading rests on conservation patterns, not direct measurement of mobility. The tension comes from [[concepts/intrinsic-versus-acquired-resistance-gene-conservation]].

## Evidence Sides

**Side A: non-core genes carry stronger lineage signal than core genes**

- Non-core (putatively acquired) AMR genes show stronger phylogenetic signal (median r = 0.222) than core genes (median r = 0.117). Signal is measured by Mantel r, a correlation between gene-content distance and phylogenetic distance. The paired t-test gave t = -8.35, p = 7.0e-16, n = 489. [src: amr_strain_variation]
- Near-universal core genes have near-zero Jaccard distances (a gene-content dissimilarity) and little variance. This suppresses Mantel r and partly explains the lower core signal independent of biology. [src: amr_strain_variation]

**Side B: core and non-core classes differ in within-species variation, with caveats**

- Core is not fully fixed within species. Atlas core AMR genes are 77.3% fixed and 22.7% variable. [src: amr_strain_variation]
- Auxiliary genes are 57.3% variable and 42.7% rare. [src: amr_strain_variation]
- Singletons are 21.3% variable and 78.7% rare. [src: amr_strain_variation]
- The atlas report claims universality. It also cautions that some singleton AMR clusters may be annotation artifacts. [src: amr_pangenome_atlas]
- The per-gene and per-phylum tests are exploratory and hypothesis-generating. No Bonferroni or FDR (false discovery rate) correction was applied, because primary p-values were extreme. [src: amr_pangenome_atlas]

## Possible Reconciliations

- **Hypothesis: the variance artifact.** Core genes are nearly invariant, so Mantel r understates their vertical inheritance. The gap may then reflect the metric, not biology. This is consistent with the report's own note. [src: amr_strain_variation]
- **Hypothesis: clonal retention of acquired genes.** A lineage may acquire a resistance element and then maintain it vertically, which would give non-core genes lineage structure. Acquisition and inheritance are then not mutually exclusive. [src: amr_strain_variation]
- **Hypothesis: annotation noise in rare classes.** Some singleton clusters may be artifacts, which would blur the non-core signal. [src: amr_pangenome_atlas]

## Resolving Work

- Data: the same 489 comparisons. Method: a signal measure not driven by variance, such as a permutation-based test restricted to variable genes. Question: does non-core still exceed core?
- Data: core genes split into fixed and variable within species. Method: compare Mantel r between the two groups. Question: is the 22.7% variable core fraction the source of any core signal?
- Data: singleton AMR clusters. Method: re-check annotations against independent databases. Question: how many are artifacts, and does removing them change the non-core signal?
- Data: per-gene and per-phylum tests. Method: apply FDR correction and report the adjusted results. Question: which findings survive correction?
- Data: genomic context of non-core AMR genes. Method: look for mobile-element flanking and compare it with lineage structure. Question: is acquisition evidenced directly, not inferred from conservation class?
