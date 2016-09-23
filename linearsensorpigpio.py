import pigpio , datetime, time

#GPIO.setmode(GPIO.BCM)
pi = pigpio.pi()

SENSORPIN1 = 23
SENSORPIN2 = 24

position = 0

start_time = time.clock()
count1=0
count2=0
targetPos = -1
targetPosCallback = None

def init():
    pi.set_mode(SENSORPIN1, pigpio.INPUT)
    pi.set_mode(SENSORPIN2, pigpio.INPUT)
    pi.callback(SENSORPIN1, pigpio.EITHER_EDGE, eventUpdateRising)

def shutDown():
    pi.stop()

def eventUpdateRising(channel , level, tick):
    pin1 = pi.read(SENSORPIN1)
    eventUpdate(pin1)

def eventUpdate(isRising):
    global targetPosCallback, targetPos
    global position
    pin2 = GPIO.input(SENSORPIN2)
    #print "eventUpdate on " +str(isRising) + " position was " + str(position) + "pin2 " + str(pin2)
    if ( not isRising ):
        if ( pin2 ):
            position = position + 1
        else:
            position = position - 1
    else:
        if ( not pin2 ):
            position = position + 1
        else:
            position = position - 1
    #print "position now " + str(position)
    if ( targetPos != -1 and abs ( targetPos - position) < 10 and targetPosCallback ):
        targetPos = -1
        targetPosCallback(position)

def setTargetPos(aPos,posCallback):
    global targetPosCallback, targetPos
    targetPosCallback = posCallback
    targetPos = aPos

def getCurrentPos():
    global position
    return position


