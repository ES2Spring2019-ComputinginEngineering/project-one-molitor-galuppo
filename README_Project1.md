# Project 1: Micro:bit Pendulum

Alexa Galuppo and Victoria Molitor
March 6, 2019

In this project, Python code was used to plot and analyze the angular movement of a pendulum both from simulated data and from
actual live data obtained using a micro:bit’s sensor. The simulated data is created at a given length using functions that 
calculate the expected angular acceleration, angular velocity, and angular position over a time interval. Graphs of each of 
these data sets are then plotted over their respective times and the theoretical period of the pendulum is calculated. As for 
the real-world data, a physical Lego pendulum attached to a micro:bit was used. The micro:bit was programmed to collect 
acceleration data in two-dimensions over time which is then converted into the angular position over time. This data set it 
then filtered to reduce the extraneous data points and plotted. Then, the period of the pendulum is calculated. Finally, in 
order to explore the differences between using simulated data and real-world data, the graphs and periods from these two 
sources at various pendulum lengths are compared below.

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
