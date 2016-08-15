#import RPi.GPIO as GPIO, sys, threading, time
slowspeed = 10.
fastspeed = 100.
speed = slowspeed



def setSpeed(newSpeed):
    global speed
    speed = float(newSpeed)
    print "setSpeed called to "# + speed

def getSpeed():
    global speed
    print "getSpeed called to "# + speed
    return speed

# start up pwms
def startPwm():
    print "startPwm called"

def forwards():
    global speed
    print speed
    print "forwards called "# + speed

def backwards():
    global speed
    print "forwards called "# + speed

def left():
    global speed
    print "forwards called "# + speed
  
def right():
    global speed
    print "forwards called "# + speed
  
def stop():
    print "forwards called "# + speed
  
def veerRight():
    print "forwards called "# + speed
  
def veerLeft():
    print "forwards called "# + speed

def veerBackRight():
    print "forwards called "# + speed
  
def veerBackLeft():
    print "forwards called "# + speed

def getInnerSpeed(speed):
    global slowspeed
    print "forwards called "# + speed
    if (speed/2<slowspeed):
        return 0
    else:
        return speed/2
