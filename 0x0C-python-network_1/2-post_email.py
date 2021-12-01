#!/usr/bin/python3
"""takes a url and email from args to do a POST request"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]
    val = {'email': email}
    data = urllib.parse.urlencode(val)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
