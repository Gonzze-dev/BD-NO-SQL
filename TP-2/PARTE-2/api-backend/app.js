
const redis = require("redis")
var express = require('express')
const cors = require('cors')
const listName = 'listChapter'

const redisclient = redis.createClient();

redisclient.connect()
var port = 3001
var app = express()

app.use(cors());

redisclient.on('connect', function(){
    console.log("Connected to redis")
})

redisclient.on("ready", () => {
    console.log("Connected!")
});
  
redisclient.on("error", (err) => {
    console.log("Error in the Connection")
});

const generateCharacters = () => {
    const chapters = [{'chapter': 1, 'name': 'The Mandalorian', 'status': 'disponible'},
              {'chapter': 2,'name': 'The Child', 'status': 'disponible'},
              {'chapter': 3,'name': 'The Sin', 'status': 'disponible'},
              {'chapter': 4,'name': 'Sanctuary', 'status': 'disponible'},
              {'chapter': 5,'name': 'The Gunslinger', 'status': 'disponible'},
              {'chapter': 6,'name': 'The Prisoner', 'status': 'disponible'},
              {'chapter': 7,'name': 'The Reckoning', 'status': 'disponible'},
              {'chapter': 8,'name': 'Redemption', 'status': 'disponible'}]

    let chaptersDump = []
    const listName = 'listChapter'

    for (chapter in chapters)
        chaptersDump.append(json.dump(chapter))

    let listExists = redisclient.exists(listName)
    console.log('ola')
    if (!listExists)
    {
        redisclient.lPush(listName, [chaptersDump])
    }
}

app.get('/'), async (req, res) => {
    cojnsol.elog('HOla mundo')
    res.status(200).send('HOla mundo')
}

app.get('/getChapters', async (req, res) => {
    
    generateCharacters()

    const chaptersDump = redisclient.lRange(listName, 0, -1)
    let chapters = []

    for (chapterDump in chaptersDump)
        chapters.append(json.load(chapterDump))
    

    res.status(200).send(chapters)
})

app.post('/delete/:numberChapter/:character', async (req, res) => {
    let numberChapter = req.params.numberChapter
    let character = req.params.character

    let chapter = `chapter${numberChapter}`

    let listExists = redisclient.exists(chapter)

    let message = ``
    let status = 0
    if (listExists)
    {
        message = `PERSONAJE '${character}' ELIMINADO DE '${chapter}'`
        status = 200
        redisclient.lRem(chapter, 0, character)
    }
    else
    {
        message = `ERROR, EL CAPITULO '${chapter}' NO EXISTE`
        status = 400
    }

    res.status(status).send(message)
})

app.get('/getCharacters/:numberChapter', async (req, res) => {
    let numberChapter = req.params.numberChapter

    let chapter = `chapter${numberChapter}`

    let listExists = redisclient.exists(chapter)
    let status = 0

    if (listExists)
    {
        const data = await redisclient.lRange(chapter, 0, -1)
        status = 200
        res.status(status).json(data)
    }
    else
    {
        message = `ERROR, EL CAPITULO '${chapter}' NO EXISTE`
        status = 400
        res.status(status).send(message)
    }
})


async function main()
{
    app.listen(port)
    console.log(`SERVER: https://localhost:${port}`)
}

main();