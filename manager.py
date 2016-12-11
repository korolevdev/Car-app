#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import socket
import serial
from utils import encode, decode
from myo_control import *
from fuzzy_logic import *
from GPIO_control import *

#get_android_commands(conn)
#fuser -vn tcp port
#sudo kill -9 27635

lv = 0
rv = 0
dist = 100
dest = 0
speed = 0
global myo_st
myo_st = 0

def motors_set(dest, speed):
    if dest in range(5):
        parse_command(dest)
    if (dest == 1):
        speed = speed*fuzzy_speed_calc(dist) 
    if speed in range(101):
        leftb.ChangeDutyCycle(speed)
        rightb.ChangeDutyCycle(speed)

def proc_imu(quat, acc, gyro, times=[]):
    global myo_st

    if myo_st == 1:
        q0, q1, q2, q3 = quat
        q0 = q0 / 16384.0
        q1 = q1 / 16384.0
        q2 = q2 / 16384.0
        q3 = q3 / 16384.0
        roll = math.atan2(2.0 * (q0 * q1 + q2 * q3), 1.0 - 2.0 * (q1 * q1 + q2 * q2))
        pitch = -math.asin(max(-1.0, min(1.0, 2.0 * (q0 * q2 - q3 * q1))))
        yaw = -math.atan2(2.0 * (q0 * q3 + q1 * q2), 1.0 - 2.0 * (q2 * q2 + q3 * q3))

        #speed of forward/backwad moving
        speed_d = int(abs(roll)/0.6 * 100)
        if (speed_d > 100):
            speed_d = 100
        if (speed_d < 20):
            speed_d = 20
        #speed of rotation
        speed_t = int(abs(pitch)/0.6 * 100)
        if (speed_t > 100):
            speed_t = 100
        if (speed_t < 40):
            speed_t = 40
         
        if (get_myo_turn(roll) == 5):
            com = get_myo_dest(pitch)
            speed = speed_d
        else:
            com = get_myo_turn(roll)
            speed = speed_t

        print (com,' ', speed)
        motors_set(com, speed)
        ## print framerate of received data
        times.append(time.time())
        if len(times) > 20:
            #print((len(times) - 1) / (times[-1] - times[0]))
            times.pop(0)     

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

def android_connect():
    sock = socket.socket()
    sock.bind(('', 9092))
    sock.listen(1)
    conn, addr = sock.accept()
    return conn

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

try:
    print 'Try to connect with android'
    android = android_connect()
except Exception, e:
    print 'Failed',e
    android.close()
    arduino.close()

try:
    print 'Try to connect with myo'
    myo = myo_connect()
except Exception, e:
    print 'Failed ',e
    android.close()
    arduino.close()     

def check_int(str):
    try:
        int(str)
        return True
    except:
        return False

def on_arduino():
    while 1:
        s = arduino.readline()
        if s and check_int(s):
            lv, rv, dist = decode(int(s))
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
        
ar = threading.Event()
my = threading.Event()


tar = threading.Thread(target=on_arduino, args=())
tmy = threading.Thread(target=on_myo, args=())

tar.start()
tmy.start()

ar.set()
my.set()

# join threads to the main thread
#tmy.join()
#ar.join()
#an.join()
try:
    while 1:
        data = android.recv(1024)  
        if data:
            dest, speed, myo_st = decode(int(data))
            if myo_st == 0:
                motors_set(dest, speed)
                print("android: ",dest, " ", speed," ", myo_st)
except KeyboardInterrupt:
    pass
finally:
    android.close()
    arduino.close()
    myo.disconnect()
