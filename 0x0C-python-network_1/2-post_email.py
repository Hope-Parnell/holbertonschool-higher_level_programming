#!/usr/bin/python3
import urllib.parse
import urllib.request
import sys

url = sys.argv[1]
email = {'email': sys.argv[2]}
data = urllib.parse.urlencode(email)
data = data.encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
   print(response.read().decode('UTF-8'))
