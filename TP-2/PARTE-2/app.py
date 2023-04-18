import json
from flask import Flask
from cargarCapitulos import cargarCapitulos
from connection import connection
from capitulos import capitulos
from getChapter import getChapter
from obtenerCapitulos import obtenerCapitulos

app = Flask(__name__)

listChapterRent = 'listChapterRent'
listCHapterALquilado = 'listChapterAlquilado'

@app.route("/")
def index():
    lr = connection.lrange("marvel",0,-1)
    print(lr)
    return "hola mundo"

@app.route("/about")
def about():
    return "about python flask"

@app.route("/generateChapters")
def generateChapters():
    cargarCapitulos(connection, capitulos)

    return 'cargados'

@app.route("/getChapters")
def getChapters():
    totalCapitulos = len(capitulos)

    chapters = obtenerCapitulos(connection, totalCapitulos)

    return chapters

@app.route("/rent/<chapterid>")
def rentChapter(chapterid=0):
    
    keyName = ('chapter' + str(chapterid))
    chapter = getChapter(connection, keyName)

    chapter['status'] = "reservado"

    if not connection.exists(listChapterRent):
        connection.lpush(listChapterRent, json.dumps(chapter))
    else:
        objDumpListChaptersRent = connection.lrange(listChapterRent, 0, -1)
        objListChaptersRent = []

        for i in range(0, len(objDumpListChaptersRent)):
            obj = objDumpListChaptersRent[i]
            objListChaptersRent.append(json.loads(obj))

        for obj in objListChaptersRent:
            chapRent = obj["name"]

            if chapter['name'] == chapRent:
                return ("ERROR, EL CAPITULO `" + chapter["name"] + "` ESTA RESERVADO")
        
        
        connection.rpush(listChapterRent, json.dumps(chapter))
        print(listChapterRent, ':%s' % i)
        connection.expire(listChapterRent, ':%s' % i, 60)
        
    return chapter

@app.route("/payment/<status>/<chapterid>")
def paymentOk(status, chapterid=0):
    keyName = ('chapter' + str(chapterid))

    chapter = getChapter(connection, keyName)
    chapter['status'] = "alquilado"

    if not connection.exists(listChapterRent):
        return "ERROR AL ENCONTRAR LA LISTA DE LOS CAPITULOS RENTADOS"
    else:
        objDumpListChaptersRent = connection.lrange(listChapterRent, 0, -1)
        objListChaptersRent = []

        for obj in objDumpListChaptersRent:
            objListChaptersRent = json.loads(obj)
        
        for obj in objListChaptersRent:
            if chapter['name'] == obj['name']:
                if not connection.exists(listCHapterALquilado):
                    connection.lpush(listCHapterALquilado, json.dumps(chapter))
                else:
                    connection.rpush(listCHapterALquilado, json.dumps(chapter))
                break
                

    return chapter

if(__name__ == "__main__"):
    app.run(host="localhost", port="3000", debug=False)