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

left = GPIO.PWM(lb, 50)
right = GPIO.PWM(rb, 50)

left.start(0)
right.start(0)

left.ChangeDutyCycle(100)
right.ChangeDutyCycle(100)

def decode(packet):
    dest = packet >> 24
    speed = (packet >> 16) & 0xff
    return dest, speed

def forward():
	GPIO.output(rr1, 1)
	GPIO.output(rr2, 0)
	GPIO.output(lr1, 0)
	GPIO.output(lr2, 1)

def backward():
	GPIO.output(rr1, 1)
	GPIO.output(rr2, 0)
	GPIO.output(lr1, 0)
	GPIO.output(lr2, 1)	

def left():
	GPIO.output(rr1, 1)
	GPIO.output(rr2, 0)
	GPIO.output(lr1, 1)	
	GPIO.output(lr2, 0)

def right():
	GPIO.output(rr1, 0)
	GPIO.output(rr2, 1)
	GPIO.output(lr1, 0)
	GPIO.output(lr2, 1)

def parse_command(com):
    return {
		com == 1:
			forward(),
		com == 2:
			backward(),
		com == 3:
			left(),
		com == 4:
			right(),
    }[True]

#sock = socket.socket()
#sock.connect(('localhost', 9093))

while 1:
	#parse_command(1)
	#forward()
	left.ChangeDutyCycle(100)
	right.ChangeDutyCycle(100)
	print '1'
	GPIO.output(rr1, 0)
	GPIO.output(rr2, 1)
	GPIO.output(lr1, 0)
	GPIO.output(lr2, 1)
	time.sleep(0.1)

sock.close()
left.stop()
right.stop()
GPIO.cleanup()