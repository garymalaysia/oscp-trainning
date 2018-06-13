#!/bin/bash

if [ -z "$1" ] ; then
echo "[*] Network Sweeper with nmap"
echo "[*] Usage  : $0 <IP address> OR <IP address>.<Range>"
echo "[*] example: $0 10.11.1.1-254"

exit 0
fi

if [[  -f ./smb.txt  || -f ./report.txt || -f ./windows._ip.txt ]]; then
        rm smb.txt report.txt windows_ip.txt

fi

touch report.txt
echo "Live IP -----------------------------------------------> " >> report.txt
nmap  -v -p 139,445 --script smb-os-discovery $1 -oG smb.txt 
for host in $(grep "445/open/" smb.txt  | cut -d " " -f 2); do
         echo -n "$host " >> windows_ip.txt
         echo "$host" >> report.txt
done

echo "NMAP SMB-vuln scan Result ------------------------------> "

nmap  -p 139,445 --script "smb-vuln*" $(cat windows_ip.txt) >> report.txt


: '
echo "" >> report.txt

if [  -f ./os.txt ]; then
        rm ./os.txt

fi
echo "Live IP w/ Winsdows ---------------------------------------> " >> report.txt
nmap -p 80 $(cat http_os.txt) -oG http_os.txt
for server in $(grep open http_os.txt | cut -d " " -f 2); do
        echo -n "$server " >> os.txt
        echo $server >> report.txt
done

nmap  -p 80 -sV -sT $(cat os.txt) -oG os.txt
grep "Ports:" os.txt
'
