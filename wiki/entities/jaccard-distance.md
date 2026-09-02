---
type: "Method"
description: "A method for measuring gene-content dissimilarity between genomes"
sources: ["summaries/ecotype_env_reanalysis__REPORT.md"]
---
# Jaccard distance

## What this entity is

**Canonical name:** Jaccard distance. [src: ecotype_env_reanalysis]

**Known aliases:** Jaccard dissimilarity; no other alias or stable external identifier is specified in this document. [src: ecotype_env_reanalysis]

Jaccard distance is a set-based method used here to quantify whole-genome gene-content differences for comparison with environmental and host-association classifications. [src: ecotype_env_reanalysis]

## Key facts from the document

The reanalysis used whole-genome Jaccard distances together with AlphaEarth embedding distances and genome-level environmental classifications to test whether environmental context predicts bacterial gene-content variation. [src: ecotype_env_reanalysis]

The environmental-versus-human-associated comparison found no stronger gene-content correlation for environmental species: environmental species had a median partial correlation of 0.051, while human-associated species had a median of 0.084. [src: ecotype_env_reanalysis]

The one-sided Mann–Whitney U test for Environmental > Human-associated gave U=1536 and p=0.83, so the null hypothesis was not rejected. [src: ecotype_env_reanalysis]

The reanalysis reported a median partial correlation of 0.081 across all 183 species, compared with 0.003 in the original analysis; the report characterizes this as a 27x difference. [src: ecotype_env_reanalysis]

The original and reanalysis correlation values are not directly comparable because the analyses used different genome sets and sampling procedures, including diversity-maximizing downsampling to a maximum of 250 genomes in the original analysis versus use of all genomes with embeddings in the reanalysis. [src: ecotype_env_reanalysis]

The report identifies a specific downsampled-versus-full-genome extraction comparison as necessary to explain the 27x partial-correlation discrepancy. [src: ecotype_env_reanalysis]

Testing functional gene subsets, including transport and secondary-metabolism categories, was proposed as a way to determine whether whole-genome Jaccard distances mask more specific environmental effects. [src: ecotype_env_reanalysis]

## Related pages

- [[summaries/ecotype_env_reanalysis__REPORT]] — source-document summary containing the Jaccard-distance analysis. [src: ecotype_env_reanalysis]
- [[concepts/ecotype-environment-gene-content]] — concept covering the null relationship between environment classification and bacterial gene-content variation. [src: ecotype_env_reanalysis]
- [[concepts/pangenome-integration]] — concept covering integration of gene-cluster memberships and environmental metadata. [src: ecotype_env_reanalysis]
- [[entities/average-nucleotide-identity]] — related genome-distance method used alongside Jaccard distances. [src: ecotype_env_reanalysis]
- [[entities/alph-aearth]] — embedding source used with gene-content distances in the reanalysis. [src: ecotype_env_reanalysis]
