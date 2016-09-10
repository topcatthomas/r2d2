import RPi.GPIO as GPIO

FORWARD = 1
BACKWARD = 2
RIGHTMOTOR = 1
LEFTMOTOR = 2

freq = 20
slowspeed = 50.
fastspeed = 100.
speed = slowspeed

leftMotorP1 = None
leftMotorP2 = None
rightMotorP1 = None
rightMotorP2 = None

def setSpeed(newSpeed):
    global speed
    speed = float(newSpeed)
    print speed
    print newSpeed

def getSpeed():
    global speed
    print "getspeed called " + str(speed)
    return speed

# start up pwms
def startPwm():
    print "start pwm called"
    init()

def cleanup():
  print "cleanup called"
  stop()
  GPIO.cleanup()

def forwards():
  global speed
  print "forwards called " + str(speed)
  run(LEFTMOTOR,FORWARD,speed)
  run(RIGHTMOTOR,FORWARD,speed)

def backwards():
  global speed
  print "backwards called " + str(speed)
  run(LEFTMOTOR,BACKWARD,speed)
  run(RIGHTMOTOR,BACKWARD,speed)

def doMove(xs,ys):
  x = float(xs)
  y = float(ys)
  print 'doing a gen move x=' + str(x) + " y=" + str(y)
  if ( abs(y-0.5) < 0.1 and abs(x-0.5) < 0.1):
    stop()
  else:
    leftbit = 1-x
    rightbit = x
    absbit = 4*abs(y-0.5)
    print "absbit "+str(absbit)
    print "leftbit "+str(leftbit)
    print "rightbit "+str(rightbit)
    leftSpeed = int(leftbit*100*absbit)
    rightSpeed = int(rightbit*100*absbit)
    if ( leftSpeed > 100 ):
       leftSpeed = 100
    if ( rightSpeed > 100 ):
       rightSpeed = 100
    print "leftSpeed "+str(leftSpeed)
    print "rightSpeed "+str(rightSpeed)
    if ( y > 0.5 ):
      run(LEFTMOTOR,FORWARD,leftSpeed)
      run(RIGHTMOTOR,FORWARD,rightSpeed)
    else:
      run(LEFTMOTOR,BACKWARD,leftSpeed)
      run(RIGHTMOTOR,BACKWARD,rightSpeed)
    

def init():
    global leftMotorP1,leftMotorP2,rightMotorP1,rightMotorP2
    print "init called"
    # one time init of io
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    # seup pins to be out fr motors
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(26, GPIO.OUT)
    # setup pwn
    leftMotorP1=GPIO.PWM(19, freq)
    leftMotorP2=GPIO.PWM(21, freq)
    rightMotorP1=GPIO.PWM(24,freq)
    rightMotorP2=GPIO.PWM(26,freq)

def run(motor,direction,speed):
    global leftMotorP1,leftMotorP2,rightMotorP1,rightMotorP2
    toRunPin = leftMotorP1
    toStopPin = leftMotorP2
    if (motor == LEFTMOTOR):
        if (direction == FORWARD):
            toRunPin = leftMotorP1
            toStopPin = leftMotorP2
        else:
            toRunPin = leftMotorP2
            toStopPin = leftMotorP1
    elif (motor == RIGHTMOTOR):
        if (direction == FORWARD):
            toRunPin = rightMotorP1
            toStopPin = rightMotorP2
        else:
            toRunPin = rightMotorP2
            toStopPin = rightMotorP1
    toRunPin.stop()
    toStopPin.stop()
    toRunPin.start(speed)


def stop():
    global leftMotorP1,leftMotorP2,rightMotorP1,rightMotorP2
    rightMotorP1.stop()
    rightMotorP2.stop()
    leftMotorP1.stop()
    leftMotorP2.stop()
