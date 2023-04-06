#!/usr/bin/python3
"""A python script that
- takes in a URL
- sends a request to the URL
- displays the value of the X-Request-Id variable found in the header of the response
"""
import sys
from urllib import request, error

if __name__ == "__main__":
    if(len(sys.argv) > 1):
        url = sys.argv[1]
        try:
            with request.urlopen(url) as response:
                print(response.headers['X-Request-Id'])

        except error.URLError as e:
            if hasattr(e, 'reason'):
                print('We failed to reach a server.')
                print('Reason: ', e.reason)
            elif hasattr(e, 'code'):
                print('The server couldn\'t fulfill the request.')
                print('Error code: ', e.code)
    else:
        print("No URL was passed")
