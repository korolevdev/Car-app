#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from myo_raw import *
import math
import time 

#roll
#>0.15 hand left - ехать влево
#<0.15 hand right - ехать вправо
# 1 - up 2- down 3 - left 4 - right 0 - stop
#pitch
#>0.1 down - команда едем вперед
#<0.1 up - команда едем назад
#>1.2 stop - команда стоим стоит 

def get_myo_dest(tmp):
    return {
                 tmp < 0:    2,
          0   <= tmp < 0.2:  0,
          0.2 <= tmp:        1
    }[True]

def get_myo_turn(tmp):
    return {
                tmp < -0.4: 4,
        -0.4 <= tmp < 0.4:  5,
         0.4 <= tmp:        3
    }[True]

def get_pitch(quat):
    q0, q1, q2, q3 = quat
    q0 = q0 / 16384.0
    q1 = q1 / 16384.0
    q2 = q2 / 16384.0
    q3 = q3 / 16384.0
    return -math.asin(max(-1.0, min(1.0, 2.0 * (q0 * q2 - q3 * q1))))

def get_roll(quat):
    q0, q1, q2, q3 = quat
    q0 = q0 / 16384.0
    q1 = q1 / 16384.0
    q2 = q2 / 16384.0
    q3 = q3 / 16384.0
    return math.atan2(2.0 * (q0 * q1 + q2 * q3), 1.0 - 2.0 * (q1 * q1 + q2 * q2))

def speed_setting(action, min, max):
    speed = int(abs(action)/0.6 * 100)
    if (speed > max):
        speed = max
    if (speed < min):
        speed = min
    return speed