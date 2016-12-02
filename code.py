from GPIO_config.py import * 
import time
import socket

GPIO_setup()

leftb = GPIO.PWM(lb, 50)
rightb = GPIO.PWM(rb, 50)

leftb.start(0)
rightb.start(0)

def decode(packet):
    dest = packet >> 24
    speed = (packet >> 16) & 0xff
    return dest, speed

def set_speed(speed):
	leftb.ChangeDutyCycle(speed)
	rightb.ChangeDutyCycle(speed)

def parse_command(com):
	if com == 0:
		stop()
	elif com == 1:
		forward()
	elif com == 2:
		backward()
	elif com == 3:
		left()
	elif com == 4:
		right()

sock = socket.socket()
sock.connect(('localhost', 9093))

while 1:
	data = sock.recv(1024)
	dest, speed = decode(int(data))
	parse_command(dest)
	set_speed(speed)
	time.sleep(0.1)

left.stop()
right.stop()
GPIO.cleanup()
