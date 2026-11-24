---
type: "Finding"
description: "ENIGMA holds 36% of tables but appears in only 6 audited BERIL projects."
finding_id: "berdl_data_atlas--37042adf"
result: "observation"
source: "berdl_data_atlas"
quantities: [{"value": "36%", "what": "share of lakehouse tables held by ENIGMA", "unit": "", "denominator": "", "scope": ""}, {"value": "6", "what": "audited BERIL projects using ENIGMA", "unit": "projects", "denominator": "", "scope": ""}]
caveat: "The realized-use audit is README-based, so data-source mentions in research plans or notebook source may have been missed and true per-project tenant breadth is a lower bound."
first_added: "2026-11-24"
source_hash: "be5f29816668f7662998e22a666a6a398c84a18d10e70464cfbd943fc645831e"
---
# ENIGMA is table-rich but rarely used in BERIL projects

ENIGMA holds 36% of tables but appears in only 6 audited BERIL projects. [src: berdl_data_atlas]

## Key figures

- **36%**: share of lakehouse tables held by ENIGMA [src: berdl_data_atlas]
- **6 projects**: audited BERIL projects using ENIGMA [src: berdl_data_atlas]

## Evidence

> ENIGMA holds 36% of tables but appears in only 6 projects [src: berdl_data_atlas]

From the report [[summaries/berdl_data_atlas__REPORT]].

## Caveat

The realized-use audit is README-based, so data-source mentions in research plans or notebook source may have been missed and true per-project tenant breadth is a lower bound. [src: berdl_data_atlas]

> **Realized-use audit is README-based** — data-source mentions buried in research plans or in notebook source may have been missed. True per-project tenant breadth is a **lower bound**. [src: berdl_data_atlas]

## Other caveats in this report

- The proposed structural fitness atlas join required correction because FitnessBrowser exposes (orgId, locusId), not protein_id, and its AlphaFold bridge runs through besthitswissprot.sprotAccession. [src: berdl_data_atlas]
- The proposed structural-fitness atlas bridge through protein_id was incorrect because FitnessBrowser uses a composite (orgId, locusId) primary key and does not expose protein_id. [src: berdl_data_atlas]
- The atlas references canonically cite catalogued data systems rather than biological hypotheses being tested. [src: berdl_data_atlas]
- Join value-space validity is established only for UC1; the bridge atlas establishes schema compatibility but not overlapping values. [src: berdl_data_atlas]
- The genome_id key has different meanings in KBase, NCBI, and MAG pipelines: UPA, accession, and hash, respectively. [src: berdl_data_atlas]
