#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
import json
import requests
from sys import argv


def json_dict():
    """Export data in the JSON format for all"""
    url = "https://jsonplaceholder.typicode.com/"
    r_users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as write_file:
        json.dump({
            user.get("id"): [{
                "username": user.get("username"),
                "task": todo.get("title"),
                "completed": todo.get("completed")
            } for todo in requests.get(url + "todos",
                                       params={"userId": user.get("id")})
                                       .json()]
            for user in r_users}, write_file)


if __name__ == '__main__':
    json_dict()
