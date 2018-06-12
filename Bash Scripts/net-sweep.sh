#!/bin/bash

if [ -z "$1" ] ; then
echo "[*] Network Sweeper with nmap"
echo "[*] Usage  : $0 <IP address> OR <IP address>.<Range>"
echo "[*] example: $0 10.11.1.1-254"

exit 0
fi

if [[  -f ./http_os.txt  || -f ./report.txt ]]; then
        rm http_os.txt report.txt

fi

touch report.txt
echo "Live IP -----------------------------------------------> " >> report.txt
nmap -v -sn $1 -oG ping-sweep.txt
for host in $(grep Up ping-sweep.txt | cut -d " " -f 2); do
         echo -n "$host " >> http_os.txt
         echo "$host" >> report.txt
done

echo "" >> report.txt

if [  -f ./os.txt ]; then
        rm ./os.txt

fi
echo "Live IP w/ HTTP ---------------------------------------> " >> report.txt
nmap -p 80 $(cat http_os.txt) -oG http_os.txt
for server in $(grep open http_os.txt | cut -d " " -f 2); do
        echo -n "$server " >> os.txt
        echo $server >> report.txt
done

nmap  -p 80 -sV -sT $(cat os.txt) -oG os.txt
grep "Ports:" os.txt

