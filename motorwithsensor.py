import sys, threading, time, atexit
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import linearsensor as lin 


speed = 20
emergencyStop = False

mh = Adafruit_MotorHAT(addr=0x60)

motor = mh.getMotor(3)

def turnOffMotors():
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

def emergencyStop():
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
    curPos = lin.getCurrentPos()
    while ( curPos != aPos and not emergencyStop ):
        goLeft = curPos < aPos
        if ( goLeft ):
            motor.run(Adafruit_MotorHAT.FORWARD)
        else:
            motor.run(Adafruit_MotorHAT.BACKWARD)

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
            if ( newPos < 0 )
                break
            print "moving to " + str(newPos)
            moveToPos(newPos)
        cleanup()
    except KeyboardInterrupt:
        cleanup()