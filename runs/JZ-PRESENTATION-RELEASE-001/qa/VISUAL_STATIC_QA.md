# Visual HTML Static QA

## Local HTTP admission

The offline pages were served locally only for QA:

```text
http://127.0.0.1:8765/visual/index.html    HTTP 200
http://127.0.0.1:8765/visual/index.en.html HTTP 200
```

The final pages are static and contain no CDN, remote font, map tile, API,
form, tracker or script dependency.

## Responsive/accessibility static checks

- Wide, normal-laptop and narrow CSS paths are declared; below 850 px, the
  spatial/story grids collapse to one column and the audit metrics stack.
- Both pages expose a skip link, visible `:focus-visible` navigation state,
  visible native `summary` focus, native `<details>`, reduced-motion fallback,
  semantic heading hierarchy and image alt text.
- Static inspection confirms reader-language parity and required gate markers.

The connected in-app browser did not expose an interactive tab/session, so a
browser-rendered screenshot could not be captured through the approved browser
bridge. This is a QA-transport limitation, not a dependency of the submitted
offline pages; the two local HTML paths remain the review targets.
