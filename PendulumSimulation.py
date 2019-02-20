from math import *
import numpy as np

#calculates the time in the period
def calc_PT():
    PT = 2*pi*(L/g)**(1/2)
    return PT

def update_system(time1, time2):
    dt = time2-time1
    NextAngle = (MaxAngle*sin((g/L)**(1/2))*dt) *180/pi                                                           #calculates the current angle to vertical of the pendulum based on the time elapsed
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
ang = [0]
vel = [0]
MaxHeight = L - L*cos(MaxAngle)


i = 1
while i < len(time):
    print_system(1,1,1)
    i += 1

calc_PT()

print(update_system(1,1.01))
print(MaxHeight)