import sys, threading, time, atexit
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import linearsensor as lin 
motorpin = 3
speed = 100
emergencyStop = False

mh = Adafruit_MotorHAT(addr=0x60, freq=100)

motor = mh.getMotor(motorpin)

def turnOffMotor():
    motor.run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotor)

def doEmergencyStop():
    emergencyStop = True
    turnOffMotors()

def cleanup():
    emergencyStop = True
    turnOffMotor()
    lin.shutDown()

def init():
    motor.setSpeed(speed)
    lin.init()

def moveToPos(aPos):
    motor.setSpeed(speed)
    print "moveToPos called " + str(aPos)
    curPos = lin.getCurrentPos()
    lin.setTargetPos(aPos,targetCallBack)
    print "curPos is " + str(curPos) + " ES " + str(emergencyStop)
    if ( curPos != aPos and not emergencyStop ):
        goLeft = curPos > aPos
        print "curPos is " + str(curPos) + " goLeft " + str(goLeft) 
        if ( goLeft ):
            motor.run(Adafruit_MotorHAT.FORWARD)
        else:
            motor.run(Adafruit_MotorHAT.BACKWARD)
    lin.setTargetPos(aPos,targetCallBack)

def targetCallBack(pos):
    motor.setSpeed(0)

def testIt():
    try:
        init()
        while ( True ):
            newPos = int(raw_input("enter new pos\n>"))
	    print "new pos entered was " + str(newPos)
            if ( newPos < 0 ):
                break
            print "moving to " + str(newPos)
            moveToPos(newPos)
        cleanup()
    except KeyboardInterrupt:
        cleanup()
