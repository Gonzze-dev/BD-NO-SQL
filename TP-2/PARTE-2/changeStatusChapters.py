import json
from connection import connection
from capitulos import capitulos

def getIdsChapters(chapters):
    chaptersId = []
    for i in range(0, len(chapters)):
        chapter1d = chapters[i]['chapter']
        chaptersId.append(chapter1d)

    return chapters

def changeStatusChapters(chapters, status):
    listChapter = 'listChapter'
    lenListChapter = connection.llen(listChapter)
    chaptersId = getIdsChapters(chapters)
    

    for j in range(0, lenListChapter):
        chapterList = json.loads(connection.lindex(listChapter, j))
        if (chapterList['chapter'] not in chaptersId
            and chapterList['status'] == status):
            chapterList['status'] = 'disponible'

            #chapterListJdump = json.dump(chapterList)
            #connection.lset(listChapter, j, chapterListJdump)



