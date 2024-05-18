# 使い方: .\FindFileByHashInFolder.ps1 <検索されるフォルダのパス> <検索するファイルのパス>

Get-ChildItem -Path $Args[0] -File | ? { (Get-FileHash -Path $_.FullName).Hash -eq (Get-FileHash -Path $Args[1]).Hash } | % { Write-Output "$($_.Name)" }
