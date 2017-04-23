#!/usr/bin/env python

from pwn import *

a = open("crypto10.enc").read()
b = 0xee
c = xor(a,b)

file = open("flag.bmp","w")
file.write(c)
file.close()
