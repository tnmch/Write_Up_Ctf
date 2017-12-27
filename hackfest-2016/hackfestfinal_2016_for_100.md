
hi
this is my write up about forensic 100 task in the final hackfest ctf in tunisia 

so we have a for100.pcap [file](https://volafile.io/get/N24ePzEIw65nm/for100.pcap)

first we open it with wireshark and check what's going on there 

there is many request and nothing good for us 

but before the ctf end we noticed that there is a not valid domain there "harmlessdomain.net"


so we decided to extract it all 
using a simple truck in wireshark 

```
dns.flags == 0x0100 and dns.qry.name matches "[0-9]{1}.[0-9a-f]{4}.harmlessdomain.net"
```

and then File" -> "Export Specified Packets" we get another pcap file with just what we need

then we extract the hex caracteres 
```
strings for100_filtred.pcap | grep -P "^[0-9a-f]{4}$" | tr -d "\n" > res
```

we get this : 
```
8b1f00087dac57170300d0ed0a3131028414d4e1629e204fc6c91cbc64279d35491082de7a7a2d9591b416adfe1199af9a627a61b6397ba2aabd8cd9127dbc39c5d23f603173e30668c64483ef11758c7bde83316edddbd235dc61b75330df3eab736f5feb5894ff9ad6ee4aa4b74d355d259d5abb4f8f5f00020000000000000000000000007aac9d009a45009a00280000
```
so we can see that its a broken Signature header of gzip file 1F 8B 08 00

and we just swap them but we still get a broken file 
and finaly we just swap two by two to get : 
```
1f8b0800ac7d17570003edd0310a02311484e1d49e624f20c9c6bc1c2764359d1049de827a7a952db491ad1611feaf99629a617a39b6a27bbdaad98c7d1239bcd2c5603f733106e3c668834411ef8c75de7b3183dd6ed2dbdc35b76130533edf73ab5f6f58ebff94d69a4aeeb7a4354d255d5a9d4fbb5f8f0200000000000000000000000000ac7a009d459a9a0028000000
```
and just a simple python script

```
#!/usr/bin/python
file_hex = open('res','r').read()
open('flag.tar','w').write(file_hex.decode('hex')) 
```

then  
```
tar -xvf flag.tar
```


and pwn :D  we get a secret.txt file which we have there our flag :D 

```
flag = " too_easy_to_be_proud"
```

thanks :) 
