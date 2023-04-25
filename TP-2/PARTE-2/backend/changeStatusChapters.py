import json
from connection import connection

def getIdsChapters(lenChapters):
    chaptersId = []
    chapterId = ''
    for i in range(0, lenChapters):
        chapterIdDump = connection.get(i+1)


        if chapterIdDump is not None:
            chapterId = json.loads(chapterIdDump)['chapter']
            chaptersId.append(chapterId)

    return chaptersId

def changeStatusChapters(status):
    listChapter = 'listChapter'
    lenListChapter = connection.llen(listChapter)
    chaptersId = getIdsChapters(lenListChapter) #obtengo los capitulos rentados o alquilados

    for j in range(0, lenListChapter):
        chapterList = json.loads(connection.lindex(listChapter, j))
        if (chapterList['chapter'] not in chaptersId
            and chapterList['status'] == status):
            chapterList['status'] = 'disponible'

            chapterListJdump = json.dumps(chapterList)
            connection.lset(listChapter, j, chapterListJdump)



