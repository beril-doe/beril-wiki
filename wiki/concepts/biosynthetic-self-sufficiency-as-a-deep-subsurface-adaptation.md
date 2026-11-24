---
type: "Concept"
description: "Whether deep-subsurface bacteria show higher amino-acid biosynthetic pathway completeness (self-sufficiency), as measured in cultured genomes; includes ceiling and quality-filter caveats and stops at the cultured clay cohort."
sources: ["summaries/bacillota_b_subsurface_accessory__REPORT.md", "summaries/clay_confined_subsurface__REPORT.md", "summaries/discoveries.md"]
---
# Biosynthetic self-sufficiency as a deep-subsurface adaptation

Deep-subsurface bacteria are proposed to be biosynthetically self-sufficient, but cultured genomes in the KBase Data Lakehouse do not show it. Deep-clay genomes have no higher GapMind amino-acid pathway completeness than soil baseline, and after quality filtering they have lower completeness. [src: clay_confined_subsurface] The test is limited by a very small deep cohort and a ceiling in the metric, so the result applies only to the cultured clay cohort. [src: clay_confined_subsurface]

## The hypothesis

Beaver & Neufeld (2024) is described as proposing biosynthetic self-sufficiency as the canonical deep-subsurface adaptation, exemplified by Ca. Desulforudis audaxviator (Becraft 2021). [src: clay_confined_subsurface] Becraft's genome is described as containing all genes necessary for carbon and nitrogen fixation and all necessary amino acid biosynthesis pathways. [src: bacillota_b_subsurface_accessory] See [[entities/candidatus-desulforudis-audaxviator]].

## Evidence from cultured clay genomes

Completeness was scored as the number of 18 GapMind amino-acid pathways present (see [[entities/gapmind]]), compared with a two-sided Mann–Whitney U test and Cohen's d. [src: clay_confined_subsurface] Deep-clay genomes were not above soil baseline when unfiltered: means 16.22 versus 16.66, n=9 versus 150, d=−0.17, p=0.153. [src: clay_confined_subsurface] With CheckM filtering (≥80% completeness, ≤5% contamination), deep-clay completeness was lower: 15.50 versus 17.14, n=6 versus 137, d=−0.84, p=0.009. [src: clay_confined_subsurface] Within Bacillota_B, deep-clay genomes were not significantly higher: 16.50 versus 16.79, n=4 versus 19, d=−0.13, p=0.073. [src: clay_confined_subsurface]

The shallow-clay cohort went the other way. It scored 17.87 versus 16.66 unfiltered (n=30 versus 150, d=+0.52, p=0.006) and 17.87 versus 17.14 with CheckM≥80 (n=30 versus 137, d=+0.43, p=0.029). [src: clay_confined_subsurface]

## Related genome-content signal

Pathway completeness and genome content differ. In Bacillota_B, deep-clay genomes encode about 25% more orthogroups than soil congeners, which the report reads as consistent with self-sufficiency. [src: bacillota_b_subsurface_accessory] The orthogroup counts are 2,771 versus 2,233 (d=+1.32, p=0.009). [src: discoveries] The report treats this as consistent with Beaver & Neufeld and with Becraft's genome, which retains full N-fixation, amino-acid biosynthesis and C-fixation without streamlining. [src: bacillota_b_subsurface_accessory] This is a reading of orthogroup counts, not a direct measure of amino-acid pathways. See [[entities/bacillota-b]] and [[concepts/genome-streamlining-and-genome-size-in-ecological-specialists]].

## Caveats

- The deep cohort has n=9 genomes, so only large effects (Cohen's d > 0.7) are reliably detectable in unfiltered comparisons. [src: clay_confined_subsurface] Marginal p-values, such as the within-Bacillota_B p=0.07, are descriptive. [src: clay_confined_subsurface]
- The 18-pathway universe saturates near 18 for most cultivable bacteria, which limits resolution at the upper end. [src: clay_confined_subsurface] Most cultured organisms, deep or shallow, reach 17–18/18, leaving little room for a positive signal. [src: clay_confined_subsurface] See [[concepts/reliability-and-coverage-limits-of-gapmind-pathway-predictions]].
- The report reads its negative result as absence of extreme self-sufficient lineages from the cultured cohort. Such lineages are characteristically uncultivated MAGs (metagenome assembled genomes) or single-cell genomes. [src: clay_confined_subsurface] It states that the archetype holds for uncultivated lineages but does not propagate to the cultivable cohort. [src: clay_confined_subsurface] See [[concepts/cultivation-bias-in-genome-collections-versus-uncultivated-lineages]].

## Tensions

- The orthogroup expansion in deep-clay Bacillota_B is read as consistent with self-sufficiency. [src: bacillota_b_subsurface_accessory] GapMind pathway completeness in the within-Bacillota_B comparison shows no significant gain. [src: clay_confined_subsurface]
- The negative result agrees with critiques of universal subsurface streamlining or self-sufficiency. Props et al. 2019 is cited as documenting expansion and positive selection in oligotrophic engineered cooling water. Cortez et al. 2022 is cited as showing streamlining is acidophile-specific. [src: clay_confined_subsurface] Streamlining in Patescibacteria/CPR (candidate phyla radiation) is reported not to generalize to cultivable subsurface Firmicutes. [src: discoveries] It is read as a CPR-specific adaptation to episymbiotic life, with cultivable Firmicutes showing the opposite pattern. [src: discoveries]

## Proposed next steps in the report

The report proposes a finer-grained sensitivity check: presence of all standard amino-acid biosynthesis EC (Enzyme Commission) numbers in eggNOG. [src: clay_confined_subsurface] It also proposes ingesting deep-subsurface MAGs from Mont Terri, Olkiluoto, MX-80 bentonite and Oak Ridge, to test whether self-sufficiency emerges with rock-attached and uncultivated lineages. [src: clay_confined_subsurface]

## Open Directions

- Ingest the deep-subsurface MAGs named above and re-run the comparisons. This would test whether the signal emerges once uncultivated lineages are present.
- Add the EC-number metric from eggNOG to get past the GapMind ceiling.
- Enlarge the CheckM-passing deep cohort (currently 6 genomes) so that moderate effects become detectable.
