# this is code for operating the 14 UV lights on the Plant Wall
# project for EE400
# we want to connect all the UV lights to power and connect them
# to transistors which are then connected to PINS
# an array of switches and we only close the switches
# (and therefore connect to ground and enable current flow)
#  for 12 hours and then disconnect for 12 hours

import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin array for the UV
UV_pin_array = [18, 19, 20]

# Set the LED pin as an output
for i in UV_pin_array:
    GPIO.setup(UV_pin_array[i], GPIO.OUT)


try:
    while True:
        # Turn the UV on
        GPIO.output(UV_pin, GPIO.LOW)
        print("UV ON")
        
        # Wait for 12 hours
        time.sleep(12 * 60 * 60)  # 12 hours
        
        # Turn the UV off
        GPIO.output(UV_pin, GPIO.HIGH)
        print("UV OFF")
        
        # Wait for 12 hours
        time.sleep(12 * 60 * 60)  # 12 hours

except KeyboardInterrupt:
    # If the user interrupts the program, clean up GPIO settings
    GPIO.cleanup()