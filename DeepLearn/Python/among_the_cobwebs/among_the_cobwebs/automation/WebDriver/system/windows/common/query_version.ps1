param($binary_path)

[System.Diagnostics.FileVersionInfo]::GetVersionInfo($binary_path).FileVersion
