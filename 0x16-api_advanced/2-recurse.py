#!/usr/bin/python3

"""  Python script that takes in a URL, sends a request to the URL and displays
     the body of the response. """

import requests


def recurse(subreddit, hot_list=[], nexT=""):
    headers = {'User-agent': 'Alb4tr02'}
    url = "https://www.reddit.com/r/"+subreddit+"/hot/.json"+nexT
    req = requests.get(url, headers=headers)
    json = req.json()
    if ('error' in json.keys()):
        return None
    for post in json['data']['children']:
        hot_list.append(post['data']['title'])
    if (json['data']['after'] is not None):
        return recurse(subreddit, hot_list, "?after="+json['data']['after'])
    else:
        return hot_list
