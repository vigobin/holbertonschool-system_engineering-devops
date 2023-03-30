#!/usr/bin/python3
"""Gather data from an API """

import json
import requests
from sys import argv


def gather(emp_id):
    """Returns TODO list progress"""
    emp_id = {'id': argv[1]}
    task = {'userID': argv[1]}
    url1 = 'https://jsonplaceholder.typicode.com/users'
    url2 = 'https://jsonplaceholder.typicode.com/todos'

    user = requests.get(url1, params=emp_id)
    todo = requests.get(url2, params=task)

    print(user.content)
    print(todo.content)


if __name__ == '__main__':
    gather(emp_id=argv[1])
