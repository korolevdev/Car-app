#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
sys.path.insert(0, '../')
from GPIO_control import * 
from utils import check_int, decode
from cvcam import *
import threading
import serial

lv = 0
rv = 0
dist = 100

def on_arduino():
    global lv, rv, dist
    t = threading.currentThread()
    while getattr(t,'do_run', True):
        s = arduino.readline()
        if s and check_int(s):
            lv, rv, dist = decode(int(s))
            print 'arduino: ',lv,' ',rv,' ',dist

try:
    print 'Try to connect with Arduino'
    arduino = serial.Serial('/dev/arduino', 9600)
    arduino.readline()
    print 'Success'
except Exception, e:
    print 'Failed ',e

ar = threading.Event()
ca = threading.Event()
tar = threading.Thread(target=on_arduino, args=())
tca = threading.Thread(target=on_turn, args=())
tar.do_run = True
tca.do_run = True
tar.start()
tca.start()
ar.set()
ca.set()


#Pins:
'''
lb = 20
lr1 = 26
lr2 = 19
rb = 21 
rr1 = 13 
rr2 = 6
'''

def test1_motors():
    GPIO_setup()
    flb = GPIO.gpio_function(lb)
    frb = GPIO.gpio_function(rb)
    if (flb == GPIO.OUT and frb == GPIO.OUT):
        print("Test 1: OK")
    else:
        print("Test 1: FAILED")

def test2_motors():
    GPIO_setup()
    flr1 = GPIO.gpio_function(lr1)
    flr2 = GPIO.gpio_function(lr2)
    frr1 = GPIO.gpio_function(rr1)
    frr2 = GPIO.gpio_function(rr2)
    if (flr1 == GPIO.OUT and flr2 == GPIO.OUT and frr1 == GPIO.OUT and frr2 == GPIO.OUT):
        print("Test 2: OK")
    else:
        print("Test 2: FAILED")

def test3_motors():
    GPIO_setup()
    GPIO.output(lb, 0)
    GPIO.output(rb, 0)
    time.sleep(1)
    if (lv == 0 and rv == 0):
        print("Test 3: OK")
    else:
        print("Test 3: FAILED")
    stop()
    GPIO.cleanup()

def test4_motors():
    GPIO_setup()
    GPIO.output(lb, 1)
    GPIO.output(rb, 1)
    time.sleep(1)
    if (lv == 0 and rv == 0):
        print("Test 4: OK")
    else:
        print("Test 4: FAILED")
    stop()
    GPIO.cleanup()

def test5_motors():
    GPIO_setup()
    leftb = GPIO.PWM(lb, 50)
    rightb = GPIO.PWM(rb, 50)
    forward()
    leftb.start(0)
    rightb.start(0)
    res = 1
    speed = 0
    while speed < 10:
        leftb.ChangeDutyCycle(speed)
        rightb.ChangeDutyCycle(speed)
        time.sleep(0.5)
        if (lv > 0 and rv > 0):
            res = 0
        speed = speed + 2
    if res:
        print("Test 5: OK ")
    else:
        print("Test 5: FAILED")
    stop()
    GPIO.cleanup()

def test6_motors():
    GPIO_setup()
    leftb = GPIO.PWM(lb, 50)
    rightb = GPIO.PWM(rb, 50)
    forward()
    leftb.start(0)
    rightb.start(0)
    res = 0
    speed = 10
    while speed < 18:
        leftb.ChangeDutyCycle(speed)
        rightb.ChangeDutyCycle(speed)
        time.sleep(0.5)
        if (lv > 0 and rv > 0 and lv < 4 and rv < 4):
            res = 1
        speed = speed + 2
    if res:
        print("Test 6: OK ")
    else:
        print("Test 6: FAILED")
    stop()
    GPIO.cleanup()

def test7_motors():
    print("ATTENTION! HIGH SPEED!")
    i = 5
    while i >= 0:
        print(i)
        time.sleep(1)
        i = i - 1

    GPIO_setup()
    leftb = GPIO.PWM(lb, 50)
    rightb = GPIO.PWM(rb, 50)
    forward()
    leftb.start(0)
    rightb.start(0)
    res = 0
    start_time = time.time()
    while time.time() - start_time < 1.0:
        leftb.ChangeDutyCycle(40)
        rightb.ChangeDutyCycle(40)
        time.sleep(0.5)
        if (lv > 0 and rv > 0 and lv > 10 and rv > 10):
            res = 1
    if res:
        print("Test 8: OK ")
    else:
        print("Test 8: FAILED")       

    stop()
    GPIO.cleanup()

def test8_motors():
    print("ATTENTION! HIGH SPEED!")
    i = 5
    while i >= 0:
        print(i)
        time.sleep(1)
        i = i - 1

    GPIO_setup()
    leftb = GPIO.PWM(lb, 50)
    rightb = GPIO.PWM(rb, 50)
    backward()
    leftb.start(0)
    rightb.start(0)
    res = 0
    start_time = time.time()
    while time.time() - start_time < 1.0:
        leftb.ChangeDutyCycle(60)
        rightb.ChangeDutyCycle(60)
        time.sleep(0.5)
        if (lv > 0 and rv > 0 and lv > 10 and rv > 10):
            res = 1
    if res:
        print("Test 8: OK ")
    else:
        print("Test 8: FAILED")       

    stop()
    GPIO.cleanup()

 def test9_motors():
    print("ATTENTION! HIGHEST SPEED!")
    i = 5
    while i >= 0:
        print(i)
        time.sleep(1)
        i = i - 1

    GPIO_setup()
    leftb = GPIO.PWM(lb, 50)
    rightb = GPIO.PWM(rb, 50)
    forward()
    leftb.start(0)
    rightb.start(0)
    res = 0
    start_time = time.time()
    while time.time() - start_time < 1.0:
        leftb.ChangeDutyCycle(80)
        rightb.ChangeDutyCycle(80)
        time.sleep(0.5)
        if (lv > 0 and rv > 0 and lv > 20 and rv > 20):
            res = 1
    if res:
        print("Test 9: OK ")
    else:
        print("Test 9: FAILED")       

    stop()
    GPIO.cleanup()   

 def test10_motors():
    print("ATTENTION! HIGHEST SPEED!")
    i = 5
    while i >= 0:
        print(i)
        time.sleep(1)
        i = i - 1

    GPIO_setup()
    leftb = GPIO.PWM(lb, 50)
    rightb = GPIO.PWM(rb, 50)
    backward()
    leftb.start(0)
    rightb.start(0)
    res = 0
    start_time = time.time()
    while time.time() - start_time < 1.0:
        leftb.ChangeDutyCycle(100)
        rightb.ChangeDutyCycle(100)
        time.sleep(0.5)
        if (lv > 0 and rv > 0 and lv > 20 and rv > 20):
            res = 1
    if res:
        print("Test 10: OK ")
    else:
        print("Test 10: FAILED")       

    stop()
    GPIO.cleanup() 

 def test11_motors():
    GPIO_setup()
    leftb = GPIO.PWM(lb, 50)
    rightb = GPIO.PWM(rb, 50)
    left()
    leftb.start(0)
    rightb.start(0)
    res = 0
    start_time = time.time()
    while time.time() - start_time < 3.0:
        #leftb.ChangeDutyCycle(70)
        #rightb.ChangeDutyCycle(70)
        time.sleep(0.5)
        if (lv > 0 and rv > 0 and tca.turn > 0 and tca.turn == 3):
            res = 1
    if res:
        print("Test 11: OK ")
    else:
        print("Test 11: FAILED")       

    stop()
    GPIO.cleanup() 

def test_motors():
    print("ATTENTION! You must control carmyo when testing is running! ")
    print("Testing motors:")
    '''
    test1_motors()
    test2_motors()
    test3_motors()
    test4_motors()
    test5_motors()
    test6_motors()
    test7_motors()
    test8_motors()
    test9_motors()
    test10_motors()   
    '''
    test11_motors()
    tar.do_run = False
    tca.do_run = False

test_motors()