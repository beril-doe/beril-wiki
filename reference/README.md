# reference/ — not the wiki

Neither directory here is published, and neither should be cited. They exist so
the compiler's provenance and its acceptance test stay auditable.

## `wiki-v3/` — superseded corpus

The output of the previous wiki generation (OpenKB + Sonnet/Luna), kept only as
the benchmark for the parity protocol in `DESIGN.md` and `PARITY_REPORT.md`.

It looks like the live wiki and is not. Its numbers, citations and page set are
frozen at the v3 build and were never carried forward — several claims here
were corrected in the current corpus. **The published wiki is `wiki/` and
`wiki-extra/`, rendered at the site linked from the README.** If you found a
page under `reference/wiki-v3/` through a code search, you want its counterpart
one directory up.

## `openkb-src/` — vendored third party

A copy of [OpenKB](https://github.com/VectifyAI/OpenKB) (Apache-2.0), the
compiler this pipeline replaced. Retained because the current compile prompts
are derived from `agent/compiler.py`, so the derivation is checkable against
the original. Attribution is in the repository `LICENSE`; the upstream licence
is at `openkb-src/LICENSE`. Nothing in the pipeline imports it at runtime.
