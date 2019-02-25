import matplotlib.pyplot as plt
import numpy as np
import math

def calc_PT():
    PT = 2*math.pi*(L/g)**(1/2)
    return PT

def update_system(pos,vel,acc,time1,time2):
    dt = time2-time1
    posNext = pos + vel*dt
    velNext = vel + acc*dt
    accNext = (g/L)*math.cos(((math.pi)/2)-posNext)
    return posNext, velNext, accNext

    #NextAngle = (ang*math.sin((g/L)**(1/2))*dt) *180/math.pi                                                           #calculates the current angle to vertical of the pendulum based on the time elapsed
    #NextAccel = (g/L) * math.sin(NextAngle)
    #NextHeight = L - L*math.cos(NextAngle)
    #NextVelocity = (2*g*L*(1-math.cos(NextAngle)))**(1/2)
    #return NextAngle, NextAccel, NextHeight, NextVelocity

def print_system(time,pos,vel,acc):
    print("Time:         ", time)
    print("Position:     ", pos)
    print("Velocity:     ", vel)
    print("Acceleration: ", acc)
   

# initial conditions
L = 1                                                        #inputs length
MaxAngleDegrees = 90            #inputs max angle
MaxAngle = MaxAngleDegrees *math.pi/180#converts degrees to radians
g = -9.81                                                                                                              #force of gravity (m/s**2)
time = np.linspace(0,20,20000)
pos = [math.pi/6]
vel = [0]
acc = [(g/L)*math.cos((math.pi/2)-math.pi/6)]
MaxHeight = L - L*math.cos(MaxAngle)

i = 1
while i < len(time):
    posNext, velNext, accNext = update_system(pos[i-1], vel[i-1], acc[i-1], time[i-1], time[i])
    #print("Time: ", time[i], "Position: ", pos[i-1], "Velocity: ", vel[i-1], "Accel: ", acc[i-1])
    vel.append(velNext)
    pos.append(posNext)
    acc.append(accNext)
    i += 1
#calc_PT()


plt.subplot(3,1,1)
plt.plot(time, pos, 'r--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Position (m)')
plt.title('Position vs Time')
plt.xlim((0, 20)) # set x range to -1 to 8
plt.grid()


plt.subplot(3,1,2)
plt.plot(time, vel, 'r--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (rad/s)')
plt.title('Velocity vs Time')
plt.xlim((0, 20)) # set x range to -1 to 8
plt.grid()


plt.subplot(3,1,3)
plt.plot(time, acc, 'r--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (rad/s^2)')
plt.title('Acceleration vs Time')
plt.xlim((0, 20)) # set x range to -1 to 8
plt.grid()
plt.tight_layout()
plt.show()