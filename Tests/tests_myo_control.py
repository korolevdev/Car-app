# some_file.py
import sys
sys.path.insert(0, '../')
from myo_control import *

#TODO borders

def test1_get_command_dest():
	tmp = -0.4
	comm = get_command_dest(tmp)
	if (comm == 2):
		print("Backward|OK")
	else:
		print("Backward|FAIL")


def test2_get_command_dest():
	tmp = 0.1
	comm = get_command_dest(tmp)
	if (comm == 0):
		print("Stop|OK")
	else:
		print("Stop|FAIL")

def test3_get_command_dest():
	tmp = 0.6
	comm = get_command_dest(tmp)
	if (comm == 1):
		print("Forward|OK")
	else:
		print("Forward|FAIL")

def test4_get_command_dest():
	tmp = 0
	comm = get_command_dest(tmp)
	if (comm == 0):
		print("STOP|OK")
	else:
		print("STOP|FAIL")

def test5_get_command_dest():
	tmp = 0.2
	comm = get_command_dest(tmp)
	if (comm == 1):
		print("Forward|OK")
	else:
		print("Forward|FAIL")


def test1_get_command_turn():
	tmp = -0.5
	comm = get_command_turn(tmp)
	if (comm == 3):
		print("Left|OK")
	else:
		print("Left|FAIL")

def test2_get_command_turn():
	tmp = 0
	comm = get_command_turn(tmp)
	if (comm == 5):
		print("Toward|OK")
	else:
		print("Toward|FAIL")

def test3_get_command_turn():
	tmp = 0.5
	comm = get_command_turn(tmp)
	if (comm == 4):
		print("Right|OK")
	else:
		print("Right|FAIL")

def test4_get_command_turn():
	tmp = -0.4
	comm = get_command_turn(tmp)
	if (comm == 4):
		print("Right|OK")
	else:
		print("Right|FAIL")

def test5_get_command_turn():
	tmp = 0.4
	comm = get_command_turn(tmp)
	if (comm == 5):
		print("Toward|OK")
	else:
		print("Toward|FAIL")

def test_myo_control():
	print ("Testing get_command_dest:")
	test1_get_command_dest()
	test2_get_command_dest()
	test3_get_command_dest()
	test4_get_command_dest()
	test5_get_command_dest()
	print ("Testing get_command_turn:")
	test1_get_command_turn()
	test2_get_command_turn()
	test3_get_command_turn()
	test4_get_command_turn()
	test5_get_command_turn()
	
test_myo_control()
