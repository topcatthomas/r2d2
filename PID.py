############################################################################################
#
# PID algorithm to take input sensor readings, and target requirements, and
# as a result feedback new rotor speeds.
#
# c = (E*Kp)+(Ed*Kd)+(Ei*Ki)
# where c is the modifier to for example pwm duty
# E is the error, ie diff between target speed and current speed
# Ed is delta on error, so last error - current error
# Ei sum of error
# see http://letsmakerobots.com/node/865
# https://studentnet.cs.manchester.ac.uk/resources/library/thesis_abstracts/MSc14/FullText/Ioannidis-Feidias-fulltext.pdf
# http://stackoverflow.com/questions/25897723/pid-controller-for-dc-motor
#import PID
#import time
#
#dc_pid = PID.PID(2.5, .1, 1.5)
#
#
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.add_event_detect(22, GPIO.FALLING, callback=self.interrupt_function,bouncetime=5) #GPIO where encoders signal is conected
#
#
#def interrupt_function():
#
#   """on this function you make calculations depending on what PID you are planning to use , for example if you are planning to do a Velocity PID , and the encoder signal is connected to a GPIO pin you should take time stamps and convert signal frecuency to velocity , save it as a variable and #then update that value to the PID controller"""
#   error = dc_pid.update(velocity) 
#   #once you get your error you actuate it to your DC motor , via PWM , previously mapped function depending on your dc motor voltage and velocity it has depending on the PWM's duty cycle
#   pwm.ChangeDutyCycle(error/15) # or whatever your convertion is 
#
#
#readings = [1, 3, 5, 7, 12, 15, 17, 19, 27, 24, 24, 26]
#initial_time = time.time
#for reading in readings:
#    dc_pid.setPoint(reading)
#    time.sleep(10)
#
############################################################################################
class PID:

   def __init__(self, p_gain, i_gain, d_gain, now):
      self.last_error = 0.0
      self.last_time = now

      self.p_gain = p_gain
      self.i_gain = i_gain
      self.d_gain = d_gain

      self.i_error = 0.0


   def Compute(self, input, target, now):
      dt = (now - self.last_time)

      #---------------------------------------------------------------------------
      # Error is what the PID alogithm acts upon to derive the output
      #---------------------------------------------------------------------------
      error = target - input

      #---------------------------------------------------------------------------
      # The proportional term takes the distance between current input and target
      # and uses this proportially (based on Kp) to control the ESC pulse width
      #---------------------------------------------------------------------------
      p_error = error

      #---------------------------------------------------------------------------
      # The integral term sums the errors across many compute calls to allow for
      # external factors like wind speed and friction
      #---------------------------------------------------------------------------
      self.i_error += (error + self.last_error) * dt
      i_error = self.i_error

      #---------------------------------------------------------------------------
      # The differential term accounts for the fact that as error approaches 0,
      # the output needs to be reduced proportionally to ensure factors such as
      # momentum do not cause overshoot.
      #---------------------------------------------------------------------------
      d_error = (error - self.last_error) / dt

      #---------------------------------------------------------------------------
      # The overall output is the sum of the (P)roportional, (I)ntegral and (D)iffertial terms
      #---------------------------------------------------------------------------
      p_output = self.p_gain * p_error
      i_output = self.i_gain * i_error
      d_output = self.d_gain * d_error

      #---------------------------------------------------------------------------
      # Store off last input for the next differential calculation and time for next integral calculation
      #---------------------------------------------------------------------------
      self.last_error = error
      self.last_time = now

      #---------------------------------------------------------------------------
      # Return the output, which has been tuned to be the increment / decrement in ESC PWM
      #---------------------------------------------------------------------------
      return p_output, i_output, d_output


############################################################################################
#
#  Class for managing each blade + motor configuration via its ESC
#
############################################################################################
class HEATER:

   def __init__(self, pin):
      #---------------------------------------------------------------------------
      # The GPIO BCM numbered pin providing PWM signal for this ESC
      #---------------------------------------------------------------------------
      self.bcm_pin = pin

      #---------------------------------------------------------------------------
      # Initialize the RPIO DMA PWM for the THERMOSTAT in microseconds - full range
      # of pulse widths for 3ms carrier.
      #---------------------------------------------------------------------------
      self.min_pulse_width = 0
      self.max_pulse_width = 2999

      #---------------------------------------------------------------------------
      # The PWM pulse range required by this ESC
      #---------------------------------------------------------------------------
      pulse_width = self.min_pulse_width

      #---------------------------------------------------------------------------
      # Initialize the RPIO DMA PWM for the THERMOSTAT.
      #---------------------------------------------------------------------------
      PWM.add_channel_pulse(RPIO_DMA_CHANNEL, self.bcm_pin, 0, pulse_width)

   def update(self, temp_out):
      pulse_width = int(self.min_pulse_width + temp_out)

      if pulse_width < self.min_pulse_width:
         pulse_width = self.min_pulse_width
      if pulse_width > self.max_pulse_width:
         pulse_width = self.max_pulse_width

      PWM.add_channel_pulse(RPIO_DMA_CHANNEL, self.bcm_pin, 0, pulse_width)

temp_pid = PID(PID_TEMP_P_GAIN, PID_TEMP_I_GAIN, PID_TEMP_D_GAIN, time_now)
heater = HEATER(RPIO_THERMOSTAT_PWM)

[p_out, i_out, d_out] = temp_pid.Compute(temp_now, MPU6050_TEMP_TARGET, time_now)
temp_out = p_out + i_out + d_out
heater.update(temp_out)