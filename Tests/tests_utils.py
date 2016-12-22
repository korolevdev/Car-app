import sys
sys.path.insert(0, '../')
from utils import *

def test_encode_1():
	a,b, c = decode(encode(1,2,3))
	print (a,b,c)

test_encode_1()
