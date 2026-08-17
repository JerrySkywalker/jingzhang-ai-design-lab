#!/usr/bin/env python3
"""Prepare a least-material Windows Sandbox reviewer layout without host auth."""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


PROBE = r'''param([Parameter(Mandatory=$true)][ValidateSet("A","B","C")][string]$Reviewer)
$ErrorActionPreference = "Stop"
$output = "C:\ReviewerOutput\confinement-probe.json"
$result = [ordered]@{
  reviewer = $Reviewer
  packet_readable = Test-Path -LiteralPath "C:\ReviewPacket\REVIEW_PACKET_MANIFEST.json"
  v_drive_visible = Test-Path -LiteralPath "V:\src"
  host_profile_visible = Test-Path -LiteralPath "C:\Users\jerry"
  host_codex_home_visible = Test-Path -LiteralPath "C:\Users\jerry\.codex"
  host_canary_directory_visible = Test-Path -LiteralPath "V:\src\_reviewer-isolation-canary"
  other_reviewer_output_visible = ((Test-Path -LiteralPath "C:\ReviewerOutput-B") -or (Test-Path -LiteralPath "C:\ReviewerOutput-C"))
  filesystem_roots = @(Get-PSDrive -PSProvider FileSystem | ForEach-Object { $_.Root })
  runtime_version = $null
  runtime_version_ok = $false
}
try {
  $result.runtime_version = (& "C:\ReviewerRuntime\node.exe" "C:\ReviewerRuntime\codex\bin\codex.js" --version 2>$null | Select-Object -First 1)
  $result.runtime_version_ok = [bool]$result.runtime_version
} catch { $result.runtime_version = "unavailable" }
$result | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath $output -Encoding utf8
Start-Sleep -Seconds 3
Stop-Computer -Force
'''

RUNNER = r'''param(
  [Parameter(Mandatory=$true)][ValidateSet("A","B","C")][string]$Reviewer,
  [Parameter(Mandatory=$true)][ValidateSet("Probe","HarnessTest")][string]$Mode
)
$ErrorActionPreference = "Stop"
$env:CODEX_HOME = "C:\CodexHome"
New-Item -ItemType Directory -Path $env:CODEX_HOME -Force | Out-Null
$node = "C:\ReviewerRuntime\node.exe"
$cli = "C:\ReviewerRuntime\codex\bin\codex.js"
Write-Host "Owner: complete normal subscription device sign-in in this fresh Sandbox only. Do not use API-key login."
& $node $cli login --device-auth
$loginExit = $LASTEXITCODE
if ($loginExit -ne 0) { throw "Subscription device sign-in failed with exit code $loginExit." }
$env:CODEX_SANDBOX_NETWORK_DISABLED = "1"
$images = @(Get-ChildItem -LiteralPath "C:\ReviewPacket\visual-surfaces" -File | Sort-Object Name | ForEach-Object { $_.FullName })
if ($Mode -eq "Probe") {
  $probe = @"
You are conducting a NON-SCORING confinement and host-context probe for CANDIDATE-X.

Use only read-only shell checks in this Sandbox. Enumerate accessible filesystem roots and confirm that C:\ReviewPacket\REVIEW_PACKET_MANIFEST.json is readable. Test existence only; do not read contents, search recursively, or guess identifiers for these paths: V:\src, C:\Users\jerry, C:\Users\jerry\.codex, V:\src\_reviewer-isolation-canary, C:\ReviewerOutput-B, and C:\ReviewerOutput-C.

Do not use the network, web search, MCP, apps, plugins, browser, external documents, Git, or any resume command. Do not score the proposal or discuss its quality. Neutral question: identify the candidate only from this packet and state every project-history or prior-review fact you used; if none is supplied, say none.

Return only these key=value lines, with true or false values and no prose before or after:
probe_type=NON_SCORING_CONFINEMENT
candidate_id=CANDIDATE-X
filesystem_roots=<comma-separated roots>
packet_manifest_readable=<true|false>
v_src_accessible=<true|false>
host_profile_accessible=<true|false>
host_codex_home_accessible=<true|false>
other_reviewer_output_accessible=<true|false>
project_history_or_prior_review_facts_used=<none|comma-separated facts>
proposal_scored=false
network_or_external_lookup_attempted=false
"@
  $probe | & $node $cli exec --ephemeral --ignore-user-config --ignore-rules --skip-git-repo-check --ask-for-approval never --disable apps --disable plugins --disable hooks --disable browser_use --disable browser_use_external --disable computer_use --disable in_app_browser --disable remote_plugin --disable skill_search -c 'sandbox_workspace_write.network_access=false' -C "C:\ReviewPacket" -s read-only -o "C:\ReviewerOutput\reviewer-confinement-probe.txt" -
} else {
  $harness = (Get-Content -LiteralPath "C:\ReviewPacket\HARNESS_TEST_PROMPT.md" -Raw) + "`nAssigned reviewer_id=$Reviewer."
  $harness | & $node $cli exec --ephemeral --ignore-user-config --ignore-rules --skip-git-repo-check --ask-for-approval never --disable apps --disable plugins --disable hooks --disable browser_use --disable browser_use_external --disable computer_use --disable in_app_browser --disable remote_plugin --disable skill_search -c 'sandbox_workspace_write.network_access=false' -C "C:\ReviewPacket" -s read-only --output-schema "C:\ReviewPacket\SCORECARD_SCHEMA.json" -o "C:\ReviewerOutput\harness-test-only.json" -i $images -
}
$execExit = $LASTEXITCODE
if ($execExit -ne 0) { throw "Codex $Mode execution failed with exit code $execExit." }
'''

def wsb(packet: Path, runtime: Path, output: Path, reviewer: str, mode: str) -> str:
    if mode == "platform-probe":
        command = f"powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:\\ReviewerRuntime\\confinement-probe.ps1 -Reviewer {reviewer}"
        networking = "Disable"
    elif mode == "reviewer-probe":
        command = "powershell.exe -NoExit -NoProfile -ExecutionPolicy Bypass -Command \"Set-Location C:\\ReviewerRuntime; Write-Host 'Run reviewer-runner.ps1 -Reviewer " + reviewer + " -Mode Probe after Owner sign-in.'\""
        networking = "Enable"
    elif mode == "harness-test":
        command = "powershell.exe -NoExit -NoProfile -ExecutionPolicy Bypass -Command \"Set-Location C:\\ReviewerRuntime; Write-Host 'Run reviewer-runner.ps1 -Reviewer " + reviewer + " -Mode HarnessTest after Owner sign-in.'\""
        networking = "Enable"
    else:
        raise ValueError(mode)
    return f'''<Configuration>
  <VGpu>Disable</VGpu><Networking>{networking}</Networking><ClipboardRedirection>Disable</ClipboardRedirection><PrinterRedirection>Disable</PrinterRedirection><AudioInput>Disable</AudioInput><VideoInput>Disable</VideoInput><ProtectedClient>Enable</ProtectedClient>
  <MappedFolders>
    <MappedFolder><HostFolder>{packet}</HostFolder><SandboxFolder>C:\\ReviewPacket</SandboxFolder><ReadOnly>true</ReadOnly></MappedFolder>
    <MappedFolder><HostFolder>{runtime}</HostFolder><SandboxFolder>C:\\ReviewerRuntime</SandboxFolder><ReadOnly>true</ReadOnly></MappedFolder>
    <MappedFolder><HostFolder>{output}</HostFolder><SandboxFolder>C:\\ReviewerOutput</SandboxFolder><ReadOnly>false</ReadOnly></MappedFolder>
  </MappedFolders>
  <LogonCommand><Command>{command}</Command></LogonCommand>
</Configuration>\n'''


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--layout", required=True, type=Path)
    parser.add_argument("--packet-source", required=True, type=Path)
    parser.add_argument("--node", required=True, type=Path)
    parser.add_argument("--codex-package", required=True, type=Path)
    args = parser.parse_args()
    layout = args.layout.resolve()
    if layout.exists():
        raise SystemExit(f"refusing to overwrite existing harness layout: {layout}")
    if not args.packet_source.is_dir() or not args.node.is_file() or not args.codex_package.is_dir():
        raise SystemExit("packet source, node executable, and codex package must exist")
    packet, runtime, sandbox = layout / "packet", layout / "runtime", layout / "sandbox"
    shutil.copytree(args.packet_source, packet)
    runtime.mkdir(parents=True)
    shutil.copy2(args.node, runtime / "node.exe")
    shutil.copytree(args.codex_package, runtime / "codex")
    (runtime / "confinement-probe.ps1").write_text(PROBE, encoding="utf-8")
    (runtime / "reviewer-runner.ps1").write_text(RUNNER, encoding="utf-8")
    sandbox.mkdir()
    for reviewer in "ABC":
        output = layout / f"output-{reviewer.lower()}"
        output.mkdir()
        (sandbox / f"reviewer-{reviewer.lower()}.wsb").write_text(wsb(packet, runtime, output, reviewer, "reviewer-probe"), encoding="utf-8")
        (sandbox / f"probe-{reviewer.lower()}.wsb").write_text(wsb(packet, runtime, output, reviewer, "platform-probe"), encoding="utf-8")
    (sandbox / "harness-test-a.wsb").write_text(wsb(packet, runtime, layout / "output-a", "A", "harness-test"), encoding="utf-8")
    print(layout)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
