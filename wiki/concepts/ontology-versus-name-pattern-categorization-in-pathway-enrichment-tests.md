---
type: "Concept"
description: "How the choice of category schema (regex on pathway names versus a curated class hierarchy) can reverse a pathway-enrichment verdict on identical data; stops at the specific biology of the enriched themes."
sources: ["summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md"]
---
# Ontology versus name-pattern categorization in pathway enrichment tests

In the ibd_phage_targeting project, one test gave opposite verdicts on identical data depending on how pathways were sorted into categories. A regex on pathway names gave FAIL, and a curated MetaCyc class hierarchy gave SUPPORTED. The evidence is one project and one test, but the report states the data, the differential-abundance pipeline and the statistics were the same. [src: discoveries, ibd_phage_targeting] Related pages: [[entities/metacyc-pathway-class-hierarchy]], [[summaries/ibd_phage_targeting__REPORT]], [[summaries/discoveries]].

## The test and the two schemas

The test, H3a (b), asked whether pathways higher in Crohn's disease (CD-up) concentrate in inflammatory bowel disease (IBD) mechanism themes. The verdict flipped with the category schema, while differential-abundance outputs, statistical test and nulls stayed the same. [src: discoveries] The report attributes the reversal to ontology choice. [src: ibd_phage_targeting]

### v1.7: regex on pathway names

The v1.7 schema used 7 a-priori IBD categories matched by regex on descriptive names. [src: discoveries] These categories were bile-acid, mucin, sulfide, TMAO, eut/pdu, polyamine and AA-decarb. [src: ibd_phage_targeting] They matched 44 of 409 prevalence-filtered pathways. [src: discoveries] Only 3 of 52 CD-up pathways fell in the set. [src: discoveries] The test had about zero power, and the null was also at 100% top-3 concentration. [src: ibd_phage_targeting] The verdict was FAIL, structurally degenerate. [src: discoveries, ibd_phage_targeting]

Species-resolved analysis (NB07b) did not rescue it. H3a (b) was NOT SUPPORTED for all 6 Tier-A core species, and the report calls this verdict structural, not biological. [src: ibd_phage_targeting] *Hungatella hathewayi* had only 1 of 16 CD-up pathways in the 7-category set. [src: ibd_phage_targeting] *Mediterraneibacter gnavus* had 0 CD-up and 0 CD-down pathways and was untestable. [src: ibd_phage_targeting]

### v1.8: curated class hierarchy

The v1.8 schema used the MetaCyc class hierarchy from ModelSEEDDatabase's MetaCyc_Pathways.tbl, with a 12-theme IBD overlay. [src: discoveries, ibd_phage_targeting] Of 409 pathways, 357 (87%) had class data and 262 (64%) were assigned to at least one theme. [src: discoveries] Each theme got a Fisher's exact test of CD-up status against in-theme status, with Benjamini-Hochberg false discovery rate (BH-FDR) control across the 12 themes. [src: discoveries] A theme counted as supported at FDR < 0.10 and odds ratio (OR) > 1.5. [src: ibd_phage_targeting]

The verdict became SUPPORTED. Iron/heme acquisition was the dominant CD-up theme (OR = 8.1, FDR 7e-6; 15 of 52 CD-up pathways). [src: discoveries, ibd_phage_targeting] The report's cross-project summary describes the v1.8 coverage as 514/575 pathways in 12 themes. [src: ibd_phage_targeting] That differs from the 357/409 count above, and the quotes do not say why. [src: discoveries, ibd_phage_targeting]

Not every theme gained support. Anaerobic respiration (OR 1.36, FDR 1.0) and mucin/glycan/host (OR 1.06, FDR 1.0) were not enriched. [src: ibd_phage_targeting] The unstratified signal did not load preferentially on the classical IBD categories. [src: ibd_phage_targeting] It instead captured broader themes: heme/iron, glyoxylate, fat metabolism and allantoin/purines. [src: ibd_phage_targeting]

## Why the regex missed iron

The regex did not match "iron" in "PWY-5920: superpathway of heme biosynthesis from glycine", so the pathway fell into "0_other". [src: discoveries, ibd_phage_targeting] That bucket hid 15+ heme/iron pathways. [src: discoveries] MetaCyc places PWY-5920 under HEME-SYN, Heme-b-Biosynthesis, Cofactor-Biosynthesis and Tetrapyrrole-Biosynthesis. [src: discoveries] The iron/heme result converged with E. coli Yersiniabactin/Enterobactin MIBiG matches, the NB07a attribution of heme biosynthesis to E. coli, and adherent-invasive E. coli (AIEC) iron-acquisition literature. [src: discoveries] See also [[concepts/iron-acquisition-as-an-aiec-specific-genomic-specialization-in-crohn-s-disease]].

## What the reversal does and does not mean

The report treats the v1.7 FAIL as technically correct for its schema but not a scientific refutation. A "structurally degenerate" verdict is a prompt to fix the schema. [src: discoveries] The refutation holds only for the v1.7 category set. It does not mean no compositional themes exist. [src: ibd_phage_targeting] NB07a rated H3a v1.7 as partially supported, with 2 of 3 clauses passing. [src: ibd_phage_targeting]

The report proposes broadening the literature-derived categories to alternative-electron-acceptor metabolism, iron acquisition and fat utilization in inflammation. [src: ibd_phage_targeting] It also suggests housekeeping pathways shared across genera may dominate the unstratified level. [src: ibd_phage_targeting] This is a hypothesis.

## Resulting rule

Plan norm N17 prefers curator-validated ontologies or class hierarchies over name-pattern regex for pathway, gene or metabolite category enrichment. Regex stays as a sensitivity check. [src: discoveries, ibd_phage_targeting] ModelSEEDDatabase's MetaCyc hierarchy covers 90%+ of HUMAnN3 outputs, and the report recommends it as the default. [src: discoveries, ibd_phage_targeting] The v1.8 figure is 90% of 575 pathways. [src: ibd_phage_targeting] KEGG BRITE and the Gene Ontology (GO) biological-process subontology are named as analogues for KEGG/EC-level data. [src: discoveries] This fits the wider discipline in [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]].

## Open Directions

- Re-run v1.8 with a regex-derived category set as a sensitivity check, to see which themes are robust to schema (closes the single-schema gap).
- Apply the hierarchy test species by species (NB07b) to see whether the iron/heme signal is attributable to specific species such as E. coli.
- Test KEGG BRITE or GO biological-process categories on KEGG/EC-level data, to check whether the reversal generalizes beyond MetaCyc.
- Reconcile the 357/409 and 514/575 coverage counts by documenting the denominators.
- Test the proposed broadened literature categories (electron acceptors, iron, fat use) against the hierarchy result.
