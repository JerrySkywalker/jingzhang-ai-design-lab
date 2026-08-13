# Formal Repository Receipt

## Fork and remotes

```text
fork=https://github.com/JerrySkywalker/haidian
fork_created_in_goal=true
fork_parent=open-city-ai/haidian
local=V:\src\haidian
origin=https://github.com/JerrySkywalker/haidian.git
upstream=https://github.com/open-city-ai/haidian.git
branch=submission/JerrySkywalker/jingzhang-in-place
branch_head=c50d5594c3747ea69f34af6ad03978e40a86463e
upstream_head=5cef3aa58a8306450684bd1d64ff651fd6b51e4b
package=submissions/JerrySkywalker/jingzhang-in-place
```

The canonical repository was not mutated and no upstream PR was created.

## Workspace contract

- official bootstrap helper was downloaded from exact kickoff head and inspected before execution;
- helper blob SHA-1: `038bcaad0f386e3d91a88447d229a0d359aedabc`;
- clone filter: `blob:none`;
- shallow, sparse participant workspace; initial on-disk size was approximately 15.6 MB;
- sparse paths include official contract/tooling plus only `submissions/JerrySkywalker/jingzhang-in-place`;
- branch works against fork `origin`, canonical `upstream`.

## Skill and environment

```text
skill_target=C:\Users\jerry\.codex\skills\urban-design-ai-submission
skill_check=PASS
skill_tree_digest=758fdb076fe54e645a7f4d2ff34dc003e03ba7e6466d353b5212203f85f02a2b
python=CPython 3.12.13
environment=V:\src\haidian\.venv
installer=uv 0.12.2
```

Review dependencies are isolated in `.venv`: `jsonschema 4.26.0`, `Pillow 12.3.0`, `pyproj 3.7.2`, `shapely 2.1.2`. Export/QA additions are `ReportLab 5.0.0`, `pdfplumber 0.11.10`, `pypdf 6.15.0` and their local transitive dependencies. No system-wide application was installed.

## Export stack

```text
FIGURE_EXPORTER=Python 3.12 + Pillow 12.3.0 + deterministic participant builder
PDF_EXPORTER=ReportLab 5.0.0
HTML_RENDERER=official scripts/render_proposal_html.py plus offline static visual shell
BILINGUAL_FONT_STRATEGY=system Microsoft YaHei for Chinese and Arial for English; SimHei/built-in sans fallback; fonts not redistributed
```

Poppler from the installed MiKTeX runtime is used only for QA rendering. The smoke export produced Chinese/English vector/text diagrams as PNG, correct A3/A0 PDFs, paired report HTML and paired offline visual HTML without CDN, remote font, tile or script dependencies.

The production builder and SHA receipt live in design-lab rather than the formal package because the official package path allowlist rejects participant `.py` and JSON files under `assets/`. This contract discovery was fixed before the final validator baseline.
