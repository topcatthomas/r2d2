#import RPi.GPIO as GPIO, sys, threading, time
slowspeed = 10.
fastspeed = 100.
speed = slowspeed

def doMove(x,y):
    print 'doMove called'
    print x
    print y

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

def cleanup():
    print "cleanup called"

def forwards():
    global speed
    print speed
    print "forwards called "# + speed

def backwards():
    global speed
    print "backwards called "# + speed

def left():
    global speed
    print "left called "# + speed
  
def right():
    global speed
    print "right called "# + speed
  
def stop():
    print "stop called " + str(speed)
  
def veerRight():
    print "veer right called "# + speed
  
def veerLeft():
    print "veer left called "# + speed

def veerBackRight():
    print "veer Back right called "# + speed
  
def veerBackLeft():
    print "veer back left called "# + speed

def getInnerSpeed(speed):
    global slowspeed
    print "forwards called "# + speed
    if (speed/2<slowspeed):
        return 0
    else:
        return speed/2
