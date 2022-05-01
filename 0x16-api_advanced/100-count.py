#!/usr/bin/python3
"""
a recursive function that queries the Reddit API, parses the title
of all hot articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces. Javascript
should count as javascript, but java should not)
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """If not a valid subreddit, return None"""
    url = "https://www.reddit.com/r/{:s}/hot.json".format(subreddit)
    headers = {'User-agent': 'api_advanced'}
    params = {'after': after}
    res = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False)

    if res.status_code != 200:
        return None
    res = res.json()
    after = res['data']['after']
    top_list = res['data']['children']
    for top in top_list:
        hot_list.append(top['data']['title'])

    if after is None:
        if len(hot_list) == 0:
            return None
        return hot_list
    return recurse(subreddit, hot_list, after)


def count_words(subreddit, word_list):
    """If no posts match or the subreddit is invalid, print nothing"""
    rec = recurse(subreddit)
    count = {word: 0 for word in word_list}
    for i in rec:
        for word in word_list:
            if word in i.lower():
                count[word] += 1

    for num in list(count):
        if count[num] == 0:
            del count[num]

    count = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
    for k, v in count.items():
        print(f'{k}: {v}')
