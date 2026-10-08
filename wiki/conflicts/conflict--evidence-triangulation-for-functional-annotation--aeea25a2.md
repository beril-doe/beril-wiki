<!-- tension-hash: aeea25a27ab519a4 -->
# Do the Fitness Browser ManXYZ Substrate Values Match Between the Discoveries Digest and the SNIPE Project Report?

Two corpus sources agree that gene-fitness data contradict a curated functional annotation of ManX, a component of the mannose phosphotransferase system (PTS, a sugar uptake system that phosphorylates sugars as it imports them). [src: discoveries, snipe_defense_system] They do not agree on the per-substrate fitness values behind that conclusion. [src: discoveries, snipe_defense_system] This matters for [[concepts/evidence-triangulation-for-functional-annotation]]: if fitness evidence is to overrule a curated annotation, the numbers it rests on must be traceable. Here, the central digest and the project report give different values for the same genes and conditions.

## Evidence Sides

**Discoveries digest**

The digest draws on Fitness Browser data from 168 experiments with the *E. coli* K-12 Keio collection, a library of single-gene knockouts. [src: discoveries] It reports severe ManXYZ knockout defects on D-mannose (fit = -3.93) and D-glucosamine (fit = -2.75). [src: discoveries] It reports dispensability on D-fructose (fit = +0.18 to +0.66). [src: discoveries] On that basis it says the data contradict the UniProt annotation "fructose import across plasma membrane" (GO:0005354, a Gene Ontology term) for ManX. [src: discoveries]

**snipe_defense_system project report**

The report gives per-gene values. On D-mannose they are manX -2.75, manY -3.00 and manZ -2.74. [src: snipe_defense_system] On D-glucosamine they are manX -3.79, manY -2.79 and manZ -3.63. [src: snipe_defense_system] On D-fructose they are manX -0.22, manY +0.15 and manZ -0.07. [src: snipe_defense_system] The report identifies -3.93 as manX's worst fitness across 168 experiments, not as its D-mannose value. [src: snipe_defense_system] It presents its table as Fitness Browser data that directly contradict UniProt's annotation of ManX as a "fructose-specific" PTS component. The table shows ManXYZ defects on D-mannose and D-glucosamine but not on D-fructose, where FruA fitness is -1.44. [src: snipe_defense_system]

**Shared ground**

Both sources report defects on mannose and glucosamine and no defect on fructose. The qualitative challenge to the GO annotation is therefore common to both. [src: discoveries, snipe_defense_system] The digest's substrate-level values do not match the project report, and they should not be cited until the two are reconciled. [src: discoveries, snipe_defense_system]

## Possible Reconciliations

- *Hypothesis:* the digest's D-mannose figure (-3.93) [src: discoveries] may be manX's worst fitness across 168 experiments, which the report gives as a summary value rather than a D-mannose value [src: snipe_defense_system], mislabelled as a substrate value.
- *Hypothesis:* the digest's D-glucosamine figure (-2.75) [src: discoveries] may have been transposed from the report's manX D-mannose value, which is also -2.75. [src: snipe_defense_system]
- *Hypothesis:* the digest's D-fructose range (+0.18 to +0.66) [src: discoveries] may come from a different gene, replicate set or aggregation than the report's per-gene values of manX -0.22, manY +0.15 and manZ -0.07. [src: snipe_defense_system] Neither source states which.

None of these is confirmed by the evidence. Each would need checking against the underlying records.

## Resolving Work

- Re-query the Fitness Browser *E. coli* K-12 records for manX, manY and manZ on D-mannose, D-glucosamine and D-fructose. Tabulate per-experiment and averaged fit values to establish which source's substrate-level numbers the data reproduce.
- Trace the digest's provenance by comparing its figures against the snipe_defense_system tables, testing whether a worst-fitness value or a transposed cell was copied into the digest.
- Recover the replicate-level D-fructose scores for all three genes, showing whether any experiment or aggregation yields the digest's +0.18 to +0.66 range. [src: discoveries]
- Once the values are settled, correct or annotate the digest entry and re-state the GO:0005354 contradiction with cited per-gene values, so that triangulation pages cite one consistent table.
