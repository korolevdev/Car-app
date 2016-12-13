# some_file.py
import sys
sys.path.insert(0, '../')
from fuzzy_logic import *

def test1_fuzzy():
	print 'Car is very far'
	arr = [170, 200, 240, 360, 400]
	for i in range(len(arr)):
		if (0.90 <= fuzzy_speed_calc(arr[i]) <= 1):
			print 'OK'
		else:
			print fuzzy_speed_calc(arr[i])

def test2_fuzzy():
	print 'Car is far'
	arr = [90, 120, 130, 160]
	for i in range(len(arr)):
		if (0.65 <= fuzzy_speed_calc(arr[i]) <= 0.90):
			print 'OK'
		else:
			print fuzzy_speed_calc(arr[i])

def test3_fuzzy():
	print 'Medium distance'
	arr = [40, 60, 70, 80, 85]
	for i in range(len(arr)):
		if (0.35 <= fuzzy_speed_calc(arr[i]) <= 0.65):
			print 'OK'
		else:
			print fuzzy_speed_calc(arr[i])

def test4_fuzzy():
	print 'Car is close'
	arr = [10, 20, 25, 35, 40]
	for i in range(len(arr)):
		if (0.1 <= fuzzy_speed_calc(arr[i]) <= 0.35):
			print 'OK'
		else:
			print fuzzy_speed_calc(arr[i])

def test5_fuzzy():
	print 'Car is very close'
	arr = [1, 5, 7, 9]
	for i in range(len(arr)):
		if (0 <= fuzzy_speed_calc(arr[i]) <= 0.1):
			print 'OK'
		else:
			print fuzzy_speed_calc(arr[i])

test1_fuzzy()
test2_fuzzy()
test3_fuzzy()
test4_fuzzy()
test5_fuzzy()
