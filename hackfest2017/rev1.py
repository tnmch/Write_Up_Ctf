#!/usr/bin/env python
#rev1 [HackFest Qualification 2017]

flag='2GYhdiSLoJTRvASGXjIHtatb9Kdr'
b='123456789NOPQRSTUWXYZACDEFGHIJKLMnopqrstuvwxzabcdefghijklm'
c=[]
for i in flag:
    for j in range(len(b)):
        if i==b[j]:
            c.append(j)
a=c[0]
for i in range(len(c)-1):
    a=a*58+c[i+1]

p=1
ar=[]
for i in range(28):
    p=p<<8
    if p>a:
        break

p=1461501637330902918203684832716283019655932542976
x=a
f = []
while(p!=1):
    p=p>>8
    m,x=divmod(x,p)
    f.append(m)


print "flag :",''.join(chr(i) for i in f)
    
