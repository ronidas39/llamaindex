import json

def readfile(file):
    with open(file,"r") as f1:
        data=json.load(f1)
        return data
