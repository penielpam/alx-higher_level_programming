#!/bin/bash
# Perform a GET request to the provided URL and show the HTTP response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
