#!/usr/bin/python3
"""Uses GitHub API and Basic Auth to display the user ID."""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = (sys.argv[1], sys.argv[2])
    r = requests.get(url, auth=auth)
    try:
        print(r.json().get('id'))
    except ValueError:
        print("None")
