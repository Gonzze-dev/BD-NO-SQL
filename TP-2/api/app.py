import asyncio
import json
from flask import Flask
from cargarCapitulos import cargarCapitulos
from connection import connection
from capitulos import capitulos
from getChapter import getChapter
from obtenerCapitulos import obtenerCapitulos

app = Flask(__name__)

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
async def rentChapter(chapterid=0):
    keyName = ('chapter' + str(chapterid))

    chapter = getChapter(connection, keyName)
    chapter['status'] = "reservado"

    connection.getset(keyName, json.dumps(chapter))
    await asyncio.sleep(10)

    return chapter

@app.route("/payment/<status>/<chapterid>")
def paymentStatus(status, chapterid=0):
    keyName = ('chapter' + str(chapterid))

    chapter = getChapter(connection, keyName)

    chapter['status'] = "alquilado"

    connection.set(keyName, json.dumps(chapter))
    
    return chapter

if(__name__ == "__main__"):
    app.run(host="localhost", port="3000", debug=False)