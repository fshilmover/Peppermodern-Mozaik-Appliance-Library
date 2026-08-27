# Peppermodern-internal: refresh the repo copy from the live production library.
# Reads P: only (never writes there). Applies the PW -> PM rename, reports the
# diff, and stages changes in the working tree for review before any commit.
#
# Usage: powershell -File tools\sync-from-production.ps1

$ErrorActionPreference = 'Stop'
$src  = 'P:\Shared drives\Mozaik\Product Libraries\PW Fixtures and Appliances'
$repo = Split-Path $PSScriptRoot -Parent
$dest = Join-Path $repo 'Product Libraries\PM Fixtures and Appliances'

if (-not (Test-Path $src))  { throw "Production library not found: $src" }
if (-not (Test-Path $dest)) { throw "Repo library not found: $dest" }

# Stage into a temp copy first so the rename never touches production bytes.
$tmp = Join-Path $env:TEMP ("pm-lib-sync-" + (Get-Date -Format yyMMdd-HHmmss))
robocopy $src $tmp /E /XF *.LCK /NFL /NDL /NJH /NJS | Out-Null

$old = [byte[]][char[]]'SourceLib="PW Fixtures and Appliances"'
$new = [byte[]][char[]]'SourceLib="PM Fixtures and Appliances"'
Get-ChildItem "$tmp\Products" -Filter *.moz | ForEach-Object {
    $text = [IO.File]::ReadAllText($_.FullName)
    $patched = $text.Replace('SourceLib="PW Fixtures and Appliances"', 'SourceLib="PM Fixtures and Appliances"')
    if ($patched -ne $text) {
        [IO.File]::WriteAllText($_.FullName, $patched, (New-Object Text.UTF8Encoding($false)))
    }
}

# Diff report: temp (renamed production) vs repo copy.
$changes = @(); $adds = @(); $dels = @()
$tmpFiles  = Get-ChildItem $tmp -Recurse -File
$destFiles = Get-ChildItem $dest -Recurse -File
$tmpRel  = $tmpFiles  | ForEach-Object { $_.FullName.Substring($tmp.Length + 1) }
$destRel = $destFiles | ForEach-Object { $_.FullName.Substring($dest.Length + 1) }

foreach ($rel in $tmpRel) {
    $d = Join-Path $dest $rel
    if (-not (Test-Path $d)) { $adds += $rel; continue }
    $h1 = (Get-FileHash (Join-Path $tmp $rel) -Algorithm MD5).Hash
    $h2 = (Get-FileHash $d -Algorithm MD5).Hash
    if ($h1 -ne $h2) { $changes += $rel }
}
foreach ($rel in $destRel) {
    if (-not (Test-Path (Join-Path $tmp $rel))) { $dels += $rel }
}

Write-Host "New in production : $($adds.Count)";    $adds    | ForEach-Object { Write-Host "  + $_" }
Write-Host "Changed           : $($changes.Count)"; $changes | ForEach-Object { Write-Host "  ~ $_" }
Write-Host "Removed           : $($dels.Count)";    $dels    | ForEach-Object { Write-Host "  - $_" }

if ($adds.Count + $changes.Count + $dels.Count -eq 0) {
    Write-Host 'Repo copy already matches production. Nothing to do.'
} else {
    robocopy $tmp $dest /MIR /NFL /NDL /NJH /NJS | Out-Null
    Write-Host ''
    Write-Host 'Applied to the working tree. Review with git diff / git status, update'
    Write-Host 'MANIFEST.md + CHANGELOG.md, run python tools\validate.py, then commit.'
}
Remove-Item $tmp -Recurse -Force
