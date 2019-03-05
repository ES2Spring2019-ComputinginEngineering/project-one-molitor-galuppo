from microbit import *
import math
import random as r


angle_time = []
hourglass = Image("99999:09090:00900:09090:99999")

while True:
    display.scroll("Press A to Start!")
    sleep(1000)
    if button_a.was_pressed() == True:
        sleep(1500)
        start_time = running_time()
        filename = "Pendulum Data 2"  + ".csv"
        with open(filename, 'w') as file:
            updated_time = 0
            while updated_time < 5:
                display.show(hourglass)
                sleep(10)
                x = accelerometer.get_x()
                y = accelerometer.get_y()
                angle = math.atan2(y,x)
                finish_time = running_time()
                elapsed_time1 = (finish_time - start_time)/1000
                updated_time = elapsed_time1
                file.write(str(elapsed_time1) + ", " + str(angle) + "," + srt(x) + ", " + str(y) + "\n" )
        display.scroll("Done!")


with open('microbit.data', 'w') as my_file:
    for i in angle_time:
        my_file.write(str(i) + "\n")