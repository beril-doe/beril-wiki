<!-- tension-hash: 25579b23a142c77a -->
# Tension: Broad Pfam Coverage Versus Legacy Annotation Specificity in Cofitness Analysis

Two projects disagree about which annotation source best supports functional interpretation of genome-wide cofitness (genes whose fitness effects across experiments are correlated). One side expects Pfam (a protein domain database) to give broad coverage, but cautions that domain-level labels may overcount functional associations. The other side reports that legacy annotations are not uniformly worse: old KEGG (a pathway database) annotations found mechanism-specific terms that InterProScan GO (Gene Ontology terms assigned by the InterProScan tool) did not. This matters because the choice of annotation source decides which enrichment signals can be seen. The concept context is [[concepts/annotation-coverage-and-resolution-in-genome-wide-cofitness-analysis]].

## Evidence Sides

**Side A: Pfam is broad but may overcount, and may be more specific than GO**

- Pfam gives the broadest coverage in fitness_modules, but its domain-level labels may overcount functional associations. [src: fitness_modules]
- In the antimicrobial resistance (AMR) project, Pfam domain-level enrichment is proposed as a way to find more specific support-network functions than broad GO terms. [src: amr_cofitness_networks]
- Both statements are expectations or cautions, not tested results.

**Side B: legacy annotations are not uniformly worse**

- Old KEGG annotations identified 2 mechanism-specific terms at FDR<0.05 (lipoprotein, toluene tolerance), whereas InterProScan GO identified 0. [src: amr_cofitness_networks]
- FDR is the false discovery rate, the expected share of false positives among the significant results. FDR<0.05 is the threshold used.
- This is a reported comparison result, not only an expectation. It comes from one analysis design in one project.

## Possible Reconciliations

- **Hypothesis 1: different questions.** Broad terms may suit detecting shared themes, and more specific labels may suit mechanism-specific signals. The two sides may measure different things.
- **Hypothesis 2: Pfam overcounting is a separate issue from specificity.** Pfam may add specific signals and also inflate associations, so each effect would need its own test.
- **Hypothesis 3: the KEGG result is annotation-specific.** The 2 terms may reflect the content of KEGG for those mechanisms and not general legacy quality.

## Resolving Work

- Run Pfam domain enrichment in the AMR cofitness neighborhoods, using the same FDR<0.05 threshold. The question is whether it recovers the 2 KEGG terms (lipoprotein, toluene tolerance) that InterProScan GO missed. [src: amr_cofitness_networks]
- Compare Pfam against permuted or matched random gene sets in fitness_modules. The question is how much Pfam domain labels inflate associations. [src: fitness_modules]
- Re-run the KEGG versus InterProScan GO comparison with other organism sets or analysis designs. The question is whether the 2 versus 0 mechanism-specific result holds.
- Test annotation sources with a common denominator of genes and tests. The question is whether coverage differences, not resolution, explain the mechanism-specific results.
- Manually check the KEGG terms found against known biology. The question is whether they are real functional signals or annotation artifacts.
