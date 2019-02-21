from math import *
import numpy as np

#calculates the time in the period
def calc_PT():
    PT = 2*pi*(L/g)**(1/2)
    return PT

def update_system(ang,height,acc,vel,time1,time2):
    dt = time2-time1
    NextAngle = (ang*sin((g/L)**(1/2))*dt) *180/pi                                                           #calculates the current angle to vertical of the pendulum based on the time elapsed
    NextAccel = (-g/L) * sin(NextAngle)
    NextHeight = L - L*cos(NextAngle)
    NextVelocity = (2*g*L*(1-cos(NextAngle)))**(1/2)
    return NextAngle, NextAccel, NextHeight, NextVelocity

#prints calculated values as time progresses
def print_system(time, CurrentAngle, CurrentAccel):
    print("Time of Period:     ", calc_PT()) #does not change based on time, will remove from print statement
    #print("Current Angle (in degrees): ", CurrentAngle)
    print("\n")

#initial conditions and constants
L = float(input("What is the length in m of the pendulum?"))                                                          #inputs length
MaxAngleDegrees = float(input("At what angle in degrees from vertical is the pendulum released?"))                    #inputs max angle
MaxAngle = MaxAngleDegrees *pi/180#converts degrees to radians
g = 9.81                                                                                                              #force of gravity (m/s**2)
time = np.linspace(0,20,21)
ang = [90]
height = [1]
vel = [0]
acc = [0]
MaxHeight = L - L*cos(MaxAngle)


i = 1
while i < len(time):
    NextAngle, NextAccel, NextHeight, NextVelocity = update_system(ang[i-1], height[i-1], acc[i-1], vel[i-1], time[i-1], time[i])
    print("Time:", time[i], "Angle: ", NextAngle, "Accel: ", NextAccel, "Height: ", NextHeight, "Velocity: ", NextVelocity)
    i += 1
    ang.append(NextAngle)
    vel.append(NextVelocity)
    height.append(NextHeight)
    acc.append(NextAccel)
calc_PT()

print(MaxHeight)