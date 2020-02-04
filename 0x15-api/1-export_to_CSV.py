#!/usr/bin/python3

"""  Python script that takes in a URL, sends a request to the URL and displays
     the body of the response. """

import requests
import sys
import csv

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
    my_file = open(query+".cvs", 'w')
    with my_file:
        writer = csv.writer(my_file, quoting=csv.QUOTE_ALL)
        for task in json:
            data = [[query, name, str(task['completed']), task['title']]]
            writer.writerows(data)
