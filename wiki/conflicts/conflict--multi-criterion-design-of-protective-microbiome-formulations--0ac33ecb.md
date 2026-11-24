<!-- tension-hash: 0ac33ecb14dac9a3 -->
# Niche Coverage Versus Engraftability in Protective Microbiome Formulations

Defined commensal consortia for cystic fibrosis (CF) airways are designed against several criteria at once, as described in [[concepts/multi-criterion-design-of-protective-microbiome-formulations]]. The disagreement is over formulation size. A formulation of k=3 organisms reaches 100% niche coverage but has 0.140 engraftability. [src: cf_formulation_design] A formulation of k=2 has 0.820 engraftability but 18% coverage. [src: cf_formulation_design] The digest says exclusion needs 3+ organisms covering the niche, yet the design report recommends k=2. [src: discoveries, cf_formulation_design] This matters because the choice decides which consortia go forward to mouse testing.

## Evidence Sides

**Side A: coverage needs three or more organisms**

- At k=3, niche coverage is 100% and engraftability is 0.140. [src: cf_formulation_design]
- The digest says exclusion needs 3+ organisms covering the niche. [src: discoveries, cf_formulation_design]
- Under this reading, k=2 falls short because its coverage is only 18%. [src: cf_formulation_design]

**Side B: engraftability, and perhaps direct antagonism, favour k=2**

- At k=2, engraftability is 0.820 (the k=3 value is 0.140). [src: cf_formulation_design]
- The report recommends k=2 despite its 18% coverage. [src: discoveries, cf_formulation_design]
- The report suggests that, with 84% mean inhibition, direct antagonism may matter more than coverage. It labels this a hypothesis to test in mice, not an established finding. [src: cf_formulation_design]

Neither side is preferred here. The two sets of figures are reported side by side and are not averaged.

## Possible Reconciliations

- **Hypothesis 1: antagonism dominates.** If direct antagonism drives suppression, coverage matters less and k=2 suffices. The report itself labels this a hypothesis. [src: cf_formulation_design]
- **Hypothesis 2: the criteria apply to different stages.** Coverage may govern the exclusion mechanism, and engraftability may govern whether a consortium persists. A larger consortium might be reached by changing delivery or the engraftability scoring. This idea is not tested in the sources.
- **Hypothesis 3: the scoring is the problem.** Both numbers come from one design report, so the disagreement may reflect the scoring and not the biology. This idea is also untested.

## Resolving Work

- **Data:** mouse colonization experiments. **Method:** compare k=2 and k=3 consortia against the pathogen strain PA14. **Question:** does the 84% mean inhibition of k=2 hold in vivo despite its 18% coverage?
- **Data:** the existing inhibition assays. **Method:** separate antagonism from metabolic competition for each member. **Question:** does direct antagonism explain more suppression than niche coverage?
- **Data:** the engraftability scores for k=3 (0.140) and k=2 (0.820). **Method:** sensitivity analysis of how engraftability is defined and weighted. **Question:** is the gap robust to the scoring choices?
- **Data:** the pairwise interaction measurements. **Method:** test the additive-inhibition assumption directly in mixtures. **Question:** do the rankings of k=2 and k=3 survive when inhibition is not assumed additive?
- **Data:** additional pathogen strains beyond PA14. **Method:** repeat the design search. **Question:** does the 3+ organism requirement hold beyond a single strain?
