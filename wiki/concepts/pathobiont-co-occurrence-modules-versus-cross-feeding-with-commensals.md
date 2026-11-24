---
type: "Concept"
description: "Whether Crohn's-associated pathobionts co-cluster in single ecological modules, and whether coupling to butyrate-producing commensals reflects cross-feeding or shared environment; covers consequences for multi-target cocktails and collateral depletion."
sources: ["summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md"]
---
# Pathobiont co-occurrence modules versus cross-feeding with commensals

This page covers whether Crohn's-associated pathobionts co-cluster in single ecological modules, and whether coupling to butyrate-producing commensals reflects cross-feeding or shared environment. In ibd_phage_targeting, 4–5 of 6 actionable Tier-A candidates fell into one module in every subnet. [src: ibd_phage_targeting] Coupling to Anaerostipes caccae was first read as consistent with cross-feeding, and paired metabolite data later did not support that reading, favoring shared environment. [src: ibd_phage_targeting] Both results are correlational. See [[summaries/ibd_phage_targeting__REPORT]] for the full report.

## Do pathobionts co-cluster in one module?

Yes in every subnet tested, although the raw average was below the plan's bar. Centered log-ratio (CLR) plus Spearman plus Louvain networks on E1_all, E1_CD, E3_all and E3_CD gave 3–7 modules per subnet. [src: ibd_phage_targeting] In every subnet, 4–5 of the 6 actionable Tier-A candidates fell into a single pathobiont module of 57–84 nodes. [src: ibd_phage_targeting] The raw mean of actionable candidates per module was 1.38 on E1_all + E3_all, below the plan's ≥ 2 bar, so the signal is concentrated in one module rather than spread evenly. [src: ibd_phage_targeting] The report reads this as one ecologically linked co-occurrence module within Crohn's disease (CD) ecotypes. [src: ibd_phage_targeting]

Membership varies by ecotype. Flavonifractor plautii is in the main pathobiont module in E1 but in the generalist module in E3. [src: ibd_phage_targeting] Escherichia coli is in the pathobiont module only in E3. The report considers this consistent with adherent-invasive E. coli (AIEC) being more characteristic of severe-Bacteroides-expanded E3 than of transitional E1. [src: ibd_phage_targeting] This matters for per-patient cocktail specificity. [src: ibd_phage_targeting]

### Consequence for cocktails

The report concludes that multi-target cocktails suit module members. [src: ibd_phage_targeting] It argues this because the module would likely re-equilibrate around a remaining hub if only one species were targeted. [src: ibd_phage_targeting] It proposes that members co-favor similar conditions, likely bile-acid dysregulation and low-oxygen inflammation. [src: ibd_phage_targeting] It hypothesizes that a cocktail hitting 3+ of M. gnavus, E. lenta, E. bolteae, H. hathewayi and E. coli will have compounding effects. [src: ibd_phage_targeting]

## Cross-feeding or shared environment?

The first reading was cross-feeding. In E3, Butyricicoccus pullicaecorum and A. caccae are top-degree hubs of the pathobiont module, not members of a separate healthy-commensal module. [src: ibd_phage_targeting] The report proposed a metabolic-partner or cross-feeding interpretation and cautioned against "preserve butyrate-producers" as a naive goal. [src: ibd_phage_targeting] Module-anchor commensals were suggested as functional-driver context. [src: ibd_phage_targeting]

In E1_CD, NB07c found associations that were initially consistent with butyrogenic cross-feeding. A. caccae coupled positively with all 5 module pathobionts, with sign concordance 1.0 across all 3 substudies. [src: ibd_phage_targeting] Species-level Spearman ρ values were +0.39 (E. bolteae), +0.33 (H. hathewayi), +0.31 (M. gnavus) and +0.29 (F. plautii). [src: ibd_phage_targeting] The E. bolteae pair was the strongest in E1_CD. [src: ibd_phage_targeting] B. nordii coupled negatively with M. gnavus (ρ_meta −0.21) and F. plautii (−0.20), read as niche competition. [src: ibd_phage_targeting] Iron pathways did not explain the coupling. A. caccae's mean iron-pathway correlation was +0.13 over 15 pathways, against +0.45 for E. coli. The report therefore called the coupling most likely substrate-, sugar- or lactate-mediated. [src: ibd_phage_targeting] NB07c deferred the cross-feeding versus shared-environment question to NB09c. [src: ibd_phage_targeting] It rated H3a-new only partially supported. [src: ibd_phage_targeting]

NB09c then did not support cross-feeding. [src: ibd_phage_targeting] Its strict triangle test required same-sign anchor–pathobiont correlations, both |ρ|>0.20 and both false discovery rate (FDR) <0.10. It found only 7 triangles across 8 species × 583 named HMP2 metabolites. [src: ibd_phage_targeting] None was a butyrogenic cross-feeding intermediate. [src: ibd_phage_targeting] Lactate × A. caccae (+0.18) had the opposite sign to lactate × F. plautii (−0.23) and lactate × E. bolteae (−0.20). [src: ibd_phage_targeting] The report calls this its strongest evidence against cross-feeding, and reads it as different cohort-level metabolic niches. [src: ibd_phage_targeting]

The report instead favors shared-environment co-occurrence as more parsimonious. [src: ibd_phage_targeting] It reads A. caccae, B. nordii, F. plautii and E. lenta as co-occurring in healthy or normobiotic samples. Mostly negative cholate and positive urobilin correlations support this, relative to CD-dysbiotic samples. [src: ibd_phage_targeting] H3a-new therefore got a PARTIAL verdict, reframed as shared-environment coupling. [src: ibd_phage_targeting]

## Collateral depletion

The earlier concern was that depleting M. gnavus, F. plautii, H. hathewayi or E. bolteae could incidentally reduce A. caccae through substrate loss. [src: ibd_phage_targeting] A. caccae is the only genuine butyrate producer among the module-anchor commensals, so its loss could partly offset the benefit. [src: ibd_phage_targeting] After NB09c, the report calls this concern less load-bearing. No substrate–product relationship is detectable at sample level, so substantial depletion of A. caccae through metabolic coupling is unlikely. [src: ibd_phage_targeting]

Two limits apply. The coupling was weaker in E3_CD. The two oral Actinomyces anchors coupled only weakly (~ρ=0.17–0.19) to module pathobionts. [src: ibd_phage_targeting] E3_CD anchors lacked metabolic-coupling structure. [src: ibd_phage_targeting] The cocktail implication is therefore E1-specific. UC Davis E3 patients (31 % of the cohort) may need a different module-anchor design framework. [src: ibd_phage_targeting]

The general warning still stands. Depleting the target species should not be the sole optimization criterion. Ecological cost, such as loss of 7α-dehydroxylation or butyrogenesis, bears on net inflammatory balance. [src: discoveries] See [[concepts/bile-acid-7-dehydroxylation-deficit-and-the-ecological-cost-of-targeting-bile-acid-transforming-species]] and [[summaries/discoveries]].

## Tensions

- Cross-feeding versus shared environment. NB07c's positive associations were initially consistent with cross-feeding, and the report proposed it for the E3 hub finding. [src: ibd_phage_targeting] NB09c's paired sample-level data did not support it. [src: ibd_phage_targeting]
- Collateral risk. NB07c warned of incidental A. caccae loss. [src: ibd_phage_targeting] NB09c downgraded the warning. [src: ibd_phage_targeting]

## Open Directions

- Test the E3 hub result (butyrate producers inside the pathobiont module) with paired metabolomics in an E3 cohort. NB09c rests on HMP2 only, so this would show whether E3 differs.
- Run in vitro co-culture of A. caccae with E. bolteae and F. plautii on lactate. This tests directly what the opposite-sign correlations only imply.
- Model post-cocktail re-equilibration by simulating hub removal in the NB06 networks. This tests the claim that the module re-forms around a remaining hub.
- Build a module-anchor framework for E3 patients, where oral-gut co-trafficking dominates.
