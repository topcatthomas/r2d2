import RPi.GPIO as GPIO , datetime, time
GPIO.setmode(GPIO.BCM)

#GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

start_time = time.clock()
count24=0
count23=0

def my_callback(channel):
    global count24,start_time
    count24 = count24 + 1
    timePassed = time.clock()# - start_time
    print "falling edge detected on 24 " + str(count24) + " : " + str(timePassed)

def my_callback2(channel):
    global count23, start_time
    count23 = count23 + 1
    timePassed = time.clock()# - start_time
    print "falling edge detected on 23 " + str(count23) + " : " + str(timePassed)


# when a falling edge is detected on port 17, regardless of whatever
# else is happening in the program, the function my_callback will be run
GPIO.add_event_detect(23, GPIO.FALLING, callback=my_callback)

# when a falling edge is detected on port 23, regardless of whatever
# else is happening in the program, the function my_callback2 will be run
# 'bouncetime=300' includes the bounce control written into interrupts2a.py
GPIO.add_event_detect(24, GPIO.FALLING, callback=my_callback2)

try:
   raw_input("Press Enter when ready\n>")
except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit
