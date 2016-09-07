import sys, threading, time
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import atexit


slowspeed = 20
fastspeed = 255
speed = slowspeed

mh = Adafruit_MotorHAT(addr=0x60)

leftMotor = mh.getMotor(2)
rightMotor = mh.getMotor(1)

def turnOffMotors():
        mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)


def startPwm():
    mh = Adafruit_MotorHAT(addr=0x60)

def setSpeed(newSpeed):
    global speed
    speed = int(newSpeed)*2
    print speed
    print newSpeed

def getSpeed():
    global speed
    return float(speed)

def backwards():
  global speed
  print 'doing forwards'
  print speed
  leftMotor.setSpeed(speed)
  leftMotor.run(Adafruit_MotorHAT.FORWARD);
  rightMotor.setSpeed(speed)
  rightMotor.run(Adafruit_MotorHAT.FORWARD);

def forwards():
  global speed
  leftMotor.setSpeed(speed)
  leftMotor.run(Adafruit_MotorHAT.BACKWARD);
  rightMotor.setSpeed(speed)
  rightMotor.run(Adafruit_MotorHAT.BACKWARD);

def left():
  global speed
  leftMotor.setSpeed(speed)
  leftMotor.run(Adafruit_MotorHAT.FORWARD);
  rightMotor.setSpeed(0)
  rightMotor.run(Adafruit_MotorHAT.FORWARD);
  
def right():
  global speed
  leftMotor.setSpeed(0)
  leftMotor.run(Adafruit_MotorHAT.FORWARD);
  rightMotor.setSpeed(speed)
  rightMotor.run(Adafruit_MotorHAT.FORWARD);
  
def stop():
  leftMotor.setSpeed(0)
  rightMotor.setSpeed(0)
  
def veerRight():
  leftMotor.setSpeed(0)
  leftMotor.run(Adafruit_MotorHAT.FORWARD);
  rightMotor.setSpeed(getInnerSpeed(speed))
  rightMotor.run(Adafruit_MotorHAT.FORWARD);
  
def veerLeft():
  rightMotor.setSpeed(0)
  leftMotor.run(Adafruit_MotorHAT.FORWARD);
  lefttMotor.setSpeed(getInnerSpeed(speed))
  rightMotor.run(Adafruit_MotorHAT.FORWARD);

def veerBackRight():
  rightMotor.setSpeed(0)
  leftMotor.run(Adafruit_MotorHAT.BACKWARD);
  lefttMotor.setSpeed(getInnerSpeed(speed))
  rightMotor.run(Adafruit_MotorHAT.BACKWARD);
  
def veerBackLeft():
  leftMotor.setSpeed(0)
  leftMotor.run(Adafruit_MotorHAT.BACKWARD);
  rightMotor.setSpeed(getInnerSpeed(speed))
  rightMotor.run(Adafruit_MotorHAT.BACKWARD);

def getInnerSpeed(speed):
  global slowspeed
  if (speed/2<slowspeed):
    return 0
  else:
    return speed/2
