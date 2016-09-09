import RPi.GPIO as GPIO, sys, threading, time
slowspeed = 50.
fastspeed = 100.
speed = slowspeed



# one time init of io
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# seup pins to be out fr motors
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

# setup pwn
p=GPIO.PWM(19, speed)
q=GPIO.PWM(21, speed)
a=GPIO.PWM(24,speed)
b=GPIO.PWM(26,speed)

def setSpeed(newSpeed):
    global speed
    speed = float(newSpeed)
    print speed
    print newSpeed

def getSpeed():
    global speed
    return speed

# start up pwms
def startPwm():
  p.start(0)
  q.start(0)
  a.start(0)
  b.start(0)

def cleanup():
  print "cleanup called"
  GPIO.cleanup()

def doMove(x,y):
  print 'doing a gen move x=' + str(x) + " y=" + str(y)

def forwards():
  global speed
  print "forwards called " + str(speed)
  p.ChangeDutyCycle(speed)
  q.ChangeDutyCycle(0)
  a.ChangeDutyCycle(speed)
  b.ChangeDutyCycle(0)

def backwards():
  global speed
  print "backwards called " + str(speed)
  q.ChangeDutyCycle(speed)
  p.ChangeDutyCycle(0)
  b.ChangeDutyCycle(speed)
  a.ChangeDutyCycle(0)

def left():
  global speed
  print "left called " + str(speed)
  p.ChangeDutyCycle(speed)
  q.ChangeDutyCycle(0)
  a.ChangeDutyCycle(0)
  b.ChangeDutyCycle(0)
  
def right():
  global speed
  print "right called " + str(speed)
  a.ChangeDutyCycle(speed)
  q.ChangeDutyCycle(0)
  p.ChangeDutyCycle(0)
  b.ChangeDutyCycle(0)
  
def stop():
  print "stop called " + str(speed)
  p.ChangeDutyCycle(0)
  q.ChangeDutyCycle(0)
  a.ChangeDutyCycle(0)
  b.ChangeDutyCycle(0)
  
def veerRight():
  global speed
  print "veerRight called " + str(speed)
  p.ChangeDutyCycle(getInnerSpeed(speed))
  q.ChangeDutyCycle(0)
  a.ChangeDutyCycle(speed)
  b.ChangeDutyCycle(0)
  
def veerLeft():
  global speed
  print "veerLeft called " + str(speed)
  a.ChangeDutyCycle(getInnerSpeed(speed))
  q.ChangeDutyCycle(0)
  p.ChangeDutyCycle(speed)
  b.ChangeDutyCycle(0)

def veerBackRight():
  global speed
  print "veerBackRight called " + str(speed)
  q.ChangeDutyCycle(getInnerSpeed(speed))
  p.ChangeDutyCycle(0)
  b.ChangeDutyCycle(speed)
  a.ChangeDutyCycle(0)
  
def veerBackLeft():
  global speed
  print "veerBackLeft called " + str(speed)
  q.ChangeDutyCycle(getInnerSpeed(speed))
  a.ChangeDutyCycle(0)
  b.ChangeDutyCycle(speed)
  p.ChangeDutyCycle(0)

def getInnerSpeed(speed):
  global speed
  global slowspeed
  if (speed/2<slowspeed):
    return 0
  else:
    return speed/2
