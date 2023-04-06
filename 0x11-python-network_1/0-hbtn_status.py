#!/usr/bin/python3
"""A python script that
- fetches https://alx-intranet.hbtn.io/status
- use the urllib package
"""

from urllib import request, error

if __name__ == "__main__":
    try:
        with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
            html = response.read()
            print("Body response:")
            print(f"\t- type: {type(html)}\n\t- content: {html}\n\t- utf8 content: {html.decode()}")
    except error.URLError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
