#!/usr/bin/python3
"""using this REST API, for a given employee ID, returns
   information about his/her TODO list progress.
"""
from sys import argv
import json
import requests

if __name__ == "__main__":
    num = argv[1]
    u_link = "https://jsonplaceholder.typicode.com/users/{}".format(num)
    r = requests.get(u_link)
    r_user = r.json()['name']
    r_username = r.json()['username']

    t_link = "https://jsonplaceholder.typicode.com/user/{}/todos".format(num)
    t_l = requests.get(t_link)
    t_link_data = t_l.json()
    t_lengh = len(t_link_data)
    lengh = 0
    task = []
    for i in t_link_data:
        """export to csv"""
        _str = {
            "task": i['title'],
            "completed": i['completed'],
            "username": r_username,
        }

        task.append(_str)
    _task = {str(argv[1]): task}

    with open(f"{num}.json", "w") as file:
        json.dump(_task, file)
    # with open(f"{num}.csv", 'w', newline='') as file:
    #   data = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
    #   data.writerows(task)
    # print(_task)
