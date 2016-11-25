#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyoConnect import * 
import socket
import serial

#roll
#>0.15 hand left - ехать влево
#<0.15 hand right - ехать вправо

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

sock = socket.socket()
sock.bind(('', 9093))
sock.listen(1)
conn, addr = sock.accept()

print 'connected:', addr

myo = Myo(sys.argv[1] if len(sys.argv) >= 2 else None)
myo.connect()
while (not myo.getGyro()):
	print('Wait a myo')
	myo.run()

print 'Myo connected'


def decode(packet):
    lv = packet >> 24
    rv = (packet >> 16) & 0xff
    dist = packet & 0xffff

    if dist & 0x8000:
        dist = dist - 0x10000
    return dist, lv, rv

#ls /dev/tty*
ser = serial.Serial('/dev/ttyACM0', 9600)
print 'Arduino connected'

def get_distance():
	return {
				int(ser.readline())
   	}[True]

while True:
	myo.run()
	turn = myo.getRoll()
	dest = myo.getPitch()
	command = 't' + str(get_command_turn(turn)) + 'd' + str(get_command_dest(dest))	
	dist, lv, rv = decode(int(ser.readline()))
	print(command)
	conn.send(command)

conn.close()
