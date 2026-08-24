[CmdletBinding()]
param(
    [ValidateSet('Prepare', 'Preflight', 'Review', 'Anchors', 'Calibrate', 'Candidates', 'Shadow', 'Normalize', 'Analyze', 'All')]
    [string]$Action = 'All',
    [string]$RuntimeRoot = 'V:\src\_review_isolation\codex-native\JZ97-CODEX-NATIVE-CUTOVER-AND-CONVERGENCE-001',
    [string]$SourcePacketsRoot = 'V:\src\_review_isolation\packets',
    [string]$ProductRepo = 'V:\src\haidian',
    [ValidatePattern('^P[0-9]{2}$')]
    [string]$PacketId,
    [ValidateSet('PRIMARY', 'CHALLENGER', 'HOLDOUT')]
    [string]$ReviewerRole,
    [ValidateRange(1, 8)]
    [int]$MaxParallel = 4
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$ScriptRoot = Split-Path -Parent $PSCommandPath
$RepoRoot = (Resolve-Path (Join-Path $ScriptRoot '..\..')).Path
$SchemaPath = Join-Path $ScriptRoot 'schema\scorecard.schema.json'
$PromptPath = Join-Path $ScriptRoot 'prompts\reviewer.md'
$RubricPath = Join-Path $RepoRoot 'runs\JZ97-G01-G02-OFFICIAL-TRUTH-AND-ANCHOR-CORPUS-001\G01_CURRENT_OFFICIAL_RUBRIC.md'
$LegacySchemaPath = Join-Path $RepoRoot 'runs\JZ97-G01-G02-OFFICIAL-TRUTH-AND-ANCHOR-CORPUS-001\SCORECARD_SCHEMA.json'
$PacketRoot = Join-Path $RuntimeRoot 'packets'
$RawRoot = Join-Path $RuntimeRoot 'raw'
$OutputRoot = Join-Path $RuntimeRoot 'output'
$CoordinatorRoot = Join-Path $RuntimeRoot 'coordinator'
$RunOutputRoot = Join-Path $RepoRoot 'runs\JZ97-CODEX-NATIVE-CUTOVER-AND-CONVERGENCE-001'
$SubmissionPath = 'submissions/JerrySkywalker/jingzhang-in-place'

$Dimensions = @(
    'brief_alignment',
    'originality',
    'ai_planning_innovation',
    'implementation_feasibility',
    'public_interest_inclusion',
    'risk_compliance',
    'expression_completeness'
)
$Weights = [ordered]@{
    brief_alignment = 4
    originality = 2
    ai_planning_innovation = 3
    implementation_feasibility = 4
    public_interest_inclusion = 2
    risk_compliance = 2
    expression_completeness = 3
}
$Profiles = [ordered]@{
    PRIMARY = [ordered]@{ model = 'gpt-5.6-sol'; requested_alias = 'gpt-5.6'; resolved_model = 'gpt-5.6-sol'; reasoning = 'max' }
    CHALLENGER = [ordered]@{ model = 'gpt-5.6-terra'; resolved_model = 'gpt-5.6-terra'; reasoning = 'xhigh' }
    HOLDOUT = [ordered]@{ model = 'gpt-5.6-sol'; resolved_model = 'gpt-5.6-sol'; reasoning = 'xhigh' }
}
$PacketMap = [ordered]@{
    P01 = [ordered]@{ class = 'ANCHOR'; source_id = 'N4'; official_score = 77; source_head = '1d5cb1aaa9d76edc3532e593c803cb936070a744' }
    P02 = [ordered]@{ class = 'ANCHOR'; source_id = 'X8'; official_score = 86; source_head = 'e5ec8ebcfd0aa29e71dd671752b07a514d7c88b9' }
    P03 = [ordered]@{ class = 'ANCHOR'; source_id = 'B2'; official_score = 90; source_head = '9622d10034440fa6e14713c7ba3dcf27756f7091' }
    P04 = [ordered]@{ class = 'ANCHOR'; source_id = 'W7'; official_score = 90; source_head = 'f32f3c7d678d92bc931f621a64f5ea7c9896085a' }
    P05 = [ordered]@{ class = 'ANCHOR'; source_id = 'J9'; official_score = 96; source_head = '30a6f44d564177d5ff53b7501b44ecddb90ce8ca' }
    P06 = [ordered]@{ class = 'CANDIDATE'; source_id = 'V041A'; source_head = '94c51f2011a365a1cb2674a62f8cc3af7aba59e5' }
    P07 = [ordered]@{ class = 'CANDIDATE'; source_id = 'V042'; source_head = 'a489aa56e07a206e308fd53d6c3dbdf44dcf1f89' }
    P08 = [ordered]@{ class = 'SHADOW'; source_id = 'FROZEN_SHADOW_V043'; source_head = '31d9ee0dba3fc81ca3d9c4a09d9dad86474d328f' }
}

function Write-JsonFile {
    param([Parameter(Mandatory)]$Value, [Parameter(Mandatory)][string]$Path, [int]$Depth = 20)
    $parent = Split-Path -Parent $Path
    if ($parent -and -not (Test-Path -LiteralPath $parent)) {
        New-Item -ItemType Directory -Path $parent -Force | Out-Null
    }
    $Value | ConvertTo-Json -Depth $Depth | Set-Content -LiteralPath $Path -Encoding utf8NoBOM
}

function Get-Sha256 {
    param([Parameter(Mandatory)][string]$Path)
    (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToLowerInvariant()
}

function Get-DeterministicTotal {
    param([Parameter(Mandatory)]$Scorecard)
    $total = 0
    foreach ($dimension in $Dimensions) {
        $value = $Scorecard.$dimension
        if ($value -isnot [int] -and $value -isnot [long]) {
            throw "$dimension must be an integer"
        }
        if ($value -lt 0 -or $value -gt 5) {
            throw "$dimension is outside 0..5"
        }
        $total += [int]$value * [int]$Weights[$dimension]
    }
    return $total
}

function Get-IdentityValues {
    param([Parameter(Mandatory)][string]$SourcePath)
    $values = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
    $identityKey = '(?i)(agent_id|agent_name|human_contributor|author_github|author_display|author_name|creator|contributor)'
    Get-ChildItem -LiteralPath $SourcePath -Recurse -File | Where-Object {
        $_.Extension.ToLowerInvariant() -in @('.json', '.md', '.html', '.txt', '.yaml', '.yml')
    } | ForEach-Object {
        $text = Get-Content -LiteralPath $_.FullName -Raw -ErrorAction SilentlyContinue
        if (-not $text) { return }
        foreach ($match in [regex]::Matches($text, '"' + $identityKey + '"\s*:\s*"([^"\r\n]+)"')) {
            $candidate = $match.Groups[2].Value.Trim()
            if ($candidate.Length -ge 3) { [void]$values.Add($candidate) }
        }
        foreach ($match in [regex]::Matches($text, '(?im)^\s*' + $identityKey + '\s*:\s*["'']?([^"''\r\n]+)')) {
            $candidate = $match.Groups[2].Value.Trim()
            if ($candidate.Length -ge 3) { [void]$values.Add($candidate) }
        }
        foreach ($match in [regex]::Matches($text, '(?i)\b([a-z0-9_-]{3,})/jingzhang-[a-z0-9_-]+\b')) {
            [void]$values.Add($match.Groups[0].Value)
        }
    }
    return @($values)
}

function New-SanitizedPacket {
    param(
        [Parameter(Mandatory)][string]$SourcePath,
        [Parameter(Mandatory)][string]$DestinationPath,
        [Parameter(Mandatory)][string]$NeutralPacketId
    )
    if (-not (Test-Path -LiteralPath $SourcePath -PathType Container)) {
        throw "Source packet is missing: $SourcePath"
    }
    if (Test-Path -LiteralPath $DestinationPath) {
        throw "Refusing to overwrite prepared packet: $DestinationPath"
    }

    $identityValues = Get-IdentityValues -SourcePath $SourcePath
    New-Item -ItemType Directory -Path $DestinationPath -Force | Out-Null
    Copy-Item -Path (Join-Path $SourcePath '*') -Destination $DestinationPath -Recurse -Force

    $dropNames = @(
        'agent.json',
        'changelog.md',
        'copyright_statement.md',
        'REVIEW_PACKET_MANIFEST.json',
        'SCORECARD_SCHEMA.json',
        'REVIEWER_PROBE_PROMPT.md',
        'HARNESS_TEST_PROMPT.md'
    )
    Get-ChildItem -LiteralPath $DestinationPath -Recurse -File | Where-Object {
        $_.Name -in $dropNames -or $_.Extension.ToLowerInvariant() -eq '.pdf'
    } | Remove-Item -Force

    $textFiles = Get-ChildItem -LiteralPath $DestinationPath -Recurse -File | Where-Object {
        $_.Extension.ToLowerInvariant() -in @('.json', '.md', '.html', '.geojson', '.txt', '.yaml', '.yml', '.csv')
    }
    foreach ($file in $textFiles) {
        $text = Get-Content -LiteralPath $file.FullName -Raw
        foreach ($identity in $identityValues) {
            if ($identity) {
                $text = [regex]::Replace($text, [regex]::Escape($identity), '[IDENTITY_REDACTED]', 'IgnoreCase')
            }
        }
        $text = [regex]::Replace($text, '(?im)^(\s*(?:author_github|author_display|author_name|human_contributor|agent_id|agent_name|creator|contributor)\s*:\s*).+$', '$1"[IDENTITY_REDACTED]"')
        $text = [regex]::Replace($text, '(?i)\bv\d+\.\d+(?:\.\d+)?[a-z]?\b', '[VERSION_REDACTED]')
        $text = [regex]::Replace($text, '(?i)\b(?:PR|pull request)\s*#?\d+\b', '[REVIEW_REFERENCE_REDACTED]')
        $text = [regex]::Replace($text, '\b[0-9a-fA-F]{40}\b', '[SOURCE_REVISION_REDACTED]')
        $text = [regex]::Replace($text, '(?i)\b(?:official|trusted|prior)\s+score\s*[:=]?\s*\d{1,3}\b', '[SCORE_REDACTED]')
        Set-Content -LiteralPath $file.FullName -Value $text -Encoding utf8NoBOM -NoNewline
    }

    "CANDIDATE $NeutralPacketId`n`nNeutral fixed evaluation packet. Review only this directory." |
        Set-Content -LiteralPath (Join-Path $DestinationPath 'CANDIDATE_CONTEXT.md') -Encoding utf8NoBOM

    $records = @()
    Get-ChildItem -LiteralPath $DestinationPath -Recurse -File | Sort-Object FullName | ForEach-Object {
        $relative = [System.IO.Path]::GetRelativePath($DestinationPath, $_.FullName).Replace('\', '/')
        $records += [ordered]@{
            relative_path = $relative
            size = $_.Length
            sha256 = Get-Sha256 -Path $_.FullName
        }
    }
    $canonical = $records | ConvertTo-Json -Depth 5 -Compress
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($canonical)
    $packetHash = [Convert]::ToHexString([System.Security.Cryptography.SHA256]::HashData($bytes)).ToLowerInvariant()
    $manifest = [ordered]@{
        schema_version = '1.0.0'
        packet_id = $NeutralPacketId
        packet_hash = $packetHash
        packet_file_count = $records.Count
        identity_redaction_applied = $true
        source_mapping_exposed = $false
        files = $records
    }
    Write-JsonFile -Value $manifest -Path (Join-Path $DestinationPath 'NEUTRAL_PACKET_MANIFEST.json')

    $forbiddenPatterns = @(
        '(?i)JerrySkywalker|jiangmuran|RootReturn0|Fritho',
        '(?i)\b(?:official|trusted|prior)\s+score\s*[:=]?\s*\d{1,3}\b',
        '(?i)\b(?:PR|pull request)\s*#?\d+\b',
        '\b[0-9a-fA-F]{40}\b',
        '(?i)\bv0\.4\.[0-9a-z]*\b'
    )
    foreach ($file in (Get-ChildItem -LiteralPath $DestinationPath -Recurse -File | Where-Object { $_.Extension.ToLowerInvariant() -in @('.json', '.md', '.html', '.geojson', '.txt', '.yaml', '.yml', '.csv') })) {
        $text = Get-Content -LiteralPath $file.FullName -Raw
        foreach ($pattern in $forbiddenPatterns) {
            if ($text -match $pattern) {
                throw "Blinding audit failed for $($file.FullName): $pattern"
            }
        }
    }
    Write-Host "PREPARED packet=$NeutralPacketId hash=$packetHash files=$($records.Count) identities_redacted=$($identityValues.Count)"
}

function Build-RawCandidatePacket {
    param([Parameter(Mandatory)][string]$NeutralPacketId)
    $entry = $PacketMap[$NeutralPacketId]
    $rawPath = Join-Path $RawRoot $NeutralPacketId
    if (Test-Path -LiteralPath $rawPath) {
        if (Test-Path -LiteralPath (Join-Path $rawPath 'REVIEW_PACKET_MANIFEST.json')) {
            Write-Host "PRESERVED raw packet=$NeutralPacketId"
            return $rawPath
        }
        throw "Incomplete raw packet already exists: $rawPath"
    }
    $builder = Join-Path $RepoRoot 'tools\build_anchor_packets.py'
    $builderOutput = & python $builder --repo $ProductRepo --head $entry.source_head --sub-path $SubmissionPath --neutral-id $NeutralPacketId --out-dir $rawPath --rubric $RubricPath --schema $LegacySchemaPath
    if ($LASTEXITCODE -ne 0) { throw "Packet builder failed for $NeutralPacketId" }
    Write-Host "BUILT raw packet=$NeutralPacketId details=$($builderOutput -join '')"
    return $rawPath
}

function Invoke-Prepare {
    foreach ($path in @($RuntimeRoot, $PacketRoot, $RawRoot, $OutputRoot, $CoordinatorRoot)) {
        if (-not (Test-Path -LiteralPath $path)) { New-Item -ItemType Directory -Path $path -Force | Out-Null }
    }
    Write-JsonFile -Value $PacketMap -Path (Join-Path $CoordinatorRoot 'packet-map.json')
    foreach ($id in $PacketMap.Keys) {
        $destination = Join-Path $PacketRoot $id
        if (Test-Path -LiteralPath $destination) {
            Write-Host "PRESERVED prepared packet=$id"
            continue
        }
        $entry = $PacketMap[$id]
        if ($entry.class -eq 'ANCHOR') {
            $source = Join-Path $SourcePacketsRoot $entry.source_id
        } else {
            $source = Build-RawCandidatePacket -NeutralPacketId $id
        }
        New-SanitizedPacket -SourcePath $source -DestinationPath $destination -NeutralPacketId $id
    }
}

function Invoke-Preflight {
    $version = (& codex --version).Trim()
    $help = & codex exec --help
    foreach ($flag in @('--ephemeral', '--sandbox', '--ignore-user-config', '--ignore-rules', '--output-schema', '--model')) {
        if (($help -join "`n") -notmatch [regex]::Escape($flag)) { throw "Installed Codex CLI lacks $flag" }
    }
    $catalog = (& codex debug models | ConvertFrom-Json).models
    foreach ($role in @('PRIMARY', 'CHALLENGER')) {
        $profile = $Profiles[$role]
        $catalogEntry = $catalog | Where-Object slug -eq $profile.resolved_model | Select-Object -First 1
        if (-not $catalogEntry) { throw "Model missing from installed catalog: $($profile.resolved_model)" }
        if ($catalogEntry.supported_reasoning_levels.effort -notcontains $profile.reasoning) {
            throw "Unsupported reasoning setting $($profile.reasoning) for $($profile.resolved_model)"
        }
    }
    $schema = Get-Content -LiteralPath $SchemaPath -Raw | ConvertFrom-Json
    foreach ($property in $schema.properties.psobject.Properties) {
        $propertyNames = @($property.Value.psobject.Properties.Name)
        if ($propertyNames -notcontains 'type' -and $propertyNames -notcontains '$ref') {
            throw "Output schema property lacks explicit type or ref: $($property.Name)"
        }
    }
    $schemaHash = Get-Sha256 -Path $SchemaPath
    $schemaHashPrefix = $schemaHash.Substring(0, 12)
    $probeRoot = Join-Path $CoordinatorRoot 'schema-probes'
    if (-not (Test-Path -LiteralPath $probeRoot)) { New-Item -ItemType Directory -Path $probeRoot -Force | Out-Null }
    foreach ($role in @('PRIMARY', 'CHALLENGER')) {
        $profile = $Profiles[$role]
        $slug = $role.ToLowerInvariant()
        $probeOutput = Join-Path $probeRoot "$slug.$schemaHashPrefix.output.json"
        $probeReceipt = Join-Path $probeRoot "$slug.$schemaHashPrefix.receipt.json"
        $probeLog = Join-Path $probeRoot "$slug.$schemaHashPrefix.codex.log"
        if (Test-Path -LiteralPath $probeReceipt) {
            $priorProbe = Get-Content -LiteralPath $probeReceipt -Raw | ConvertFrom-Json
            if ($priorProbe.status -ne 'PASS') { throw "Prior schema probe is not PASS for $role" }
            continue
        }
        $probe = [ordered]@{
            probe_class = 'CAPABILITY_PROBE_ONLY'
            discarded_for_scoring = $true
            role = $role
            model = $profile.model
            reasoning = $profile.reasoning
            schema_sha256 = $schemaHash
            status = 'STARTED'
            started_at = (Get-Date).ToUniversalTime().ToString('o')
        }
        Write-JsonFile -Value $probe -Path $probeReceipt
        $probePrompt = "CAPABILITY_PROBE_ONLY. Do not inspect files and do not score anything. Return a schema-conformance sample with reviewer_role HOLDOUT, model $($profile.model), packet_id P00, every dimension 0, weighted_total 0, top_strengths and top_deficiencies each containing one string CAPABILITY_PROBE_ONLY, blocking_issue NONE, and formal_local_evidence true."
        $reasoningConfig = 'model_reasoning_effort="' + $profile.reasoning + '"'
        $probeArgs = @(
            'exec', '--ephemeral', '--sandbox', 'read-only', '--ignore-user-config', '--ignore-rules',
            '--output-schema', $SchemaPath, '--model', $profile.model, '-c', $reasoningConfig,
            '--cd', $probeRoot, '--skip-git-repo-check', '--output-last-message', $probeOutput, '-'
        )
        $probePrompt | & codex @probeArgs 2>&1 | Tee-Object -LiteralPath $probeLog | Out-Host
        $probeExit = $LASTEXITCODE
        if ($probeExit -ne 0 -or -not (Test-Path -LiteralPath $probeOutput)) {
            $probe.status = 'FAILED'
            $probe.exit_code = $probeExit
            $probe.completed_at = (Get-Date).ToUniversalTime().ToString('o')
            Write-JsonFile -Value $probe -Path $probeReceipt
            throw "Schema transport probe failed for $role"
        }
        $probeCard = Get-Content -LiteralPath $probeOutput -Raw | ConvertFrom-Json
        if ($probeCard.packet_id -ne 'P00' -or [int]$probeCard.weighted_total -ne 0) {
            throw "Schema transport probe envelope mismatch for $role"
        }
        $probe.status = 'PASS'
        $probe.exit_code = $probeExit
        $probe.completed_at = (Get-Date).ToUniversalTime().ToString('o')
        Write-JsonFile -Value $probe -Path $probeReceipt
    }
    $receipt = [ordered]@{
        codex_native_panel = 'READY'
        codex_cli_version = $version
        required_flags = @('--ephemeral', '--sandbox read-only', '--ignore-user-config', '--ignore-rules', '--output-schema', '--model')
        primary = $Profiles.PRIMARY
        challenger = $Profiles.CHALLENGER
        schema_transport_probes = 'PASS'
        mcp_used = $false
        tui_used = $false
        checked_at = (Get-Date).ToUniversalTime().ToString('o')
    }
    Write-JsonFile -Value $receipt -Path (Join-Path $CoordinatorRoot 'preflight.json')
    Write-Host "PREFLIGHT PASS codex=$version primary=$($Profiles.PRIMARY.model)/$($Profiles.PRIMARY.reasoning) challenger=$($Profiles.CHALLENGER.model)/$($Profiles.CHALLENGER.reasoning)"
}

function Invoke-OneReview {
    param([Parameter(Mandatory)][string]$NeutralPacketId, [Parameter(Mandatory)][string]$Role)
    if (-not $PacketMap.Contains($NeutralPacketId)) { throw "Unknown packet id: $NeutralPacketId" }
    if (-not $Profiles.Contains($Role)) { throw "Unknown reviewer role: $Role" }
    $packetPath = Join-Path $PacketRoot $NeutralPacketId
    if (-not (Test-Path -LiteralPath $packetPath -PathType Container)) { throw "Prepared packet missing: $packetPath" }

    $roleSlug = $Role.ToLowerInvariant()
    $attemptPath = Join-Path $OutputRoot "$NeutralPacketId.$roleSlug.attempt.json"
    $rawPath = Join-Path $OutputRoot "$NeutralPacketId.$roleSlug.raw.json"
    $scorecardPath = Join-Path $OutputRoot "$NeutralPacketId.$roleSlug.scorecard.json"
    $logPath = Join-Path $OutputRoot "$NeutralPacketId.$roleSlug.codex.log"
    if (Test-Path -LiteralPath $attemptPath) {
        throw "At-most-once guard: attempt already exists for $NeutralPacketId/$Role"
    }

    $profile = $Profiles[$Role]
    $evidencePriority = @(
        'CANDIDATE_CONTEXT.md',
        'CURRENT_OFFICIAL_RUBRIC.md',
        'NEUTRAL_PACKET_MANIFEST.json',
        'package/proposal.md',
        'package/proposal.en.md',
        'package/metrics.json',
        'package/assumptions.json',
        'package/sources.json',
        'package/compliance_matrix.json',
        'package/standard_matrix.json',
        'package/design_depth_matrix.json',
        'package/simulation.json',
        'package/self_check.json',
        'package/report/narrative.md'
    )
    $eligibleFiles = @(Get-ChildItem -LiteralPath $packetPath -Recurse -File | Where-Object {
        $_.Extension.ToLowerInvariant() -in @('.json', '.md', '.html', '.geojson', '.txt', '.yaml', '.yml', '.csv')
    })
    $orderedFiles = @()
    foreach ($relative in $evidencePriority) {
        $candidate = Join-Path $packetPath $relative.Replace('/', '\')
        if (Test-Path -LiteralPath $candidate -PathType Leaf) { $orderedFiles += Get-Item -LiteralPath $candidate }
    }
    $prioritySet = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
    foreach ($file in $orderedFiles) { [void]$prioritySet.Add($file.FullName) }
    $orderedFiles += @($eligibleFiles | Where-Object { -not $prioritySet.Contains($_.FullName) } | Sort-Object FullName)
    $evidenceBuilder = [System.Text.StringBuilder]::new()
    $maxEvidenceChars = 500000
    $maxFileChars = 80000
    $includedFiles = @()
    $truncatedFiles = @()
    foreach ($file in $orderedFiles) {
        if ($evidenceBuilder.Length -ge $maxEvidenceChars) { break }
        $relative = [System.IO.Path]::GetRelativePath($packetPath, $file.FullName).Replace('\', '/')
        $content = Get-Content -LiteralPath $file.FullName -Raw
        if ($content.Length -gt $maxFileChars) {
            $content = $content.Substring(0, $maxFileChars) + "`n[FILE_TRUNCATED_BY_NEUTRAL_ENVELOPE]"
            $truncatedFiles += $relative
        }
        $remaining = $maxEvidenceChars - $evidenceBuilder.Length
        $section = "`n`n--- FILE: $relative ---`n$content"
        if ($section.Length -gt $remaining) {
            $section = $section.Substring(0, $remaining) + "`n[ENVELOPE_LIMIT_REACHED]"
            $truncatedFiles += $relative
        }
        [void]$evidenceBuilder.Append($section)
        $includedFiles += $relative
    }
    $images = @(Get-ChildItem -LiteralPath (Join-Path $packetPath 'visual-surfaces') -File -ErrorAction SilentlyContinue | Where-Object {
        $_.Extension.ToLowerInvariant() -in @('.png', '.jpg', '.jpeg', '.webp')
    } | Sort-Object Name)
    if ($images.Count -eq 0) { throw "No attached visual surfaces found for $NeutralPacketId" }
    $workDir = Join-Path $RuntimeRoot "review-workdirs\$NeutralPacketId\$roleSlug"
    if (Test-Path -LiteralPath $workDir) { throw "Review workdir already exists: $workDir" }
    New-Item -ItemType Directory -Path $workDir -Force | Out-Null
    $attempt = [ordered]@{
        packet_id = $NeutralPacketId
        reviewer_role = $Role
        model = $profile.model
        resolved_model = $profile.resolved_model
        reasoning = $profile.reasoning
        status = 'STARTED'
        started_at = (Get-Date).ToUniversalTime().ToString('o')
        required_flags = @('--ephemeral', '--sandbox read-only', '--ignore-user-config', '--ignore-rules', '--output-schema')
        fresh_process = $true
        mcp_used = $false
        tui_used = $false
        subagents_allowed = $false
        evidence_delivery = 'STDIN_BOUNDED_TEXT_PLUS_EXPLICIT_IMAGES'
        evidence_character_count = $evidenceBuilder.Length
        evidence_files_included = $includedFiles.Count
        evidence_files_truncated = $truncatedFiles
        attached_image_count = $images.Count
        reviewer_workdir_empty = $true
    }
    Write-JsonFile -Value $attempt -Path $attemptPath

    $prompt = (Get-Content -LiteralPath $PromptPath -Raw).
        Replace('{{REVIEWER_ROLE}}', $Role).
        Replace('{{MODEL}}', $profile.model).
        Replace('{{PACKET_ID}}', $NeutralPacketId)
    $prompt += "`n`nBEGIN_NEUTRAL_PACKET_EVIDENCE`nPACKET_ID=$NeutralPacketId`n"
    $prompt += "INCLUDED_TEXT_FILES=$($includedFiles.Count)`nATTACHED_IMAGES=$($images.Count)`n"
    $prompt += $evidenceBuilder.ToString()
    $prompt += "`nEND_NEUTRAL_PACKET_EVIDENCE`n"
    $reasoningConfig = 'model_reasoning_effort="' + $profile.reasoning + '"'
    $arguments = @(
        'exec',
        '--ephemeral',
        '--sandbox', 'read-only',
        '--ignore-user-config',
        '--ignore-rules',
        '--output-schema', $SchemaPath,
        '--model', $profile.model,
        '-c', $reasoningConfig,
        '--image'
    )
    $arguments += @($images.FullName)
    $arguments += @(
        '--cd', $workDir,
        '--skip-git-repo-check',
        '--output-last-message', $rawPath,
        '-'
    )
    try {
        $prompt | & codex @arguments 2>&1 | Tee-Object -LiteralPath $logPath | Out-Host
        $exitCode = $LASTEXITCODE
        if ($exitCode -ne 0) { throw "codex exec exited $exitCode" }
        if (-not (Test-Path -LiteralPath $rawPath)) { throw 'codex exec did not write structured output' }
        $scorecard = Get-Content -LiteralPath $rawPath -Raw | ConvertFrom-Json
        if ($scorecard.reviewer_role -ne $Role) { throw 'reviewer_role envelope mismatch' }
        if ($scorecard.model -ne $profile.model) { throw 'model envelope mismatch' }
        if ($scorecard.packet_id -ne $NeutralPacketId) { throw 'packet_id envelope mismatch' }
        if ($scorecard.formal_local_evidence -ne $true) { throw 'formal_local_evidence must be true' }
        $truncatedOutputFields = @()
        foreach ($field in @('top_strengths', 'top_deficiencies')) {
            for ($index = 0; $index -lt $scorecard.$field.Count; $index++) {
                if ($scorecard.$field[$index].Length -gt 800) {
                    $scorecard.$field[$index] = $scorecard.$field[$index].Substring(0, 766) + ' [TRUNCATED_FOR_CONCISION]'
                    $truncatedOutputFields += "$field[$index]"
                }
            }
        }
        if ($scorecard.blocking_issue.Length -gt 800) {
            $scorecard.blocking_issue = $scorecard.blocking_issue.Substring(0, 766) + ' [TRUNCATED_FOR_CONCISION]'
            $truncatedOutputFields += 'blocking_issue'
        }
        $deterministicTotal = Get-DeterministicTotal -Scorecard $scorecard
        $reportedTotal = [int]$scorecard.weighted_total
        $scorecard.weighted_total = $deterministicTotal
        Write-JsonFile -Value $scorecard -Path $scorecardPath
        $attempt.status = 'COMPLETE'
        $attempt.exit_code = $exitCode
        $attempt.reported_weighted_total = $reportedTotal
        $attempt.deterministic_weighted_total = $deterministicTotal
        $attempt.weighted_total_corrected = ($reportedTotal -ne $deterministicTotal)
        $attempt.output_text_fields_truncated = $truncatedOutputFields
        $attempt.completed_at = (Get-Date).ToUniversalTime().ToString('o')
        Write-JsonFile -Value $attempt -Path $attemptPath
        Write-Host "SCORECARD COMPLETE packet=$NeutralPacketId role=$Role total=$deterministicTotal"
    } catch {
        $attempt.status = 'FAILED_NO_REROLL'
        $attempt.error = $_.Exception.Message
        $attempt.completed_at = (Get-Date).ToUniversalTime().ToString('o')
        Write-JsonFile -Value $attempt -Path $attemptPath
        throw
    }
}

function Invoke-NormalizeExistingScorecards {
    $normalized = 0
    foreach ($path in (Get-ChildItem -LiteralPath $OutputRoot -Filter '*.scorecard.json' -File)) {
        $scorecard = Get-Content -LiteralPath $path.FullName -Raw | ConvertFrom-Json
        $changed = $false
        foreach ($field in @('top_strengths', 'top_deficiencies')) {
            for ($index = 0; $index -lt $scorecard.$field.Count; $index++) {
                if ($scorecard.$field[$index].Length -gt 800) {
                    $scorecard.$field[$index] = $scorecard.$field[$index].Substring(0, 766) + ' [TRUNCATED_FOR_CONCISION]'
                    $changed = $true
                }
            }
        }
        if ($scorecard.blocking_issue.Length -gt 800) {
            $scorecard.blocking_issue = $scorecard.blocking_issue.Substring(0, 766) + ' [TRUNCATED_FOR_CONCISION]'
            $changed = $true
        }
        if ($changed) {
            Write-JsonFile -Value $scorecard -Path $path.FullName
            $normalized++
        }
    }
    Write-Host "NORMALIZATION COMPLETE scorecards_changed=$normalized raw_outputs_preserved=true"
}

function Invoke-ReviewBatch {
    param([Parameter(Mandatory)][string[]]$PacketIds)
    $queue = [System.Collections.Generic.Queue[object]]::new()
    foreach ($id in $PacketIds) {
        foreach ($role in @('PRIMARY', 'CHALLENGER')) {
            $roleSlug = $role.ToLowerInvariant()
            $existingScorecard = Join-Path $OutputRoot "$id.$roleSlug.scorecard.json"
            $existingAttempt = Join-Path $OutputRoot "$id.$roleSlug.attempt.json"
            if (Test-Path -LiteralPath $existingScorecard) {
                Write-Host "PRESERVED completed scorecard packet=$id role=$role"
                continue
            }
            if (Test-Path -LiteralPath $existingAttempt) {
                throw "Incomplete or failed attempt blocks rerun for $id/$role"
            }
            $queue.Enqueue([pscustomobject]@{ PacketId = $id; Role = $role })
        }
    }
    $active = @()
    while ($queue.Count -gt 0 -or $active.Count -gt 0) {
        while ($queue.Count -gt 0 -and $active.Count -lt $MaxParallel) {
            $item = $queue.Dequeue()
            $stdout = Join-Path $OutputRoot "$($item.PacketId).$($item.Role.ToLowerInvariant()).launcher.stdout.log"
            $stderr = Join-Path $OutputRoot "$($item.PacketId).$($item.Role.ToLowerInvariant()).launcher.stderr.log"
            $argList = @(
                '-NoProfile', '-File', $PSCommandPath,
                '-Action', 'Review',
                '-RuntimeRoot', $RuntimeRoot,
                '-SourcePacketsRoot', $SourcePacketsRoot,
                '-ProductRepo', $ProductRepo,
                '-PacketId', $item.PacketId,
                '-ReviewerRole', $item.Role
            )
            $process = Start-Process -FilePath 'pwsh.exe' -ArgumentList $argList -PassThru -WindowStyle Hidden -RedirectStandardOutput $stdout -RedirectStandardError $stderr
            $active += [pscustomobject]@{ Process = $process; Item = $item; Stdout = $stdout; Stderr = $stderr }
            Write-Host "LAUNCHED packet=$($item.PacketId) role=$($item.Role) pid=$($process.Id)"
        }
        if ($active.Count -gt 0) {
            Start-Sleep -Seconds 2
            $remaining = @()
            foreach ($entry in $active) {
                if ($entry.Process.HasExited) {
                    if ($entry.Process.ExitCode -ne 0) {
                        $errorText = if (Test-Path -LiteralPath $entry.Stderr) { Get-Content -LiteralPath $entry.Stderr -Raw } else { '' }
                        throw "Review process failed for $($entry.Item.PacketId)/$($entry.Item.Role): $errorText"
                    }
                    Write-Host "FINISHED packet=$($entry.Item.PacketId) role=$($entry.Item.Role)"
                } else {
                    $remaining += $entry
                }
            }
            $active = $remaining
        }
    }
}

function Get-Scorecard {
    param([Parameter(Mandatory)][string]$NeutralPacketId, [Parameter(Mandatory)][string]$Role)
    $path = Join-Path $OutputRoot "$NeutralPacketId.$($Role.ToLowerInvariant()).scorecard.json"
    if (-not (Test-Path -LiteralPath $path)) { throw "Missing scorecard: $path" }
    return Get-Content -LiteralPath $path -Raw | ConvertFrom-Json
}

function Get-PairwiseRankAccuracy {
    param([Parameter(Mandatory)][double[]]$Predicted, [Parameter(Mandatory)][double[]]$Official)
    $correct = 0
    $comparable = 0
    $inversions = @()
    for ($i = 0; $i -lt $Official.Count; $i++) {
        for ($j = $i + 1; $j -lt $Official.Count; $j++) {
            $officialDelta = $Official[$j] - $Official[$i]
            if ($officialDelta -eq 0) { continue }
            $comparable++
            $predictedDelta = $Predicted[$j] - $Predicted[$i]
            if ([math]::Sign($predictedDelta) -eq [math]::Sign($officialDelta)) {
                $correct++
            } elseif ([math]::Abs($officialDelta) -ge 10 -and $predictedDelta -ne 0) {
                $inversions += [ordered]@{ lower_index = $i; higher_index = $j; official_gap = $officialDelta; predicted_gap = $predictedDelta }
            }
        }
    }
    [ordered]@{
        accuracy = if ($comparable) { [math]::Round(100.0 * $correct / $comparable, 2) } else { 0 }
        correct = $correct
        comparable = $comparable
        major_inversions = $inversions
    }
}

function Get-Vector {
    param([Parameter(Mandatory)]$Scorecard)
    $vector = [ordered]@{}
    foreach ($dimension in $Dimensions) { $vector[$dimension] = [int]$Scorecard.$dimension }
    return $vector
}

function Get-CalibrationResult {
    $official = @()
    $primaryScores = @()
    $challengerScores = @()
    $anchorRows = @()
    foreach ($id in @('P01', 'P02', 'P03', 'P04', 'P05')) {
        $p = Get-Scorecard -NeutralPacketId $id -Role 'PRIMARY'
        $c = Get-Scorecard -NeutralPacketId $id -Role 'CHALLENGER'
        $o = [double]$PacketMap[$id].official_score
        $official += $o
        $primaryScores += [double]$p.weighted_total
        $challengerScores += [double]$c.weighted_total
        $anchorRows += [ordered]@{
            packet_id = $id
            source_id = $PacketMap[$id].source_id
            official_score = $o
            primary_score = [double]$p.weighted_total
            challenger_score = [double]$c.weighted_total
            consensus_score = [math]::Round(([double]$p.weighted_total + [double]$c.weighted_total) / 2, 2)
            reviewer_spread = [math]::Abs([double]$p.weighted_total - [double]$c.weighted_total)
        }
    }
    $consensusScores = for ($i = 0; $i -lt $official.Count; $i++) { ($primaryScores[$i] + $challengerScores[$i]) / 2 }
    $metricFor = {
        param([double[]]$values)
        $errors = for ($i = 0; $i -lt $official.Count; $i++) { $values[$i] - $official[$i] }
        $rank = Get-PairwiseRankAccuracy -Predicted $values -Official $official
        [ordered]@{
            bias = [math]::Round(($errors | Measure-Object -Average).Average, 2)
            mae = [math]::Round((($errors | ForEach-Object { [math]::Abs($_) }) | Measure-Object -Average).Average, 2)
            rank_accuracy = $rank.accuracy
            rank_correct = $rank.correct
            rank_comparable = $rank.comparable
            major_inversions = $rank.major_inversions
        }
    }
    $primaryMetrics = & $metricFor $primaryScores
    $challengerMetrics = & $metricFor $challengerScores
    $consensusMetrics = & $metricFor $consensusScores
    $majorInversions = @($primaryMetrics.major_inversions).Count + @($challengerMetrics.major_inversions).Count + @($consensusMetrics.major_inversions).Count
    $absoluteTrusted = ($consensusMetrics.mae -le 5 -and $majorInversions -eq 0)
    $relativeTrusted = ($consensusMetrics.rank_accuracy -ge 80 -and $majorInversions -eq 0)
    $calibrationMode = if ($absoluteTrusted -and $relativeTrusted) { 'ABSOLUTE_AND_RELATIVE' } elseif ($relativeTrusted) { 'RELATIVE_ONLY' } elseif ($absoluteTrusted) { 'ABSOLUTE_ONLY' } else { 'UNTRUSTED' }
    $anchorHoldouts = @()
    $p02HoldoutPath = Join-Path $OutputRoot 'P02.holdout.scorecard.json'
    if (Test-Path -LiteralPath $p02HoldoutPath) {
        $p02Holdout = Get-Content -LiteralPath $p02HoldoutPath -Raw | ConvertFrom-Json
        $anchorHoldouts += [ordered]@{
            packet_id = 'P02'
            trigger = 'PRIMARY_CHALLENGER_SPREAD_17_GT_10'
            weighted_total = [int]$p02Holdout.weighted_total
            vector = Get-Vector -Scorecard $p02Holdout
            calibration_metrics_unchanged = $true
        }
    }
    $calibration = [ordered]@{
        anchor_scorecards = 10
        anchor_holdout_scorecards = $anchorHoldouts.Count
        anchor_holdouts = $anchorHoldouts
        anchor_rows = $anchorRows
        primary = $primaryMetrics
        challenger = $challengerMetrics
        consensus = $consensusMetrics
        pairwise_ordering_accuracy = $consensusMetrics.rank_accuracy
        major_inversions = $majorInversions
        local_absolute_score_trusted = $absoluteTrusted
        local_relative_order_trusted = $relativeTrusted
        calibration_mode = $calibrationMode
        thresholds = [ordered]@{ consensus_mae_max = 5; pairwise_accuracy_min = 80; major_official_gap = 10; reviewer_total_spread_tolerance = 10 }
    }
    Write-JsonFile -Value $calibration -Path (Join-Path $RunOutputRoot 'CALIBRATION.json')
    return $calibration
}

function Invoke-Analyze {
    $calibration = Get-CalibrationResult
    $calibrationMode = $calibration.calibration_mode
    $absoluteTrusted = [bool]$calibration.local_absolute_score_trusted
    $relativeTrusted = [bool]$calibration.local_relative_order_trusted
    $candidateCards = [ordered]@{}
    foreach ($id in @('P06', 'P07', 'P08')) {
        $p = Get-Scorecard -NeutralPacketId $id -Role 'PRIMARY'
        $c = Get-Scorecard -NeutralPacketId $id -Role 'CHALLENGER'
        $candidateCards[$id] = [ordered]@{
            source_id = $PacketMap[$id].source_id
            primary = $p
            challenger = $c
            consensus_total = [math]::Round(([double]$p.weighted_total + [double]$c.weighted_total) / 2, 2)
            reviewer_spread = [math]::Abs([double]$p.weighted_total - [double]$c.weighted_total)
        }
    }
    $pDelta = [double]$candidateCards.P07.primary.weighted_total - [double]$candidateCards.P06.primary.weighted_total
    $cDelta = [double]$candidateCards.P07.challenger.weighted_total - [double]$candidateCards.P06.challenger.weighted_total
    $winner = if ($pDelta -gt 0 -and $cDelta -gt 0) { 'V042' } elseif ($pDelta -lt 0 -and $cDelta -lt 0) { 'V041A' } else { 'INCONCLUSIVE' }
    $winnerPacket = if ($winner -eq 'V041A') { 'P06' } else { 'P07' }
    $blockers = @()
    foreach ($dimension in $Dimensions) {
        $pBand = [int]$candidateCards[$winnerPacket].primary.$dimension
        $cBand = [int]$candidateCards[$winnerPacket].challenger.$dimension
        $classification = if ($pBand -eq 5 -and $cBand -eq 5) {
            'MAJORITY_5'
        } elseif ($pBand -eq 4 -and $cBand -eq 4) {
            'MAJORITY_4'
        } elseif ($pBand -ne $cBand) {
            'DISAGREEMENT'
        } else {
            'MAJOR_BLOCKER'
        }
        $blockers += [ordered]@{
            dimension = $dimension
            primary_band = $pBand
            challenger_band = $cBand
            classification = $classification
            mean_band = ($pBand + $cBand) / 2
            weight = [int]$Weights[$dimension]
        }
    }
    $targets = @($blockers | Where-Object classification -ne 'MAJORITY_5' | Sort-Object @{Expression='mean_band';Ascending=$true}, @{Expression='weight';Descending=$true}, dimension | Select-Object -First 2)
    $targetResults = @()
    foreach ($target in $targets) {
        $dimension = $target.dimension
        $baseP = [int]$candidateCards[$winnerPacket].primary.$dimension
        $baseC = [int]$candidateCards[$winnerPacket].challenger.$dimension
        $shadowP = [int]$candidateCards.P08.primary.$dimension
        $shadowC = [int]$candidateCards.P08.challenger.$dimension
        $status = if ($shadowP -eq 5 -and $shadowC -eq 5 -and $shadowP -ge $baseP -and $shadowC -ge $baseC) {
            'ALREADY_SOLVED_BY_SHADOW'
        } elseif ((($shadowP + $shadowC) -gt ($baseP + $baseC)) -or (($shadowP -eq $shadowC) -and ($shadowP -ge 4) -and ($baseP -ne $baseC))) {
            'PARTIALLY_SOLVED_BY_SHADOW'
        } else {
            'NOT_SOLVED_BY_SHADOW'
        }
        $targetResults += [ordered]@{
            dimension = $dimension
            baseline_bands = @($baseP, $baseC)
            shadow_bands = @($shadowP, $shadowC)
            status = $status
        }
    }
    $regressed = @()
    foreach ($dimension in $Dimensions) {
        $baseMean = ([int]$candidateCards[$winnerPacket].primary.$dimension + [int]$candidateCards[$winnerPacket].challenger.$dimension) / 2
        $shadowMean = ([int]$candidateCards.P08.primary.$dimension + [int]$candidateCards.P08.challenger.$dimension) / 2
        if ($shadowMean -lt $baseMean) { $regressed += $dimension }
    }
    $shadowRegressionRisk = if ($regressed.Count) { 'REGRESSION_RISK:' + ($regressed -join ',') } else { 'NO_MEASURED_REGRESSION' }
    $allSolved = ($targetResults.Count -eq 2 -and @($targetResults | Where-Object status -ne 'ALREADY_SOLVED_BY_SHADOW').Count -eq 0)
    $remaining = @($targetResults | Where-Object status -ne 'ALREADY_SOLVED_BY_SHADOW').Count
    $a2Mode = if ($allSolved) { 'PROMOTE_AND_CERTIFY_SHADOW' } elseif ($remaining -eq 1) { 'ONE_TIGHTLY_TARGETED_EXPERIMENTAL_PATCH' } else { 'BLOCKER_MATRIX_RECONCILIATION_REQUIRED' }
    $holdoutReasons = @()
    foreach ($id in @('P06', 'P07', 'P08')) {
        if ($candidateCards[$id].reviewer_spread -gt 10) { $holdoutReasons += "$id reviewer spread exceeds 10" }
    }
    if (($pDelta * $cDelta) -lt 0) { $holdoutReasons += 'candidate pairwise direction conflicts materially' }

    $measurement = [ordered]@{
        calibration_mode = $calibrationMode
        local_absolute_score_trusted = $absoluteTrusted
        local_relative_order_trusted = $relativeTrusted
        v041a = $candidateCards.P06
        v042 = $candidateCards.P07
        frozen_shadow_v043 = $candidateCards.P08
        reviewer_deltas_v042_minus_v041a = [ordered]@{ primary = $pDelta; challenger = $cDelta }
        formal_measured_winner = $winner
        blocker_matrix_basis = $PacketMap[$winnerPacket].source_id
        blocker_matrix = $blockers
        primary_targets = $targets
        shadow_target_status = $targetResults
        shadow_regression_risk = $shadowRegressionRisk
        holdout_required = ($holdoutReasons.Count -gt 0)
        holdout_reasons = $holdoutReasons
        a2_mode = $a2Mode
    }
    Write-JsonFile -Value $measurement -Path (Join-Path $RunOutputRoot 'MEASUREMENT_AND_BLOCKERS.json')
    $ledgerRows = @()
    foreach ($scorecardFile in (Get-ChildItem -LiteralPath $OutputRoot -Filter '*.scorecard.json' -File | Sort-Object Name)) {
        $scorecard = Get-Content -LiteralPath $scorecardFile.FullName -Raw | ConvertFrom-Json
        $rawFile = Join-Path $OutputRoot ($scorecardFile.Name.Replace('.scorecard.json', '.raw.json'))
        $attemptFile = Join-Path $OutputRoot ($scorecardFile.Name.Replace('.scorecard.json', '.attempt.json'))
        $ledgerRows += [ordered]@{
            scorecard_file = $scorecardFile.Name
            scorecard_sha256 = Get-Sha256 -Path $scorecardFile.FullName
            raw_file = if (Test-Path -LiteralPath $rawFile) { [System.IO.Path]::GetFileName($rawFile) } else { $null }
            raw_sha256 = if (Test-Path -LiteralPath $rawFile) { Get-Sha256 -Path $rawFile } else { $null }
            attempt_sha256 = if (Test-Path -LiteralPath $attemptFile) { Get-Sha256 -Path $attemptFile } else { $null }
            packet_id = $scorecard.packet_id
            reviewer_role = $scorecard.reviewer_role
            model = $scorecard.model
            weighted_total = [int]$scorecard.weighted_total
            formal_local_evidence = [bool]$scorecard.formal_local_evidence
        }
    }
    $ledger = [ordered]@{
        schema_version = '1.0.0'
        runtime_output_root = $OutputRoot
        scorecard_count = $ledgerRows.Count
        raw_outputs_preserved = $true
        rows = $ledgerRows
    }
    Write-JsonFile -Value $ledger -Path (Join-Path $RunOutputRoot 'SCORECARD_LEDGER.json')
    Write-Host "ANALYSIS COMPLETE calibration=$calibrationMode winner=$winner a2_mode=$a2Mode holdout_required=$($measurement.holdout_required)"
}

switch ($Action) {
    'Prepare' { Invoke-Prepare }
    'Preflight' { Invoke-Preflight }
    'Review' {
        if (-not $PacketId -or -not $ReviewerRole) { throw 'Review requires -PacketId and -ReviewerRole' }
        Invoke-OneReview -NeutralPacketId $PacketId -Role $ReviewerRole
    }
    'Anchors' { Invoke-ReviewBatch -PacketIds @('P01', 'P02', 'P03', 'P04', 'P05') }
    'Calibrate' {
        $calibration = Get-CalibrationResult
        Write-Host "CALIBRATION COMPLETE mode=$($calibration.calibration_mode) primary_mae=$($calibration.primary.mae) challenger_mae=$($calibration.challenger.mae) consensus_mae=$($calibration.consensus.mae) pairwise=$($calibration.pairwise_ordering_accuracy)"
    }
    'Candidates' { Invoke-ReviewBatch -PacketIds @('P06', 'P07') }
    'Shadow' { Invoke-ReviewBatch -PacketIds @('P08') }
    'Normalize' { Invoke-NormalizeExistingScorecards }
    'Analyze' { Invoke-Analyze }
    'All' {
        Invoke-Prepare
        Invoke-Preflight
        Invoke-ReviewBatch -PacketIds @('P01', 'P02', 'P03', 'P04', 'P05')
        Invoke-ReviewBatch -PacketIds @('P06', 'P07')
        Invoke-ReviewBatch -PacketIds @('P08')
        Invoke-Analyze
    }
}
