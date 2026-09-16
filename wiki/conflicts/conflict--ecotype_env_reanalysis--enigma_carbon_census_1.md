<!-- tension-hash: db8d8c2189132c0c -->
# Conflict: Absent Biology or Absent Annotation — Four Tensions in Callability-Limited Inference

Two projects in this corpus ran into the same structural problem from opposite ends: when a comparative analysis returns *nothing* — no utilizer call, no class gradient, no ecological contrast — it is rarely clear whether the null reflects the world or the resources used to query it. The tensions recorded on [[concepts/callability-limited-comparative-inference]] pit a directional pattern against an unsupported significance test, biological darkness against database darkness, environmental presence against functional evidence, and a clean within-method null against the methodological choices that produced it. This page covers all four disagreements as stated in that concept page; it introduces no figures beyond those the concept page cites. The stakes are practical: each tension decides whether a null result is a discovery target, a coverage gap, or an artifact of filtering.

## Evidence Sides

### Disagreement 1 — A chemical-class coverage gradient: seen but not supported

**Side A: the census shows a class gradient.** The census showed a directional concentration of callable compounds in simpler, commonly represented chemical classes. [src: enigma_carbon_census_1]

**Side B: the test does not support it.** H1 was not formally supported by the chi-square test — a count-based test of whether callable compounds are distributed evenly across chemical classes. [src: enigma_carbon_census_1]

The concept page's own reading is that this tension should remain an annotation-coverage hypothesis rather than being resolved as either a true chemical-class gradient or its absence. [src: enigma_carbon_census_1] Neither side may be adopted as the finding: the direction is real as a description of the callable set, and the inferential claim it would license is not licensed.

### Disagreement 2 — Biological darkness versus database darkness

**Side A: the dark set marks unlinkable biology.** The 29 fully orphan compounds were not linkable through the queried resources. [src: enigma_carbon_census_1]

**Side B: unlinkable is not unknown.** "Organism-dark" does not mean unknown to science; the literature screen was shallow. [src: enigma_carbon_census_1]

The result therefore supports a resource-limited discovery frontier while leaving open how much of the 74-compound dark set reflects absent biology, absent annotations, absent literature retrieval, or an overly restrictive reaction filter. [src: enigma_carbon_census_1] This is the principal tension of the census. [src: enigma_carbon_census_1] Four candidate causes sit behind one observation, and the census design cannot separate them.

### Disagreement 3 — Environmental presence versus functional evidence

**Side A: occurrence data covers the implicated organisms.** The atlas provides occurrence and abundance data for implicated genera, including the 86-genera, 3825-NMDC-metagenome, and 302-Planet-Microbe-run scope. [src: enigma_carbon_census_1]

**Side B: occurrence is not catabolism.** The atlas does not provide compound-resolved catabolic activity. [src: enigma_carbon_census_1] Environmental occurrence can prioritize enrichment sources without establishing that observed organisms consume a particular dark compound. [src: enigma_carbon_census_1]

### Disagreement 4 — Environmental callability versus a null ecological contrast

**Side A: the ecological contrast is null within method.** The ecotype reanalysis found no stronger environment–gene-content association among environmental species despite confirming clinical sampling bias, with U=1536 and p=0.83 for Environmental > Human-associated. [src: ecotype_env_reanalysis] (U is the Mann–Whitney U statistic, a rank-based test of whether one group's values sit systematically higher than another's.)

**Side B: the groups were not equally callable.** Environmental species also had a higher NaN rate — NaN being a missing or undefined value where no correlation could be computed — at 21%, than human-associated species, 7%. [src: ecotype_env_reanalysis] The report further notes that the extraction methodology produced a 27x difference in overall median correlation relative to the original analysis. [src: ecotype_env_reanalysis]

The result supports the within-method null comparison but leaves unresolved how much ecological signal is lost through species-level filtering, genome-count imbalance, and extraction choices. [src: ecotype_env_reanalysis]

## Possible Reconciliations

These are hypotheses, not findings; none is tested by the evidence above.

**Coverage as the shared confound (Disagreements 1 and 2).** *Hypothesis:* the directional concentration of callables in simpler, commonly represented classes and the 74-compound dark set are two views of one annotation-coverage surface, not two biological facts. [src: enigma_carbon_census_1] If so, Side A of Disagreement 1 is descriptively correct about which compounds are *callable here*, Side B is correct that no claim about degradability follows, and the census's own framing — an annotation-coverage hypothesis — is the honest joint statement. [src: enigma_carbon_census_1]

**Definitional scope difference (Disagreement 2).** *Hypothesis:* the two sides use "dark" at different scopes. "Not linkable through the queried resources" is a statement about a retrieval boundary; "unknown to science" is a statement about the literature. [src: enigma_carbon_census_1] Both can hold simultaneously for the same 29 fully orphan compounds, and the disagreement dissolves only if the four listed causes — absent biology, absent annotations, absent literature retrieval, an overly restrictive reaction filter — are separately estimated. [src: enigma_carbon_census_1]

**Evidence-type difference, not conflict (Disagreement 3).** *Hypothesis:* occurrence and function are non-competing evidence layers, and the tension is one of over-reading rather than of contradiction. Under this reading the atlas scope — 86 genera, 3825 NMDC metagenomes, 302 Planet Microbe runs — is correctly used as a prioritization prior for enrichment sourcing and incorrectly used as catabolic evidence. [src: enigma_carbon_census_1]

**Differential missingness as a scope restriction (Disagreement 4).** *Hypothesis:* the null is real for the species that survived filtering, while the 21% versus 7% NaN asymmetry means the environmental group tested is a narrower, better-sampled subset of environmental species than the human-associated group is of human-associated species. [src: ecotype_env_reanalysis] Both sides would then be right about different populations.

**Measurement-scale difference (Disagreement 4).** *Hypothesis:* the 27x difference in overall median correlation attributable to extraction methodology shifts absolute magnitudes without reordering groups, so a group contrast can be stable while the quantity being contrasted is method-dependent. [src: ecotype_env_reanalysis] This would make the within-method null comparison sound and any cross-method magnitude comparison unsound.

## Resolving Work

**Disagreement 1 — class gradient.**
- Recount callability by chemical class after the dark set is re-queried against an expanded annotation base, and re-run the chi-square test: does the direction survive when coverage is equalized? [src: enigma_carbon_census_1]
- Build a per-class annotation-coverage index independent of callability and test whether it predicts callability; if it does, the gradient is a coverage gradient. [src: enigma_carbon_census_1]
- Power-analyze the census design at its current callable count to state the class-gradient effect size it could have detected.

**Disagreement 2 — biological versus database darkness.**
- Partition the 74-compound dark set into the four stated causes — absent biology, absent annotations, absent literature retrieval, overly restrictive reaction filter — by re-running each channel independently and recording which compounds each rescues. [src: enigma_carbon_census_1]
- Replace the shallow literature screen with a deep full-text and homology-based search over the 29 fully orphan compounds, and report the reclassification count. [src: enigma_carbon_census_1]
- Relax the reaction filter over one fixed compound set and measure how many dark compounds become callable purely from filter width.

**Disagreement 3 — presence versus function.**
- Pair the 86 implicated genera with compound-resolved growth or fitness assays on a sampled subset of dark compounds, converting occurrence to catabolic evidence. [src: enigma_carbon_census_1]
- Test whether genus occurrence across the 3825 NMDC metagenomes and 302 Planet Microbe runs predicts enrichment success for the same compounds, which is the claim occurrence data can legitimately support. [src: enigma_carbon_census_1]
- Record, per dark compound, whether any evidence line is functional rather than occurrence-based, so the two layers are never merged in downstream tables.

**Disagreement 4 — null contrast versus lost signal.**
- Impute or model the NaN species rather than dropping them, and re-run the Environmental > Human-associated test to see whether U=1536 and p=0.83 move once the 21%/7% asymmetry is absorbed. [src: ecotype_env_reanalysis]
- Match environmental and human-associated species on genome count before testing, isolating genome-count imbalance from ecology.
- Re-run the comparison under both extraction methodologies that differ by the 27x factor in overall median correlation, confirming that group ordering is invariant to extraction choice. [src: ecotype_env_reanalysis]
- Repeat the contrast below species-level filtering to quantify how much ecological signal species-level aggregation removes. [src: ecotype_env_reanalysis]
