#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers """

from sys import argv
import requests

def number_of_subscribers(subreddit):
    r_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'user-agent': 'Mozilla/5.0'}

    r = requests.get(r_url, headers=header)

    if r.status_code == 200:
        return len(r.json()['data'])
    else
