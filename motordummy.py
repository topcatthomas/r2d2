#import RPi.GPIO as GPIO, sys, threading, time
slowspeed = 10.
fastspeed = 100.
speed = slowspeed

def doMove(x,y):
    print 'doMove called x=' + str(x) + ' y=' + str(y)

def setSpeed(newSpeed):
    global speed
    print 'setSpeed called'
    speed = float(newSpeed)
    print "setSpeed called to " + str(speed)

def getSpeed():
    global speed
    print "getSpeed called to " + str(speed)
    return speed

def playAction(action,newSpeed):
    print 'playAction called'
    setSpeed(newSpeed)
    print 'deciding what to do ' + action
    if action=="forward":
        forwards()
    elif action == "stop":
        stop()
    elif action == "vleft":
        veerLeft()
    elif action == "vright":
        veerRight()
    elif action == "right":
        right()
    elif action == "left":
        left()
    elif action == "vbleft":
        veerBackLeft()
    elif action == "vbright":
        veerBackRight()
    elif action == "backward":
        backwards()
    else:
        print "what was that, huh???" + action

# start up pwms
def startPwm():
    print "startPwm called"

def cleanup():
    print "cleanup called"

def forwards():
    global speed
    print "forwards called " + str(speed)

def backwards():
    global speed
    print "backwards called " + str(speed)

def left():
    global speed
    print "left called " + str(speed)
  
def right():
    global speed
    print "right called " + str(speed)
  
def stop():
    print "stop called " + str(speed)
  
def veerRight():
    print "veer right called " + str(speed)
  
def veerLeft():
    print "veer left called " + str(speed)

def veerBackRight():
    print "veer Back right called " + str(speed)
  
def veerBackLeft():
    print "veer back left called " + str(speed)

def getInnerSpeed(speed):
    global slowspeed
    print "getInnerSpeed called " + str(speed)
    if (speed/2<slowspeed):
        return 0
    else:
        return speed/2
