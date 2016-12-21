#!/usr/bin/env python
# -*- coding: utf-8 -*-

lv = 0
rv = 0
dist = 100
dest = 0
speed = 0
myo_st = 0
conn_web = 0
web = 0

import threading
import serial
#from websocket_server import WebsocketServer
from utils import *
from connect import *
from fuzzy_logic import *
from myo_raw import *
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

    	motors_set(com)

def proc_pose(p, times=[]):
    global myo_st

    if p == Pose.DOUBLE_TAP:
        if myo_st == 2:
            myo_st = 1
        elif myo_st == 1:
            myo_st = 2

    if myo_st == 2:
        if p == Pose.REST:
            motors_set(0,100)
        elif p == Pose.FINGERS_SPREAD:
            motors_set(1,100)
        elif p == Pose.FIST:
            motors_set(2, 100)
        elif p == Pose.WAVE_IN:
            motors_set(3, 100)
        elif p == Pose.WAVE_OUT:
            motors_set(4, 100)

def myo_connect():
    myo = MyoRaw(sys.argv[1] if len(sys.argv) >= 2 else None)
    myo.add_imu_handler(proc_imu)
    myo.connect()
    myo.add_pose_handler(proc_pose)
    return myo

def on_arduino(ard):
    global lv, rv, dist
    while 1:
        s = ard.readline()
        if s and check_int(s):
            lv, rv, dist = decode(int(s))
            if conn_web != 0:
                send_web(lv, 1)
            print 'arduino: ',lv,' ',rv,' ',dist

def on_myo():
    try:
        while True:
            myo.run(1)
    except KeyboardInterrupt:
        pass
    finally:
        myo.disconnect()
        print()

def on_fuzzy():
	global speed 
	speed= int(speed*fuzzy_speed_calc(dist)) 
	if speed in range(101):
		if (dest == 1):
			leftb.ChangeDutyCycle(speed)
			rightb.ChangeDutyCycle(speed)

def start_system():
	try:
	    print 'Try to connect with Arduino'
	    arduino = serial.Serial('/dev/arduino', 9600)
	    arduino.readline()
	    print 'Success'
	except Exception, e:
	    print 'Failed ',e

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
	    print 'Try to connect with android'
	    android = android_connect()
	    print 'Success'
	except Exception, e:
	    print 'Failed',e
	    #web.close()
	    arduino.close()

	try:
	    print 'Try to connect with myo'
	    myo = myo_connect()
	except Exception, e:
	    print 'Failed ',e
	    #web.close()
	    android.close()
	    arduino.close()  
	        
	#aw = threading.Event()
	ar = threading.Event()
	my = threading.Event()
	fu = threading.Event()

	#taw = threading.Thread(target=run_socket, args=())
	tar = threading.Thread(target=on_arduino, args=(arduino))
	tmy = threading.Thread(target=on_myo, args=())
	tfu = threading.Thread(target=on_fuzzy, args=())

	#taw.start()
	tar.start()
	tmy.start()
	tfu.start()

	#aw.set()
	ar.set()
	my.set()
	fu.set()

	try:
		while 1:
			data = android.recv(1024) 
			if data:
				dest, speed, new_myo_st = decode(int(data))
				global myo_st
				myo_st = new_myo_st
				if myo_st == 0:
					motors_set(dest)
					#send_web(dest, speed)
					print("android: ",dest, " ", speed," ", myo_st)
	except KeyboardInterrupt:
		pass
	finally:
	    #web.close()
	    android.close()
	    arduino.close()
	    myo.disconnect()
start_system()

