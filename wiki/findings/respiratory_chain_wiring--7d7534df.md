---
type: "Finding"
description: "Under standard growth conditions, protein-abundance means are 27.6 for Complex I, 27.0 for NDH-2 and 26.2 for ACIAD3522 versus a genome median of 26.4, which the report interprets as metabolic rather than transcriptional wiring."
finding_id: "respiratory_chain_wiring--7d7534df"
result: "observation"
source: "respiratory_chain_wiring"
quantities: [{"value": "27.6", "what": "Complex I mean protein abundance", "unit": "", "denominator": "", "scope": "standard growth conditions"}, {"value": "27.0", "what": "NDH-2 mean protein abundance", "unit": "", "denominator": "", "scope": "standard growth conditions"}, {"value": "26.2", "what": "ACIAD3522 mean protein abundance", "unit": "", "denominator": "", "scope": "standard growth conditions"}, {"value": "26.4", "what": "genome median protein abundance", "unit": "", "denominator": "", "scope": ""}]
caveat: "Condition-specific upregulation of Complex I or NDH-2 has not been established here; reanalysis of quinate-versus-succinate proteomics is proposed."
first_added: "2026-11-09"
source_hash: "e44ee5fea95d2bf94013d27d0b2afd372d6612ac3bf997f73e2813afe5bb42b3"
---
# All three NADH dehydrogenases co-expressed, suggesting flux-based wiring

Under standard growth conditions, protein-abundance means are 27.6 for Complex I, 27.0 for NDH-2 and 26.2 for ACIAD3522 versus a genome median of 26.4, which the report interprets as metabolic rather than transcriptional wiring. [src: respiratory_chain_wiring]

## Key figures

- **27.6**: Complex I mean protein abundance (scope standard growth conditions) [src: respiratory_chain_wiring]
- **27.0**: NDH-2 mean protein abundance (scope standard growth conditions) [src: respiratory_chain_wiring]
- **26.2**: ACIAD3522 mean protein abundance (scope standard growth conditions) [src: respiratory_chain_wiring]
- **26.4**: genome median protein abundance [src: respiratory_chain_wiring]

## Evidence

> All three NADH dehydrogenases are expressed at similar protein levels under standard growth conditions: Complex I mean 27.6 (66th percentile), NDH-2 27.0 (59th percentile), ACIAD3522 26.2 (48th percentile), genome median 26.4. The spread is only 1.4 units. NDH-2 is NOT repressed — it is constitutively co-expressed with Complex I. This means the condition-specific respiratory wiring operates at the metabolic level: all three dehydrogenases are present simultaneously, and which one becomes limiting depends on the NADH flux rate from the carbon source being catabolized. The cell uses a passive, flux-based wiring system rather than an active transcriptional switch. [src: respiratory_chain_wiring]

From the report [[summaries/respiratory_chain_wiring__REPORT]].

## Caveat

Condition-specific upregulation of Complex I or NDH-2 has not been established here; reanalysis of quinate-versus-succinate proteomics is proposed. [src: respiratory_chain_wiring]

> 5. **Respiratory chain proteomics**: Does ADP1 upregulate Complex I on aromatic substrates and NDH-2 on glucose? Stuani et al. (2014) did quinate vs succinate proteomics — reanalyzing their data for respiratory chain proteins could test the wiring model. [src: respiratory_chain_wiring]

## Other caveats in this report

- The flux-balance analysis (FBA) model predicts zero flux through NDH-2 and ACIAD3522 on standard media. The report attributes its failure to predict condition-specific requirements to missing capacity constraints. [src: respiratory_chain_wiring]
- The central prediction that NDH-2 compensates on glucose cannot be directly tested because NDH-2 lacks growth data. [src: respiratory_chain_wiring]
- The NADH stoichiometry and flux-rate explanation rely on theoretical pathway biochemistry rather than measured flux distributions. [src: respiratory_chain_wiring]
- The cross-species comparison includes only 4 organisms without NDH-2 and is underpowered. [src: respiratory_chain_wiring]
- Variable annotation may cause the NDH-2 search to miss orthologs in Fitness Browser organisms. [src: respiratory_chain_wiring]
