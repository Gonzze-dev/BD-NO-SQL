from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hola mundo"

@app.route("/about")
def about():
    return "about python flask"

if(__name__ == "__name__"):
    app.run(hostname="localhost", port="3000", debug=False)