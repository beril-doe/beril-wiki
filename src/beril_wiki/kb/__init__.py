"""The wiki as structured records: claims, sections, links and the tools over them.

Git text is canonical (``wiki/``, ``knowledge/``, ``state/``); ``index`` builds a
disposable SQLite view of it per machine. ``tools`` holds every operation an agent may
perform, each write behind a deterministic gate. ``server`` and ``cli`` expose those
same functions over MCP and the command line; ``agents`` starts a vendor harness with a
skill from ``skills/`` and nothing but the wiki tools.
"""
