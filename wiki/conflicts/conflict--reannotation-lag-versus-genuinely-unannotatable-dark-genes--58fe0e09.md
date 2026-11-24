<!-- tension-hash: 58fe0e0921ca3b9c -->
# Reannotation Lag or Genuinely Unannotatable: Do Dark-Gene Counts Overstate the Unknown?

This tension concerns how much of the "dark" gene set (genes with no assigned function, such as hypothetical proteins) is truly uncharacterized. Bakta, a genome annotation tool, is used to re-annotate these genes. Its output can be read as confirming that the remaining dark genes deserve experimental follow-up. It can also be read as showing that the dark-gene count is inflated by out-of-date annotation, which is reannotation lag. The answer decides where experimental effort goes, and whether the remaining dark genes are a real gap in knowledge or a gap in database coverage. The framing comes from [[concepts/reannotation-lag-versus-genuinely-unannotatable-dark-genes]].

## Evidence Sides

**Side A: Bakta annotations validate the experimental prioritization**

- The functional_dark_matter report treats Bakta annotations as validating its experimental prioritization of dark genes. [src: functional_dark_matter]
- This side does not claim the prioritization is free of caveats. It lists two caveats of its own, described under Side B.

**Side B: the dark-gene count likely overestimates uncharacterized genes**

- Bakta "hypothetical" calls may be false negatives for genes whose functions are in fact known. A hypothetical call from Bakta therefore does not prove that a gene is unannotatable. [src: truly_dark_genes]
- Databases that were not checked may annotate some of the genes counted as dark. The dark-gene count therefore likely overestimates the number of uncharacterized genes. [src: functional_dark_matter]

Both caveats point the same way, toward overestimation. The first caveat comes from truly_dark_genes and the second from functional_dark_matter. The same project that treats Bakta as validation also states the second caveat. The two sides are therefore partly in tension within one report, not only between projects.

## Possible Reconciliations

- **Hypothesis: validation and overestimation answer different questions.** Bakta agreement may show that the prioritized genes are reasonable candidates, while the unchecked-database caveat bounds how many dark genes there really are. Neither claim has been tested against the other.
- **Hypothesis: the false negatives are concentrated in poorly covered lineages.** If Bakta hypothetical calls miss known functions mainly where database coverage is thin, the overestimate would vary by lineage and would not be uniform.
- **Hypothesis: extra databases would shrink the dark set without emptying it.** This is untested. It would leave a residue that is genuinely unannotatable, but the size of that residue is unknown.

## Resolving Work

- **Data:** the genes called hypothetical by Bakta. **Method:** search them against databases not yet checked. **Question:** what fraction receive a functional annotation, and so how large is the overestimate?
- **Data:** a set of genes with known functions, masked and then annotated by Bakta. **Method:** measure the false-negative rate of hypothetical calls. **Question:** how often does Bakta call a gene of known function hypothetical?
- **Data:** the prioritized dark genes together with their Bakta calls. **Method:** compare annotation status with the experimental evidence used for prioritization. **Question:** does Bakta agreement validate the prioritization, or does it reflect shared database gaps?
- **Data:** dark genes grouped by organism lineage. **Method:** stratify the false-negative and unchecked-database corrections by lineage. **Question:** is the overestimate uniform, or does it differ in lineages that are underrepresented in annotation databases?
