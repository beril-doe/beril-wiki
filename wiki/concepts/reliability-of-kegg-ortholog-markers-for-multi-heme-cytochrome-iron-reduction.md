---
type: "Concept"
description: "How misidentified or non-canonical KEGG orthologs corrupted an iron-reduction marker analysis and how a domain-and-motif multi-heme cytochrome detector replaces them; stops at marker-calling methodology."
sources: ["summaries/bacillota_b_subsurface_accessory__REPORT.md", "summaries/clay_confined_subsurface__REPORT.md", "summaries/discoveries.md"]
---
# Reliability of KEGG ortholog markers for multi-heme cytochrome iron reduction

This page covers how mismatched KEGG ortholog (KO) markers corrupted an iron-reduction (IR) marker analysis in the clay subsurface project, and how a triple-signal multi-heme cytochrome detector replaced them. The original markers were not iron-reduction genes. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface] After correction the cohort pattern reversed, and no cohort comparison was significant. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface] The evidence is a direct re-analysis, reported in the bacillota_b_subsurface_accessory and clay_confined_subsurface projects and in the discoveries digest. See [[entities/multi-heme-cytochrome-detector]] for the detector itself.

## Literature Context

The candidate papers describe multi-heme c-type cytochromes (MHCs) as the machinery of extracellular iron respiration. They also show how specific these proteins are. In Shewanella, dissimilatory iron reduction runs through six multiheme c-type cytochromes, and the outer membrane cytochromes OmcA and MtrC are the terminal reductases that pass electrons to iron (hydr)oxides [PMID 32978123](https://pubmed.ncbi.nlm.nih.gov/32978123/). The two proteins differ in function. In whole-cell attachment experiments with wild type and deletion mutants on goethite, OmcA gave rapid initial attachment, and MtrC gave a larger contact area and a longer-term interfacial reaction [PMID 32978123](https://pubmed.ncbi.nlm.nih.gov/32978123/). MtrA is a periplasmic decaheme cytochrome. Its hemes are bound through CXXCH motifs and distal histidines. In Shewanella sp. strain ANA-3, mutating six of nine proximal histidines in CXXCH lowered MtrA expression, and the proximal histidine mutants could not reduce ferrihydrite [PMID 22923588](https://pubmed.ncbi.nlm.nih.gov/22923588/). Distal histidine mutations had graded effects, and extracellular respiration could still proceed with them [PMID 22923588](https://pubmed.ncbi.nlm.nih.gov/22923588/). Multiheme cytochromes are also not limited to bacterial iron reducers. Members of the Methanoperedenaceae, grown in a freshwater sediment bioreactor, expressed several shared MHCs that were differentially expressed. This suggests different extracellular electron transfer pathways, in a community that coupled methane oxidation to Mn(IV) reduction [PMID 31988473](https://pubmed.ncbi.nlm.nih.gov/31988473/).

The corpus's CXXCH-motif criterion is **consistent with** this literature. The heme-binding CXXCH motif is functionally important in MtrA, because changes at proximal histidines abolished ferrihydrite reduction [PMID 22923588](https://pubmed.ncbi.nlm.nih.gov/22923588/). That supports using motif counts, together with the PFAM domains PF02085 and PF22678, as a marker for multi-heme cytochrome iron-reduction potential. The candidate papers do not test the detector itself. They do not evaluate its threshold of at least 4 CXXCH motifs, its false-positive rate, or PF22678, a nitrite-reductase family. Those points stay open, as the hub's Open Directions say.

The corpus's main claim is that K07811, K17324 and K17323 encode TMAO reductase and glycerol ABC transport proteins, not iron-reduction genes. That claim is **novel** relative to these papers, which do not address KEGG ortholog assignment. The papers do give a biological reason why a KO-based approach would be fragile. Shewanella iron reduction depends on a specific set of multiheme cytochromes with distinct roles, namely OmcA, MtrC and MtrA [PMID 32978123](https://pubmed.ncbi.nlm.nih.gov/32978123/) [PMID 22923588](https://pubmed.ncbi.nlm.nih.gov/22923588/). The hub reports that KEGG has no canonical KO for these omcS and mtr cytochromes. Substituting unrelated KOs would therefore miss them. The same reasoning suggests that the corrected cohort rates, which showed no significant differences, should be read cautiously. The anchor_deep cohort has only n=9, and the candidate papers say nothing about the clay subsurface cohorts. They are also mechanistic or single-system studies, and two of them are in vitro or laboratory-strain work. They cannot confirm or contradict the corpus's cohort-level results.

See [[concepts/limits-of-keyword-and-marker-based-functional-annotation]] and [[entities/multi-heme-cytochrome-detector]].

## What went wrong with the original markers

The merged clay_confined_subsurface project (PR #231) used K07811, K17324 and K17323 as IR markers in its H3 porewater-versus-rock-attached test. [src: discoveries, bacillota_b_subsurface_accessory] These KOs encode TMAO reductase, glycerol ABC (ATP-binding cassette) transport ATP-binding protein, and glycerol ABC transport permease. None is an iron-reduction gene. [src: clay_confined_subsurface, discoveries]

The bacillota_b_subsurface_accessory report gives the KOfam thresholds as 1336.87 for K07811, 363.93 for K17324 and 318.27 for K17323. [src: bacillota_b_subsurface_accessory] The discoveries digest gives them as 1336, 363 and 318. [src: discoveries]

KEGG has no canonical KO for the Geobacter omcS or Shewanella mtr operon multi-heme outer-surface cytochromes. The original analysis therefore substituted unrelated genes without noticing. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface, discoveries]

The bacillota_b_subsurface_accessory report attributes the "Mitzscherling rock-attached signature in shallow clay" to two things acting together. One was the mismatched gene identifiers (IDs). The other was the standard eggNOG-mapper threshold, which filters on sequence similarity and not on KO biological identity. [src: bacillota_b_subsurface_accessory]

A sister project (NB04) independently flagged the same problem, as cited by the clay_confined_subsurface report. KEGG KO assignment is unreliable for niche genes without canonical KOs, such as omcS, mtrCAB and MGE-borne resistance cassettes. KEGG-based marker mining for them will silently substitute unrelated functions. [src: clay_confined_subsurface]

## The replacement detector

A genome scores positive for multi-heme cytochrome IR potential if any of three signals is present. [src: bacillota_b_subsurface_accessory] The signals are:

- PFAM PF02085 (Cytochrom_CIII, multi-heme c-type). [src: bacillota_b_subsurface_accessory]
- PFAM PF22678 (Cytochrom_c_NrfB-like, multi-heme nitrite reductase). [src: bacillota_b_subsurface_accessory]
- A CXXCH heme-binding motif count of at least 4 in gene_cluster.faa_sequence, a canonical method since Methé et al. 2003 on Geobacter. [src: bacillota_b_subsurface_accessory]

The clay_confined_subsurface report and the discoveries digest both describe this same three-signal detector. [src: clay_confined_subsurface, discoveries] The bacillota_b_subsurface_accessory report proposes it as a reusable KBase Data Lakehouse pattern for cases where KEGG KO assignment is unreliable. [src: bacillota_b_subsurface_accessory]

## Effect on cohort rates

The correction changed the cohort rates substantially, and the direction differed by cohort. The headline correction table has 5 rows. [src: bacillota_b_subsurface_accessory]

- anchor_deep (Mont Terri Opalinus + bentonite, n=9): original wrong-KO rate 11.1% (1/9), corrected rate 55.6% (5/9). [src: bacillota_b_subsurface_accessory, clay_confined_subsurface]
- anchor_shallow (Coalvale + Cerrado + agricultural, n=30): original 50.0% (15/30), corrected 40.0% (12/30). [src: bacillota_b_subsurface_accessory, clay_confined_subsurface]
- soil_baseline (n=149): original 20.1% (30/149), corrected 40.9% (61/149). [src: bacillota_b_subsurface_accessory, clay_confined_subsurface]

The discoveries digest reports the same change as rounded figures: anchor_deep 56% (was 11%). [src: discoveries]

## Consequences for the conclusions

The original shallow >> deep pattern (50% vs 11%) reversed. After correction, shallow (40%) is lower than deep (56%). [src: bacillota_b_subsurface_accessory] No comparison is significant, and all Fisher p values are at least 0.46. [src: bacillota_b_subsurface_accessory, clay_confined_subsurface] Multi-heme cytochrome content is similar across the three cohorts and similar to the soil baseline (41%). [src: bacillota_b_subsurface_accessory]

Other tests in the report are also null. IR_complete occurred in 1 of 9 anchor_deep genomes versus 30 of 140 soil_baseline genomes (Fisher OR=0.46, p_BH=0.69). [src: clay_confined_subsurface] The IR depletion test against the rock-attached null gave n=9, observed=1, expected=0.63, p=0.87. [src: clay_confined_subsurface]

The clay_confined_subsurface correction notice says its H3 IR-side analysis, the anchor_deep (1/9) versus anchor_shallow (15/30) comparison, was driven by misidentified iron-reduction markers. [src: clay_confined_subsurface] It states that the IR-side narrative, that the clay cohort diverges from the Mitzscherling rock-attached community because shallow clay is IR-rich, is withdrawn. [src: clay_confined_subsurface]

Before correction, that report had claimed a 3.7-fold IR enrichment in shallow clay versus the broader soil baseline (p=0.0025). [src: clay_confined_subsurface] The cited claims do not separately address whether that soil-baseline comparison survives the correction.

The porewater-bias headline still holds through sulfate reduction (SR) alone. The rock-attached versus porewater dichotomy is half-supported (SR side) and half-unsupported (IR side). [src: clay_confined_subsurface] See [[concepts/iron-and-sulfate-reduction-signatures-in-clay-subsurface-porewater-versus-rock-attached-communities]] and [[concepts/limits-of-keyword-and-marker-based-functional-annotation]].

## Open Directions

- Validate the triple-signal detector against genomes with known iron-reducing phenotypes, such as Geobacter and Shewanella. This would estimate its false-positive rate, which matters because PF22678 is a nitrite-reductase family.
- Test each signal separately (PF02085, PF22678, CXXCH count ≥4). This would show which signal drives the cohort rates and whether the threshold of 4 is arbitrary.
- Re-test the shallow-clay versus soil-baseline IR enrichment with the corrected detector, to settle whether the earlier 3.7-fold result survives.
- Audit other KO-based markers in the corpus for the same mismatch, by checking each KO's name against its intended function.
- Increase the anchor_deep sample beyond n=9. The null comparisons have low power, so absence of significance is not evidence of equality.
