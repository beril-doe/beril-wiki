---
type: "Concept"
description: "Optimization of defined commensal consortia under niche coverage, inhibition, engraftability and safety criteria, including size comparisons, uncertainty and tradeoffs; stops at pathogen biology."
sources: ["summaries/cf_formulation_design__REPORT.md", "summaries/discoveries.md"]
---
# Multi-criterion design of protective microbiome formulations

This page covers how defined commensal consortia for cystic fibrosis (CF) airways are designed against several criteria at once: niche coverage, inhibition, engraftability and safety. The evidence is one design report built on a single pathogen strain, PA14, plus statements in the central discoveries digest. [src: cf_formulation_design] The optimum is confirmed by exhaustive search within the report's scoring, but formulation sizes k=2 to k=5 are not statistically distinguishable. [src: cf_formulation_design] The additive-inhibition assumption behind every ranking is untested. [src: cf_formulation_design] See [[summaries/cf_formulation_design__REPORT]] for the full report.

## Criteria and scoring

The report says formulations must cover the pathogen's metabolic niche, avoid internal metabolic competition among members, and persist in the patient airway. [src: cf_formulation_design] They must also be FDA-acceptable as live biotherapeutic products, and ideally combine metabolic competition with direct antagonism. [src: cf_formulation_design]

The scoring function evaluates communities of 1–5 organisms on PA14 niche coverage, internal complementarity, mean inhibition, engraftability and FDA safety. [src: cf_formulation_design] It integrates inhibition, metabolism, kinetics, engraftability, safety and interaction data into one score. [src: cf_formulation_design] The report presents this as addressing the lack of rational strain selection that Anderson et al. (2017) saw in CF probiotic trials. [src: cf_formulation_design] It also stresses strict safety filtering and species-specific validation over generic "probiotic" organisms. [src: cf_formulation_design]

## Safety filters as a tradeoff

The report ran two stages: a permissive filter that excludes only well-known pathogens, and a strict filter that also excludes all Pseudomonas, Enterobacteriaceae and Staphylococcus. [src: cf_formulation_design] The permissive filter surfaces the strongest inhibitors, but they are clinically problematic. These are Leclercia adecarboxylata (102%, Enterobacteriaceae), Pseudomonas_E juntendi (94%, non-aeruginosa Pseudomonas) and S. epidermidis (99%, nosocomial Staphylococcus). [src: cf_formulation_design] The report states that the strict filter costs roughly 15% inhibition ceiling but doubles engraftability. [src: cf_formulation_design]

## Optimum and size comparison

Exhaustive enumeration of all C(97,3) = 147,440 triples from the strict-safe pool scored 127,598 valid unique-species formulations. The same Micrococcus luteus + Neisseria mucosa + Streptococcus salivarius triple was the global optimum, with score 0.562. [src: cf_formulation_design] This shows the result is not an artifact of restricting the candidate pool. [src: cf_formulation_design]

The report recommends these strict-safe formulations:

| k | Members | Composite | Coverage | Inhibition | Engraftability |
|---|---|---|---|---|---|
| 1 | N. mucosa | 0.753 | 18% | 88% | 1.595 [src: cf_formulation_design] |
| 2 | R. dentocariosa + N. mucosa | 0.588 | 18% | 84% mean | 0.820 [src: cf_formulation_design] |
| 3 | M. luteus + N. mucosa + S. salivarius | 0.562 | 100% | 75% mean | 0.140 [src: cf_formulation_design] |
| 4 | the k=3 members + R. dentocariosa | 0.578 | 100% | 76% | 0.185 [src: cf_formulation_design] |
| 5 | the k=4 members + G. sanguinis | 0.587 | 100% | 78% mean | 0.188 [src: cf_formulation_design] |

The k=3 community is called the minimum viable formulation because it is the first size with full niche coverage. [src: cf_formulation_design] Rothia dentocariosa is added at k=4 for lung tropism and direct antagonism depth. [src: cf_formulation_design] The k=5 set is described as giving maximum redundancy and inhibition depth. [src: cf_formulation_design] The five-species core recurs across sizes, which the report reads as a robust solution rather than an optimization artifact. [src: cf_formulation_design] Neisseria mucosa is the indispensable anchor at every size. [src: cf_formulation_design] See [[entities/neisseria-mucosa]], [[entities/rothia-dentocariosa]] and [[entities/streptococcus-salivarius]].

### Uncertainty

Bootstrap resampling (1,000 times over the raw inhibition measurements) gave 95% confidence intervals (CIs) on composite scores. [src: cf_formulation_design] The intervals were k=1 [0.753, 0.753], k=2 [0.514, 0.588], k=3 [0.551, 0.562], k=4 [0.534, 0.578] and k=5 [0.520, 0.587]. [src: cf_formulation_design] All k=2 through k=5 intervals overlap, so those sizes are not statistically distinguishable on composite score. The report takes this as support for k=2 as the practical primary candidate. [src: cf_formulation_design]

## Engraftability against niche coverage

The best designs trade coverage against colonisation. Micrococcus luteus matters most for metabolic coverage but is the least likely to persist in the lung. [src: cf_formulation_design] The k=2 pair is lung-adapted, with 0.820 combined engraftability, nearly 6× the k=3 value of 0.140. [src: cf_formulation_design] But k=2 covers only 18% of PA niche. [src: cf_formulation_design] Neisseria mucosa alone is the best single organism, but its low coverage limits monotherapy. [src: cf_formulation_design] See [[concepts/engraftability-and-lung-adaptation-of-candidate-commensals]] and [[concepts/community-level-niche-coverage-and-resource-depletion-for-competitive-exclusion]].

The report offers three paths:
- Test k=3 in mice, because M. luteus's broad carbon utilization may compensate for low prevalence at sufficient dose. [src: cf_formulation_design]
- Prioritize k=2, sacrificing coverage for colonisation reliability. [src: cf_formulation_design]
- Search lung-adapted species for a broad-spectrum metabolizer to replace M. luteus. [src: cf_formulation_design]

It recommends k=2 as the primary clinical candidate for CF airways. [src: cf_formulation_design] It treats k=3 as an aspirational second-line candidate, contingent on showing M. luteus lung engraftment in vivo. [src: cf_formulation_design]

The discoveries digest supports the dual-mechanism emphasis. The strongest FDA-safe inhibitors (S. salivarius, N. mucosa, G. sanguinis) show 57-74% more PA14 inhibition than metabolic overlap predicts. [src: discoveries] It states that R. dentocariosa and N. mucosa anchor the FDA-safe formulation. [src: discoveries] It also states that competitive exclusion needs community-level coverage by 3+ organisms. [src: discoveries] See [[concepts/metabolic-competition-versus-direct-antagonism-in-pathogen-inhibition]].

## Proposed tests

The report proposes chronic PA14 lung infection mouse tests of k=2, k=3 and k=5, with and without xylitol + xylose supplementation. [src: cf_formulation_design] The k=2 versus k=3 comparison asks whether 100% niche coverage outperforms a lung-adapted pair with 18% coverage, which addresses the M. luteus engraftment question. [src: cf_formulation_design] The k=5 arm tests whether extra species help in vivo. [src: cf_formulation_design] It also proposes screening oral/respiratory Actinobacteria such as Kocuria, Dermacoccus or other Micrococcaceae with respiratory isolation records against the PA14 carbon utilization panel, to find a lung-adapted replacement for M. luteus. [src: cf_formulation_design] See [[concepts/selective-prebiotics-for-commensal-consortia]].

## Tensions

- Coverage versus engraftability: k=3 reaches 100% niche coverage but has 0.140 engraftability. [src: cf_formulation_design] k=2 has 0.820 engraftability but 18% coverage. [src: cf_formulation_design] The digest says exclusion needs 3+ organisms covering the niche, yet the report recommends k=2. [src: discoveries, cf_formulation_design]
- The report suggests that, with 84% mean inhibition, direct antagonism may matter more than coverage. It labels this a hypothesis to test in mice. [src: cf_formulation_design]

## Caveats

Scoring assumes additive inhibition, meaning a combination equals the mean of its members. This underestimates synergy and overestimates antagonistic combinations. [src: cf_formulation_design] The full 10-pair interaction matrix for the five-species core is a critical gap, and additive scoring stays provisional until it is measured. [src: cf_formulation_design] One untested antagonistic pair could invalidate the design, and all rankings depend on the assumption. [src: cf_formulation_design] See [[concepts/pairwise-interaction-among-commensals-in-competition-assays]].

## Open Directions

- Measure the full 10-pair interaction matrix for the five-species core and rescore with it. This replaces the additive assumption.
- Run the proposed mouse comparison of k=2, k=3 and k=5. It would settle whether coverage or engraftability drives efficacy.
- Screen Kocuria, Dermacoccus and other Micrococcaceae for a lung-adapted M. luteus replacement. This closes the coverage-engraftability gap.
- Repeat the bootstrap with more isolates, or with other pathogen strains. This would test whether the k=2 to k=5 overlap persists beyond PA14.
