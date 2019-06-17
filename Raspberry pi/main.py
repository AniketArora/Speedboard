from flask import Flask, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS

from RPi import GPIO

from helpers.Database import Database

from SerialPort import SerialPort
import threading

serialPort = SerialPort()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)
hallsensor = 4

f = 0
r = 0

eindpoint = '/api/vi/'

conn = Database(app=app, host='192.168.4.1', port=3306, user='mct', password='mct', db='projectdb')


@app.route('/')
def hallo():
    return "Server is running"


def start():
    serialPort.send("Start")
    threading.Timer(1, start).start()
    data = conn.set_data("INSERT INTO historiek(GebruikersID, ActionID, waarde) VALUES (%s, %s, %s)", [102, 1, 1])
    print("threading works")
    return data


def go():
    serialPort.send("Forward")
    threading.Timer(1, go).start()
    print("Sending forward signal")


def stop():
    serialPort.send("Backward")
    threading.Timer(1, stop).start()
    print("Sending reverse signal")


@socketio.on("connect")
def connecting():
    socketio.emit("connected")
    print("Connection with client established")
    threading.Timer(1, start).start()


@socketio.on("forward")
def forward(fSignal=f):
    print("Going forward")
    if fSignal % 2 == 0:
        fSignal += 1
        threading.Timer(1, go).start()
        data = conn.set_data("INSERT INTO historiek(GebruikersID, ActionID, waarde) VALUES (%s, %s, %s)", [102, 5, 1])
        return data
    else:
        fSignal += 1
        threading.Timer(1, go).cancel()
        data = conn.set_data("INSERT INTO historiek(GebruikersID, ActionID, waarde) VALUES (%s, %s, %s)", [102, 5, 0])
        return data


@socketio.on("reverse")
def reverse(rSignal=r):
    print("Going backwards")
    if rSignal % 2 == 0:
        rSignal += 1
        threading.Timer(1, stop).start()
        data = conn.set_data("INSERT INTO historiek(GebruikersID, ActionID, waarde) VALUES (%s, %s, %s)", [102, 5, 1])
        return data
    else:
        rSignal += 1
        threading.Timer(1, stop).cancel()
        data = conn.set_data("INSERT INTO historiek(GebruikersID, ActionID, waarde) VALUES (%s, %s, %s)", [102, 5, 0])
        return data


if __name__ == '__main__':
    socketio.run(app=app, host="0.0.0.0", port="5000")
