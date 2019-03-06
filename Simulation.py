#Project 1: Micro:bit Pendulum
#Alexa Galuppo and Victoria Molitor 
#March 6, 2019
#Step 1 - Simulation of Pendulum Motion

#Import Statements
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.signal as sig


#Function Definitions
def update_system(pos,vel,acc,time1,time2):         #updates the system based on the current values of position, velocity, and acceleration
    dt = time2-time1                                #calculates the time elapsed during this interval
    posNext = pos + vel*dt                          #calculates the next position based on the time elapsed and the current velocity
    velNext = vel + acc*dt                          #calculates the next velocity based on the current angular acceleration and time elapsed 
    accNext = (g/L)*math.cos(((math.pi)/2)-posNext) #calculates the next angular acceleration based on the starting position and the next position 
    return posNext, velNext, accNext

#Initial Conditions
L = 0.12                                             #Sets the length of the pendulum in meters                                                    
g = -9.81                                           #Force of gravity (m/s**2)
time = np.linspace(0,5,20000)                       #Creates a set of times during which the position, velocity, and acceleration of the pendulum will be calculated 
pos = [math.pi/6]                                   #Sets the initial position in radians. This list is appended in the while loop to update the new position 
vel = [0]                                           #Gives the initial velocity of 0. This list is appended in the while loop, where the velocity is updated based on acceleration and time. 
acc = [(g/L)*math.cos((math.pi/2)-math.pi/6)]       #Calculates the current angular acceleration of the pendulum, based on the starting angle. This list is appended in the while loop to add the new acceleration

#Updates the system while time is less than 5 seconds and calculates the next velocity, position, and acceleration of the pendulum based on the change in position. 
i = 1
while i < len(time):
    posNext, velNext, accNext = update_system(pos[i-1], vel[i-1], acc[i-1], time[i-1], time[i])
    vel.append(velNext)
    pos.append(posNext)
    acc.append(accNext)
    i += 1

#Finds the maximum positions of the pendulum and calculates the period based on the time elapsed between two of the maximums. 
position2 = np.array(pos)
time2 = np.array(time)
maxima, _ = sig.find_peaks(position2, prominence=.02)
print("The period time for a simulated pendulum of length",L, "meters is", round(time2[maxima[1]]-time2[maxima[0]], 3), " seconds")


#Plots the time elapsed (in seconds) and the anglular position of the pendulum (in radians)
plt.subplot(3,1,1)
plt.plot(time, pos, 'r-', time2[maxima], position2[maxima], 'ko') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angle (radians)')
plt.title('Angle vs Time')
plt.xlim((0, 5)) # set x range to -1 to 8
plt.grid()

#Plots the time elapsed (in seconds) and the velocity of the pendulum (in radians per second)
plt.subplot(3,1,2)
plt.plot(time, vel, 'r-') 
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (rad/s)')
plt.title('Velocity vs Time')
plt.xlim((0, 5)) # set x range to -1 to 8
plt.grid()

#Plots the time elapsed (in seconds) and the angular acceleration of the pendulum (in radians per second per second)
plt.subplot(3,1,3)
plt.plot(time, acc, 'r-') 
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (rad/s^2)')
plt.title('Acceleration vs Time')
plt.xlim((0, 5)) # set x range to -1 to 8
plt.grid()
plt.tight_layout()
plt.show()