from flask import Flask, render_template, request, jsonify
import recorder as rec

import injectioncontroller
mc = injectioncontroller.importMotor()


app = Flask(__name__)

# return index page when IP address of RPi is typed in the browser
@app.route("/")
def Index():
    return render_template("index.html", uptime="")

#return canvas click type controller
@app.route("/canvascontroller.html")
def canvascontroller():
    return render_template("canvascontroller.html")

#ajax call to turn recording on
@app.route("/_reconoff")
def recon():
    rec.recordingOnOff()
    return "reconoff"

#ajax call to play recording
@app.route("/_playrecording")
def playrecording():
    rec.playBack(mc)
    return "playing"

@app.route("/_saverec")
def saverecording():
    rec.saveRecording("test1.txt")
    return "saved"

@app.route("/_loadrec")
def loadrecording():
    rec.loadRecording("test1.txt")
    return "loaded"

# ajax call to do a general xy move
# where y 0,1 1/2 is stop, x left right
@app.route("/_canvas")
def canvas():
    x = request.args.get('x')
    y = request.args.get('y')
    print x
    print y
    rec.recordDoMove(x,y)
    mc.doMove(x,y)
    return "hi there"

# ajax GET call this function to do robot action
# depeding on the GET parameter sent
@app.route("/_command")
def command():
    action = request.args.get('action')
    speed = request.args.get('speed')
    print action
    print speed
    rec.recordAction(action,speed)
    mc.playAction(action,speed)
    return "hi there"


# run the webserver on standard port 80, requires sudo
if __name__ == "__main__":
    mc.startPwm()
    app.run(host='0.0.0.0', port=80, debug=True)
    mc.cleanup()

