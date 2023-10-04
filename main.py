import os
import json

def readJSON(path):
    return json.loads(open(path).read())

def processFolder(path):
    html = "<!doctype html><html><head><title>Snapchat Item Viewer</title"
    
    if os.path.exists(path + "/json"):
        # build profile info
        x = readJSON(path + "/json/" + "account.json")
        username = x["Basic Information"]["Username"]
        name = x["Basic Information"]["Name"]
        creationDate = x["Basic Information"]["Creation Date"]

        html += "</head><body><h1>{name} ({username})</h1>"
        html += "<h2>Joined: {creationDate}</h2>"

        if os.path.exists(path + "/memories"):
            for file in os.listdir(path + "/memories"):
                file_name, file_extension = os.path.splitext(path + "/memories/" + file)
                file_extension = file_extension.lower()
                if file_extension == ".mp4":
                    html += "<br>"
                    loc = "memories/" + file
                    html += '<video width="360" height="640" controls><source src="{loc}" type="video/mp4">not support</video>'
                else:
                    html += "<br>"
                    loc = "memories/" + file
                    html += "<img src='{loc}' />"
    return html
