import sys
import time
import threading
sys.path.insert(0, '../')
from connect import *
from manager import arduino_read, on_arduino

def test_arduino_connect():
	ard = arduino_connect()
	time.sleep(1)
	s = ard.readline()
	if ard and s:
		print('arduino_connect | OK')
	else:
		print('arduino_connect | FAILED')

def test_arduino_read():
	ard = arduino_connect()
	time.sleep(1)
	if arduino_read(ard):
		print('arduino_read | OK')
	else:
		print('arduino_read | FAILED')

def test_on_arduino():
	tar = threading.Thread(target=on_arduino, args=())
	tar.do_run = True
	tar.lv = tar.rv = 0
	tar.dist = 100
	tar.start()
	time.sleep(1)
	threads = threading.enumerate()
	dist = threads[1].dist
	if dist:
		print('on_arduino | OK')
	else:
		print('on_arduino | FAILED')

def test_android_connect():
	print 'Please, restart the application on your android-phone')
	try:
		android = android_connect()
		print('android_connect | OK')
	except Exception, e:
		print('android_connect | FAILED'),e

def test_android_read():
	print 'Please, restart the application on your android-phone')
	try:
		android = android_connect()
		android.setblocking(0)	
		try:
			data = android.recv(1024)
			if data:
				print('android_connect_read | OK')
			else:
				print('android_connect_read | FAILED')
		except:
			True
		print('android_connect_read | OK')
	except Exception, e:
		print('android_connect_read | FAILED'),e
		
		
def test_myo_connect():
	try:
		myo = myo_connect()
		myo.add_imu_handler(proc_imu)
		myo.add_pose_handler(proc_pose)
		print('myo_connect | OK')
	except Exception, e:
		print('myo_connect | FAILED'),e

test_arduino_connect()
test_arduino_read()
test_on_arduino()
test_android_connect()
test_android_read()
test_myo_connect()