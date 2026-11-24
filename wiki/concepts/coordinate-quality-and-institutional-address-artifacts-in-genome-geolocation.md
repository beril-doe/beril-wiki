---
type: "Concept"
description: "Detecting genome coordinates that reflect institutional addresses or approximate precision rather than true sampling sites, and the limits of heuristics; stops at downstream use of coordinates."
sources: ["summaries/discoveries.md", "summaries/ecotype_analysis__REPORT.md", "summaries/env_embedding_explorer__REPORT.md", "summaries/pitfalls.md"]
---
# Coordinate quality and institutional-address artifacts in genome geolocation

Detecting genome coordinates that reflect institutional addresses or approximate precision rather than true sampling sites, and the limits of heuristics; stops at downstream use of coordinates.

## The AlphaEarth screen

The dataset has 11,765 unique coordinate locations across 83,286 genomes with latitude/longitude. [src: env_embedding_explorer] The heuristic flags coordinates holding more than 50 genomes from more than 10 species as possible institutional addresses. [src: env_embedding_explorer] By this rule, 30,469 genomes (36.6%) fall in such clusters. [src: discoveries] The assessment sorts genomes into three classes:

| Class | Genomes | Share |
|---|---|---|
| Good | 50,109 [src: env_embedding_explorer] | 60.2% [src: env_embedding_explorer] |
| Suspicious cluster | 30,469 [src: env_embedding_explorer] | 36.6% [src: env_embedding_explorer] |
| Low precision (integer degrees) | 2,708 [src: env_embedding_explorer] | 3.3% [src: env_embedding_explorer] |

Two flagged locations are given as likely problems, but the report only calls them "likely". Pittsburgh, PA (630 genomes) is considered likely institutional because its clinical sources are diverse. [src: env_embedding_explorer] Lima, Peru (1,641 genomes) has integer coordinates that are considered likely approximate. [src: env_embedding_explorer] Neither claim establishes that the location is not a real sampling site; Lima's coordinates are described only as imprecise. [src: env_embedding_explorer]

## Where the heuristic fails

Several flagged locations are legitimate field research sites. [src: env_embedding_explorer] Rifle, CO has 1,883 genomes and is a DOE IFRC groundwater research site (see [[entities/rifle-ifrc-groundwater-research-site]]). [src: discoveries, env_embedding_explorer] Saanich Inlet, BC has 1,529 genomes and is an oceanographic O2-minimum zone (see [[entities/saanich-inlet]]). [src: discoveries, env_embedding_explorer] Siberian soda lakes have 812 genomes from extremophile sampling campaigns (see [[entities/siberian-soda-lakes]]). [src: discoveries, env_embedding_explorer] Genome and species counts alone therefore cannot separate a heavily sampled site from an institution. [src: env_embedding_explorer]

The report's proposed fix is to check isolation_source homogeneity at each location. Genomes at a real site should share a homogeneous isolation source. Genomes at an institution should show diverse, unrelated sources. [src: discoveries, env_embedding_explorer] This refinement is proposed, not tested. The report presents the framework as having known limitations. [src: env_embedding_explorer]

## Other coordinate-quality problems

Missing or imprecise NCBI coordinates reduce the quality of environmental associations in the ecotype analysis. [src: ecotype_analysis] For host-associated organisms, the coordinates reflect the collection site rather than the organism's microenvironment, so they carry less meaning. [src: ecotype_analysis] In gtdb_metadata, ncbi_lat_lon is most commonly NULL. [src: pitfalls] It also holds malformed strings such as "missing" or "not collected". [src: pitfalls] It also holds low-precision values such as "37.0 N 122.0 W". [src: pitfalls] These gaps add to the broader coverage problems discussed in [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]].

## Open Directions

- Compute isolation_source homogeneity (for example, the entropy of source terms) at each of the 11,765 locations. Then check whether it separates Rifle, Saanich Inlet and the Siberian soda lakes from Pittsburgh. This tests the proposed refinement.
- Compare AlphaEarth-based environment signals for the Good, Suspicious cluster and Low precision classes. This would show whether flagged coordinates distort downstream results, as in [[concepts/environmental-versus-phylogenetic-drivers-of-gene-content]].
- Quantify how often ncbi_lat_lon is NULL, malformed or low precision across gtdb_metadata. This would size the loss before coordinate-based analyses.
- Check integer-degree locations such as Lima against any finer-grained source metadata. This would show whether the coordinates are only approximate or actually wrong.
