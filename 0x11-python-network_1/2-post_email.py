#!/usr/bin/python3
"""
This script sends a POST request to a specified URL with a provided email.
Usage: ./post_email_request.py <URL> <email>
  - Displays the body of the response.
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email_value = {"email": sys.argv[2]}
    encoded_data = urllib.parse.urlencode(email_value).encode("ascii")

    post_request = urllib.request.Request(url, encoded_data)
    with urllib.request.urlopen(post_request) as response:
        print(response.read().decode("utf-8"))
