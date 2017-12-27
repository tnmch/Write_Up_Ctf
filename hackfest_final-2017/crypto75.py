#DATATECH fouad
#!/usr/bin/env python2
from pwn import *
import binascii
import codecs
import hashlib
import sys
from Crypto.Cipher.AES import AESCipher
from Crypto.Hash import SHA256


r = remote("challenge.hackfest.tn", 3001)
p = r.recv()

brute = '0123456789abcdefghijklmnopqrstuvwxyz'

flag1 = ''
for i in xrange(1, 32):
    for c in brute:
        
        ## remote
        r.sendline(('a' * 8 + pad(c + flag1[:16]) + 'a' * i).encode('base64'))
        h = r.recv()
        m = ''.join(h.split()).decode('base64')[16:16 * 2].encode('base64')
        s = ''.join(h.split()).decode('base64')[16 * 3:16 * 5].encode('base64')
              
        if m == s:
            print 'I get it : ' + c
            flag1 = c + flag1
            break

print flag1
