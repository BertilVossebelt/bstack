@if "%~1"=="" (powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0install.ps1") else (powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0install.ps1" -SkillsDir "%~1")
