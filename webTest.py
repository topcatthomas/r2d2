from flask import Flask, render_template, request, jsonify
#import motorcontroller as mc
import motordummy as mc

app = Flask(__name__)

# return index page when IP address of RPi is typed in the browser
@app.route("/")
def Index():
    return render_template("index.html", uptime="work to do")

# ajax GET call this function to set led state
# depeding on the GET parameter sent
@app.route("/_led")
def _led():
    state = request.args.get('state')
    if state=="on":
        mc.forwards()
    else:
        mc.stop()
    return ""


# run the webserver on standard port 80, requires sudo
if __name__ == "__main__":
    mc.startPwm()
    app.run(host='0.0.0.0', port=80, debug=True)
