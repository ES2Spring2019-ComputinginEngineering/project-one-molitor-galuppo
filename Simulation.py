import matplotlib.pyplot as plt
import numpy as np
import math

def update_system(pos,vel,acc,time1,time2): #updates the system based on the current values of position, velocity, and acceleration
    dt = time2-time1
    posNext = pos + vel*dt
    velNext = vel + acc*dt
    accNext = (g/L)*math.cos(((math.pi)/2)-posNext)
    return posNext, velNext, accNext

# Initial Conditions
L = 1                                         #Sets the length of the pendulum in meters                                                    
g = -9.81                                     #Force of gravity (m/s**2)
time = np.linspace(0,20,20000)                #Creates a set of times during which the position, velocity, and acceleration of the pendulum will be calculated 
pos = [math.pi/6]                             #Sets the initial position in radians. This list is appended in the while loop to update the new position 
vel = [0]                                     #Gives the initial velocity of 0. This list is appended in the while loop, where the velocity is updated based on acceleration and time. 
acc = [(g/L)*math.cos((math.pi/2)-math.pi/6)] #Calculates the current angular acceleration of the pendulum, based on the starting angle. This list is appended in the while loop to add the new acceleration

i = 1
while i < len(time):
    posNext, velNext, accNext = update_system(pos[i-1], vel[i-1], acc[i-1], time[i-1], time[i])
    vel.append(velNext)
    pos.append(posNext)
    acc.append(accNext)
    i += 1

#Plots the time elapsed (in seconds) and the anglular position of the pendulum (in radians)
plt.subplot(3,1,1)
plt.plot(time, pos, 'r--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angle (radians)')
plt.title('Angle vs Time')
plt.xlim((0, 20)) # set x range to -1 to 8
plt.grid()

#Plots the time elapsed (in seconds) and the velocity of the pendulum (in radians per second)
plt.subplot(3,1,2)
plt.plot(time, vel, 'r--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (rad/s)')
plt.title('Velocity vs Time')
plt.xlim((0, 20)) # set x range to -1 to 8
plt.grid()

#Plots the time elapsed (in seconds) and the angular acceleration of the pendulum (in radians per second per second)
plt.subplot(3,1,3)
plt.plot(time, acc, 'r--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (rad/s^2)')
plt.title('Acceleration vs Time')
plt.xlim((0, 20)) # set x range to -1 to 8
plt.grid()
plt.tight_layout()
plt.show()