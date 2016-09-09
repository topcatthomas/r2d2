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

def cleanup():
    turnOffMotors();

def setSpeed(newSpeed):
    global speed
    speed = int(newSpeed)*2
    print speed
    print newSpeed

def getSpeed():
    global speed
    return float(speed)

def doMove(xs,ys):
  print 'doMove called x=' + str(x) + ' y=' + str(y)
  x = float(xs)
  y = float(ys)
  print x
  print y
  if ( abs(y-0.5) < 0.1 and abs(x-0.5) < 0.1):
    stop()
  else:
    leftbit = 1-x
    rightbit = x
    absbit = 4*abs(y-0.5)
    print "absbit "+str(absbit)
    print "leftbit "+str(leftbit)
    print "rightbit "+str(rightbit)
    leftSpeed = int(leftbit*255*absbit)
    rightSpeed = int(rightbit*255*absbit)
    if ( leftSpeed > 255 ):
       leftSpeed = 255
    if ( rightSpeed > 255 ):
       rightSpeed = 255
    print "leftSpeed "+str(leftSpeed)
    print "rightSpeed "+str(rightSpeed)
    leftMotor.setSpeed(leftSpeed)
    rightMotor.setSpeed(rightSpeed)
    if ( y > 0.5 ):
      leftMotor.run(Adafruit_MotorHAT.FORWARD);
      rightMotor.run(Adafruit_MotorHAT.FORWARD);
    else:
      leftMotor.run(Adafruit_MotorHAT.BACKWARD);
      rightMotor.run(Adafruit_MotorHAT.BACKWARD);

def backwards():
  global speed
  print "backwards called " + str(speed)
  leftMotor.setSpeed(speed)
  leftMotor.run(Adafruit_MotorHAT.FORWARD);
  rightMotor.setSpeed(speed)
  rightMotor.run(Adafruit_MotorHAT.FORWARD);

def forwards():
  global speed
  print "forwards called " + str(speed)
  leftMotor.setSpeed(speed)
  leftMotor.run(Adafruit_MotorHAT.BACKWARD);
  rightMotor.setSpeed(speed)
  rightMotor.run(Adafruit_MotorHAT.BACKWARD);

def left():
  global speed
  print "left called " + str(speed)
  leftMotor.setSpeed(speed)
  leftMotor.run(Adafruit_MotorHAT.FORWARD);
  rightMotor.setSpeed(0)
  rightMotor.run(Adafruit_MotorHAT.FORWARD);
  
def right():
  global speed
  print "right called " + str(speed)
  leftMotor.setSpeed(0)
  leftMotor.run(Adafruit_MotorHAT.FORWARD);
  rightMotor.setSpeed(speed)
  rightMotor.run(Adafruit_MotorHAT.FORWARD);
  
def stop():
  print "stop called " + str(speed)
  leftMotor.setSpeed(0)
  rightMotor.setSpeed(0)
  
def veerRight():
  global speed
  print "veerRight called " + str(speed)
  leftMotor.setSpeed(0)
  leftMotor.run(Adafruit_MotorHAT.FORWARD);
  rightMotor.setSpeed(getInnerSpeed(speed))
  rightMotor.run(Adafruit_MotorHAT.FORWARD);
  
def veerLeft():
  global speed
  print "veerLeft called " + str(speed)
  rightMotor.setSpeed(0)
  leftMotor.run(Adafruit_MotorHAT.FORWARD);
  lefttMotor.setSpeed(getInnerSpeed(speed))
  rightMotor.run(Adafruit_MotorHAT.FORWARD);

def veerBackRight():
  global speed
  print "veerBackRight called " + str(speed)
  rightMotor.setSpeed(0)
  leftMotor.run(Adafruit_MotorHAT.BACKWARD);
  lefttMotor.setSpeed(getInnerSpeed(speed))
  rightMotor.run(Adafruit_MotorHAT.BACKWARD);
  
def veerBackLeft():
  global speed
  print "veerBackLeft called " + str(speed)
  leftMotor.setSpeed(0)
  leftMotor.run(Adafruit_MotorHAT.BACKWARD);
  rightMotor.setSpeed(getInnerSpeed(speed))
  rightMotor.run(Adafruit_MotorHAT.BACKWARD);

def getInnerSpeed(speed):
  global slowspeed
  global speed
  print "getInnerSpeed called " + str(speed)
  if (speed/2<slowspeed):
    return 0
  else:
    return speed/2
