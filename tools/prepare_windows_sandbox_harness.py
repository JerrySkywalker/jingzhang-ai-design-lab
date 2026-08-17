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

RUNNER = r'''param([Parameter(Mandatory=$true)][ValidateSet("A","B","C")][string]$Reviewer)
$ErrorActionPreference = "Stop"
$env:CODEX_HOME = "C:\CodexHome"
New-Item -ItemType Directory -Path $env:CODEX_HOME -Force | Out-Null
$node = "C:\ReviewerRuntime\node.exe"
$cli = "C:\ReviewerRuntime\codex\bin\codex.js"
Write-Host "Owner: complete normal subscription device sign-in in this fresh Sandbox only. Do not use API-key login."
& $node $cli login --device-auth
$images = @(Get-ChildItem -LiteralPath "C:\ReviewPacket\visual-surfaces" -File | Sort-Object Name | ForEach-Object { $_.FullName })
Get-Content -LiteralPath "C:\ReviewPacket\HARNESS_TEST_PROMPT.md" -Raw | & $node $cli exec --ephemeral --ignore-user-config --ignore-rules --skip-git-repo-check --disable apps --disable plugins --disable browser_use --disable browser_use_external --disable computer_use --disable in_app_browser --disable remote_plugin --disable skill_search -C "C:\ReviewPacket" -s read-only --output-schema "C:\ReviewPacket\SCORECARD_SCHEMA.json" -o "C:\ReviewerOutput\harness-test-only.json" -i $images -
'''

def wsb(packet: Path, runtime: Path, output: Path, reviewer: str, probe: bool) -> str:
    command = f"powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:\\ReviewerRuntime\\confinement-probe.ps1 -Reviewer {reviewer}" if probe else "powershell.exe -NoExit -NoProfile -ExecutionPolicy Bypass -Command \"Set-Location C:\\ReviewerRuntime; Write-Host 'Run reviewer-runner.ps1 -Reviewer " + reviewer + " after Owner sign-in.'\""
    return f'''<Configuration>
  <VGpu>Disable</VGpu><Networking>Default</Networking><ClipboardRedirection>Disable</ClipboardRedirection><PrinterRedirection>Disable</PrinterRedirection><AudioInput>Disable</AudioInput><VideoInput>Disable</VideoInput>
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
        (sandbox / f"reviewer-{reviewer.lower()}.wsb").write_text(wsb(packet, runtime, output, reviewer, False), encoding="utf-8")
        (sandbox / f"probe-{reviewer.lower()}.wsb").write_text(wsb(packet, runtime, output, reviewer, True), encoding="utf-8")
    print(layout)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
