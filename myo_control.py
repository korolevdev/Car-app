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
               tmp < -0.2: 2,
          -0.2 <= tmp < 0.2:  0,
          0.2 <= tmp:       1
    }[True]

def get_command_turn(tmp):
    return {
               tmp < -0.3: 4,
	-0.3 <= tmp < 0.3:  5,
         0.3 <= tmp:       3
    }[True]

def myo_command(myo):
	myo.run()
	turn = myo.getRoll()
	dest = myo.getPitch()
	speed = abs(dest)/1.2 * 100
	
	if (get_command_turn(turn) == 5):
		com = get_command_dest(dest)
	else:
		com = get_command_turn(turn) 
	return com, speed