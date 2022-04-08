import json
from urllib.request import urlopen

class Node:
    def __init__(self, name, parent, count, price, childs, cost):
        self.name = name
        self.parent = parent
        self.count = count
        self.price = price
        self.childs = childs
        self.cost = cost
def createRootNode(dict):
    root = Node("", None, 0, 0, [], 0)
    root.name = dict["name"]
    root.count = dict["count"]
    root.childs = []
    root.parent = None
    root.price = 0
    root.cost = 0
    return root

def construct(parent,childs):
    for key in childs:
        print(key["name"])
        childNode = Node("", None, 0, 0, [], 0)
        childNode.name = key["name"]
        childNode.count = key["count"]
        childNode.parent = parent
        keys = key.keys()
        if(list(keys)[2] == "price"):
            childNode.price = key["price"]
            childNode.childs = []
            parent.childs.append(childNode)
        else:
            childNode.price = 0
            childs = list(key.values())[2]
            construct(childNode, childs)
            parent.childs.append(childNode)

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
            printStructure(key)

def printRoot(root):
    print(
        "Root Node: "
        "Name:", root.name, ","
        " Count:", root.count, ","
        " Cost:", root.cost
    )

def main():
    url = "https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_3.json"
    response = urlopen(url)
    dict = json.load(response)
    root = createRootNode(dict)
    childs = list(dict.values())[2]
    construct(root, childs)
    printRoot(root)
    printStructure(root)
if __name__ == "__main__":
    main()