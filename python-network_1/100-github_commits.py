#!/usr/bin/python3
"""
Lists 10 commits (from most recent to oldest) of a specified GitHub repository
by a given user/owner using the GitHub API.
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    r = requests.get(url)
    try:
        commits = r.json()
        for commit in commits[:10]:
            sha = commit.get("sha")
            author_name = commit.get("commit").get("author").get("name")
            print("{}: {}".format(sha, author_name))
    except (TypeError, ValueError, KeyError):
        pass
