#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

lb=20
lr1=26; lr2=19
rb=21 
rr1=13; rr2=6

def GPIO_setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(lb, GPIO.OUT, initial=0)
	GPIO.setup(rb, GPIO.OUT, initial=0)
	GPIO.setup(rr1, GPIO.OUT, initial=0)
	GPIO.setup(rr2, GPIO.OUT, initial=0)
	GPIO.setup(lr1, GPIO.OUT, initial=0)
	GPIO.setup(lr2, GPIO.OUT, initial=0)

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