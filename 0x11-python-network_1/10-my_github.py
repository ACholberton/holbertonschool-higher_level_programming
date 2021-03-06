#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""

if __name__ == '__main__':
    import requests
    import sys

    arguments = (sys.argv[1], sys.argv[2])
    req = requests.get('https://api.github.com/user', auth=arguments)
    json_dict = req.json()
    print(json_dict.get('id'))
