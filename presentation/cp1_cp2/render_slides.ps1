# Requires Microsoft PowerPoint on Windows. Opens the deck without a visible window.
$ErrorActionPreference = 'Stop'
$deckPath = Join-Path $PSScriptRoot 'CP1_CP2_Nhom4Nguoi.pptx'
$pdfPath = Join-Path $PSScriptRoot 'CP1_CP2_Nhom4Nguoi.pdf'
$renderPath = Join-Path $PSScriptRoot '.rendered'
New-Item -ItemType Directory -Path $renderPath -Force | Out-Null
$pptApp = $null
$pptDeck = $null
try {
    $pptApp = New-Object -ComObject PowerPoint.Application
    $pptApp.DisplayAlerts = 1
    $pptDeck = $pptApp.Presentations.Open($deckPath, -1, 0, 0)
    $pptDeck.SaveAs($pdfPath, 32)
    for ($slideIndex = 1; $slideIndex -le $pptDeck.Slides.Count; $slideIndex++) {
        $slidePath = Join-Path $renderPath "Slide$slideIndex.PNG"
        $pptDeck.Slides.Item($slideIndex).Export($slidePath, 'PNG', 1600, 900)
    }
    Write-Output "Exported PDF and $($pptDeck.Slides.Count) slide previews."
}
finally {
    if ($pptDeck) {
        $pptDeck.Close()
        [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($pptDeck)
    }
    if ($pptApp) {
        $pptApp.Quit()
        [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($pptApp)
    }
}
