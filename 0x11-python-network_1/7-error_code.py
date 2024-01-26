#!/usr/bin/python3
"""
This script sends a request to a specified URL and prints the response body.
Usage: ./handle_http_errors.py <URL>
  - Manages HTTP errors.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
