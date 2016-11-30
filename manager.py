#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyoConnect import * 
import socket
import serial
import fuzzy.storage.fcl.Reader
system = fuzzy.storage.fcl.Reader.Reader().load_from_file("fuzzy_data")

# preallocate input and output values
my_input = {
        "Distance" : 0.0,
        }
my_output = {
        "Speed_Correction" : 0.0
        }

#roll
#>0.15 hand left - ехать влево
#<0.15 hand right - ехать вправо
# 1 - up 2- down 3 - left 4 - right 0 - stop
#pitch
#>0.1 down - команда едем вперед
#<0.1 up - команда едем назад
#>1.2 stop - команда стоим стоит 

def encode(int dest, int speed) {
  return int(dest << 24) | int(speed << 16) | 0 & 0xffff;
}

def get_android_commands(connection):
	sock = socket.socket()
	sock.bind(('', 9092))

	while True:
		sock.listen(1)
		conn, addr = sock.accept()

		print 'connected:', addr

		data = conn.recv(1024)

		if data:
			connection.send(encode(data, 50))

		conn.close()

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

get_android_commands(conn)

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

def myo_command():
	myo.run()
	turn = myo.getRoll()
	dest = myo.getPitch()
	speed = abs(dest)/1.2 * 100
	dist, lv, rv = decode(int(ser.readline()))
	my_input["Distance"] = dist
	system.calculate(my_input, my_output)
	if (get_command_turn(turn) == 5):
		com = get_command_dest(dest)
	else
		com = get_command_turn(turn) 
	return encode(com, speed)
#ls /dev/tty*
ser = serial.Serial('/dev/ttyACM0', 9600)
print 'Arduino connected'

while True:

	conn.send(com)

conn.close()
