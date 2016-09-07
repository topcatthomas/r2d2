import Tkinter
import tkMessageBox
import injectioncontroller

mc = injectioncontroller.importMotor();

#one timeinit of gui
top = Tkinter.Tk()

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

mc.cleanup()
