---
type: "Finding"
description: "Per-OG Fisher's exact tests (anchor n=10 vs baseline n=62) on 14,109 eggNOG OGs, using Firmicutes-level OGs where available and Bacteria/root OGs as fallbacks, BH-FDR corrected with q<0.05, fold-difference\u22653 and \u22653 anchor genomes positive, yielded 547 enriched OGs, far above the H1 prediction of \u226510."
finding_id: "bacillota_b_subsurface_accessory--b2fd7eb1"
result: "observation"
source: "bacillota_b_subsurface_accessory"
quantities: [{"value": "547", "what": "OGs enriched in deep-clay anchor", "unit": "OGs", "denominator": "14,109 OGs tested", "scope": "anchor n=10 vs baseline n=62; mixed Firmicutes-level and Bacteria/root-level OGs"}]
caveat: "The OG presence matrix uses Firmicutes-level orthologous groups where available, with Bacteria/root fallbacks, so the enrichment inputs are not uniformly Firmicutes-level OGs."
first_added: "2026-10-27"
source_hash: "d7e7f6138df01ab1518706a0ea0667b6ddedc64f7966c6ac95c3ec44bcd45441"
---
# Many orthogroups are enriched in deep-clay anchors versus soil baselines

Per-OG Fisher's exact tests (anchor n=10 vs baseline n=62) on 14,109 eggNOG OGs, using Firmicutes-level OGs where available and Bacteria/root OGs as fallbacks, BH-FDR corrected with q<0.05, fold-difference≥3 and ≥3 anchor genomes positive, yielded 547 enriched OGs, far above the H1 prediction of ≥10. [src: bacillota_b_subsurface_accessory]

## Key figures

- **547 OGs**: OGs enriched in deep-clay anchor (denominator 14,109 OGs tested; scope anchor n=10 vs baseline n=62; mixed Firmicutes-level and Bacteria/root-level OGs) [src: bacillota_b_subsurface_accessory]

## Evidence

> Per-OG Fisher's exact (anchor n=10 vs baseline n=62) on 14,109 Firmicutes-level eggNOG OGs, BH-FDR corrected. Filters: q<0.05, fold-difference≥3, ≥3 anchor genomes positive. **547 OGs enriched** in deep-clay anchor — far above the H1 prediction of "≥10". Pre-registered functional categories (keyword-scanned on eggNOG `Description`/`Preferred_name` + bakta `gene`/`product`): [src: bacillota_b_subsurface_accessory]

From the report [[summaries/bacillota_b_subsurface_accessory__REPORT]].

## Caveat

The OG presence matrix uses Firmicutes-level orthologous groups where available, with Bacteria/root fallbacks, so the enrichment inputs are not uniformly Firmicutes-level OGs. [src: bacillota_b_subsurface_accessory]

> | `02_og_presence.ipynb` | Genome × eggNOG OG presence matrix (Firmicutes-level OG with bacteria/root fallbacks) | [src: bacillota_b_subsurface_accessory]

## Other caveats in this report

- The keyword screen placed 462 enriched OGs in an other/unannotated category that includes missed anaerobic-niche signals. [src: bacillota_b_subsurface_accessory]
- Gene-family and domain names caused the preregistered keyword scan to miss anaerobic-niche signals; manual review of the top 15 enriched OGs found additional anaerobic-respiration/electron-transfer hits. [src: bacillota_b_subsurface_accessory]
- The report estimates that manual reclassification could raise the H1-relevant count from the keyword count of 42 to approximately 80–100 of 547; this is not a finalized count. [src: bacillota_b_subsurface_accessory]
- Bacillota_B gene-content expansion contrasts with Patescibacteria/CPR streamlining (≤1 Mbp, episymbiotic), but the cited Tian result concerns another superphylum. The report connects expansion to a self-sufficiency hypothesis and identifies *Ca.* Desulforudis audaxviator genome GB_GCA_020725505.1 in the anchor. [src: bacillota_b_subsurface_accessory]
- Only ~6 clusters across four multi-heme-cytochrome PFAMs were available in Bacillota_B; sequence-level CXXCH motif counting supplied most of the corrected iron-reduction signal. [src: bacillota_b_subsurface_accessory]
