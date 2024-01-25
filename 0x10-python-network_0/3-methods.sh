#!/bin/bash
# Show the supported HTTP methods by the server for the provided URL.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
