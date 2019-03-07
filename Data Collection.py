#Project 1: Micro:bit Pendulum
#Alexa Galuppo and Victoria Molitor
#March 6, 2019
#Step 3.2 - Create a micro:bit program to log sensor data to a text file

#Import Statements
from microbit import *
import math

#Initial Conditions
hourglass = Image("99999:09090:00900:09090:99999")

#Main Script
while True:
    display.scroll("Press A to Start!")
    sleep(1000)
    if button_a.was_pressed() == True:
        sleep(1500) #waits 1.5 seconds before beginning data collection to eliminate noisy data at the time of release.
        start_time = running_time() #sets the initial time elapsed to 0
        filename = "Pendulum Data 12 cm"  + ".csv"
        with open(filename, 'w') as file:
            updated_time = 0
            while updated_time < 5: #collects data for 5 seconds of pendulum motion.
                display.show(hourglass) #the microbit displays an hourglass while data is collected.
                sleep(10)
                x = accelerometer.get_x() #Collects x-acceleration data
                y = accelerometer.get_y() #Collects y-acceleration data
                angle = math.atan2(y,x)   #Uses trigonometry to calculate the angular position of the pendulum
                finish_time = running_time()
                elapsed_time1 = (finish_time - start_time)/1000
                updated_time = elapsed_time1
                file.write(str(elapsed_time1) + ", " + str(angle) + "," + str(x) + ", " + str(y) + "\n" ) #writes the x-acceleration, y-acceleration, time, and angle as a comma separated list to a text file
        display.scroll("Done!")