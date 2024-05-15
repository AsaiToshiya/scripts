param(
    [string]$targetFolder,
    [string]$targetFile
)

$targetHash = (Get-FileHash -Path $targetFile).Hash

Get-ChildItem -Path $targetFolder -File |
    ? { (Get-FileHash -Path $_.FullName).Hash -eq $targetHash } |
    % { Write-Output "$($_.Name)" }
