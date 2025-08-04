# 获取脚本所在目录，并拼接输出文件路径
$outputCsv = Join-Path -Path $PSScriptRoot -ChildPath "InstalledApps.csv"

# 扫描注册表列出已安装程序
Get-ChildItem -Path @(
    'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*'
    'HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*'
    'HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*'
) | ForEach-Object {
    $app = Get-ItemProperty $_.PSPath

    if ($app.DisplayName -and $app.InstallLocation) {
        [PSCustomObject]@{
            Name        = $app.DisplayName
            InstallPath = $app.InstallLocation
        }
    }
} | Export-Csv -Path $outputCsv -NoTypeInformation -Encoding UTF8
