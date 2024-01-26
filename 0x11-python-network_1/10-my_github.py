#!/usr/bin/python3
"""
Utilizes the GitHub API to retrieve a GitHub ID with provided credentials.
Usage: ./fetch_github_id.py <GitHub username> <GitHub password>
  - Employs Basic Authentication for accessing the ID.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth_credentials = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth_credentials)
    print(response.json().get("id"))
