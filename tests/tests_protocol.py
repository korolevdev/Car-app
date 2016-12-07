import sys
sys.path.insert(0, '../')
from protocol import * 

def test1_encode():
    print encode(1,100,0)
    #if (encode(1,100,0) == 2):
    #   print("Backward|OK")
    #else:
    #    print("Backward|FAIL")
    
test1_encode()

