import sys
sys.path.insert(0, '../')
from myo_raw import *
from myo_control import *

flags = [1, 0, 0, 0, 0, 0]

def proc_imu(quat, acc, gyro, times=[]):
	roll = get_roll(quat)
	pitch = get_pitch(quat)
	if flags[0] == 1:
		test2_myo(roll,pitch)
	if flags[1] == 1:
		test3_myo(roll,pitch)
	if flags[2] == 1:
		test4_myo(roll,pitch)
	if flags[3] == 1:
		test5_myo(roll,pitch)
	if flags[4] == 1:
		test6_myo(roll,pitch)
	if flags[5] == 1:
		test7_myo(roll,pitch)
	if flags == 0:
		print("TESTS OK")


def test1_myo():
	myo = MyoRaw(sys.argv[1] if len(sys.argv) >= 2 else None)
	myo.connect()
	myo.add_imu_handler(proc_imu)
	print("Connection|OK")
	return myo

def test2_myo(roll,pitch):	
	if (get_myo_turn(roll) == 3):
		print("Turn left|OK")
		flags[0] = 0
		flags[1] = 1
		

def test3_myo(roll,pitch):
	if (get_myo_turn(roll) == 5):
		print("Toward|OK")
		flags[1] = 0
		flags[2] = 1
		
def test4_myo(roll,pitch):
	if (get_myo_turn(roll) == 4):
		print("Turn right|OK")
		flags[2] = 0
		flags[3] = 1

def test5_myo(roll,pitch):
	if (get_myo_dest(pitch) == 1):
		print("Forward|OK")
		flags[3] = 0
		flags[4] = 1

def test6_myo(roll,pitch):
	if (get_myo_dest(pitch) == 0):
		print("Stop|OK")
		flags[4] = 0
		flags[5] = 1
		

def test7_myo(roll,pitch):
	if (get_myo_dest(pitch) == 2):
		print("Backward|OK")
		flags[5] = 0

try:
	print("Waiting connection")
	myo = test1_myo()
	while True:
		myo.run(1) 
except KeyboardInterrupt:
	pass
		

