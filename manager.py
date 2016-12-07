#!/usr/bin/env python
# -*- coding: utf-8 -*-
from protocol import encode,decode
from myo_control import *
from fuzzy_logic import *
from GPIO_control import *
import socket
import serial

#get_android_commands(conn)
#fuser -vn tcp port
#sudo kill -9 27635

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
	print 'Success'
except Exception, e:
	print 'Failed to connect with Arduino'

try:
	print 'Try to setup motors'
	GPIO_setup()

	leftb = GPIO.PWM(lb, 50)
	rightb = GPIO.PWM(rb, 50)

	leftb.start(0)
	rightb.start(0)
	print 'Success'
except Exception, e:
	print 'Failed to setup motors',e
	#arduino.close()


'''
try:
	print 'Try to connect with android'
	android = android_connect()
except Exception, e:
	print 'Failed to connect with android',e
	#arduino.close()	
'''
try:
	print 'Try to connect with MYO'
	myo = myo_connect()
	print 'Success'
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
			lv, rv, dist = decode(int(s))
		'''
		data = android.recv(8).strip('\0')
		if data:
			dest, speed, myo_st = decode(long(data))
			print dest, speed, myo_st
			speed = fuzzy_speed_calc(dist)
			motors.send(str(encode(dest,speed,0)))
		'''

		if myo_st:	
			dest, speed = myo_command(myo) 

			if dest in range(5):
				parse_command(dest)
				if (dest == 1):
					speed = speed*fuzzy_speed_calc(dist) 
			if speed in range(101):
				leftb.ChangeDutyCycle(speed)
				rightb.ChangeDutyCycle(speed)

		parse_command(1)
		speed = fuzzy_speed_calc(dist) 
		leftb.ChangeDutyCycle(speed)
		rightb.ChangeDutyCycle(speed)		
		#time.sleep(0.1)
except KeyboardInterrupt:
	arduino.close()
	android.close()
	leftb.stop()
	rightb.stop()
	GPIO.cleanup()
	print 'bad'
