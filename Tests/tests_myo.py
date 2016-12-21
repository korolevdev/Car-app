# some_file.py
import sys
sys.path.insert(0, '../')
from myo_control import *
from manager import myo_connect

#TODO borders

def test1_myo():
	myo = myo_connect()
	print("Connection|OK")
	myo.disconnect()

myo = myo_connect()

def test2_myo():
	while True:	
		myo.run()
		turn = get_roll()
		if (get_myo_turn(turn) == 3):
			print("Turned left|OK")
			break
def test3_myo():
	while True:	
		myo.run()
		turn = get_roll()
		if (get_myo_turn(turn) == 5):
			print("Toward|OK")
			break
def test4_myo():
	while True:	
		myo.run()
		turn = get_roll()
		if (get_myo_turn(turn) == 4):
			print("Turned right|OK")
			break

def test5_myo():
	while True:	
		myo.run()
		dest = get_pitch()
		if (get_myo_dest(dest) == 1):
			print("Forward|OK")
			break
def test6_myo():
	while True:	
		myo.run()
		dest = get_pitch()
		if (get_myo_dest(dest) == 0):
			print("Stop|OK")
			break

def test7_myo():
	while True:	
		myo.run()
		dest = get_pitch()
		if (get_myo_dest(dest) == 2):
			print("Backward|OK")
			break

def test_myo():
	print("Testing myo:")
	print("Waiting connection:")	
	test1_myo()
	print ("Waiting left:")
	test2_myo()
	print ("Waiting toward:")
	test3_myo()
	print ("Waiting right:")
	test4_myo()
	print ("Waiting forward:")
	test5_myo()
	print ("Waiting stop:")
	test6_myo()
	print ("Waiting backward:")
	test7_myo()

test_myo()
