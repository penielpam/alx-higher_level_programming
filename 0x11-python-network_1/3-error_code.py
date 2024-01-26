#!/usr/bin/python3
"""
This script sends a request to a specified URL and prints the response body.
Usage: ./handle_http_errors.py <URL>
  - Manages HTTP errors.
"""

import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as http_error:
        print("Error code: {}".format(http_error.code))
