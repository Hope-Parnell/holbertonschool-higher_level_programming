#!/usr/bin/python3
import urllib.parse
import urllib.request
from sys import argv

url = argv[1]
email = {"email": argv[2]}
data = urllib.parse.urlencode(email)
data = data.encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
   print(response.read().decode('UTF-8'))
