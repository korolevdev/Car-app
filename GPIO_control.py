#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from fuzzy_logic import *

lb = 20
lr1 = 26
lr2 = 19

rb = 21 
rr1 = 13 
rr2 = 6

def GPIO_setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(lb, GPIO.OUT, initial = 0)
	GPIO.setup(rb, GPIO.OUT, initial = 0)
	GPIO.setup(rr1, GPIO.OUT, initial = 0)
	GPIO.setup(rr2, GPIO.OUT, initial = 0)
	GPIO.setup(lr1, GPIO.OUT, initial = 0)
	GPIO.setup(lr2, GPIO.OUT, initial = 0)

def stop():
	GPIO.output(rr1, 1)
	GPIO.output(rr2, 1)
	GPIO.output(lr1, 1)
	GPIO.output(lr2, 1)

def left():
	GPIO.output(rr1, 1)
	GPIO.output(rr2, 0)
	GPIO.output(lr1, 0)
	GPIO.output(lr2, 1)

def right():
	GPIO.output(rr1, 0)
	GPIO.output(rr2, 1)
	GPIO.output(lr1, 1)
	GPIO.output(lr2, 0)

def forward():
	GPIO.output(rr1, 0)
	GPIO.output(rr2, 1)
	GPIO.output(lr1, 0)
	GPIO.output(lr2, 1)	

def backward():
	GPIO.output(rr1, 1)
	GPIO.output(rr2, 0)
	GPIO.output(lr1, 1)
	GPIO.output(lr2, 0)

def parse_command(com):
	if com  ==  0:
		stop()
	elif com  ==  1:
		forward()
	elif com  ==  2:
		backward()
	elif com  ==  3:
		left()
	elif com  ==  4:
		right()

def motors_set(dest, speed, dist, leftb, rightb):
	if dest in range(5):
		parse_command(dest)
	if (dest == 1):
		speed = int(speed*fuzzy_speed_calc(dist)) 
	print dest, ' ',speed, ' ', dist
	if speed in range(101):
			leftb.ChangeDutyCycle(speed)
			rightb.ChangeDutyCycle(speed)