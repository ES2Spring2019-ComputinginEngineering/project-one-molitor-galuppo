#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:22:44 2019

@author: victoriamolitor
"""

import matplotlib.pyplot as plt
import numpy as np
import math

def update_system(pos,vel,acc,time1,time2): #updates the system based on the current values of position, velocity, and acceleration
    dt = time2-time1
    velNext = vel + acc*dt
    accNext = (g/L)*math.cos(pos)
    return velNext, accNext
    
# Initial Conditions
L = 1                                                                                           
g = -9.81   
time = []
pos = []                                                             
vel = [0,0]                                     
acc = [0,(g/L)*math.cos((math.pi/2)-math.pi/6)] 
i = 1

fin = open("Pendulum Data.csv")

for line in fin: 
    time.append(float(line.split(",")[0]))
    pos.append(float(line.split(",")[1]))

while i < len(time):
    velNext, accNext = update_system(pos[i], vel[i], acc[i], time[i], time[i+1])
    vel.append(velNext)
    acc.append(accNext)
    i += 1
    
plt.subplot(3,1,1)
plt.plot(time, pos, 'r--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angle (radians)')
plt.title('Angle vs Time')
plt.xlim((0, 5.1)) # set x range 
plt.grid()


plt.subplot(3,1,2)
plt.plot(time, vel, 'r--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (rad/s)')
plt.title('Velocity vs Time')
plt.xlim((0, 5.1)) # set x range
plt.grid()


plt.subplot(3,1,3)
plt.plot(time, acc, 'r--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (rad/s^2)')
plt.title('Acceleration vs Time')
plt.xlim((0, 5.1)) # set x range 
plt.grid()
plt.tight_layout()
plt.show()