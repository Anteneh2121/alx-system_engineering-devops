#!/usr/bin/python3
"""
recursive
"""
import requests as r
from sys import argv


def count_words(subreddit, word_list, key=""):
    """
    recursive function that queries the Reddit API, 
	parses the title of all hot articles, and prints 
	a sorted count of given keywords (case-insensitive,
	delimited by spaces. Javascript should count as 
	javascript, but java should not).
    """
    headers = {"User-Agent": "Frocuts"}
    endpoint = "http://reddit.com/r/{}/hot.json?after={}"
    subs = r.get(endpoint.format(subreddit, key), headers=headers)
    if subs.status_code != 200:
        print(None)
        return 0
    subs = subs.json()
    if subs["kind"] == "Listing":
        # for data in subs["data"]["children"]:
            # print(data["data"]["title"])
        for word in word_list:
            print('{}: {}'.format(word, 0))
    else:
        print(None)
