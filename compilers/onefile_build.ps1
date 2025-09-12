# ───────────────────────────────────────────────
# 🚀 SeasonTrack Build Script
# ───────────────────────────────────────────────

# Clear the screen for a clean look
Clear-Host

# Banner
Write-Host "╔══════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║          🔥 Building SeasonTrack 🔥              ║" -ForegroundColor Cyan
Write-Host "╚══════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Define pyinstaller command
$pyinstallerCmd = @(
    "pyinstaller --clean -n SeasonTrack",
    "-F --windowed",
    "--icon=assets/AppIcon.ico",
    "--add-data `"assets;assets`"",
    "--add-data `"helpers;helpers`"",
    "season_track.py"
) -join " "

# Run pyinstaller
Write-Host "▶ Running PyInstaller..." -ForegroundColor Yellow
Invoke-Expression $pyinstallerCmd

# Check exit code
if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✅ Build completed successfully!" -ForegroundColor Green
} else {
    Write-Host "`n❌ Build failed with exit code $LASTEXITCODE" -ForegroundColor Red
    exit $LASTEXITCODE
}

# Clean up
Write-Host "`n🧹 Cleaning up build artifacts..." -ForegroundColor Yellow

if (Test-Path "build") {
    Remove-Item -Recurse -Force "build"
    Write-Host "✔ Removed build folder" -ForegroundColor DarkGray
}

$specFile = "SeasonTrack.spec"
if (Test-Path $specFile) {
    Remove-Item -Force $specFile
    Write-Host "✔ Removed $specFile" -ForegroundColor DarkGray
}

Write-Host "`n🎉 All done! Your executable is in the 'dist' folder." -ForegroundColor Cyan
