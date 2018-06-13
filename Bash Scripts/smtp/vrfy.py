#!/usr/bin/python
import subprocess 
import socket
import sys
from subprocess import Popen, PIPE

if len(sys.argv) != 3:
	print "Usage: vrfy.py <username> <IP Address> OR vrfy.py <username> <IP Addresses>"
	print "example : vrfy.py root 10.11.1.1"
	print "example : vrfy.py root 10.11.1.1-254"
	sys.exit(0)

ip = str(sys.argv[2])
subprocess.call(["nmap" , "-p25", ip, "-oG", "smtp.txt"], shell=False)
grep = subprocess.Popen(["grep", "-w" , "open", "smtp.txt"], stdout=subprocess.PIPE)
output = subprocess.Popen(["cut", '-d', ' ', "-f2"], stdin=grep.stdout, stdout=subprocess.PIPE)
grep.stdout.close()

#output= str(output)
for i in output.stdout:
	print i 
	# Create a Socket
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Connect to the Server 
	connect=s.connect((i,25))
	# Receive the banner
	banner=s.recv(1024)
	print banner
	# VRFY a user
	s.send('VRFY ' + sys.argv[1] + '\r\n')
	result=s.recv(1024)
	print result
	# Close the socket
	s.close()
