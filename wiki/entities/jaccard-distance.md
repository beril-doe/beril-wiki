---
type: Method
description: A method for measuring gene-content dissimilarity between genomes
sources:
- id: ecotype_env_reanalysis
  resource: ../summaries/ecotype_env_reanalysis__REPORT.md
  title: ecotype env reanalysis
title: Jaccard distance
---
# Jaccard distance

## What this entity is

**Canonical name:** Jaccard distance. [^ecotype_env_reanalysis]

**Known aliases:** Jaccard dissimilarity; no other alias or stable external identifier is specified in this document. [^ecotype_env_reanalysis]

Jaccard distance is a set-based method used here to quantify whole-genome gene-content differences for comparison with environmental and host-association classifications. [^ecotype_env_reanalysis]

## Key facts from the document

The reanalysis used whole-genome Jaccard distances together with AlphaEarth embedding distances and genome-level environmental classifications to test whether environmental context predicts bacterial gene-content variation. [^ecotype_env_reanalysis]

The environmental-versus-human-associated comparison found no stronger gene-content correlation for environmental species: environmental species had a median partial correlation of 0.051, while human-associated species had a median of 0.084. [^ecotype_env_reanalysis]

The one-sided Mann–Whitney U test for Environmental > Human-associated gave U=1536 and p=0.83, so the null hypothesis was not rejected. [^ecotype_env_reanalysis]

The reanalysis reported a median partial correlation of 0.081 across all 183 species, compared with 0.003 in the original analysis; the report characterizes this as a 27x difference. [^ecotype_env_reanalysis]

The original and reanalysis correlation values are not directly comparable because the analyses used different genome sets and sampling procedures, including diversity-maximizing downsampling to a maximum of 250 genomes in the original analysis versus use of all genomes with embeddings in the reanalysis. [^ecotype_env_reanalysis]

The report identifies a specific downsampled-versus-full-genome extraction comparison as necessary to explain the 27x partial-correlation discrepancy. [^ecotype_env_reanalysis]

Testing functional gene subsets, including transport and secondary-metabolism categories, was proposed as a way to determine whether whole-genome Jaccard distances mask more specific environmental effects. [^ecotype_env_reanalysis]

## Related pages

- [ecotype_env_reanalysis__REPORT](../summaries/ecotype_env_reanalysis__REPORT.md) — source-document summary containing the Jaccard-distance analysis. [^ecotype_env_reanalysis]
- [ecotype-environment-gene-content](../concepts/ecotype-environment-gene-content.md) — concept covering the null relationship between environment classification and bacterial gene-content variation. [^ecotype_env_reanalysis]
- [pangenome-integration](../concepts/pangenome-integration.md) — concept covering integration of gene-cluster memberships and environmental metadata. [^ecotype_env_reanalysis]
- [average-nucleotide-identity](average-nucleotide-identity.md) — related genome-distance method used alongside Jaccard distances. [^ecotype_env_reanalysis]
- [alph-aearth](alph-aearth.md) — embedding source used with gene-content distances in the reanalysis. [^ecotype_env_reanalysis]

[^ecotype_env_reanalysis]: [ecotype env reanalysis](../summaries/ecotype_env_reanalysis__REPORT.md)
