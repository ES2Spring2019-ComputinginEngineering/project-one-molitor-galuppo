#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:22:44 2019

@author: victoriamolitor
"""

import matplotlib.pyplot as plt
import numpy as np
import math

#Initial Conditions
g = -9.81
L = 1 
pos = []
time = []
vel = []
acc = []

fin = open("Pendulum Data.csv")
for line in fin: 
    time.append(float(line.split(",")[0]))
    pos.append(float(line.split(",")[1]))

acc.append((g/L)*math.cos(pos[0]))
vel.append(acc[0]*(time[1]-time[0]))   
ipos = pos[0]

def update_system(pos,vel,acc,time1,time2): 
    dt = time2-time1
    currentAccel = (g/L)*math.cos(ipos-pos)
    currentVel = vel + currentAccel*dt
    return currentVel, currentAccel

i = 1
while i < len(time):
    currentVel, currentAccel = update_system(pos[i-1], vel[i-1], acc[i-1], time[i-1], time[i])
    vel.append(currentVel)
    acc.append(currentAccel)
    i += 1


plt.subplot(3,1,1)
plt.plot(time, pos, 'r-') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angle (radians)')
plt.title('Angle vs Time')
plt.xlim((0, 5)) # set x range from 0 to 5 
plt.grid()


plt.subplot(3,1,2)
plt.plot(time, vel, 'r-') 
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (rad/s)')
plt.title('Velocity vs Time')
plt.xlim((0, 5)) # set x range from 0 to 5
plt.grid()


plt.subplot(3,1,3)
plt.plot(time, acc, 'r-') 
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (rad/s^2)')
plt.title('Acceleration vs Time')
plt.xlim((0, 5)) # set x range from 0 to 5
plt.grid()
plt.tight_layout()
plt.show()