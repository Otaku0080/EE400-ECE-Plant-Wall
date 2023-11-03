import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
moisture_sensor_pin = 14  # Replace with the actual GPIO pin for your moisture sensor
relay_pin = 18  # Replace with the actual GPIO pin for your relay module

# Set up GPIO pins
GPIO.setup(moisture_sensor_pin, GPIO.IN)
GPIO.setup(relay_pin, GPIO.OUT)

# Moisture threshold (adjust as needed)
moisture_threshold = 500

# Watering duration in seconds (adjust as needed)
watering_duration = 5

def read_moisture_level():
    return GPIO.input(moisture_sensor_pin)

def activate_relay():
    GPIO.output(relay_pin, GPIO.HIGH)

def deactivate_relay():
    GPIO.output(relay_pin, GPIO.LOW)

try:
    while True:
        moisture_level = read_moisture_level()

        if moisture_level < moisture_threshold:
            print("Soil moisture is below threshold. Watering plants...")
            activate_relay()
            time.sleep(watering_duration)
            deactivate_relay()
            print("Watering complete.")

        time.sleep(60)  # Check moisture level every minute

except KeyboardInterrupt:
    print("Script terminated by user.")
    deactivate_relay()
    GPIO.cleanup()

