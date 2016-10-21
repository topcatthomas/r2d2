import pigpio , datetime, time

pi = pigpio.pi()

SENSORPIN1 = 23
SENSORPIN2 = 24

lastPos = 0
lastTime = time.clock()
speed = 0.0

position = 0
levA = 0
levB = 0
lastGpio = None

start_time = time.clock()
count1=0
count2=0
targetPos = -1
targetPosCallback = None

def init():
    pi.set_mode(SENSORPIN1, pigpio.INPUT)
    pi.set_mode(SENSORPIN2, pigpio.INPUT)
    pi.callback(SENSORPIN1, pigpio.EITHER_EDGE, eventUpdateRising)
    pi.callback(SENSORPIN2, pigpio.EITHER_EDGE, eventUpdateRising)

def shutDown():
    pi.stop()

def eventUpdateRising(gpio , level, tick):
    global targetPosCallback, targetPos
    global position, lastGpio, levA, levB
    if gpio == SENSORPIN1:
       levA = level
    else:
       levB = level
    if gpio != lastGpio: # debounce
       lastGpio = gpio
       if   gpio == SENSORPIN1 and level == 1:
          if levB == 1:
            position = position - 1 
       elif gpio == SENSORPIN2 and level == 1:
          if levA == 1:
            position = position + 1 
       #print "eventUpdate on " + str(gpio)+ " position was " + str(position) + "leva/levb " + str(levA) + "/" + str(levB) + " level " + str(level)
       #print "position now " + str(position)
       nowTime = time.clock()
       if ( lastPos != -1 ):
        speed = ( position - lastPos ) / ( nowTime -lastTime )
       print "speed is " + str(speed)
       lastPos = position
       lastTime = nowTime
       if ( targetPos != -1 and targetPosCallback ):
          abspos =  abs ( targetPos - position)
          if ( abspos < 2 ): 
              targetPos = -1
          if ( abspos < 15000 ):
              targetPosCallback(abspos)

def setTargetPos(aPos,posCallback):
    global targetPosCallback, targetPos
    targetPosCallback = posCallback
    targetPos = aPos
    speed = 0.0
    lastTime = time.clock()
    lastPos = -1

def getTargetPos():
    return targetPos

def getCurrentPos():
    global position
    return position

def getCurrentSpeed():
    return speed

