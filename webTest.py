from flask import Flask, render_template, request, jsonify

import injectioncontroller
mc = injectioncontroller.importMotor();

app = Flask(__name__)

# return index page when IP address of RPi is typed in the browser
@app.route("/")
def Index():
    return render_template("index.html", uptime="")

# ajax GET call this function to set led state
# depeding on the GET parameter sent
@app.route("/_command")
def command():
    action = request.args.get('action')
    speed = request.args.get('speed')
    print action
    print speed
    mc.setSpeed(speed)
    if action=="forward":
        mc.forwards()
    elif action == "stop":
        mc.stop()
    elif action == "vleft":
        mc.veerLeft()
    elif action == "vright":
        mc.veerRight()
    elif action == "right":
        mc.right()
    elif action == "left":
        mc.left()
    elif action == "vbleft":
        mc.veerBackLeft()
    elif action == "vbright":
        mc.veerBackRight()
    elif action == "backward":
        mc.backwards()





    else:
        print "what was that, huh???" + action
    return "hi there"


# run the webserver on standard port 80, requires sudo
if __name__ == "__main__":
    mc.startPwm()
    app.run(host='0.0.0.0', port=80, debug=True)
    mc.cleanup()

