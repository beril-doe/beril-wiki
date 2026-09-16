<!-- tension-hash: 0f75deea0809f532 -->
# Does genome expansion in deep subsurface Bacillota_B indicate biosynthetic self-sufficiency?

Two lines of evidence point in different directions. In subsurface Bacillota_B, genome size and orthologous group (OG, a cluster of genes inferred to share a common ancestral function) content are consistent with a self-sufficiency model. A GapMind comparison, however, finds no elevated amino-acid pathway completeness in the deep cohort, and it finds lower completeness after quality filtering [src: bacillota_b_subsurface_accessory, clay_confined_subsurface]. The disagreement matters for [[concepts/biosynthetic-self-sufficiency-and-cultivation]], which asks whether cultured-genome collections miss the most biosynthetically self-sufficient community members. The two measurements address different aspects of genomic and metabolic capacity, so neither establishes self-sufficiency on its own [src: bacillota_b_subsurface_accessory, clay_confined_subsurface].

## Evidence Sides

**Side A: genome expansion is consistent with self-sufficiency**

- The deep cohort mixes isolates with metagenomic genomes and MAGs (metagenome-assembled genomes, which are genomes reconstructed computationally from community sequencing rather than from a cultured isolate). In this cohort, subsurface Bacillota_B have larger genome size and more OG content [src: bacillota_b_subsurface_accessory, clay_confined_subsurface].
- This pattern is described as *consistent with* a self-sufficiency model. It is not described as a demonstration of one [src: bacillota_b_subsurface_accessory, clay_confined_subsurface].

**Side B: pathway completeness is not elevated**

- The GapMind comparison finds no elevated amino-acid pathway completeness in the deep cohort. GapMind is a tool that predicts whether amino-acid biosynthesis pathways are complete in a genome [src: bacillota_b_subsurface_accessory, clay_confined_subsurface].
- After quality filtering, the same comparison finds *lower* completeness in the deep cohort [src: bacillota_b_subsurface_accessory, clay_confined_subsurface].

The source wiki states that these findings should not be reconciled by treating genome expansion as proof of biosynthetic self-sufficiency, because they measure different aspects of genomic and metabolic capacity [src: bacillota_b_subsurface_accessory, clay_confined_subsurface].

## Possible Reconciliations

- **Hypothesis 1: different capacities.** The expanded gene content may encode functions other than amino-acid biosynthesis, such as accessory or environmental-response genes. In that case, both observations could hold at once, with no contradiction about biosynthesis itself.
- **Hypothesis 2: genome-quality artefact.** Incomplete MAGs and metagenomic genomes in the mixed deep cohort could depress measured pathway completeness. This would make the lower post-filtering completeness partly a property of genome quality rather than biology. The same artefact could also bias the size and OG comparison in either direction.
- **Hypothesis 3: self-sufficiency via other routes.** Self-sufficiency, if present, may lie in pathways or cofactors that the amino-acid GapMind comparison does not assess.

None of these hypotheses is supported over the others by the current evidence.

## Resolving Work

- Restrict both comparisons to high-completeness, low-contamination genomes, and then to isolates alone, using the same deep and comparison cohorts. The question is whether the genome-size/OG difference and the GapMind deficit persist once MAG quality is controlled.
- Annotate the OGs that drive the expansion signal, and test whether any fall in amino-acid or cofactor biosynthesis pathways. The question is whether genome expansion maps onto biosynthetic functions at all.
- Extend GapMind-style completeness scoring beyond amino acids to vitamin and cofactor pathways, and compare the deep and comparison cohorts. The question is whether self-sufficiency appears in pathway classes not yet measured.
- Regress pathway completeness on genome size within the cohort, using a phylogenetic correction (a statistical adjustment for shared evolutionary ancestry among genomes). The question is whether larger genomes predict more complete biosynthesis, independent of lineage.
