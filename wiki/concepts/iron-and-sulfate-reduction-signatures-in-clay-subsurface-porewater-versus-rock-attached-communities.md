---
type: "Concept"
description: "Whether corrected multi-heme cytochrome iron-reduction and sulfate-reduction marker prevalence differ between deep clay, shallow clay and soil cohorts."
sources: ["summaries/bacillota_b_subsurface_accessory__REPORT.md", "summaries/clay_confined_subsurface__REPORT.md", "summaries/discoveries.md"]
---
# Iron- and sulfate-reduction signatures in clay subsurface porewater versus rock-attached communities

This page covers whether corrected multi-heme cytochrome iron-reduction (IR) and sulfate-reduction (SR) marker prevalence differs between deep clay, shallow clay and soil cohorts. After correction, no IR comparison between cohorts is significant. [src: bacillota_b_subsurface_accessory, discoveries] The SR signal in deep clay stands. [src: bacillota_b_subsurface_accessory, discoveries] The evidence comes from one project's cohorts, re-analysed in a second report and restated in the central digest. See also [[concepts/reliability-of-kegg-ortholog-markers-for-multi-heme-cytochrome-iron-reduction]] and [[concepts/cultivation-bias-toward-porewater-versus-rock-attached-subsurface-communities]].

## The IR correction

The original clay project used the wrong KEGG orthologs (KOs) for IR. A re-run replaced them with a multi-heme cytochrome detector ([[entities/multi-heme-cytochrome-detector]]). [src: discoveries] A genome scores positive if any of three signals is present. [src: bacillota_b_subsurface_accessory] The signals are PFAM PF02085 (Cytochrom_CIII multi-heme c-type) [src: bacillota_b_subsurface_accessory], PFAM PF22678 (Cytochrom_c_NrfB-like multi-heme nitrite reductase) [src: bacillota_b_subsurface_accessory], and a CXXCH heme-binding motif count ≥4 in gene_cluster.faa_sequence, described as a canonical method since Methé et al. 2003 *Geobacter*. [src: bacillota_b_subsurface_accessory]

The correction changed every cohort's rate, and it reversed the deep-versus-shallow order. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface]

| Cohort | n | Original IR rate | Corrected rate |
|---|---|---|---|
| anchor_deep (Mont Terri Opalinus + bentonite) | 9 | 11.1% (1/9) | 55.6% (5/9) [src: bacillota_b_subsurface_accessory, clay_confined_subsurface] |
| anchor_shallow (Coalvale + Cerrado + agricultural) | 30 | 50.0% (15/30) | 40.0% (12/30) [src: bacillota_b_subsurface_accessory, clay_confined_subsurface] |
| soil_baseline | 149 | 20.1% (30/149) | 40.9% (61/149) [src: bacillota_b_subsurface_accessory, clay_confined_subsurface] |

The digest gives the same rounded values: 56% (was 11%), 40% (was 50%) and 41% (was 20%). [src: discoveries]

Corrected pairwise Fisher's exact tests ([[entities/fisher-s-exact-test-with-benjamini-hochberg-fdr]]) were all non-significant. Deep versus shallow gave OR (odds ratio)=1.88, p=0.46. [src: bacillota_b_subsurface_accessory] Deep versus baseline gave OR=1.80, p=0.49. [src: bacillota_b_subsurface_accessory] Shallow versus baseline gave OR=0.96, p=1.0. [src: bacillota_b_subsurface_accessory] The report states that all pairwise Fisher p ≥ 0.46. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface, discoveries] The IR comparison loses significance entirely. [src: bacillota_b_subsurface_accessory]

The original pre-correction claim was a 3.7-fold IR-marker enrichment in shallow clay versus the broader soil baseline (p=0.0025). The marker correction invalidated it. [src: clay_confined_subsurface] The report says shallow (40%) is now lower than deep (56%), but not significantly. Multi-heme cytochrome content is similar across the three cohorts and similar to the soil baseline (41%). [src: bacillota_b_subsurface_accessory] The IR-side narrative that the clay cohort diverges from the Mitzscherling rock-attached community because shallow clay is IR-rich is withdrawn. [src: clay_confined_subsurface] The digest calls it an artefact. [src: discoveries] See [[entities/mitzscherling-et-al-2023-rock-attached-community-profile]].

## Sulfate reduction stands

The SR markers K11180, K11181, K00394, K00395 and K00958 were correctly identified. [src: bacillota_b_subsurface_accessory] The deep clay cohort is enriched for SR markers, with 5/9 (56%) positive. [src: clay_confined_subsurface] Against the Mitzscherling rock-attached null of 0.2%, the binomial p is 4×10⁻¹². [src: bacillota_b_subsurface_accessory, discoveries] Five of nine anchor_deep genomes carry the Sat, AprAB, DsrAB module ([[entities/dissimilatory-sulfate-reduction-pathway]]). [src: clay_confined_subsurface]

The CheckM-filtered marker-class counts show the contrast. The source claims do not state which IR markers define the IR_only and neither classes, so read the IR columns with caution. [src: clay_confined_subsurface]

| Cohort | IR_only | SR_only | both | neither |
|---|---|---|---|---|
| anchor_deep | 1 | 5 | 0 | 3 [src: clay_confined_subsurface] |
| anchor_shallow | 15 | 0 | 0 | 15 [src: clay_confined_subsurface] |
| soil_baseline | 29 | 4 | 1 | 106 [src: clay_confined_subsurface] |

SR_complete occurred in 5 of 9 anchor_deep genomes versus 5 of 140 soil_baseline genomes (OR=33.8, p_BH=2.5×10⁻⁴). [src: clay_confined_subsurface] Pairwise tests gave deep versus shallow OR=∞, p=2×10⁻⁴ [src: clay_confined_subsurface], and deep versus soil_baseline OR=33.8, p=5×10⁻⁵. [src: clay_confined_subsurface] Shallow versus soil_baseline was not significant (OR=0.0, p=0.59). [src: clay_confined_subsurface] The IR_complete test of deep versus baseline was also null (1/9 versus 30/140, OR=0.46, p_BH=0.69). [src: clay_confined_subsurface]

## What this means for the porewater framing

The porewater-bias headline holds through SR alone. The rock-attached versus porewater dichotomy is half supported (SR) and half unsupported (IR, after correction). [src: bacillota_b_subsurface_accessory, clay_confined_subsurface] The correction is robust for the multi-heme cytochrome signal. It does not settle whether the original porewater-pattern narrative is fully recovered or partly undercut. [src: bacillota_b_subsurface_accessory] The report proposes a correction notebook and a report amendment marking the IR-side H3 finding as artefactual. [src: bacillota_b_subsurface_accessory]

## Open Directions

- Test the corrected IR detector on a larger deep-clay set. With n=9, an OR of 1.88 cannot be told apart from no difference.
- Compare the corrected IR rates against the Mitzscherling rock-attached profile directly, as was done for SR, to see whether any IR contrast with the rock-attached community survives.
- Control for phylum when comparing cohorts (see [[concepts/phylum-level-confounding-of-habitat-specific-anaerobic-gene-content]]), to check whether the SR enrichment is a lineage effect.
- Re-run the marker-class breakdown with the corrected IR detector, so the IR_only, SR_only, both and neither classes are on the corrected markers.
