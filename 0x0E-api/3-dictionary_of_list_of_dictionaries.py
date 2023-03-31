#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
import csv
import json
import requests
from sys import argv


def json_dict():
    """Export data in the JSON format for all"""
    user = 'https://jsonplaceholder.typicode.com/users'
    todo = 'https://jsonplaceholder.typicode.com/todos'

    r_user = (requests.get(user)).json()
    r_todo = (requests.get(todo)).json()

    for user in r_user:
        name = r_user.get('username')
        ee_id = r_user.get('id')
        task_list = []

    for j in r_todo:
        title = j.get('title')
        status = j.get('completed')

        new_dict = {'task': title,
                    'completed': status,
                    'username': name}

        task_list.append(new_dict)

    data = {ee_id: task_list}
    with open('todo_all_employees.json', 'w', newline='') as write_file:
        json.dump(data, write_file)


if __name__ == '__main__':
    json_dict()
