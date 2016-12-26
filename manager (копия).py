#!/usr/bin/env python
# -*- coding: utf-8 -*-


leftb = None
rightb = None
myo = None
myo_st = 0

import threading
#from websocket_server import WebsocketServer
from utils import *
from connect import *
from myo_control import *

#get_android_commands(conn)
#fuser -vn tcp port
#sudo kill -9 27635


'''
def new_client(client, server):
	global conn_web
	conn_web = client

def run_socket():
	global web
	web.run_forever()

def send_web(dest, speed):
	global web, conn_web
	if conn_web != 0 :
	   web.send_message(conn_web, perform_json(speed, dest, speed))
'''

def proc_imu(quat, acc, gyro, times=[]):
	global myo_st
	threads = threading.enumerate()
	dist = threads[1].dist

	if myo_st == 1:
		roll = get_roll(quat)
		pitch = get_pitch(quat)

		speed_d = speed_setting(pitch, 20, 100)
		speed_t = speed_setting(roll, 40, 100)

		if (get_myo_turn(roll) == 5):
			com = get_myo_dest(pitch)
			speed = speed_d
		else:
			com = get_myo_turn(roll)
			speed = speed_t

		motors_set(com, speed, dist)

def proc_pose(p, times=[]):
	global myo_st
	threads = threading.enumerate()
	dist = threads[1].dist
	
	if p == Pose.DOUBLE_TAP:
		if myo_st == 2:
			myo_st = 1
		elif myo_st == 1:
			myo_st = 2

	if myo_st == 2:
		if p == Pose.REST:
			motors_set(0, 70, dist)
		elif p == Pose.FINGERS_SPREAD:
			motors_set(1, 70, dist)
		elif p == Pose.FIST:
			motors_set(2, 70, dist)
		elif p == Pose.WAVE_IN:
			motors_set(3, 70, dist)
		elif p == Pose.WAVE_OUT:
			motors_set(4)

def arduino_read(ard):
	lv = rv = dist = s = 0
	s = ard.readline()
	ard.reset_input_buffer()
	if s and check_int(s):
		lv, rv, dist = decode(int(s))
		return lv, rv, dist
	else:
		None, None, None

def on_arduino():
	is_connect = 0
	print 'Try to connect with Arduino'
	try:   
		arduino = arduino_connect()
		is_connect = 1
		print 'Success'
	except Exception, e:
		print 'Failed ',e

	if is_connect:
		t = threading.currentThread()
		while getattr(t,'do_run', True):
			_lv, _rv, _dist = arduino_read(arduino)
			setattr(t, 'lv', _lv)
			setattr(t, 'rv', _rv)
			setattr(t, 'dist', _dist)

if __name__ == "__main__":
	try:
		print 'Try to setup motors'
		GPIO_setup()

		leftb = GPIO.PWM(lb, 50)
		rightb = GPIO.PWM(rb, 50)

		leftb.start(0)
		rightb.start(0)

		print 'Success'
	except Exception, e:
		print 'Failed ',e  
	
	ar = threading.Event()
	tar = threading.Thread(target=on_arduino, args=())
	tar.do_run = True
	tar.lv = tar.rv = 0
	tar.dist = 100
	tar.start()
	ar.set()

	try:
		print 'Try to connect with myo'
		myo = myo_connect()
		myo.add_imu_handler(proc_imu)
		myo.add_pose_handler(proc_pose)
		print 'Success'
	except Exception, e:
		print 'Failed ',e

	try:
		print 'Try to connect with android'
		android = android_connect()
		print 'Success'
	except Exception, e:
		print 'Failed',e
		#web.close()
		arduino.close()
	
	''' 
	try:
		print 'Try to connect with web'
		web = WebsocketServer(8082, host='0.0.0.0')
		client = web.set_fn_new_client(new_client)
		print 'Succes'
	except Exception, e:
		print 'Failed',e
	'''

	try:
		while 1:
			myo.run(1)
			threads = threading.enumerate()
			dist = threads[1].dist
			android.setnonblocking(0)	
			try:
				data = android.recv(1024)
				dest, speed, myo_st = decode(int(data))
				motors_set(dest, speed, tar.dist)
			except:
				data = None
			if myo_st:
				myo.run(1)
	except KeyboardInterrupt:
		pass
	finally:
		True