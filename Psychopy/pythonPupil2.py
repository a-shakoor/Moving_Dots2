"""
Receive data from Pupil using ZMQ. This script will connect to PupilRemote and start streaming incoming data to Matlab
via UDP

Send simple string messages to control Pupil Capture functions:
    'R' start recording with auto generated session name
    'R rec_name' start recording and name new session name: rec_name
    'r' stop recording
    'C' start currently selected calibration
    'c' stop currently selected calibration
    'T 1234.56' Timesync: make timestamps count form 1234.56 from now on.
    't' get pupil capture timestamp; returns a float as string.


    # IPC Backbone communication
    'PUB_PORT' return the current pub port of the IPC Backbone
    'SUB_PORT' return the current sub port of the IPC Backbone
"""
import zmq
from msgpack import loads

from pylive import live_plotter
import numpy as np
print('reached here')
## 1. SETUP
distanceToScreen = 57 # in cm
context = zmq.Context()
# open a req port to talk to pupil
addr = '127.0.0.1'  # remote ip or localhost
req_port = "50020"  # same as in the pupil remote gui
req = context.socket(zmq.REQ)
req.connect("tcp://{}:{}".format(addr, req_port))
print('reached here 2')
# ask for the sub port
req.send_string('SUB_PORT')
sub_port = req.recv_string()
print('reached here 3')
# open a sub port to listen to pupil
sub = context.socket(zmq.SUB)
sub.connect("tcp://{}:{}".format(addr, sub_port))

# set subscriptions to topics
# recv just pupil/gaze/notifications
#sub.setsockopt_string(zmq.SUBSCRIBE, 'pupil.')
sub.setsockopt_string(zmq.SUBSCRIBE, 'gaze.')
# sub.setsockopt_string(zmq.SUBSCRIBE, 'notify.')
# sub.setsockopt_string(zmq.SUBSCRIBE, 'logging.')
# or everything:
# sub.setsockopt_string(zmq.SUBSCRIBE, '')

## 2. Receive data

size = 120
t_vec = np.linspace(0,1,size+1)[0:-1]
x_vec = np.zeros(size)
line1 = []


while True:
    topic, payload = sub.recv_multipart()
    gaze_point_x = loads(payload)[b'gaze_point_3d'][0]

    gaze_point_x_ang = np.degrees(np.arctan(gaze_point_x / 10 / distanceToScreen)) # divide by 10 to get cm

    print("gaze in deg:", gaze_point_x_ang)


    x_vec[-1] = gaze_point_x_ang
    line1 = live_plotter(t_vec, x_vec, line1)
    x_vec = np.append(x_vec[1:], 0.0)


