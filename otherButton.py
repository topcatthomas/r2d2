import Tkinter
import tkMessageBox
import motorcontroller as mc

#one timeinit of gui
top = Tkinter.Tk()

"""
import RPi.GPIO as GPIO, sys, threading, time

# glbal speed variable
slowspeed = 10.
fastspeed = 100.
speed = slowspeed

#one timeinit of gui
top = Tkinter.Tk()

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

# start up pwms
def startPwm():
  p.start(0)
  q.start(0)
  a.start(0)
  b.start(0)

def forwards():
  global speed
  print speed
  p.ChangeDutyCycle(speed)
  q.ChangeDutyCycle(0)
  a.ChangeDutyCycle(speed)
  b.ChangeDutyCycle(0)

def backwards():
  global speed
  q.ChangeDutyCycle(speed)
  p.ChangeDutyCycle(0)
  b.ChangeDutyCycle(speed)
  a.ChangeDutyCycle(0)

def left():
  global speed
  p.ChangeDutyCycle(speed)
  q.ChangeDutyCycle(0)
  a.ChangeDutyCycle(0)
  b.ChangeDutyCycle(0)
  
def right():
  global speed
  a.ChangeDutyCycle(speed)
  q.ChangeDutyCycle(0)
  p.ChangeDutyCycle(0)
  b.ChangeDutyCycle(0)
  
def stop():
  p.ChangeDutyCycle(0)
  q.ChangeDutyCycle(0)
  a.ChangeDutyCycle(0)
  b.ChangeDutyCycle(0)
  
def veerRight():
  p.ChangeDutyCycle(getInnerSpeed(speed))
  q.ChangeDutyCycle(0)
  a.ChangeDutyCycle(speed)
  b.ChangeDutyCycle(0)
  
def veerLeft():
  a.ChangeDutyCycle(getInnerSpeed(speed))
  q.ChangeDutyCycle(0)
  p.ChangeDutyCycle(speed)
  b.ChangeDutyCycle(0)

def veerBackRight():
  q.ChangeDutyCycle(getInnerSpeed(speed))
  p.ChangeDutyCycle(0)
  b.ChangeDutyCycle(speed)
  a.ChangeDutyCycle(0)
  
def veerBackLeft():
  q.ChangeDutyCycle(getInnerSpeed(speed))
  a.ChangeDutyCycle(0)
  b.ChangeDutyCycle(speed)
  p.ChangeDutyCycle(0)
def getInnerSpeed(speed):
  global slowspeed
  if (speed/2<slowspeed):
    return 0
  else:
    return speed/2
"""
def createButtons():
  B = Tkinter.Button(top, text ="forwards", command = mc.forwards)
  B.grid(row=0,column=1)
  
  B = Tkinter.Button(top, text ="backwards", command = mc.backwards)
  B.grid(row=2,column=1)
  
  B = Tkinter.Button(top, text ="left", command = mc.left)
  B.grid(row=1, column=0)
  
  B = Tkinter.Button(top, text ="right", command = mc.right)
  B.grid(row=1, column=2)
  
  B = Tkinter.Button(top, text ="veer right", command = mc.veerRight)
  B.grid(row=0, column=2)
  
  B = Tkinter.Button(top, text ="veer left", command = mc.veerLeft)
  B.grid(row=0, column=0)
  
  B = Tkinter.Button(top, text ="veer  back right", command = mc.veerBackRight)
  B.grid(row=2, column=2)
  
  B = Tkinter.Button(top, text ="veer back left", command = mc.veerBackLeft)
  B.grid(row=2, column=0)
  
  B = Tkinter.Button(top, text ="stop", command = mc.stop)
  B.grid(row=1, column=1)

  L = Tkinter.Label(top,text="speed changer")
  L.grid(row=3,column=0)                    
  Slider = Tkinter.Scale(top, width=5,length=300,from_=mc.getSpeed(), to=100, orient=Tkinter.HORIZONTAL, command = mc.setSpeed)
  Slider.set(mc.getSpeed())
  Slider.grid(row=3,column=1,columnspan=3)



createButtons()
mc.startPwm()

top.mainloop()

GPIO.cleanup()
