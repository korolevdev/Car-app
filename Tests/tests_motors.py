#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '../')
from manager import *

ar = threading.Event()
tar = threading.Thread(target=on_arduino, args=())
tar.start()
ar.set()

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
        print("Destination control is activated | OK")
    else:
        print("Destination control is activated | FAILED")

def test2_motors():
    GPIO_setup()
    flr1 = GPIO.gpio_function(lr1)
    flr2 = GPIO.gpio_function(lr2)
    frr1 = GPIO.gpio_function(rr1)
    frr2 = GPIO.gpio_function(rr2)
    if (flr1 == GPIO.OUT and flr2 == GPIO.OUT and frr1 == GPIO.OUT and frr2 == GPIO.OUT):
        print("Turn control is activated | OK")
    else:
        print("Turn control is activated | FAILED")

def test3_motors():
    GPIO_setup()
    GPIO.output(lb, 1)
    GPIO.output(rb, 1)
    stop()
    if (lv == 0 and rv == 0):
        print("Motors is stopped | OK")
    else:
        print("Motors is stopped | FAILED")
    stop()
    GPIO.cleanup()

#May be add a data from URM37?
def test4_motors():
    GPIO_setup()
    GPIO.output(lb, 1)
    GPIO.output(rb, 1)
    forward()
    time.sleep(1.5)
    if (lv > 0 and rv > 0):
        print("Motors is running | OK")
    else:
        print("Motors is running | FAILED")
    stop()
    GPIO.cleanup()

def test5_motors():
    GPIO_setup()
    GPIO.output(lb, 1)
    GPIO.output(rb, 1)
    backward()
    time.sleep(1.5)
    if (lv > 0 and rv > 0):
        print("Motors is running | OK")
    else:
        print("Motors is running | FAILED")
    stop()
    GPIO.cleanup()

def test6_motors():
    GPIO_setup()
    GPIO.output(lb, 1)
    GPIO.output(rb, 1)
    left()
    time.sleep(1.5)
    #Here will be a opencv data about side of turn
    if (lv > 0 and rv > 0):
        print("Motors is running | OK")
    else:
        print("Motors is running | FAILED")        
    stop()
    GPIO.cleanup()

def test7_motors():
    GPIO_setup()
    GPIO.output(lb, 1)
    GPIO.output(rb, 1)
    right()
    time.sleep(1.5)
    #Here will be a opencv data about side of turn
    if (lv > 0 and rv > 0):
        print("Motors is running | OK")
    else:
        print("Motors is running | FAILED")
    stop()
    GPIO.cleanup()

def test8_motors():
    GPIO_setup()
    GPIO.output(lb, 1)
    GPIO.output(rb, 1)
    parse_command(0)
    time.sleep(1)
    if (lv == 0 and rv == 0):
        print("Motors is stopped | OK")
    else:
        print("Motors is stopped | FAILED")        
    stop()
    GPIO.cleanup()

def test9_motors():
    GPIO_setup()
    GPIO.output(lb, 1)
    GPIO.output(rb, 1)
    parse_command(1)
    time.sleep(1.5)
    if (lv > 0 and rv > 0):
        print("Motors is running | OK")
    else:
        print("Motors is running | FAILED") 
    stop()
    GPIO.cleanup()

def test10_motors():
    GPIO_setup()
    GPIO.output(lb, 1)
    GPIO.output(rb, 1)
    parse_command(2)
    time.sleep(1.5)
    if (lv > 0 and rv > 0):
        print("Motors is running | OK")
    else:
        print("Motors is running | FAILED") 
    stop()
    GPIO.cleanup()

def test11_motors():
    GPIO_setup()
    GPIO.output(lb, 1)
    GPIO.output(rb, 1)
    parse_command(3)
    time.sleep(1.5)
    if (lv > 0 and rv > 0):
        print("Motors is running | OK")
    else:
        print("Motors is running | FAILED") 
    stop()
    GPIO.cleanup()

def test12_motors():
    GPIO_setup()
    GPIO.output(lb, 1)
    GPIO.output(rb, 1)
    parse_command(1)
    time.sleep(1.5)
    if (lv > 0 and rv > 0):
        print("Motors is running | OK")
    else:
        print("Motors is running | FAILED") 
    stop()
    GPIO.cleanup()

def test13_motors():
    GPIO_setup()
    leftb = GPIO.PWM(lb, 50)
    rightb = GPIO.PWM(rb, 50)
    leftb.start(0)
    rightb.start(0)

    leftb.ChangeDutyCycle(0)
    rightb.ChangeDutyCycle(0)

    time.sleep(1.5)
    if (lv == 0 and rv == 0):
        print("Motors is stopped | OK")
    else:
        print("Motors is stopped | FAILED") 
    stop()
    GPIO.cleanup()

def test14_motors():
    GPIO_setup()
    leftb = GPIO.PWM(lb, 50)
    rightb = GPIO.PWM(rb, 50)
    leftb.start(0)
    rightb.start(0)

    leftb.ChangeDutyCycle(25)
    rightb.ChangeDutyCycle(25)

    time.sleep(1.5)
    #CHANGE!!! ORGANIZE REAL TEST!!!
    if (lv > 10 and rv > 10):
        print("Motors is running | OK")
    else:
        print("Motors is running | FAILED") 
    stop()
    GPIO.cleanup()

def test15_motors():
    GPIO_setup()
    leftb = GPIO.PWM(lb, 50)
    rightb = GPIO.PWM(rb, 50)
    leftb.start(0)
    rightb.start(0)

    leftb.ChangeDutyCycle(50)
    rightb.ChangeDutyCycle(50)

    time.sleep(1.5)
    #CHANGE!!! ORGANIZE REAL TEST!!!
    if (lv > 20 and rv > 20):
        print("Motors is running | OK")
    else:
        print("Motors is running | FAILED") 
    stop()
    GPIO.cleanup()

def test16_motors():
    GPIO_setup()
    leftb = GPIO.PWM(lb, 50)
    rightb = GPIO.PWM(rb, 50)
    leftb.start(0)
    rightb.start(0)

    leftb.ChangeDutyCycle(75)
    rightb.ChangeDutyCycle(75)

    time.sleep(1.5)
    #CHANGE!!! ORGANIZE REAL TEST!!!
    if (lv > 30 and rv > 30):
        print("Motors is running | OK")
    else:
        print("Motors is running | FAILED") 
    stop()
    GPIO.cleanup()

def test17_motors():
    GPIO_setup()
    leftb = GPIO.PWM(lb, 50)
    rightb = GPIO.PWM(rb, 50)
    leftb.start(0)
    rightb.start(0)

    leftb.ChangeDutyCycle(100)
    rightb.ChangeDutyCycle(100)

    time.sleep(1.5)
    #CHANGE!!! ORGANIZE REAL TEST!!!
    if (lv > 50 and rv > 50):
        print("Motors is running | OK")
    else:
        print("Motors is running | FAILED") 
    stop()
    GPIO.cleanup()

def test18_motors():
    GPIO_setup()
    leftb = GPIO.PWM(lb, 50)
    rightb = GPIO.PWM(rb, 50)
    leftb.start(0)
    rightb.start(0)

    motors_set(0, 0)
    time.sleep(1.5)
    #CHANGE!!! ORGANIZE REAL TEST!!!
    if (lv == 0 and rv == 0):
        print("Motors is stopped | OK")
    else:
        print("Motors is stopped | FAILED") 
    stop()
    GPIO.cleanup()

def test19_motors():
    GPIO_setup()
    leftb = GPIO.PWM(lb, 50)
    rightb = GPIO.PWM(rb, 50)
    leftb.start(0)
    rightb.start(0)

    motors_set(0, 50)
    time.sleep(1.5)
    #CHANGE!!! ORGANIZE REAL TEST!!!
    if (lv == 0 and rv == 0):
        print("Motors is stopped | OK")
    else:
        print("Motors is stopped | FAILED") 
    stop()
    GPIO.cleanup()

def test18_motors():
    GPIO_setup()
    leftb = GPIO.PWM(lb, 50)
    rightb = GPIO.PWM(rb, 50)
    leftb.start(0)
    rightb.start(0)

    motors_set(0, 100)
    time.sleep(1.5)
    #CHANGE!!! ORGANIZE REAL TEST!!!
    if (lv == 0 and rv == 0):
        print("Motors is stopped | OK")
    else:
        print("Motors is stopped | FAILED") 
    stop()
    GPIO.cleanup()

def test19_motors():
    GPIO_setup()
    leftb = GPIO.PWM(lb, 50)
    rightb = GPIO.PWM(rb, 50)
    leftb.start(0)
    rightb.start(0)

    motors_set(1, 50)
    time.sleep(1.5)
    #CHANGE!!! ORGANIZE REAL TEST!!! AND ADD A DATA FROM CAMERA!
    if (lv > 10 and rv > 10):
        print("Motors is running | OK")
    else:
        print("Motors is running | FAILED") 
    stop()
    GPIO.cleanup()

def test20_motors():
    GPIO_setup()
    leftb = GPIO.PWM(lb, 50)
    rightb = GPIO.PWM(rb, 50)
    leftb.start(0)
    rightb.start(0)

    motors_set(2, 50)
    time.sleep(1.5)
    #CHANGE!!! ORGANIZE REAL TEST!!! AND ADD A DATA FROM CAMERA!
    if (lv > 10 and rv > 10):
        print("Motors is running | OK")
    else:
        print("Motors is running | FAILED") 
    stop()
    GPIO.cleanup()

def test21_motors():
    GPIO_setup()
    leftb = GPIO.PWM(lb, 50)
    rightb = GPIO.PWM(rb, 50)
    leftb.start(0)
    rightb.start(0)

    motors_set(3, 50)
    time.sleep(1.5)
    #CHANGE!!! ORGANIZE REAL TEST!!! AND ADD A DATA FROM CAMERA!
    if (lv > 10 and rv > 10):
        print("Motors is running | OK")
    else:
        print("Motors is running | FAILED") 
    stop()
    GPIO.cleanup()

def test22_motors():
    GPIO_setup()
    leftb = GPIO.PWM(lb, 50)
    rightb = GPIO.PWM(rb, 50)
    leftb.start(0)
    rightb.start(0)

    motors_set(4, 50)
    time.sleep(1.5)
    #CHANGE!!! ORGANIZE REAL TEST!!! AND ADD A DATA FROM CAMERA!
    if (lv > 10 and rv > 10):
        print("Motors is running | OK")
    else:
        print("Motors is running | FAILED") 
    stop()
    GPIO.cleanup()

def test_motors():
    print("ATTENTION! You must control carmyo when testing is running! ")
    print("Testing motors:")
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
    test11_motors()
    test12_motors()
    test13_motors()
    test14_motors()
    test15_motors()
    test16_motors()
    test17_motors()
    test18_motors()
    test19_motors()
    test20_motors()
    test21_motors()
    test22_motors()

test_motors()
