---
type: "Organism"
description: "Alistipes onderdonkii, a gut commensal bacterium that is one of the two species with the most inferred metabolic ecotypes in the corpus's pathway-profile clustering."
sources: ["summaries/discoveries.md", "summaries/pathway_capability_dependency__REPORT.md"]
---
# Alistipes onderdonkii

*Alistipes onderdonkii* is a gut commensal bacterium that the corpus describes as having substantial intraspecific metabolic diversity [src: pathway_capability_dependency]. The assigned evidence records no external identifier, such as an NCBI taxid.

## Metabolic ecotypes

The pathway capability and dependency analysis grouped binary GapMind pathway profiles by hierarchical clustering with Jaccard distance. It covered 225 species that had sufficient genome diversity, meaning 50+ genomes and 3+ variable pathways. In that analysis, *A. onderdonkii* (8 ecotypes) and *Barnesiella intestinihominis* (8 ecotypes) were the species with the most inferred metabolic ecotypes. Both are gut commensals with substantial intraspecific metabolic diversity [src: pathway_capability_dependency].

The central discoveries digest repeats this pathway_capability_dependency finding rather than corroborating it independently. Its entry lists *Alistipes onderdonkii* (8) and *Barnesiella intestinihominis* (8) as the top ecotyped species [src: discoveries].

Caveat: the ecotype count of 8 is a clustering inference, not a set of directly observed populations. The source calls its hierarchical clustering with a fixed 50% distance threshold a simplification and states that different distance thresholds would yield different ecotype counts. It also says the median of 4 ecotypes per species should be read as an order-of-magnitude estimate. The figure of 8 for *A. onderdonkii* therefore depends on the threshold that was chosen. For broader discussion, see [[concepts/ecotype-clustering-validity]] [src: pathway_capability_dependency].

## Related

- [[entities/barnesiella-intestinihominis]]: the other gut commensal with 8 inferred ecotypes [src: pathway_capability_dependency]
- [[summaries/pathway_capability_dependency__REPORT]]
- [[summaries/discoveries]]
- [[concepts/ecotype-environment-gene-content]]
