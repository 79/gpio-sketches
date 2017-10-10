#!/usr/bin/python

#= Poor man's blink...
# Test that communication with pi is working!

import RPi.GPIO as GPIO
from subprocess import Popen
from time import sleep
state = GPIO.LOW

print("Here we go! Press CTRL+C to exit")
try:
    while True:
        state = GPIO.HIGH if state == GPIO.LOW else GPIO.LOW
        cmd = "echo {0} > /sys/class/leds/led0/brightness".format(state)
        Popen(cmd, shell=True).wait()
        sleep(1)
except KeyboardInterrupt: # CTRL+C
    GPIO.cleanup()

