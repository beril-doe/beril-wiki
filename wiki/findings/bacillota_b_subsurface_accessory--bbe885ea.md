---
type: "Finding"
description: "With the corrected multi-heme cytochrome detector, pairwise Fisher tests found deep vs shallow OR=1.88 p=0.46, deep vs baseline OR=1.80 p=0.49, and shallow vs baseline OR=0.96 p=1.0; no comparison was significant after correction, and the earlier shallow>deep iron-reduction pattern disappeared."
finding_id: "bacillota_b_subsurface_accessory--bbe885ea"
result: "null result"
source: "bacillota_b_subsurface_accessory"
quantities: [{"value": "OR=1.88 p=0.46", "what": "deep vs shallow pairwise Fisher test, corrected detector", "unit": "", "denominator": "", "scope": "clay-project cohorts"}, {"value": "OR=1.80 p=0.49", "what": "deep vs baseline pairwise Fisher test, corrected detector", "unit": "", "denominator": "", "scope": ""}, {"value": "OR=0.96 p=1.0", "what": "shallow vs baseline pairwise Fisher test, corrected detector", "unit": "", "denominator": "", "scope": ""}]
caveat: "Only ~6 clusters across all four multi-heme-cytochrome PFAMs were available in Bacillota_B, so CXXCH motif counting on gene_cluster.faa_sequence carried most of the corrected IR signal (rates of 40\u201356%)."
first_added: "2026-10-27"
source_hash: "d7e7f6138df01ab1518706a0ea0667b6ddedc64f7966c6ac95c3ec44bcd45441"
---
# Corrected iron-reduction comparison shows no significant deep versus shallow difference

With the corrected multi-heme cytochrome detector, pairwise Fisher tests found deep vs shallow OR=1.88 p=0.46, deep vs baseline OR=1.80 p=0.49, and shallow vs baseline OR=0.96 p=1.0; no comparison was significant after correction, and the earlier shallow>deep iron-reduction pattern disappeared. [src: bacillota_b_subsurface_accessory]

## Key figures

- **OR=1.88 p=0.46**: deep vs shallow pairwise Fisher test, corrected detector (scope clay-project cohorts) [src: bacillota_b_subsurface_accessory]
- **OR=1.80 p=0.49**: deep vs baseline pairwise Fisher test, corrected detector [src: bacillota_b_subsurface_accessory]
- **OR=0.96 p=1.0**: shallow vs baseline pairwise Fisher test, corrected detector [src: bacillota_b_subsurface_accessory]

## Evidence

> Pairwise Fisher (corrected): deep vs shallow OR=1.88 p=0.46; deep vs baseline OR=1.80 p=0.49; shallow vs baseline OR=0.96 p=1.0. **No comparison is significant after correction.** The original clay-project analysis showed shallow >> deep (50% vs 11%) — a "Mitzscherling rock-attached IR-rich pattern in shallow clay" interpretation. With the corrected detector, shallow (40%) is *lower* than deep (56%) and the difference is not statistically significant; multi-heme cytochrome content is similar across all three clay-project cohorts and similar to soil baseline (41%). [src: bacillota_b_subsurface_accessory]

From the report [[summaries/bacillota_b_subsurface_accessory__REPORT]].

## Caveat

Only ~6 clusters across all four multi-heme-cytochrome PFAMs were available in Bacillota_B, so CXXCH motif counting on gene_cluster.faa_sequence carried most of the corrected IR signal (rates of 40–56%). [src: bacillota_b_subsurface_accessory]

> PF14537 confirmed silently absent (the documented `plant_microbiome_ecotypes` pitfall). Multi-heme cytochrome PFAMs are sparse within Bacillota_B (only ~6 clusters total across all four PFAMs); CXXCH motif counting on `gene_cluster.faa_sequence` carried most of the IR signal in NB06 — which is why the corrected IR rates (40–56%) are far higher than what PFAM-only detection would yield. [src: bacillota_b_subsurface_accessory]

## Other caveats in this report

- The keyword screen placed 462 enriched OGs in an other/unannotated category that includes missed anaerobic-niche signals. [src: bacillota_b_subsurface_accessory]
- Gene-family and domain names caused the preregistered keyword scan to miss anaerobic-niche signals; manual review of the top 15 enriched OGs found additional anaerobic-respiration/electron-transfer hits. [src: bacillota_b_subsurface_accessory]
- The report estimates that manual reclassification could raise the H1-relevant count from the keyword count of 42 to approximately 80–100 of 547; this is not a finalized count. [src: bacillota_b_subsurface_accessory]
- Bacillota_B gene-content expansion contrasts with Patescibacteria/CPR streamlining (≤1 Mbp, episymbiotic), but the cited Tian result concerns another superphylum. The report connects expansion to a self-sufficiency hypothesis and identifies *Ca.* Desulforudis audaxviator genome GB_GCA_020725505.1 in the anchor. [src: bacillota_b_subsurface_accessory]
- The report specifies erroneous KO identities and thresholds—K07811 TMAO reductase 1336.87, K17324 glycerol ABC ATP-binding 363.93, K17323 glycerol ABC permease 318.27—and identifies the former iron-reduction framing as artefactual. [src: bacillota_b_subsurface_accessory]
