#!/usr/bin/python3
"""takes a url and email from args to do a POST request"""


if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    email = sys.argv[2]
    print(requests.post(url, data={'email': email}).text)
