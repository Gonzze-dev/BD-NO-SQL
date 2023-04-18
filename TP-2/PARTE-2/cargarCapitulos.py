import json


def cargarCapitulos(connection, capitulos):

    for i in range(0, len(capitulos)):
        capitulo = json.dumps(capitulos[i])
        
        keyName = ('chapter' + str(i+1))

        connection.set(keyName, capitulo)

