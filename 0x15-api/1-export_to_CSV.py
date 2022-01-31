#!/usr/bin/python3
"""
module that takes argv 1 and uses it to request to a fake api!
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2 and argv[1].isdigit():
        num = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        usr = requests.get(url+'users/{}'.format(argv[1])).json()["username"]
        r = requests.get(url + "todos?userId={}".format(num)).json()
        nametask = ""
        for element in r:
            nametask += '"{}","{}","{}","{}"\n'.format(
                num, usr,  element["completed"], element["title"])
        with open("{}.csv".format(num), "w") as f:
            f.write(nametask)
    else:
        print("length WRONG")
