import sys
sys.path.insert(0, '../')
from protocol import * 

def test1_encode():
    if (encode(0,0,0) == 0):
        print("Encoded | OK")
    else:
        print("Encoded | FAILED")

def test2_encode():
    if (encode(1,100,0) == 0):
        print("Encoded  | OK")
    else:
        print("Encoded | FAILED")

def test3_encode():
    if (encode(1,100,0) == 0):
        print("Encoded | OK")
    else:
        print("Encoded | FAILED")

def test4_encode():
    if (encode(1,100,0) == 0):
        print("Encoded | OK")
    else:
        print("Encoded | FAILED")

def test1_decode():
    if (decode(87436874) == 0):
        print("Decoded | OK")
    else:
        print("Decoded | FAILED")

test1_encode()

