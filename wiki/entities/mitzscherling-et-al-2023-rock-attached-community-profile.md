---
type: "Dataset"
description: "Published rock-attached Opalinus Clay community profile (SRB <0.2%, IRB 4.3–10.2%, Geobacter and Geothrix dominated) used as a null for cultivation-bias tests."
sources: ["summaries/clay_confined_subsurface__REPORT.md", "summaries/discoveries.md"]
aliases: ["Mitzscherling 2023"]
---
# Mitzscherling et al. 2023 rock-attached community profile

The clay_confined_subsurface report used this profile as a null distribution for its cultivation-bias tests. [src: clay_confined_subsurface, discoveries]

## Key facts

- The profile is SRB <0.2% and IRB 4.3–10.2% of the community, dominated by *Geobacter* and *Geothrix*. [src: clay_confined_subsurface]
- The report reduced the profile to a null of SR (sulfate reduction) ~0.2% and IR (iron reduction) ~7% for its H3 tests. [src: clay_confined_subsurface]
- The discoveries digest describes the same clay site as having two paradigms. The Bagnoud (2016) porewater paradigm is dominated by sulfate reducers. The Mitzscherling (2023) rock-attached paradigm is dominated by Geobacter/Geothrix iron reducers. [src: discoveries] See [[entities/bagnoud-et-al-2016-opalinus-porewater-food-web]].

## Use as a null in the cultivation-bias diagnostic

The diagnostic computes SR-marker (dsrAB-aprAB-sat) and IR-marker (omcS / mtrC / mtrA) prevalences in cultured clay-isolated genomes. It compares them with the Mitzscherling frequencies (SRB ~0.2%, IRB ~7%) by binomial test. [src: discoveries] See [[entities/cultivation-bias-diagnostic]] and [[concepts/cultivation-bias-toward-porewater-versus-rock-attached-subsurface-communities]].

- **SR enrichment:** Against this null, SR enrichment is reported as overwhelming. The binomial p is 4.0×10⁻¹², with 5 observed versus 0.018 expected of 9. [src: clay_confined_subsurface]
- **IR depletion:** This test was not significant. The numbers were n=9, observed=1, expected=0.63 and p=0.87. [src: clay_confined_subsurface]

## Interpretation and correction

The report reads its H3 result as directly diverging from the Mitzscherling profile. Because the Data Lakehouse has no genomes from rock-attached MAGs (metagenome assembled genomes) at Mont Terri, the report calls the divergence mechanistic. It says the divergence shows what cultivation-accessible cohorts miss. [src: clay_confined_subsurface]

The discoveries digest corrects one part of this. The clay project's interpretation of a "Mitzscherling rock-attached IR-rich pattern in shallow clay" was an artefact. The SR-side H3 finding (p=4×10⁻¹² against the Mitzscherling rock-attached null) remains intact. [src: discoveries] See [[concepts/iron-and-sulfate-reduction-signatures-in-clay-subsurface-porewater-versus-rock-attached-communities]] and [[summaries/clay_confined_subsurface__REPORT]].
