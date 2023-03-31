#!/usr/bin/python3
"""Gather data from an API """
import json
import requests
from sys import argv


def gather(emp_id):
    """Returns TODO list progress"""
    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)
    todo = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(emp_id)

    r_user = (requests.get(user)).json()
    r_todo = (requests.get(todo)).json()

    name = r_user.get('name')
    tasks = len(r_todo)
    completed = sum(i.get('completed') for i in r_todo if i)

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, tasks))
    for j in r_todo:
        title = j.get('title')
        if j.get('completed'):
            print('\t {}'.format(title))


if __name__ == '__main__':
    gather(argv[1])
