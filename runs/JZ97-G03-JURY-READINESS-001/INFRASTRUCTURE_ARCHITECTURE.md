# G03 Anchor Jury Infrastructure Architecture

## 1. Physical Isolation & Windows Sandbox

Physical isolation is achieved through disposable Windows Sandbox containers with strict host barrier configurations:

- **Isolated Ephemeral Environments**: Each reviewer executes in an independent Windows Sandbox instance.
- **Hardware Isolation**:
  - `VGpu: Disable` (eliminates GPU state sharing)
  - `ProtectedClient: Enable` (enhanced security container)
  - `ClipboardRedirection: Disable` (prevents host-guest clipboard leakage)
  - `PrinterRedirection: Disable`
  - `AudioInput / VideoInput: Disable`
- **Network Access**:
  - `Networking: Enable` (strictly required for in-sandbox AGY device OAuth authentication with model providers)
- **Directory Air Gap**:
  - Host filesystems `V:\`, `C:\Users\jerry`, and other reviewer directories are completely invisible to the sandbox container.

---

## 2. Multi-Anchor Storage & Partitioning

Packets are stored under `V:\src\_review_isolation\packets\` with 7 neutral identifiers:
- `N4` (Baseline 77)
- `X8` (Strong 86)
- `B2` (High-A 90)
- `W7` (High-B 90)
- `J9` (Ceiling 96)
- `L5` (Backup-A 90)
- `P3` (Backup-B 91)

Output structure is cleanly partitioned by reviewer and anchor ID:

```text
V:\src\_review_isolation\
 ├── output-a\
 │    ├── N4\scorecard.json, scoring-log.txt
 │    ├── X8\scorecard.json, scoring-log.txt
 │    └── ... (7 anchors)
 ├── output-b\
 │    ├── N4\scorecard.json, scoring-log.txt
 │    └── ... (7 anchors)
 ├── output-c\
 │    ├── N4\scorecard.json, scoring-log.txt
 │    └── ... (7 anchors)
 └── output-tb\
      └── <AnchorId>\scorecard.json (if invoked)
```

---

## 3. Cross-Anchor Memory Sanitization

Inside `reviewer-runner-agy.ps1`, when `-Anchor All` or multiple anchors are evaluated in the same Sandbox session:
Before each anchor evaluation, the script forcefully deletes:
- `C:\AgyHome\brain`
- `C:\AgyHome\antigravity-cli\brain`

This ensures that the AGY CLI starts with a clean slate for each anchor, eliminating cross-anchor conversation history or memory bleeding.

---

## 4. Deterministic Scoring & Schema Validation

Each scorecard returned by the model is parsed and strictly validated against `SCORECARD_SCHEMA.json`:
1. Validates all 7 dimension IDs:
   - `brief_alignment` (weight: 20)
   - `originality` (weight: 10)
   - `ai_planning_innovation` (weight: 15)
   - `implementation_feasibility` (weight: 20)
   - `public_interest_inclusion` (weight: 10)
   - `risk_compliance` (weight: 10)
   - `expression_completeness` (weight: 15)
2. Validates that every score is an integer $\in \{0, 1, 2, 3, 4, 5\}$.
3. Computes the deterministic total weighted score:
   $$\text{total\_weighted\_score} = \sum_{i=1}^{7} \left(\frac{\text{score}_i}{5.0} \times \text{weight}_i\right)$$
4. Stores visual surfaces inspected and structured rationale.
