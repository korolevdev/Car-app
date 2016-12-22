import sys
sys.path.insert(0, '../')
from utils import *

def test_encode_decode_1():
	a,b,c = 0, 0, 0
	a1,b1,c1 = decode(encode(a,b,c))
	if a1 == a and b1 == b and c1 == c:
		print('encode_decode1 | OK')
	else:
		print('encode_decode1 | FAILED')


def test_encode_decode_2():
	a,b,c = 1, 22, -8
	a1,b1,c1 = decode(encode(a,b,c))
	if a1 == a and b1 == b and c1 == c:
		print('encode_decode2 | OK')
	else:
		print('encode_decode2 | FAILED: CANT DECODE NEGATIVE DIGITS')
	
def test_encode_decode_3():
	a,b,c = 1, 2, 3
	a1,b1,c1 = decode(encode(a,b,c))
	if a1 == a and b1 == b and c1 == c:
		print('encode_decode3 | OK')
	else:
		print('encode_decode3 | FAILED')

def test_encode_decode_4():
	a,b,c = 255, 255, 255
	a1,b1,c1 = decode(encode(a,b,c))
	if a1 == a and b1 == b and c1 == c:
		print('encode_decode4 | OK')
	else:
		print('encode_decode4 | FAILED')

def test_encode_decode_5():
	a,b,c = 255, 256, 256
	a1,b1,c1 = decode(encode(a,b,c))
	if a1 == a and b1 == b and c1 == c:
		print('encode_decode5 | OK')
	else:
		print('encode_decode5 | FAILED: CANT DECODE POSITIVE DIGITS MORE THAN 8 bit')

def test_encode_decode_6():
	a,b,c = 'a', 'b', 'c'
	a1,b1,c1 = decode(encode(a,b,c))
	if a1 == a and b1 == b and c1 == c:
		print('encode_decode6 | OK')
	else:
		print('encode_decode6 | FAILED: CANT ENCODE SYMBOLS')

def test_check_int_1():
	a = "str"
	if not check_int(a):
		print('check_int_1 | OK')
	else:
		print('check_int_1| FAILED')

def test_check_int_2():
	a = "3"
	if check_int(a):
		print('check_int_2 | OK')
	else:
		print('check_int_2| FAILED')

def test_check_int_3():
	a = "-3"
	if check_int(a):
		print('check_int_3 | OK')
	else:
		print('check_int_3| FAILED')

def test_check_int_4():
	a = "1000000000000000"
	if check_int(a):
		print('check_int_4 | OK')
	else:
		print('check_int_4 | FAILED')

def test_check_int_5():
	a = "-100000000000000"
	if check_int(a):
		print('check_int_5 | OK')
	else:
		print('check_int_5| FAILED')

test_encode_decode_1()
test_encode_decode_2()
test_encode_decode_3()
test_encode_decode_4()
test_encode_decode_5()
#test_encode_decode_6()
test_check_int_1()
test_check_int_2()
test_check_int_3()
test_check_int_4()
test_check_int_5()
