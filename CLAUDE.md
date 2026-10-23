# beril-wiki contributor rules

`AGENTS.md` links to this file, so Claude and Codex sessions read the same
rules.

## Personal artifacts stay out of Git

Plans, specs, and HTML pages written while working on the wiki go in
`docs/drafts/` or `docs/superpowers/`, which `.gitignore` excludes. That
includes html-artifact pages and their `.excalidraw` and `.json` diagram
sources. `.gitignore` also excludes every `.html` and `.excalidraw` file under
`docs/`. Never stage these files. To publish one on GitHub, ask the maintainer
first, then add it with `git add -f <path>`. `docs/agentic-workflow.html` is
published documentation that the README links to, so it stays tracked.
