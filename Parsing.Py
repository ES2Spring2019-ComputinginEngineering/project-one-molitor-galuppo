#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:22:44 2019

@author: victoriamolitor
"""

#Parsing reads the text file of angle and time data collected by the microbit and plots the raw data of angle vs. time elapsed
#Import Statements
import matplotlib.pyplot as plt
import numpy as np
import math


#Initial Conditions
g = -9.81
L = 0.5 
pos = []
time = []
x_accel = []
y_accel = []

#Reads the raw data from the microbit and splits it into two lists - one list for the time elapsed and one for the angular position of the pendulum. 
fin = open("Pendulum Data 2.csv")
for line in fin: 
    time.append(float(line.split(",")[0]))
    pos.append(float(line.split(",")[1]))
    x_accel.append(float(line.split(",")[2]))
    y_accel.append(float(line.split(",")[3]))

#Plots the angular position of the pendulum over time 
plt.figure()
plt.plot(time, pos, 'r-') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angle (radians)')
plt.title('Angle vs Time')
plt.xlim((0, 5)) # set x range from 0 to 5 
plt.grid()
plt.show()