import pigpio

#connect to pigpiod daemon
pi = pigpio.pi()

FORWARD = 1
BACKWARD = 2
RIGHTMOTOR = 1
LEFTMOTOR = 2

freq = 20
slowspeed = 50
fastspeed = 100
speed = slowspeed

leftMotorP1 = 19
leftMotorP2 = 21
rightMotorP1 = 24
rightMotorP2 = 26

def setSpeed(newSpeed):
    global speed
    speed = int(newSpeed)*2
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
  pi.stop()

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
    pi.set_mode(19, pigpio.OUTPUT)
    pi.set_mode(21, pigpio.OUTPUT)
    pi.set_mode(24, pigpio.OUTPUT)
    pi.set_mode(26, pigpio.OUTPUT)
    # setup pwn
    pi.set_PWM_frequency(19, freq)
    pi.set_PWM_frequency(21, freq)
    pi.set_PWM_frequency(24,freq)
    pi.set_PWM_frequency(26,freq)

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
    print "duty cycle will be " + str(speed) 
    pi.set_PWM_dutycycle(toRunPin,0)
    pi.set_PWM_dutycycle(toStopPin,0)
    pi.set_PWM_dutycycle(toRunPin,speed)


def stop():
    global leftMotorP1,leftMotorP2,rightMotorP1,rightMotorP2
    pi.set_PWM_dutycycle(rightMotorP1,0)
    pi.set_PWM_dutycycle(rightMotorP2,0)
    pi.set_PWM_dutycycle(leftMotorP1,0)
    pi.set_PWM_dutycycle(leftMotorP2,0)

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

