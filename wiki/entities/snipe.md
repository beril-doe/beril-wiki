---
type: "Gene_Or_Pathway"
description: "Anti-phage defense protein with DUF4041 and a GIY-YIG nuclease domain that targets the ManYZ mannose transporter pore."
sources: ["summaries/discoveries.md", "summaries/snipe_defense_system__REPORT.md"]
aliases: ["DUF4041", "IPR025280", "PF13250", "SNIPE associated domain", "T5orf172", "T5orf172 family"]
---
# SNIPE

SNIPE is an anti-phage defense protein that carries a DUF4041 domain (also called PF13250, IPR025280, T5orf172 family, or "SNIPE associated domain") and a GIY-YIG nuclease domain. It targets the ManYZ mannose transporter pore. [src: discoveries, snipe_defense_system] The evidence on this page comes from a survey of domain annotations in the KBase Data Lakehouse pangenome and from InterPro/UniProt checks. [src: discoveries] One archaeal homologue in the Fitness Browser has fitness data. [src: discoveries, snipe_defense_system]

## Key facts

- Function: Saxton et al. 2026 showed that SNIPE constitutively localizes to the inner membrane and cleaves phage DNA as it passes through the ManYZ mannose transporter pore. [src: snipe_defense_system] ManYZ is the mannose transporter that phage lambda exploits for DNA injection, not a general sugar transporter. [src: discoveries] SNIPE therefore acts at the adsorption/injection step. [src: snipe_defense_system]
- Names: InterPro renamed IPR025280 from "Domain of unknown function DUF4041" to "SNIPE associated domain". [src: snipe_defense_system] DUF4041 is the report's diagnostic SNIPE domain. [src: snipe_defense_system]
- Trade-off: The report states that SNIPE-bearing strains keep full ManYZ function and gain phage resistance without the metabolic cost of *man* knockouts. [src: snipe_defense_system] See [[concepts/phage-resistance-versus-metabolic-cost-trade-off-at-receptor-transporters]].

## Domain architecture

The *Escherichia coli* SNIPE protein A0A0A1A5Z2 is 558 aa. InterPro annotates PF13250 at positions 232–333 and PF13455 at positions 443–520. [src: snipe_defense_system, discoveries] The PF13250 region is the DNA/TMP-binding domain. [src: snipe_defense_system]

The nuclease domain belongs to Pfam PF13455 (Mug113), not PF01541, the canonical GIY-YIG restriction enzyme/DNA repair family. Both families sit in the GIY-YIG clan CL0418 but are distinct. [src: discoveries] See [[entities/mug113-nuclease-domain-pf13455]] and [[entities/canonical-giy-yig-nuclease-family-pf01541]]. The SNIPE paper names the nuclease only as "GIY-YIG" at the superfamily level and cites no Pfam accessions. [src: discoveries] No gene cluster shows DUF4041 together with PF01541. The report attributes this to distinct nuclease family identity, not an annotation artifact. [src: discoveries] This matters for [[concepts/domain-based-marker-detection-and-annotation-method-bias]].

## Distribution

A survey of the KBase Data Lakehouse 293K-genome pangenome found DUF4041 in 4,572 gene clusters across 1,696 species and 33 phyla. [src: discoveries, snipe_defense_system] The report notes this is far more than the >500 homologues reported in Saxton et al. 2026. [src: snipe_defense_system] SNIPE homologues were identified by the DUF4041 Pfam domain in eggNOG annotations. [src: snipe_defense_system]

Of these genes, 86.7% are accessory or singleton, consistent with mobile defense island carriage. [src: discoveries, snipe_defense_system] The report reads the patchy distribution across many phyla and families as support for horizontal gene transfer. [src: discoveries] See [[concepts/pan-bacterial-prevalence-phylum-distribution-and-mobility-of-anti-phage-defense-systems]].

Among the DUF4041 clusters, 2,109 are described as T5orf172, the gene family name for DUF4041, and 1,566 as "Domain of unknown function (DUF4041)". [src: snipe_defense_system] The InterPro/UniProt IPR025280 dataset has 1,612 SNIPE proteins across 1,373 species. [src: snipe_defense_system] A separate domain-assignment table lists 1,612 proteins and 2,466 species for DUF4041. [src: snipe_defense_system] The two species counts differ and the claims do not reconcile them.

SNIPE-bearing species occupy statistically distinct environmental niches in 22/64 AlphaEarth dimensions (p < 0.05, Bonferroni-corrected). [src: snipe_defense_system] See [[concepts/environmental-niche-association-of-defense-system-carriers]].

## Fitness Browser homologue

The Fitness Browser contains one archaeal SNIPE protein, from *Methanococcus maripaludis* JJ (locus MMJJ_RS01635). [src: discoveries] It carries PF13250, PF13455 and PF10544 (DUF2525). [src: discoveries] It has 129 experiments of fitness data, described as the first SNIPE homologue with genome-wide knockout phenotypes. [src: discoveries, snipe_defense_system] Only *M. maripaludis* has the full two-domain architecture in the Fitness Browser. [src: snipe_defense_system] See [[entities/methanococcus-maripaludis]] and [[concepts/fitness-data-coverage-gaps-for-defense-genes]].

## Klebsiella

SNIPE was detected in *Klebsiella*, a key phage therapy target. [src: snipe_defense_system] The PhageFoundry Klebsiella genome browser has 1 DUF4041 annotation covering 3 proteins of 558 aa, the same length as *E. coli* SNIPE, and 4,619 PTS_EIIC (PF02378/ManY family) annotations. [src: discoveries] The three proteins are JJW41_17025, KFB13_RS08150 and KFB31_RS01490. Their length strongly suggests full-length two-domain SNIPE proteins. [src: snipe_defense_system] This is inferred from length and not from domain calls. *Klebsiella* is the only PhageFoundry species with both SNIPE and the ManX-family PTS domain PF00358. [src: discoveries] The report proposes that SNIPE could affect phage therapy efficacy in this pathogen. [src: discoveries] See [[entities/klebsiella-pneumoniae]] and [[concepts/adsorption-receptors-versus-defense-systems-as-determinants-of-phage-host-range]].

## Sources

See [[summaries/snipe_defense_system__REPORT]] and [[summaries/discoveries]].

## Open Directions

- Run the Fitness Browser *M. maripaludis* MMJJ_RS01635 experiments to see which conditions give a phenotype.
- Confirm the Klebsiella proteins' domain architecture with direct domain calls.
- Reconcile the 1,373 and 2,466 species counts.
