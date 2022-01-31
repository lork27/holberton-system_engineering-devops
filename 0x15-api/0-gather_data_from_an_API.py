#!/usr/bin/python3
from markupsafe import re
import requests
from sys import argv
"""
module that takes argv 1 and uses it to request to a fake api
"""

if __name__ == "__main__":
    if len(argv) == 2:
        num = argv[1]
        url = "https://jsonplaceholder.typicode.com"
        # print("{:d} type: {}".format(request_num, type(request_num)))
        usr = requests.get("{}/users/{}".format(url, num)).json()["name"]
        r = requests.get("{}/todos?userId={}".format(url, num)).json()
        # name = usr.json()["name"]
        tasks = 0
        total = 0
        nametask = ""
        for element in r:
            if element["completed"] is True:
                tasks += 1
                nametask += "\t" + element["title"] + "\n"
            total += 1
        print("Exployee {} is done with tasks ({}/{}):".format(usr,
                                                               tasks, total))
        print(nametask)
    else:
        print("length WRONG")
