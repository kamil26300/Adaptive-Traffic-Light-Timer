import RPi.GPIO as GPIO
import time

# Set the pin mode to BCM (Broadcom SOC channel) numbering
GPIO.setmode(GPIO.BCM)

# Set GPIO pin 4 as output
GPIO.setup(4, GPIO.OUT)

# Turn on GPIO pin 4
GPIO.output(4, GPIO.HIGH)

# Keep the pin on for 5 seconds (adjust as needed)
time.sleep(5)

# Turn off GPIO pin 4
GPIO.output(4, GPIO.LOW)

# Clean up the GPIO resources
GPIO.cleanup()