import json
from connection import connection
from capitulos import capitulos

def getChaptersRentTemp():
    chapters = []
    
    for i in range(0, len(capitulos)):
        keyName = "chapter" + str(i)
        chapter = connection.get(keyName)

        if (chapter is not None):
            chapters.append(json.loads(chapter))
    
    return chapters