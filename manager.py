#!/usr/bin/env python
# -*- coding: utf-8 -*-


leftb = None
rightb = None
myo = None
android = None
myo_st = 0

web = 0
conn_web = 0

import threading
from websocket_server import WebsocketServer
from utils import *
from connect import *
from myo_control import *

def new_client(client, server):
	global conn_web
	conn_web = client

def run_socket():
	global web
	web.run_forever()

def send_web(lv, dist, speed, dest, dest_myo):
	global web, conn_web
	if conn_web != 0 :
		web.send_message(conn_web, perform_json(lv, dist, speed, dest, dest_myo))


def proc_imu(quat, acc, gyro, times=[]):
	global myo_st
	threads = threading.enumerate()
	dist = threads[1].dist
	lv = threads[1].lv
	rv = threads[1].rv
	lv = (lv + rv) // 2

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
		print 'com = ',com,' speed = ', speed
		send_web(lv,dist,speed,com,com)
		motors_set(com, speed, dist, leftb, rightb)

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
			motors_set(0, 30, dist, leftb, rightb)
		elif p == Pose.FINGERS_SPREAD:
			motors_set(1, 30, dist, leftb, rightb)
		elif p == Pose.FIST:
			motors_set(2, 30, dist, leftb, rightb)
		elif p == Pose.WAVE_IN:
			motors_set(3, 30, dist, leftb, rightb)
		elif p == Pose.WAVE_OUT:
			motors_set(4, 30, dist, leftb, rightb)

def arduino_read(ard):
	lv = rv = dist = s = 0
	s = ard.readline()
	ard.reset_input_buffer()
	if s and check_int(s):
		lv, rv, dist = decode(int(s))
		return lv, rv, dist
	else:
		0, 0, 100

def on_arduino():
	is_connect = 0
	print 'Try to connect with Arduino'
	try:   
		arduino = arduino_connect()
		is_connect = 1
		print 'Success'
	except Exception, e:
		print 'Failed ',e
	time.sleep(1)
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
		tar.do_run = False
	
	try:
		print 'Try to connect with android'
		android = android_connect()
		print 'Success'
	except Exception, e:
		print 'Failed',e
		tar.do_run = False
		myo.disconnect()

	try:
		print 'Try to connect with web'
		web = WebsocketServer(8082, host='0.0.0.0')
		client = web.set_fn_new_client(new_client)
		print 'Success'
	except Exception, e:
		print 'Failed',e
		tar.do_run = False
		myo.disconnect()
		android.close()
	
	twe = threading.Thread(target=run_socket, args=())
	twe.start()
	try:
		while 1:
			if myo_st:
				myo.run(1)

			android.setblocking(0)	
			try:
				data = android.recv(1024)
				if data:
					dest, speed, myo_st = decode(int(data))
					send_web(tar.lv,tar.dist,speed,dest,dest)
			except:
				True

	except KeyboardInterrupt:
		pass
	finally:
		web.close()
		tar.do_run = False
		myo.disconnect()
		android.close()
		