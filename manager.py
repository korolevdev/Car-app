#!/usr/bin/env python
# -*- coding: utf-8 -*-
from protocol import encode,decode
from myo_control import *
from fuzzy_logic import *
import socket
import serial

#get_android_commands(conn)

#print 'connected:', addr

#Connect Arduino
try:
	ser = serial.Serial('/dev/arduino', 9600)
	ser.readline()
	print 'Arduino connected'
except Exception, e:
	print 'Failed to connect with Arduino'

try:
	sock = socket.socket()
	sock.bind(('', 9093))
	sock.listen(1)
	conn, addr = sock.accept()
except Exception, e:
	print 'Failed to connect with code.py'
	ser.close()

try:
	while True:
		#conn.send(myo_command())
		lv, rv, dist = decode(int(ser.readline()))
		print lv, rv, dist
		#fuzzy_speed_calc(dist)
except KeyboardInterrupt:
	ser.close()
