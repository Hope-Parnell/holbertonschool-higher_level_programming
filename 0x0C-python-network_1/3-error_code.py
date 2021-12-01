#!/usr/bin/python3
"""catches errors from requests"""
import urllib.request
from urllib.error import HTTPError
import sys


if __name__ == "__main__":

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
