import json

def obtenerCapitulos(connection, totalCapitulos):
    chapters = []

    for i in range(0, totalCapitulos):
        keyName = ('chapter' + str(i+1))

        chapter = json.loads(connection.get(keyName))

        chapters.append(chapter)

    print(chapters)

    return chapters
