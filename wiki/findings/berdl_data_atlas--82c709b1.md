---
type: "Finding"
description: "UC1 was sample-validated on the live cluster after its proposed protein_id join was corrected (FitnessBrowser exposes (orgId, locusId); the bridge runs through besthitswissprot.sprotAccession), yielding 55,454 FitnessBrowser genes across 48 organisms with fitness measurements and an AlphaFold model, and SwissProt-best-hit coverage of AlphaFold of 99.5%."
finding_id: "berdl_data_atlas--82c709b1"
result: "correction"
source: "berdl_data_atlas"
quantities: [{"value": "55,454", "what": "FitnessBrowser genes with both fitness data and an AlphaFold model", "unit": "genes", "denominator": "", "scope": "48 organisms"}, {"value": "48", "what": "organisms in the joined cohort", "unit": "organisms", "denominator": "", "scope": ""}, {"value": "99.5%", "what": "SwissProt-best-hit coverage of AlphaFold", "unit": "percent", "denominator": "", "scope": "live cluster"}]
caveat: "The validated 55,454-gene cohort lacks structural features because kescience_alphafold.alphafold_entries does not carry per-residue pLDDT or structural-feature data."
first_added: "2026-11-11"
source_hash: "be5f29816668f7662998e22a666a6a398c84a18d10e70464cfbd943fc645831e"
---
# Corrected join links fitness genes to AlphaFold models via SwissProt best hits

UC1 was sample-validated on the live cluster after its proposed protein_id join was corrected (FitnessBrowser exposes (orgId, locusId); the bridge runs through besthitswissprot.sprotAccession), yielding 55,454 FitnessBrowser genes across 48 organisms with fitness measurements and an AlphaFold model, and SwissProt-best-hit coverage of AlphaFold of 99.5%. [src: berdl_data_atlas]

## Key figures

- **55,454 genes**: FitnessBrowser genes with both fitness data and an AlphaFold model (scope 48 organisms) [src: berdl_data_atlas]
- **48 organisms**: organisms in the joined cohort [src: berdl_data_atlas]
- **99.5%**: SwissProt-best-hit coverage of AlphaFold (scope live cluster) [src: berdl_data_atlas]

## Evidence

> 6. **UC1 (structural fitness atlas) has been sample-validated on the live cluster.** The proposed join recipe required correction (FitnessBrowser exposes `(orgId, locusId)`, not `protein_id`; the bridge to AlphaFold runs through `besthitswissprot.sprotAccession`). The corrected join produces a working dataset of **55,454 FitnessBrowser genes across 48 organisms** with both fitness measurements AND an AlphaFold model. SwissProt-best-hit coverage of AlphaFold is 99.5%. [src: berdl_data_atlas]

From the report [[summaries/berdl_data_atlas__REPORT]].

## Caveat

The validated 55,454-gene cohort lacks structural features because kescience_alphafold.alphafold_entries does not carry per-residue pLDDT or structural-feature data. [src: berdl_data_atlas]

> 2. **Promote UC1 into its own project.** The validated 55,454-gene cohort is the seed dataset. The known gap is that `kescience_alphafold.alphafold_entries` does not carry per-residue pLDDT or structural-feature data; either ingest those features or compute them from PDB files as a derived BERDL collection. [src: berdl_data_atlas]

## Other caveats in this report

- The 29 canonical keys include sample_id across 10 tenants and genome_id, ncbi_taxon_id, and feature_id across 9 each; 536 bridges are counted at tenant × topic cell granularity, not as validated record-level joins. [src: berdl_data_atlas]
- The unused-bridge ranking is based on schema-level join surface and project use only at audit time. [src: berdl_data_atlas]
- UC2 proposes testing prophage-mediated metal-resistance along the Oak Ridge contamination gradient using enigma ↔ phagefoundry (11 shared keys); this is a question, not a demonstrated effect. [src: berdl_data_atlas]
- UC3 proposes comparing GTDB clades and KBase species pangenomes using kbase ↔ refdata (11 shared keys); disagreement and gene-flow implications remain questions. [src: berdl_data_atlas]
- UC4 proposes linking environmental pathogen occurrence and biogeochemistry using nmdc ↔ protect (10 shared keys); occurrence is not reported as a result. [src: berdl_data_atlas]
