#!/usr/bin/python3
"""
Contains the recurse method
"""
from collections import defaultdict
import random
import requests
user_agent = "User Agent{:d}".format(random.randrange(1000, 9999))
header = {'User-Agent': user_agent}


def count_words(subreddit, word_list, base=0, keywords={}, after=""):
    """
    Creates a list of all the titles of the hot list
    input:
        subreddit: the name of a reddit subreddit
        hot_list: list to be filled with the sub reddit name
    return: host_list or None otherwise
    """
    if keywords == {}:
        word_list = [word.lower() for word in word_list]
        word_list = list(set(word_list))
        keywords = defaultdict(int)
    url = "https://www.reddit.com/r/{}/.json".format(subreddit)
    r = requests.get(url, headers=header, params={"after": after},
                     allow_redirects=False)
    if r.status_code == 200:
        r_dict = r.json()
        for reddit_post in r_dict["data"]["children"]:
            title_words = reddit_post['data']['title'].lower().split()
            for title_word in title_words:
                for word in word_list:
                    if word == title_word:
                        keywords[word] += 1
        after = r_dict['data']['after']
        if after is None:
            return keywords
        else:
            count_words(subreddit, word_list,
                                   base + 1, keywords, after)
    else:
        return None
    # only to be executed for before the recursive
    if base is 0:
        keywords_list = list(keywords.items())
        keywords_list = sorted(keywords_list, key=lambda x: x[1], reverse=True)
        for pair in keywords_list:
            if pair[1] is not 0:
                print("{}: {}".format(pair[0], pair[1]))
    return keywords
