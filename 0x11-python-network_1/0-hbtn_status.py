#!/usr/bin/python3
"""
This is a script that fetches https://alx-intranet.hbtn.io/status
Packages
- urllib
"""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
    response = r.read()
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
    print("\t- utf8 content: {}".format(response.decode('utf-8')))
