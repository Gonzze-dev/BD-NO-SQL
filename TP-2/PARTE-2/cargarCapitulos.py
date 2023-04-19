import json


def cargarCapitulos(connection, chapters):
    listChapter = 'listChapter'
    
    for i in range(0, len(chapters)):
        capitulo = json.dumps(chapters[i])
        
        if not connection.exists(listChapter):
            connection.lpush(listChapter, capitulo)
        else:
            connection.rpush(listChapter, capitulo)
