<!-- tension-hash: 07279e23e42f5243 -->
# Universal Positive Metal Cross-Resistance or Metal-Dependent Overlap with Salt Stress?

The metal cross-resistance study reads its metal–metal fitness correlations as a universal positive "directional layer" of tolerance shared across metals. [src: metal_cross_resistance] The counter-ion analysis finds that metal–sodium chloride (NaCl) correlations vary substantially across metals. [src: counter_ion_effects] Because the analyses compare different condition pairs, they do not directly contradict each other, and the disagreement is about interpretation. [src: metal_cross_resistance, counter_ion_effects] Predominantly positive metal–metal correlations do not establish a uniform response to NaCl or identify which shared stressor generates the signal. Separating those components is the decomposition [[concepts/shared-stress-versus-stressor-specific-fitness]] requires before mechanistic interpretation. [src: metal_cross_resistance, counter_ion_effects]

## Evidence Sides

**Side A: Metal–metal correlations form a universal positive layer**

The metal cross-resistance study interprets its metal-pair correlations as a universal positive directional layer. [src: metal_cross_resistance] Inside the same report, the statement that all tested metal pairs are positive appears next to a count of 311/317 (98.1%) positive correlations. These are conflicting source statements, so universal positivity should not be treated as established. [src: metal_cross_resistance] The defensible reading of this side is "predominantly positive," not "universally positive." [src: metal_cross_resistance]

**Side B: Overlap with salt stress varies widely by metal**

The counter-ion analysis shows that correlations between metal and NaCl fitness profiles vary substantially across metals. Examples include iron at r=0.086 and zinc at r=0.715, where r is the correlation coefficient between gene-level fitness profiles. [src: counter_ion_effects]

**Relation between the sides**

The two sides measure different condition pairs, so this is not a direct contradiction. Side B does **refine** Side A in two ways. First, predominantly positive metal–metal correlations do not establish a uniform response to NaCl. Second, they do not identify which shared stressor generates the signal. [src: metal_cross_resistance, counter_ion_effects]

## Possible Reconciliations

- **Hypothesis 1:** Metal–metal positivity is driven largely by a general cellular-stress component. Metals differ in how strongly they engage that component, which would produce mostly positive metal–metal correlations alongside variable metal–NaCl correlations.
- **Hypothesis 2:** Some metal pairs correlate positively through shared metal-specific machinery that NaCl does not engage. In that case, metal–metal positivity and metal–NaCl overlap reflect partly different gene sets.
- **Hypothesis 3:** The "universal" wording reflects summarization, not the underlying counts. Once the non-positive observations are examined, the directional layer may be better described as predominant than universal.

## Resolving Work

- **Non-positive cases.** Using the cross-resistance organism–metal pair observations, inspect the non-positive observations organism by organism. Do they cluster by metal, by organism or by low data quality, and can the "all pairs positive" statement survive under any defined threshold?
- **Removing the salt component.** In organisms profiled under both metals and NaCl, compute partial correlations between metal profiles while controlling for the NaCl profile. A partial correlation measures association after removing the variance explained by a third variable. Does metal–metal positivity survive once the salt-shared component is removed?
- **Low-overlap versus high-overlap metals.** Compare the genes driving metal–metal correlations for a low-NaCl-overlap metal (iron) against a high-overlap metal (zinc). Use gene-set enrichment, which tests whether functional categories are over-represented among those genes relative to the genome background. Do low-overlap metals share a distinct, metal-specific tolerance layer?
- **Decomposing the shared signal.** Fit a factor decomposition across the full metal and salt condition matrix. This method models each fitness profile as a weighted combination of shared and condition-specific components. What fraction of each metal's profile loads on a common stress factor, and which stressor anchors that factor?
