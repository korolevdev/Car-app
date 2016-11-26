import RPi.GPIO as GPIO
import time
import socket

GPIO.setmode(GPIO.BCM)

lb = 6
rb = 19 
rr = 26
lr = 13

GPIO.setup(lb, GPIO.OUT, initial = 0)
GPIO.setup(rb, GPIO.OUT, initial = 0)
GPIO.setup(rr, GPIO.OUT, initial = 0)
GPIO.setup(lr, GPIO.OUT, initial = 0)

GPIO.output(rr, 1)
GPIO.output(lr, 0)

left = GPIO.PWM(lb, 100)
right = GPIO.PWM(rb, 100)

left.start(0)
right.start(0)

while 1:
	left.ChangeDutyCycle(100)
	right.ChangeDutyCycle(100)
	time.sleep(50)


left.stop()
right.stop()
GPIO.cleanup()

#sock = socket.socket()
#sock.connect(('localhost', 9093))

#while 1:
	#data = sock.recv(1024)
	#print data	

#sock.close()

