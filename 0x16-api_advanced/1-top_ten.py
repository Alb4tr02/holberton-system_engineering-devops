#!/usr/bin/python3

"""  Python script that takes in a URL, sends a request to the URL and displays
     the body of the response. """

import requests


def top_ten(subreddit):
    headers = {'User-agent': 'Alb4tr02'}
    url = "https://www.reddit.com/r/"+subreddit+"/hot/.json"
    req = requests.get(url, headers=headers, params={'limit': 10})
    json = req.json()
    if ('error' in json.keys()):
        print(None)
        return
    for post in json['data']['children']:
        print(post['data']['title'])
