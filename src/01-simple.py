import serial
from flask import *

arduino = serial.Serial('/dev/ttyACM0', 9600)

app = Flask(__name__)
@app.route("/")
def index():
  luz = arduino.readline()
  return "<html><body>fotosensor: " + luz + "</body><html>"

app.run (host='localhost',  port=8080)