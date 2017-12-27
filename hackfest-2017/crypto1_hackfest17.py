def swap(s):
	s = list(s)
	for c in range(0,len(s),4):
		if c > ( len(s) - 4 ):
			break
		t  = s[c]
		t1 = s[c+1]
		s[c] = s[c+2]
		s[c+1] = s[c+3]
		s[c+2] = t
		s[c+3] = t1
	return "".join(s)

def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))


cipher = '4b4241494f4c5e594251471a67196e1e751958495a531a1d58135a1e73621b757559191319641e58664675731a411f646e1b78196e191d75751a19686775581a7519787a441a75191a1d4875137f0b590b0b7d'

#swap every 4 caracteres together 4b42 -> 424b
cipher = swap(cipher)

#xor key
key_xor = "2a"*(len(cipher)/2)

#xor cipher with key
binary_a = cipher.decode("hex")
binary_b = key_xor.decode("hex")


xored = xor_strings(binary_a, binary_b).encode("hex")
flag =  xored.encode()

#hex to string
flag = ''.join(chr(int(flag[i:i+2], 16)) for i in range(0, len(flag), 2))
print "flag is : ",flag