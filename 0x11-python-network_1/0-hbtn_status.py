#!/usr/bin/python3
# Script that fetches a URL using urlib
from urllib import request
if __name__ == "__main__":
        with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
            html = response.read()
            print(f"Body response:\n\t- type: {type(html)}\n\t- content: {html}\n\t- utf8 content: {html.decode()}")
