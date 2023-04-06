#!/usr/bin/python3
"""A python script that
- takes in a URL and an email
- sends a POST request to the passed URL with the email as a parameter
- displays the body of the response (decoded in utf-8)
"""
import sys
from urllib import request, parse, error

if __name__ == "__main__":
    url = sys.argv[1]
    data = {}
    data["email"] = sys.argv[2]
    data = parse.urlencode(data)
    data = data.encode('ascii')
    req = request.Request(url, data)
    try:
        with request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except error.URLError as e:
            if hasattr(e, 'reason'):
                print('We failed to reach a server.')
                print('Reason: ', e.reason)
            elif hasattr(e, 'code'):
                print('The server couldn\'t fulfill the request.')
                print('Error code: ', e.code)
