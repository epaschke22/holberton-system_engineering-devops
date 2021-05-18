#!/usr/bin/python3
"""task 1"""
import requests


def top_ten(subreddit):
    """returns top 10 hot posts of a subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'Python:sub.counter:v0.1 (by /u/willy)'}
    param = {'limit': 10}
    try:
        subtop10 = requests.get(url, headers=header, params=param,
                                allow_redirects=False).json()
        for post in subtop10['data']['children']:
            print(post['data']['title'])
    except:
        print(None)
