#!/usr/bin/python
''' DON'T TOUCH THESE FIRST LINES! '''
''' ============================== '''
from PyoConnect import *
myo = Myo(sys.argv[1] if len(sys.argv) >= 2 else None) 
''' ============================== '''

''' OK, edit below to make your own fancy script ^.^ '''

# Edit here:

def onPoseEdge(pose, edge):
	print("onPoseEdge: "+pose+", "+edge)

# Stop editting

# Comment out below the events you are not using
#myo.onLock = onLock
#myo.onUnlock = onUnlock
#myo.onPoseEdge = onPoseEdge 
#myo.onPeriodic = onPeriodic
#myo.onWear = onWear
#myo.onUnwear = onUnwear
#myo.onEMG = onEMG
#myo.onBoxChange = onBoxChange

''' DON'T TOUCH BELOW THIS LINE! '''
''' ============================ '''
myo.connect()
while (not myo.getGyro()):
	print('Wait a myo')
	myo.run()

while True:
	myo.run()
	Ax, Ay, Az = myo.getAccel()
	Gx, Gy, Gz = myo.getGyro()

	print(str(x))
