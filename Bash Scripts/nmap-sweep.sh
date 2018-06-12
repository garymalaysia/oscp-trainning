#!/bin/bash


if [ -z "$1" ] ; then
echo "[*] Network Sweeper with nmap"
echo "[*] Usage  : $0 <IP address> OR <IP address>.<Range>"
echo "[*] example: $0 10.11.1.1-254"

exit 0
fi

nmap -v -sn $1 -oG ping-sweep.txt
grep Up ping-sweep.txt | cut -d " " -f 2

