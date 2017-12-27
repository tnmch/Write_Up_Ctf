                            ###########get N,e,and key length########
#using openssl like always give error so i switched to ruby to get N and E 
#E is == 3 (CVE-2016-1494)

# N:ruby -r openssl -e 'p OpenSSL::PKey::RSA.new(File.open("public.pem")).n.to_i'
#output :99103278939331174405096046174826505890630650433457474512679503637107184969587849584143967014347754889469667043136895601008192434248630928076345525071962146097925698057299368797800220354529704116063015906135093873544219941584758892847007593809714204471472620455658479996846811490190888414921319427626842981521

# E : ruby -r openssl -e 'p OpenSSL::PKey::RSA.new(File.open("public.pem")).e.to_i'
#output : 3

# Length: ruby -r openssl -e 'p OpenSSL::PKey::RSA.new(File.open("public.pem")).n.num_bits'
#output : 1024
import os
import binascii
import hashlib
import rsa
from pwn import *
from gmpy2 import mpz, iroot, powmod, mul, t_mod

def to_bytes(n, endianess='big'):
    h = '%x' % n
    s = ('0'*(len(h) % 2) + h).decode('hex')
    return s

def from_bytes(b):
    return int(b.encode('hex'), 16)

def get_bit(n, b):
    return ((1 << b) & n) >> b

def set_bit(n, b, x):
    if x == 0: return ~(1 << b) & n
    if x == 1: return (1 << b) | n

def cube_root(n):
    return int(iroot(mpz(n), 3)[0])
    
message = "0YMrY4ZuMYU2YhoTZTSZROgC0HTQNI6M".encode("ASCII")
message_hash = hashlib.md5(message).digest()

ASN1_blob = rsa.pkcs1.HASH_ASN1['MD5']
suffix = b'\x00' + ASN1_blob + message_hash

sig_suffix = 1
for b in range(len(suffix)*8):
    if get_bit(sig_suffix ** 3, b) != get_bit(from_bytes(suffix), b):
        sig_suffix = set_bit(sig_suffix, b, 1)
        

while True:
    prefix = b'\x00\x01' + os.urandom(1024/8 - 2)
    sig_prefix = to_bytes(cube_root(from_bytes(prefix)))[:-len(suffix)] + b'\x00' * len(suffix)
    sig = sig_prefix[:-len(suffix)] + to_bytes(sig_suffix)
    if b'\x00' not in to_bytes(from_bytes(sig) ** 3)[:-len(suffix)]: break

exploit = binascii.b2a_hex(sig)
print "message : 0YMrY4ZuMYU2YhoTZTSZROgC0HTQNI6M"
print "exploit : " ,exploit


r = remote('rsasign1.2017.teamrois.cn', 3001)
print r.recvuntil('Show me your magic words:\n')
r.send(message)
print r.recvuntil('Show me again:\n')
r.send(exploit)
print r.recv(1024)

#RCTF{perfect_si9_i_can_nerver_Do_b3tter}
