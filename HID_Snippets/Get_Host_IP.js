
type('(Get-NetIPAddress -InterfaceAlias "Wi-Fi" -AddressFamily IPv4).IPAddress >> "$env:PUBLIC\\ip.txt"')
press('ENTER')
