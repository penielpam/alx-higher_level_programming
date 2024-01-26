#!/usr/bin/python3
"""Fetches content from a specified URL (https://alx-intranet.hbtn.io/status)."""
import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    request = urllib.request.Request(url)
    
    with urllib.request.urlopen(request) as response:
        fetched_content = response.read()
        print("Fetched content:")
        print("\t- type: {}".format(type(fetched_content)))
        print("\t- content: {}".format(fetched_content))
        print("\t- utf8 content: {}".format(fetched_content.decode("utf-8")))
