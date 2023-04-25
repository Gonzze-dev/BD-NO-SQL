import json
import threading
import time

from flask import Flask, jsonify
from cargarCapitulos import cargarCapitulos
from changeStatusChapters import changeStatusChapters
from connection import connection
from capitulos import capitulos

from obtenerCapitulos import obtenerCapitulos

from flask_cors import CORS

from response import resp

app = Flask(__name__)

CORS(app)
port = '3001'
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

def generateChapters():
    listChapter = 'listChapter'

    listExists = connection.exists(listChapter)
    if(not listExists):
        cargarCapitulos(connection, capitulos)

#PUNTO 1
@app.route("/getChapters", methods=['GET'])
def getChapters():
    resp = {
        'status': 200,
        'message': '',
        'data': []
    }
    listChapter = 'listChapter'
    totalChapters = 0
    generateChapters()

    totalChapters = connection.llen(listChapter)

    chapters = obtenerCapitulos(connection, totalChapters)

    resp['status'] = 200
    resp['message'] = 'Capitulos obteniudos con exito!'
    resp['data'] = chapters

    return resp

#PUNTO 2
@app.route("/rent/<chapterid>", methods=['POST'])
def rentChapter(chapterid=0):
    resp = {
        'status': 200,
        'message': '',
        'data': []
    }
    chapters = getChapters()['data'][:]

    listChapter = "listChapter"
    chapteridInt = int(chapterid) - 1

    minutos_exp = 1
    tiempo_exp = 10 * minutos_exp

    if(chapteridInt >= 0 and chapteridInt <= 7):
        chapter = chapters[chapteridInt]
    else:
        resp['message'] = 'ERROR, ID FUERA DE RANGO'
        resp['status'] = 400

        return jsonify(resp)

    chapteridInt += 1

    chapterRentDump = connection.get(chapteridInt)

    if(chapterRentDump is None):
        resp['message'] = 'Capitulo reservado'

        chapter['status'] = 'reservado'
        chapterJDump = json.dumps(chapter)
        
        chapterIdJDump = chapter['chapter'] - 1
        connection.setex(chapteridInt, tiempo_exp, chapterJDump)
        connection.lset(listChapter, chapterIdJDump, chapterJDump)
        return resp
    
    else:
        resp['message'] = 'ERROR, EL CAPITULO ESTA RESERVADO'
        resp['status'] = 400

        return resp

@app.route("/payment/<chapterid>",methods=['POST'])
def paymentOk(chapterid=0):
    resp = {
        'status': 200,
        'message': '',
        'data': []
    }
    chapters = getChapters()['data'][:]

    listChapter = "listChapter"
    chapteridInt = int(chapterid) - 1

    minutos_exp = 1
    tiempo_exp = 20 * minutos_exp

    if(chapteridInt >= 0 and chapteridInt <= 7):
        chapter = chapters[chapteridInt]
    else:
        resp['message'] = 'ERROR, ID FUERA DE RANGO'
        resp['status'] = 400
        return resp

    chapteridInt += 1

    chapterRentDump = connection.get(chapteridInt)

    if(chapterRentDump is not None):
        chapterRent = json.loads(chapterRentDump)

        if(chapterRent['status'] == 'reservado'):

            chapter['status'] = 'alquilado'
            chapterJDump = json.dumps(chapter)
            chapterIdJDump = chapter['chapter'] - 1
            connection.setex(chapteridInt, tiempo_exp, chapterJDump)
            connection.lset(listChapter, chapterIdJDump, chapterJDump)

            resp['message'] = 'Capitulo alquilado'
            return resp
        else:
            resp['status'] = 400
            resp['message'] = 'ERROR, EL CAPITULO NO ESTA DISPONIBLE'
            return resp
       
    else:

        resp['status'] = 400
        resp['message'] = 'ERROR, AL INTENTAR PROCESAR EL PAGO'

        return resp

def verificarYCambiarEstado(status):
    chapters = getChapters()['data']
    changeStatusChapters(status)

def timerVerificarYCambiarEstado(totalTime, status):
    while True:
        verificarYCambiarEstado(status)
        time.sleep(totalTime)

if(__name__ == "__main__"):

    timeRentThread = 10
    timeAlqThread = 60
    threading.Thread(target=timerVerificarYCambiarEstado, args=(timeRentThread,'reservado', )).start()
    threading.Thread(target=timerVerificarYCambiarEstado, args=(timeAlqThread,'alquilado', )).start()
    app.run(host="localhost", port="3001", debug=False)