<!-- tension-hash: 9d0916a3d5714ed2 -->
# Are Literature-Free Protein Families Unstudied, or Missed by Retrieval?

A recurring claim in the [[concepts/research-attention-inequality]] page is that some protein families have never been studied. The disagreement is over what "zero literature" means. One reading treats literature-free families as true gaps in biological knowledge. The other treats them, at least in part, as artefacts: of the reference resource consulted, or of text-mining retrieval failing to find papers that exist. This matters because "dark" families and genes are used to prioritize targets for characterization. If darkness labels are partly artefacts, such priorities could be misdirected.

## Evidence Sides

**Side 1: Literature-free families are genuinely unstudied**

The PaperBLAST report describes the 5,218 literature-free multi-member families as genuinely unstudied. [src: paperblast_explorer] PaperBLAST is a resource that links protein sequences to papers mentioning them, using text mining (automated extraction of gene or protein mentions from publications). The same report also states that, without negative controls, it cannot easily distinguish genuinely unstudied genes from genes whose literature was missed by text mining. [src: paperblast_explorer] So this side's own source records the caveat that its framing cannot easily be separated from retrieval misses without such controls. [src: paperblast_explorer]

**Side 2: Zero-literature and "dark" labels can reflect the resource consulted or retrieval failure**

In a different dataset, Bakta reclassification of 33,105 of 39,532 linked dark genes (83.7%) shows how strongly darkness labels can depend on the reference resource consulted. Bakta is a bacterial genome annotation pipeline. In addition, the ~80% PaperBLAST false-negative rate for *Caulobacter* lipid A genes shows that zero-literature calls can be retrieval failures. A false-negative rate is the share of genes that have literature but are scored as having none. [src: functional_dark_matter, truly_dark_genes, caulobacter_fur_lipida_loss]

This evidence does not directly re-test the PaperBLAST families: the Bakta result concerns annotation-based darkness of genes in a different dataset, and the false-negative rate concerns *Caulobacter* lipid A genes. [src: functional_dark_matter, truly_dark_genes, caulobacter_fur_lipida_loss] Applying either to the PaperBLAST families is an extrapolation.

## Possible Reconciliations

- **Hypothesis A:** Both sides hold for different categories. Some literature-free families are truly unstudied, while others are retrieval or annotation artefacts, and their proportion is unknown.
- **Hypothesis B:** The *Caulobacter* false-negative rate reflects gene-naming conventions specific to lipid A genes. If so, it would not generalize to the PaperBLAST dark families.
- **Hypothesis C:** "Dark" as defined by literature absence and "dark" as defined by annotation absence are distinct properties. In that case, the Bakta result bears on annotation lag rather than on literature coverage.

## Resolving Work

- **Measure the PaperBLAST miss rate.** Data: a curated set of genes with known publications spread across many organisms. Method: run PaperBLAST retrieval on this negative-control set. Question: is the PaperBLAST false-negative rate near the *Caulobacter* figure, or specific to that gene set?
- **Annotate the dark families.** Data: the PaperBLAST dark families. Method: cross-reference them against Bakta and other current annotation resources. Question: do literature-free families also lack annotation, or is literature absence decoupled from annotation absence?
- **Search for missed literature.** Data: a random sample of literature-free families. Method: manual or full-text literature search by alternative gene names and locus tags. Question: what fraction of these families have published work that text mining missed?
- **Stratify dark families by type.** Data: dark families grouped by source collection and functional class. Method: compare retrieval failure rates across the groups. Question: are retrieval artefacts concentrated in particular kinds of families?
