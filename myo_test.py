#!/usr/bin/env python
# -*- coding: utf-8 -*-
from myo_control import *
import socket

def myo_connect():
	myo = Myo(sys.argv[1] if len(sys.argv) >= 2 else None)
	myo.connect()
	while (not myo.getGyro()):
		print('Wait a myo')
		myo.run()
	return myo

try:
	print 'Try to connect with myo'
	myo = myo_connect()
except Exception, e:
	print 'Failed to connect with myo',e
	#arduino.close()	

myo_st = True

try:
	while True:
		if myo_st:
			dest, speed = myo_command(myo)
			print dest,' ',speed
		
		#time.sleep(0.1)
except KeyboardInterrupt:
	print 'bad'
