import json

def getChapter(connection, keyName):
    chapter = json.loads(connection.get(keyName))

    return chapter
