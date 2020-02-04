#!/usr/bin/python3

"""  Python script that takes in a URL, sends a request to the URL and displays
     the body of the response. """

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    query = sys.argv[1]
    url = url+query
    req = requests.get(url)
    jjson = req.json()
    name = jjson['username']
    url = "https://jsonplaceholder.typicode.com/todos/"
    req = requests.get(url, params={"userId": query})
    jjson = req.json()
    my_file = open(query+".json", 'w')
    l = []
    for task in jjson:
        l.append({"task": task['title'], "completed": task['completed'],
                  "username": name})
    data = {query: l}
    with my_file:
            json.dump(data, my_file)
