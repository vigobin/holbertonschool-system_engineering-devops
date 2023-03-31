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
    completed = sum(i.get('completed') for i in r_todo if i)

    with open('{}.csv'.format(emp_id), 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quoting=csv.QUOTE_ALL)
        for j in r_todo:
            title = j.get('title')
            status = j.get('completed')
            spamwriter.writerow([emp_id, name, status, title])


if __name__ == '__main__':
    gather(argv[1])
