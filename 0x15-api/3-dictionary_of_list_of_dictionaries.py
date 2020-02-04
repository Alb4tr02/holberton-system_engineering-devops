#!/usr/bin/python3

"""  Python script that takes in a URL, sends a request to the URL and displays
     the body of the response. """

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    req = requests.get(url)
    jjson = req.json()
    my_file = open("todo_all_employees.json", 'w')
    all_data = {}
    for person in jjson:
        query = person['id']
        name = person['username']
        url = "https://jsonplaceholder.typicode.com/todos/"
        req = requests.get(url, params={"userId": query})
        jjson = req.json()
        l = []
        for task in jjson:
            l.append({"username": name, "task": task['title'],
                      "completed": task['completed']})
        all_data[query] = l
    with my_file:
        json.dump(all_data, my_file)
