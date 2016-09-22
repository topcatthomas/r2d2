import sys, threading, time, atexit
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import linearsensor as lin 

motorpin = 3
speed = 255
emergencyStop = False

mh = Adafruit_MotorHAT(addr=0x60)

motor = mh.getMotor(motorpin)

def turnOffMotors():
    mh.getMotor(motorpin).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

def doEmergencyStop():
    emergencyStop = True

def startPwm():
    mh = Adafruit_MotorHAT(addr=0x60)

def cleanup():
    emergencyStop = True
    turnOffMotors()
    lin.shutDown()

def init():
    motor.setSpeed(speed)
    lin.init()

def moveToPos(aPos):
    print "moveToPos called " + str(aPos)
    curPos = lin.getCurrentPos()
    print "curPos is " + str(curPos) + " ES " + str(emergencyStop)
    lastLeft = None
    while ( curPos != aPos and not emergencyStop ):
        curPos = lin.getCurrentPos()
        goLeft = curPos > aPos
        print "curPos is " + str(curPos) + " goLeft " + str(goLeft) + " lastLeft " + str(lastLeft)
        if ( lastLeft != None and goLeft != lastLeft ):
            break
        if ( lastLeft == None ):
            lastLeft = goLeft
            if ( goLeft ):
                motor.run(Adafruit_MotorHAT.FORWARD)
            else:
                motor.run(Adafruit_MotorHAT.BACKWARD)
        threading.sleep(100)

def turnOffMotors():
        mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

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
