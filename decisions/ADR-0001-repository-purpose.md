# ADR-0001: Separate Persistent Design Lab from Formal Submission Fork

- **Status:** Accepted
- **Date:** 2026-08-11

## Context

The design process is expected to span many AI/human sessions, while the official submission repository has strict file-scope and validation requirements. Relying on conversational context risks losing design rationale; storing exploratory governance and research directly in the official fork risks polluting the eventual PR.

## Decision

Use `JerrySkywalker/jingzhang-ai-design-lab` as the public persistent design-memory repository. Use a separate future fork of `open-city-ai/haidian` for the formal participant workspace and PR.

## Consequences

Positive:

- ideas and rejected alternatives remain inspectable;
- owner decisions survive chat-context loss;
- benchmark/source research can evolve independently;
- formal PR scope stays clean.

Trade-offs:

- selected information must later be migrated intentionally;
- canonical competition rules must still be refreshed from upstream rather than copied here;
- duplicate stale facts are a risk, so this lab stores pointers and dated interpretations rather than pretending to be canonical.
