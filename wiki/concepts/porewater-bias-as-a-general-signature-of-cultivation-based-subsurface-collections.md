---
type: "Concept"
description: "Whether cultured collections systematically favour motile, aerobic, high-energy-acceptor organisms from mobile porewater, and whether this holds across subsurface lithologies; stops at the specific KO-level results."
sources: ["summaries/clay_confined_subsurface__REPORT.md", "summaries/discoveries.md", "summaries/oak_ridge_cultivation_gap__REPORT.md"]
---
# Porewater bias as a general signature of cultivation-based subsurface collections

This page covers whether cultured genome collections systematically favour motile, aerobic organisms that use high-energy electron acceptors and come from mobile porewater, and whether that holds across subsurface lithologies. The evidence is a clay (Opalinus) cohort and an ENIGMA cultured-versus-MAG comparison (MAG = metagenome assembled genomes) in mixed groundwater/aquifer, and they agree. [src: oak_ridge_cultivation_gap] The generality claim is the reports' suggestion and rests on these two lithologies only. [src: oak_ridge_cultivation_gap]

## Evidence in clay

In clay, the report treats the cohort as a porewater sample. All 8 Opalinus genomes in the KBase Data Lakehouse trace to BRC-3 or BIC-A1 borehole isolation sources, which the report calls a direct, quantitative diagnostic that cultivation captures the porewater rather than the rock-attached fraction. [src: clay_confined_subsurface] The report says the in-situ porewater versus rock-attached dichotomy, described by Bagnoud and Mitzscherling at community level, is preserved at genome-content level among cultured isolates. [src: clay_confined_subsurface] The central digest repeats this interpretation of the sulfate-reduction marker result. [src: discoveries] See [[concepts/cultivation-bias-toward-porewater-versus-rock-attached-subsurface-communities]], [[entities/mont-terri-opalinus-clay]] and [[summaries/clay_confined_subsurface__REPORT]].

## Replication in mixed groundwater/aquifer

The ENIGMA comparison of cultured isolates against subsurface MAGs shows the same direction of enrichment. Aerobic-respiration coxABC markers had mean log2 enrichment = +7.29 with 91% prevalence in cultured genomes. [src: oak_ridge_cultivation_gap] Motility/chemotaxis markers (fliC, cheA, cheW) had mean log2 = +7.23 with 80% cultured prevalence. [src: oak_ridge_cultivation_gap] All 6 denitrification marker KOs (KEGG orthologs) were enriched in cultured genomes (log2 +1.5 to +3.0), narGH most strongly [src: oak_ridge_cultivation_gap]; the category mean was +2.05, and the report describes it as variable as predicted. [src: oak_ridge_cultivation_gap] The report states that this recapitulates the signature first documented in the clay project. [src: oak_ridge_cultivation_gap] It also finds the enrichment of aerobic respiration, motility and denitrification consistent between clay and mixed groundwater/aquifer lithologies. [src: oak_ridge_cultivation_gap] See [[summaries/oak_ridge_cultivation_gap__REPORT]].

## Interpretation and its limits

The report reads these functions as systematic selection, during standard cultivation, of organisms from mobile, oxygenated porewater adapted to flow, oxygen gradients and high-energy electron acceptors. [src: oak_ridge_cultivation_gap] It suggests porewater bias appears to be a general property of cultivation-based genome collections, not specific to one subsurface lithology. [src: oak_ridge_cultivation_gap] This is a hypothesis resting on two lithologies. The two projects use different comparisons, so their numbers are not set against each other. See also [[concepts/cultivation-bias-in-genome-collections-versus-uncultivated-lineages]] and [[entities/cultivation-bias-diagnostic]].

## Proposed tests

The clay report proposes testing the same SR/IR (sulfate reduction / iron reduction) marker framework on granite-hosted Olkiluoto, basalt-hosted Oak Ridge and salt-cavern cohorts in the KBase Data Lakehouse or future ingests. [src: clay_confined_subsurface] The Oak Ridge report proposes running cultivation_bias_diagnostic() at other Lakehouse sites with both cultured and MAG collections, to test whether the signature is universal. [src: oak_ridge_cultivation_gap]

## Open Directions

- Apply the SR/IR marker framework to Olkiluoto, Oak Ridge basalt and salt-cavern cohorts, to test lithologies beyond clay and aquifer.
- Run cultivation_bias_diagnostic() at every Lakehouse site holding both cultured and MAG collections, to test universality.
- Compare isolation-source metadata (porewater versus rock-attached sampling) with marker enrichment within a site, to test the porewater interpretation directly.
