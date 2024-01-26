#!/usr/bin/python3
"""
Fetches and displays the X-Request-Id header variable from a specified URL.
Usage: ./custom_header_fetcher.py <URL>
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        x_request_id = dict(response.headers).get("X-Request-Id")
        print(x_request_id)
