#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request


def intranet_status():
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        printinfo = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(printinfo)))
        print("\t- content: {}".format(printinfo))
        print("\t- utf8 content: {}".format(printinfo.decode('utf-8')))

if __name__ == '__main__':
    intranet_status()
