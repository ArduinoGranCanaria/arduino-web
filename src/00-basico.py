from flask import *

app = Flask(__name__)

@app.route("/")
def index():
  return "<html><body> Hola mundo! </body><html>"

app.run (host='localhost',  port=8080)
