---
type: "Finding"
description: "The kescience \u2194 refdata bridge had zero realized use at audit time despite 12 keys, including AlphaFold IDs; it was one of five high-leverage bridges with zero realized use."
finding_id: "berdl_data_atlas--a3de4519"
result: "observation"
source: "berdl_data_atlas"
quantities: [{"value": "12", "what": "keys on the kescience \u2194 refdata bridge", "unit": "keys", "denominator": "", "scope": ""}]
caveat: "Value-space validity of joins is established only for UC1; the bridge atlas proves the schema admits a join but not that the value space overlaps."
first_added: "2026-11-24"
source_hash: "be5f29816668f7662998e22a666a6a398c84a18d10e70464cfbd943fc645831e"
---
# High-leverage bridge between kescience and refdata went unused

The kescience ↔ refdata bridge had zero realized use at audit time despite 12 keys, including AlphaFold IDs; it was one of five high-leverage bridges with zero realized use. [src: berdl_data_atlas]

## Key figures

- **12 keys**: keys on the kescience ↔ refdata bridge [src: berdl_data_atlas]

## Evidence

> **Five high-leverage bridges had zero realized use at audit time**: `kescience ↔ refdata` (12 keys, including AlphaFold IDs), `enigma ↔ phagefoundry` (11), `kbase ↔ refdata` (11, including `gtdb_taxonomy`), `nmdc ↔ protect` (10), `nmdc ↔ refdata` (9). [src: berdl_data_atlas]

From the report [[summaries/berdl_data_atlas__REPORT]].

## Caveat

Value-space validity of joins is established only for UC1; the bridge atlas proves the schema admits a join but not that the value space overlaps. [src: berdl_data_atlas]

> **Value-space validity of joins is established only for UC1.** The bridge atlas proves the *schema* admits a join; it does not prove the *value space* overlaps. [src: berdl_data_atlas]

## Other caveats in this report

- The proposed structural fitness atlas join required correction because FitnessBrowser exposes (orgId, locusId), not protein_id, and its AlphaFold bridge runs through besthitswissprot.sprotAccession. [src: berdl_data_atlas]
- The proposed structural-fitness atlas bridge through protein_id was incorrect because FitnessBrowser uses a composite (orgId, locusId) primary key and does not expose protein_id. [src: berdl_data_atlas]
- The atlas references canonically cite catalogued data systems rather than biological hypotheses being tested. [src: berdl_data_atlas]
- The genome_id key has different meanings in KBase, NCBI, and MAG pipelines: UPA, accession, and hash, respectively. [src: berdl_data_atlas]
- UC2–UC5 require their own initial sample execution before publication, whereas UC1 has been completed. [src: berdl_data_atlas]
