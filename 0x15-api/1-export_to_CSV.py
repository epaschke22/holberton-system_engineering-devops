#!/usr/bin/python3
"""returns employee todo data and exports to CSV"""
import requests
import csv
from sys import argv


user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                    .format(argv[1])).json()
name = user['username']
tasks = requests.get('https://jsonplaceholder.typicode.com/todos').json()
with open('{}.csv'.format(argv[1]), mode='w') as employee_file:
    for i in tasks:
        if i['userId'] == int(argv[1]):
            writer = csv.writer(employee_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
            writer.writerow([str(argv[1]), name, i['completed'], i['title']])
