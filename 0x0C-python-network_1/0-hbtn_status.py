#!/usr/bin/python3
"""fetches status from holberton intranet"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print("Body Response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(str(html)))
        print("\t- utf8 content: {}".format(html.decode('UTF-8')))
