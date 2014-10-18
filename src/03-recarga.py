import serial
from flask import *

arduino = serial.Serial('/dev/ttyACM0', 9600)

app = Flask(__name__)
@app.route("/")
def index():
  arduino.write("GET\n")
  luz = arduino.readline()
  
  return """
  <html>
  <head>
    <meta http-equiv="refresh" content="1">  
  </head>
    <body> potenciometro: %s </body>
  </html>""" % luz

app.run (host='localhost',  port=8080)
