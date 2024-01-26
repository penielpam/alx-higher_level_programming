#!/usr/bin/python3
"""
This script sends a POST request to a specified URL with a provided email.
Usage: ./post_email_request.py <URL> <email>
  - Displays the body of the response.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email_value = {"email": sys.argv[2]}

    response = requests.post(url, data=email_value)
    print(response.text)
