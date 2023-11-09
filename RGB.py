import RPi.GPIO as GPIO
import time

# Setup the GPIO pins
red_pin = 17  # Replace with the actual GPIO pin numbers you're using
green_pin = 18
blue_pin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

# Function to set the color of the RGB LED
def set_rgb_color(red, green, blue):
    GPIO.output(red_pin, red)
    GPIO.output(green_pin, green)
    GPIO.output(blue_pin, blue)

try:
    while True:
        # Full intensity of each color, resulting in white light
        set_rgb_color(1, 1, 1)
        time.sleep(2)

        # Turn off the LED
        set_rgb_color(0, 0, 0)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()