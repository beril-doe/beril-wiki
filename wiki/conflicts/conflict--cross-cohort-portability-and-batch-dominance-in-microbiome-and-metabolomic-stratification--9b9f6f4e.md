<!-- tension-hash: 9b9f6f4e3d962891 -->
# Pool Size Versus Pathway Capacity, and Pooled Versus Within-Substudy Calls, in Crohn's Disease Stratification

Two disagreements sit inside the cross-cohort work summarised in [[concepts/cross-cohort-portability-and-batch-dominance-in-microbiome-and-metabolomic-stratification]]. In the first, polyamines look depleted in Crohn's disease (CD) by pathway differential abundance (DA, a test of which features differ between groups) and strongly enriched by metabolomics. In the second, *C. scindens* is called CD-enriched by pooled DA, a call the report labels false, yet a confound-free within-substudy analysis also finds it CD↑. It matters because the readings point in opposite directions, and the labels decide which findings are treated as current.

## Evidence Sides

**Side A: pathway-level and pooled evidence**

- Pathway-level DA found `06_polyamine_urea` CD-DOWN, with an odds ratio (OR, a measure of enrichment) of 0.42. [src: discoveries, ibd_phage_targeting]
- Pathway DA measures production capacity. [src: discoveries]
- Pooled DA called *C. scindens* CD-enriched, and the report calls that a false call. [src: discoveries]

**Side B: metabolomic and within-substudy evidence**

- Metabolomics found polyamines CD-UP at OR=14.6, the largest theme-level metabolite effect in the project. [src: discoveries, ibd_phage_targeting]
- Untargeted metabolomics measures steady-state pool size. Pools reflect production minus consumption plus dietary and host inputs, so pool and flux measurements are not interchangeable. [src: ibd_phage_targeting]
- Confound-free within-substudy analysis nonetheless found *C. scindens* CD↑. The report treats this result as current. [src: discoveries]

The report says the polyamine result is not necessarily a contradiction. [src: discoveries] The two *C. scindens* analyses disagree on the evidence behind the label. [src: discoveries]

## Possible Reconciliations

- **Hypothesis: pool accumulation without elevated biosynthesis.** More dietary-protein or mucin catabolism, plus reduced microbial clearance, could raise polyamine pools while pathway capacity falls. [src: ibd_phage_targeting]
- **Hypothesis: capacity and pool answer different questions.** Both measurements may be correct, since production capacity and steady-state pool size are distinct quantities. [src: discoveries]
- **Open question for *C. scindens*:** the input does not say why pooled and within-substudy analyses disagree. This is a question to test, not an explanation.

## Resolving Work

- **Data:** polyamine pathway and metabolite measurements from the same samples. **Method:** paired comparison of capacity and pool by group. **Question:** do the CD-DOWN pathway signal and the CD-UP pool signal co-occur within individuals?
- **Data:** diet and host-input annotations. **Method:** stratify the polyamine pool comparison by these inputs. **Question:** does dietary-protein or mucin catabolism account for the pool difference?
- **Data:** microbial polyamine consumption genes or uptake measurements. **Method:** test clearance against pool size. **Question:** is reduced microbial clearance associated with higher pools?
- **Data:** the pooled and within-substudy *C. scindens* tables. **Method:** side-by-side re-run with identical thresholds. **Question:** what accounts for the disagreement between the two analyses?
