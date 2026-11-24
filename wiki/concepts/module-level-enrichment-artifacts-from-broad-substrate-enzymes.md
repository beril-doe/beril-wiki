---
type: "Concept"
description: "How pathway-module enrichment can be driven by generic or broad-substrate KOs, and how per-KO step dissection (e.g. limonene degradation) corrects false-positive pathway calls."
sources: ["summaries/neon_mag_functional_discovery__REPORT.md"]
---
# Module-level enrichment artifacts from broad-substrate enzymes

Module-level pathway enrichment can be driven by a few generic or broad-substrate KOs (KEGG orthologs). [src: neon_mag_functional_discovery] The evidence here comes from one report, [[summaries/neon_mag_functional_discovery__REPORT]], on NEON metagenome-assembled genomes (MAGs). Its per-step dissection of limonene degradation showed that the limonene framing is largely an artifact. [src: neon_mag_functional_discovery]

## The limonene case

The KEGG-module enrichment in NB04b first flagged M00322 (limonene degradation, limonene to β-ketoadipate) as field-only-enriched. [src: neon_mag_functional_discovery] Per-step dissection showed that the limonene-degradation framing is largely an artifact. [src: neon_mag_functional_discovery] The module enrichment hid heterogeneity in which pathway step each MAG encodes. [src: neon_mag_functional_discovery] The report dissected KEGG ko00903 using five informative KOs. [src: neon_mag_functional_discovery]

Two of those KOs explain the artifact:
- K00128 is an NAD-dependent aldehyde dehydrogenase (EC 1.2.1.3), a housekeeping enzyme present in essentially every aerobic organism. [src: neon_mag_functional_discovery]
- K14731 is ε-lactone hydrolase (EC 3.1.1.83), a broad-substrate late-pathway enzyme that opens lactone intermediates and is not limonene-exclusive. [src: neon_mag_functional_discovery]

### Classes of MAG by step content

| Class | MAGs | Meaning |
|---|---|---|
| GENERIC_ONLY (K00128 only) | 43 | False-positive limonene-degrader signal; includes all 14 Planktothrix and Dolichospermum MAGs [src: neon_mag_functional_discovery] |
| LATE_ONLY (K14731 ± K00128) | 15 | Can process lactone intermediates but cannot initiate limonene oxidation [src: neon_mag_functional_discovery] |
| PARTIAL_NO_HYDROLASE | 2 | Both Bradyrhizobium; entry-point monooxygenase plus lactone hydrolase, lacking the diol-forming step [src: neon_mag_functional_discovery] |
| OTHER (K10533 only) | 1 | A 13-2-20CM-66-19 MAG with the Step 2 hydrolase only [src: neon_mag_functional_discovery] |
| ENTRY_ONLY (K14733 only) | 1 | A Rubrivivax MAG with the entry point and nothing downstream [src: neon_mag_functional_discovery] |
| FULL | 1 | A Mycobacterium MAG with 5 KOs [src: neon_mag_functional_discovery] |

The LATE_ONLY MAGs are concentrated in soil Acidobacteriota: Sulfotelmatobacter (4), Palsa-465 (3), Palsa-1447 (3), Acidoferrum (1), 13-2-20CM-66-19 (1), Terracidiphilus (1), Rhizomicrobium (1), Palsa-295 (0, generic-only), plus Rubrivivax (1). [src: neon_mag_functional_discovery]

## Consequences for biological claims

**Cyanobacteria.** The M00322 enrichment contribution from 14 Planktothrix and Dolichospermum MAGs at NEON PRLA (Prairie Lake, ND) was driven entirely by K00128. [src: neon_mag_functional_discovery] These MAGs carry none of K14733, K07381, K07382, or K14731. [src: neon_mag_functional_discovery] The report notes that this agrees with the literature, which frames these organisms only as terpene producers. [src: neon_mag_functional_discovery]

**Palsa-peat Acidobacteriota.** The report downgraded its novel limonene-degradation claim for these MAGs. Their field-only KO is K14731, which also acts on caprolactam, various Baeyer-Villiger products and other ε-lactones. [src: neon_mag_functional_discovery] None of the novel-genus MAGs carry the entry-point monooxygenase K14733. [src: neon_mag_functional_discovery] They cannot initiate limonene catabolism. They can only process ring-opened intermediates supplied by other community members or by natural plant-litter lactones. [src: neon_mag_functional_discovery]

**Established degraders.** The only MAG with the full canonical pathway is a [[entities/mycobacterium|Mycobacterium]] MAG. Mycobacterium has been a cultivated limonene-biocatalysis workhorse for about 20 years, so the report finds no lineage novelty. [src: neon_mag_functional_discovery] [[entities/bradyrhizobium|Bradyrhizobium]] MAGs carry K14733 at field abundance comparable to cultured representatives. The report flags them as additional soil biocatalyst candidates but not as novel relative to the cultured accessory. [src: neon_mag_functional_discovery] Their partial-pathway KOs are also present in the cultured Bradyrhizobium pangenome, so they are not field-only. [src: neon_mag_functional_discovery]

## General lessons

The report states a methodological rule: cross-check module-level enrichment with per-KO step assignment before drawing biological conclusions. Broad-substrate housekeeping enzymes, such as an aldehyde dehydrogenase shared by dozens of pathways, can drive spurious module enrichment alone. [src: neon_mag_functional_discovery]

A second, related caution concerns universal cellular machinery. Habitat enrichment of such modules usually reflects a taxonomic-abundance shift, for example Cyanobacteria over-represented in water. It does not usually reflect a novel functional capability. [src: neon_mag_functional_discovery] See [[concepts/habitat-and-soil-chemistry-structuring-of-metagenomic-functional-gene-content]].

A third artifact comes from how "field-only" is defined. Ribosomal protein KOs appear field-only in 52 of 54 cases. The report attributes this to the [[entities/kbase-ke-pangenome]] `is_core = false` definition. Ribosomal genes can be classed as accessory when they vary across species within a genus. [src: neon_mag_functional_discovery] See [[concepts/field-only-accessory-gene-content-absent-from-cultured-pangenomes]].

## Open Directions

- Re-run the module enrichment for other KEGG modules with per-KO step assignment. Flag modules where one KO accounts for most of the signal. This would show how often the limonene pattern recurs.
- Weight each KO by how many pathways it appears in, and test whether enrichment survives after removing the top shared KO. This would give a systematic filter for housekeeping-driven hits.
- Check whether the K14731-carrying Acidobacteriota MAGs encode other lactone-processing or plant-litter degradation genes. This would test the proposal that they use supplied lactones.
- Redefine "core" for ribosomal and other universal KOs in the field-only comparison. This would show how many of the 52 of 54 hits disappear.
