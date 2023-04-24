import json
import threading
import time

from flask import Flask
from cargarCapitulos import cargarCapitulos
from changeStatusChapters import changeStatusChapters
from connection import connection
from capitulos import capitulos
from getChapter import getChapter
from obtenerCapitulos import obtenerCapitulos
from multiprocessing import process

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

#PUNTO 1
@app.route("/getChapters")
def getChapters():
    listChapter = 'listChapter'
    totalChapters = 0

    if(not connection.exists(listChapter)):
        return 'ERROR, LA LISTA NO EXISTE'
    
    totalChapters = connection.llen(listChapter)

    chapters = obtenerCapitulos(connection, totalChapters)

    return chapters

#PUNTO 2
@app.route("/rent/<chapterid>")
def rentChapter(chapterid=0):
    chapters = getChapters()
    listChapter = "listChapter"
    chapteridInt = int(chapterid) - 1

    minutos_exp = 1
    tiempo_exp = 10 * minutos_exp

    if(chapteridInt >= 0 and chapteridInt <= 7):
        chapter = chapters[chapteridInt]
    else:
        return 'ERROR, ID FUERA DE RANGO'

    chapteridInt += 1

    chapterRentDump = connection.get(chapteridInt)

    if(chapterRentDump is None):
        chapter['status'] = 'reservado'
        chapterJDump = json.dumps(chapter)
        chapterIdJDump = chapter['chapter'] - 1
        connection.setex(chapteridInt, tiempo_exp, chapterJDump)
        connection.lset(listChapter, chapterIdJDump, chapterJDump)
    
        return 'Capitulo reservado'
    else:
        return 'ERROR, EL CAPITULO ESTA RESERVADO'

@app.route("/payment/<chapterid>")
def paymentOk(chapterid=0):
    chapters = getChapters()
    listChapter = "listChapter"
    chapteridInt = int(chapterid) - 1

    minutos_exp = 1
    tiempo_exp = 20 * minutos_exp

    if(chapteridInt >= 0 and chapteridInt <= 7):
        chapter = chapters[chapteridInt]
    else:
        return 'ERROR, ID FUERA DE RANGO'

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

            return 'Capitulo alquilado'
        else:
             return 'ERROR, EL CAPITULO NO ESTA DISPONIBLE'
       
    else:
        return 'ERROR, AL INTENTAR PROCESAR EL PAGO'

def verificarYCambiarEstado(status):
    chapters = getChapters()
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
    app.run(host="localhost", port="3000", debug=False)

    #verificarYCambiarEstadoAlq = threading.Timer(3, verificarYCambiarEstado('alquilado'))

    #verificarYCambiarEstado('reservado')

        #verificarYCambiarEstado('reservado')

    #verificarYCambiarEstadoRent.start()
