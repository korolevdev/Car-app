#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyoConnect import * 

#roll
#>0.15 hand left - ехать влево
#<0.15 hand right - ехать вправо
# 1 - up 2- down 3 - left 4 - right 0 - stop
#pitch
#>0.1 down - команда едем вперед
#<0.1 up - команда едем назад
#>1.2 stop - команда стоим стоит 

def get_command_dest(tmp):
    return {
               tmp < 0: 2,
          0 <= tmp < 0.2:  0,
          0.2 <= tmp:       1
    }[True]

def get_command_turn(tmp):
    return {
               tmp < -0.4: 4,
	-0.4 <= tmp < 0.4:  5,
         0.4 <= tmp:       3
    }[True]

def myo_command(myo):
    myo.run()
    myo.tick()
    turn = myo.getRoll()
    dest = myo.getPitch()
    #speed of forward/backwad moving
    speed_d = int(abs(dest)/0.6 * 100)
    if (speed_d > 100):
        speed_d = 100
    if (speed_d < 20):
        speed_d = 20
    #speed of rotation
    speed_t = int(abs(turn)/0.6 * 100)
    if (speed_t > 100):
        speed_t = 100
    if (speed_t < 40):
        speed_t = 40
    
    if (get_command_turn(turn) == 5):
        com = get_command_dest(dest)
        speed = speed_d
    else:
        com = get_command_turn(turn)
        speed = speed_t
    return com, speed
