import threading
import injectioncontroller

mc = injectioncontroller.importMotor();

mc.startPwm()

mc.setSpeed(0)
mc.forwards()
threading._sleep(1)
mc.stop()

mc.setSpeed(25)
mc.forwards()
threading._sleep(1)
mc.stop()

mc.setSpeed(75)
mc.forwards()
threading._sleep(1)
mc.stop()

mc.setSpeed(100)
mc.forwards()
threading._sleep(1)
mc.stop()

mc.setSpeed(0)
mc.backwards()
threading._sleep(1)
mc.stop()

mc.setSpeed(25)
mc.backwards()
threading._sleep(1)
mc.stop()

mc.setSpeed(75)
mc.backwards()
threading._sleep(1)
mc.stop()

mc.setSpeed(100)
mc.backwards()
threading._sleep(1)
mc.stop()

mc.setSpeed(50)
mc.right()
threading._sleep(3)
mc.stop()

mc.setSpeed(50)
mc.left()
threading._sleep(3)
mc.stop()


mc.setSpeed(100)
mc.right()
threading._sleep(2)
mc.stop()

mc.setSpeed(100)
mc.left()
threading._sleep(3)
mc.stop()

mc.doMove(0.5,0)
threading._sleep(2)
mc.stop()


mc.cleanup()
