#!/usr/bin/python3

"""  Python script that takes in a URL, sends a request to the URL and displays
     the body of the response. """

import requests


def number_of_subscribers(subreddit):
    headers = {'User-agent': 'Alb4tr02'}
    url = "https://www.reddit.com/r/"+subreddit+"/about.json"
    req = requests.get(url, headers=headers)
    json = req.json()
    if ('error' in json.keys()):
        return 0
    name = json['data']['subscribers']
    return name
