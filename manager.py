#!/usr/bin/env python
# -*- coding: utf-8 -*-
from protocol import encode,decode
from myo_control import *
from fuzzy_logic import *
import socket
import serial

#get_android_commands(conn)

def motors_connect():
	sock = socket.socket()
	sock.bind(('', 9093))
	sock.listen(1)
	conn, addr = sock.accept()
	return conn

def android_connect():
	sock = socket.socket()
	sock.bind(('', 9092))
	sock.listen(1)
	conn, addr = sock.accept()
	return conn

def myo_connect():
	myo = Myo(sys.argv[1] if len(sys.argv) >= 2 else None)
	myo.connect()
	while (not myo.getGyro()):
		print('Wait a myo')
		myo.run()
	return myo

try:
	print 'Try to connect with Arduino'
	arduino = serial.Serial('/dev/arduino', 9600)
	arduino.readline()
	print 'Arduino successfully connected'
except Exception, e:
	print 'Failed to connect with Arduino'

try:
	print 'Try to connect with motors driver'
	motors = motors_connect()
	print 'Motors driver successfully connected'
except Exception, e:
	print 'Failed to connect with motors driver',e
	#arduino.close()

try:
	print 'Try to connect with android'
	android = android_connect()
except Exception, e:
	print 'Failed to connect with android',e
	#arduino.close()	

try:
	print 'Try to connect with MYO'
	myo = myo_connect()
	print 'MYO successfully connected'
except Exception, e:
	print 'Failed to connect with MYO',e
	#arduino.close()	

def check_int(str):
    try:
        int(str)
        return True
    except:
        return False

myo_st = False
try:
	while True:
		s = arduino.readline()
		if check_int(s):
			data = int(s)
			lv, rv, dist = decode(data)
		
		if myo_st:	
			com, speed = myo_command(myo)
			speed = speed*fuzzy_speed_calc(dist)
			data = encode(com,speed,0)
			motors.send(str(data)) 
	
		data = android.recv(1024)
		if data:
			#dest, speed, myo_st = decode(int(data))
			#speed = speed*fuzzy_speed_calc(dist)
			#motors.send(str(encode(data,50,0)))
except KeyboardInterrupt:
	arduino.close()
	android.close()
	motors.close()
	print 'bad'
