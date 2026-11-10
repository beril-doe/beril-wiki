---
type: "Finding"
description: "The earlier clay project (PR #231, merged) used K07811/K17324/K17323 as iron-reduction markers, but those KOs are TMAO reductase, glycerol ABC transport and glycerol permease, not the intended multi-heme outer-surface cytochromes."
finding_id: "bacillota_b_subsurface_accessory--2f0dbfa7"
result: "correction"
source: "bacillota_b_subsurface_accessory"
quantities: []
caveat: "The erroneous KOs (K07811 TMAO reductase threshold 1336.87, K17324 glycerol ABC ATP-binding threshold 363.93, K17323 glycerol ABC permease threshold 318.27) made the earlier iron-reduction framing artefactual, and after correction the IR comparison loses statistical significance entirely."
first_added: "2026-10-27"
source_hash: "d7e7f6138df01ab1518706a0ea0667b6ddedc64f7966c6ac95c3ec44bcd45441"
---
# Earlier clay iron-reduction markers were unrelated genes, not cytochromes

The earlier clay project (PR #231, merged) used K07811/K17324/K17323 as iron-reduction markers, but those KOs are TMAO reductase, glycerol ABC transport and glycerol permease, not the intended multi-heme outer-surface cytochromes. [src: bacillota_b_subsurface_accessory]

## Evidence

> The clay project (PR #231, merged) used K07811/K17324/K17323 as iron-reduction markers — but those KOs are **TMAO reductase, glycerol ABC transport, and glycerol permease** respectively. KEGG has no canonical KO for the Geobacter omcS / Shewanella mtr operon multi-heme outer-surface cytochromes; the clay project unknowingly substituted unrelated genes. [src: bacillota_b_subsurface_accessory]

From the report [[summaries/bacillota_b_subsurface_accessory__REPORT]].

## Caveat

The erroneous KOs (K07811 TMAO reductase threshold 1336.87, K17324 glycerol ABC ATP-binding threshold 363.93, K17323 glycerol ABC permease threshold 318.27) made the earlier iron-reduction framing artefactual, and after correction the IR comparison loses statistical significance entirely. [src: bacillota_b_subsurface_accessory]

> - **H3 correction is a real bug fix in PR #231.** The `clay_confined_subsurface` project's IR-side analysis used K07811 (TMAO reductase, threshold 1336.87), K17324 (glycerol ABC ATP-binding, threshold 363.93), K17323 (glycerol ABC permease, threshold 318.27) — none are iron-reduction genes, and KEGG has no canonical KO for Geobacter omcS / Shewanella mtr lineages. The clay project's "Mitzscherling rock-attached signature in shallow clay" framing was an artefact of mismatched gene IDs combined with the standard eggNOG-mapper threshold (which doesn't filter on KO biological identity, just sequence similarity). After correction, the IR comparison loses statistical significance entirely. [src: bacillota_b_subsurface_accessory]

## Other caveats in this report

- The keyword screen placed 462 enriched OGs in an other/unannotated category that includes missed anaerobic-niche signals. [src: bacillota_b_subsurface_accessory]
- Gene-family and domain names caused the preregistered keyword scan to miss anaerobic-niche signals; manual review of the top 15 enriched OGs found additional anaerobic-respiration/electron-transfer hits. [src: bacillota_b_subsurface_accessory]
- The report estimates that manual reclassification could raise the H1-relevant count from the keyword count of 42 to approximately 80–100 of 547; this is not a finalized count. [src: bacillota_b_subsurface_accessory]
- Bacillota_B gene-content expansion contrasts with Patescibacteria/CPR streamlining (≤1 Mbp, episymbiotic), but the cited Tian result concerns another superphylum. The report connects expansion to a self-sufficiency hypothesis and identifies *Ca.* Desulforudis audaxviator genome GB_GCA_020725505.1 in the anchor. [src: bacillota_b_subsurface_accessory]
- Only ~6 clusters across four multi-heme-cytochrome PFAMs were available in Bacillota_B; sequence-level CXXCH motif counting supplied most of the corrected iron-reduction signal. [src: bacillota_b_subsurface_accessory]
