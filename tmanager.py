#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
from protocol import encode,decode
from myo_control import *
from fuzzy_logic import *
from GPIO_control import *
import socket
import serial
import time

#get_android_commands(conn)
#fuser -vn tcp port
#sudo kill -9 27635

def motors_connect():
    sock = socket.socket()
    sock.bind(('', 9093))
    sock.listen(1)
    conn, addr = sock.accept()
    return conn

def android_connect():
    sock = socket.socket()
    sock.bind(('', 9092))
    sock.listen(1)
    conn, addr = sock.accept()
    #conn.setblocking(0)
    return conn

def myo_connect():
    myo = Myo(sys.argv[1] if len(sys.argv) >= 2 else None)
    myo.connect()
    while (not myo.getGyro()):
        print('Wait a myo')
        myo.run()
    return myo

try:
    print 'Try to connect with Arduino'
    arduino = serial.Serial('/dev/arduino', 9600)
    arduino.readline()
    print 'Success'
except Exception, e:
    print 'Failed to connect with Arduino'


try:
    print 'Try to setup motors'
    GPIO_setup()

    leftb = GPIO.PWM(lb, 50)
    rightb = GPIO.PWM(rb, 50)

    leftb.start(0)
    rightb.start(0)
    print 'Success'
except Exception, e:
    print 'Failed to setup motors',e
    #arduino.close()

try:
    print 'Try to connect with myo'
    myo = myo_connect()
except Exception, e:
    print 'Failed to connect with android',e
    #arduino.close()    

try:
    print 'Try to connect with android'
    android = android_connect()
except Exception, e:
    print 'Failed to connect with android',e
    #arduino.close()    

def check_int(str):
    try:
        int(str)
        return True
    except:
        return False

lv = 0
rv = 0
dist = 100
dest = 0
speed = 0
myo_st = 1

def arduino_read(n, event_for_wait, event_for_set):
    #event_for_wait.wait() # wait for event
    #event_for_wait.clear() # clean event for future
    while 1:
        s = arduino.readline()
        if s and check_int(s):
            lv, rv, dist = decode(int(s))
            print 'arduino: ',lv,' ',rv,' ',dist
    #event_for_set.set() # set event for neighbor thread

def android_read(n, event_for_wait, event_for_set):
    #event_for_wait.wait() # wait for event
    #event_for_wait.clear() # clean event for future    
    while 1:  
        do_read = False 
	try: 
	    r, _, _ = select.select([android], [], []) 
            do_read = bool(r) 
        except socket.error: 
            pass 
        if do_read: 
            data = adnroid.recv(1024) 
            print "Got data: ", data 
            #android.settimeout(0)
            #data = android.recv(8)       
            if data:
                data = data.strip('\0')
                dest, speed, myo_st = decode(long(data))
                print 'android: ',dest,' ',speed,' ',myo_st
     #event_for_set.set() # set event for neighbor thread
        
# init events
#my = threading.Event()
#ar = threading.Event()
an = threading.Event()


# init threads
#tmy = threading.Thread(target=myo_read, args=(0, my, ar))
#tar = threading.Thread(target=arduino_read, args=(1, ar, ar))
tan = threading.Thread(target=android_read, args=(0, an, an))

# start threads
#tmy.start()
#tar.start()
tan.start()

#an.set() # initiate the first event
#ar.set()
an.set()
# join threads to the main thread
#tmy.join()
#ar.join()
#an.join()

while 1:
    #if myo_st:
    try:
        dest, speed = myo_command(myo)
        print 'myo: ',dest,' ',speed
    except:
        True
        print 'bad'
    #print '1'
'''
    if dest in range(5):
        parse_command(dest)
    if (dest == 1):
        speed = speed*fuzzy_speed_calc(dist) 
    if speed in range(101):
        leftb.ChangeDutyCycle(speed)
        rightb.ChangeDutyCycle(speed)
'''
