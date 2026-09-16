<!-- tension-hash: f75b7c122e13ebb4 -->
# Shared-Coordinate Filtering: Removing Institutional Artefacts vs. Keeping Intensively Sampled Field Sites

The disagreement is about whether dense clusters of genomes that share coordinates should be filtered out of geographic analyses. A shared-coordinate heuristic is meant to flag institutional addresses, yet the flagged clusters include legitimate, intensively sampled field sites. [src: env_embedding_explorer, discoveries] Keeping every dense cluster also keeps likely institutional or approximate locations. [src: env_embedding_explorer] The choice matters for [[concepts/spatial-sampling-effort-confounding]], where uneven sampling effort already threatens geographic hotspot inferences.

## Evidence Sides

**Side 1: Dense clusters include legitimate field sites, so filtering on density risks discarding them.**
The shared-coordinate heuristic is meant to flag institutional addresses. Yet the flagged clusters include legitimate, intensively sampled field sites such as Rifle, CO and Saanich Inlet. [src: env_embedding_explorer, discoveries] A filter that treats high genome density as an artefact therefore risks discarding sites where sampling effort is high by design. [src: env_embedding_explorer, discoveries] On this side, high density is potentially informative rather than diagnostic of error.

**Side 2: Dense clusters also include likely institutional or approximate locations, so keeping them all risks retaining such placements.**
Keeping every dense cluster also keeps likely institutional or approximate locations, such as Pittsburgh and Lima. [src: env_embedding_explorer] On this side, at least some high-density coordinates likely do not mark true sampling sites, so retaining them could let such coordinates stand in for real sampling locations. [src: env_embedding_explorer]

Neither side's evidence establishes how many flagged clusters belong to each category. The TENSION text reports examples, not a classification rate.

## Possible Reconciliations

- *Hypothesis:* Genome density alone cannot separate the two kinds of cluster. A second signal, such as the environment label or the metadata for the originating study, may distinguish a field campaign from an institutional address.
- *Hypothesis:* Field-site clusters and institutional clusters differ in their within-cluster environmental composition. Field sites may be dominated by one environment type, while institutional addresses may mix unrelated sources.
- *Hypothesis:* A curated allow-list of known long-term field sites, applied before the density filter, would keep sites like Rifle, CO and Saanich Inlet without also keeping locations like Pittsburgh and Lima. This depends on such a list being reasonably complete.

## Resolving Work

- **Data:** genome metadata for every cluster flagged by the shared-coordinate heuristic. **Method:** manually annotate each cluster as field site, institutional address or approximate location. **Question:** what fraction of flagged clusters falls into each class?
- **Data:** environment labels within each flagged cluster. **Method:** compare label diversity between annotated field-site and institutional clusters. **Question:** does environmental homogeneity separate the two classes?
- **Data:** study and BioProject identifiers attached to clustered genomes. **Method:** test whether a cluster traces to one sampling campaign or to many unrelated submissions. **Question:** does study provenance predict which clusters are artefacts?
- **Data:** geographic analyses run with and without the filter. **Method:** rerun the analyses three ways: unfiltered, filtered, and filtered with a field-site allow-list. **Question:** do the conclusions change depending on which dense clusters are kept?
