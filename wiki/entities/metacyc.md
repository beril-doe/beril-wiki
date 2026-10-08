---
type: "Dataset"
description: "MetaCyc is a curated metabolic-pathway database whose class hierarchy, distributed through ModelSEEDDatabase, was used in this corpus to categorize HUMAnN3 pathway outputs for theme-enrichment tests."
sources: ["summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md"]
---
# MetaCyc

**Type:** dataset. In this corpus the MetaCyc pathway class hierarchy is not used directly from MetaCyc but from a provenance file shipped with ModelSEEDDatabase, `MetaCyc_Pathways.tbl` [src: discoveries].

MetaCyc is a curated database of metabolic pathways with a curator-validated class hierarchy. In this corpus its pathway classes were taken from the [[entities/modelseed]] database file `/global_share/KBaseUtilities/ModelSEEDDatabase/Biochemistry/Aliases/Provenance/MetaCyc_Pathways.tbl`, and its pathway identifiers (e.g. PWY-5920) are the units reported by [[entities/humann3]] pathway profiling [src: discoveries, ibd_phage_targeting].

## Use in the IBD pathway analysis

The first Pillar 3 notebook (NB07a) of [[summaries/ibd_phage_targeting__REPORT]] ran a within-IBD-substudy meta-analysis of Crohn's disease (CD) versus non-IBD samples on `fact_pathway_abundance` (HUMAnN3 MetaCyc, CMD_IBD only). Three substudies were robust (HallAB_2017, IjazUZ_2017, NielsenHB_2014) and one was boundary (LiJ_2014, nonIBD = 10). VilaAV_2018 was excluded (CD = 216, nonIBD = 0). After a 10%-prevalence filter, 575 unstratified MetaCyc pathways were reduced to 409 [src: ibd_phage_targeting].

This differential-abundance (DA) analysis found 52 CD-up MetaCyc pathways (FDR<0.10, |effect|>0.5), where FDR is the false discovery rate. The permutation null mean was 0.077. It also found 137 pathway–pathobiont attribution pairs at |ρ_meta|>0.4. The report does not agree with itself about which pair ranks first. Its overview names heme biosynthesis (PWY-5920) ↔ [[entities/escherichia-coli]] at ρ=0.640 as the top hit and reads it as recapitulating AIEC biology. NB07a's ranked attribution table, however, puts heme biosynthesis from glycine at rank 19 (ρ_meta 0.640) and puts GLYOXYLATE-BYPASS (glyoxylate cycle) at rank 1 (ρ_meta 0.797). The heme pair is therefore the overview's headline example, not the strongest correlation [src: ibd_phage_targeting].

## Name regex versus MetaCyc classes

The v1.7 H3a (b) verdict, "FAIL — degenerate", came from a regex on pathway names. Only 44/409 background pathways matched the 7 a-priori category patterns. PWY-5920 (superpathway of heme biosynthesis from glycine) was silently put in "0_other" because "heme" / "iron" were not in the regex set. The v1.8 retest replaced the regex with structured MetaCyc class assignments and expanded to 12 IBD-relevant themes, including iron/heme acquisition, fat metabolism / glyoxylate, anaerobic respiration, purine/pyrimidine recycling, and aromatic AA / chorismate / indole [src: ibd_phage_targeting].

The central digest explains the miss. A regex on the PWY-5920 name does not match "iron", but MetaCyc's curator-validated class hierarchy places PWY-5920 under `HEME-SYN`, `Heme-b-Biosynthesis`, `Cofactor-Biosynthesis` and `Tetrapyrrole-Biosynthesis`. The v1.7 "0_other" bucket was hiding 15+ heme/iron pathways [src: discoveries].

In the digest's account of v1.8, 357/409 (87 %) of pathways had MetaCyc class data and 262/409 (64 %) were assigned to ≥ 1 IBD theme. The analysis used a per-theme [[entities/fishers-exact-test]] (CD-up × in-theme) with [[entities/benjamini-hochberg-fdr]] correction across 12 themes. The verdict was SUPPORTED: iron/heme acquisition was the dominant CD-up theme (OR = 8.1, FDR 7e-6; 15 of 52 CD-up pathways) [src: discoveries].

The project report states that the MetaCyc class hierarchy gave H3a (b) SUPPORTED. It gives the hierarchy's coverage as 90 % of 575 HUMAnN3 pathways, and elsewhere as 514/575 pathways categorized across 12 themes. Iron/heme acquisition was the dominant CD-up theme (OR=8.1, FDR 7e-6; 15 of 52 CD-up pathways), an 8.1× enriched dominant theme. Two other themes were also enriched: *H. hathewayi* ([[entities/hungatella-hathewayi]]) purine/pyrimidine recycling (OR=4.9) and TMA/choline (OR=9.3). The verdict reversed on the same data and the same DA pipeline, driven by ontology choice. The report calls the iron/heme result causally consistent with the broader IBD-iron literature. Within this corpus it rests on one project's cohort analysis. The result feeds iron acquisition and pathobiont expansion [src: ibd_phage_targeting].

## Recommended default for category enrichment

The report calls v1.7 → v1.8 a major scientific reversal driven entirely by category-schema choice. It encodes the lesson as plan norm N17: prefer an ontology / class hierarchy over name-pattern regex for pathway / gene / metabolite categorization wherever feasible, and keep regex as a sensitivity check. It states that ModelSEEDDatabase ships a usable MetaCyc class hierarchy with 90 % coverage of HUMAnN3 outputs, which should be the default for any pathway category-enrichment test in BERIL projects [src: ibd_phage_targeting]. This is the main case behind [[concepts/ontology-and-category-schema-sensitivity]].

The central digest also records that ModelSEEDDatabase ships a usable MetaCyc class hierarchy at the `MetaCyc_Pathways.tbl` path, with 90 %+ coverage of HUMAnN3 outputs [src: discoveries].

## Coverage figures as reported

The sources state the coverage of the MetaCyc class hierarchy differently, depending on the denominator, and the figures are not reconciled here. The digest gives 357/409 (87 %) of prevalence-filtered pathways with class data and 90 %+ coverage of HUMAnN3 outputs [src: discoveries]. The project report gives 90 % coverage of 575 HUMAnN3 pathways and 514/575 pathways categorized [src: ibd_phage_targeting].
