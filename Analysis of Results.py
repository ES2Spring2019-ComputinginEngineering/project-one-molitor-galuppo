#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:13:57 2019

@author: alexagaluppo"""
#Project 1: Micro:bit Pendulum
#Alexa Galuppo and Victoria Molitor 
#March 6, 2019

#Step 4: Analysis of Results
#in order to read, analyze, and visualize data
    
import matplotlib.pyplot as plt
import math
import numpy as np
import scipy.signal as sig
import Parsing as data

#will need to bring in time and theta lists from parsing
time = np.array(data.time)
theta = np.array(data.pos)

theta2 = np.arctan2(sig.medfilt(data.x_accel,21), sig.medfilt(data.y_accel,21))
theta_filt = sig.medfilt(theta) 
    

#Calculate the period of the pendulum and minimizing false positives
maxima, _ = sig.find_peaks(theta2, prominence=.02)
    
period_1 = time[maxima[1]] - time[maxima[0]]
period_2 = time[maxima[2]] - time[maxima[1]]
avg_period = (period_1 + period_2)/2

#Plot X Acceleration vs Time
plt.figure()
plt.plot(time, data.x_accel, 'r-')
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (rad/s^2)')
plt.title('X Acceleration vs Time')
plt.grid()
plt.show()

#Plot Y Acceleration vs Time
plt.figure()
plt.plot(time, data.y_accel, 'r-')
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (rad/s^2)')
plt.title('Y Acceleration vs Time')
plt.grid()
plt.show()


#Calculate theta vs time

#Prints the average period length underneath the angular position vs time graph
print("The average period length for a pendulum of length 48 cm is", round(avg_period,3), "seconds")

#Plot theta vs time
plt.subplot(2,1,2)
plt.plot(time, theta2, 'r-', time[maxima], theta2[maxima], 'ko') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angular position (rad)')
plt.title('Angular Position vs Time')
plt.grid()

plt.tight_layout()
plt.show()

