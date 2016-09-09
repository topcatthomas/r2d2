import threading
import injectioncontroller

mc = injectioncontroller.importMotor();

mc.startPwm()

mc.setSpeed(0)
mc.forwards()
threading._sleep(.25)
mc.stop()

mc.setSpeed(25)
mc.forwards()
threading._sleep(.25)
mc.stop()

mc.setSpeed(75)
mc.forwards()
threading._sleep(.25)
mc.stop()

mc.setSpeed(100)
mc.forwards()
threading._sleep(.25)
mc.stop()

mc.setSpeed(0)
mc.backwards()
threading._sleep(.25)
mc.stop()

mc.setSpeed(25)
mc.backwards()
threading._sleep(.25)
mc.stop()

mc.setSpeed(75)
mc.backwards()
threading._sleep(.25)
mc.stop()

mc.setSpeed(100)
mc.backwards()
threading._sleep(.25)
mc.stop()


mc.cleanup()
