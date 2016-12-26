import serial
import socket
from myo_raw import *

def arduino_connect():
	ard = serial.Serial('/dev/arduino', 9600)
	ard.readline()
	return ard

def android_connect():
    sock = socket.socket()
    sock.bind(('', 9092))
    sock.listen(1)
    conn, addr = sock.accept()
    return conn

def myo_connect():
    myo = MyoRaw(sys.argv[1] if len(sys.argv) >= 2 else None)
    myo.connect()
    return myo