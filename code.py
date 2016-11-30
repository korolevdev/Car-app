import RPi.GPIO as GPIO
import time
import socket

GPIO.setmode(GPIO.BCM)

lb=20 ; rb=21 ; 
rr1=13 ; rr2=6;
lr1=26; lr2=19;

GPIO.setup(lb, GPIO.OUT, initial=0)
GPIO.setup(rb, GPIO.OUT, initial=0)
GPIO.setup(rr1, GPIO.OUT, initial=0)
GPIO.setup(rr2, GPIO.OUT, initial=0)
GPIO.setup(lr1, GPIO.OUT, initial=0)
GPIO.setup(lr2, GPIO.OUT, initial=0)

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
	if com == 1:
		forward()
	elif com == 2:
		backward()
	elif com == 3:
		left()
	elif com == 4:
		right()

def left():
	GPIO.output(rr1, 1)
	GPIO.output(rr2, 0)
	GPIO.output(lr1, 0)
	GPIO.output(lr2, 1)

def right():
	GPIO.output(rr1, 0)
	GPIO.output(rr2, 1)
	GPIO.output(lr1, 1)
	GPIO.output(lr2, 0)

def forward():
	GPIO.output(rr1, 0)
	GPIO.output(rr2, 1)
	GPIO.output(lr1, 0)
	GPIO.output(lr2, 1)	

def backward():
	GPIO.output(rr1, 1)
	GPIO.output(rr2, 0)
	GPIO.output(lr1, 1)
	GPIO.output(lr2, 0)

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
