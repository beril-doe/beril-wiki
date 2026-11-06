---
type: "Finding"
description: "92 CAZy families show elevated co-occurrence with T4SS loci at \u226410 kb (threshold validation pending); GT2 glycosyltransferases are the top hit (767 genomes, avg 5,041 bp)."
finding_id: "t4ss_cazy_environmental_hgt--91e33b0b"
result: "observation"
source: "t4ss_cazy_environmental_hgt"
quantities: [{"value": "92", "what": "CAZy families with elevated co-occurrence with T4SS loci", "unit": "families", "denominator": "", "scope": "within \u226410 kb"}, {"value": "767", "what": "genomes with GT2 near T4SS", "unit": "genomes", "denominator": "", "scope": "GT2 top hit"}, {"value": "5,041", "what": "average distance of GT2 to T4SS", "unit": "bp", "denominator": "", "scope": "GT2"}]
caveat: "The synteny-threshold permutation test, which requires Spark unfiltered data, is still pending."
first_added: "2026-10-27"
source_hash: "51a111efe7b5ea5f55b6310291e8badbd42dcc5ebe29717b03e23d2c103de389"
---
# Many CAZy families co-occur near T4SS loci, led by GT2

92 CAZy families show elevated co-occurrence with T4SS loci at ≤10 kb (threshold validation pending); GT2 glycosyltransferases are the top hit (767 genomes, avg 5,041 bp). [src: t4ss_cazy_environmental_hgt]

## Key figures

- **92 families**: CAZy families with elevated co-occurrence with T4SS loci (scope within ≤10 kb) [src: t4ss_cazy_environmental_hgt]
- **767 genomes**: genomes with GT2 near T4SS (scope GT2 top hit) [src: t4ss_cazy_environmental_hgt]
- **5,041 bp**: average distance of GT2 to T4SS (scope GT2) [src: t4ss_cazy_environmental_hgt]

## Evidence

> **92 CAZy families** show elevated co-occurrence with T4SS loci at ≤10 kb (threshold validation pending); GT2 glycosyltransferases are the top hit (767 genomes, avg 5,041 bp). [src: t4ss_cazy_environmental_hgt]

From the report [[summaries/t4ss_cazy_environmental_hgt__REPORT]].

## Caveat

The synteny-threshold permutation test, which requires Spark unfiltered data, is still pending. [src: t4ss_cazy_environmental_hgt]

> 1. Synteny threshold permutation test (requires Spark unfiltered data) 2. Node_4915 BLAST validation (requires BLAST against NCBI nr) 3. Housekeeping gene null baseline 4. Biome enrichment factorisation: θ = OR(T4SS-CAZy) / [OR(T4SS) × OR(CAZy)] [src: t4ss_cazy_environmental_hgt]

## Other caveats in this report

- The report labels the work preliminary and says NB05 threshold validation and NB06 manuscript figures are pending, although it later presents NB05 analysis results. [src: t4ss_cazy_environmental_hgt]
- T4SS-mediated dissemination of carbohydrate-active enzymes is presented as a hypothesis, not a demonstrated mechanism; the associations are observational and require experimental validation. [src: t4ss_cazy_environmental_hgt]
- The report links CAZy–T4SS synteny to a metal-resistance niche-breadth hypothesis; describing these genomes as transfer hubs is interpretive. [src: t4ss_cazy_environmental_hgt]
