import os
import json

def readJSON(path):
    return json.loads(open(path).read())

def processFolder(path):
    html = "<!doctype html><html><head><title>Snapchat Item Viewer"
    if os.path.exists(path + "/json"):
        # build profile info
        x = readJSON(path + "/json/" + "account.json")
        username = x["Basic Information"]["Username"]
        name = x["Basic Information"]["Name"]
        creationDate = x["Basic Information"]["Creation Date"]
