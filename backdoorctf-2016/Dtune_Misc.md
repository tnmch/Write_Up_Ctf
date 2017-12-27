Hi

today i will explain how i solve a task in backdoorctf 

first we have a simple ![wav](Dtune.wav) file 

the sound look like someone typing his password in old phone, 
so its DTMF Tones 

convert the wav to phone number 
we get this 
```
84433033355524044477770777744225606663330337222344994462222779
```

as in the ctf the hint said that the flag is a capital alphabet

so this is not the final flag 

as this number used to write some text in the phone so  we need to use T9 

using a t9 emulator online or a simple code we can get the final flag

my code used to solve this is ![script](t9.java)

so the output is 
```
the flag is shbjm of EPCDHXHMCAQW
```

as in this ctf all the flag should be converted to sha256 before submit so the final text is 

```
the flag is sha256 of EPCDHXHMCAQW
```

and the flag is : 39551506faa3c2b1c1ee082adf79938da826910bf953665df882dd62b579759e

thanks 
