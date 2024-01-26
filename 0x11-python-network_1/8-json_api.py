#!/usr/bin/python3
"""
Python script that
- takes in a letter
-sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    parameters = {
        'q': ""
    }
    if len(argv) > 1:
        parameters["q"] = argv[1]
    req = requests.post('http://0.0.0.0:5000/search_user', data=parameters)
    try:
        json_data = req.json()
        id, name = json_data.get('id'), json_data.get('name')
        if len(json_data) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
    except Exception:
        print("Not a valid JSON")
