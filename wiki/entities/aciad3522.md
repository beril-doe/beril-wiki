---
type: "Gene_Or_Pathway"
description: "ACIAD3522 is an NADH-FMN oxidoreductase with acetate-specific fitness effects in ADP1."
sources: ["summaries/respiratory_chain_wiring__REPORT.md"]
---
# ACIAD3522

## What this entity is

**Canonical name:** ACIAD3522. [src: respiratory_chain_wiring]  
**Known aliases:** No aliases are reported in the source document. [src: respiratory_chain_wiring]  
**Stable external identifier:** No stable external identifier is reported in the source document. [src: respiratory_chain_wiring]

ACIAD3522 is described as a single-subunit NADH-FMN oxidoreductase and is analyzed as one of three parallel NADH dehydrogenase activities in [[entities/acinetobacter-baylyi-adp1]]. [src: respiratory_chain_wiring] The report cautions that ACIAD3522 may not be a respiratory NADH dehydrogenase in the strict sense and could instead have another metabolic function. [src: respiratory_chain_wiring]

## Evidence from respiratory-chain wiring

ACIAD3522 is dispensable on quinate and glucose but has a growth ratio of 0.013 on acetate, where the report describes its phenotype as lethal. [src: respiratory_chain_wiring] Acetate therefore specifically requires ACIAD3522 in the reported respiratory-chain profile, alongside Complex I, cytochrome bo3, and additional components. [src: respiratory_chain_wiring]

Flux-balance analysis (FBA), a computational optimization method for predicting metabolic fluxes, predicts zero flux through ACIAD3522 on all standard media because the model routes NADH through Complex I, which produces more ATP per NADH. [src: respiratory_chain_wiring] This result illustrates how growth optimization in [[concepts/metabolic-model-gapfilling]] can miss alternative or conditionally required respiratory pathways. [src: respiratory_chain_wiring]

Under standard growth conditions, ACIAD3522 had a mean protein level of 26.2 at the 48th percentile, compared with a genome median of 26.4. [src: respiratory_chain_wiring] Its similar abundance to Complex I and NDH-2 supports the report's passive, flux-based wiring interpretation rather than a transcriptional switch, although this interpretation does not establish ACIAD3522's biochemical function. [src: respiratory_chain_wiring]

## Interpretation and open tests

The acetate-specific fitness effect supports a condition-specific respiratory requirement in [[concepts/condition-specific-fitness]] and adds evidence to [[concepts/gene-essentiality]] that gene importance can change with carbon source. [src: respiratory_chain_wiring] The source identifies characterization of ACIAD3522 as a needed test because its NADH-FMN oxidoreductase annotation may represent a function other than respiratory NADH dehydrogenation. [src: respiratory_chain_wiring]

## Related pages

- [[summaries/respiratory_chain_wiring__REPORT]] — source summary containing the ACIAD3522 fitness, flux, and proteomics evidence. [src: respiratory_chain_wiring]
- [[entities/acinetobacter-baylyi-adp1]] — organism in which ACIAD3522 is studied. [src: respiratory_chain_wiring]
- [[entities/complex-i]] — alternative NADH dehydrogenase used by the model for NADH oxidation. [src: respiratory_chain_wiring]
- [[entities/ndh-2]] — other NADH dehydrogenase included in the respiratory-chain comparison. [src: respiratory_chain_wiring]
- [[concepts/condition-specific-fitness]] — concept covering substrate-dependent gene fitness. [src: respiratory_chain_wiring]
- [[concepts/metabolic-model-gapfilling]] — concept addressing limitations of growth-optimized metabolic models. [src: respiratory_chain_wiring]
- [[concepts/gene-essentiality]] — concept receiving the acetate-specific ACIAD3522 fitness evidence. [src: respiratory_chain_wiring]
- [[concepts/multi-omics-integration]] — concept receiving the integrated fitness, FBA, stoichiometric, and proteomic interpretation. [src: respiratory_chain_wiring]
