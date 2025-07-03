Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

while ($true) {
    # Ctrl+R を送信
    [System.Windows.Forms.SendKeys]::SendWait("^{r}")
    
    # 3 分待機
    Start-Sleep -Seconds 180
}
