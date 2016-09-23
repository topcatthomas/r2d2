import pigpio , datetime, time

pi = pigpio.pi()

SENSORPIN1 = 23
SENSORPIN2 = 24

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
       levB = level;
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
       if ( targetPos != -1 and targetPosCallback ):
          abspos =  abs ( targetPos - position)
          if ( abspos < 2 ): 
              targetPos = -1
          if ( abspos < 150 ):
              targetPosCallback(abspos)

def setTargetPos(aPos,posCallback):
    global targetPosCallback, targetPos
    targetPosCallback = posCallback
    targetPos = aPos

def getTargetPos():
    return targetPos

def getCurrentPos():
    global position
    return position


