import pigpio

#connect to pigpiod daemon
pi = pigpio.pi()

FORWARD = 1
BACKWARD = 2
RIGHTMOTOR = 1
LEFTMOTOR = 2

freq = 60
slowspeed = 50
fastspeed = 100
speed = slowspeed

leftMotorP1 = 10
leftMotorP2 = 9
rightMotorP1 = 8
rightMotorP2 = 7

def setSpeed(newSpeed):
    global speed
    speed = int(int(newSpeed)*2.5)
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
    pi.set_mode(leftMotorP1, pigpio.OUTPUT)
    pi.set_mode(leftMotorP2, pigpio.OUTPUT)
    pi.set_mode(rightMotorP1, pigpio.OUTPUT)
    pi.set_mode(rightMotorP2, pigpio.OUTPUT)
    # setup pwn
    pi.set_PWM_frequency(leftMotorP1, freq)
    pi.set_PWM_frequency(leftMotorP2, freq)
    pi.set_PWM_frequency(rightMotorP1,freq)
    pi.set_PWM_frequency(rightMotorP2,freq)

def right():
  global speed
  print "right called " + str(speed)
  run(LEFTMOTOR,FORWARD,speed)
  run(RIGHTMOTOR,FORWARD,0)
    
def left():
  global speed
  print "right called " + str(speed)
  run(LEFTMOTOR,FORWARD,0)
  run(RIGHTMOTOR,FORWARD,speed)

def veerRight():
  global speed
  print "veerRight called " + str(speed)
  run(LEFTMOTOR,FORWARD,getInnerSpeed(speed))
  run(RIGHTMOTOR,FORWARD,speed)
  
def veerLeft():
  global speed
  print "veerLeft called " + str(speed)
  run(RIGHTMOTOR,FORWARD,getInnerSpeed(speed))
  run(LEFTMOTOR,FORWARD,speed)

def veerBackRight():
  global speed
  print "veerBackRight called " + str(speed)
  run(LEFTMOTOR,BACKWARD,getInnerSpeed(speed))
  run(RIGHTMOTOR,BACKWARD,speed)
  
def veerBackLeft():
  global speed
  print "veerBackLeft called " + str(speed)
  run(RIGHTMOTOR,BACKWARD,getInnerSpeed(speed))
  run(LEFTMOTOR,BACKWARD,speed)

def getInnerSpeed(speed):
  global slowspeed
  if (speed/2<slowspeed):
    return 0
  else:
    return speed/2

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

