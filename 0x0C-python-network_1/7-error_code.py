#!/usr/bin/python3
"""catches errors from requests"""


if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    req = requests.get(url)

    print("Error code: {}".format(req.status_code) if req.status_code >= 400
          else req.text)
