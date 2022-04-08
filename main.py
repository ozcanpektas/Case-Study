import json
from sqlite3 import paramstyle
import urllib.request
import urllib.error
from json.decoder import JSONDecodeError

class Node:
    def __init__(self, name, parent, count, price, childs, cost):
        self.name = name
        self.parent = parent
        self.count = count
        self.price = price
        self.childs = childs
        self.cost = cost

    def construct(self, childs):
        for key in childs:
            print(key["name"])
            childNode = Node("", None, 0, 0, [], 0)
            childNode.name = key["name"]
            childNode.count = key["count"]
            childNode.parent = self
            keys = key.keys()
            if("price" in keys):
                childNode.price = key["price"]
                self.childs.append(childNode)
            else:
                childs = list(key.values())[2]
                childNode.construct(childs)
                self.childs.append(childNode)

    def printStructure(root):
        for key in root.childs:
            print(
                "Name:", key.name , ","
                " Count:", key.count, ","
                " Parent:",key.parent.name, ","
                " Price:", key.price, ","
                " Cost:", key.cost
            )
            if(key.parent != []):
                key.printStructure()

    def printRoot(root):
        print(
            "Root Node: "
            "Name:", root.name, ","
            " Count:", root.count, ","
            " Cost:", root.cost
        )

# Reads input from url
def readInput():
    try:
        url = input("Please enter the url or to exit press 'x': ")
        if(url == "x"):
            exit()
        page = urllib.request.urlopen(url)
        try:
            dict = json.load(page)
            return dict
        except JSONDecodeError as e:
            print("The url does not contain a json file.")
            return
    except urllib.error.HTTPError as err:
        if err.code == 404:
            print("Page not found!")
            return
        elif err.code == 403:
            print("Access denied!")
            return
        else:
            print("Something happened! Error code"), err.code
            return

def main():
    while(1):
        input = readInput()
        if(input == None):
            continue
        root = Node(input["name"], None, input["count"], 0, [], 0)
        childs = list(input.values())[2]
        root.construct(childs)
        root.printRoot()
        root.printStructure()
if __name__ == "__main__":
    main()