#!/usr/bin/python3
"""Sends a request to a URL using requests and prints X-Request-Id header."""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
