#!/usr/bin/python3
"""
Displays the 10 most recent commits on a specified GitHub repository.
Usage: ./github_commits.py <repository name> <repository owner>
"""

import sys
import requests

if __name__ == "__main__":
    repository_name = sys.argv[1]
    repository_owner = sys.argv[2]
    
    url = "https://api.github.com/repos/{}/{}/commits".format(repository_owner, repository_name)

    response = requests.get(url)
    commits = response.json()

    try:
        for i in range(10):
            commit_sha = commits[i].get("sha")
            commit_author = commits[i].get("commit").get("author").get("name")
            print("{}: {}".format(commit_sha, commit_author))
    except IndexError:
        pass
