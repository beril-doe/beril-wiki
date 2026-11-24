---
type: "Concept"
description: "How the choice of detection evidence (eggNOG descriptions, specific or broad Pfam/InterPro domains, versioned domain IDs) changes marker-gene and defense prevalence estimates or produces false absences, and how to detect and recover them."
sources: ["summaries/lanthanide_methylotrophy_atlas__REPORT.md", "summaries/phage_defense_arsenal__REPORT.md", "summaries/phb_granule_ecology__REPORT.md", "summaries/pitfalls.md", "summaries/plant_microbiome_ecotypes__REPORT.md", "summaries/snipe_defense_system__REPORT.md"]
---
# Domain-based marker detection and annotation-method bias

Detection evidence changes prevalence estimates. Broad eggNOG descriptions inflate CRISPR counts from ~55 % to 96 % of species. [src: phage_defense_arsenal] Unversioned Pfam IDs return zero rows from a table that stores versioned IDs. [src: plant_microbiome_ecotypes] A table that lacks a Pfam produces false absences for 12 of 22 markers. [src: plant_microbiome_ecotypes] The SNIPE report adds a further case: the wrong Pfam family (PF01541) and low co-annotation of the true nuclease domain (PF13455) hide most SNIPE nuclease domains. [src: snipe_defense_system]

## Over-counting from broad descriptions and broad domains

Permissive text or domain matching inflates prevalence. In the same pangenome dataset, eggNOG description matches give 96 % species prevalence for CRISPR, against ~55 % using the specific Cas1 Pfam (PF01867). [src: phage_defense_arsenal] The report calls this an over-count of ~40 percentage points. [src: phage_defense_arsenal] It warns that any comparison of CRISPR prevalence across studies must state the detection method, because a 40-percentage-point gap on the same pangenome is an interpretation trap. [src: phage_defense_arsenal]

The same problem affects other markers:
- **DISARM:** The DrmB SNF2 helicase anchor (PF00176) is a widespread housekeeping-helicase family. It adds non-DISARM hits and biases the cluster distribution toward core, so the DISARM accessory-enrichment result is unreliable. [src: phage_defense_arsenal]
- **Retron:** Detection uses only RVT_1 (PF00078), a broad reverse-transcriptase Pfam. [src: phage_defense_arsenal] The Retron_stringent variant requires another narrow defense system in the species. That is a defense-context filter, not a retron-specificity filter. [src: phage_defense_arsenal] It is essentially a no-op (15,109 → 15,098; 11 species dropped), because narrow defense systems are near-universal among RVT_1 carriers. [src: phage_defense_arsenal] Results should be read as reverse-transcriptase candidates in defense-syndrome context, not characterized retron systems. [src: phage_defense_arsenal]
- **Prophage:** The prophage_ecology classifier over-counts by design, because integrase, holin and endolysin terms also match non-phage genes such as host integrases and cell-wall lysins. [src: phage_defense_arsenal] n_prophage_modules saturates at 7 for 35 % of species and is not a specific prophage count. [src: phage_defense_arsenal]

For broad Pfams (Retron RVT_1, DISARM PLD/SNF2, Gabija UvrD), species-level anchor-plus-context filtering was required. Specific markers (CRISPR Cas1, CBASS SAVED, BREX PglZ, Gabija OLD_TOPRIM_C) can be single-marker calls. [src: phage_defense_arsenal]

In a separate calibration, eggNOG Preferred_name='lanM' was unusable for lanmodulin and KO (KEGG ortholog) K02030 was non-specific for xoxJ. The report trusts the bakta product field. [src: lanthanide_methylotrophy_atlas] For lanmodulin, 0 genomes were called by both sources, 505 by eggNOG only and 62 by bakta only. [src: lanthanide_methylotrophy_atlas]

## Wrong family and domain-level detection: the SNIPE case

In the SNIPE report, the nuclease was first queried as canonical GIY-YIG (PF01541), which proved to be the wrong Pfam family. The SNIPE nuclease is PF13455 (Mug113, GIY-YIG clan CL0418). [src: snipe_defense_system] PF13455 and PF01541 are distinct Pfam families in the same clan. The paper's "GIY-YIG" label is at the superfamily level. [src: snipe_defense_system] The original paper named DUF4041 and GIY-YIG without Pfam accessions, which left room for this mistake. [src: snipe_defense_system] See [[entities/mug113-nuclease-domain-pf13455]] and [[entities/canonical-giy-yig-nuclease-family-pf01541]].

- Domain architecture of the *Escherichia coli* SNIPE protein A0A0A1A5Z2 (558 aa) was checked through InterPro and UniProt: PF13250 at positions 232–333 and PF13455 at positions 443–520. [src: snipe_defense_system] The binding domain (DUF4041 / SNIPE, DNA/TMP binding) is PF13250 at 232–333. [src: snipe_defense_system] The nuclease, Mug113 in the GIY-YIG clan, is PF13455 at 443–520. [src: snipe_defense_system] The nuclease domain is not PF01541. [src: snipe_defense_system]
- Canonical GIY-YIG is PF01541 (IPR000305), covering 68,148 proteins such as restriction enzymes and DNA repair proteins. It is not the SNIPE nuclease. [src: snipe_defense_system] The report therefore concludes that the 74,686 PF01541 clusters it found are not SNIPE nucleases. [src: snipe_defense_system]
- No gene cluster carried both DUF4041 and PF01541 in eggNOG Pfam annotations. [src: snipe_defense_system] The report treats this as genuine, because the two are different Pfam families, and not as an annotation artifact. [src: snipe_defense_system]
- The recommended search uses PF13250 (or the names DUF4041 / T5orf172) for the binding domain and PF13455 for the nuclease. [src: snipe_defense_system] DUF4041 is PF13250 and IPR025280, the diagnostic SNIPE domain, found in 4,572 gene clusters across 1,696 species in 33 bacterial and archaeal phyla. [src: snipe_defense_system] A separate domain-assignment table lists 1,612 proteins and 2,466 species for it. InterPro renamed IPR025280 "SNIPE associated domain". [src: snipe_defense_system]

Detection by domain name also has limits. Only 54 of 4,572 DUF4041 clusters carry the description "Meiotically up-regulated gene 113", so many SNIPE nuclease domains probably go undetected. [src: snipe_defense_system] The report adds that eggNOG Pfam annotations may miss divergent SNIPE homologues. [src: snipe_defense_system]

DUF4041 itself is not fully specific. Descriptions of the 4,572 clusters include T5orf172 (2,109), "Domain of unknown function (DUF4041)" (1,566), Histidine kinase (319) and seryl-tRNA aminoacylation (238). [src: snipe_defense_system] The report counts the first two, 3,675/4,572 clusters (80.4%), as bona fide SNIPE-family proteins. [src: snipe_defense_system] It reads the remaining ~20% (897 clusters) as likely annotation noise, with DUF4041 as a secondary domain. [src: snipe_defense_system] It states that a stricter description filter would leave the 86.7% accessory rate and taxonomic patterns not substantially affected. [src: snipe_defense_system] It cautions that some DUF4041 hits may be non-SNIPE proteins. [src: snipe_defense_system] COG (clusters of orthologous groups) categories for these clusters were D (cell cycle) 1,533, T (signal transduction) 1,118, J (translation) 1,066 and M (cell wall/membrane) 834. [src: snipe_defense_system] The report considers category M consistent with SNIPE's inner-membrane localization. [src: snipe_defense_system]

## False absences from identifier format and table coverage

Zero counts arose in the corpus from wrong query formats and from tables that lack the domain. [src: pitfalls, plant_microbiome_ecotypes] See also [[concepts/reference-database-table-choice-and-pfam-versioning-in-lakehouse-queries]] and [[concepts/annotation-source-disagreement-and-coverage]].

### Wrong accession or name format

- In snipe_defense_system, searching PFAMs for PF13250 returned 0 rows. Searching for DUF4041 returned 2,962. [src: pitfalls] The pitfalls entry lists zero co-occurrence hits for domains that should co-occur, or unexpected annotations, as symptoms of a wrong accession. [src: pitfalls] For [[entities/snipe]], DUF4041 is PF13250 (IPR025280), not PF13291 (ACT_4). [src: pitfalls] The nuclease is PF13455 (Mug113, GIY-YIG clan CL0418), not PF01541. [src: pitfalls]
- In phb_granule_ecology, the PHA (polyhydroxyalkanoate) synthase class analysis failed. All phaC clusters were classed "other_pfam", because eggNOG PFAMs use domain names rather than accession IDs (identifiers). [src: phb_granule_ecology] The report proposes mapping PF00561 to Abhydrolase_1 (Class I/II) and PF07167 to PhaC_N (Class III/IV). [src: phb_granule_ecology] The 11,792 phaC clusters would then be classifiable. [src: phb_granule_ecology]

### Versioned IDs and incomplete tables

The pitfalls entry first recorded 0 hits for 11 domains, such as PF00771, in [[entities/bakta-pfam-domains]]. It guessed at domain names or versioned accessions and left the correct format unresolved. [src: pitfalls] The plant_microbiome_ecotypes report then showed that the exact-ID query failed because the table stores versioned IDs such as PF00771.22. [src: plant_microbiome_ecotypes] The report gives PF13629.12 versus bare PF00771 as the example, and says this caused zero hits in the original NB02 query. [src: plant_microbiome_ecotypes] NB02 therefore found no Pfam hits and relied on gene names, KEGG KOs and product keywords. [src: plant_microbiome_ecotypes] The fix, in NB13 Cell 3, was a LIKE 'PF00771%' pattern. [src: plant_microbiome_ecotypes] LIKE 'PF00771%' patterns on the 10 Phase 2b marker Pfams recovered 19,364 domain hits across 7,962 species. [src: plant_microbiome_ecotypes] Only five of the 10 gave hits, and the other five returned 0. [src: plant_microbiome_ecotypes] The five with hits, as hits, species and core fraction, were:
- nitrogenase NifH PF00142: 6,632 hits, 4,040 species, 32.4% core. [src: plant_microbiome_ecotypes]
- cellulase GH5 PF00150: 6,898 hits, 3,234 species, 25.9% core. [src: plant_microbiome_ecotypes]
- pectate lyase 3 PF12708: 4,149 hits, 2,283 species, 24.6% core. [src: plant_microbiome_ecotypes]
- pectate lyase PF00544: 1,115 hits, 546 species, 20.8% core. [src: plant_microbiome_ecotypes]
- T6SS (type VI secretion system) VgrG PF05943: 570 hits, 343 species, 10.9% core. [src: plant_microbiome_ecotypes]

Versioning was not the whole story. An audit of all 22 marker Pfams across NB02 and NB10 found 12 completely absent from bakta_pfam_domains despite abundance in interproscan_domains. [src: plant_microbiome_ecotypes] The audit is in data/pfam_bakta_ips_audit.csv. [src: plant_microbiome_ecotypes] The silent-gap set is dominated by secretion-system components, with InterProScan (IPS) hit counts as follows.
- T3SS (type III secretion system): PF00771 18.6K, PF01313 13.6K, PF01514 15.0K, PF02579 16.8K, PF04610 15.6K, PF07916 8.4K, PF09599 0.3K, PF01312 22.0K. [src: plant_microbiome_ecotypes]
- T4SS (type IV secretion system): PF03135 11.0K, PF03743 17.5K. [src: plant_microbiome_ecotypes]
- T6SS: PF05936 (Hcp tube) 7.5K, PF04183 7.5K. [src: plant_microbiome_ecotypes]

The 10 Pfams present in bakta return only 10–35% of the IPS hit count, so they are systematically undercounted. [src: plant_microbiome_ecotypes] The report proposes that bakta uses a reduced core Pfam HMM profile set, while InterProScan uses the full Pfam-A release. [src: plant_microbiome_ecotypes] The same pattern shows in the defense markers: bakta_pfam_domains returns 0 hits for CRISPR Cas1 PF01867, against ~25K in InterProScan. [src: phage_defense_arsenal] Feasibility of 19 Pfam markers across 7 systems was tested against both tables. [src: phage_defense_arsenal] See [[entities/interproscan-domain-annotation]].

### Pfam LIKE recovery adds species where the two sources diverge

For nitrogen fixation and CWDEs, Pfam LIKE recovery added 4,217 species that gained at least one new marker InterProScan had missed. [src: plant_microbiome_ecotypes] Of these, 2,872 gained nitrogen fixation, 1,082 gained CWDE pectinase and 811 gained CWDE cellulase. [src: plant_microbiome_ecotypes] These are cases where bakta and InterProScan diverge. [src: plant_microbiome_ecotypes] So the gap runs in both directions: bakta recovered markers InterProScan had missed [src: plant_microbiome_ecotypes], while 12 of 22 marker Pfams were absent from bakta_pfam_domains but present in InterProScan. [src: plant_microbiome_ecotypes] This bears on bacterial nitrogen fixation nif genes.

### What the audit left unaffected

NB10 already used interproscan_domains signature_acc for T3SS, T4SS, T6SS and CWDE (cell wall degrading enzyme) markers. The report therefore treats its 280,193-hit recovery as correct and the refined cohort assignments as unaffected. [src: plant_microbiome_ecotypes] That recovery found 280,193 marker domain hits across 24,595 species. [src: plant_microbiome_ecotypes] It added 2,804 species with CWDE cellulase/pectinase domains (PF00150, PF00544) that the Phase 1 bakta-only search missed. [src: plant_microbiome_ecotypes] NB10's pipeline was unaffected by the Pfam gap, while Phase 1 NB02's bakta-only query caused the original zero-hit problem. [src: plant_microbiome_ecotypes] Phase 1 NB02 fell back to gene-name keyword matching, which is also unaffected. [src: plant_microbiome_ecotypes] The NB13 Cell 3 LIKE recovery confirmed rather than expanded the InterProScan secretion-system numbers. [src: plant_microbiome_ecotypes]

## Recovery approaches

- Compare detection sources on the same set of genomes, as in the lanmodulin source calibration. [src: lanthanide_methylotrophy_atlas]
- Use a specific domain as the anchor, or require anchor plus context for broad domains. [src: phage_defense_arsenal]
- Use prefix (LIKE) matching for versioned IDs, and map accessions to names where a table stores names. [src: plant_microbiome_ecotypes, phb_granule_ecology]
- Use interproscan_domains when bakta_pfam_domains lacks the Pfam. Treat bakta_pfam_domains as a supplement, not a substitute, and cross-check any Pfam query against the IPS table before concluding a function is missing. [src: plant_microbiome_ecotypes]
- Check accessions against the protein's own domain architecture, as done for the *E. coli* SNIPE protein. [src: snipe_defense_system]
- The phage_defense_arsenal report proposes PADLOC's MacSyFinder-style operon-level rules (multi-Pfam plus gene-order constraints) for Retron, DISARM and Gabija. [src: phage_defense_arsenal] It says housekeeping-helicase false positives inflate DISARM and reduce retron specificity. [src: phage_defense_arsenal] It predicts this would fix the DISARM result and sharpen syndrome and arms-race analyses without changing the qualitative conclusions. [src: phage_defense_arsenal]
- It also proposes a Millman-2020-Table-S1 retron-effector Pfam filter. The deviation from plan is recorded in RESEARCH_PLAN.md Revision History v2. [src: phage_defense_arsenal]

## Open Directions

- Re-run DISARM, Gabija and retron calls with multi-Pfam plus gene-order rules. Compare core, accessory and singleton fractions with the single-Pfam results, to test the prediction that the qualitative conclusions hold.
- Repeat the 96 % versus ~55 % CRISPR comparison for other defense systems. This would show which eggNOG description classes over-count.
- Tabulate stored ID formats (versioned, unversioned, names) for every domain table in the lakehouse, to prevent zero-hit queries.
- Test the reduced-profile-set explanation for the bakta gap by comparing the Pfam HMM versions and set sizes each tool uses.
- Rebuild the PHA synthase class analysis with the accession-to-name mapping, then check it against InterProScan.
- Search the 4,572 DUF4041 clusters for PF13455 with InterProScan instead of eggNOG, to test whether the 54 Mug113 co-annotations undercount SNIPE nuclease domains.
- Re-score nitrogen fixation and CWDE presence per species as the union of InterProScan and Pfam LIKE hits, to see how the 4,217 added species shift the core/accessory fractions.
