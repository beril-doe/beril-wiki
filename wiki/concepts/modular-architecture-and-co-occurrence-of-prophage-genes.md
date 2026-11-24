---
type: "Concept"
description: "Whether prophage functional modules (packaging, lysis, lysogenic regulation, integration, anti-defense) co-occur and co-localize on contigs as linked units, and which modules behave as accessory; limited to within-species co-occurrence tests."
sources: ["summaries/prophage_ecology__REPORT.md"]
---
# Modular architecture and co-occurrence of prophage genes

Within-species co-occurrence tests in one report (prophage_ecology, notebook NB03) suggest that packaging, lysis and lysogenic regulation genes behave as physically linked units. Integration and anti-defense genes do not. The evidence comes from one species per phylum, so it is broad but thin within each phylum. [src: prophage_ecology] For the full report see [[summaries/prophage_ecology__REPORT]].

## Core backbone modules co-occur and co-localize

The report describes the NB03 results as the first large-scale empirical validation of the modular theory of phage evolution (Hendrix et al. 2000) at the pangenome level. [src: prophage_ecology] It reads strong co-occurrence and contig co-localization of packaging (A), lysis (D) and lysogenic regulation (F) genes as showing that these functions are physically linked in prophage elements, not independently distributed annotations. [src: prophage_ecology]

The test used 15 phylogenetically stratified species, one per phylum, with at most 300 genomes each and 200 null permutations. Of 95 module-species tests, 44 (46.3%) showed significantly higher within-module gene co-occurrence than chance (z > 1.96, one-tailed). [src: prophage_ecology] Mean contig co-localization across all tests was 0.769. [src: prophage_ecology]

| Module | Significant species tests | Mean Z | Mean contig co-localization | Report's reading |
|---|---|---|---|---|
| A. Packaging | 11/15 | 3.40 | 0.986 | Strong co-occurrence; genes cluster on same contig [src: prophage_ecology] |
| B. Head morphogenesis | 1/6 | -0.44 | 0.474 | Weak; sparse across species [src: prophage_ecology] |
| C. Tail | 5/12 | 1.43 | 0.752 | Moderate co-occurrence [src: prophage_ecology] |
| D. Lysis | 13/15 | 4.45 | 0.901 | Strongest co-occurrence of any module [src: prophage_ecology] |
| E. Integration | 1/15 | -1.93 | 0.420 | Not co-occurring, expected for integrases [src: prophage_ecology] |
| F. Lysogenic regulation | 10/15 | 2.16 | 1.000 | Significant; perfect contig co-localization [src: prophage_ecology] |
| G. Anti-defense | 3/11 | 1.50 | 0.281 | Weak co-occurrence; scattered genomic placement [src: prophage_ecology] |

## Accessory modules behave differently

Integration (E) and anti-defense (G) genes behave differently from the core modules. [src: prophage_ecology] The report therefore supports a two-tier model: a core backbone of packaging, lysis and lysogenic regulation, plus genomically independent integration and anti-defense functions, across 15 phyla. [src: prophage_ecology]

The report calls the lack of integration co-occurrence biologically expected. It says integrases sit at different genomic insertion sites and many are domesticated remnants. [src: prophage_ecology] It cites Bobay et al. (2014), who showed that domesticated prophage remnants are more common than intact prophages and often keep only integrases. [src: prophage_ecology] See [[concepts/annotation-based-prophage-detection-prevalence-and-domesticated-remnants]].

The low anti-defense co-localization (0.281) fits the known clustering of anti-defense and defense systems into "defense islands" apart from the core prophage (Pinilla-Redondo et al. 2020; Rahimian et al. 2026). [src: prophage_ecology] See [[concepts/prophage-anti-defense-genes-and-host-phage-arms-races]].

Head morphogenesis (B) and tail (C) are intermediate or weak. The report's proposed split places them with the accessory functions. [src: prophage_ecology]

## Caveats

- NB03 tested one species per phylum, giving broad phylogenetic coverage but limited within-phylum replication. [src: prophage_ecology]
- Head morphogenesis (B) was testable in only 6 species because of sparsity. [src: prophage_ecology]
- Module definitions are validated for the core backbone (A, D, F) but less so for the accessory functions (E, G). [src: prophage_ecology]

## Open Directions

- Test several species within a few well-sampled phyla. This would show whether the one-species-per-phylum pattern holds within phyla. [src: prophage_ecology]
- Run the proposed split analysis: core backbone (A, D, F) against accessory functions (B, C, E, G). [src: prophage_ecology]
- Validate the E and G module definitions, for example with curated integrase and anti-defense gene sets. This would show whether their weak co-occurrence reflects biology or definition. [src: prophage_ecology]
- Pool sparse head morphogenesis (B) data across more genomes to test whether its weak signal is due to sparsity. [src: prophage_ecology]
