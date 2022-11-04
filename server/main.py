# python -m flask --app main run

from flask import Flask, request, jsonify
from SimConnect import *
import time
import vgamepad as vg
from flask_cors import CORS, cross_origin

buttons = [
    vg.DS4_BUTTONS.DS4_BUTTON_THUMB_RIGHT  ,
    vg.DS4_BUTTONS.DS4_BUTTON_THUMB_LEFT  ,
    vg.DS4_BUTTONS.DS4_BUTTON_OPTIONS ,
    vg.DS4_BUTTONS.DS4_BUTTON_SHARE  ,
    vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_RIGHT  ,
    vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_LEFT  ,
    vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_RIGHT  ,
    vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT  ,
    vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE  ,
    vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE ,
    vg.DS4_BUTTONS.DS4_BUTTON_CROSS ,
    vg.DS4_BUTTONS.DS4_BUTTON_SQUARE ,
]

actions = {
    'TOGGLE AUTOPILOT MASTER': [buttons[0]],
    'TOGGLE AUTOPILOT HEADING HOLD': [buttons[1]],
    'AUTOPILOT VS HOLD ON': [buttons[2]],
    'TOGGLE AUTOPILOT ALTITUDE HOLD': [buttons[3]],
    'AUTOPILOT NAV1 HOLD': [buttons[4]],
}

def pressButton(button_array, time_diff=0.3):
    for btn in button_array:
        gamepad.press_button(btn)        
    gamepad.update()
    
    time.sleep(time_diff)

    for btn in button_array:
        gamepad.release_button(btn)
    gamepad.update()

# Flight Simulator Connection
sm = None
while sm is None:
    print('Trying to Connect to Flight Simulator')
    try:
        sm = SimConnect()
    except:
        print('Failed to Connect. Will try again in 5 seconds')
        time.sleep(5)

print('Flight Simulator Connected')
ae = AircraftEvents(sm)
aq = AircraftRequests(sm, _time=10)

gamepad = vg.VDS4Gamepad()

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    print(request.json)
    return request.json

@app.route("/send_command", methods=['POST'])
def send_command():
    if request.json['command'] not in actions:
        return "Command not found", 400

    pressButton(actions[request.json['command']])
    return "Command sent", 200

@app.route("/send_event", methods=['POST'])
def send_event():
    event_to_trigger = ae.find(request.json['command'])
    if 'value' in request.json:
        event_to_trigger(request.json['value'])
    else:
        event_to_trigger()
    return "Command sent", 200

@app.route("/get_variable", methods=['POST'])
def get_variable():
    print(request.json)
    return {'result': aq.get(request.json['var'])}

@app.route("/set_variable", methods=['POST'])
def set_variable():
    aq.set(request.json['var'], request.json['value'])
    return "Command sent", 200

app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)