#!/usr/bin/python3
"""
module that takes argv 1 and uses it to request to a fake api!
"""
import json
import requests

if __name__ == "__main__":
    num = 2
    url = "https://jsonplaceholder.typicode.com/"
    users = []

    for i in range(1, 11):
        users.append(requests.get(url+'users/{}'.format(i)).json()["username"])
    nametask = {}
    for num, usr in enumerate(users, 1):
        r = requests.get(url + "todos?userId={}".format(num)).json()
        nametask[num] = []
        for element in r:
            tmp_dict = {'username': usr,
                        'task': element["title"],
                        'completed': element["completed"]
                        }
            nametask[num].append(tmp_dict)

    with open("todo_all_employees.json", "w") as f:
        json.dump(nametask, f)
