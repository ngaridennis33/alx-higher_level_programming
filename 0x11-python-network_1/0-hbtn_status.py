#!/usr/bin/python3
"""A python script that
- fetches  a url using urllib package
"""
from urllib import request, error

if __name__ == "__main__":
    try:
        with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
            html = response.read()
            print(f"Body response:\n\t- type: {type(html)}\n\t- content: {html}\n\t- utf8 content: {html.decode()}")
    except error.URLError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
