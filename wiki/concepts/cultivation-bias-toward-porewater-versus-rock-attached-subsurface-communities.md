---
type: "Concept"
description: "Whether cultured isolate genomes from clay-confined subsurface sites represent porewater or rock-attached communities, tested against published community profiles; stops at the clay cohort and does not cover uncultivated MAG-based surveys."
sources: ["summaries/bacillota_b_subsurface_accessory__REPORT.md", "summaries/clay_confined_subsurface__REPORT.md", "summaries/discoveries.md"]
---
# Cultivation bias toward porewater versus rock-attached subsurface communities

This page asks whether cultured isolate genomes from clay-confined subsurface sites represent porewater or rock-attached communities. In one cohort the SR (sulfate reduction) signal points to porewater and survives a later correction. The IR (iron reduction) side lost its narrative force after marker correction. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface] The page covers only the cultured clay cohort. See [[concepts/porewater-bias-as-a-general-signature-of-cultivation-based-subsurface-collections]] for the general pattern.

## Two published paradigms at one site

Published work describes two different communities at the same clay site. Porewater is dominated by sulfate reducers, and rock surfaces by Geobacter/Geothrix iron reducers. [src: discoveries, clay_confined_subsurface] Mitzscherling et al. (2023) reported a rock-attached profile with SRB <0.2% and IRB 4.3–10.2%, dominated by Geobacter and Geothrix. [src: clay_confined_subsurface] The report's null used SR ~0.2% and IR ~7%. [src: clay_confined_subsurface] Bagnoud reported an Opalinus porewater food web in which Desulfobulbaceae c16a expressed the complete Wood–Ljungdahl pathway, group 1 [NiFe]-hydrogenase, and Sat–AprAB–DsrAB. Three MAGs (metagenome assembled genomes) recurred across seven boreholes. [src: clay_confined_subsurface] Bagnoud (2016) reported protein-level expression of the toolkit modules. [src: clay_confined_subsurface]

## Evidence that the cultured cohort is porewater-like

The isolation sources and the sulfate-reduction marker content both point to porewater. All 8 Opalinus genomes in the KBase Data Lakehouse come from BRC-3 or BIC-A1 boreholes. The report calls this a direct, quantitative diagnostic of cultivation bias. [src: clay_confined_subsurface] The Desulfosporosinus and BRH-c8a lineages match the three MAGs Bagnoud detected, which the report reads as cross-platform validation of indigeneity. [src: clay_confined_subsurface]

- The 9 deep clay genomes are enriched for SR markers (5/9 = 56%). [src: clay_confined_subsurface] The same report also gave IR depletion (1/9 = 11%) [src: clay_confined_subsurface], but that IR side was later judged artefactual (see the correction section below). [src: bacillota_b_subsurface_accessory]
- Against the rock-attached null, SR enrichment gave observed 5 versus expected 0.018 of 9, with binomial p = 4.0×10⁻¹². [src: clay_confined_subsurface]
- Five of nine carry the Sat, AprAB, DsrAB module. Seven carry group 1 [NiFe]-hydrogenase markers, including direct hits on BRH-c8a and Desulfosporosinus. [src: clay_confined_subsurface]
- IR depletion against the null was not significant (observed 1, expected 0.63, p=0.87). [src: clay_confined_subsurface]
- The SR_complete Fisher test of deep versus shallow cultured clay gave OR=∞, p=2×10⁻⁴. [src: clay_confined_subsurface] The report also described the deep and shallow profiles as mirror images, with shallow dominated by IR_only. That IR-based part rests on the markers later judged artefactual, so only the SR comparison is treated as supported. [src: clay_confined_subsurface, bacillota_b_subsurface_accessory]
- Deep versus soil baseline gave OR=33.8, p=5×10⁻⁵. [src: clay_confined_subsurface] Shallow versus soil baseline was not significant (OR=0.0, p=0.59). [src: clay_confined_subsurface]
- Marker classes as originally reported (IR_only, SR_only, both, neither): anchor_deep 1, 5, 0, 3. [src: clay_confined_subsurface] anchor_shallow 15, 0, 0, 15. [src: clay_confined_subsurface] soil_baseline 29, 4, 1, 106. [src: clay_confined_subsurface] The IR_only counts predate the correction. [src: bacillota_b_subsurface_accessory]

The report concludes that H3 replicates the Bagnoud porewater paradigm at population-genome level. [src: clay_confined_subsurface] It also says H3 diverges from the Mitzscherling profile. It reads the divergence as showing what cultivation-accessible cohorts miss, since the KBase Data Lakehouse has no genomes from rock-attached MAGs at Mont Terri. [src: clay_confined_subsurface] The report claims this is the first quantitative test of the dichotomy in cultured pangenome data. [src: clay_confined_subsurface] It states that the dichotomy is preserved at genome-content level among cultured isolates. That claim is limited by the later correction: the SR side stands, the IR-side comparison loses force, and whether the original narrative is fully recovered is unresolved. [src: clay_confined_subsurface, bacillota_b_subsurface_accessory] The cross-project digest reads the SR result as direct quantitative evidence for the porewater fraction. [src: discoveries]

The diagnostic compares SR-marker (dsrAB-aprAB-sat) and IR-marker (omcS / mtrC / mtrA) prevalences with rock-attached frequencies by binomial test. [src: discoveries] The report proposes it as a p-valued statistic that generalizes to future cohorts. [src: clay_confined_subsurface] See [[entities/cultivation-bias-diagnostic]].

## Correction to the IR side

A later project corrected the IR markers. The SR-side finding stands: the markers K11180/K11181/K00394/K00395/K00958 were correctly identified, and p=4×10⁻¹² is robust. [src: clay_confined_subsurface, bacillota_b_subsurface_accessory, discoveries] The "Mitzscherling rock-attached IR-rich pattern in shallow clay" interpretation was an artefact. [src: discoveries] The report attributes it to mismatched gene IDs combined with an eggNOG-mapper threshold that filters sequence similarity rather than KO (KEGG ortholog) identity. [src: bacillota_b_subsurface_accessory] It calls the IR-side H3 finding artefactual and proposes a correction notebook and amendment. [src: bacillota_b_subsurface_accessory]

The porewater-bias headline therefore holds via SR alone. The rock-attached versus porewater framing is half supported (SR) and half unsupported (IR). [src: bacillota_b_subsurface_accessory] The correction is robust for multi-heme cytochromes. It does not settle whether the original porewater-pattern narrative is fully recovered or partly undercut. [src: bacillota_b_subsurface_accessory] See [[concepts/reliability-of-kegg-ortholog-markers-for-multi-heme-cytochrome-iron-reduction]].

## Limits

- The cohort is cultured-only, so conclusions apply to cultivable porewater-cultured deep-clay isolates, not the full Mont Terri or bentonite community. [src: clay_confined_subsurface]
- CPR (candidate phyla radiation) and DPANN episymbionts, and rock-attached Geobacter/Geothrix lineages, are essentially absent. [src: clay_confined_subsurface]
- MAG-augmented work is necessary to test whether the genuine clay-confined community matches the literature predictions. [src: clay_confined_subsurface]
- The report proposes ANI (average nucleotide identity) matching of Opalinus genomes to Bagnoud's MAGs, to test whether gene presence corresponds to expression-validated activity. [src: clay_confined_subsurface]
- Compartment labels are keyword-inferred from isolation_source strings, and some bentonite or "rock" entries could be either type. [src: clay_confined_subsurface] H3 results were robust to two stricter compartment definitions. [src: clay_confined_subsurface]
- The Bacillota_B anchor cohort is borehole/porewater-dominated by construction, so it cannot test rock-attached Bacillota_B gene content. [src: bacillota_b_subsurface_accessory]

## Open Directions

- Add MAG-based rock-attached Mont Terri genomes and rerun the SR/IR diagnostic, to test whether the genuine community matches the literature.
- Match the Opalinus genomes to Bagnoud's MAGs by ANI. Then ask whether gene presence matches expression-validated activity.
- Rerun the IR-side comparison with corrected multi-heme cytochrome markers, to see how much of the porewater narrative is recovered.
- Re-annotate compartments from curated metadata, to bound the effect of keyword inference.
