#!/usr/bin/python3
""" takes in a letter and sends a POST request"""
import requests
import sys


if __name__ == "__main__":

    var = sys.argv[1] if len(sys.argv) > 1 else ""

    req = requests.post("http://0.0.0.0:5000/search_user", data={'q': var})
    try:
        j = req.json()
        print("[{}] {}".format(j.get('id'), j.get('name')) if len(j) > 0
              else "No result")
    except ValueError:
        print("Not a valid JSON")
