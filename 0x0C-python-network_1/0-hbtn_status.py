#!/usr/bin/python3
"""fetches status from holberton intranet"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body Response:")
        print(" - type: {}".format(type(html)))
        print(" - content: {}".format(html))
        print(" - utf8 content: {}".format(html.decode('UTF-8')))
