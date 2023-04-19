import json

def obtenerCapitulos(connection, totalCapitulos):
    objListChapters = []
    listChapter = 'listChapter'

    for i in range(0, totalCapitulos):
        objDumpListChapters = connection.lrange(listChapter, 0, -1)
        

    for i in range(0, len(objDumpListChapters)):
        obj = objDumpListChapters[i]
        objListChapters.append(json.loads(obj))

    return objListChapters
