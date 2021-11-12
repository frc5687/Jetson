#!/usr/bin/python
# -*- coding: utf-8 -*-
## License: Apache 2.0. See LICENSE file in root directory.
## Copyright(c) 2019 Intel Corporation. All Rights Reserved.

#####################################################
##           librealsense T265 rpy example         ##
#####################################################

# First import the library
import socket

import pyrealsense2 as rs
import math as m
import matplotlib.pyplot as plt
import socket as so
import tqdm
import os
import time



def send_msg(sock, msg):
    pass


# Configuring the plotter
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_title('Thingy')
# defining all 3 axes


# Default socket config
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096  # send 4096 bytes each time ste

# The ip address  or hostname of the server, the receiver
host = "123.467"
# The port
port = 5001
# The name of file we want to send,






# Declare RealSense pipeline, encapsulating the actual device and sensors
pipe = rs.pipeline()

# Build config object and request pose data
cfg = rs.config()
cfg.enable_stream(rs.stream.pose)

# Start streaming with requested config
pipe.start(cfg)

try:
    while True:
        # Wait for the next set of frames from the camera
        frames = pipe.wait_for_frames()

        # Fetch pose frame
        pose = frames.get_pose_frame()
        if pose:
            # Print some of the pose data to the terminal
            data = pose.get_pose_data()

            # Euler angles from pose quaternion
            # See also https://github.com/IntelRealSense/librealsense/issues/5178#issuecomment-549795232
            # and https://github.com/IntelRealSense/librealsense/issues/5178#issuecomment-550217609

            w = data.rotation.w
            x = -data.rotation.z
            y = data.rotation.x
            z = -data.rotation.y

            tx = data.translation.z

            pitch = -m.asin(2.0 * (x * z - w * y)) * 180.0 / m.pi
            roll = m.atan2(2.0 * (w * x + y * z), w * w - x * x - y * y + z * z) * 180.0 / m.pi
            yaw = m.atan2(2.0 * (w * z + x * y), w * w + x * x - y * y - z * z) * 180.0 / m.pi

            z = pitch
            x = roll
            y = yaw
            # Fetch pose frame
            pose = frames.get_pose_frame()
            print("Position: {}".format(data.translation))
            print("Velocity: {}".format(data.velocity))
            print("Acceleration: {}\n".format(data.acceleration))
            # print("Frame #{}".format(pose.frame_number))
            # print("RPY [deg]: Roll: {0:.7f}, Pitch: {1:.7f}, Yaw: {2:.7f}".format(roll, pitch, yaw))
            time.sleep(1)


finally:
    pipe.stop()



