#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv) < 2:
        variable = " "
    else:
        variable = sys.argv[1]

    val = {'q': variable}

    req = requests.post('http://0.0.0.0:5000/search_user', data=val)

    try:
        json_dict = r.json()
        if json_dict == {}:
            print("No result")
        else:
            print('[{}] {}'.format(json_dict['id'], json_dict['name']))

    except ValueError:
        print('Not a valid JSON')
