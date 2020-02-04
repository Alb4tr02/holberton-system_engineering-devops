#!/usr/bin/python3

"""  Python script that takes in a URL, sends a request to the URL and displays
     the body of the response. """

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    query = sys.argv[1]
    url = url+query
    req = requests.get(url)
    json = req.json()
    name = json['name']
    url = "https://jsonplaceholder.typicode.com/todos/"
    req = requests.get(url, params={"userId": query})
    json = req.json()
    total = len(json)
    comp = ""
    n_comp = 0
    for task in json:
        if (task['completed']):
            comp = comp + "\t " + task['title'] + "\n"
            n_comp = n_comp + 1
    print("Employee {} is done with tasks({}/{}):".format(name, n_comp, total))
    print(comp, end="")
