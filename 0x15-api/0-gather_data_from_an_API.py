#!/usr/bin/python3
"""using this REST API, for a given employee ID, returns
   information about his/her TODO list progress.
"""
import requests
from sys import argv

if __name__ == "__main__":
    num = argv[1]
    u_link = "https://jsonplaceholder.typicode.com/users/{}".format(num)
    r = requests.get(u_link)
    r_user = r.json()['name']

    t_link = "https://jsonplaceholder.typicode.com/user/{}/todos".format(num)
    t_l = requests.get(t_link)
    t_link_data = t_l.json()
    t_lengh = len(t_link_data)
    lengh = 0
    task = []
    for i in t_link_data:
        if i['completed'] is True:
            lengh += 1
            task.append(i['title'])
        pass

    print("Employee {} is done with tasks({}/{}):"
          .format(r_user, lengh, t_lengh))
    for i in task:
        print("\t {}".format(i))
