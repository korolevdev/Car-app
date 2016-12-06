#!/usr/bin/env python
# -*- coding: utf-8 -*-

from GPIO_control import *
from protocol import decode 
import time
import socket

GPIO_setup()

leftb = GPIO.PWM(lb, 50)
rightb = GPIO.PWM(rb, 50)

leftb.start(0)
rightb.start(0)

def set_speed(speed):
	leftb.ChangeDutyCycle(speed)
	rightb.ChangeDutyCycle(speed)

def parse_command(com):
	if com == 0:
		stop()
	elif com == 1:
		forward()
	elif com == 2:
		backward()
	elif com == 3:
		left()
	elif com == 4:
		right()

try:
	sock = socket.socket()
	sock.connect(('localhost', 9093))
except Exception, e:
	print 'Failed to create socket connection'
	sock.close()

try:
	while 1:
		data = sock.recv(1024)
		dest, speed = decode(int(data))
		print dest, speed
		#parse_command(dest)
		#set_speed(speed)
		time.sleep(0.1)
except Exception, KeyboardInterrupt:
	sock.close()
	leftb.stop()
	rightb.stop()
	GPIO.cleanup()
