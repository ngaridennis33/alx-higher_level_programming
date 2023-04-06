#!/usr/bin/python3
"""A python script that
- takes in a URL
- sends a request to the URL
- displays the body of the response (decoded in utf-8)
"""
import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode("utf-8"))

    except error.HTTPError as e:
            print('Error code: ', e.code)
