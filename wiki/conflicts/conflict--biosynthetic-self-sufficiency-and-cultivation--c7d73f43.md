<!-- tension-hash: c7d73f4374576e32 -->
# Is *Candidatus* (*Ca.*) Desulforudis audaxviator-style self-sufficiency in the Bacillota_B deep-anchor cohort or absent from the cultured cohort?

Two projects disagree on whether *Ca.* Desulforudis audaxviator, the lineage that exemplifies extreme biosynthetic self-sufficiency in the deep subsurface, belongs to the genome cohorts they analysed. The Bacillota_B report lists one of this organism's genomes in its anchor cohort and reads deep-clay gene-content expansion as consistent with self-sufficiency. [src: bacillota_b_subsurface_accessory] The clay report states that its cultured cohort does not include such extreme self-sufficient lineages. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface] The disagreement bears on how far cultured-genome results represent self-sufficient lineages, the question of [[concepts/biosynthetic-self-sufficiency-and-cultivation]]. The corpus does not currently settle it.

## Evidence Sides

**Side A: the self-sufficient lineage is in the anchor cohort, and the expansion is read as consistent with self-sufficiency**

- The Bacillota_B report finds gene-content expansion, opposite in direction to the "small is mighty" streamlining finding of Tian et al. (2020). [src: bacillota_b_subsurface_accessory]
- The report limits Tian's claim to the Patescibacteria/CPR (Candidate Phyla Radiation) superphylum, with ≤1 Mbp (million base pairs) genomes and an episymbiotic lifestyle (living attached to a host's surface). Bacillota_B are anaerobic Firmicutes that grow free-living rather than as episymbionts. [src: bacillota_b_subsurface_accessory]
- The report reads the expansion as consistent with the Beaver & Neufeld (2024) self-sufficiency hypothesis. [src: bacillota_b_subsurface_accessory]
- It lists *Ca.* Desulforudis audaxviator genome `GB_GCA_020725505.1` in its anchor cohort; Becraft et al. (2021) showed this genome retains full nitrogen fixation, amino-acid biosynthesis and carbon fixation, with no streamlining. [src: bacillota_b_subsurface_accessory]

**Side B: the cultured cohort lacks the extreme self-sufficient lineages**

- The clay report states that the cultured cohort does not include the extreme self-sufficient lineages that *Ca.* Desulforudis audaxviator exemplifies. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface]

**Cohort definitions differ**

- The two reports define their deep anchor cohorts differently: 10 deep-clay Bacillota_B genomes versus 9 unfiltered deep anchors. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface]
- The Bacillota_B cohort also includes metagenomic genomes and rock-porewater MAGs (metagenome-assembled genomes, which are reconstructed from environmental sequence rather than from isolates). [src: bacillota_b_subsurface_accessory, clay_confined_subsurface]
- The corpus does not establish how `GB_GCA_020725505.1` was recovered. It also does not report how this genome scored on GapMind, a tool that predicts whether biosynthetic pathways are complete. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface]

## Possible Reconciliations

- **Hypothesis 1: the cohorts differ in composition.** The Bacillota_B anchor cohort also includes metagenomic genomes and rock-porewater MAGs, while the clay report's statement concerns a cultured cohort. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface] On this reading, both statements could hold for their own cohorts.
- **Hypothesis 2: cohort membership differs.** The genome may fall inside one anchor definition and outside the other, for example if one cohort is filtered by habitat or recovery method and the other is not.
- **Hypothesis 3: the expansion has another source.** The expansion may come from lineages other than *Ca.* Desulforudis audaxviator, making the Becraft et al. (2021) citation supporting context rather than evidence drawn from the cohort.

## Resolving Work

- **Recovery method:** Retrieve assembly metadata for `GB_GCA_020725505.1` in the KBase Data Lakehouse and classify it as isolate, MAG or single-cell genome, to show whether it can belong to a cultured cohort.
- **Cohort overlap:** Compare the 10 deep-clay Bacillota_B genomes against the 9 unfiltered deep anchors by set overlap, to show which genomes sit in both cohorts.
- **GapMind scoring:** Score `GB_GCA_020725505.1` with GapMind alongside the clay cohort, to show whether it appears self-sufficient under the clay report's pathway criteria.
- **Expansion in verified isolates:** Recompute the Bacillota_B gene-content expansion restricted to genomes with verified isolate provenance, to show whether the expansion holds within cultured genomes.
