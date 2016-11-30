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

def decode(packet):
    dest = packet >> 24
    speed = (packet >> 16) & 0xff
    return dest, speed

def parse_command(com):
    return {
    	com == 1: #вперед
    		GPIO.output(rr1, 0)
			GPIO.output(rr2, 1)
			GPIO.output(lr1, 1)	
			GPIO.output(lr2, 0),
        com == 2: #назад
        	GPIO.output(rr1, 1)
			GPIO.output(rr2, 0)
			GPIO.output(lr1, 0)	
			GPIO.output(lr2, 1),
        com == 3: #влево
        	GPIO.output(rr1, 1)
			GPIO.output(rr2, 0)
			GPIO.output(lr1, 1)	
			GPIO.output(lr2, 0),
		com == 4: #вправо
			GPIO.output(rr1, 0)
			GPIO.output(rr2, 1)
			GPIO.output(lr1, 0)	
			GPIO.output(lr2, 1)    
    }[True]

sock = socket.socket()
sock.connect(('localhost', 9093))

while 1:
	data = sock.recv(1024)
	if data:
		dest, speed = decode(data)
		parse_command(data)
		left.ChangeDutyCycle(speed)
		right.ChangeDutyCycle(speed)

	time.sleep(0.1)

sock.close()
left.stop()
right.stop()
GPIO.cleanup()