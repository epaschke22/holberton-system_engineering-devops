#!/usr/bin/python3
"""returns employee todo data and exports to CSV"""
import requests
import json
from sys import argv

id = str(argv[1])
user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                    .format(id)).json()
name = user['username']
tasks = requests.get('https://jsonplaceholder.typicode.com/todos').json()
topdict = {}
tasklist = []
for i in tasks:
    if i['userId'] == int(argv[1]):
        taskdict = {}
        taskdict["task"] = i['title']
        taskdict["completed"] = i['completed']
        taskdict["username"] = name
        tasklist.append(taskdict)
topdict[id] = tasklist
with open("{}.json".format(id), 'w') as f:
    json.dump(topdict, f)
