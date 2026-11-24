---
type: "Concept"
description: "What RB-TnSeq fitness across carbon sources shows about the ManXYZ phosphotransferase system versus fructose PTS in Escherichia coli K-12, including cofitness and annotation conflicts."
sources: ["summaries/discoveries.md", "summaries/snipe_defense_system__REPORT.md"]
---
# Substrate specificity of the mannose PTS ManXYZ from genome-wide fitness

Random barcode transposon sequencing (RB-TnSeq) fitness data from the [[entities/fitness-browser]] show that the [[entities/manxyz-mannose-phosphotransferase-system]] in [[entities/escherichia-coli]] K-12 serves mannose and glucosamine, not fructose. The evidence is direct measurement in one organism (the Keio collection, 168 experiments), and it contradicts a UniProt annotation. [src: discoveries, snipe_defense_system]

## Literature Context

The candidate papers describe the Escherichia coli mannose phosphotransferase system (PTS, the phosphoenolpyruvate-dependent sugar uptake and phosphorylation system) as a transporter that handles glucose-class sugars. A purified ManXYZ complex reconstituted into phospholipid vesicles carried out vectorial glucose import coupled to phosphorylation, with Km 30 +/- 6 microM and kcat 401 +/- 32 pmol of Glc/micrograms of IICDMan/min [PMID 7890636](https://pubmed.ncbi.nlm.nih.gov/7890636/). This is an in vitro reconstitution. In Pasteurella multocida, a mannose PTS functionally similar to the E. coli one transports glucose as well as mannose [PMID 9766212](https://pubmed.ncbi.nlm.nih.gov/9766212/). For glucosamine, one study states that it is normally not a substrate of the glucose PTS (PtsG) but is transported by the mannose PTS encoded by manXYZ [PMID 11021940](https://pubmed.ncbi.nlm.nih.gov/11021940/). Mutational work shows that PtsG specificity can be broadened to mannose and glucosamine [PMID 10913076](https://pubmed.ncbi.nlm.nih.gov/10913076/). The N-acetylglucosamine PTS can be altered or overproduced to carry glucose in strains lacking the glucose and mannose PTSs [PMID 29393018](https://pubmed.ncbi.nlm.nih.gov/29393018/). That result comes from revertant mutant backgrounds, not from the unperturbed system. A Clostridium beijerinckii GlcNAc PTS transported glucose but did not complement PTS-dependent mannose utilization in an E. coli mutant [PMID 23995920](https://pubmed.ncbi.nlm.nih.gov/23995920/). In E. coli, growth on N-acetylmuramic acid needed the MurP PTS, and ManXYZ was not necessary [PMID 15060041](https://pubmed.ncbi.nlm.nih.gov/15060041/).

None of these candidate papers addresses fructose transport by ManXYZ, so they neither support nor contradict the fructose result. The corpus finding that manX, manY and manZ knockouts in the Keio collection are severely defective on D-glucosamine and D-mannose but dispensable on D-fructose (fruA, the fructose PTS gene, is -1.44 on fructose) comes from RB-TnSeq (random barcode transposon sequencing) fitness data. It is therefore not tested by these papers. The glucosamine defects (manX -3.79, manY -2.79, manZ -3.63) are consistent with the literature statement that glucosamine is carried by the mannose PTS [PMID 11021940](https://pubmed.ncbi.nlm.nih.gov/11021940/). The strong mannose defects (manX -2.75, manY -3.00, manZ -2.74) are consistent with the mannose PTS's established role. The literature also shows that the mannose PTS transports glucose [PMID 7890636](https://pubmed.ncbi.nlm.nih.gov/7890636/). Glucose was not among the conditions the hub reports, so that part cannot be compared.

The corpus claim that the UniProt "fructose-specific" annotation of ManX is wrong is not addressed by these papers. It remains a novel, annotation-level conclusion that rests on direct measurement in one organism. The tight cofitness of manX, manY and manZ (r = 0.705 to 0.851) agrees with these genes acting as one transporter complex, as in the reconstituted ManXYZ [PMID 7890636](https://pubmed.ncbi.nlm.nih.gov/7890636/). Because the literature shows other PTS components can substitute for glucose transport in altered strains [PMID 29393018](https://pubmed.ncbi.nlm.nih.gov/29393018/), the proposed double-mutant assays are a reasonable way to test cross-talk.

## Fitness across carbon sources

ManXYZ knockouts are severely defective on D-mannose and D-glucosamine but dispensable on D-fructose. [src: discoveries] The discoveries digest gives fit = -3.93 on D-mannose and -2.75 on D-glucosamine, and +0.18 to +0.66 on D-fructose. [src: discoveries] All scores are log2 ratios from RB-TnSeq, and carbon-source conditions were identified by condition_1 and expGroup = 'carbon source'. [src: snipe_defense_system]

The snipe_defense_system report gives per-gene means on sole carbon sources, listed below. Its D-mannose means differ from the single values in the discoveries digest. The claims do not say how the figures relate, so each stands as reported. [src: discoveries, snipe_defense_system]

- D-glucosamine (sole C), mean: manX -3.79, manY -2.79, manZ -3.63. [src: snipe_defense_system]
- D-mannose (sole C), mean: manX -2.75, manY -3.00, manZ -2.74. [src: snipe_defense_system]
- D-trehalose (sole C): manX -1.27, manY -1.49, no manZ value shown. [src: snipe_defense_system]
- Sodium chlorite: manX -1.47, manY -1.32, manZ -1.08. [src: snipe_defense_system]

Across all 168 experiments, the three genes have these profiles:

- manX: worst fitness -3.93, average -0.249, 6 conditions with fit < -1, 4 with fit < -2. [src: snipe_defense_system]
- manY: worst fitness -3.82, average -0.171, 10 conditions with fit < -1, 4 with fit < -2. [src: snipe_defense_system]
- manZ: worst fitness -4.14, average -0.082, 7 conditions with fit < -1, 4 with fit < -2. [src: snipe_defense_system]

## ManXYZ versus the fructose PTS

ManXYZ and FruA show opposite substrate patterns. [src: snipe_defense_system] ManXYZ mutants grow normally on fructose (fitness ≈ 0) but are crippled on mannose and glucosamine. [src: snipe_defense_system] FruA, the actual fructose PTS, is essential for fructose but dispensable for mannose. [src: snipe_defense_system]

- D-mannose: manX -2.75, manY -3.00, manZ -2.74, fruA -0.06. [src: snipe_defense_system]
- D-glucosamine: manX -3.79, manY -2.79, manZ -3.63, fruA -1.02. [src: snipe_defense_system]
- D-fructose: manX -0.22, manY +0.15, manZ -0.07, fruA -1.44. [src: snipe_defense_system]

The report reads this separation as confirming that ManYZ is a mannose/glucosamine-specific transporter. It also notes this is consistent with the role of ManYZ as the phage lambda entry receptor. [src: snipe_defense_system] See [[concepts/phage-resistance-versus-metabolic-cost-trade-off-at-receptor-transporters]].

## Cofitness and operon structure

The three genes are tightly co-fitness correlated: manX↔manZ r=0.851, manX↔manY r=0.705, and manY↔manZ r=0.725. The report interprets this as confirming a single operon. [src: snipe_defense_system] The report also lists manX (EIIAB, b1817) with specific defects on D-mannose and D-glucosamine. [src: snipe_defense_system]

## Tensions

- UniProt annotates ManX as a "fructose-specific" PTS component and with "fructose import across plasma membrane" (GO:0005354, Gene Ontology). [src: snipe_defense_system, discoveries] The fitness data show ManXYZ is dispensable for fructose, and the discoveries digest states that this contradicts the annotation. [src: discoveries, snipe_defense_system]

## Scope

ManXYZ was present only in E. coli K-12 (Keio collection) among the 48 Fitness Browser organisms. The conclusions therefore rest on one organism. [src: snipe_defense_system]

## Open Directions

- Run fitness assays of manXYZ and fruA double mutants on mixed fructose and mannose media. This would test whether any cross-talk exists that single-mutant data miss.
- Check the 6 to 10 conditions per gene with fit < -1 beyond the sugars, such as trehalose and sodium chlorite. This would show whether the non-sugar defects are real or polar effects.
- Compare ManXYZ homologs in other bacteria with RB-TnSeq data on mannose and fructose. This would test whether the specificity holds outside E. coli K-12.
- Submit a correction for the GO:0005354 annotation of ManX. This would resolve the annotation conflict.
