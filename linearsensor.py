import RPi.GPIO as GPIO , datetime, time

GPIO.setmode(GPIO.BCM)

SENSORPIN1 = 23
SENSORPIN2 = 24

position = 0

start_time = time.clock()
count1=0
count2=0

def init():
    GPIO.setup(SENSORPIN1, GPIO.IN)
    GPIO.setup(SENSORPIN2, GPIO.IN)
    GPIO.add_event_detect(SENSORPIN1, GPIO.BOTH, callback=eventUpdate)
    GPIO.add_event_detect(SENSORPIN2, GPIO.BOTH, callback=eventUpdate)

def shutDown():
    GPIO.cleanup()           # clean up GPIO on normal exit

def eventUpdate(channel):
    global position
    print "eventUpdate on " + str(channel) + " position was " + str(position)
    pin1 = GPIO.input(SENSORPIN1)
    pin2 = GPIO.input(SENSORPIN2)
    print "lines " + str(pin1) + " , " + str(pin2)
    if ( channel == SENSORPIN1 ):
        if ( pin1 != pin2 ):
            position = position + 1
        else:
            position = position - 1
    else: 
        if ( pin1 == pin2 ):
            position = position + 1
        else:
            position = position - 1
    print "position now " + str(position)

def getCurrentPos():
    global position
    return position

def manualTest():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SENSORPIN1, GPIO.IN)
        GPIO.setup(SENSORPIN2, GPIO.IN)
        GPIO.add_event_detect(SENSORPIN1, GPIO.BOTH, callback=my_callback)
        GPIO.add_event_detect(SENSORPIN2, GPIO.BOTH, callback=my_callback2)
        raw_input("Press Enter when ready\n>")
        shutDown()
    except KeyboardInterrupt:
        shutDown()

def my_callback(channel):
    global count1,start_time
    count1 = count1 + 1
    timePassed = time.clock()# - start_time
    print "falling edge detected on 2 " + str(count1) + " : " + str(timePassed)

def my_callback2(channel):
    global count2, start_time
    count2 = count2 + 1
    timePassed = time.clock()# - start_time
    print "falling edge detected on 23 " + str(count2) + " : " + str(timePassed)

