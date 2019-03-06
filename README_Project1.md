# Project 1: Micro:bit Pendulum
Alexa Galuppo and Victoria Molitor
March 6, 2019
The goal of this project was to simulate the motion of a pendulum by using accurate physics-based time-step based equations
to calculate pendulum position, velocity, and acceleration. A pendulum was constructed and files were written to take acceleration values in the x- and y- directions and calculated angular position. Noise from real world data was minimized and the period of the real-world pendulum was calculated. Finally, the simulated and real-world periods were compared for pendulums of different lengths. 

## Instructions
In order to obtain our results for Project 1: Micro:bit Pendulum, run the following files. 
First, open Simulation.py and change the variable 'L' to the desired pendulum length under the heading Initial Conditions 
Our experiments were based on pendulums of lengths 0.6 m, 0.48 m, 0.36 m, 0.24 m, and 0.12 m. 
Once the desired length has been entered, run the file in order to obtain graphs for position, velocity, 
and acceleration, in addition to the period of the simulated pendulum. 

Next, open Parsing.py and chance the file name in line 27 "Pendulum Data __ cm.csv" to reflect the desired length. 
Our GitHub includes the real-world data we collected at each pendulum length. 
Once the file name has been changed, run this file to obtain the unfiltered graph of angular position vs. time. 

Finally, open Analysis of Results.py and change the pendulum length in line 57 to reflect the length of 
pendulum being used. Run this file. If two peaks have been found by find_peaks near each other (as can be seen on the graph), 
the indexing of the calculations in lines 31-33 will have to be shifted in order to give an accurate estimate for the real-
world period of the pendulu. 

In order to collect new data, open Data Collection.py in Mu. Edit the file name in line 21 to reflect
the pendulum length and flash Data Collection onto a microbit. To begin data collection, press A on the microbit. 
Data will be collected for 5 seconds and written onto a file. To transfer this file from the micro:bit 
to the computer, reconnect the micro:bit to the computer and open the micro:bit files using Mu. 
