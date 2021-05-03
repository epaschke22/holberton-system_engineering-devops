#!/usr/bin/python3
"""returns employee todo data and exports to CSV"""
import json
import requests


if __name__ == "__main__":
    Users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    Tasks = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    topdict = {}
    for user in Users:
        tasklist = []
        for task in Tasks:
            if task['userId'] == user['id']:
                taskdict = {}
                taskdict["task"] = task['title']
                taskdict["completed"] = task['completed']
                taskdict["username"] = user['username']
                tasklist.append(taskdict)
        topdict[user['id']] = tasklist
    with open("todo_all_employees.json", 'w') as f:
        json.dump(topdict, f)
