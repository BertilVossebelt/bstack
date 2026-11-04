# Links every bstack skill in this repo into an agent's skills folder, so edits in the repo apply at once.
param(
    [string]$SkillsDir = (Join-Path $HOME '.claude\skills')
)
$ErrorActionPreference = 'Stop'

New-Item -ItemType Directory -Force -Path $SkillsDir | Out-Null

foreach ($skill in Get-ChildItem -Path $PSScriptRoot -Directory | Where-Object { Test-Path (Join-Path $_.FullName 'SKILL.md') }) {
    $link = Join-Path $SkillsDir $skill.Name
    $existing = Get-Item -LiteralPath $link -Force -ErrorAction SilentlyContinue

    if ($existing -and -not $existing.LinkType) {
        Write-Warning "Skipped $($skill.Name): $link is a real folder. Move it away and run again."
        continue
    }

    # A junction needs no admin rights or developer mode on Windows.
    if ($existing) { $existing.Delete() }
    New-Item -ItemType Junction -Path $link -Target $skill.FullName | Out-Null
    Write-Host "Linked $($skill.Name) into $SkillsDir"
}
