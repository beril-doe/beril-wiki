---
type: "Gene_Or_Pathway"
description: "pcaC (locus ACIAD1710) encodes 4-carboxymuconolactone decarboxylase (EC 4.1.1.44), a core protocatechuate (pca) pathway enzyme that a keyword annotation pass misclassified and co-fitness analysis recovered."
sources: ["summaries/aromatic_catabolism_network__REPORT.md", "summaries/pitfalls.md"]
---
pcaC encodes 4-carboxymuconolactone decarboxylase (EC 4.1.1.44), a core enzyme of the protocatechuate (pca) branch of aromatic catabolism. The pitfalls digest records it under the locus tag ACIAD1710, which is the gene it reports as recovered as pcaC. Known aliases: ACIAD1710; 4-carboxymuconolactone decarboxylase. [src: pitfalls]

## Keyword misclassification

A classifier that sorted genes by keyword matching on [[entities/rast]] function descriptions misclassified ACIAD1710 (4-carboxymuconolactone decarboxylase, EC 4.1.1.44). The gene is a core pca pathway enzyme, but the classifier labelled it "Other" because its keyword list checked for "muconate" and not "muconolactone". [src: pitfalls]

## Recovery by co-fitness

Co-fitness analysis put pcaC back in the aromatic pathway despite the keyword error. Its co-fitness correlation with the Aromatic pathway was r=0.978. This rests on a single gene's correlation in one project, not on a systematic benchmark of the method. [src: pitfalls]

The aromatic catabolism project reports the same result. Its co-fitness method recovered pcaC (4-carboxymuconolactone decarboxylase), which keyword matching had initially miscategorized. The same method also identified two DUF (domain of unknown function) proteins as probable [[entities/complex-i]] accessory factors. That Complex I assignment comes from co-fitness and is a proposal, not a biochemical confirmation. The project lists an important limitation: its co-fitness analysis uses only 8 conditions (8-dimensional growth vectors), which limits how finely it can resolve gene-gene correlations. The pcaC recovery and the DUF assignments should be read with that limit in mind. [src: aromatic_catabolism_network]

## Lesson for annotation practice

The recommended practice is to treat keyword-based categorization as an initial pass and then check it against co-fitness correlations. A keyword classifier for gene functions should also be tested against known members of each category, with missing synonyms added. pcaC is the worked example of why. [src: pitfalls]

## Related

- [[entities/beta-ketoadipate-pathway]]
- [[entities/protocatechuate]]
- [[concepts/evidence-triangulation-for-functional-annotation]]
- [[concepts/cofitness-network-architecture]]
- [[summaries/aromatic_catabolism_network__REPORT]]
- [[summaries/pitfalls]]
