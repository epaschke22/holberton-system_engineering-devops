#!/usr/bin/python3
"""returns employee todo data"""
import requests
from sys import argv

if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1])).json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    name = user['name']
    tkslistdone = []
    tkstotal = 0
    tksdone = 0
    for i in tasks:
        if i['userId'] == int(argv[1]):
            tkstotal += 1
            if i['completed']:
                tksdone += 1
                tkslistdone.append(i['title'])
    print("Employee {} is done with tasks({}/{}):"
          .format(name, tksdone, tkstotal))
    for i in tkslistdone:
        print("\t {}".format(i))
