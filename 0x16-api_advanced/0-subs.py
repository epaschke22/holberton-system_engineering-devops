#!/usr/bin/python3
"""task 0"""
import requests


def number_of_subscribers(subreddit):
    """gets the number of subscribers from a subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent':'Python:sub.counter:v0.1 (by /u/willy)'}
    try:
        subinfo = requests.get(url, headers=headers, allow_redirects=False).json()
        return subinfo['data']['subscribers']
    except:
        return 0
