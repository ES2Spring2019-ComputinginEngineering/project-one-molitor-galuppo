from math import *

#calculates the time in the period
def calc_PT():
    PT = 2*pi*(L/g)**(1/2)
    return PT

#calculates the current angle to vertical of the pendulum based on the time elapsed
def calc_angle():
    CurrentAngle = (MaxAngle*sin((g/L)**(1/2))*t) *180/pi
    return CurrentAngle

#def update_system:
    #return

#prints calculated values as time progresses
def print_system():
    print("Time of Period:     ", calc_PT()) #does not change based on time, will remove from print statement
    print("Current Angle (in degrees): ", calc_angle())
    print("\n")

#initial conditions and constants
L = float(input("What is the length in m of the pendulum?"))                                                          #inputs length
MaxAngleDegrees = float(input("At what angle in degrees from vertical is the pendulum released?"))                    #inputs max angle
MaxAngle = MaxAngleDegrees *pi/180                                                                                    #converts degrees to radians
t = float(input("How many seconds have passed?") )                                                                    #inputs time, will change to loop
g = 9.81                                                                                                              #force of gravity (m/s**2)

#while True:

calc_PT()

print_system ()