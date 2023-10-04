import os
import json

def readJSON(path):
    return json.loads(open(path).read())

def writeFile(content, name):
    with open(name, 'a') as w:
        w.write(content)

def processFolder(path):
    html = "<!doctype html><html><head><title>Snapchat Item Viewer</title"
    
    if os.path.exists(path + "/json"):
        # build profile info
        x = readJSON(path + "/json/" + "account.json")
        username = x["Basic Information"]["Username"]
        name = x["Basic Information"]["Name"]
        creationDate = x["Basic Information"]["Creation Date"]

        html += f"</head><body><h1>{name} ({username})</h1>"
        html += f"<h2>Joined: {creationDate}</h2>"

        if os.path.exists(path + "/memories"):
            for file in os.listdir(path + "/memories"):
                file_name, file_extension = os.path.splitext(path + "/memories/" + file)
                file_extension = file_extension.lower()
                if file_extension == ".mp4":
                    html += "<br>"
                    loc = "memories/" + file
                    html += f'<video width="360" height="640" controls><source src="{loc}" type="video/mp4">not support</video>'
                else:
                    html += "<br>"
                    loc = "memories/" + file
                    html += f"<img src='{loc}' />"
    return html

writeFile(processFolder(r"C:\Users\ufhw8\Downloads\snapchat_sep2023-2_s1"), "new.html")