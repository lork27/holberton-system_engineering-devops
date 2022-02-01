#!/usr/bin/python3
"""
module that takes argv 1 and uses it to request to a fake api!
"""
import requests
from sys import argv
import json

if __name__ == "__main__":
    if len(argv) == 2 and argv[1].isdigit():
        num = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        usr = requests.get(url+'users/{}'.format(argv[1])).json()["username"]
        r = requests.get(url + "todos?userId={}".format(num)).json()

        nametask = {str(num): []}
        for element in r:
            tmp_dict = {'task': str(element["title"]),
                        'completed': element["completed"],
                        'username': str(usr)}
            nametask[str(num)].append(tmp_dict)
        with open("{}.json".format(num), "w") as f:
            json.dump(nametask, f)
    else:
        print("length WRONG")
