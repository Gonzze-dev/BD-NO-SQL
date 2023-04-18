
const redis = require("redis")
var express = require('express')
const cors = require('cors')


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

app.post('/add/:numberChapter/:character', async (req, res) => {
    let numberChapter = req.params.numberChapter
    let character = req.params.character

    let chapter = `chapter${numberChapter}`

    let listExists = redisclient.exists(chapter)

    let message = ``

    if (listExists)
    {
        message = `CAPITULO '${chapter}' CREADO y PERSONAJE '${character} AGREGADO'`
        redisclient.lPush(chapter, [character])
    }
    else
    {
        message = `PERSONAJE '${character}' AGREGADO A '${chapter}'`
        redisclient.rPush(chapter, [character])
    }

    const result = await redisclient.lRange(chapter, 0, -1)
    console.log(result)

    res.status(200).send(message)
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