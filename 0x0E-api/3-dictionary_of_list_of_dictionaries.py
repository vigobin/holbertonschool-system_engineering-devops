#!/usr/bin/python3
"""Export to CSV"""
import csv
import json
import requests
from sys import argv


def gather(emp_id):
    """Export data in the CSV format."""
    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)
    todo = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(emp_id)

    r_user = (requests.get(user)).json()
    r_todo = (requests.get(todo)).json()

    name = r_user.get('username')
    task_list = []

    for j in r_todo:
        title = j.get('title')
        status = j.get('completed')

        new_dict = {'task': title,
                    'completed': status,
                    'username': name}

        task_list.append(new_dict)

    data = {emp_id: task_list}
    with open(emp_id + '.json', 'w', newline='') as write_file:
        json.dump(data, write_file)
